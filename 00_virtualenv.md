# Python/virtualenv

virtualenv es una herramienta que permite crear una instalación encapsulada de Python dentro de una carpeta. Esto tiene varias ventajas, por ejemplo:

* No *contaminamos* nuestra instalación local de Python con paquetes que utilizaremos sólo para un proyecto
* Es más sencillo tener instaladas distintas versiones de la misma biblioteca (por ejemplo, es posible que para un proyecto necesitemos utilizar alguna versión vieja de una biblioteca)
* Al llevar el proyecto a otra máquina (o un host en la nube) es más fácil replicar el entorno virtual y asegurar las condiciones para el correcto funcionamiento del proyecto.


## Instalar virtualenv en Windows

1. Descargar e instalar Python desde http://www.python.org
2. Agregar la carpeta de instalación de Python al PATH de sistema
3. Instalar virtualenv
```
python -m pip install virtualenv
```
4. Crear el entorno virtual en la carpeta venv
```
python -m virtualenv venv
```
5. Activar el entorno virtual (hay que hacerlo nuevamente cada vez que se empieza a trabajar)
```
venv/bin/activate
```

## Instalar virtualenv en Ubuntu/Linux

1. Instalar virtualenv
```
sudo apt-get install virtualenv
```
2. Crear el entorno virtual en la carpeta venv
```
virtualenv venv
```
3. Activar el entorno virtual (hay que hacerlo nuevamente cada vez que se empieza a trabajar)
```
source venv/bin/activate
```



## Instalar Flask en Windows

Con el entorno virtual activado corremos el siguiente comando

```
python -m pip install flask
```


## Instalar Flask en Ubuntu/Linux

Con el entorno virtual activado corremos el siguiente comando

```
pip install flask
```

## Otras operaciones con el entorno virtual

### Guardar todas las dependencias instaladas en el archivo requirements.txt

El siguiente comando debe ejecutarse con el entorno virtual activado

#### Windows
```
python -m pip freeze > requirements.txt
```

#### Ubuntu/Linux
```
pip freeze > requirements.txt
```

### Instalar todas las dependencias del archivo requirements.txt en el entorno virtual

El siguiente comando debe ejecutarse con el entorno virtual activado

#### Windows
```
python -m pip install -r requirements.txt
```

#### Ubuntu/Linux
```
pip install -r requirements.txt
```
