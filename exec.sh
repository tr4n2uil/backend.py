export DJANGO_SETTINGS_MODULE="core.server"
uwsgi --ini uwsgi.ini
service nginx start
