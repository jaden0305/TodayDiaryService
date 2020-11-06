import axios from 'axios';

export function youtubeSearch(string) {
	return axios.get('https://www.googleapis.com/youtube/v3/search', {
		params: {
			part: 'snippet',
			type: 'video',
			q: `${string}`,
			key: process.env.VUE_APP_YOUTUBE_API_KEY,
		},
	});
}
