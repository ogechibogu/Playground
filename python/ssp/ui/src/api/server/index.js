import Vue from 'vue'

export default {

  fetchToken(user) {
    return Vue.axios.post('auth/login', user)
      .then(response => response.data)
      .catch(error => Promise.reject(error))
  },

  fetchPublicKeys() {
    return Vue.axios.get('/ssh/keys')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  addPublicKey(key) {
    return Vue.axios.post('/ssh/keys', key)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  removePublicKey(key) {
    return Vue.axios.delete('/ssh/keys', {data: {'key': key}})
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  fetchSshPermissions() {
    return Vue.axios.get('/ssh/permissions')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  fetchUserData() {
    return Vue.axios.get('/user')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  fetchMacAddresses() {
    return Vue.axios.get('/macaddress')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  addMacAddress(addressForm) {
    return Vue.axios.post('/macaddress', addressForm)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  removeMacAddress(address) {
    return Vue.axios.delete('/macaddress', {data: {'address': address}})
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  changePassword(passwordForm) {
    return Vue.axios.put('/user/password', passwordForm)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  fetchVpnAccess() {
    return Vue.axios.get('/vpn/access')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

  fetchVpnConfig(vpnName){
    return Vue.axios.get('/vpn/' + vpnName + '/config')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data))
  },

}
