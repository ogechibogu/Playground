from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api, reqparse, abort
from srvault import KVStore, SRVault

import random
import os
from flask_jwt import JWT, jwt_required, current_identity
from functools import wraps

from resources.ssh import ssh_bp

from api import app
from auth import jwt


api = Api(app)

app.register_blueprint(ssh_bp, url_prefix='/ssh')

@app.route("/")
def index():
    return render_template("index.html") 
 
    
if __name__ == "__main__": 
    app.run(debug=True)
