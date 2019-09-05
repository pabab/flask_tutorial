
### Hello World Flask

Para crear una aplicación en Flask, crear un archivo de Python con el nombre app.py (u otro nombre) y con el siguiente contenido.

```python
from flask import Flask

app = Flask("myapp")

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route("/hello")
def hello2():
    return "<h1>Hello World</h1><p>This is a paragraph</p>"

app.run()
```

Para crear una aplicación de Flask es necesario:

1. Importar el módulo Flask
2. Crear un objeto de tipo Flask (la aplicación) pasándole como argumento el nombre de la aplicación (puede ser cualquiera)
3. Definir las vistas/controladores
4. Correr la aplicación con app.run()

Para definir las vistas/controladores se debe crear funciones que devuelvan el código HTML que se visualizará.
Antes de la definición de la función se debe anteponer el decorator ```@app.route(...)``` que define cuál es la dirección que al visualizarse con el navegador disparará la vista.


Para correr la aplicación, el siguiente comando crea un servidor temporal de desarrollo para probar la aplicación:

```
python app.py
```

