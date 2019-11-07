# Creación y manejo de entorno virtual en Windows

## Instalar virtualenv

1. Descargar e instalar Python desde http://www.python.org
1. Abrir la línea de comando para escribir los siguientes comandos (Inicio -> cmd -> ENTER)
1. Agregar la carpeta de instalación de Python al PATH de sistema
1. Instalar virtualenv
```
python -m pip install virtualenv
```
1. Crear el entorno virtual (el siguiente comando creará una carpeta *venv* que alojará el entorno virtual)
```
virtualenv venv
```
ó, si el comando anterior no funciona
```
python -m virtualenv venv
```

1. Activar el entorno virtual (hay que hacerlo nuevamente cada vez que se empieza a trabajar)
```
venv\Scripts\activate
```


## Instalar Flask

Con el entorno virtual activado corremos el siguiente comando

```
python -m pip install flask
```


## Otras operaciones con el entorno virtual

### Guardar todas las dependencias instaladas en el archivo requirements.txt

Guardar la lista de todos los paquetes instalados en el entorno virtual nos sirve para volver a instalar todos esos paquetes de manera automática y con un sólo comando en un entorno virtual limpio. De esta manera, cuando queremos llevar el proyecto a otra computadora, sólo necesitaremos copiar el código fuente y el archivo con la lista de paquetes instalados (requirements.txt).  

El siguiente comando debe ejecutarse con el entorno virtual activado.

```
python -m pip freeze > requirements.txt
```

### Instalar todas las dependencias del archivo requirements.txt en el entorno virtual

Para instalar una lista de paquetes leída desde un archivo (requirements.txt) en un entorno virtual limpio podemos utilizar el siguiente comando (debe ejecutarse con el entorno virtual activado):

```
python -m pip install -r requirements.txt
```
