import { report } from './index';

export function fetchMonthReport({ year, month }) {
	return report.get(`/month?year=${year}&month=${month}`);
}
export function fetchWeekReport({ year, month }) {
	return report.get(`/week?year=${year}&month=${month}`);
}
