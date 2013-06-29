THUMBNAIL_FORMAT = "PNG"

INSTALLED_APPS = (
  'grappelli',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
)

try:
  import south
  INSTALLED_APPS += ('south',)
except ImportError:
  pass