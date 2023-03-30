from app.main import api
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse
from app.main.service.SrLdapProvider import SrLdapProvider
from app.main.model.User import User
from ldap3.core.exceptions import LDAPOperationResult


class SshKeys(Resource):
    decorators = [jwt_required]

    def get(self):
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        return {"keys": User(ldapUser, ldapClient).getSshKeys()}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('key', required=True, type=str, location='json')
        args = parser.parse_args(strict=True)
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        try:
            user.addSshKey(args['key'])
            return '', 201
        except LDAPOperationResult as ex:
            return {"msg": "Failed to add key"}, 400

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('key', required=True, type=str, location='json')
        args = parser.parse_args(strict=True)
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        try:
            user.removeSshKey(args['key'])
            return '', 204
        except LDAPOperationResult as ex:
            return {"msg": "Failed to remove key"}, 400


api.add_resource(SshKeys, '/ssh/keys')
