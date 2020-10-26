<template>
	<div class="report-wrap">
		<div class="report-wordcloud">
			<span class="report-title">나의 감정 사전</span>
			<vue-word-cloud
				style="height:40vh; border-radius: 8px;"
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
			<span class="report-title">나의 감정 그래프</span>
			<div class="report-btnbox">
				<button @click="selectChart(0)" class="report-btn">이번주</button>
				<button @click="selectChart(1)" class="report-btn select">
					이번달
				</button>
				<button @click="selectChart(2)" class="report-btn">이번해</button>
			</div>
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
				['romance', 19],
				['magic', 2],
				['fantasy', 7],
				['adventure', 4],
			],
			chartLoading: false,
			chartData: {
				labels: ['01', '02', '03', '04', '05', '06', '07'],
				chartData: [
					{
						label: '뉴스원',
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
	}
	.report-chart {
		width: 100%;
		height: 50%;
	}
	.report-title::before {
		content: '';
	}
	.report-title {
		font-size: 1.5rem;
		font-weight: 800;
	}
}
.report-btnbox {
	margin-top: 1rem;
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
		margin: 0 auto;
	}
	.select {
		color: black;
	}
	.select:after {
		content: '';
		display: block;
		width: 2rem;
		border-bottom: 2px solid black;
		margin: 0 auto;
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
.shape {
	background: linear-gradient(45deg, var(--primary) 0%, var(--secondary) 100%);
	animation: morph 8s ease-in-out infinite;
	border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
	height: 400px;
	transition: all 1s ease-in-out;
	width: 400px;
	z-index: 5;
}

@keyframes morph {
	0% {
		border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
		background: linear-gradient(
			45deg,
			var(--primary) 0%,
			var(--secondary) 100%
		);
	}

	50% {
		border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
		background: linear-gradient(45deg, var(--third) 0%, var(--secondary) 100%);
	}

	100% {
		border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
		background: linear-gradient(
			45deg,
			var(--primary) 0%,
			var(--secondary) 100%
		);
	}
}
</style>
