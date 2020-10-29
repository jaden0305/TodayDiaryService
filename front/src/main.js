import Vue from 'vue';
import App from './App.vue';
import VueWordCloud from 'vuewordcloud';
import './registerServiceWorker';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.component(VueWordCloud.name, VueWordCloud);

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app');
