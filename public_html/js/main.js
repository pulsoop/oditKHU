import Vue from 'vue';
import store from './store/index';
import App from './App';
import axios from 'axios';
import router from './router';

Vue.config.productionTip = false;
Vue.prototype.$EventBus = new Vue();
Vue.prototype.$http = axios;

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});