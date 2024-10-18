# API-CRUD

Para realizar este ejercicio he creado un entorno virtual en ubuntu y he usado la siguientes herramientas y estructura de carpetas.

## HERRAMIENTAS

Las herramientas utilizadas son:

- Flask
- Sqlite3
- SQLAlchemy
- Python
- Locust (para las pruebas de rendimiento)

## ESTRUCTURA DE CARPETAS

He creado la siguiente estructura de carpetas: 

```plaintext
API-CRUD/
│
├── entorno_api/
│   ├── app.py            # Aplicación
│   ├── instance/  
|       └── database.bd   # Base de datos SQLite
│   ├── templates/        # Plantillas HTML
│   │   ├── index.html
│   │   ├── create.html
│   │   └── update.html
│   └── static/               # Archivos estáticos
│       └── styles.css        # Archivo CSS para estilos
│
└── pruebas/                  # Directorio para pruebas
    ├── locustfile.py                 # Pruebas de rendimiento para app.py
    ├── test_prueba_funcional.py      # Pruebas de funcionalidad para app.py
    ├── test_prueba_integracion.py    # Pruebas de integración para app.py
    ├── test_prueba_unitaria.py       # Pruebas unitarias para app.py
    └── test_seguridad.py             # Pruebas de seguridad para app.py
```



## PRUEBAS

Para las pruebas de rendimiento he usado este comando:

```bash
locust -f locustfile.py --host=http://127.0.0.1:5000
```

estando en esta ruta:

```plaintext
/Escritorio/MONITORIZACION/API-CRUD/entorno_api/pruebas
```

<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/locustfile_comando.png" alt="Imagen de comando de Locust" />
</p>


Para realizar esta prueba es necesario tener en ejecución la aplicación en una terminal y ejecutar el comando anterirormente visto en otra terminal diferente.
Al abrir la dirección de ese comando (http://0.0.0.0:8089/) se nos abre una ventana en el navegador de Locust donde podremos elegir el número de usuarios simultáneos, etc

<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/locustfile_conf.png" alt="Imagen configuración en Locust" />
</p>


Una vez tenemos todos los parámetros ajustados se nos muestra esto.

<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/locustfile.png" alt="Imagen de rendimiento en Locust" />
</p>


Para las demás pruebas he utilizado este comando:

```bash
PYTHONPATH=. pytest entorno_api/pruebas/
```

y lo he ejecutado desde la ruta: 

```plaintext
/Escritorio/MONITORIZACION/API-CRUD$
```

Aquí hay algunas imagenes de las pruebas:

<p align="center">Prueba unitaria</p>
<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/prueba unitaria bien.png" alt="Imagen de prueba unitaria" />
</p>

<p align="center">Prueba de integración</p>
<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/prueba integracion.png" alt="Imagen de prueba de integración" />
</p>

<p align="center">Todas las pruebas</p>
<p align="center">
  <img width='60%' src="https://github.com/alvarodelburgoperez/API-CRUD/blob/main/assets/prueba seguridad.png" alt="Imagen de prueba de seguridad" />
</p>



