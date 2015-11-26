import json
import os

import server_configuration


# Is debug
DEBUG = server_configuration.get_debug_status()
TEMPLATE_DEBUG = server_configuration.get_template_debug_status()

def get_credentials_file_path():
    """
    Location for the standalone credentials file in json format
    :return: String
    """

    if DEBUG is True:
        return (os.path.join(os.path.dirname(__file__), 'data.json'))
    else:
        return (os.path.join(os.path.dirname(__file__), 'data.json'))


def getdata(func):
    """Decorator to Deserialize json data and passes it to functions """
    def inner():
        with open(get_credentials_file_path()) as data_file:
            # deserialize json data to python object
            try:
                # TRY If debug is true load default values ELSE load production
                # values
                data = json.load(data_file)['DEFAULT'] if DEBUG is True else json.load(
                    data_file)['PRODUCTION']
            except Exception as e:
                # http://stackoverflow.com/questions/4308182/getting-the-exception-value-in-python
                print type(e)
                print e.message
        # pass the appropriate parameters into the function
        credential = func(data)
        return credential

    return inner


@getdata
def get_post_gres_password(data):
    return data["post_gres_password"]


@getdata
def get_secret_key(data):
    return data["secret_key"]


@getdata
def get_post_gres_NAME(data):
    return data["post_gres_NAME"]


@getdata
def get_post_gres_USER(data):
    return data["post_gres_user"]


@getdata
def get_email_host_user(data):
    return data["email_host_user"]


@getdata
def get_email_host_password(data):
    return data["email_host_password"]


@getdata
def get_rabbit_username(data):
    return data["rabbit_username"]


@getdata
def get_rabbit_password(data):
    return data["rabbit_password"]


@getdata
def get_aws_access_key_id(data):
    return data["aws_access_key_id"]


@getdata
def get_aws_secret_access_key(data):
    return data["aws_secret_access_key"]


@getdata
def get_aws_bucket_name(data):
    return data["aws_bucket_name"]