import os
import string
import random
from decouple import config


BASE_DIR = os.path.abspath('.')

#DEBUG = config('DEBUG', cast=bool)
DEBUG = False

#SECRET_KEY = config('SECRET_KEY') or \
SECRET_KEY = ''.join(random.choice(string.ascii_letters) for i in range(42))

#SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI') or \
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')

SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', True, cast=bool)
