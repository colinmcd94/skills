# Django settings for skills project.

import os

BASE_URL = ""

try:
    
    import sys, os
    sys.path.append(os.path.abspath('/Users/colinmcd94/Documents/Programs/Django/extras'))
    import locals
    DATABASES = locals.DATABASES
    STATIC_ROOT = '/Users/colinmcd94/Documents/Programs/Django/extras/static'
    DEBUG = True
    MEDIA_ROOT =  '/Users/colinmcd94/Documents/Programs/Django/extras/media'
    MEDIA_URL = "/static/"

except:

    DEBUG = False
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'colinmcd+skills',
        'OPTIONS': {
            'read_default_file' : os.path.expanduser('~/.my.cnf'),
            },
        'PORT': '',                      # Set to empty string for default. Notused with sqlite3.
        }

    }
    TEST_SETTING = 'Dev try statement failed'
    STATIC_ROOT = '/mit/colinmcd/web_scripts/skills/static'
    MEDIA_ROOT = '/mit/colinmcd/web_scripts/skills/static/img'
    MEDIA_URL = "/media/"

TEMPLATE_DEBUG = DEBUG

SERVE_MEDIA = True

ADMINS = (
    ('colinmcd', 'colinmcd@mit.edu'),
)

MANAGERS = ADMINS


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

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

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = '/mit/colinmcd/web_scripts/skills/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/skills/static/'

# URL used when user is redirected to login screen
LOGIN_REDIRECT_URL = "/"

LOGIN_URL = "/"

# Additional locations of static files
STATICFILES_DIRS = (
    'static/',
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
SECRET_KEY = 'wjx$6(72=07n1!rpcndfa1%dqc)^s1dhabh_xx6d82a%hl7x81'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'skills.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'skills.wsgi.application'

AUTH_PROFILE_MODULE="userapp.NewUserProfile"
DJANGO_SETTINGS_MODULE='skills.settings'
TEMPLATE_DIRS = (
    'templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.admindocs',
#    'practice',
    'south',
    'userapp',
    'skillapp',
    'messageapp',

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


