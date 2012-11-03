import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

ACCOUNT_ACTIVATION_DAYS = 7

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_db',                      # Or path to database file if using sqlite3.
        'USER': os.environ.get('PG_USER',None),                      # Not used with sqlite3.
        'PASSWORD': os.environ.get('PG_PASSWORD', None),                  # Not used with sqlite3.
     #   'HOST': '198.151.130.98',                      # Set to empty string for localhost. Not used with sqlite3.
          'HOST': '',
           'PORT': '',
    #    'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = './media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = './Home/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://localhost:8000/static/'

MEDIA_BUNDLES = (
    ('style.css',
        'css/style.css',
        
    ),
    ('login.css',
        'css/login.css',
    ),
    ('registration.css',
        'css/registration.css',
    ),
    ('style1.css',
        'css/style1.css',
    ),

    ('prettyPhoto.css',
         'prettyPhoto/css/prettyPhoto.css',
    ),
    ('slide.css',
        'css/slide.css'
    ),
    ('slide.js', 
        'js/slide.js'
    ),
    ('jquery.js',
        'js/jquery.js'
    ),
    ('jquery.prettyPhoto.js',
        'prettyPhoto/js/jquery.prettyPhoto.js'
    ),
    ('swfobject.js',
        'slideshow/js/swfobject/swfobject.js'
    ),
    ('custom.js',
        'js/custom.js'
    ),
    ('backbone.js',
        'js/backbone-0.5.3.min.js'
    ),
    ('960.css',
        'css/960.css'
    ),
    ('app.js',
        'js/app.js'
    ),
    ('ICanHaz.js',
        'js/ICanHaz.js'
    ),
    ('backbone-tastypie.js',
        'js/backbone-tastypie.js'
    ),
    ('underscore.js',
        'js/underscore-1.3.0.min.js'
    ),
    ('forms.js',
       'js/forms.js'
    )
)
# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

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
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lw&!-o_8sqv@2#ew80r)&@pbv7(3e0bqu6(h(nf+es%8is$c$e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'mediagenerator.middleware.MediaMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django-crossdomainxhr-middleware.XsSharing',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
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
    'django.contrib.admin',
    'mediagenerator',
    # 'django.contrib.admindocs',
    'apps.calendar',
   # 'tastypie',
    'piston',
    'registration',
)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST',None)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER',None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD',None)
EMAIL_PORT = os.environ.gAUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

ROOT_MEDIA_FILTERS = {
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = 'compress/yuicompressor-2.4.7.jar'

