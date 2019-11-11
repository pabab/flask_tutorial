
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

El código anterior realiza lo siguiente:

1. Importar el módulo Flask
2. Crear un objeto de tipo Flask (la aplicación) pasándole como argumento el nombre de la aplicación (puede ser cualquier nombre)
3. Definir las vistas/controladores
4. Correr la aplicación con app.run()

Para definir las vistas/controladores se debe crear funciones que devuelvan el código HTML que se visualizará.
Antes de la definición de la función se debe anteponer el decorator ```@app.route(...)``` que define cuál es la dirección que al visualizarse con el navegador disparará la vista. Más adelante veremos formas más sencillas de hacerlo mediante *templates*.

Para correr la aplicación, el siguiente comando crea un servidor temporal de desarrollo para probar la aplicación:

```
python app.py
```
También se puede ejecutar el servidor, de manera que se reinicie automáticamente cuando detecte cambios en el código, con el siguiente comando:

```
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run
```

[Descargar ejemplo](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/pabab/flask_tutorial/tree/master/examples/helloworld)