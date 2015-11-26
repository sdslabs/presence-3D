__author__ = 'gautham'

# MODIFY CONFIGURATION VALUES HERE , FOR CHANGING CREDENTIALS
##########################################################################
DEBUG = True

TEMPLATE_DEBUG = {"default": True,
                  "production": True}

EMAIL_USE_TLS = {"default": True,
                 "production": True}

ALLOWED_HOSTS = {"default": ['localhost',
                                '127.0.0.1',
                                '0.0.0.0'],
                 "production": ['sdslabs.co.in',
                                 'sdslabs.co',
                                 ]}
# FIND SETTINGS
FIND_HOST = {"default": "localhost",
                 "production": "localhost"}

FIND_PORT = {"default": "8080",
                 "production": "8080"}

# DATABASE SETTINGS
POSTGRES_HOST = {"default": "localhost",
                 # todo: confirm with Gautham "production"  : "postgres"}
                 "production": "localhost"}

POSTGRES_PORT = {"default": "5432",
                 "production": "5432"}

# EMAIL BACKEND
EMAIL_HOST = {"default": "smtp.sendgrid.net",
              "production": "smtp.sendgrid.net"}

EMAIL_PORT = {"default": "587",
              "production": "587"}

# RABBITMQ
RABBIT_HOSTNAME = {"default": "localhost",
                   "production": "localhost"}

RABBIT_VHOST = {"default": "/",
                "production": "/"}

# HTTPS RELATED
CSRF_COOKIE_SECURE = {"default": False,
                      "production": False}
# Below settings in production mode will make us not login into admin panel if
#HTTPS is not there
SESSION_COOKIE_SECURE = {"default": False,
                         "production": False
                         }
# OPTIMIZATION
CONN_MAX_AGE = {"default": 0,
                "production": 0
                }

##########################################################################
"""For using the below decorator the function has to return a dictionary {"default":whatever config,
                                                                          "production":whatever config}"""


def getconfig(func):
    """checks whether debug is true and returns appropriate configuration"""
    def inner():
        if get_debug_status():
            config = func()['default']
        else:
            config = func()['production']
        return config
    return inner

# This function does not need decorator , as it is called in the decorator itself and DEBUG has to be manually changed
# in the beginning of this file


def get_debug_status():
    return DEBUG


@getconfig
def get_template_debug_status():
    return TEMPLATE_DEBUG


@getconfig
def get_email_tls_status():
    return EMAIL_USE_TLS


@getconfig
def get_allowed_hosts():
    return ALLOWED_HOSTS


@getconfig
def get_email_host():
    return EMAIL_HOST


@getconfig
def get_email_port():
    return EMAIL_PORT


@getconfig
def get_rabbit_hostname():
    return RABBIT_HOSTNAME


@getconfig
def get_rabbit_vhost():
    return RABBIT_VHOST


@getconfig
def get_postgres_host():
    return POSTGRES_HOST


@getconfig
def get_postgres_port():
    return POSTGRES_PORT


@getconfig
def get_csrf_cookie_secure_status():
    return CSRF_COOKIE_SECURE


@getconfig
def get_session_cookie_secure_status():
    return SESSION_COOKIE_SECURE


@getconfig
def get_conn_max_age():
    return CONN_MAX_AGE

@getconfig
def get_find_host():
    return FIND_HOST


@getconfig
def get_find_port():
    return FIND_PORT