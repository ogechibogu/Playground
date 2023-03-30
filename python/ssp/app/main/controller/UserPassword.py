from app.main import api
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse
from app.main.service.SrLdapProvider import SrLdapProvider
from app.main.model.User import User
from ldap3.core.exceptions import LDAPOperationResult


class UserPassword(Resource):
    decorators = [jwt_required]

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', required=True, type=str, location='json')
        args = parser.parse_args()
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        try:
            user.changePassword(args['password'])
            return '', 204
        except LDAPOperationResult as ex:
            return {"msg": "Failed to change password"}, 400


api.add_resource(UserPassword, '/user/password')
