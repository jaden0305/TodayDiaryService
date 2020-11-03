import axios from 'axios';
import { setInterceptors } from '@/api/common/interceptors';

function create(url, options) {
	const instance = axios.create(Object.assign({ baseURL: url }, options));
	return instance;
}

function createWithAuth(url, options) {
	const instance = axios.create(Object.assign({ baseURL: url }, options));
	setInterceptors(instance);
	return instance;
}

export const base = create(process.env.VUE_APP_API_URL);
export const auth = createWithAuth(
	`${process.env.VUE_APP_AUTH_API_URL}accounts`,
);
export const diary = createWithAuth(`${process.env.VUE_APP_API_URL}post`);
export const calendar = createWithAuth(
	`${process.env.VUE_APP_API_URL}calendar`,
);
export const report = createWithAuth(
	`${process.env.VUE_APP_REPORT_API_URL}text`,
);
