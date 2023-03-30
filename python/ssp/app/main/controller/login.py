from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from manage import app
from app.main.service.SrLdapProvider import SrLdapProvider
from ldap3.core.exceptions import LDAPException
import logging

logger = logging.getLogger(__name__)

@app.route('/auth/login', methods=['POST'])
def login():
    ldapClient = SrLdapProvider().create()
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = ldapClient.findUser(username)
    if user:
        try:
            userLdap = SrLdapProvider().create(user['dn'], password)
            userLdap.bind()
            logger.info("Authenticated user: {}".format(username))
            access_token = create_access_token(identity={"user_dn": user['dn'], "user_pw": password})
            return jsonify(access_token=access_token), 200
        except LDAPException as ex:
            logger.error("Failed to authenticate user: {}".format(username))
            return jsonify({"msg": "Authentication failed"}), 401
    logger.error("User not found: {}".format(username))
    return jsonify({"msg": "Authentication failed"}), 401


@app.route('/logged')
@jwt_required
def logged():
    i = get_jwt_identity()
    return i['user_dn']
