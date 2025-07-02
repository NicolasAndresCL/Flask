# 🚀 Flask Task Manager - Aplicación Web RESTful

## 📌 Descripción
Este es un proyecto web desarrollado con Flask, que ha evolucionado de una aplicación basada en plantillas con Jinja2 a una arquitectura moderna basada en API REST. Incluye una estructura backend sólida, documentación interactiva y una base ideal para futuras integraciones con frontend como React.

## 🔗 Puedes ver más de mis proyectos en: 👉 nicolasandrescl.pythonanywhere.com ⚙️ Este proyecto pronto estará desplegado y accesible desde mi portafolio.

___

## ⚙️ Tecnologías utilizadas

- Python 3.12 – Lógica principal del backend

- Flask – Framework web ligero y modular

- Blueprints – Modularización de rutas en la API

- SQLite + SQLAlchemy – Base de datos relacional con ORM

- Flasgger (Swagger) – Documentación automática de la API

- Jinja2 – Renderizado de HTML dinámico

- Bootstrap – Diseño responsivo para el frontend

- Pytest – Pruebas unitarias

- Postman – Validación de endpoints

- Git – Control de versiones

___

## 🌟 Funcionalidades principales

✅ Renderizado de HTML usando Jinja2

✅ API RESTful con operaciones CRUD para tareas

✅ Documentación interactiva vía Swagger (/apidocs)

✅ Integración con SQLite y manejo de base de datos con SQLAlchemy

✅ Conjunto completo de pruebas unitarias con Pytest y base en memoria

✅ Patrón de fábrica para la creación de la app con modo de testing

✅ Manejo estructurado de errores y respuestas JSON

✅ Listo para producción y despliegue remoto

___

# 📁 Estructura del proyecto

```/Flask-TaskManager
│── /api
│   ├── __init__.py        # Registro del Blueprint
│   ├── routes.py          # Rutas y lógica de la API
│   ├── models.py          # Modelos con SQLAlchemy
│   └── database.py        # Configuración de la base de datos
│
│── /static                # Archivos estáticos (CSS, JS, etc.)
│── /templates             # Plantillas HTML con Jinja2
│── /tests                 # Pruebas con Pytest
│
│── app.py                 # Inicialización principal (factory)
│── requirements.txt       # Dependencias del proyecto
│── .gitignore             # Exclusiones para Git
│── README.md
```
___


# ⚙️ Instalación y ejecución

- Clona el repositorio:

```bash
git clone https://github.com/NicolasAndresCL/Flask
cd Flask-TaskManager
```
- Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
- Instala las dependencias:

```bash
pip install -r requirements.txt
```
- Ejecuta la aplicación:

```bash
python app.py
```
- Corre los tests:

```bash
pytest
```
## 📘 Documentación de la API
Una vez ejecutada la app, puedes acceder a la documentación Swagger desde: 📚 http://localhost:5000/apidocs

## 🌍 En camino a producción
Este proyecto será pronto desplegado y accesible desde mi portafolio personal en: 🔗 nicolasandrescl.pythonanywhere.com En futuras versiones incluirá autenticación, paginación y conexión con frontend dinámico.

## 🤝 Contribución
¿Tienes ideas para mejorar este proyecto? ¡Siéntete libre de abrir un issue o enviar un pull request! Todas las sugerencias son bienvenidas 🙌