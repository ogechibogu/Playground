from SrLdapClient import SrLdapClient
import json
from ldap3.utils import hashed as password

class User:

    def __init__(self, ldapUser, ldapClient: SrLdapClient):
        self.ldapClient = ldapClient
        self.ldapUser = ldapUser

    def __getattr__(self, item):
        return self.ldapUser['attributes'][item]

    def getSshKeys(self):
        if 'sshPublicKey' in self.ldapUser['attributes']:
            return list(map(lambda x: x.decode(), self.ldapUser['attributes']['sshPublicKey']))
        return []

    def addSshKey(self, key):
        self.ldapClient.addAttribute(self.ldapUser['dn'], 'sshPublicKey', key)

    def removeSshKey(self, key):
        self.ldapClient.removeAttribute(self.ldapUser['dn'], 'sshPublicKey', key)

    def getSshAccesses(self):
        accesses = self.ldapUser['attributes'].get('memberOf', [])
        timeLimitedAccesses = {}
        for description in self.ldapUser['attributes'].get('description', []):
            loads = json.loads(description)
            timeLimitedAccesses[loads['group']] = loads['expire']
        permissions = []
        for access in accesses:
            splitedDn = access.split(",")
            cn = splitedDn[0].split("=")[1]
            if cn.startswith("access_vpn"):
                continue
            permission = {"name": cn, "expire": timeLimitedAccesses.get(access, None)}
            permissions.append(permission)
        return permissions

    def getMacAddressess(self):
        if 'macAddress' in self.ldapUser['attributes']:
            return self.ldapUser['attributes']['macAddress']
        return []

    def addMacAddress(self, address):
        self.ldapClient.addAttribute(self.ldapUser['dn'], 'macAddress', address)

    def removeMacAddress(self, address):
        self.ldapClient.removeAttribute(self.ldapUser['dn'], 'macAddress', address)

    def changePassword(self, newPassword):
        hashedPassword = password.hashed(password.HASHED_SALTED_SHA, newPassword)
        self.ldapClient.replaceAttribute(self.ldapUser['dn'], 'userPassword', hashedPassword)

    def getAttributes(self):
        attributes = {}
        for key, value in self.ldapUser['attributes'].items():
            if isinstance(value, list):
                attributes[key] = list(map(lambda x: x.decode() if isinstance(x, bytes) else x, value))
            elif isinstance(value, bytes):
                attributes[key] = value.decode()
            else:
                attributes[key] = value
        return attributes

    def getVpnAccesses(self):
        groups = self.ldapUser['attributes'].get('memberOf', [])
        vpns = []
        for group in groups:
            cn = group.split(",")[0].split("=")[1]
            if cn.startswith("access_vpn"):
                vpns.append(cn)
        return sorted(vpns)
