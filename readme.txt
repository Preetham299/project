#install python 
#install django  -- pip install django
#create a server on django ---django-admin startproject server ( server is name of the django project)
#go into the server repo -- cd server
#check for the derver is working on the port or not -- python manage.py runserver ( http://127.0.0.1:8000/) it should run here by ddefault
#ctrl + c to keep the server down.
#now create a application(module) which hold attribute of one of your component of the whole project. many applications can be handeled by standalone server.
# create app using manage.py file -- pyhton manage.py startapp content_manager
#append(app_name) the app name into the server/settings.py file to get handeled by server with out any explicit configurations.
# --created_apps=['content_manager']
# --NSTALLED_APPS=INSTALLED_APPS+created_apps

#create a file urls.py at contenet_manager/
#include content_manager/urls.py file urls into server/urls.py  in url patterns...
# --from django.urls import include
# --path('', include('content_manager.urls'))


#create a templates folder in your app to connect with front-end 


#open models.py in contact_manager
'''
from django.db import models

# Table 1: User
class User(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Table 2: Contact
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.phone_no}"
'''
# here is the code to create tables required to manage the contacts and data of users...

# and make the table run and create in db using
# --python manage.py makemigrations
# --python manage.py migrate

#in template write html code (interface)
#views.py is used for main logic and register approptiate functions in urls to make sure communicate efficiently in backside data routing




