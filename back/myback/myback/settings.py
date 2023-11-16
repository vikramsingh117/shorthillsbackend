import os
from pathlib import Path
import cloudinary
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
cloudinary.config(
    cloud_name="dqjru6fzb",
    api_key="146611421282597",
    api_secret="JJB3ikvpDliBoq8R_lKjSw5rezA",
)
    
# settings.py

CLOUDINARY = {
    'cloud_name': 'dqjru6fzb',
    'api_key': '146611421282597',
    'api_secret': 'JJB3ikvpDliBoq8R_lKjSw5rezA',
}

    
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1i&3b0u3ni^jztk4na=)23y-4gbd_eh8)%gq$lvinmk+=)j&fj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'camp',


]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
CORS_ALLOW_ALL_ORIGINS = True


# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'http://localhost:3000/input/',
#     'http://localhost:8000/api/api/submit/',
#     'http://localhost:8000/',
#     'http://localhost:8000/api/add-product/',
    
# ]

ROOT_URLCONF = 'myback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'myback.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crud',
        'USER': 'root',
        'PASSWORD': 'Vikram 121',
        'HOST': 'localhost',  
        'PORT': '3306',       
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())