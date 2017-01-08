# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
import os

from .base import BASE_DIR


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "fastube", "static"),
]
STATIC_URL = '/static/'
