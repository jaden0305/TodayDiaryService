<template>
	<section class="toast" :class="toastAnimationClass">
		{{ message }}
	</section>
</template>

<script>
import bus from '@/utils/bus.js';
let toastTimer;
export default {
	data() {
		return {
			open: false,
			message: '',
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? 'show' : null;
		},
	},
	methods: {
		showToast(message) {
			this.message = message;
			this.open = true;
			clearTimeout(toastTimer);
			toastTimer = setTimeout(this.hideToast, 2000);
		},
		hideToast() {
			this.open = false;
		},
	},
	created() {
		bus.$on('show:error', this.showToast);
	},
	beforeDestroy() {
		bus.$off('show:error', this.showToast);
	},
};
</script>

<style lang="scss" scoped>
.toast {
	font-family: 'Poor Story';
	position: fixed;
	width: 280px;
	padding: 1rem 0.5rem;
	height: 64px;
	font-size: 13px;
	background-color: #ff922b;
	border-radius: 3px;
	word-break: normal;
	box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.2);
	color: white;
	margin-left: -140px;
	top: -120px;
	left: 50%;
	display: flex;
	justify-content: center;
	align-items: center;
	font-weight: 600;
	@media screen and (min-width: 321px) {
		width: 320px;
		margin-left: -160px;
	}
}
.toast.show {
	transform: translateY(150px);
}
</style>
