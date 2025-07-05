# Setup
0. створюжмо нове віртуальане оточення
    
    python -m venv %pyenv%\lyuda_site
    %pyenv%\lyuda_site\scripts\activate.bat
    %pyenv%\lyuda_site\scripts\deactivate.bat

1. Переходимо в діректорію проекту
```cmd
cd site
```

2. встновлюємо poetry і налаштувати poetry
    ```cmd
    pip install poetry
    %GitHub%\site-lyuda-card
    poetry init
    ```

3. Встановлюємо необхідні бібліотеки
```
poetry add django
poetry add psycopg2-binary
poetry add django-environ
poetry add whitenoise
poetry add gunicorn
poetry add environ
poetry add geoip2
```

4. потрібно створити `.env` файл в середині `site` папці
```
SECRET_KEY=secret
DATABASE_NAME=db-name
DATABASE_USER=db-user
DATABASE_PASSWORD=password
DATABASE_HOST=host
DATABASE_PORT=5432
PUBLIC_KEY=secret
EMAIL_HOST=smtp.meta.ua
EMAIL_PORT=465
EMAIL_HOST_USER=xxx@meta.ua
EMAIL_HOST_PASSWORD=email-password
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
DEFAULT_FROM_EMAIL=Personal Assistant <xxx@meta.ua>
USE_CREDENTIALS=True
VALIDATE_CERTS=True
```

5. створити проекту + аплікейшин в Django
```cmd
django-admin startproject site
python manage.py startapp app_main
```

6. налаштовуємо config або залишаємо дефолтним

7. створюємо суперюзера
```cmd
python manage.py migrate
python manage.py createsuperuser
```

8. перший запуск і пеервірка
```cmd
python manage.py runserver
```
* Шлях до застосутнку - http://127.0.0.1:8000/
* Шлях до адмін-панелі - http://127.0.0.1:8000/admin/login
-----------------
# How to?
1. застосовуємо міграцію та сворюємо суперкористувача (адміна)
```cmd
python manage.py migrate
python manage.py createsuperuser
```
1. Виконуємо перший запуск застосунку на перевірку коректності
```cmd
python manage.py runserver
```
1. як створити документацію?
```cmd
cd docs
make html
```

. як згенерувати requirements.txt?
    pip freeze > requirements.txt
    poetry export -f requirements.txt --output requirements.txt --without-hashes

. як встановити модулі із requirements.txt?
    pip freeze > requirements.txt
    poetry export -f requirements.txt --output requirements.txt --without-hashes

. як перевірити встановлені модулі?
    pip freeze > installed_packages.txt
---------------------
## Links
* Шлях до застосутнку
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/about/
    http://127.0.0.1:8000/services/
* Шлях до адмін-панелі - http://127.0.0.1:8000/admin/login
* Шлях до документації - 


# User
viktor
123456


https://github.com/P3TERX/GeoLite.mmdb