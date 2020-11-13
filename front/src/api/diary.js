import { diary } from './index';

export function createDiary(diaryData) {
	const formdata = new FormData();
	if (diaryData.image) {
		formdata.append('image', diaryData.image);
	}
	if (diaryData.sticker_image) {
		formdata.append('sticker_image', diaryData.sticker_image);
	}
	formdata.append('title', diaryData.title);
	formdata.append('content', diaryData.content);
	formdata.append('stickers', JSON.stringify(diaryData.stickers));
	formdata.append('search_music', JSON.stringify(diaryData.search_music));
	if (diaryData.recommend_music) {
		formdata.append('recommend_music', diaryData.recommend_music.id);
	}
	formdata.append('user_emotion', diaryData.user_emotion);
	formdata.append('font', diaryData.font.id);
	formdata.append('pattern', diaryData.pattern.id);
	formdata.append('created', diaryData.created);

	return diary.post('/', formdata);
}
export function fetchDiary(diaryId) {
	return diary.get(`/${diaryId}/`);
}
export function isWritten() {
	return diary.get(`/written/`);
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
export function deleteDiary(diaryId) {
	return diary.delete(`/${diaryId}/`);
}
