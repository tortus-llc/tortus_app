import os


from .common import *

# Override environment variables
DEBUG = False

INSTALLED_APPS += [
  'storages',
]

SECRET_KEY = os.environ['SECRET_KEY']

# Postgres
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ['RDS_DB_NAME'],
    'USER': os.environ['RDS_USERNAME'],
    'PASSWORD': os.environ['RDS_PASSWORD'],
    'HOST': os.environ['RDS_HOSTNAME'],
    'PORT': os.environ['RDS_PORT'],
  }
}

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'tortus/static'),
]

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'tortus-assets'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
  'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

DEFAULT_FILE_STORAGE = 'tortus.storage_backends.MediaStorage'
