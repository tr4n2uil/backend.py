export DJANGO_SETTINGS_MODULE="core.server"
uwsgi --stop /tmp/deltaturtle-poc.pid
uwsgi --ini uwsgi.ini
