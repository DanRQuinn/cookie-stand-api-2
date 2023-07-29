# cookie-stand-api-2

## collaberators

Athony walked me through this entire repo after I restarted 3 different times. They will be nearly identical as when I was making my own repo they would break everytime. He is very aware that I'm using his and spend hours with me over the weekend walking me through it

## setup

- <http://localhost:8000>

- docker compose up --build

- username: admin

- password: admin

## Customization Steps for using template

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `cookie_stands` folder to the app name of your choice
- Search through entire code base for `Cookie`,`Cookies` and `cookies` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update ThingModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`

Template Project for starting up CRUD API with Django Rest Framework
