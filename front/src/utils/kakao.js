import axios from 'axios';

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
			// console.log('아이듸!')
			// console.log(res);
			// console.log(kakao_account);
			const req_body = {
				id: res.id,
				name: kakao_account.profile.nickname,
				email: kakao_account.email,
				// token: res.access_token,
				// birthday: kakao_account.birthday,
				// kakaoAccessToken: authObj.access_token,
				profileIMG: kakao_account.profile.profile_image_url,
			};
			// social_login(req_body);
			console.log(req_body);
			// alert('로그인 했어용....')
			axios
				.get('http://192.168.100.82:8000/accounts/check/email/', {
					email: req_body.email,
				})
				.then(() => {
					axios
						.post('http://192.168.100.82:8000/accounts/login/', {
							email: req_body.email,
							password: req_body.email,
						})
						.then(() => {
							// console.log(res.data)
						})
						.catch(() => {
							alert('로그인 할 수 없습니다!');
						});
				})
				.catch(() => {
					axios
						.post('http://192.168.100.82:8000/accounts/signup/', {
							email: req_body.email,
							password1: req_body.email,
							password2: req_body.email,
						})
						.then(() => {
							// console.log(res + 'DB 저장')
						})
						.catch(() => {
							alert('가입 할 수 없습니다. 다시 시도 해 주세요.');
						});
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
