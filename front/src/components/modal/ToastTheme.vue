<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-themes">
				테마 폰트
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="closeTheme">
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
		closeTheme() {
			this.$emit('close-theme');
		},
	},
};
</script>

<style lang="scss" scoped></style>
