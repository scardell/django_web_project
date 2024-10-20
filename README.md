# django_web_project
Proyecto Web con Django - Este es un proyecto web desarrollado en Django. El objetivo es aprender los conceptos fundamentales de Django, desde la creación de un entorno virtual hasta la implementación de funcionalidades básicas de una aplicación web.

python -m venv venv
.\\venv\\Scripts\\Activate
pip install -r requirements.txt
django-admin startproject proyectoWeb .
python manage.py startapp ProyectoWebApp
python manage.py runserver
python manage.py startapp servicios
python -m pip install Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp blog
python manage.py makemigrations blog
python manage.py migrate blog
pip freeze > requirements.txt


