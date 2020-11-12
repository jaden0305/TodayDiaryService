import { auth } from '@/api/index';

export function refreshToken(token) {
	return auth.post('/refresh/', { token });
}

export function likeMusics() {
	return auth.get('/music/like/');
}
// export function addLikeMusic() {
// 	return auth.post('/music/like/', { music_id });
// }
