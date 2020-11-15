<template>
	<section class="calendar-wrap">
		<div class="calendar-content">
			<div class="calendar-header">
				<button @click="movePrevMonth" class="calendar-header__prev">
					이전달
				</button>
				<div class="calendar-header__box">
					<span class="calendar-header__year">{{ year }}</span>
					<span class="calendar-header__month">{{ month | filterMonth }}</span>
					<span class="calendar-header__span"></span>
				</div>

				<button @click="moveNextMonth" class="calendar-header__next">
					다음달
				</button>
			</div>
			<div class="calendar-weekdays">
				<span class="calendar-weekday sunday">일</span>
				<span class="calendar-weekday monday">월</span>
				<span class="calendar-weekday tuesday">화</span>
				<span class="calendar-weekday wednesday">수</span>
				<span class="calendar-weekday thursday">목</span>
				<span class="calendar-weekday friday">금</span>
				<span class="calendar-weekday saturday">토</span>
			</div>
			<div class="calendar-days">
				<CalendarDay
					:day="day"
					:year="day.year"
					:toDay="toDay"
					:todayMonth="todayMonth"
					:nowDay="nowDay"
					:todayYear="todayYear"
					:weekWidth="weekWidth"
					:key="index"
					v-for="(day, index) in preMonth"
				></CalendarDay>
				<CalendarDay
					:day="day"
					:year="day.year"
					:toDay="toDay"
					:todayMonth="todayMonth"
					:nowDay="nowDay"
					:todayYear="todayYear"
					:weekWidth="weekWidth"
					:key="'B' + index"
					v-for="(day, index) in nowMonth"
				></CalendarDay>
				<CalendarDay
					:day="day"
					:year="day.year"
					:toDay="toDay"
					:todayMonth="todayMonth"
					:nowDay="nowDay"
					:todayYear="todayYear"
					:weekWidth="weekWidth"
					:key="'A' + index"
					v-for="(day, index) in nextMonth"
				></CalendarDay>
			</div>
		</div>
	</section>
</template>

<script>
import bus from '@/utils/bus';
import CalendarDay from '@/components/common/CalendarDay.vue';
import { fetchCalendar } from '@/api/calendar';
export default {
	components: {
		CalendarDay,
	},
	data() {
		return {
			year: null,
			month: null,
			preMonth: [],
			nowMonth: [],
			nextMonth: [],
			token: null,
			toDay: null,
			todayMonth: null,
			nowDay: null,
		};
	},
	mounted() {
		const days = document.querySelector('.calendar-days');
		this.weekWidth = days.clientWidth / 7;
		window.scrollTo(0, 0);
	},
	updated() {
		const emotions = document.querySelectorAll('.emoticon');
		emotions.forEach(emotion => {
			emotion.style.width = this.weekWidth;
			emotion.style.height = this.weekWidth;
		});
	},
	methods: {
		writeDiary(dayString) {
			this.$router.push({ name: 'diary', query: { day: dayString } });
		},
		readDiary(diary_pk) {
			this.$router.push(`/diary/${diary_pk}`);
		},
		async fetchMonth({ year, month }) {
			try {
				const { data } = await fetchCalendar({ year, month });
				this.preMonth = [];
				this.nowMonth = [];
				this.nextMonth = [];
				let pre = this.month - 1;
				if (pre === 0) {
					pre = 12;
				}
				let nex = this.month + 1;
				if (nex == 13) {
					nex = 1;
				}
				data[pre].forEach(day => {
					this.preMonth.push(day);
				});
				data[nex].forEach(day => {
					this.nextMonth.push(day);
				});
				data[this.month].forEach(day => {
					this.nowMonth.push(day);
				});
			} catch (error) {
				// console.log(error.response);
				// bus.$emit('show:error', error.response.data);
				bus.$emit('show:error', '캘린더를 불러오는데 실패했습니다 :(');
			}
		},
		movePrevMonth() {
			if (this.month > 1) {
				this.month -= 1;
			} else {
				this.month = 12;
				this.year -= 1;
			}
			this.fetchMonth({ year: this.year, month: this.month });
		},
		moveNextMonth() {
			if (this.month < 12) {
				this.month += 1;
			} else {
				this.month = 1;
				this.year += 1;
			}
			this.fetchMonth({ year: this.year, month: this.month });
		},
		lastTwo(string) {
			return ('0' + string).slice(-2);
		},
	},
	created() {
		const day = new Date();
		this.nowDay = new Date(
			`${day.getFullYear()}-${this.lastTwo(day.getMonth() + 1)}-${this.lastTwo(
				day.getDate(),
			)}`,
		);
		this.todayMonth = day.getMonth() + 1;
		this.toDay = day.getDate();
		this.todayYear = day.getFullYear();
		this.month = day.getMonth() + 1;
		this.year = day.getFullYear();
		this.fetchMonth({ year: this.year, month: this.month });
	},
};
</script>

<style lang="scss">
.calendar-wrap {
	max-width: 100%;
	height: 100%;
	padding: 0.5rem;
	padding-top: 1.25rem;
	margin-bottom: 75px;
	.calendar-content {
		border-radius: 1rem;
		background: #f0f0f0;
		box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
	}
}
.calendar-header {
	display: flex;
	justify-content: space-around;
	align-items: center;
	text-align: center;
	padding-top: 1rem;
	margin-bottom: 0.5rem;
	.calendar-header__box {
		display: flex;
		flex-direction: column;
		justify-content: center;
		position: relative;
		.calendar-header__year {
			opacity: 0.8;
			color: #495057;
		}
		.calendar-header__month {
			font-size: 1.5rem;
			font-weight: 600;
			color: #495057;
			@media (max-width: 300px) {
				font-size: 1.25rem;
			}
		}
		.calendar-header__span {
			position: absolute;
			bottom: -6px;
			left: 0;
			width: 100%;
			height: 12px;
			background: linear-gradient(to right, #9200b9 8%, #6c23c0 75%, #5600c7);
			opacity: 0.5;
		}
	}
	.calendar-header__prev {
		align-self: flex-end;
		margin-right: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #adb5bd;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-right: 3rem;
			font-size: 0.6rem;
		}
	}
	.calendar-header__next {
		align-self: flex-end;
		margin-left: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #adb5bd;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-left: 3rem;
			font-size: 0.6rem;
		}
	}
}

.calendar-weekdays {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	color: #495057;
	margin-top: 1.5rem;
	margin-bottom: 0.5rem;
	.calendar-weekday {
		padding-top: 10px;
		padding-bottom: 10px;
		width: 100 / 7 * 1%;
		text-align: center;
		font-weight: 600;
	}
}
.display-none {
	display: none !important;
}

.calendar-days {
	width: 100%;
	display: flex;
	flex-wrap: wrap;
	.calendar-day {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100 / 7 * 1%;

		margin-bottom: 1.25rem;
		text-align: center;
		i {
			display: flex;
			font-size: 2rem;
			justify-content: center;
			align-items: center;
		}
		.ion-ios-brush {
			color: grey;
		}
		.emoticon {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 90%;
			margin: 0;
		}
		.pencil {
			width: 90%;
		}
		.today {
			color: royalblue;
		}
		p {
			margin: 0;
			margin-top: 3px;
			font-size: 0.7rem;
			font-weight: 600;
			color: #868e96;
		}
	}
}
</style>
