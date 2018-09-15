# elifin-okuzu - http://142.93.167.4:400/
**********************************************************************************************************************
*                                       Etymological dictionary software                                             *
**********************************************************************************************************************
INSTALLATION
 
First of all install virtual environment for your PC 
 (for Windows you need to download virtualenv: check http://pip.readthedocs.io/en/stable/installing/#do-i-need-to-install-pip)
```
apt-get install python3-pip
pip3 install virtualenv
```

Create a folder for your virtual environment
```
mkdir env
cd env
virtualenv myenv
```

Activate your virtual environment
```
FOR LINUX:
source myenv/bin/activate

FOR WINDOWS:
myvenv/Scripts/activate
```

To install requirements for project go to base folder which has requirements.txt in it, open terminal and type
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

On your base file (\elifinokuzu\) open terminal and type the followings:

```
 python manage.py makemigrations                  (to making migretions ready for database to pull)
 python manage.py migrate                         (to migrate ready migrations)
 python manage.py migrate --run-syncdb            (to create SQL tables if there is a problem)
```

Create a super user
```
python manage.py createsuperuser
```

run server
```
python manage.py runserver
```
