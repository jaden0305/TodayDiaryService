<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-stickers">
				<label for="toast-sticker__all">전체</label>
				<input
					type="radio"
					name="sticker"
					id="toast-sticker__all"
					value="all"
					v-model="selectedSticker"
				/>
				<label for="toast-sticker__animal">동물</label>
				<input
					type="radio"
					name="sticker"
					id="toast-sticker__animal"
					value="animal"
					v-model="selectedSticker"
				/>
				<label for="toast-sticker__figure">도형</label>
				<input
					type="radio"
					name="sticker"
					id="toast-sticker__figure"
					value="figure"
					v-model="selectedSticker"
				/>
			</div>
			<div class="toast-sticker">
				<div class="toast-sticker__view">
					<img
						v-if="selectedSticker === 'all'"
						src="@/assets/images/temp/1.jpg"
						alt="all"
					/>
					<img
						v-if="selectedSticker === 'animal'"
						src="@/assets/images/temp/2.png"
						alt="all"
					/>
					<img
						v-if="selectedSticker === 'figure'"
						src="@/assets/images/temp/3.jpg"
						alt="all"
					/>
				</div>
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="closeSticker">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
		</section>
	</section>
</template>

<script>
export default {
	data() {
		return {
			selectedSticker: 'all',
		};
	},
	props: {
		open: Boolean,
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		closeSticker() {
			this.$emit('close-sticker');
		},
	},
};
</script>

<style lang="scss" scoped>
.toast-sticker__view {
	img {
		width: 100px;
	}
}
</style>
