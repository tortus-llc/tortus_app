from .common import *

# Override environment variables
SECRET_KEY = 'e85&&l8x!fd4(%5!86wp-pc!#exc3-axx!69qq=jlmm26_(wos'

DEBUG = False

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
