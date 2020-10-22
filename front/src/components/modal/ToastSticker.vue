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

<style lang="scss" scoped>
.toast {
	width: 98%;
	height: 65%;
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: #646464;
	background-color: #ffffff;
	box-shadow: 0 0 15px rgba(53, 53, 53, 0.5);
	border-radius: 4px;
	z-index: 100;
	.toast-wrap {
		width: 90%;
		height: 85%;
		.toast-close {
			margin-top: 30px;
			text-align: center;
			.toast-close__btn {
				border: none;
				background: none;
				img {
					width: 30px;
				}
			}
		}
	}
}
.toast.none {
	display: none;
}
</style>
