import sshKeys from './data/ssh_keys'
import sshPermissions from './data/ssh_permissions'
import authLogin from './data/auth_login'
import user from './data/user'
import MacAddress from "./data/macaddress";
import VpnAccess from "./data/vpn_access"
import VpnConfig from "./data/vpn_config"

const fetch = (mockData, time = 0) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(mockData)
    }, time)
  })
};

const fetchError = (mockData, time = 0) => {
  return new Promise((resolve, reject) => {
    reject("error")
  })
};

export default {
  fetchPublicKeys() {
    return fetch(sshKeys, 1000)
  },
  fetchToken() {
    return fetch(authLogin, 1000)

  },

  addPublicKey(key) {
    return fetch('', 1000)
  },

  removePublicKey(key) {
    return fetch('', 1000)
  },

  fetchSshPermissions() {
    return fetch(sshPermissions, 1500)
  },

  fetchUserData() {
    return fetch(user, 500)
  },

  fetchMacAddresses() {
    return fetch(MacAddress, 500)
  },

  removeMacAddress(address) {
    return fetch('', 100)
  },

  addMacAddress(addressForm) {
    return fetch('', 100)
  },

  changePassword(passwordForm) {
    return fetch('', 100)
  },

  fetchVpnAccess() {
    return fetch(VpnAccess, 700)
  },

  fetchVpnConfig(vpnName){
    return fetch(VpnConfig.config, 700)
  },

  loginError() {
    return fetchError('401')
  }
}
