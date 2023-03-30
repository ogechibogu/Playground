
import Vue from 'vue';
import App from './App';
import router from './router';
import store from './store'

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios);

import 'vuetify/dist/vuetify.min.css';
import 'font-awesome/css/font-awesome.css';

import Vuetify from 'vuetify';

import 'material-design-icons-iconfont/dist/material-design-icons.css';
import './styles/global.css';

import VueChartkick from 'vue-chartkick';
import Chart from 'chart.js';
import fullCalendar from 'vue-fullcalendar';
import { setupComponents } from './config/setup-components';

import swatches from 'vue-swatches';
import "vue-swatches/dist/vue-swatches.min.css"

import ConsoleIcon from 'vue-material-design-icons/Console.vue';
Vue.component('terminal-icon', ConsoleIcon);

import VPNIcon from 'vue-material-design-icons/Key.vue';
Vue.component('vpn-icon', VPNIcon);

import WIFIIcon from 'vue-material-design-icons/Wifi.vue';
Vue.component('wifi-icon', WIFIIcon);

import ExpanssionCard from 'vue-material-design-icons/ExpansionCardVariant.vue';
Vue.component('expansion-card-icon', ExpanssionCard);

import HelpIcon from 'vue-material-design-icons/CommentQuestionOutline';
Vue.component('help-icon', HelpIcon);

Vue.use(VueChartkick, { adapter: Chart });
Vue.component('full-calendar', fullCalendar);
Vue.component('swatches', swatches);

setupComponents(Vue);

Vue.use(Vuetify);

Vue.config.productionTip = false;
Vue.axios.defaults.maxRedirects = 0;
Vue.axios.defaults.headers.common['Content-Type'] = 'application/json';
const token = sessionStorage.getItem('token');
if (token) {
  Vue.axios.defaults.headers.common['Authorization'] = "JWT " + token
}


new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  data: {
    themeColor: '#10181f',

  }
});
