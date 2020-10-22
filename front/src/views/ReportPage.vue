<template>
	<div class="report-wrap">
		<vue-word-cloud
			style="height:40%;"
			:words="words"
			:color="
				([, weight]) =>
					weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'
			"
			:rotation="rotation"
			font-family="Quicksand"
			:spacing="parseInt(0.5)"
		/>
		<line-chart class="line-container" :chartData="chartData"></line-chart>
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
	},
};
</script>

<style lang="scss">
.report-wrap {
	box-sizing: border-box;
	max-width: 100%;
	height: 100vh;
	padding: 10px;
	display: flex;
	flex-wrap: wrap;
	align-content: center;
}
.line-container {
	box-sizing: border-box;
	width: 100%;
	height: 40%;
}
#line-chart {
	box-sizing: border-box;
	width: 100% !important;
	height: 100% !important;
}
</style>
