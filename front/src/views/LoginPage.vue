<template>
	<section class="login-wrap">
		<section class="login-body">
			<input class="login-input" type="text" v-model="email" />
			<input class="login-input" type="password" v-model="password" />
			<button @click="submitLogin()">로그인</button>
		</section>
	</section>
</template>

<script>
import { Login } from '@/api/auth';
import bus from '@/utils/bus';
// import { mapMutations } from 'vuex';
export default {
	data() {
		return {
			email: null,
			password: null,
		};
	},
	methods: {
		async submitLogin() {
			try {
				const { data } = await Login(this.email, this.password);
				this.$store.commit('SETUSERINFO', {
					username: data.user.username,
					token: data.token,
				});
				this.$cookies.set('auth-token', data.token);
				this.$cookies.set('username', data.user.username);
				this.$router.push('/calendar');
			} catch (error) {
				bus.$emit('show:error', '로그인 할 수 없습니다!');
			}
		},
	},
};
</script>

<style lang="scss">
.login-body {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	.login-input {
		margin: 5px 0;
		width: 50%;
		line-height: 1.6;
	}
	button {
		margin: 10px;
		padding: 5px 8px;
		border: none;
		font-size: 1.1rem;
	}
}
</style>
