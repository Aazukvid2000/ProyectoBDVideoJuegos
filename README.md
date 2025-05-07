# ProyectoBDVideoJuegos
Proyecto del Segundo Parcial de la Materia de "Bases de Datos" en donde se tiene que subir una base de datos, hacer consultas en Pandas, Seaborn y SQL.

# Game Database API

## Descripción del Proyecto

Este proyecto consiste en una API para consultar y visualizar información sobre videojuegos, incluyendo datos sobre títulos, plataformas, ventas por región, géneros y editoriales. El sistema está desarrollado con FastAPI y utiliza una base de datos MySQL para almacenar la información, todo empaquetado en contenedores Docker para facilitar su despliegue.

## Características Principales

- API RESTful con múltiples endpoints para consultar información de videojuegos
- Visualización de datos mediante tablas HTML formateadas
- Generación de gráficos estadísticos utilizando seaborn y matplotlib
- Análisis de datos con pandas
- Interfaz de administración de base de datos con phpMyAdmin
- Despliegue containerizado con Docker y Docker Compose

## Estructura del Proyecto

### Organización de Archivos

El proyecto debe tener la siguiente estructura de directorios y archivos:

```
.
├── __pycache__/
├── sql/                      # Scripts SQL para inicializar la base de datos
├── database.py               # Conexión a la base de datos
├── docker-compose.yml        # Configuración de servicios Docker
├── Dockerfile                # Instrucciones para la imagen Docker
├── formato.py                # Formateo de tablas HTML
├── main.py                   # Punto de entrada de la API
├── pandas_consultas.py       # Consultas avanzadas con pandas
├── requirements.txt          # Dependencias del proyecto
└── seaborn_graficas.py       # Generación de gráficos
```

### Descripción de Archivos Principales

- **main.py**: Punto de entrada de la aplicación FastAPI y definición de todos los endpoints.
- **database.py**: Módulo para la conexión y operaciones con la base de datos MySQL.
- **pandas_consultas.py**: Consultas avanzadas utilizando pandas para análisis de datos.
- **seaborn_graficas.py**: Generación de gráficos estadísticos utilizando seaborn.
- **formato.py**: Funciones para formatear datos en tablas HTML.
- **docker-compose.yml**: Configuración de los servicios Docker (API, base de datos, phpMyAdmin).
- **Dockerfile**: Instrucciones para construir la imagen Docker de la aplicación.
- **requirements.txt**: Dependencias del proyecto.

## Requisitos Previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalación y Ejecución

1. Clona el repositorio o descarga los archivos del proyecto:

