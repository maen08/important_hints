# by myself 

# first stage
>git push -u origin master
>heroku login 
>heroku create HereDomainName
>hahahahah !!
connect the project with git and github (have the master access).that is after push the project 
to the repo then push the repo to heroku ie > git push heroku master.
make sure you have the required packages:
-gunicorn
-whitenoise(if you'll choose to)
-psycopg2
-dj_database_url
-django-heroku (very crucial)
 
and important files:
-Procfile, in there:   web: gunicorn nameofyourproject.wsgi:application


# second stage
in settings.py (special for dj_database_url and django-heroku):
import django_heroku
import env (this is the module for env. variables, ie. env.py)
import dj_database_url

SECRET_KEY = env.SECRET_KEY  (plus other env. variables)
'whitenoise.middleware.WhiteNoiseMiddleware'
ALLOWED_HOSTS = ['127.0.0.1', 'yourdomain.herokuapp.com'] #you get it in >heroku create HereDomainName
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# very important for db  (at the bottom):
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())


# third stage

debugging is an unavoidable process...hahah!
nothing easy boi

by 
@maen
@ioi










