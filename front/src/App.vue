<template>
	<div id="app" :class="[appNone ? 'app-none' : 'app-block']">
		<header>
			<h1 :class="[NoneLogo ? 'hidden-logo' : 'display-logo']">오늘 하루</h1>
		</header>
		<main class="container">
			<router-view> </router-view>
		</main>
	</div>
</template>

<script>
export default {
	computed: {
		NoneLogo() {
			return (
				this.$route.name === 'main' ||
				this.$route.name === 'calendar' ||
				this.$route.name === 'report'
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
	},
};
</script>

<style lang="scss">
@import './assets/css/reset.css';
@import './assets/css/color.css';
#app {
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
