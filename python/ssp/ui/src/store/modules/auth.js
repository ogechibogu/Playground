/* eslint-disable promise/param-names */
import {AUTH_REQUEST, AUTH_ERROR, AUTH_SUCCESS, AUTH_LOGOUT} from '../actions/auth'
import {USER_REQUEST, USER_SUCCESS} from '../actions/user'
import client from 'api-client'
import Vue from 'vue';

const state = {token: sessionStorage.getItem('token') || '', status: '', hasLoadedOnce: false};

const getters = {
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
};

const actions = {
  [AUTH_REQUEST]: ({commit, dispatch}, user) => {
    return new Promise((resolve, reject) => {
      commit(AUTH_REQUEST);

      client.fetchToken(user)
        .then(response => {
          sessionStorage.setItem('token', response.access_token);
          Vue.axios.defaults.headers.common['Authorization'] = 'JWT ' + response.access_token;
          commit(AUTH_SUCCESS, response.access_token);
          // dispatch(USER_REQUEST);
          resolve(response.access_token)
        })
        .catch(err => {
          commit(AUTH_ERROR, err);
          sessionStorage.removeItem('token');
          reject(err)
        })
    })
  },
  [AUTH_LOGOUT]: ({commit, dispatch}) => {
    return new Promise((resolve, reject) => {
      commit(AUTH_LOGOUT);
      sessionStorage.removeItem('token');
      // remove the axios default header
      delete Vue.axios.defaults.headers.common['Authorization'];
      resolve()
    })
  }
};

const mutations = {
  [AUTH_REQUEST]: (state) => {
    state.status = 'loading'
  },
  [AUTH_SUCCESS]: (state, token) => {
    state.status = 'success';
    state.token = token;
    state.hasLoadedOnce = true
  },
  [AUTH_ERROR]: (state) => {
    state.status = 'error';
    state.hasLoadedOnce = true
  },
  [AUTH_LOGOUT]: (state) => {
    state.token = ''
  }
};

export default {
  state,
  getters,
  actions,
  mutations,
}
