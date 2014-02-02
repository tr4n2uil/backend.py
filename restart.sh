export DJANGO_SETTINGS_MODULE="core.server"
uwsgi --stop /tmp/backend.pid
uwsgi --ini uwsgi.ini
