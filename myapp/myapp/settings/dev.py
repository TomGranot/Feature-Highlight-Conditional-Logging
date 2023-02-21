from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass


INSTALLED_APPS += [
    'debug_toolbar',
]



INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")
def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_currentuser.middleware.ThreadLocalUserMiddleware', # current user
    'debug_toolbar.middleware.DebugToolbarMiddleware',        
]



import sys
import lightrun
try:
    if os.environ.get('RUN_MAIN') or '--noreload' in sys.argv:
        import lightrun
        lightrun.enable(
            company_key=os.environ.get('LIGHTRUN_COMPANY_KEY'),
            metadata_registration_tags='[{"name": "dev"}]'
        )

except ImportError as e:
    print("Error importing Lightrun: ", e)

SITE_ID = 2