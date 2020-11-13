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
	if (typeof string === 'string' && string.length > 10) {
		return string.substr(0, 10) + '..';
	}
	return string;
}
export function musicTruncate(string) {
	if (string.length > 16) {
		return string.substr(0, 16) + '..';
	}
	return string;
}

export function emotionFilter(number) {
	switch (number) {
		case 1:
			return '오늘 하루, "행복"하게 보내셨네요.';
		case 2:
			return '오늘 하루, 따뜻한 위로가 필요하진 않으신가요?';
		case 3:
			return '삼 월';
		case 4:
			return '오늘 하루, 무료하진 않으셨나요?';
		case 5:
			return '오늘 하루, 기분전환이 필요하진 않으신가요?';
		case 6:
			return '오늘 하루, 다이나믹하게 보내셨네요.';
		case 7:
			return '오늘 하루, 않으셨나요?';
		case 8:
			return '팔 월';
		default:
			throw new Error('해당 감정 정보가 정확하지 않습니다.');
	}
}
