<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-stickers"></div>
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

<style lang="scss" scoped></style>
