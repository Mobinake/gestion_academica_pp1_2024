# gestion_academica_pp1_2024

Este proyecto es la continuacion de la creacion del Sistema de Gestion Academica, elaborado en la materia de Practica
Profesional 1.

## Que es este proyecto?

Es un proyecto web, basado en python con el framework de django.

# Modulo Noticias
## Funcionalidades

1. **Listado de Noticias**:
   - URL: `/noticias/`: Muestra todas las noticias con opciones para ver detalles.
2. **Detalles de una Noticia**:
   - URL: `/noticias/detalle/<id_noticia>/`: Muestra el contenido completo de una noticia seleccionada.

3. **Crear Noticias**:
   - URL: `/noticias/crear/`: Formulario para crear nuevas noticias, con selección de autor desde un menú desplegable.

## Requisitos Previos
- Usuario autenticado para acceder y gestionar noticias.
- Base de datos configurada con usuarios existentes para asignar autores.

## Version Data

asgiref==3.8.1
autopep8==2.3.1
Django==5.0.4
django-filter==24.3
djangorestframework==3.15.2
et-xmlfile==1.1.0
Markdown==3.7
mysql-connector==2.2.9
mysqlclient==2.2.4
numpy==2.1.1
openpyxl==3.1.5
pandas==2.2.3
pillow==10.4.0
pycodestyle==2.12.1
python-dateutil==2.9.0.post0
pytz==2024.2
six==1.16.0
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.2

