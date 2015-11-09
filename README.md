# ecs160web

Setting up apache:

Run the following commands:

sudo apt-get install python-pip  
sudo apt-get install python-dev  
pip install PIL  --allow-unverified PIL --allow-all-external  
sudo pip install django django-cms  
sudo apt-get install libapache2-mod-wsgi  
sudo pip install django-simple-email-confirmation to install the necessary email verification app.    
sudo pip install django-widget-tweaks to install the dependencies for the forms.  
sudo pip install django-celery for the celery schedule  


Modify /etc/apache2/apache2.conf to be the same as the apache2.conf in the repository, substituting your koding username for my apmishra100

Modify /etc/apache2/sites-enabled/000-default.conf to be the same as the 000-default.conf in the repository substituting your koding username for my apmishra100.

Replace apmishra100 with your username in ecs160/ecs160/settings.py
---
Setting up messaging

Change directories to the django-messages directory located within the ecs160 project folder and run:  
  sudo python setup.py install  
---
python ~/ecs160/manage.py collectstatic

sudo apachectl restart

Visit username.koding.io and you should be able to view the website




