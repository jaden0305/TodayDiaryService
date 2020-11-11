import { analysis } from './index';

export function createDiaryanalysis(diaryAnalysisData) {
	return analysis.post('/analysis/', diaryAnalysisData);
}
