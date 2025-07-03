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
✅ Documentación interactiva vía Swagger en /apidocs 
✅ Conjunto completo de pruebas unitarias con Pytest y base en memoria 
✅ Integración con SQLite y manejo de base de datos con SQLAlchemy 
✅ Patrón de fábrica (create_app) para entornos productivos y de testing 
✅ Manejo estructurado de errores y respuestas JSON 
✅ Modularización clara usando Blueprints separados 
✅ Aplicación lista para despliegue remoto en producción
___

## 🔐 Autenticación implementada con JWT

- El proyecto ya cuenta con un flujo de autenticación seguro y profesional:

- POST /api/register: Registro de usuarios nuevos

- POST /api/login: Autenticación y generación de token JWT

- Protección de rutas sensibles con @jwt_required()

- Swagger configurado para enviar el token automáticamente desde el botón Authorize

- Esquema Bearer documentado para acceso autenticado

- Tokens correctamente identificados y validados mediante get_jwt_identity()

## 🎯 Esta arquitectura está preparada para escalar con:

- Refresh Tokens

- Perfiles de usuario

- Autorización por roles o permisos

- Integración con frontend dinámico como React

___

## 📘 Documentación de la API
Una vez ejecutada la aplicación, podés acceder a la documentación Swagger desde: 📚 http://localhost:5000/apidocs

___

# 📁 Estructura del proyecto

```//Flask
│── /api
│   ├── __init__.py        # Registro del Blueprint
│   ├── routes.py          # Rutas y lógica de la API de tareas
│   ├── auth.py            # Rutas de autenticación (login y registro)
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
cd Flask
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
___

## 🌍 Despliegue y próximos pasos

El proyecto será desplegado en breve en: 🔗 nicolasandrescl.pythonanywhere.com

🧠 En próximas versiones se integrarán:

- Refresh tokens

- Paginación y filtros

- Login desde frontend React

- Roles y permisos dinámicos

- Panel de administración

## 🤝 Contribución
¿Tienes ideas para mejorar este proyecto? ¡Siéntete libre de abrir un issue o enviar un pull request! Todas las sugerencias son bienvenidas 🙌