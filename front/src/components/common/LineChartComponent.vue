<template>
	<line-chart class="line-container" :chartData="chartData"></line-chart>
</template>

<script>
import LineChart from '@/components/common/LineChart.vue';
export default {
	components: { LineChart },
	data() {
		return {
			chartLoading: false,
			chartData: {
				labels: [
					'01',
					'02',
					'03',
					'04',
					'05',
					'06',
					'07',
					'08',
					'09',
					'10',
					'11',
				],
				chartData: [
					{
						label: '다음',
						data: [
							'65',
							'13',
							'22',
							'125',
							'41',
							'142',
							'156',
							'121',
							'24',
							'29',
							'151',
						],
					},
					{
						label: '다우존스',
						data: ['1', '1', '0', '6', '1', '3', '6', '8', '0', '0', '6'],
					},
					{
						label: '네이버',
						data: [
							'65',
							'13',
							'22',
							'119',
							'41',
							'139',
							'150',
							'119',
							'20',
							'28',
							'147',
						],
					},
					{
						label: '뉴스원',
						data: [
							'61',
							'7',
							'17',
							'105',
							'28',
							'128',
							'138',
							'108',
							'10',
							'20',
							'137',
						],
					},
					{
						label: '다나와',
						data: ['0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0'],
					},
				],
			},
		};
	},
	methods: {
		// init() {
		// let item =
		// 	'{"labels":["01","02","03","04","05","06","07","08","09","10","11"],"chartData":[{"label":"다음","data":["65","13","22","125","41","142","156","121","24","29","151"]},{"label":"다우존스","data":["1","1","0","6","1","3","6","8","0","0","6"]},{"label":"네이버","data":["65","13","22","119","41","139","150","119","20","28","147"]},{"label":"뉴스원","data":["61","7","17","105","28","128","138","108","10","20","137"]},{"label":"다나와","data":["0","0","0","1","0","0","1","0","0","0","0"]}]}';
		// let data = JSON.parse(item);
		// this.chartData = { labels: data.labels, chartData: data.chartData };
		// this.chartLoading = false;
		// },
	},
};
</script>

<style></style>
