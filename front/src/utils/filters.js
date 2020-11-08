export function filterMonth(month) {
	switch (month) {
		case 1:
			return '일 월';
		case 2:
			return '이 월';
		case 3:
			return '삼 월';
		case 4:
			return '사 월';
		case 5:
			return '오 월';
		case 6:
			return '유 월';
		case 7:
			return '칠 월';
		case 8:
			return '팔 월';
		case 9:
			return '구 월';
		case 10:
			return '시 월';
		case 11:
			return '십일월';
		case 12:
			return '십이월';
		default:
			throw new Error('해당 월의 정보가 정확하지 않습니다.');
	}
}

export function truncate(string) {
	if (string.length > 7) {
		return string.substr(0, 7) + '..';
	}
	return string;
}
