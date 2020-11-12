import { analysis } from './index';

export function createDiaryanalysis(diaryAnalysisData) {
	return analysis.post('/analysis/', diaryAnalysisData);
}
export function reselectEmotion(id) {
	return analysis.get(`/select/?emotion=${id}`);
}
