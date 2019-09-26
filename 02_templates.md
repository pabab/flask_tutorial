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
```

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

Una plantilla puede tomar como base a otra y reemplazar sólo algunas partes de la misma, esto se conoce como **herencia de plantilla**. Para hacer esto se necesitan dos archivos: una plantilla de base que será la plantilla general y una segunda que heredará de la primera (tomará todo el contenido de la primera y reemplazará o agregará algunas partes).

Debajo se muestra el contenido del archivo *base.html* que constituye una plantilla que se utilizará como base común para otras.


```html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <div class="container">
            <header>

            </header>

            <nav>

            </nav>

            {% block content %}

            {% endblock %}
        </div>
    </body>
</html>
```

La directiva ```{% block content %}``` define una porción de la plantilla que será reemplazada o redefinida en las plantillas que hereden de la misma. En este caso, el nombre de dicho bloque es *content* y finaliza con la directiva ```{% endblock %}```

Para heredar de la plantilla *base.html* se debe incluir la directiva ```{% extends "base.html" %}``` al principio de la nueva plantilla. Además, se puede redefinir el contenido del bloque *content* utilizando las directivas ```{% block content %}``` y ```{% endblock %}```. Por ejemplo, la plantilla *main.html* que hereda de *base.html* se vería como se muestra debajo.

```html
{% extends "base.html" %}
{% block content %}
<div>
	Este es el contenido
</div>
{% endblock %}
```

El resultado de invocar a *render_template()* para renderizar la plantilla *main.html* sería el siguiente:


```html
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <div class="container">
            <header>

            </header>

            <nav>

            </nav>

            <div>
		Este es el contenido
	    </div>
        </div>
    </body>
</html>
```

Así, mediante herencia de plantillas se puede evitar repetir código y ordenar mejor el contenido HTML.
