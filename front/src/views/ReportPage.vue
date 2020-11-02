<template>
	<div class="report-wrap">
		<div class="report-header">
			<div class="report-btnbox">
				<button @click="selectChart(0)" class="report-btn">
					전체
				</button>
				<button @click="selectChart(1)" class="report-btn select">
					주별
				</button>
				<button @click="selectChart(2)" class="report-btn">
					월별
				</button>
			</div>
		</div>
		<div class="report-content">
			<div class="report-selectbox display-none">
				<button @click="movePrevMonth" class="report-select__prev">
					이전달
				</button>
				<div class="report-select">
					<span class="report-select__month">{{ month | filterMonth }}</span>
					<span class="report-select__span"></span>
				</div>
				<button @click="moveNextMonth" class="report-select__next">
					다음달
				</button>
			</div>
			<div class="report-selectweekbox">
				<button @click="movePrevWeek" class="report-select__prev">
					이전주
				</button>
				<div class="report-select">
					<span class="report-select__month"
						>{{ startString }}~{{ endString }}</span
					>
					<span class="report-select__span"></span>
				</div>
				<button @click="moveNextWeek" class="report-select__next">
					다음주
				</button>
			</div>
			<div class="report-wordcloud">
				<span class="report-title">감정 사전</span>
				<vue-word-cloud
					style="height:35vh; border-radius: 8px;"
					:words="words"
					:color="
						([, weight]) =>
							weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'
					"
					:rotation="rotation"
					font-family="Quicksand"
					:spacing="parseInt(0.5)"
				/>
			</div>
			<div class="report-chart">
				<span class="report-title">감정 그래프</span>
				<line-chart class="line-container" :chartData="chartData"></line-chart>
			</div>
		</div>
	</div>
</template>

<script src="https://unpkg.com/chance@1.1.6/dist/chance.min.js"></script>
<script>
import LineChart from '@/components/common/LineChart.vue';
import cookies from 'vue-cookies';
import { fetchWeekReport, fetchMonthReport } from '@/api/report';
export default {
	components: { LineChart },
	data() {
		return {
			startWeek: null,
			endWeek: null,
			month: null,
			year: null,
			startString: null,
			endString: null,
			weekcnt: 0,
			words: [
				['romance', 300],
				['magic', 200],
				['fantasy', 100],
				['adventure', 150],
			],
			chartLoading: false,
			chartData: {
				labels: ['01', '02', '03', '04', '05', '06', '07'],
				chartData: [
					{
						label: `${cookies.get('username')}`,
						data: ['61', '7', '17', '63', '28', '99', '-70'],
					},
				],
			},
		};
	},
	created() {
		const day = new Date();
		this.month = day.getMonth() + 1;
		this.year = day.getFullYear();
		let weekDay = new Date();
		this.weekday = weekDay;
		// console.log(this.weekday);
		this.endWeek = new Date(
			this.weekday.setDate(
				this.weekday.getDate() + (6 - this.weekday.getDay() + this.weekcnt * 7),
			),
		);
		this.startWeek = new Date(this.weekday.setDate(this.weekday.getDate() - 6));
		const start = `${this.startWeek.getFullYear()}-${this.startWeek.getMonth() +
			1}-${this.startWeek.getDate()}`;
		const end = `${this.endWeek.getFullYear()}-${this.endWeek.getMonth() +
			1}-${this.endWeek.getDate()}`;
		this.startString = `${this.startWeek.getMonth() +
			1}-${this.startWeek.getDate()}`;
		this.endString = `${this.endWeek.getMonth() + 1}-${this.endWeek.getDate()}`;
		// this.fetchWeek(startString, endString);
		console.log(this.startString, this.endString);
	},
	methods: {
		movePrevMonth() {
			if (this.month > 1) {
				this.month -= 1;
			} else {
				this.month = 12;
				this.year -= 1;
			}
		},
		moveNextMonth() {
			if (this.month < 12) {
				this.month += 1;
			} else {
				this.month = 1;
				this.year += 1;
			}
		},
		movePrevWeek() {
			this.endWeek = new Date(this.endWeek.setDate(this.endWeek.getDate() - 7));
			this.startWeek = new Date(
				this.startWeek.setDate(this.startWeek.getDate() - 7),
			);
			const start = `${this.startWeek.getFullYear()}-${this.startWeek.getMonth() +
				1}-${this.startWeek.getDate()}`;
			const end = `${this.endWeek.getFullYear()}-${this.endWeek.getMonth() +
				1}-${this.endWeek.getDate()}`;
			this.startString = `${this.startWeek.getMonth() +
				1}-${this.startWeek.getDate()}`;
			this.endString = `${this.endWeek.getMonth() +
				1}-${this.endWeek.getDate()}`;
			// this.fetchWeek(startString, endString);
			console.log(this.startString, this.endString);
		},
		moveNextWeek() {
			this.endWeek = new Date(this.endWeek.setDate(this.endWeek.getDate() + 7));
			this.startWeek = new Date(
				this.startWeek.setDate(this.startWeek.getDate() + 7),
			);
			const start = `${this.startWeek.getFullYear()}-${this.startWeek.getMonth() +
				1}-${this.startWeek.getDate()}`;
			const end = `${this.endWeek.getFullYear()}-${this.endWeek.getMonth() +
				1}-${this.endWeek.getDate()}`;
			this.startString = `${this.startWeek.getMonth() +
				1}-${this.startWeek.getDate()}`;
			this.endString = `${this.endWeek.getMonth() +
				1}-${this.endWeek.getDate()}`;
			// this.fetchWeek(startString, endString);
			console.log(this.startString, this.endString);
		},
		async fetchWeek(startWeek, endWeek) {
			const { data } = await fetchWeekReport(startWeek, endWeek);
			console.log(data);
		},
		rotation: ([word]) => {
			var chance = new Chance(word[0]);
			return chance.pickone([0, 1 / 8, 3 / 4, 7 / 8]);
		},
		selectChart(num) {
			const selected = document.querySelector('.select');
			const charts = document.querySelectorAll('.report-btn');
			selected.classList.remove('select');
			charts[num].classList.add('select');
			const selectBox = document.querySelector('.report-selectbox');
			const selectWeekBox = document.querySelector('.report-selectweekbox');

			switch (num) {
				case 0:
					if (!selectBox.classList.contains('display-none')) {
						selectBox.classList.add('display-none');
					}
					if (!selectWeekBox.classList.contains('display-none')) {
						selectWeekBox.classList.add('display-none');
					}
					break;
				case 1:
					if (selectWeekBox.classList.contains('display-none')) {
						selectWeekBox.classList.remove('display-none');
					}
					if (!selectBox.classList.contains('display-none')) {
						selectBox.classList.add('display-none');
					}
					break;
				case 2:
					if (!selectWeekBox.classList.contains('display-none')) {
						selectWeekBox.classList.add('display-none');
					}
					if (selectBox.classList.contains('display-none')) {
						selectBox.classList.remove('display-none');
					}
					break;
				default:
					throw new Error('입력 값이 잘못되었습니다');
			}
		},
	},
};
</script>

