import { diary } from './index';

export function createDiary(diaryData) {
	const formdata = new FormData();
	formdata.append('image', diaryData.image);
	formdata.append('title', diaryData.title);
	formdata.append('content', diaryData.content);
	formdata.append('fontsize', diaryData.fontsize);
	formdata.append('music_name', diaryData.music_name);
	formdata.append('music_artist', diaryData.music_artist);
	formdata.append('postcolor', diaryData.postcolor);
	formdata.append('font', diaryData.font);
	formdata.append('pattern', diaryData.pattern);
	formdata.append('emotion', diaryData.emotion);
	formdata.append('created', diaryData.created);

	return diary.post('/', formdata);
}
export function fetchDiary(diaryId) {
	return diary.get(`/${diaryId}/`);
}
export function updateDiary(diaryData, diaryId) {
	const formdata = new FormData();
	formdata.append('image', diaryData.image);
	formdata.append('title', diaryData.title);
	formdata.append('content', diaryData.content);
	formdata.append('fontsize', diaryData.fontsize);
	formdata.append('music_name', diaryData.music_name);
	formdata.append('music_artist', diaryData.music_artist);
	formdata.append('postcolor', diaryData.postcolor);
	formdata.append('font', diaryData.font);
	formdata.append('pattern', diaryData.pattern);
	formdata.append('emotion', diaryData.emotion);

	return diary.put(`/${diaryId}/`, formdata);
}
export function deleteDiary(diaryId) {
	return diary.delete(`/${diaryId}/`);
}
