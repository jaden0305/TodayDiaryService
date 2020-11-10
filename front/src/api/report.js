import { report } from './index';

export function fetchMonthReport({ year, month }) {
	return report.get(`/monthly/?year=${year}&month=${month}`);
}
export function fetchWeekReport(startWeek, endWeek) {
	const today = new Date();

	return report.get(
		`/weekly/?start=${startWeek}&end=${endWeek}&today=${today.getFullYear()}-${today.getMonth() +
			1}-${today.getDate()}`,
	);
}
