# wecodeit.academy
## setup

```
# create a python3 virtualenv
virtualenv -p python3 venv

# activate the venv
source venv/bin/activate

# install all the requirements
pip install -r requirements.txt

# run migrations like (will also create a sqlite database file)
python3 django-sites/manage.py migrate

# create a super user
python3 django-sites/manage.py createsuperuser

# start the dev server
python3 django-sites/manage.py runserver 

# login with the superuser and create your own database entries on:
http://127.0.0.1:8000/admin 
```