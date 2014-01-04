# Backend settings for demo project.
import os, sys
os.environ['LANG'] = 'en_US.UTF-8'

ROOT = os.path.dirname( os.path.abspath( __file__ ) )
BACKEND = ROOT + '/../../'
sys.path.append( BACKEND + 'src' )
sys.path.append( BACKEND + 'lib/django_avatar' )


ROOTPATH = 'http://127.0.0.1:8000'
SESSION_COOKIE_DOMAIN = '127.0.0.1'


# Django settings for demo project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'backend',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'krishna',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ROOT + '/../drive/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/drive/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/ui/'

# Additional locations of static files
STATICFILES_DIRS = (
    ROOT + '/../ui/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rc(3sut%cs%qdn+7+t7w%u$%uqb%c0*hk54y3x82^oupm4l5f+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    (
        'pyjade.ext.django.Loader',
        (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            #'django.template.loaders.eggs.Loader',
        )
    ),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ROOT + '/../tpl/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'avatar',
    'social.apps.django_app.default',
    'fs',
    'util',
    'apps.profile',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'util.settings_context_processor.add_settings',
    #'social.apps.django_app.context_processors.backends',
    #'social.apps.django_app.context_processors.login_redirect',
)


DEFAULT_FROM_EMAIL = 'Sample Email <demo@adhyayan.org.in>'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'demo@adhyayan.org.in'
EMAIL_HOST_PASSWORD = 'sampledemo'
EMAIL_USE_TLS = True


AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    #'social.backends.open_id.OpenIdAuth',
    #'social.backends.google.GoogleOpenId',
    #'social.backends.google.GoogleOAuth',
    #'social.backends.twitter.TwitterOAuth',
    #'social.backends.yahoo.YahooOpenId',
    
    #'django.contrib.auth.backends.ModelBackend',
)


LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_REQUIRED_REDIRECT = '/login/?next=%s'

AUTH_PROFILE_MODULE = 'apps.UserData'

AVATAR_GRAVATAR_BACKUP = True
AVATAR_GRAVATAR_DEFAULT = 'http://vibhaj.com/ui/letters/%(letter)s.png'
AVATAR_DEFAULT_URL = '/ui/lib/letters/%(letter)s.png'


STG_KB = 1024
STG_MB = 1048576
STG_GB = 1073741824
STG_TB = 1099511627776

AVATAR_MAX_SIZE = 10 * STG_MB
STG_USER = 500 * STG_MB

MAP_FILE = {
    'flv': 'Video',
    'mp4': 'Video',
    'aac': 'Video',
    'mp3': 'Video',
    'ppt': 'Sides',
    'pptx': 'Slides',
    'png': 'Image',
    'jpg': 'Image',
    'jpeg': 'Image'
}


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


PERSON_RESET_SUBJECT = 'Demo - Verify Company'
PERSON_RESET_BODY = 'Hello %(name)s,\n\nPlease use the following link to verify company on demo:\n\n%(rootpath)s/verify/%(password)s/\n\n\nRegards,\nTeam Backend\n\n'

PAGE_DEFAULT = 15

# social api keys
SOCIAL_AUTH_SLUGIFY_USERNAMES = False
SOCIAL_AUTH_UUID_LENGTH = 0

SOCIAL_AUTH_FACEBOOK_KEY = '189445084592792'
SOCIAL_AUTH_FACEBOOK_SECRET = '5cbaae479621145a23eec8612acedf68'
SOCIAL_AUTH_FACEBOOK_SCOPE = [ 'email', 'friend_list' ]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '531768047342-309n41kf7db4gr2r43gu8p2250v0otqc.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '64DH1H0K4IJcayMBow5pANsz'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [ 'email', 'profile' ]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    # 'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
