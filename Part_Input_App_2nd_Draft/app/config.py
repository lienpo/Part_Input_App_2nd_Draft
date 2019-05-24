import os
basedir = os.path.abspath(os.path.dirname(__file__))

conn_str = 'postgresql://jfine:uni1cast@192.168.1.25:5432/unidata'

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or conn_str
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
