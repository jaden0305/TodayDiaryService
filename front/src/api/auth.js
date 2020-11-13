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
