import { report } from './index';

export function fetchMonthReport({ year, month }) {
	return report.get(`/monthly/?year=${year}&month=${month}`);
}
export function fetchWeekReport({ startWeek, endWeek }) {
	return report.get(`/weekly/?start=${startWeek}&end=${endWeek}`);
}
