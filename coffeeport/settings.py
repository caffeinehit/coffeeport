# Django settings for coffeeport project.
import dj_database_url, os

DEBUG = os.environ.get('DEBUG', False) == 'True'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    os.environ.get('ADMINS', 'No One!example@example.com').split('!'),
)

MANAGERS = ADMINS

# Default database URL is a local SQLite instance
DATABASE_URL = 'sqlite:///{}'.format(os.path.join(os.path.dirname(__file__), 'db.sqlite'))

DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', default=DATABASE_URL),
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = os.environ.get('TIME_ZONE', 'Europe/London')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-gb')

SITE_ID = int(os.environ.get('SITE_ID', 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = os.environ.get('USE_I18N', True) == True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = os.environ.get('USE_L10N', True) == True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = os.environ.get('USE_TZ', True) == True

# The media storage backend used by this application. Override to
# upload to S3 in production for example.
DEFAULT_FILE_STORAGE = os.environ.get(
    'DEFAULT_FILE_STORAGE',
    'django.core.files.storage.FileSystemStorage')

# The static assets storage backend used by this application when
# invoking `collectstatic`. Override to upload to S3 in production for
# example.
STATICFILES_STORAGE = os.environ.get(
    'STATICFILES_STORAGE',
    'django.contrib.staticfiles.storage.StaticFilesStorage')


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.environ.get('MEDIA_ROOT',
                            os.path.join(os.path.dirname(__file__), 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.environ.get('STATIC_ROOT',
                             os.path.join(os.path.dirname(__file__), 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY', 'hmvnn6cvc2zjcc@*o#k1wfn9df79s&ek&v2^v9l_zf@$!1ru&3')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'coffeeport.urls')

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = os.environ.get('WSGI_APPLICATION',
                                  'coffeeport.wsgi.application')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'gunicorn',
    'rest_framework',
    'coffeeport.app',
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

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 25))
EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', '[Django] ')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'False') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'coffeeport.herokuapp.com'
    ]
