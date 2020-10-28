<template>
	<div class="report-wrap">
		<div class="report-btnbox">
			<button
				@click="
					selectChart(0);
					onDisplayNone();
				"
				class="report-btn"
			>
				전체
			</button>
			<button
				@click="
					selectChart(1);
					onDisplay();
				"
				class="report-btn select"
			>
				주별
			</button>
			<button
				@click="
					selectChart(2);
					onDisplay();
				"
				class="report-btn"
			>
				월별
			</button>
		</div>
		<div class="report-selectbox">
			<button class="report-select__prev">
				이전달
			</button>
			<div class="report-select">
				<span class="report-select__month">시월</span>
				<span class="report-select__span"></span>
			</div>
			<button class="report-select__next">
				다음달
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
</template>

<script src="https://unpkg.com/chance@1.1.6/dist/chance.min.js"></script>
<script>
import LineChart from '@/components/common/LineChart.vue';
export default {
	components: { LineChart },
	data() {
		return {
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
						label: '메리윌',
						data: ['61', '7', '17', '63', '28', '99', '-70'],
					},
				],
			},
		};
	},
	methods: {
		rotation: ([word]) => {
			var chance = new Chance(word[0]);
			return chance.pickone([0, 1 / 8, 3 / 4, 7 / 8]);
		},
		selectChart(num) {
			const selected = document.querySelector('.select');
			const charts = document.querySelectorAll('.report-btn');
			selected.classList.remove('select');
			charts[num].classList.add('select');
		},
		onDisplay() {
			const selectBox = document.querySelector('.report-selectbox');
			if (selectBox.classList.contains('display-none')) {
				selectBox.classList.remove('display-none');
			}
		},
		onDisplayNone() {
			const selectBox = document.querySelector('.report-selectbox');
			if (!selectBox.classList.contains('display-none')) {
				selectBox.classList.add('display-none');
			}
		},
	},
};
</script>

<style lang="scss">
:root {
	--background: #005;
	--primary: #88d5bf;
	--secondary: #5d6bf8;
	--third: #e27fcb;
}

.report-wrap {
	box-sizing: border-box;
	width: 100%;
	max-width: 100%;
	min-height: 100vh;
	height: 100%;
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	align-content: center;
	padding: 1rem;
	.report-wordcloud {
		width: 100%;
		height: 50%;
		padding: 1rem;
		border-radius: 1rem;
		background: #f0f0f0;
		box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
		/* border-radius: 0.5rem; */
		/* background: white; */
		/* box-shadow: 13px 32px 36px -14px hsla(0, 0%, 70%, 0.3); */
		margin-bottom: 1rem;
	}
	.report-chart {
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
	margin-bottom: 1.5rem;
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
		margin: 0 auto 0.5rem;
	}
	.select {
		color: #343a40;
		border-radius: 1rem;
		padding: 0.75rem;
		background: linear-gradient(145deg, #d8d8d8, #ffffff);
		box-shadow: 5px 5px 10px #b4b4b4, -5px -5px 10px #ffffff;
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
