"""
Django settings for indianNavy project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
#fdfd
import os

import ldap
import os
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# # Baseline configuration.
AUTH_LDAP_SERVER_URI = 'ldap://192.168.0.6/'
AUTH_LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'sudha007'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'ou=users,dc=example,dc=com',
    ldap.SCOPE_SUBTREE,
    '(uid=%(user)s)',
)

## # Or:
AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'

# # Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'ou=groups,ou=groups,dc=example,dc=com',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfNames)',
)
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::megha", AUTH_LDAP_GROUP_SEARCH)

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=django,ou=groups,dc=example,dc=com'
AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=django,ou=groups,dc=example,dc=com'

# # Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}



AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': 'cn=active,ou=django,ou=groups,dc=example,dc=com',
    'is_staff': 'cn=staff,ou=django,ou=groups,dc=example,dc=com',
    'is_superuser': 'cn=superuser,ou=django,ou=groups,dc=example,dc=com',
}
from django_auth_ldap.config import LDAPGroupQuery
AUTH_LDAP_USER_FLAGS_BY_GROUP = {"is_active": "cn=active,ou=groups,dc=example,dc=com",
"is_staff": (LDAPGroupQuery("cn=staff,ou=groups,dc=example,dc=com")| LDAPGroupQuery("cn=admin,ou=groups,dc=example,dc=com")),
"is_superuser": "cn=superuser,ou=groups,dc=example,dc=com",}

# # This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# # Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# # Cache distinguished names and group memberships for an hour to minimize
# # LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# # Keep ModelBackend around for per-user permissions and maybe a local
# # superuser.
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
#from django_auth_ldap.backend import LDAPBackend 


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i13(&sip2@&nr8gdwa7js-zw$0426256p+gpt+-&jrqvk1^ne2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.6','localhost']

#AUTH_USER_MODEL = "users.CustomUser"
#AUTH_USER_MODEL = "users.User"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LOCAL_APPS = [
            'application',
            #'users',
            'acknowledge',
            'blogs',
            'rest_framework',
            'socialSites',
            'othersites',
            'rest_framework.authtoken',

            ]

INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'indianNavy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates','media'],
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

WSGI_APPLICATION = 'indianNavy.wsgi.application'

DATE_INPUT_FORMATS = ("%d-%m-%Y"),
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #   'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'indiannavy',
        # 'USER': 'postgres',
        # 'PASSWORD': 'sudha',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
     }
   
    #'users': {
     #   'NAME': 'users',
      #  'ENGINE': 'django.db.backends.mysql',
       # 'USER': 'root',
        #'PASSWORD': ''
   # }
}

#AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django_auth_ldap.backend.LDAPBackend",
]


PAGINATION_SIZE = 10
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = ""

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#######    Media  ########

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication'
    ),

}
