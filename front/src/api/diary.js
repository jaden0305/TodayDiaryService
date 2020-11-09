import { diary } from './index';

export function createDiary(diaryData) {
	const formdata = new FormData();
	if (diaryData.image) {
		formdata.append('image', diaryData.image);
	}
	formdata.append('title', diaryData.title);
	formdata.append('content', diaryData.content);
	formdata.append('fontsize', diaryData.fontsize);
	formdata.append('music_name', diaryData.music_name);
	formdata.append('music_artist', diaryData.music_artist);
	formdata.append('postcolor', diaryData.postcolor.id);
	formdata.append('font', diaryData.font.id);
	formdata.append('pattern', diaryData.pattern.id);
	formdata.append('created', diaryData.created);

	return diary.post('/', formdata);
}
export function fetchDiary(diaryId) {
	return diary.get(`/${diaryId}/`);
}
export function fetchFonts() {
	return diary.get(`/fonts/`);
}
export function fetchPapers() {
	return diary.get(`/papers/`);
}
export function fetchStickers() {
	return diary.get(`/sticker/all/`);
}
export function updateDiary(diaryData, diaryId) {
	const formdata = new FormData();
	if (diaryData.image) {
		formdata.append('image', diaryData.image);
	}
	formdata.append('title', diaryData.title);
	formdata.append('content', diaryData.content);
	formdata.append('fontsize', diaryData.fontsize);
	formdata.append('music_name', diaryData.music_name);
	formdata.append('music_artist', diaryData.music_artist);
	formdata.append('postcolor', diaryData.postcolor.id);
	formdata.append('font', diaryData.font.id);
	formdata.append('pattern', diaryData.pattern.id);
	console.log(diaryData.postcolor);

	return diary.put(`/${diaryId}/`, formdata);
}
export function deleteDiary(diaryId) {
	return diary.delete(`/${diaryId}/`);
}
