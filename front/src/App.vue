<template>
	<div id="app">
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
	/* margin: 0 auto; */
	/* padding: 10px; */
}
.container {
	flex: 1 1 auto;
	max-width: 100%;
	position: relative;
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
