# PI-MLOps---STEAM
Proyecto Integrador de Data Engineer y machine learning para Henry
El siguiente proyecto de Data Science para la institución educativa Henry, trata sobre general un modelo de recomendación de videojuegos usando los Algoritmos de Machine Learning y 5 funciones que permitan responder las preguntas de negocio más importantes
## Fases
Se detallarán las fases más importantes de lo que fue generar el modelo de recomendación para que pueda ser consumido por cualquier usuario mediante la app de render
### Proceso de ETL (Extraccion, transformacion y carga)
Se tuvieron 4 documentos (tablas), Reviews, Items, SteamGames y Diccionarios asociados a los tipos de datos de cada tabla, en cada dataset se eliminaron dimensiones irrelevantes para el cálculo de las funciones y el modelo de machine learning, Asimismo se eliminaron los datos nulos, repetidos y datos con errores
### Elaboracion de Funciones 
1. Primera Función (Debe devolver año con más horas jugadas para dicho género), Se realizo este cálculo tomando en cuenta los años jugados por todos los juegos respecto al año de lanzamiento
2. Segunda Función (Debe devolver los años con sus respectivas horas de cada usuario que jugo más para un género dado), Se realizo el cálculo tomando en cuenta las horas de juego, los id de cada usuario, los géneros y la fecha que publicaron una reseña sobre ese juego
3. Tercera Función (Debe devolver los 3 juegos más recomendados para dicho año). Se hizo un análisis de sentimiento a cada comentario de cada usuario que hizo para cada juego, dando valores de 0 si su posición era negativa, 1 si era neutral y 2 si su posición era positiva. Asimismo, se tomó en cuenta si fue recomendado (True or False)
4. Cuarta Función (Debe devolver los 3 juegos menos recomendado para dicho año. Los procesos fueron igual que la función de recomendación para los juegos más recomendados, con la diferencia que en este no se tomaron en cuenta si fueron recomendados (False)
5. Quinta función (Devuelve el acumulado de positivo, negativo, neutral según año). Se hizo una sumatoria convirtiendo el sentimiento analizado a variables dummies, que permitió hallar los acumulados respectivos a cada año
### Modelo de Machine Learning
Devuelve 5 juegos más recomendados según un id asociado a un juego que se introduzca, para este modelo solo se usaron la dimensión de id del juego, el nombre del juego y al género que pertenecía cada juego, luego se procedieron a vectorizar las funciones para obtener las similaridades entre estos, y solo se seleccionaron los primeros 5 que coincidían
### Analisis Exploratorio de datos
Para el análisis exploratorio de datos se establecieron los valores más importantes como medias, medianas, promedios, cuartiles. Asimismo, las relaciones que existen entre las variables más relevantes de todo el trabajo
### Creacion de la API
Se creo una API mediante la librería FastApi, que permitió mediante la creación de un entorno virtual, saber cómo sería documentada con las funciones más importantes y el modelo de machine learning, acá se realizaron procesos que permitieron crear funciones de consulta optimizadas en un archivo final llamado main.py
### Deployement en Henry
Ya con el script de la API en un archivo main.py, se adjuntaron las tablas optimizadas de consulta y un archivo .txt que contenía las librerías a usar en cada consulta. Podrán acceder a la API deployada mediante el siguiente link:
Link de Render: https://josepazosmlops.onrender.com
