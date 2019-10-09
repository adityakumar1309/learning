mod wsgi = apache module that connects wsgi application of python like django etc

sudo a2enmod wsgi - enables the mod wsgi

wsgi.py = has projects settings path

app.conf (inside apache)

declare port

we need to declare static path of django project

we need to point to application path and python path

wsgi.py path 

https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04

