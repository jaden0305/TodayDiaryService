import { auth } from '@/api/index';

export function refreshToken(token) {
	return auth.post('/refresh/', { token });
}

export function likeMusic(musicId, search) {
	return auth.post('/music/like/', { music_id: musicId, search });
}
export function likeMusics() {
	return auth.get('/music/like/');
}

export function Login(email, password) {
	return auth.post('/login/', {
		email,
		password,
	});
}

export function isOpenTutorial() {
	return auth.get(`/tutorial/`);
}
export function hideTutorial() {
	return auth.patch(`/tutorial/`);
}
