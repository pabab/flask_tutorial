# Formularios y procesamiento de información

## Métodos GET y POST

HTTP funciona como un protocolo de pedido-respuesta entre un **cliente** y un **servidor**.

El **cliente** (por ejemplo el navegador web) solicita un recurso al **servidor** (por ejemplo la aplicación en Flask) y este último le devuelve una respuesta. La respuesta contiene información sobre el estado del pedido y también puede incluir contenido (código HTML por ejemplo) como se muestra en la siguiente imagen.

![](https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_ResponseMessageExample.png)

Existen diferentes métodos para realizar un pedido, los métodos más comunes son **GET** y **POST**.

El método **GET** se utiliza para *solicitar* al servidor un determinado recurso (por ejemplo una página).
El método **POST** *envía* información al servidor para crear o actualizar un recurso.

Más infomación: [https://www.w3schools.com/tags/ref_httpmethods.asp](https://www.w3schools.com/tags/ref_httpmethods.asp)

Existen diferentes maneras de generar estos pedidos. Por ejemplo, los pedidos GET se generan al escribir una URL en la barra de direcciones y presionar ENTER, o al hacer clic sobre un enlace.

## Formularios y pedidos POST

Una forma de generar pedidos POST es a través de formularios. La etiqueta <form> permite definir un formulario. Los atributos *method* y *action* especifican el tipo de request que generará el formulario (por ejemplo GET o POST) y la URL o dirección del servidor al cual se dirigirá dicho mensaje.


```html
<form method="POST" action="/agregar">
    <label>Nombre: </label>
    <input name="user">
    <br>
    <label>Tiempo: </label>
	<input name="time">
    <br>
	<button>lalal</button>
</form>
```

El formulario del ejemplo enviará los datos mediante un método POST al endpoint /agregar del mismo servidor desde el cual se cargo el formulario. Los datos consistirán en dos variables: *user* y *time*.

Hay que programar desde el lado del servidor un endpoint */agregar* que reciba dichos datos, es decir que reciba pedidos GET y también pedidos POST. Para eso se agrega el siguiente decorador arriba de la función:

```python
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
	...
```

El tema es que el endpoint agregar sirve para 2 cosas:
Recibir un pedido GET y mostrar el HTML con el formulario
Recibir un pedido POST con los datos enviados por el formulario

```python
@app.route("/agregar", methods=["GET", "POST"])
def hello2():
    if request.method == "POST":
        
    else:
        ...
   	return render_template("agregar.html")
```

Entonces, si el pedido fue un POST, vamos a procesar los datos del formulario, si fue un GET simplemente renderizamos la plantilla

## El patron POST, REDIRECT, GET

Una vez que procesamos el pedido POST e hicimos algo con los datos que el usuario ingresó en el formulario, debemos enviarle una respuesta.

Para evitar repetir código, una manera rápida de generar una respuesta es devolver un mensaje REDIRECT, que indica que la navegación se debe redireccionar a otra URL.

Cuando el cliente (el navegador) recibe un mensaje REDIRECT hace un nuevo pedido GET a la URL indicada en el mensaje.

En Flask se puede devolver una respuesta con el mensaje REDIRECT con el siguiente código:

```python
return redirect("/lista")
```
![](https://www.seobility.net/en/wiki/images/d/d3/Post-Redirect-Get.png)

## Validación de formularios

### Validación desde el servidor vs validación desde el cliente

Validar los datos del formulario implica comprobar que el usuario ingresó datos correctos o que tienen sentido. La validación puede y debe hacerse desde ambos lados: servidor y cliente.

Para validar los datos del formulario desde el cliente debemos editar el código HTML del formulario para agregar a los *inputs* los atributos necesarios, por ejemplo: *required*, *type*, *min*, *max*, etc.

Validar los datos desde el cliente nos ahorra tiempo porque evitamos la demora de enviar los datos al servidor y esperar la respuesta, pero **siempre es necesario validar también los datos desde el servidor**. Esto es así por varias razones, en primer lugar porque no todas las validaciones se pueden realizar desde el cliente, hay datos que sólo están disponibles del lado del servidor (por ejemplo cuando al crear una cuenta el usuario ingresa un correo válido pero ya existe una cuenta con esa dirección de correo). Por otro lado, existen otras formas de enviar mensajes POST a un servidor además de los formularios, por eso no es suficiente contar sólo con la validación del cliente. 

### FlaskWTF

Como la creación y validación de formularios involucra cierta complejidad, vamps a utilizar una herramienta para facilitar la tarea: *FlaskWTF*.

En primer lugar, es necesario instalar el paquete en el entorno virtual:

```
python -m pip install flask-wtf
```

La idea de FlaskWTF es un crear **modelo** (es decir, una entidad que representa un modelo real). A partir de ese modelo *FlaskWTF* podrá ayudarnos generando el HTML del formulario y validando el mismo.

Para crear un modelo para el formulario se debe heredar de la clase 

```python 
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect

class FormularioAgregar(FlaskForm):
    name = StringField('name')
    time = IntegerField('time')
```

Dentro de la clase se agregan los datos que nos interesa que tenga el formulario. El tipo de cada dato corresponde a los [https://wtforms.readthedocs.io/en/stable/fields.html#basic-fields](tipos específicos que ofrece FlaskWTF), por ejemplo: BooleanField, IntegerField, StringField, etc.

Además, como segundo parámetro de cada campo se puede agregar un parámetro opcional llamado *validators* que consiste en un arreglo de elementos del tipo **Validator** de WTForms. Los validadores se encargan precisamente de validar automáticamente los campos del formulario cuando el mismo es enviado.

Por ejemplo, en el siguiente código se agregan validadores para cada uno de los campos. En el primer caso se agrega el validador **DataRequired** revisará que el campo *name* tenga un valor no nulo cuando el servidor reciba el formulario.

Notar que los validadores van entre [] ya que su valor es una lista.

En el caso del campo *time*, se trata de un IntegerField, es decir un campo entero. La lista lleva dos validadores un **DataRequired** y un **NumberRange**. Éste último valida que el valor numérico del campo se encuentre dentro de cierto rango.

```python
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect

class FormularioAgregar(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    time = IntegerField('time', validators=[DataRequired(), NumberRange(min=0, max=100)])
```

### CSRF Protection

CSRF (Cross Site Request Forgery) es un tipo de exploit malicioso de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía.

Es necesario programar en el servidor mecanismos que permitan evitar este tipo de ataques.

Afortunadamente Flask-WTF provee mecanismos para evitar este tipo de ataques agregando un número clave a cada formulario que se renderiza. Cuando el usuario envía los datos del formulario, también se envía este número clave junto con los datos, lo cual le permite al servidor saber que los datos provienen de un usuario legítimo.

Para configurar estos mecanismos de proteccion es necesario realizar algunos pasos. 

En primer lugar, importar **CSRFProtect** 

```python
from flask_wtf.csrf import CSRFProtect
```

En segundo lugar, es necesario crear un objeto **CSRFProtect** para proteger la aplicación: 

```python
app = Flask("myapp")
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "secret"
```

El último paso agrega una clave secreta a partir de la cual se generarán los números clave para los formularios. En este caso la clave es "*secret*", pero puede ser cualquier palabra o frase.

## Renderizado y validación

En la vista, se debe crear una instancia del formulario-modelo que creamos anteriormente (FormularioAgregar). Este objeto nos permitirá, como dijimos antes, facilitar el renderizado del formulario por un lado y la validación de datos por otro.

El llamado al método *validate_on_submit()* del formulario permite validar los datos enviados por el usuario. El método **sólo devolverá verdadero** si el usuario envió datos al endpoint (es decir, con el método POST) y los datos cumplen con los criterios de validación expresados durante la creación del modelo.

En este caso, si los datos son válidos, se puede acceder a los datos del formulario utilizando los mismos campos que se declararon al crear el modelo (en este caso *name* y *time*). Estos datos ya se encontrarán validados por el propio formulario.

Es importante, al acceder a los datos, hacerlo con el subcampo *data* de cada campo, por ejemplo, ```form.name.data``` y no sólo ```form.name```, ya que esta última forma implica acceder a todo el campo (el control gráfico donde se ingresan los datos) y la primer manera proporciona únicamente los datos ingresados. 

En el ejemplo siguiente se creará un diccionario (*competidor*) con los datos enviados y se añadirá al arreglo *competidores*.

```python
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    form = FormularioAgregar()
    if form.validate_on_submit():
        competidor = {
            'nombre': form.name.data,
            'tiempo': form.time.data,
        }
        competidores.append(competidor)
        return redirect("/lista")
    else:
        return render_template("agregar.html", form=form)
```

Además, para poder renderizar el formulario más fácilmente es conveniente pasar el objeto formulario creado antes al método *render_template()* para poder acceder a dicho objeto desde el formulario.

## Renderizado del formulario 

Para renderizar el formulario, desde la plantilla, **y si pasamos el formulario como argumento** a la función *render_template()* podemos hacer lo siguiente para crear automáticamente el HTML correspondiente a los campos.

```html
<form method="POST" action="/agregar">
    {{ form.csrf_token }}
    {{ form.name.label }}{{ form.name }}
    <br>
    {{ form.time.label }}{{ form.time }}
    <br>
    <input type="submit" value="ajskhd">
</form>
```

La línea ```{{ form.csrf_token }}``` renderiza un campo oculto del formulario (no se visualizará pero sí se enviará con los datos).

La sentencia ```{{ form.name.label }}``` renderiza una etiqueta **<label>** corre con los datos correspondientes al campo *name* declarado en el modelo del formulario. Por otro lado, la sentencia ```{{ form.name.field }}``` renderiza el campo **<input>**, con los atributos necesarios para las validaciones declaradas para el campo *name* en el modelo del formulario.


[Descargar ejemplo](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/pabab/flask_tutorial/tree/master/examples/forms_wtf)