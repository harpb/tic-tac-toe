import os
import sys
import settings
import socket
import logging
logger = logging.getLogger(__name__)

def set_local():
    pass

def set_debug():
    settings.DEV_PORT = 8000

def set_test():
    settings.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    settings.USE_TZ = True

def set_prod(debug = False):
    settings.SWAMP_DRAGON_HOST = '0.0.0.0'
    hostname = 'tic-tac-toe.harpb.com'
    settings.ALLOWED_HOSTS = (hostname, '.harpb.com')
    if not debug:
        settings.DEBUG = False
    settings.TEMPLATE_DEBUG = False

    settings.DRAGON_URL = settings.DRAGON_URL.replace('localhost', hostname)

#===============================================================================
# CONFIGURE environment
#===============================================================================
HOSTNAME = socket.gethostname()
settings.SERVER_ENVIRONMENT = os.environ.get('SERVER_ENVIRONMENT')
if not settings.SERVER_ENVIRONMENT:
    if 'web-' in HOSTNAME or 'db-' in HOSTNAME:
        settings.SERVER_ENVIRONMENT = 'PROD'
    else:
        for arg in sys.argv:
            if 'test' in arg or 'nose' in arg:
                settings.SERVER_ENVIRONMENT = 'TEST'
                break
        if not settings.SERVER_ENVIRONMENT:
            settings.SERVER_ENVIRONMENT = 'LOCAL'


def configure(environment_type):
    settings.SERVER_ENVIRONMENT = environment_type.upper()
#     print r"settings.SERVER_ENVIRONMENT: '%s'" % settings.SERVER_ENVIRONMENT
    if 'PROD' == settings.SERVER_ENVIRONMENT:
        set_prod()
    elif 'DEBUG_PROD' == settings.SERVER_ENVIRONMENT:
        settings.SERVER_ENVIRONMENT = 'PROD'
        set_prod(debug = True)
    elif 'TEST' == settings.SERVER_ENVIRONMENT:
        set_test()
    elif 'DEBUG' == settings.SERVER_ENVIRONMENT:
        set_debug()
    else:
        set_local()

configure(settings.SERVER_ENVIRONMENT)


