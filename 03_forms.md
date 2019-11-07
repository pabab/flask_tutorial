# Formularios y procesamiento de información

## Métodos GET y POST

HTTP funciona como un protocolo de pedido-respuesta entre un **cliente** y un **servidor**.

El **cliente** (por ejemplo el navegador web) solicita un recurso al **servidor** (por ejemplo la aplicación en Flask) y este último le devuelve una respuesta. La respuesta contiene información sobre el estado del pedido y también puede incluir contenido (código HTML por ejemplo).

Existen diferentes métodos para realizar un pedido, los métodos más comunes son **GET** y **POST**.

El método **GET** se utiliza para *solicitar* al servidor un determinado recurso (por ejemplo una página).
El método **POST** *envía* información al servidor para crear o actualizar un recurso.

Más infomación: [https://www.w3schools.com/tags/ref_httpmethods.asp](https://www.w3schools.com/tags/ref_httpmethods.asp)

Existen diferentes maneras de generar estos pedidos. Por ejemplo, los pedidos GET se generan al escribir una URL en la barra de direcciones y presionar ENTER, o al hacer clic sobre un enlace.

## Formularios y pedidos POST

Una forma de generar pedidos POST es a través de formularios. La etiqueta <form> permite especificar los atributos *method* y *action*. En *method* se puede especificar el tipo de request que generará el formulario (por ejemplo GET o POST).


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

Hay que programar desde el lado del servidor un endpoint /agregar que reciba los datos, es decir que reciba pedidos GET y también pedidos POST. Para eso se agrega el siguiente decorador arriba de la función:

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
