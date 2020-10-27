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
		children: [
			{
				path: 'stickerAll',
				name: 'stickerAll',
				component: () => import('@/views/modalChildren/StickerAll.vue'),
			},
			{
				path: 'stickerAnimal',
				name: 'stickerAnimal',
				component: () => import('@/views/modalChildren/StickerAnimal.vue'),
			},
			{
				path: 'stickerFigure',
				name: 'stickerFigure',
				component: () => import('@/views/modalChildren/StickerFigure.vue'),
			},
		],
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
