from app.main import api
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.main.service.SrLdapProvider import SrLdapProvider
from app.main.model.User import User


class UserController(Resource):
    decorators = [jwt_required]

    def get(self):
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        return user.getAttributes()


api.add_resource(UserController, '/user')
