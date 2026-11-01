# Biblioteca de la asociación

Aplicación web para gestionar la biblioteca de una asociación, desarrollada con Python y Django.

## Tecnologías utilizadas

- Python y Django
- Django REST Framework
- HTML, CSS y JavaScript
- Bootstrap y Sass
- PostgreSQL (pendiente de configuración)

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

4. Instalar las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

5. Aplicar las migraciones:

   ```powershell
   python manage.py migrate
   ```

6. Iniciar el servidor:

   ```powershell
   python manage.py runserver
   ```

7. Abrir en el navegador:

   http://127.0.0.1:8000/

## Estado del proyecto

El proyecto se encuentra en fase de desarrollo. Actualmente dispone de una página de inicio y una estructura inicial sobre la que se añadirán las funcionalidades de gestión de la biblioteca.