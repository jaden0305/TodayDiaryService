<template>
	<div class="report-wrap">
		<div class="report-btnbox">
			<button @click="selectChart(0)" class="report-btn">전체</button>
			<button @click="selectChart(1)" class="report-btn select">
				주별
			</button>
			<button @click="selectChart(2)" class="report-btn">월별</button>
		</div>
		<div class="report-selectbox">
			<button class="report-select__prev">
				<i class="icon ion-ios-arrow-back"></i>
			</button>
			<div class="report-select">
				<span class="report-select__month">10월</span>
				<span class="report-select__span"></span>
			</div>
			<button class="report-select__next">
				<i class="icon ion-ios-arrow-forward"></i>
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
		border-radius: 0.5rem;
		padding: 1rem;
		background: white;
		box-shadow: 13px 32px 36px -14px hsla(0, 0%, 70%, 0.3);
		margin-bottom: 1rem;
	}
	.report-chart {
		width: 100%;
		height: 50%;
		border-radius: 0.5rem;
		padding: 1rem;
		background: white;
		box-shadow: 13px 32px 36px -14px hsla(0, 0%, 70%, 0.3);
	}
	.report-title::after {
		content: '';
		display: block;
		width: 100%;
		border-bottom: 2px solid #e9ecef;
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
		font-size: 1rem;
		font-weight: 800;
		margin: 0 auto 0.5rem;
	}
	.select {
		color: #343a40;
	}
	.select:after {
		content: '';
		display: block;
		width: 100%;
		border-bottom: 2px solid black;
		margin: 0 auto;
	}
}
.report-selectbox {
	display: flex;
	justify-content: center;
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

	.report-select__prev,
	.report-select__next {
		font-size: 1.5rem;
		border: 0;
		outline: 0;
		background: none;
		color: #adb5bd;
		cursor: pointer;
		font-weight: 800;
	}
	.report-select__prev {
		margin-right: 1.5rem;
	}
	.report-select__next {
		margin-left: 1.5rem;
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
