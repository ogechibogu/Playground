<template>
  <div>
    <template v-if="!$route.meta.allowAnonymous">
      <v-app id="inspire">
        <div class="app-container">
          <toolbar @toggleNavigationBar="drawer = !drawer"/>
          <navigation :toggle="drawer"/>
          <v-content>
            <breadcrumbs/>
            <router-view/>
          </v-content>
        </div>
        <page-footer/>
      </v-app>
    </template>
    <template v-else>
      <transition>
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </template>
  </div>
</template>

<script>
import Vue from "vue";
import store from './store'
import router from './router'
import {AUTH_LOGOUT} from './store/actions/auth'

export default {
  name: "App",

  created: function () {
    Vue.axios.interceptors.response.use(
      function (response) {
        return response;
      },
      function (error) {
        if ([401, 422].includes(error.response.status) && error.config && !error.config.__isRetryRequest && !error.config.url.endsWith('auth/login')) {
          store.dispatch(AUTH_LOGOUT).then(() => router.push({ name: 'LoggedOut' }));
        }
        return Promise.reject(error);
      }
    );
  },
  data() {
    return {
      drawer: true
    };
  }
};
</script>

<style>
</style>
