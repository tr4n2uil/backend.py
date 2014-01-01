export DJANGO_SETTINGS_MODULE="demo.server"
uwsgi --stop /tmp/backend.pid
uwsgi --ini uwsgi.ini
