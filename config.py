from os import environ

class Config(object):
    API_TOKEN = environ.get('API_TOKEN')