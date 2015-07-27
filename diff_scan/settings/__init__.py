import os, sys, re, socket
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = 'uploads'

DEBUG = TEMPLATE_DEBUG = True
ADMINS = MANAGERS = (
)

MEDIA_ROOT = os.path.join(BASE_DIR,'.media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR,'.static/')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
)

LESS_EXECUTABLE = 'lessc'
COMPRESS_PRECOMPILERS = (('text/less', 'lessc {infile} {outfile}'),)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
)
STATICFILES_DIRS = ()
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR,'main/webfront.db'),
  }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = USE_L10N = USE_TZ = True

ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'
SECRET_KEY = '5i4*stnx^12a+wow1_lrz(jb!d*e^tkzq+t8o)_5f-2$n9k*@a'

from .apps import *

# Import a setting file naed after hostname
try:
  istr = 'settings.' + re.sub('[^A-z0-9._]', '_', socket.gethostname())
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

