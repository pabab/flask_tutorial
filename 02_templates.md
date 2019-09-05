# Plantillas

Las plantillas son fragmentos parciales de HTML que el servidor puede procesar y así producir documentos dinámicos (cambian).

Se debe crear en el proyecto una carpeta llamada ```templates```
y colocar allí los archivos HTML.

```
from flask import Flask, render_template

app = Flask("myapp")

@app.route("/")
def hello():
    return render_template("hello.html", nombre="Pablo")
``

Para renderizar una plantilla se debe:

1. Importar la función ```render_template()```
2. La vista debe devolver el resultado de la llamada a ```render_template()```
3. ```render_template()``` recibe como argumentos el nombre del archivo plantilla y una cantidad arbitraria de variables que podrán ser accesibles desde la plantilla. En el código de ejemplo se ha pasado a la plantilla una variable llamada ```nombre```.

Desde la plantilla se puede acceder al valor de las variables pasadas a ```render_template()``` utilizando ```{{ }}```, por ejemplo.

```html
<html>
    <body>
        <p>
            Hola {{nombre}}!!!
        </p>    
    </body>
</html>
```

## Archivos estáticos

Las plantillas que pueden ser procesadas por el servidor para producir documentos dinámicos. Los archivos estáticos, por otro lado, son archivos que no son modificados ni procesados por el servidor.

Para los archivos estáticos se debe crear una carpeta llamada ```static``` dentro de la carpeta del proyecto. Todos los archivos colocados dentro de esa carpeta serán accesibles desde la url: ```/static```. Por ejemplo, si dentro de la carpeta ```/static``` existe una carpeta ```css``` y dentro de ella un archivo ```style.css```, se puede incluir el archivo en la plantilla de la siguiente manera:

```html
<html>
    <head>
        <link rel="stylesheet" href="/static/css/style.css">
    <head>
    <body>
        <p>
            Hola {{nombre}}!!!
        </p>    
    </body>
</html>
```

Los archivos estáticos son generalmente:

* Hojas de estilo
* Scripts de Javascript
* Imágenes, sonidos, etc.

## Herencia de plantillas

