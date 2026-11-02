# Biblioteca de la asociación sindical

Aplicación web para gestionar la biblioteca de una asociación, desarrollada con Python y Django.

## Tecnologías utilizadas

- Python y Django
- Django REST Framework
- HTML, CSS y JavaScript
- Bootstrap y Sass
- PostgreSQL (pendiente de configuración)

## Requisitos previos

Para instalar y ejecutar la aplicación es necesario tener instalado:

- Python
- Node.js (incluye npm)

## Instalación

1. Descargar o clonar el repositorio de GitHub.
2. Crear un entorno virtual:

   ```powershell
   python -m venv .venv
   ```

3. Activar el entorno virtual en Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Instalar las dependencias de Python:

   ```powershell
   pip install -r requirements.txt
   ```
5. Instalar las dependencias de npm:

   ```powershell
   npm install
   ```
   
6. Aplicar las migraciones:

   ```powershell
   python manage.py migrate
   ```

7. Iniciar el servidor:

   ```powershell
   python manage.py runserver
   ```

8. Abrir en el navegador:

   http://127.0.0.1:8000/

## Estado del proyecto

El proyecto se encuentra en fase de desarrollo. 
Actualmente dispone de una página de inicio y una estructura inicial sobre la que se añadirán las funcionalidades de gestión de la biblioteca.