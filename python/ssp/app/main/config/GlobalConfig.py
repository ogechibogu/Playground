import ssl
from datetime import timedelta


class GlobalConfig:
    JWT_SECRET_KEY = "secret123"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_HEADER_TYPE = 'JWT'
    BUNDLE_ERRORS = True
    LDAP_BASE_DN = "dc=srinternal,dc=net"
    LDAP_SERVER = '127.0.0.1'
    LDAP_BINDDN = 'cn=ssp,ou=service,ou=users,dc=srinternal,dc=net'
    LDAP_SECRET = 'ssp123'
    LDAP_REQUIRE_CERT = ssl.CERT_NONE
    LDAP_CA = None
    DEBUG = False
    PROPAGATE_EXCEPTIONS = True
