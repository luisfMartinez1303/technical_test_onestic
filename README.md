# Sistema para enriquecer un catálogo de productos de una tienda online con inteligencia artificial

Este proyecto implementa un sistema basado en modelos de lenguaje grandes (LLM) para generar una ficha técnica SEO.

## Tabla de Contenidos


- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Memoria de la Prueba Técnica](#memoria-de-la-prueba-técnica)
- [Investigación Inicial](#investigación-inicial)
- [Variables Determinadas](#variables-determinadas)
- [Planificación de la Solución](#planificación-de-la-solución)
- [Desarrollo de la Solución](#desarrollo-de-la-solución)
- [Video de Ejecución](#video-de-ejecución)


## Descripción

Este sistema procesa dos archivos CSV: uno que contiene datos detallados de los productos y otro con URLs de imágenes asociadas. A partir de esta información, un modelo de inteligencia artificial generativa crea fichas técnicas enriquecidas y optimizadas para SEO. El objetivo es mejorar el posicionamiento de los productos en Internet, asegurando una mayor visibilidad y atractivo en los resultados de búsqueda.

## Instalación

Sigue estos pasos para instalar el proyecto:

```bash
# Clonar el repositorio
git clone https://github.com/luisfMartinez1303/technical_test_onestic.git

# Entrar al directorio del proyecto
cd tu-repositorio

# Crear un entorno virtual (opcional pero recomendado)
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

# Instalar dependencias
pip install -r requirements.txt

```

## Uso

Para ejecutar el script principal `main.py`, sigue estos pasos:

1. **Actualiza el archivo `.env`**:
   - Abre el archivo `.env` que ya existe en el directorio raíz del proyecto.
   - Asegúrate de que contiene las siguientes líneas, reemplazando `YOUR_OPENAI_API_KEY`, `YOUR_SERPAPI_API_KEY` y `YOUR_LANGCHAIN_API_KEY` con tus claves API correspondientes:

     ```dotenv
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
     LANGCHAIN_API_KEY=YOUR_LANGCHAIN_API_KEY
     ```
     - **Nota**: El resto de las variables que aparecen en el archivo `.env` se utilizan solo para fines de evaluación y no es necesario completarlas para el funcionamiento del script.

2. **Ejecuta el script**:
   - Una vez que hayas actualizado el archivo `.env`, ejecuta el script principal con el siguiente comando:

     ```bash
     python3 main.py
     ```
     El script leerá automáticamente las claves API desde el archivo `.env` y procederá con la ejecución.
     
3. **Resultado**
   - La ficha técnica enriquecida la encontraras en formato csv en la carpeta `result` en el archivo `seo_technical_sheet.csv`.

   
### Memoria de la Prueba Técnica

## Investigación Inicial

Para abordar esta prueba técnica, mi primer objetivo fue comprender claramente los requisitos. Comencé investigando para profundizar en conceptos que, aunque no eran completamente nuevos para mí, necesitaba entender con mayor profundidad. Me enfoqué en temas clave como SEO, fichas de productos y eCommerce, y exploré cómo estos conceptos se interrelacionan y afectan el desarrollo de la solución.

#### Fuentes Consultadas

- **ChatGPT:** Utilizado para obtener una comprensión inicial y realizar consultas específicas sobre términos desconocidos.
- **Google:** Para buscar información adicional y contrastar lo obtenido.
- **Sitios Web Especializados:**
  - **Soy Isabel Romero:** [Información sobre estrategias SEO](https://www.soyisabelromero.com/tips-de-seo-para-fichas-de-producto/)
  - **Moodlemetrics:** [Consejos SEO para fichas de producto](https://muddlemetrics.com/blog/seo-para-fichas-de-producto/)
  - **Velfix:** [Cómo optimizar de Fichas de Producto: SEO y Usabilidad](https://www.velfix.es/como-optimizar-fichas-de-producto-seo-y-usabilidad/)

#### Algunas estadísticas
- **Meta descripciones y H1:** El 99% de los sitios posicionados en el top 10 han usado meta descripciones en sus estrategias de optimización, y el 80% han usado etiquetas H1 en su contenido. [semrush](https://es.semrush.com/blog/estadisticas-seo/)
- **long tail keywords**:  De las consultas dentro de los resultados de búsqueda el 69,7% se conforma de cuatro palabras o más, es decir, de long tail keywords.[NichoSEO](https://nichoseo.com/estadisticas-seo/)
- **Importancia del posicionamiento**: De los usuarios de Google el 99,22 % selecciona solo los resultados de la primera página dejando afuera el resto de las páginas de la SERP.[NichoSEO](https://nichoseo.com/estadisticas-seo/)

Una vez consultadas las fuentes de información, entendí que uno de los principales retos sería definir los campos que el modelo debería enriquecer. Encontré que se mencionaban muchas variables para una ficha técnica, pero no todas eran adecuadas con los datos proporcionados en los recursos. Observé que había conceptos comunes sobre los tipos de variables que se deben considerar para crear una ficha técnica efectiva. Entre las variables más frecuentes en los documentos que leí están las palabras clave, los títulos del producto, la descripción del producto, las imágenes proporcionadas, una metadescripción y los datos estructurados en Schema Markup. Esta última parte me resultó especialmente interesante, ya que mejora la visibilidad en los resultados de búsqueda.

Dentro de la investigación también logré determinar y me llamó mucho la atención los Keywords Long Tail. Estas son palabras clave de cola larga, más específicas, que suelen tener menos competencia que las palabras clave más generales y populares. Esto facilita un ranking más alto en los resultados de búsquedas. Este aspecto me pareció particularmente relevante para la optimización de títulos y descripciones de productos.

## Variables Determinadas

Una vez completada la investigación y teniendo en cuenta las estadísticas encontradas, decidí determinar las variables que se incluirían en el sistema automatizado. Las variables seleccionadas son:

- **SKU:** Referencia del producto, esencial para la identificación.
- **URL de la Imagen:** Enlace a la imagen del producto.
- **SEO Title:** Título optimizado para motores de búsqueda.
- **Meta Descripción:** Breve descripción optimizada para SEO.
- **H1 Heading:** Etiqueta H1, importante para el posicionamiento del producto.
- **Product Description:** Descripción detallada del producto.
- **Keywords:** Palabras clave relevantes.
- **JSON Array Marker:** Sistema de datos estructurados que ayuda a que un producto se destaque en los resultados de búsqueda a través de fragmentos enriquecidos.

## Planificación de la Solución

Una vez determinadas las variables a utilizar, comencé a planear la solución. Decidí implementar la solución en Python, creando diferentes scripts que automatizarían todo el proceso. Las tecnologías seleccionadas para el desarrollo son:

- **Python:** Lenguaje de programación principal para la automatización.
- **Pandas:** Librería para el manejo y procesamiento de datos.
- **OpenAI:** Para los modelos de lenguaje.
- **LangSmith:** Para el seguimiento y evaluación de los prompts.

## Desarrollo de la Solución

### Generación de Títulos Optimizados

Al considerar la importancia del título, pensé que sería útil realizar una búsqueda del nombre del producto presente en los datos para ver los principales resultados en Google o Google Shopping. La idea sería obtener los títulos de los primeros 10 productos en los resultados y luego pasárselos al modelo para que utilizando la técnica de títulos de cola larga, el modelo pudiea generar un título relevante y optimizado.

Para implementar esta función, consideré inicialmente usar **BeautifulSoup**, una librería con la que había trabajado anteriormente. Sin embargo, al investigar un poco más, encontré un api reciente llamada [SerpApi](https://serpapi.com/) que resultó ser muy fácil de implementar. Con un pequeño código logré obtener los resultados deseados, lo que me permitió extraer los títulos de los productos de manera eficiente.

Comencé a desarrollar mis funciones en un Jupyter Notebook, una herramienta que facilita la prueba de fragmentos de código sin necesidad de tener el script completo. Esto me permite optimizar mi trabajo al experimentar y ajustar pequeñas secciones de código de manera eficiente.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/test_serpapi.png)

### Lectura de Imágenes

Después de desarrollar la función de generación de títulos, decidí implementar la lectura de las imágenes. Comencé explorando los archivos CSV `product-data` y `product-images`, y observé que el CSV de imágenes contiene 73 filas, mientras que el de datos solo tiene 14. Al inspeccionar más a fondo, noté que para cada SKU había diferentes URLs de imagen y una variable llamada `is_main_image` con un valor booleano. El valor True indica la imagen principal, mientras que los demás valores representan diferentes perspectivas de la misma imagen.

Decidí filtrar el CSV de las imágenes, quedándome solo con las filas donde `is_main_image` es `True`. De este modo, obtuve únicamente la URL de la imagen principal de cada producto, lo cual es crucial para optimizar el tiempo y los recursos, ya que procesar todas las URLs sería demasiado costoso y lento. Con la imagen principal, puedo generar una descripción adecuada para el campo correspondiente dentro de la ficha del producto.

Las primeras pruebas las hice a través del modelo GPT-4 Mini de OpenAI, uno de los últimos modelos que da muy buenos resultados y maneja un costo bastante bajo, lo cual lo hace muy óptimo para producción. Aquí me enfrenté a un primer problema: OpenAI comenzó a generar un error con las URLs de las imágenes `message: ‘Invalid image.’, type: ‘invalid_request_error’`. Al parecer, este error es muy común con estas solicitudes. Investigando un poco, descubrí que las páginas donde están alojadas estas URLs tienen algún tipo de bloqueo sobre IP asociadas con OpenAI, o a veces es simplemente suerte, este problema aún se discute en la actualidad. [Foro de discusión](https://community.openai.com/t/invalid-image-error-in-gpt-4-vision/505843/23)

Después de varias pruebas, decidí implementar una opción alternativa que tiene OpenAI: convertir las imágenes en un formato base64. De esta forma, logré que el modelo pudiera leer las imágenes sin ningún tipo de error.

### Generación de la ficha técnica optimizada

Para esta parte, el mayor desafío fue encontrar el mejor prompt (lo explicaré detalladamente más adelante) que garantizara una respuesta coherente y consistente. Para facilitar el posprocesamiento de la respuesta, decidí implementar el parámetro `"type": "json_object"`, que garantiza una respuesta en este formato y permite un mejor manejo de la información.

### Creación de la Clase SEO Agent

Para mantener una estructura más organizada, decidí crear una clase llamada SEO_agent, que cuenta con cuatro métodos, de los cuales dos son principales. Esta clase se encarga de generar la información optimizada para cada producto.

- **Método 1: generate_seo_spec_sheet:** Este método se encarga de generar la ficha técnica completa del producto. Recibe como parámetro cada fila del dataframe preprocesado con los datos disponibles, el top 10 de títulos encontrados en la búsqueda de Google Shopping y la descripción de la imágen.
- **Método 2: read_images:** Este método utiliza el modelo de OpenAI para leer y describir las imágenes del producto.
- **Método 3: url_to_base64:** Este es un método interno que convierte las URLs de las imágenes a formato base64, permitiendo que el modelo de OpenAI pueda procesarlas sin errores.
- **Método 4: evaluation:** Este método ayudará en la evaluación para determinar los prompts que generan las mejores respuestas.

### Flujo de Procesamiento de Datos

En un segundo script, decidí implementar el proceso principal donde se desarrolla todo el procesamiento de los datos hasta obtener la respuesta final. El proceso de datos consiste en una serie de pasos diseñados para transformar los datos iniciales en fichas técnicas optimizadas y organizadas. A continuación, se describe cada uno de los pasos involucrados:

1. **Cargar los CSVs:** Lo primero en este proceso es cargar los dos CSVs (datos del producto e imágenes) en Pandas.
2. **Filtrar el CSV de Imágenes:** Después de filtrar el CSV de imágenes según el campo **IsMainImage**, decidí quedarme solo con las columnas **SKU** y **URL**, ya que los demás datos eran irrelevantes para el proceso.
3. **Unir los CSVs:** Realicé un merge o unión entre el CSV de datos del producto y el CSV de imágenes, combinándolos a través del campo **SKU**. Esto me permitió obtener un CSV unificado con todos los datos relevantes.
4. **Agregar Columnas para el Modelo:**
   - **Top Titles:** Añadí una nueva columna llamada **Top Titles** que invoca la función que busca los 10 títulos más relevantes de la búsqueda en Google utilizando el nombre del producto presente en el CSV.
   - **Image Description:** Agregué una nueva columna llamada **Image Description**, que llama a la función de lectura de imágenes y almacena la descripción de la imagen en este nuevo campo.

  Esta es una muestra de la información procesada que finalmente llega al modelo para crear la ficha tecnica:
  
![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/df1.png)


5. **Crear la Columna JSON Response:** Esta columna llama al método encargado de generar la ficha técnica del producto en formato JSON. Este método utiliza los datos de la tabla anterior para generar una respuesta estructurada con el esquema especificado.
6. **Convertir JSON a DataFrame:** El JSON generado se convierte en un DataFrame utilizando Pandas. Esto permite organizar las fichas técnicas con los campos definitivos según los requisitos especificados.
7. **Concatenar Ejecuciones:** Utilizando funciones de Pandas, se concatena el JSON con las diferentes ejecuciones realizadas, asegurando que todas las fichas técnicas estén integradas en un único DataFrame.
8. **Guardar Resultados:** Finalmente, se guarda el DataFrame resultante como un archivo CSV para su presentación. También se muestra por pantalla en formato DataFrame para una visualización inmediata.


### Definición y evaluación de los Prompts 

He dejado esta parte para el final porque considero que es una de las más importantes. Redactar y evaluar prompts de manera efectiva puede ser determinante para lograr un buen resultado que se alinee con todo el desarrollo realizado hasta ahora.

Todo este módulo se desarrolló en un tercer script, utilizando LangSmith, una plataforma diseñada específicamente para facilitar la depuración, prueba, evaluación y monitoreo de aplicaciones impulsadas por LLMs. En este script, se crearon diferentes funciones que permiten intervenir en las ejecuciones de los modelos para rastrear y evaluar las respuestas. Además, podemos agregar puntuaciones con los evaluadores, que nos permiten luego poder tomar desiciones informadas.
El proceso consistió en crear diferentes prompts, en este caso para leer imágenes y para generar la ficha técnica. Una vez desarrollados estos prompts, creé dos bases de datos: una para las imágenes y otra para las fichas técnicas. Estas bases de datos son diccionarios clave-valor, donde, en el caso de las imágenes, la clave es la URL y una descripción hecha con un prompt básico, y en el de SEO, un JSON correspondiente a la información de cada ficha técnica introducida al modelo, así como un JSON resultante creado sintéticamente.

Para la estructura de los prompts utilicé la técnica de "few-shot" o "one-shot", que consiste en proporcionar un ejemplo para guiar la salida del modelo. Esta técnica es particularmente efectiva y asegura una respuesta consistente, al menos en cuanto a formato y estructura. Para asegurar que las respuestas sean siempre en formato JSON, se especificó el parámetro `response_format={ "type": "json_object" }` dentro de la solicitud a OpenAI.

En los siguientes enlaces, se puede revisar la estructura de cada prompt. Cada commit dentro del prompt representa las diferentes opciones que fueron evaluadas:
  
  **Enriquecer ficha técnica**:
  [seo_generation_prompt](https://smith.langchain.com/hub/luis-fernando-martinez/seo_generation_prompt)
  
  El formato de respuesta que debe seguir el modelo fue proporcionado a través del script, tal como lo requiere LangSmith, y se encuentra en el archivo de prompts.py dentro del proyecto.

   **Leer imagenes**:
  [read_images_prompt](https://smith.langchain.com/hub/luis-fernando-martinez/read_images_prompt)
  
#### Base de datos de descripción de imagenes
![images2](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/bd_images.png)

#### Base de datos de ficha SEO
![images2](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/bd_seo.png)

A continuación tambien se encuentran los links de los evaluadores, tanto en la descripción de las imágenes como en la creación de la ficha técnica. Estos prompts asignan un puntaje basado en diversos aspectos de las respuestas.
 
 **Evaluador de ficha técnica**:
  [evaluation_generate_seo_spec_sheet_prompt](https://smith.langchain.com/hub/luis-fernando-martinez/evaluation_generate_seo_spec_sheet_prompt)

   **Evaluador de descripción de imagenes**:
  [evaluation_read_images](https://smith.langchain.com/hub/luis-fernando-martinez/evaluation_read_images)

Una vez definidos los prompts, se comienzan a realizar ejecuciones de la base de datos con cada uno de ellos. En este proceso, la respuesta pasa por el evaluador, quien devuelve un valor promedio de todas las puntuaciones asignadas por el modelo. Este valor se registra como "average" en la plataforma LangSmith.

### Resultados

#### Evaluación de los prompts para la funcion generate_seo_spec_sheet

En esta primera imagen, atraves de la plataforma de langsmith podemos ver las cuatro ejecuciones de la base de datos con los cuatro diferentes commits del prompt. También se muestran diversas métricas, que incluyen la latencia, los tokens utilizados para la respuesta y el costo total de la solicitud.
En una primera inspección podemos observar como las ejecuciones 3 y 4 presentan un `averange` mas alto, lo que los posiciona como dos de las mejores opciones

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/score_seo.png)

El valor `average` se obtiene al pasar los scores que devuelve el prompt evaluador y posteriormente, con una función desarrollada en el script `evaluation.py`, se promedian para retornar ese resultado. A continuación, se muestra un ejemplo de la respuesta del evaluador que se ejecuta con cada una de las filas de la base de datos en cada ejecución.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/eval_1.png)

También podemos hacer una comparativa de las diferentes ejecuciones tomando como referencia cualquiera de los prompts, en este caso el primero con ID **de77979a-dbb66ea2**, y vemos cómo las ejecuciones 2, 3 y 4 superan a la ejecución 1 con hasta 11 mejores resultados. Esto confirma que las ejecuciones 3 y 4 siguen mostrando un mejor desempeño al tener solo 2 resultados inferiores con respetco a la ejecución 1.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/score_seo2.png)

Finalmente, decido seleccionar el prompt la ejecución 3. Aunque tiene el mismo average que la ejecución 4, los resultados de latencia y los tokens utilizados para la respuesta son más bajos, lo que lo convierte en un prompt más óptimo para producción, ya que representaría un menor coste.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/score_seo3.png)

En el siguiente link se puede ver toda esta información con mas detalle. [generate_seo_spec_sheet en Langsmith](https://smith.langchain.com/public/eb8d05f6-e62f-4a18-a736-9e3de78478de/d)

#### Evaluación de los prompts para la funcion read_images

Para las imágenes, repetí el mismo procedimiento. En este caso, solo creé 3 prompts, por lo que solo hay 3 ejecuciones. Aquí se puede ver con más claridad cómo la ejecución 2 tiene un average más alto. Los tokens en este caso no los podemos visualizar debido al tipo de solicitud alternativa que se usó para leer imagenes en formato base64.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/images_2.png)

Aqui podemos ver como es una de las respuestas del evaluador de imagenes.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/eval_2.png)

Hacemos una comparativa de las diferentes ejecuciones tomando como referencia la primera con ID **d65b43cf-4137b6d4**, y vemos cómo la ejecución 2 es superior, registrando hasta 4 mejores respuestas en comparación con los otros dos prompts.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/images_3.png)

Para la lectura decido seleccionar el prompt de la ejecución 2, no solo porque su `averange` es mas alto si no que su latencia es considerablemente mas baja.

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/images_1.png)

En el siguiente link se puede ver toda esta información con mas detalle. [read_images en Langsmith](https://smith.langchain.com/public/c91028e2-76a4-4477-b11b-e3d03d939ed6/d)

### Resultado Final

Una vez determinados los prompts y con los scripts terminados, se ejecuta el programa que generará un CSV con la ficha enriquecida en la carpeta result.

## Video de Ejecución

A continuación se muestra el video solicitado en la prueba, que demuestra la ejecución del sistema y los resultados obtenidos.

[![Título del Video](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/min_video.png)](https://youtu.be/8I2uSxCjaHo)

### Comparataiva

**Datos recibidos**

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/seo_result3.png)

**Ficha enriquecida**

![images1](https://github.com/luisfMartinez1303/technical_test_onestic/blob/main/images/seo_result2.png)
