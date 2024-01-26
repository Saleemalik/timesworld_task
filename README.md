# start project

python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=admin ./manage.py createsuperuser --username=admin --email=admin@alain.com --noinput
./manage.py runserver
goto =>  http://127.0.0.1:8000/