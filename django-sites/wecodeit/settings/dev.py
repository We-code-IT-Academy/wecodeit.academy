from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o#w^h(pwe!rer)3vwl@7(^!2$6_-!$+kzt1ygq=g7l4u9e4(j('

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    # ...
    'django_extensions',
]


try:
    from .local import *
except ImportError:
    pass