<style lang="scss">
.report-wrap {
	box-sizing: border-box;
	width: 100%;
	max-width: 100%;
	height: 100%;
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	align-content: center;
	.report-header {
		width: 100%;
		background: #f0f0f0;
		box-shadow: 5px 5px 10px #d8d8d8, -5px -5px 10px #ffffff;
	}
	.report-content {
		margin-top: 1rem;
		width: 100%;
		height: 100%;
		box-sizing: border-box;
		padding: 1rem;
	}
	.report-wordcloud {
		box-sizing: border-box;

		width: 100%;
		height: 50%;
		border-radius: 1rem;
		background: #f0f0f0;
		box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
		padding: 1rem;
		margin-bottom: 1rem;
	}
	.report-chart {
		box-sizing: border-box;
		width: 100%;
		height: 50%;
		padding: 1rem;
		border-radius: 1rem;
		background: #f0f0f0;
		box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
		/* border-radius: 0.5rem;
		background: white;
		box-shadow: 13px 32px 36px -14px hsla(0, 0%, 70%, 0.3); */
	}
	.report-title::after {
		content: '';
		display: block;
		width: 100%;
		border-bottom: 2px solid #d3d6d8;
		margin: 16px 0 10px 0;
	}
	.report-title {
		color: #495057;
		font-size: 1.25rem;
		font-weight: 800;
	}
}
.report-btnbox {
	padding: 0.5rem;
	box-sizing: border-box;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.report-btn {
		outline: none;
		border: none;
		background: none;
		color: #868e96;
		font-size: 0.8rem;
		font-weight: 800;
		padding: 0.75rem;
		margin: 0.25rem auto;
	}
	.select {
		color: #343a40;
		border-radius: 1rem;
		padding: 0.75rem;
		/* background: linear-gradient(145deg, #d8d8d8, #ffffff);
		box-shadow: 5px 5px 10px #b4b4b4, -5px -5px 10px #ffffff; */
		background: linear-gradient(145deg, #f0f0f0, #f0f0f0);
		box-shadow: 5px 5px 10px #cccccc, -5px -5px 10px #ffffff;
	}
	.select:after {
		content: '';
		display: block;
		width: 100%;
		border-bottom: 2px solid black;
		margin: 0 auto;
	}
}
.display-none {
	display: none !important;
}
.report-selectbox {
	width: 100%;
	display: flex;
	justify-content: space-around;
	align-items: center;
	text-align: center;
	margin-bottom: 1.5rem;
	color: #495057;
	font-weight: 400;
	.report-select {
		display: inline-block;
		position: relative;
		.report-select__month {
			font-size: 1.5rem;
		}
	}
	.report-select__span {
		position: absolute;
		bottom: -6px;
		left: 0;
		width: 100%;
		height: 12px;
		background: linear-gradient(to right, #9200b9 8%, #6c23c0 75%, #5600c7);
		opacity: 0.5;
	}

	.report-select__prev {
		align-self: flex-end;
		margin-right: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #868e96;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-right: 3rem;
			font-size: 0.6rem;
		}
	}
	.report-select__next {
		align-self: flex-end;
		margin-left: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #868e96;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-left: 3rem;
			font-size: 0.6rem;
		}
	}
}
.report-selectweekbox {
	width: 100%;
	display: flex;
	justify-content: space-around;
	align-items: center;
	text-align: center;
	margin-bottom: 1.5rem;
	color: #495057;
	font-weight: 400;
	.report-select {
		display: inline-block;
		position: relative;
		.report-select__month {
			font-size: 1.5rem;
		}
	}
	.report-select__span {
		position: absolute;
		bottom: -6px;
		left: 0;
		width: 100%;
		height: 12px;
		background: linear-gradient(to right, #9200b9 8%, #6c23c0 75%, #5600c7);
		opacity: 0.5;
	}

	.report-select__prev {
		align-self: flex-end;
		margin-right: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #868e96;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-right: 3rem;
			font-size: 0.6rem;
		}
	}
	.report-select__next {
		align-self: flex-end;
		margin-left: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #868e96;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-left: 3rem;
			font-size: 0.6rem;
		}
	}
}
.line-container {
	box-sizing: border-box;
	width: 100%;
	/* height: 50%; */
}
#line-chart {
	box-sizing: border-box;
	width: 100% !important;
	height: 100% !important;
}
</style>
