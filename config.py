import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')