# Documentación de la API REST con Flask

## Descripción
Bienvenido a la documentación de esta API REST desarrollada con Flask. Esta API proporciona acceso a un catálogo de libros, incluyendo detalles como autor, género, año de publicación y resumen.

## Índice

1. [Instalación](#instalación)
2. [Configuración](#configuración)
3. [Uso](#uso)
4. [Rutas de la API](#rutas-de-la-api)
5. [Ejemplos](#ejemplos)
6. [Contribución](#contribución)
7. [Licencia](#licencia)

## Instalación

Para utilizar esta API en tu entorno local, sigue estos pasos:

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/PabloJRW/rest-api.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd rest-api
    ```

3. Crea un entorno virtual (se recomienda el uso de `venv`):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    En Windows:

    ```bash
    venv\Scripts\activate
    ```

    En macOS y Linux:

    ```bash
    source venv/bin/activate
    ```

5. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

Asegúrate de configurar las variables de entorno adecuadas y el archivo de configuración según sea necesario. Puedes encontrar ejemplos de configuración en el archivo `config.py`.



## Uso

Para iniciar el servidor de desarrollo, ejecuta:

```bash
python run.py
```

La API estará disponible en http://localhost:5000/books.


## Rutas de la API

A continuación, se describen las rutas principales de la API:

- `GET /books`: Obtiene una lista de todos los libros disponibles en la biblioteca.
- `GET /books/{id}`: Obtiene información detallada sobre un libro específico identificado por su ID.
- `POST /books`: Permite agregar un nuevo libro a la biblioteca.
- `PUT /books/{id}`: Actualiza la información de un libro existente.
- `DELETE /books/{id}`: Elimina un libro de la biblioteca.
- `GET /books/by-author/{author}`: Busca libros por autor, proporcionando una lista de libros escritos por el autor especificado.
- `GET /books/by-genre/{genre}`: Filtra libros por género, devolviendo una lista de libros que pertenecen al género especificado.
- `GET /books/search?q={query}`: Realiza una búsqueda de libros utilizando una consulta de búsqueda proporcionada en el parámetro `q`.
- `POST /books/{id}/reviews`: Permite a los usuarios agregar reseñas a un libro específico.
- `GET /books/{id}/reviews`: Obtiene todas las reseñas de un libro específico.

Cada ruta tiene su propia funcionalidad y parámetros específicos. Consulta la documentación detallada de cada ruta para obtener más información sobre cómo utilizarlas.

    
## Ejemplos

Puedes encontrar ejemplos de solicitud y respuesta en la carpeta examples.

## Contribución

Aprecio las contribuciones! Si deseas mejorar este proyecto, sigue estos pasos:

1. Abre un issue para discutir tu propuesta de cambio.
2. Realiza un fork del repositorio.
3. Crea una rama para tu contribución: ```git checkout -b mi-contribucion```.
4. Realiza los cambios y asegúrate de que las pruebas pasen.
5. Envía un pull request con tus cambios.


## Licencia

Este proyecto está bajo la licencia [nombre de la licencia]. Consulta el archivo LICENSE para obtener más detalles.

Gracias por tu interés en nuestro proyecto. ¡Esperamos que sea útil para ti y tu equipo!

