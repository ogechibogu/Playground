import os
import sys
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from .config import configByName
import logging

configName = os.getenv('ENVIRONMENT') or 'dev'
app = Flask(__name__, static_folder="../../ui/dist/static", template_folder="../../ui/dist/")
app.config.from_object(configByName.get(configName))
if app.config.get('DEBUG'):
    level = logging.DEBUG
else:
    level = logging.INFO
logging.basicConfig(stream=sys.stdout, level=level, format='%(asctime)s,%(msecs)d %(levelname)-8s %(name)s [ %(filename)s %(lineno)d ] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
jwt = JWTManager(app)
api = Api(app)

from .controller import *
