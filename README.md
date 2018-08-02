# elifin-okuzu
***************************************************************************************************************************
*                                          Etymological dictionary software                                               *
***************************************************************************************************************************
 INSTALLATION
 
 to install requirements for project go to base folder which has requirements.txt, open terminal and type
 ```
 pip install -r requirements.txt
 ```
 
 After you done with installing requirements go to folder where setting.py is (\elifinokuzu\elifinokuzu) and create local_settings.py file it should include:
  
 ```
SECRET_KEY = 'INSERT YOUR SECRET_KEY HERE'
ALLOWED_HOSTS = []
DEBUG = True
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}
```
(You can create your own SECRET_KEY on https://www.miniwebtool.com/django-secret-key-generator/)

Then on your base file (\elifinokuzu\) open termaninal and type the followings:

```
 python manage.py makemigrations                  (to making migretions ready for database to pull)
 python manage.py migrate                         (to migrate ready migrations)
 python manage.py migrate --run-syncdb            (to create SQL tables if there is a problem)
```
