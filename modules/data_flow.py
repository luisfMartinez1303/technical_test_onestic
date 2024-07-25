import pandas as pd
import os
import json

from modules.SEO_agent import SEO_agent
from serpapi import GoogleSearch
from dotenv import load_dotenv 
from pprint import pprint
from langsmith.evaluation import evaluate
from langsmith.schemas import Example, Run
from pathlib import Path

current_dir = Path(__file__).resolve().parent
env_path = current_dir / '.env'
resource_dir = current_dir.parent / 'resources'
result_dir = current_dir.parent / 'result'
load_dotenv(dotenv_path=env_path)

def process_row(json_str: str) -> pd.DataFrame:
    """
    Processes a JSON string to convert it into a pandas DataFrame.
    Extracts and normalizes the JSON data, including a specific 'JSON-LD_Marker' field.

    Args:
        json_str (str): JSON-formatted string to be processed.

    Returns:
        pd.DataFrame: DataFrame containing the normalized JSON data with an added 'JSON-LD_Marker' column.
    """
    try:
        json_to_dict = json.loads(json_str)
        ld_marker = json.dumps(json_to_dict.pop('JSON-LD_Marker', {}))
        df = pd.json_normalize(json_to_dict)
        df['JSON-LD_Marker'] = ld_marker
        return df
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return pd.DataFrame()  

def get_top_titles(name: str) -> str:
    """
    Retrieves the top titles from a Google search for a given product name.

    Args:
        name (str): Product name to search for.

    Returns:
        str: Comma-separated string of top titles and their positions or an empty list if an error occurs.
    """
    search = GoogleSearch({
        "q": name,
        "tbm": "shop",  
        "tbs": "p_ord:rv",
        "num": 9,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "hl": "es",
        "gl": "es",
        "location": "Spain"
    })
    data = search.get_dict()
    try:
        top_title = [f"{shopping_result['position']} - {shopping_result['title']}" for shopping_result in data['shopping_results']]
        top_title = ", ".join(top_title)
        return top_title
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def extract_data_from_csv(seo_agent: SEO_agent) -> pd.DataFrame:
    """
    Extracts and processes data from CSV files, merges product data with images, and applies SEO-related functions.

    Args:
        seo_agent (SEO_agent): Instance of the SEO_agent class used for processing.

    Returns:
        pd.DataFrame: DataFrame containing merged product data, top titles, and image descriptions.
    """
    data_file_path = resource_dir / "product-data.csv"
    images_file_path = resource_dir / "product-images.csv"
    data = pd.read_csv(data_file_path)
    images = pd.read_csv(images_file_path)

    images = images[images['is_main_image']]
    images = images[['sku', 'url']]

    df = pd.merge(data, images, on='sku').drop('channel', axis=1)
    df['top_title'] = df['name'].apply(get_top_titles)
    df['image_description'] = df['url'].apply(seo_agent.read_images)

    return df

def generate_seo_technical_sheet() -> None:
    """
    Generates an SEO technical sheet by processing data from CSV files, generating SEO specifications, 
    and saving the results to a CSV file.

    Returns:
        None
    """
    seo_agent = SEO_agent()
    df = extract_data_from_csv(seo_agent)
    df['json_response'] = df.apply(seo_agent.generate_seo_spec_sheet, axis=1)

    df_list = df['json_response'].apply(process_row)
    df_list = df_list.tolist()
    df_final = pd.concat(df_list, ignore_index=True)

    df = df.loc[:, ['sku', 'url']]
    df = pd.concat([df, df_final], axis=1)

    df.to_csv(result_dir / 'seo_technical_sheet.csv')
    
    return print("Ejecución exitosa, el CSV lo encontrarás en la carpeta 'result'")

