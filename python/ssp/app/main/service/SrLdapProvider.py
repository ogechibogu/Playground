from flask import current_app
from SrLdapClient import SrLdapClient


class SrLdapProvider:

    def __init__(self):
        self.baseDn = current_app.config['LDAP_BASE_DN']
        self.server = current_app.config['LDAP_SERVER']
        self.validate = current_app.config['LDAP_REQUIRE_CERT']
        self.ldapCA = current_app.config['LDAP_CA']

    def create(self, bindDn=None, bindPw=None):
        if not bindDn and not bindPw:
            bindDn = current_app.config['LDAP_BINDDN']
            bindPw = current_app.config['LDAP_SECRET']
        return SrLdapClient(bindDn, bindPw, server=self.server, ldapBase=self.baseDn, validate=self.validate, ca=self.ldapCA, raiseExceptions=True)
