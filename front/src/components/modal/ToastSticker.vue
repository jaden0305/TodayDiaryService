<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-stickers">
				전체 동물 도형
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="open = false">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
		</section>
	</section>
</template>

<script>
import bus from '@/utils/bus.js';
export default {
	data() {
		return {
			open: false,
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		openMethod() {
			this.open = true;
		},
	},
	created() {
		bus.$on('show:stickerModal', this.openMethod);
	},
};
</script>

<style lang="scss" scoped></style>
