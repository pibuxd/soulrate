import Vue from 'vue'
import App from './App.vue'
import VueCookies from 'vue-cookies';

// global css
import './assets/css/style.css'

import router from './router'

Vue.config.productionTip = false

Vue.use(VueCookies);
Vue.$cookies.set('theme', 'white');

import axios from 'axios'
const axiosConfig = {
    baseURL: 'http://0.0.0.0:5000/api/',
};
Vue.prototype.$axios = axios.create(axiosConfig)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')