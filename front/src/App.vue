<template>
	<div id="app">
		<router-view> </router-view>
		<ToastMusic />
		<ToastSticker />
		<ToastTheme />
	</div>
</template>

<script>
import ToastMusic from '@/components/modal/ToastMusic.vue';
import ToastSticker from '@/components/modal/ToastSticker.vue';
import ToastTheme from '@/components/modal/ToastTheme.vue';
export default {
	components: {
		ToastMusic,
		ToastSticker,
		ToastTheme,
	},
};
</script>

<style lang="scss">
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	max-width: 768px;
	min-width: 280px;
	margin: 50px auto;
	padding: 10px;
}

#nav {
	padding: 30px;

	a {
		font-weight: bold;
		color: #2c3e50;

		&.router-link-exact-active {
			color: #42b983;
		}
	}
}
</style>
