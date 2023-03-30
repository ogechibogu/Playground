from flask import Flask
from srvault import KVStore
from datetime import timedelta
app = Flask(__name__, static_folder="../ui/dist/static", template_folder="../ui/dist/") 
kv = KVStore('int', 'infra')
app.config['kv'] = kv
config = kv.get('srinfrass/config')
app.config['cfg'] = config 
app.config['JWT_AUTH_URL_RULE'] = '/auth/login'
app.config['JWT_SECRET_KEY'] =  config['jwt_secret']
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=10)
