# Plantillas

Las plantillas son fragmentos parciales de HTML que el servidor puede procesar y así producir documentos dinámicos (es decir, que cambian cada vez que se los consulta según determinados parámetros).

Para utilizarlas se debe crear, en la carpeta del proyecto, una carpeta llamada ```templates```
y colocar allí los archivos HTML correspondientes a las plantillas.

El siguiente código muestra como crear una vista/controlador que devuelve el contenido de una plantilla.

```
from flask import Flask, render_template

app = Flask("myapp")

@app.route("/")
def hello():
    return render_template("hello.html", nombre="Pablo")
```

El código anterior realiza los siguientes pasos:

1. Importar la función ```render_template()```
2. La vista debe devolver el resultado de la llamada a ```render_template()```, por eso el **return**
3. ```render_template()``` recibe como argumentos el nombre del archivo plantilla (*hello.html* en este caso) y una cantidad arbitraria de variables que podrán ser accesibles desde la plantilla. En el código del ejemplo se ha pasado a la plantilla una variable llamada ```nombre``` con el valor *Pablo*.

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

Cuando ```render_template()``` procese la plantilla con el código mostrado anteriormente, el resultado que recibirá el navegador del cliente será el siguiente:

```html
<html>
    <body>
        <p>
            Hola Pablo!!!
        </p>    
    </body>
</html>
```

De esta manera, a partir del código del servidor se puede modificar dinámicamente el contenido HTML que se generará.


## Archivos estáticos

Las plantillas que pueden ser procesadas por el servidor para producir documentos dinámicos. Los archivos estáticos, por otro lado, son archivos que no son modificados ni procesados por el servidor. Por ejemplo: archivos .css, archivos de media (imágenes, sonidos, etc), archivos de Javascript (.js).

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

[Descargar ejemplo](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/pabab/flask_tutorial/tree/master/examples/templates_static)


## Herencia de plantillas

Una plantilla puede tomar como base a otra y reemplazar sólo algunas partes de la misma, esto se conoce como **herencia de plantillas**. Esto resulta útil en diversas situaciones, por ejemplo cuando existen varios documentos HTML que comparten partes en común.

Para aplicar esta técnica hacen falta al menos dos archivos: una plantilla de base que será la plantilla general y una segunda que heredará de la primera (tomará todo el contenido de la primera y reemplazará o agregará algunas partes).

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

[Descargar ejemplo](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/pabab/flask_tutorial/tree/master/examples/templates_inheritance)