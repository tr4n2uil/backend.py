export DJANGO_SETTINGS_MODULE="demo.server"
uwsgi --ini uwsgi.ini
service nginx start
