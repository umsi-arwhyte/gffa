A Galaxy Far, Far Away.

Commands to get started:
python -m venv venv
source env/scripts/activate
python -m pip install django psycopg2
python -m pip freeze > requirements.txt
django-admin startproject gffa
cd gffa
python manage.py makemigrations
python manage.py migrate
winpty python manage.py createsuperuser
username: gffa-superuser
password: <some_password>
email: <some_email>
python manage.py runserver
