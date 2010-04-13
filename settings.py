# -*- coding: utf-8 -*-
"""
Settings for Django.

%%COPYRIGHT%%
"""

# See http://docs.djangoproject.com/en/dev/ref/settings/ for inspiration

import os
import django

OUR_ROOT = os.path.dirname(os.path.realpath(__file__))

# HUDORA specific config
from cs.global_django_settings import *

DEBUG = True
if os.environ.get('SILVER_VERSION', '').startswith('silverlining/'):
    # we are running on a silverlining managed production server.
    # see http://cloudsilverlining.org/services.html#silver-version-environmental-variable
    DEBUG = False

TEMPLATE_DEBUG = DEBUG
if DEBUG:
    TEMPLATE_STRING_IF_INVALID = "__%s__"
else:
    SEND_BROKEN_LINK_EMAILS = True

MEDIA_URL = 'http://s.hdimg.net/%%MODULENAME%%/'
# for development you can use something like this:
# MEDIA_URL = '/media/'

ROOT_URLCONF = 'urls'
SITE_ID = 3 # shop.hudora.de

TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'generic_templates/templates'), )

AUTHENTICATION_BACKENDS = ('googleappsauth.backends.GoogleAuthBackend',)
GOOGLE_OPENID_REALM = 'http://%%PROJECTNAME%%.hudora.biz/'
if not os.environ.get('SILVER_VERSION', '').startswith('silverlining/'):
    GOOGLE_OPENID_REALM = 'http://127.0.0.1:8080/'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.environ['CONFIG_FILES'], '%%MODULENAME%%.db')

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

try:
    from settings_local import *
except ImportError:
    pass
