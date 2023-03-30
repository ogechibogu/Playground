from .GlobalConfig import GlobalConfig
import ssl
import os
from srvault import SRVault, KVStore


class Production(GlobalConfig):
    vault_token = SRVault('glob-prod-fran').get_token()
    secret = KVStore('glob-prod-fran', 'secret', token=vault_token)
    JWT_SECRET_KEY = os.urandom(24).hex()
    LDAP_SERVER = 'ldap.ops.srinternal.net'
    LDAP_BINDDN = secret.get('sr-ssp/ldap.credentials')['user_dn']
    LDAP_SECRET = secret.get('sr-ssp/ldap.credentials')['user_pw']
    LDAP_REQUIRE_CERT = ssl.CERT_REQUIRED
    DEBUG = False
