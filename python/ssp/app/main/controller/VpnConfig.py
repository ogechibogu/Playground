from app.main import api
from flask_restful import Resource
from flask import Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.main.service.SrLdapProvider import SrLdapProvider
from app.main.model.User import User
from boto3 import client
import logging

logger = logging.getLogger(__name__)


class VpnConfig(Resource):
    decorators = [jwt_required]

    s3 = client('s3')

    def get(self, vpnGroup):
        credentials = get_jwt_identity()
        ldapClient = SrLdapProvider().create(credentials['user_dn'], credentials['user_pw'])
        ldapUser = ldapClient.getUser(credentials['user_dn'])
        user = User(ldapUser, ldapClient)
        if vpnGroup not in user.getVpnAccesses():
            logger.info("User: {} doesn't have permission to {}".format(user.uid, vpnGroup))
            return {"msg": "Config not found"}, 404
        try:
            config = self._getConfigFor(vpnGroup, user.uid.pop())
            return Response(
                config['Body'].read(),
                mimetype='text/plain',
            )
        except self.s3.exceptions.NoSuchBucket as ex:
            logger.error(ex)
            return {"msg": "Config not found"}, 404
        except self.s3.exceptions.NoSuchKey as ex:
            logger.error(ex)
            return {"msg": "Config doesn't exists please try again later."}, 404

    def _getConfigFor(self, name, uid):
        split = name.split("_")
        environment = split[2]
        vpnType = split[1]
        bucket = "sr-{}-keys-{}".format(vpnType, environment)
        logger.info("Trying download config from bucket: {}".format(bucket))
        key = self.getBucketKey(environment, uid, vpnType)
        logger.info("Trying download config for key: {}".format(key))
        return self.s3.get_object(Bucket=bucket, Key=key)

    def getBucketKey(self, environment, uid, vpnType):
        if environment == 'int':
            return "keys/{}_{}.tblk/{}.ovpn".format(environment, uid, uid)
        return "keys/{}/{}.ovpn".format(uid, uid)


api.add_resource(VpnConfig, '/vpn/<string:vpnGroup>/config')
