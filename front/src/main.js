import Vue from 'vue';
import App from './App.vue';
import VueWordCloud from 'vuewordcloud';
import './registerServiceWorker';
import router from './router';
import store from './store';
import VueCookies from 'vue-cookies';
import { filterMonth, truncate } from '@/utils/filters';
import Chartkick from 'chartkick';
import VueChartkick from 'vue-chartkick';
import VueVideoWrapper from 'vue-video-wrapper';

Vue.use(VueVideoWrapper);
Vue.use(VueChartkick, { Chartkick });
Vue.use(VueCookies);
Vue.$cookies.config('6h');
Vue.filter('filterMonth', filterMonth);
Vue.filter('truncate', truncate);

Vue.config.productionTip = false;

Vue.component(VueWordCloud.name, VueWordCloud);

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app');
