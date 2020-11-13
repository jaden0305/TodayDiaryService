import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store/index';

Vue.use(VueRouter);

const requireAuth = (to, from, next) => {
	if (store.getters.getToken === null) {
		return next();
	}
	next('/calendar');
};
const notRequireAuth = (to, from, next) => {
	if (store.getters.getToken !== null) {
		return next();
	}
	next('/');
};

const routes = [
	{
		path: '',
		name: 'main',
		component: () => import('@/views/MainPage.vue'),
		beforeEnter: requireAuth,
	},
	{
		path: '/calendar',
		name: 'calendar',
		component: () => import('@/views/CalendarPage.vue'),
		beforeEnter: notRequireAuth,
	},
	{
		path: '/diary',
		name: 'diary',
		component: () => import('@/views/WriteDiaryPage.vue'),
		beforeEnter: notRequireAuth,
	},
	{
		path: '/diary/:diaryId',
		name: 'fetchDiary',
		props: route => ({ propsDiaryId: Number(route.params.diaryId) }),
		component: () => import('@/views/ReadDiaryPage.vue'),
		beforeEnter: notRequireAuth,
	},
	{
		path: '/saveDiary',
		name: 'saveDiary',
		component: () => import('@/views/CompleteDiaryPage.vue'),
		beforeEnter: notRequireAuth,
	},
	{
		path: '/report',
		name: 'report',
		component: () => import('@/views/ReportPage.vue'),
		beforeEnter: notRequireAuth,
	},
	{
		path: '/music',
		name: 'music',
		component: () => import('@/views/MusicPlayerPage.vue'),
		beforeEnter: notRequireAuth,
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
