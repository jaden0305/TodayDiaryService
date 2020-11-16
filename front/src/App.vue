<template>
	<div id="app" :class="[appNone ? 'app-none' : 'app-block']">
		<header>
			<h1
				@click="$router.push('/calendar')"
				:class="[NoneLogo ? 'hidden-logo' : 'display-logo']"
			>
				오늘 하루
			</h1>
		</header>
		<main class="container">
			<router-view> </router-view>
		</main>
		<ToastComplete></ToastComplete>
		<ToastError></ToastError>
		<ToastDelete></ToastDelete>
		<MusicBar v-if="$route.name === 'fetchDiary'"></MusicBar>
		<NavBar v-if="navOn"></NavBar>
	</div>
</template>

<script>
import ToastDelete from '@/components/common/ToastDelete.vue';
import ToastError from '@/components/common/ToastError.vue';
import ToastComplete from '@/components/common/ToastComplete.vue';
import MusicBar from '@/components/common/MusicBar.vue';
import NavBar from '@/components/common/NavBar.vue';
export default {
	computed: {
		NoneLogo() {
			return (
				this.$route.name === 'main' ||
				this.$route.name === 'calendar' ||
				this.$route.name === 'report' ||
				this.$route.name === 'music'
			);
		},
		appNone() {
			return (
				this.$route.name === 'main' ||
				this.$route.name === 'calendar' ||
				this.$route.name === 'report' ||
				this.$route.name === 'music'
			);
		},
		navOn() {
			return (
				this.$route.name === 'calendar' ||
				this.$route.name === 'report' ||
				this.$route.name === 'music'
			);
		},
	},
	components: {
		MusicBar,
		NavBar,
		ToastComplete,
		ToastError,
		ToastDelete,
	},
};
</script>

<style lang="scss">
@import './assets/css/reset.css';
@import './assets/css/color.css';
#app {
	position: relative;
	width: 100%;
	min-height: 100vh;
	max-width: 768px;
	min-width: 280px;
	margin: 0 auto;
	box-sizing: border-box;
	header {
		display: flex;
		justify-content: center;
		.display-logo {
			margin: 18px 0 25px;
			font-family: 'pentastic';
			font-size: 40px;
			cursor: pointer;
		}
		.hidden-logo {
			display: none;
		}
	}
}
.app-block {
	border: 8px solid #f0f0f0;
	border-radius: 15px;
	background: #f0f0f0;
	box-shadow: inset 7px 7px 12px #dfdfdf, inset -7px -7px 12px #ffffff;
}
.app-none {
}

.container {
	flex: 1 1 auto;
	max-width: 100%;
	position: relative;
}
</style>
