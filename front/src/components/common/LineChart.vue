<script>
import bus from '@/utils/bus';
import { Line } from 'vue-chartjs';
export default {
	name: 'LineChart',
	extends: Line,
	props: ['chartData'],
	data: () => ({
		colorSets: [
			{ fore: '#343a40', back: '#868e96' },
			{ fore: '#F48FB1', back: '#880E4F' },
			{ fore: '#CE93D8', back: '#4A148C' },
			{ fore: '#B39DDB', back: '#311B92' },
			{ fore: '#9FA8DA', back: '#1A237E' },
			{ fore: '#64B5F6', back: '#0D47A1' },
			{ fore: '#4FC3F7', back: '#01579B' },
			{ fore: '#0097A7', back: '#006064' },
			{ fore: '#00897B', back: '#004D40' },
			{ fore: '#81C784', back: '#1B5E20' },
		],
		datacollection: {
			labels: [
				'January',
				'February',
				'March',
				'April',
				'May',
				'June',
				'July',
				'August',
				'September',
				'October',
				'November',
				'December',
			],
			datasets: [
				{
					label: 'Data One',
					backgroundColor: '#f87979',
					pointBackgroundColor: 'white',
					borderWidth: 1,
					pointBorderColor: '#249EBF',
					data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100],
				},
			],
		},
		options: {
			scales: {
				yAxes: [
					{
						ticks: {
							display: true,
							stepSize: 50,
							beginAtZero: true,
							suggestedMin: -100,
							suggestedMax: 100,
						},
						gridLines: { display: true },
					},
				],
				xAxes: [{ gridLines: { display: false } }],
			},
			legend: { display: true },
			responsive: false,
			maintainAspectRatio: false,
		},
	}),
	mounted() {
		bus.$on('lineUpdate', this.init);
		this.init();
	},
	methods: {
		init() {
			let data = this.chartData.chartData;
			let datasets = [];
			let pos = 0;
			data.forEach(site => {
				let colors = this.colorSets[pos];
				datasets.push({
					label: site.label,
					borderWidth: 2,
					borderColor: colors.back,
					backgroundColor: colors.back,
					pointBorderColor: colors.fore,
					pointBackgroundColor: colors.fore,
					fill: false,
					data: site.data,
				});
				pos++;
			});
			this.datacollection = {
				labels: this.chartData.labels,
				datasets: datasets,
			};
			this.render();
		},
		render() {
			this.renderChart(this.datacollection, this.options);
		},
	},
};
</script>
<style></style>
