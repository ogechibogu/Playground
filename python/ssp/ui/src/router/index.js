import Vue from 'vue';
import Router from 'vue-router';

import Dashboard from '../pages/Dashboard.vue';
import Ssh from '../pages/Ssh.vue';
import MacAddress from '../pages/MacAddress.vue'
import VpnAccess from '../pages/VpnAccess.vue'
import WiFi from '../pages/WiFi.vue'
import Login from '../pages/core/Login.vue';
import LoggedOut from '../pages/core/LoggedOut.vue';
import Error from '../pages/core/Error.vue';
import store from '../store'

Vue.use(Router);

const ifNotAuthenticated = (to, from, next) => {
  if (!store.getters.isAuthenticated) {
    next();
    return
  }
  next('/')
};

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next();
    return
  }
  next('/login')
};

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: ifAuthenticated,
      meta: {
        breadcrumb: [
          { name: 'Dashboard' }
        ]
      }
    },
    {
      path: '/ssh',
      name: 'Ssh',
      component: Ssh,
      beforeEnter: ifAuthenticated,
      meta: {
        breadcrumb: [
          { name: 'SSH' }
        ]
      }
    },
    {
      path: '/vpn',
      name: 'VpnAccess',
      component: VpnAccess,
      beforeEnter: ifAuthenticated,
      meta: {
        breadcrumb: [
          { name: 'VPN Access' }
        ]
      }
    },
    {
      path: '/wifi',
      name: 'WiFi',
      component: WiFi,
      beforeEnter: ifAuthenticated,
      meta: {
        breadcrumb: [
          { name: 'WIFI' }
        ]
      }
    },
    {
      path: '/macaddress',
      name: 'MacAddress',
      component: MacAddress,
      beforeEnter: ifAuthenticated,
      meta: {
        breadcrumb: [
          { name: 'Mac Address' }
        ]
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: ifNotAuthenticated,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/loggedout',
      name: 'LoggedOut',
      component: LoggedOut,
      beforeEnter: ifNotAuthenticated,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/error',
      name: 'Error',
      component: Error,
      meta: {
        allowAnonymous: true
      }
    },
  ]
});
