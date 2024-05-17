from pathlib import Path
import os
from datetime import timedelta
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*=x5#a_e8at@yrvp0nmz=3*rkyc^2s(_24b*+pr)=_y6vyaxnr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['new-arts-api.onrender.com', '127.0.0.1', 'localhost','https://artstraining.co.uk/' ]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # created apps
    'registration',
    'courses',
    'assessments',

    # installed apps
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'social.apps.django_app.default',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    # 'paypal.standard.ipn',
    # 'paypalrestsdk'
    # 'stripe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'new_arts_api.urls'
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = ['*']

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

WSGI_APPLICATION = 'new_arts_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'new_arts_websiteDB',         # Name of your PostgreSQL database
#         'USER': 'ekenehanson',         # PostgreSQL username
#         'PASSWORD': '1234567890qwerty1234567890',
#         'HOST': '92.205.171.87',        
#         'PORT': '3306',   
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',         # Name of your PostgreSQL database
#         'USER': 'postgres',         # PostgreSQL username
#         'PASSWORD': 'TlASehOdbdRvCLQuMVjxMGBcYXJoCrKX',
#         'HOST': 'monorail.proxy.rlwy.net',        
#         'PORT': '26160',   
#     }
# }

# DATABASES['default'] = dj_database_url.parse('postgres://new_arts_db_sp4n_user:7w8poglw6KyM6DNTn73cQkF8ETdFOXgr@dpg-cosd3na0si5c739tgmg0-a.oregon-postgres.render.com/new_arts_db_sp4n')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

AUTH_USER_MODEL = 'registration.CustomUser'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),

    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# # Email configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server address
# EMAIL_PORT = 587  # Your SMTP server port (587 is the default for SMTP with TLS)
# EMAIL_USE_TLS = True  # Whether to use TLS (True by default)
# EMAIL_HOST_USER = 'ekenehanson@gmail.com'  # Your email address
# EMAIL_HOST_PASSWORD = 'pduw cpmw dgoq adrp'  # Your email password or app-specific password if using Gmail, etc.
# DEFAULT_FROM_EMAIL = 'ekenehanson@gmail.com'  # The default email address to use for sending emails
# EMAIL_DEBUG = True

# # Email configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.office365.com'  # Your SMTP server address
# EMAIL_PORT = 58  # Your SMTP server port (587 is the default for SMTP with TLS)
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = 'ekenehanson@gmail.com'  # Your email address
# EMAIL_HOST_PASSWORD = 'yjmglxzktxbgaxsp'  # Your email password or app-specific password if using Gmail, etc.
# DEFAULT_FROM_EMAIL = 'ekenehanson@gmail.com'  # The default email address to use for sending emails
# EMAIL_DEBUG = True


#Your new code is 4PSC6-34552-TCL2Y-X7U9V-M5QQ


# # # Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server address
EMAIL_PORT = 465  # Your SMTP server port (587 is the default for SMTP with TLS)
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'training.arts.co.uk@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'docg qver jlgv ywyy'  # Your email password or app-specific password if using Gmail, etc.
DEFAULT_FROM_EMAIL = 'training.arts.co.uk@gmail.com'  # The default email address to use for sending emails
EMAIL_DEBUG = True

# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtpout.secureserver.net'
# EMAIL_PORT=465
# EMAIL_USE_SSL=True
# EMAIL_USE_TLS=False
# EMAIL_HOST_USER='training@artstraining.co.uk'
# EMAIL_HOST_PASSWORD='%EBpd76ZrhUC'
# ADMIN_EMAIL='training@artstraining.co.uk'
#EMail Password: %EBpd76ZrhUC
#gvgmufyo4pr7
#bVv$%09eY7#n
# sendgrid Rovery Code: LXKNM2FGV9LFC98NXBTH21GW


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Strict'




