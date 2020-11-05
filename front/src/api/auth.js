import { auth } from '@/api/index';

export function refreshToken(token) {
	return auth.post('/refresh/', { token });
}
