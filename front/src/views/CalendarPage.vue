<template>
	<section class="calendar-wrap">
		<div class="calendar-content">
			<div class="calendar-header">
				<button @click="movePrevMonth" class="calendar-header__prev">
					이전달
				</button>
				<div class="calendar-header__box">
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
				<span
					:key="index"
					v-for="(day, index) in preMonth"
					class="calendar-day"
				>
					<img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">{{ day.day }}</p>
				</span>
				<span
					:key="'A' + index"
					v-for="(day, index) in nowMonth"
					class="calendar-day"
				>
					<img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">{{ day.day }}</p>
				</span>
				<span
					:key="'B' + index"
					v-for="(day, index) in nextMonth"
					class="calendar-day"
				>
					<img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">{{ day.day }}</p>
				</span>
			</div>
		</div>
	</section>
</template>

<script>
import { fetchCalendar } from '@/api/calendar';
export default {
	data() {
		return {
			year: null,
			month: null,
			preMonth: [],
			nowMonth: [],
			nextMonth: [],
			token: null,
		};
	},
	methods: {
		async fetchMonth({ year, month }) {
			try {
				const { data } = await fetchCalendar({ year, month });
				console.log(this.month, data);
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
				console.log(error);
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
	},
	created() {
		const day = new Date();
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
	padding: 1rem;
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
		display: inline-block;
		position: relative;
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
	/* .calendar-weekday:nth-child(1) { */
	// border-top-left-radius: 8px;
	// border-bottom-left-radius: 8px;
	/* } */
	/* .calendar-weekday:nth-last-child(1) { */
	// border-top-right-radius: 8px;
	// border-bottom-right-radius: 8px;
	/* } */
	.calendar-weekday {
		padding-top: 10px;
		padding-bottom: 10px;
		width: 100 / 7 * 1%;
		text-align: center;
		font-weight: 600;
		// background: #495057;
	}

	// .calendar-weekday::after {
	// 	content: '';
	// 	display: block;
	// 	width: 100%;
	// 	padding-bottom: 10px;
	// 	border-bottom: 2px solid grey;
	// }
	// .sunday,
	// .saturday {
	// 	color: #adb5bd;
	// }
}

.calendar-days {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	flex-wrap: wrap;
	.calendar-day {
		display: flex;
		flex-direction: column;
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
			width: 50%;
			margin: 0;
		}
		.today {
			color: royalblue;
		}
		p {
			margin: 0;
			margin-top: 0.15rem;
			font-size: 0.5rem;
			font-weight: 600;
			color: #868e96;
		}
	}
	// .calendar-day__title {
	// 	color: ;
	// }
	// .calendar-day:nth-child(7n + 1),
	// .calendar-day:nth-child(7n) {
	// 	.calendar-day__title {
	// 		color: #868e96;
	// 	}
	// }
}
</style>
