# Create Virtual Environment

`virtualenv venv`

# Activate Virtual Environment

Mac, Linux:

`source venv/bin/activate`

Windows

`venv\Scripts\activate`

# Installation 

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

# Load Example Data

1) `python manage.py add_users`

Mac, Linux:

2) `python manage.py loaddata data/main/*.json`

Windows:

2) `python manage.py add_fixtures data\main\`

Run Server

`python manage.py runserver`

# deactivate venv

`deactivate`
