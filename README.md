# Project setup

Create a new Python environment

```shell
python -m venv env
```

Activate the newly created Python environment (Windows)

```shell
source env/Scripts/activate
```

Activate the newly created Python environment (Ubuntu / Mac)

```shell
source env/Scripts/activate
```

Install Python Poetry using the docs at [https://python-poetry.org/](https://python-poetry.org/docs/#installing-with-the-official-installer)

```shell
curl -sSL https://install.python-poetry.org | python -

Test if Poetry is installed

```shell
poetry --version
```

Initialize Poetry using MIT license

```shell
poetry init
```

Add a few essential packages (Windows)

```shell
poetry add django djangorestframework psycopg2 django-filter
```

Add a few essential packages (Ubuntu / Mac)

```shell
poetry add django djangorestframework psycopg2 django-filter
```

Install required packages

```shell
poetry install
```

Create `/core`` folder in project folder and set up the Django main folder in the `/core`

```shell
django-admin startproject config .
```
Modify `/core/manage.py`

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.project.settings")
```

Modify `/core/config/settings.py`

```python
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_URLCONF = "core.project.urls"
WSGI_APPLICATION = "core.project.wsgi.application"
```

Add split settings package
```shell
poetry add django-split-settings PyYAML
```

Copy developer settings
```shell
mkdir -p local
cp core/config/settings/templates/settings.dev.py ./local/settings.dev.py
```

Add two development packages
```shell
poetry add -D flake8
poetry add -D pre-commit
poetry run pre-commit sample-config
poetry run pre-commit install
poetry run pre-commit run --all-files
poetry run pre-commit uninstall
poetry run pre-commit install
```

Modify Makefile to have pre-commit commands

**AWS**
bucket_name=farrokhtala-backend
secret_key=AKIATSXJHY4PHDMVYTGH
jtbdPfXIoQRFfmk5oJEdd7McSisnEtZCHFcb3FNg
ip = 54.218.28.41
