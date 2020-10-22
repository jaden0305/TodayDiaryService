<template>
	<vue-word-cloud
		style="height:50%;"
		:words="words"
		:color="
			([, weight]) =>
				weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'
		"
		:rotation="rotation"
		font-family="Quicksand"
		:spacing="parseInt(0.5)"
	/>
</template>

<script src="https://unpkg.com/chance@1.1.6/dist/chance.min.js"></script>
<script>
export default {
	data() {
		return {
			words: [
				['romance', 19],
				['magic', 2],
				['fantasy', 7],
				['adventure', 4],
			],
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

<style></style>
