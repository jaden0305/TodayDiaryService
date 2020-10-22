<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-themes">
				테마 폰트
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
		bus.$on('show:themeModal', this.openMethod);
	},
};
</script>

<style lang="scss" scoped></style>
