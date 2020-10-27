import Vue from 'vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter);

const routes = [
	{
		path: '/calendar',
		name: 'calendar',
		component: () => import('@/views/CalendarPage.vue'),
	},
	{
		path: '/diary',
		name: 'diary',
		component: () => import('@/views/WriteDiaryPage.vue'),
	},
	{
		path: '/diary/:diaryId',
		name: 'fetchDiary',
		props: route => ({ diaryId: Number(route.params.diaryId) }),
		component: () => import('@/views/ReadDiaryPage.vue'),
	},
	{
		path: '/report',
		name: 'report',
		component: () => import('@/views/ReportPage'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
