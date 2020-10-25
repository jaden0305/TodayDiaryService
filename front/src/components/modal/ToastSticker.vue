<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-stickers">
				<!-- <router-link :to="{ name: 'stickerAll' }">전체</router-link>
				<router-link :to="{ name: 'stickerFigure' }">도형</router-link>
				<router-link :to="{ name: 'stickerAnimal' }">동물</router-link>
				<div class="toast-sticker">
					<router-view></router-view>
				</div> -->
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
