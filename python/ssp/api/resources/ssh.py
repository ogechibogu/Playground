from flask import Flask, Blueprint
import flask_restful
from flask_jwt import  current_identity, jwt_required
import sys
import sshpubkeys
sys.path.append('..')
from api import app
ssh_bp = Blueprint('ssh', __name__)
ssh_r = flask_restful.Api(ssh_bp)

class Publickeys(flask_restful.Resource):
    decorators = [jwt_required()]
    def get(self):
        profile = app.config['kv'].get("users/{}/profile".format(current_identity))
        
        keys = [ {"hash": sshpubkeys.SSHKey(x).hash_md5().replace("MD5:", ""), "key": x} for x in profile['ssh']['public_keys'] ] 
        return keys, 200
        

ssh_r.add_resource(Publickeys, '/keys')