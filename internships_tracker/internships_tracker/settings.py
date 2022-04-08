"""
Django settings for internships_tracker project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django_auth_ldap.config import LDAPSearch
# from django.utils.translation import get_language
import os
import ldap
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "internships_app",
    "carrier",
    "supervisor",
    "applicant",
    "secretary",
    "crispy_forms",
    "phonenumber_field",
    "dal",
    "dal_select2",
    "bootstrap5",
    "bootstrapform",
    "django_bootstrap_icons",
    "django_filters",
]
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "internships_tracker.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

LOGIN_REDIRECT_URL = "internships_app:redirect_base"  # equals '/'
LOGOUT_REDIRECT_URL = "home"  # equals '/'
WSGI_APPLICATION = "internships_tracker.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_DATABASE_NAME"),
        "USER": env("DB_USERNAME"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT", default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# auth django
AUTH_USER_MODEL = 'internships_app.User'
AUTHENTICATION_BACKENDS = [
    "internships_app.backends.EmailBackend", "django_auth_ldap.backend.LDAPBackend"]
AUTH_LDAP_SERVER_URI = env('AUTH_LDAP_SERVER_URI')
AUTH_LDAP_BIND_DN = env('AUTH_LDAP_BIND_DN')
AUTH_LDAP_BIND_PASSWORD = env('AUTH_LDAP_BIND_PASSWORD')
AUTH_LDAP_START_TLS = env('AUTH_LDAP_START_TLS') == 'True'
AUTH_LDAP_BASE_DN = env('AUTH_LDAP_BASE_DN')
AUTH_LDAP_USER_SEARCH_ATTR = env('AUTH_LDAP_USER_SEARCH_ATTR')
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    AUTH_LDAP_BASE_DN,
    ldap.SCOPE_SUBTREE,
    "(" + AUTH_LDAP_USER_SEARCH_ATTR + "=%(user)s)"
)
AUTH_LDAP_SN = env('AUTH_LDAP_SN')
AUTH_LDAP_EMAIL = env('AUTH_LDAP_EMAIL')
AUTH_LDAP_TITLE = env('AUTH_LDAP_TITLE')
AUTH_LDAP_DEPARTMENT = env('AUTH_LDAP_DEPARTMENT')
AUTH_LDAP_GIVEN_NAME = env('AUTH_LDAP_GIVEN_NAME')
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": AUTH_LDAP_GIVEN_NAME,
    "last_name": AUTH_LDAP_SN,
    "email": AUTH_LDAP_EMAIL,
    'uni_department': AUTH_LDAP_DEPARTMENT,
    'title': AUTH_LDAP_TITLE
}
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=django,ou=people,dc=hua,dc=gr",
#     "is_staff": "cn=staff,ou=django,ou=people,dc=hua,dc=gr",
#     "is_superuser": "cn=superuser,ou=people,ou=groups,dc=hua,dc=gr",
# }
AUTH_LDAP_INTERNAL_DOMAIN = env('AUTH_LDAP_INTERNAL_DOMAIN')

# logging in internships app
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/django_app.log',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django_auth_ldap': {
            'level': 'DEBUG',
            'handlers': ['file', 'console']
        },
        'huaskel': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
