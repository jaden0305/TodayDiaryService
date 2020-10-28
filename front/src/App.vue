<template>
	<div id="app">
		<header>
			<img
				:class="[NoneLogo ? 'hidden-logo' : 'display-logo']"
				src="@/assets/images/logo3.png"
				alt="오늘하루로고"
			/>
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
	},
};
</script>

<style lang="scss">
@import './assets/css/reset.css';
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	width: 100%;
	min-height: 100vh;
	max-width: 768px;
	min-width: 280px;
	margin: 0 auto;
	box-sizing: border-box;
	border: 8px solid #f0f0f0;
	border-radius: 15px;
	background: #f0f0f0;
	box-shadow: inset 7px 7px 12px #dfdfdf, inset -7px -7px 12px #ffffff;
	header {
		display: flex;
		justify-content: center;
		.display-logo {
			margin: 18px 0 25px;
			width: 150px;
		}
		.hidden-logo {
			display: none;
		}
	}
}
.container {
	flex: 1 1 auto;
	max-width: 100%;
	position: relative;
}
</style>
