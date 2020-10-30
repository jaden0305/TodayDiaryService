import { calendar } from './index';

export function fetchCalendar({ year, month }) {
	return calendar.get(`/?year=${year}&month=${month}`);
}
