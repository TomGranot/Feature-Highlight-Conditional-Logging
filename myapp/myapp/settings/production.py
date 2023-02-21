from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '*.myapp.dev',
    '127.0.0.1',
    'localhost',
    '0.0.0.0',    
    ]

# allow CIDR
ALLOWED_CIDR_NETS = ['10.0.0.0/8']

MIDDLEWARE = [
    'allow_cidr.middleware.AllowCIDRMiddleware', # django allow CIDR middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = os.environ['DATABASE_PORT']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

BASE_URL = 'https://myapp.dev'


# templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request', # for django allauth
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],            
        },
    },
]


# When the automatic setup is used, the Debug Toolbar is not compatible with GZipMiddleware. Please disable that middleware during development or use the explicit setup to allow the toolbar to function properly.
MIDDLEWARE += [
    'django.middleware.gzip.GZipMiddleware',
]

# cache
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"
KEY_PREFIX = "myapp_"

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 			
CACHE_MIDDLEWARE_KEY_PREFIX = ''

CACHES = {
    "default": { 
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + os.environ['REDIS_HOST'] + ":" + os.environ['REDIS_PORT'] + "/" + os.environ['REDIS_DB'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,  # Use the latest protocol version
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            # "SOCKET_TIMEOUT": 5,  # in seconds
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10000, "retry_on_timeout": True},
        },
    },
    "disk": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, 'cache'),
        "KEY_PREFIX": "myapp_",
        "TIMEOUT": 3600*24*7, # one hour * 24 hours * 7 days (in seconds)
        "LOCATION": "/var/tmp/django_cache",
    }    
}









import sys
import lightrun
try:
    if os.environ.get('RUN_MAIN') or '--noreload' in sys.argv:
        import lightrun
        lightrun.enable(
            company_key="ae4f9fec-4174-4e17-b662-3618bdb7b595",
            metadata_registration_tags='[{"name": "prod"}]'
        )

except ImportError as e:
    print("Error importing Lightrun: ", e)