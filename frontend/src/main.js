import Vue from 'vue'
import App from './App.vue'
import VueCookies from 'vue-cookies';

// global css
import './assets/css/style.css'

// axios config
import axiosConfig from './assets/js/configs/axios'

// router
import router from './router'

// deploy cookies
Vue.use(VueCookies);

// default cookies
Vue.$cookies.set('theme', 'white');

Vue.prototype.$axios = axiosConfig;

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')