
def get_example_response_seo_generation_prompt():
   example_response = {
                        "SEO_Title": "[Título SEO del producto utilizando una técnica de keywords long tail basada en la descripción de la imagen y los top_title]",

                        "Meta_Description": "[Metadescripción atractiva y persuasiva que resume las características clave del producto]",

                        "H1_Heading": "[Encabezado H1 claro, relevante y que contenga la palabra clave principal del producto]",

                        "Product_Description": "[Descripción detallada y exhaustiva del producto, incluyendo sus características, beneficios y usos]",

                        "Keywords": [
                            "[palabra clave 1]",
                            "[palabra clave 2]",
                            "[palabra clave 3]",
                            "[palabra clave 4]",
                            "[palabra clave 5]"
                        ],

                        "JSON-LD_Marker": {
                            "@context": "http://schema.org",

                            "@type": "Product",

                            "name": "[Nombre del producto]",

                            "description": "[Descripción breve del producto]",

                            "brand": {
                            "@type": "Thing",
                            "name": "[Marca del producto]"
                            },

                            "offers": {
                            "@type": "Offer",
                            "priceCurrency": "EU",
                            "price": "[Precio del producto]",
                            "itemCondition": "http://schema.org/NewCondition",
                            "availability": "http://schema.org/InStock"
                            },

                            "category": "[Categoría del producto]",

                            "image": "[URL de la imagen del producto]",

                            "sku": "[SKU del producto]"
                        }
                        }
   return example_response

def get_example_response_evaluation_seo_generation_prompt():
    example_response = {
                        "evaluation": {
                            "SEO_Title": 4,
                            "use_of_keywords": 5,
                            "Meta_description": 4,
                            "H1_Heading": 5,
                            "Product_Description": 4,
                            "Keywords": 5,
                            "JSON_LD_Schema": 4,
                            "SKU": 5
                        },
                        "comments": {
                            "SEO_Title": "El título SEO es mayormente relevante y sigue las mejores prácticas de SEO, pero podría ser un poco más atractivo.",
                            "use_of_keywords": "Todas las palabras clave se utilizan de manera óptima y efectiva en el contenido.",
                            "Meta_description": "La meta descripción es mayormente relevante, concisa y atractiva, pero puede mejorarse ligeramente para ser más persuasiva.",
                            "H1_Heading": "La etiqueta H1 es completamente relevante y sigue perfectamente las mejores prácticas de SEO.",
                            "Product_Description": "La descripción del producto es mayormente precisa, relevante y detallada, aunque podría incluir más detalles específicos del producto.",
                            "Keywords": "Todas las palabras clave seleccionadas son altamente adecuadas y relevantes para el producto.",
                            "JSON_LD_Schema": "El JSON LD Schema está mayormente bien estructurado y contiene la mayoría de la información relevante, pero hay espacio para una mejor organización.",
                            "SKU": "El SKU es completamente claro, preciso y altamente relevante para el producto."
                        }
    }
    return example_response
    
def get_example_response_evaluation_read_images_prompt():
    example_response = {
                        "evaluation": {
                            "Color_Accuracy": 4,
                            "Object_Accuracy": 5,
                            "Composition_Accuracy": 4,
                            "Overall_Coherence": 5
                        },
                        "comments": {
                            "Color_Accuracy": "La mayoría de los colores mencionados en la descripción coinciden con los colores presentes en la imagen, aunque algunos tonos menores no se mencionaron.",
                            "Object_Accuracy": "Todos los objetos mencionados en la descripción coinciden perfectamente con los objetos presentes en la imagen.",
                            "Composition_Accuracy": "La mayoría de las disposiciones o ubicaciones mencionadas coinciden con la imagen, aunque hay pequeñas discrepancias en la ubicación exacta de algunos objetos.",
                            "Overall_Coherence": "La descripción es completamente coherente y tiene una relación perfecta con la imagen, ofreciendo una visión clara y precisa de la misma."
                        }
                        }

    return example_response
    