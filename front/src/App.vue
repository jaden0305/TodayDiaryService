<template>
	<div id="app">
		<header><img src="@/assets/images/logo3.png" alt="오늘하루로고" /></header>
		<main class="container">
			<router-view> </router-view>
		</main>
	</div>
</template>

<script>
export default {};
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
	header {
		display: flex;
		justify-content: center;
		padding: 18px 0 25px;
		img {
			width: 150px;
		}
	}
}
.container {
	flex: 1 1 auto;
	max-width: 100%;
	position: relative;
}
</style>
