cardiologytrials
================

Code for the cardiologytrials.org Django-powered website

This was my first Django projecting and looking back on it it's appropriately dirty and inefficient. However, it works well.

Things you will need to do

1. Set up an Apache webserver (or whatever webserver you wish; or skip this and use the Django runserver during development - THIS IS HIGHLY ADVISABLE IF YOU ARE NEW TO DJANGO AS THE RUNSERVER'S DEBUG IS MUCH EASIER TO INTERPRET AND YOU DON'T NEED TO KEEP RESTARTING APACHE EVERY 30 SECONDS WHILST YOU CHANGE FILES!)

2. Install Django (and configure the werbserver appropriate - see the Django documentation)

NB for ease of use I've included the relevant code from my /etc/httpd/conf/extra/httpd-vhosts.conf to get the site working with the supplied django.wsgi & wsgi_app.py files:

   <VirtualHost *:80>
      ServerAdmin cardiologytrials_apache@jph.am
      DocumentRoot "/home/james/sites/cardiologytrials.org/www"
      ServerName cardiologytrials.org
      ServerAlias cardiologytrials.org www.cardiologytrials.org
       ErrorLog "/var/log/httpd/cardiologytrials.org-error_log"
       CustomLog "/var/log/httpd/cardiologytrials.org" combined
       <Directory /home/james/sites/cardiologytrials.org/www/>
                       DirectoryIndex index.php index.htm index.html
                       AddHandler cgi-script .cgi .pl
                       Options ExecCGI Indexes FollowSymLinks MultiViews +Includes
                       AllowOverride None
                       Order allow,deny
                       allow from all
           </Directory>
   
       <Directory /home/james/sites/cardiologytrials.org/>
           Order allow,deny
           Allow from all
       </Directory>
   
       Alias /static/ /home/james/sites/cardiologytrials.org/www/
       WSGIScriptAlias / /home/james/sites/cardiologytrials.org/django.wsgi/
       WSGIScriptAlias /wsgi_app /home/james/sites/cardiologytrials.org/wsgi_app.py
   </VirtualHost>

Obviously you'll need to change the absolute paths to the directories

3. Either create a django project and then an application - necessary to set up users etc. and create your database file.

4. Copy all the files from this repository into their appropriate locations, e.g. /django_cardiologytrials/django_cardiologytrials/ will become /<yourprojectname>/<yourprojectname>/; /django_cardiologytrials/traislapp/ will become /<yourprojectname>/<yourappname>/ 

4. Alter the settings.py file - not much should need changing except changing the name of the app in the INSTALLED_APPS = () list (from 'trialsapp') and the absolute paths e.g. to the database.

5. Change the views.py and urls.py (and maybe some others, I can't remember) at the top so they stop trying to import e.g. "from trialsapp.feeds import AllTrialsFeed" (urls.py), "from trialsapp.models import Trial,Topic" (views.py), instead inport "from <yourapp>.whatever..."

6. Take a look at the models.py file to see how it works:
There are 5 models; the first 4 correspond exactly to the first 4 columns on the website (Topic=Topic; Therapy=Therapy group; Intervention=Therapy; Trial=Trial) - sorry about the confusing names regarding the middle two, I redesigned the site but couldn't be bothered changing the database - do so if you wish.
The last model - Papers - refer to actual papers in press. Remember each trial can have multiple papers (different endpoints, different subgroups, different follow-ups), so we need to be able to add multiple papers.

7. The site should be working now - either use the Django runserver or restart Apache (or whatever you use).

8. Go to http://<whatever>/admin and start adding your columns.
You need to add the columns in left to right. More left-sided columns can be added later, but the parent e.g. topic needs to exist before the children therapies etc. can be added.
When you add a therapy, select the Topic(s) it should be listed under (you can select multiple using control-clicking). Do this for Interventions and Trials, too. Then add paper(s) for each trial.

9. Access the website's root directory and ensure it's able to output some data.

10. Change how the site looks by altering the files in the /<projectname>/templates directory/<appname>/

11. To allow selection of the specific topics e.g. via http://cardiologytrials.org/acs/ you need to set up the regex in the /<projectname>/urls.py file, and the corresponding function in the /<yourapp>/views.py

It maybe might work now? Who knows. This is a crap guide but hopefully it's enough for you to be able to figure out how to get it working.
