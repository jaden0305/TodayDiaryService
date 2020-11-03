<script>
//Importing Bar class from the vue-chartjs wrapper
import { Bar } from 'vue-chartjs';
//Exporting this so it can be used in other components
export default {
	name: 'Chart',
	extends: Bar,
	props: ['chartData'],

	data() {
		return {
			datacollection: {
				//Data to be represented on x-axis
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
						//Data to be represented on y-axis
						data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100],
					},
				],
			},
			//Chart.js options that controls the appearance of the chart
			options: {
				scales: {
					yAxes: [
						{
							ticks: {
								display: true,
								stepSize: 25,
								beginAtZero: true,
								suggestedMax: 100,
							},
							gridLines: {
								display: true,
							},
						},
					],
					xAxes: [
						{
							gridLines: {
								display: false,
							},
						},
					],
				},
				legend: {
					display: true,
				},
				responsive: true,
				maintainAspectRatio: false,
			},
		};
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
					borderWidth: 1,
					borderColor: colors.back,
					backgroundColor: colors.back,
					pointBorderColor: colors.fore,
					pointBackgroundColor: colors.fore,
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
	},
	mounted() {
		//renderChart function renders the chart with the datacollection and options object.
		this.renderChart(this.datacollection, this.options);
	},
};
</script>
