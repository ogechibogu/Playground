from app.main import api
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse
from app.main.service.SrLdapProvider import SrLdapProvider
from app.main.model.User import User
from ldap3.core.exceptions import LDAPOperationResult, LDAPAttributeOrValueExistsResult, LDAPConstraintViolationResult


class MacAddress(Resource):
    decorators = [jwt_required]

    def get(self):
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        return {"addresses": User(ldapUser, ldapClient).getMacAddressess()}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address', required=True, type=str, location='json')
        args = parser.parse_args(strict=True)
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        try:
            user.addMacAddress(args['address'])
            return '', 201
        except LDAPAttributeOrValueExistsResult as ex:
            return {'msg': 'Mac address already exists'}, 400
        except LDAPConstraintViolationResult as ex:
            return {'msg': 'Mac address already used by another user'}, 400
        except LDAPOperationResult as ex:
            return {'msg': 'Failed to save mac address'}, 400

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address', required=True, type=str, location='json')
        args = parser.parse_args(strict=True)
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        try:
            user.removeMacAddress(args['address'])
            return '', 204
        except LDAPOperationResult as ex:
            return {'msg': 'Failed to remove mac address'}, 400

api.add_resource(MacAddress, '/macaddress')
