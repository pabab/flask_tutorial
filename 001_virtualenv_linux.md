# Instalar virtualenv en Ubuntu/Linux

1. Instalar virtualenv
```
sudo apt-get install virtualenv
```
1. Crear el entorno virtual en la carpeta venv
```
virtualenv venv
```
1. Activar el entorno virtual (hay que hacerlo nuevamente cada vez que se empieza a trabajar)
```
source venv/bin/activate
```



## Instalar Flask en Ubuntu/Linux

Con el entorno virtual activado corremos el siguiente comando

```
pip install flask
```

#### Ubuntu/Linux
```
pip freeze > requirements.txt
```


#### Ubuntu/Linux
```
pip install -r requirements.txt
```