```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Asegúrate de que la estructura de archivos sea la correcta según se detalla en la sección "Estructura del Proyecto".

3. Asegúrate de crear una carpeta `sql/` en la raíz del proyecto. Esta carpeta debe contener los scripts SQL necesarios para inicializar la base de datos con las tablas y datos de videojuegos.

4. Inicia los servicios con Docker Compose:

```bash
docker-compose up -d
```

Este comando levantará tres servicios:
- **fastapi**: API en el puerto 8085
- **db**: Base de datos MySQL en el puerto 3308
- **phpmyadmin**: Interfaz de administración de la base de datos en el puerto 8086

5. Espera unos segundos para que la base de datos se inicialice correctamente.

6. Verifica que la API esté funcionando correctamente accediendo a:
```
http://localhost:8085
```

## Acceso a los Servicios

- **API REST**: http://localhost:8085
- **Documentación de la API**: http://localhost:8085/docs
- **phpMyAdmin**: http://localhost:8086 (usuario: root, contraseña: rootpassword)

## Descripción de los Endpoints

### Endpoints Básicos

| Endpoint | Descripción |
|----------|-------------|
| `/` | Página principal, verifica que la API está funcionando |
| `/tables` | Lista todas las tablas de la base de datos |
| `/tables/{table_name}` | Muestra datos de una tabla específica |
| `/games` | Obtiene un listado de juegos |
| `/games/{game_id}` | Obtiene información de un juego específico |
| `/games/{game_id}/complete` | Obtiene información completa de un juego (con relaciones) |
| `/platforms` | Obtiene un listado de plataformas |
| `/publishers` | Obtiene un listado de editores |
| `/genres` | Obtiene un listado de géneros |
| `/regions` | Obtiene un listado de regiones |
| `/sales` | Obtiene información de ventas |

### Endpoints Estadísticos (JSON)

| Endpoint | Descripción |
|----------|-------------|
| `/stats/best-sellings-games/{numero}` | Obtiene los juegos más vendidos |
| `/stats/sales-by-genre` | Obtiene ventas por género |
| `/stats/sales-by-platform` | Obtiene ventas por plataforma |
| `/stats/sales-by-publisher` | Obtiene ventas por editor |
| `/stats/sales-by-year-platform` | Obtiene ventas por año y plataforma |
| `/games/by-year/{year}` | Filtra juegos por año de lanzamiento |

### Endpoints con Pandas (HTML)

| Endpoint | Descripción |
|----------|-------------|
| `/pandas/top-generos/{top}` | Muestra los géneros con más juegos |
| `/pandas/juegos-menos-ventas/{top}` | Muestra los juegos con menos ventas |
| `/pandas/top-publishers/{top}` | Muestra los editores con más juegos |

### Endpoints con Seaborn (Gráficos)

| Endpoint | Descripción |
|----------|-------------|
| `/seaborn/top-juegos-ventas/{top}` | Genera un gráfico de los juegos con más ventas |
| `/seaborn/top-generos-ventas/{top}` | Genera un gráfico de los géneros con más ventas |
| `/seaborn/ventas-plataforma-region/{top}` | Genera un gráfico de ventas por plataforma y región |

## Ejemplos de Uso

### Consulta de juegos más vendidos:
```
http://localhost:8085/stats/best-sellings-games/10
```

### Visualización de géneros más populares:
```
http://localhost:8085/pandas/top-generos/5
```

### Gráfico de ventas por género:
```
http://localhost:8085/seaborn/top-generos-ventas/10
```

## Cómo verificar que todo funciona correctamente

1. Accede a la URL base para confirmar que la API está en funcionamiento:
```
http://localhost:8085
```
Deberías ver un mensaje JSON: `{"message": "Game Database API is running"}`

2. Revisa la documentación de la API para probar los endpoints interactivamente:
```
http://localhost:8085/docs
```

3. Verifica que la base de datos esté funcionando correctamente accediendo a phpMyAdmin:
```
http://localhost:8086
```
Inicia sesión con usuario: `root` y contraseña: `rootpassword`

4. Prueba algunos endpoints específicos:
   - Lista de juegos: `http://localhost:8085/games`
   - Gráfico de mejores juegos: `http://localhost:8085/seaborn/top-juegos-ventas/10`
   - Tabla de editores: `http://localhost:8085/pandas/top-publishers/5`

## Detención de los servicios

Para detener los servicios, ejecuta:

```bash
docker-compose down
```

Si además deseas eliminar los volúmenes de datos:

```bash
docker-compose down -v
```

## Descripción de Códigos

### database.py
Maneja la conexión a la base de datos MySQL, proporciona funciones para ejecutar consultas SQL, convertir resultados a DataFrames de pandas y generar gráficos básicos.

### formato.py
Contiene funciones para formatear los resultados de las consultas en tablas HTML con estilos Bootstrap.

### main.py
Define todos los endpoints de la API utilizando FastAPI. Importa funciones de los otros módulos y coordina la interacción entre ellos.

### pandas_consultas.py
Contiene consultas específicas que utilizan pandas para análisis más complejos de datos.

### seaborn_graficas.py
Genera visualizaciones avanzadas utilizando seaborn y matplotlib para análisis estadístico de datos.

### docker-compose.yml
Define y configura los servicios Docker necesarios para el proyecto, incluyendo la API, la base de datos MySQL y phpMyAdmin.

## Solución de problemas

### La base de datos no se inicializa correctamente
Si la base de datos no se inicializa correctamente, puede ser necesario reiniciar los servicios:

```bash
docker-compose down
docker-compose up -d
```

Asegúrate de que la carpeta `sql/` contenga los scripts SQL necesarios y que estos tengan permiso de lectura:

```bash
ls -la sql/
chmod +r sql/*.sql  # Si es necesario dar permisos de lectura
```

### La API no responde
Verifica los logs para diagnosticar el problema:

```bash
docker-compose logs fastapi
```

### Problemas de conexión a la base de datos
Asegúrate de que el servicio de la base de datos esté funcionando correctamente:

```bash
docker-compose ps
```

Si el servicio de la base de datos está activo pero sigue habiendo problemas de conexión, verifica los logs:

```bash
docker-compose logs db
```
