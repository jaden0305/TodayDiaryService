<script>
import { Line } from 'vue-chartjs';
export default {
	name: 'LineChart',
	extends: Line,
	props: ['chartData'],
	data: () => ({
		colorSets: [
			{ fore: '#EF9A9A', back: '#B71C1C' },
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
						ticks: { beginAtZero: true, suggestedMin: -100, suggestedMax: 100 },
						gridLines: { display: true },
					},
				],
				xAxes: [{ gridLines: { display: false } }],
			},
			legend: { display: true },
			responsive: false,
			maintainAspectRatio: false,
			plugins: [
				{
					id: 'kwhWeek',
					beforeRender(x) {
						console.log(x);
						var c = x.chart;
						var dataset = x.data.datasets[0];
						var yScale = x.scales['y-axis-0'];
						var yPos = yScale.getPixelForValue(0);

						var gradientFill = c.ctx.createLinearGradient(0, 0, 0, c.height);
						gradientFill.addColorStop(0, 'red');
						gradientFill.addColorStop(yPos / c.height - 0.01, 'red');
						gradientFill.addColorStop(yPos / c.height + 0.01, 'blue');
						gradientFill.addColorStop(1, 'blue');

						var model =
							x.data.datasets[0]._meta[Object.keys(dataset._meta)[0]].dataset
								._model;
						model.backgroundColor = gradientFill;
					},
				},
			],
		},
	}),
	mounted() {
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
					fill: true,
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
