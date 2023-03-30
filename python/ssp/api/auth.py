import hashlib, binascii, os
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import abort
from api import app

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def authenticate(username, password):
    profile = app.config['kv'].get("users/{}/profile".format(username))
    if profile and verify_password(profile.get('password', None), password):
        u = User(username, username, password)
        return u
    abort(401)
     


def identity(payload):
    user_id = payload['identity']
    return user_id



jwt = JWT(app, authenticate, identity)