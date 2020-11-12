import axios from 'axios';
import store from '@/store/index';
import cookies from 'vue-cookies';
import router from '../router';
import bus from '@/utils/bus';

let onSuccess = data => {
	GetMe(data);
};
let onFailure = data => {
	data;
};

let GetMe = async authObj => {
	authObj;

	window.Kakao.API.request({
		url: '/v2/user/me',
		success: async res => {
			const kakao_account = res.kakao_account;
			const req_body = {
				id: res.id,
				name: kakao_account.profile.nickname,
				email: kakao_account.email,
				token: res.access_token,
				profileIMG: kakao_account.profile.profile_image_url,
			};
			cookies.set('username', req_body.name);
			axios
				.post(
					`${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_AUTH_API_URL}accounts/check/email/`,
					{
						email: `${req_body.email}`,
					},
				)
				.then(res => {
					console.log(res);
					if (res.status === 200) {
						axios
							.post(
								`${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_AUTH_API_URL}accounts/login/`,
								{
									email: req_body.email,
									password: req_body.email,
								},
							)
							.then(res => {
								store.commit('SETUSERINFO', {
									token: res.data.token,
									username: cookies.get('username'),
								});
								cookies.set('auth-token', res.data.token);
								router.push('/calendar');
							})
							.catch(() => {
								// alert('로그인 할 수 없습니다!');
								bus.$emit('show:error', '로그인 할 수 없습니다!');
							});
					} else if (res.status === 204) {
						axios
							.post(
								`${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_AUTH_API_URL}accounts/signup/`,
								{
									email: req_body.email,
									password1: req_body.email,
									password2: req_body.email,
								},
							)
							.then(res => {
								store.commit('SETUSERINFO', {
									token: res.data.token,
									username: cookies.get('username'),
								});
								cookies.set('auth-token', res.data.token);
								router.push('/calendar');
							})
							.catch(() => {
								bus.$emit(
									'show:error',
									'가입 할 수 없습니다. 다시 시도 해 주세요.',
								);
							});
					}
				})
				.catch(() => {
					bus.$emit('show:error', '로그인에 실패했습니다. 다시 시도 해주세요');
				});
		},
		fail: () => {
			// LoginFailure();
		},
	});
};

let Logout = () => {
	window.Kakao.API.request({
		url: '/v1/user/unlink',
		success: function(response) {
			response;
		},
		fail: function(error) {
			error;
		},
	});
};

export { onSuccess, onFailure, GetMe, Logout };
