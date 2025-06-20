from toastmaster.settings import env

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

SECRET_KEY = env("SECRET_KEY", default="")

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authtools.User'

# Default settings for the application
WSGI_APPLICATION = 'toastmaster.wsgi.application'
ALLOWED_HOSTS = []
ROOT_URLCONF = 'toastmaster.urls'