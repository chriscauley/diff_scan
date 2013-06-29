import os, sys, re, socket
SPATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '..')) # directory containing settings/
PPATH = os.path.join(SPATH,"..") # project root
UPLOAD_DIR = 'uploads'

DEBUG = TEMPLATE_DEBUG = True
ADMINS = MANAGERS = (
)

MEDIA_ROOT = os.path.join(PPATH,'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PPATH,'static/')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_DIRS = (os.path.join(SPATH,'templates'),)
STATICFILES_DIRS = ()
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(PPATH,'webfront/webfront.db'),
  }
}
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

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = USE_L10N = USE_TZ = True

ROOT_URLCONF = 'webfront.urls'
WSGI_APPLICATION = 'webfront.wsgi.application'
SECRET_KEY = '5i4*stnx^12a+wow1_lrz(jb!d*e^tkzq+t8o)_5f-2$n9k*@a'

# Remove characters that are invalid for python modules.
machine = re.sub('[^A-z0-9._]', '_', socket.gethostname())
try:
  istr = 'settings.' + machine
  tmp = __import__(istr)
  mod = sys.modules[istr]
except ImportError:
  print "No %r module found for this machine" % istr
else:
  for setting in dir(mod):
    if setting == setting.upper():
      setattr(sys.modules[__name__], setting, getattr(mod, setting))

try:
  from local_settings import *
except ImportError:
  pass

from .apps import *