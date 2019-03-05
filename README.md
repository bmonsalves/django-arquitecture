# django-arquitecture

### install
    pip3 install -r requirements.txt

### .env
crear archivo .env en la raiz del proyecto

    SECRET_KEY=<secret_key>
    STATIC_URL=/static/
    DEBUG=True
    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_NAME=<database name>
    DATABASE_USER=<database username>
    DATABASE_PASSWORD=<database password>
    DATABASE_HOST=<host>
    DATABASE_PORT=<port>

### migrate
    python3 manage.py makemigrations
    python3 manage.py migrate