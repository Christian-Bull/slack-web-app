import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    WORKSPACE = os.environ.get('WORKSPACE') or 'generic-slack-name'
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'