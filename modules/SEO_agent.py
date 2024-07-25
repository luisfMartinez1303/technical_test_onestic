import os
import base64
import requests
import json

from openai import OpenAI
from dotenv import load_dotenv 
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from langchain import hub
from pathlib import Path
from modules.prompt import (get_example_response_seo_generation_prompt, 
                    get_example_response_evaluation_seo_generation_prompt,
                    get_example_response_evaluation_read_images_prompt)
                    
current_dir = Path(__file__).resolve().parent
env_path = current_dir / '.env'
load_dotenv(dotenv_path=env_path)

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "onestic"


class SEO_agent:
    """
    SEO_agent class to handle SEO specification sheet generation, 
    URL to base64 image conversion, and image reading for SEO purposes.

    Attributes:
        openai_api_key (str): API key for OpenAI.
        serpapi_api_key (str): API key for SerpAPI.
        openai_client (OpenAI): OpenAI client wrapped in a wrap_openai function.
    """

    def __init__(self):
        """
        Initializes an instance of the SEO_agent class. Retrieves API keys 
        from environment variables and sets up the OpenAI client.
        """
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.serpapi_api_key = os.getenv("SERPAPI_API_KEY")
        self.openai_client = wrap_openai(OpenAI(api_key=self.openai_api_key))

    @traceable
    def generate_seo_spec_sheet(self, product_data: dict) -> dict:
        """
        Generates an SEO specification sheet based on product data.

        Args:
            product_data (dict): Dictionary containing product data.

        Returns:
            dict: Generated response in JSON format with the SEO specification sheet.
        """
        prompt = hub.pull(os.getenv("ID_GENERATE_SEO_SPEC_SHEET_PROMPT"))
        prompt = prompt.messages[0].prompt.template.format(
            product_data=product_data, 
            example_response=get_example_response_seo_generation_prompt()
        )

        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[{"role": "system", "content": prompt}],
        )
        response_json = response.choices[0].message.content
        
        return response_json

    def url_to_base64(self, image_url: str) -> str:
        """
        Converts an image URL to a base64 string.

        Args:
            image_url (str): URL of the image to be converted.

        Returns:
            str: Base64 string of the image or an error message if the download fails.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9'
        }
    
        response = requests.get(image_url, headers=headers)

        try:
            image_data = response.content
            base64_image = base64.b64encode(image_data).decode('utf-8')
            return base64_image
        except:
            return f"Error {response.status_code}: Unable to download the image"

    def read_images(self, image_url: str) -> str:
        """
        Reads the content of an image from a URL using OpenAI's API.

        Args:
            image_url (str): URL of the image to be read.

        Returns:
            str: Content extracted from the image or an error message if the download fails.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        base64_image = self.url_to_base64(str(image_url))
        prompt = hub.pull(os.getenv("ID_READ_IMAGES_PROMPT"))
        prompt = prompt.messages[0].prompt.template
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "messages": [
                {
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ]
                },
            ],
            "model": "gpt-4o-mini",
        }   
        
        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response = response.json()['choices'][0]['message']['content']
            return response
        except:
            return f"Error {response.status_code}: Unable to download the image"

    def evaluation(self, output: dict, eval: bool = True, url: str = "", json_data: dict = None) -> dict:
        """
        Evaluates the generated SEO specification sheet or image description.

        Args:
            output (dict): The generated output to be evaluated.
            eval (bool): Indicates if the evaluation is for the SEO specification sheet or image description.
            url (str): URL of the image to be read if eval is False.
            json_data (dict): JSON data to be used in the evaluation if eval is True.

        Returns:
            dict: Evaluation response in JSON format.
        """
        if eval:
            prompt = hub.pull("evaluation_generate_seo_spec_sheet_prompt")
            prompt = prompt.messages[0].prompt.template.format(
                json_data=json_data, 
                seo_technical_sheet=output, 
                json_example=get_example_response_evaluation_seo_generation_prompt()
            )
        else:
            description = self.read_images(url)
            prompt = hub.pull("evaluation_read_images")
            prompt = prompt.messages[0].prompt.template.format(
                description=description, 
                json_example=get_example_response_evaluation_read_images_prompt()
            )
        
        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[{"role": "system", "content": prompt}],
        )
        response_json = response.choices[0].message.content
        
        return response_json
