import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		username: cookies.isKey('username') ? cookies.get('username') : null,
	},
	mutations: {
		SETUSERINFO(state, { username, token }) {
			state.username = username;
			state.token = token;
		},
		CLEARINFO(state) {
			state.token = null;
			state.username = null;
		},
	},
	actions: {},
	modules: {},
});
