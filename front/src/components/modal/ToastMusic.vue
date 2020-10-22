<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-search">
				<input
					class="toast-search__input"
					placeholder="음악을 검색하세요 :)"
					type="text"
				/>
				<button class="toast-search__btn">
					<!-- <img src="@/assets/images/search.svg" alt="" /> -->
				</button>
			</div>

			<!-- <button class="toast-btn-white" @click="open = false">취소</button>
			<button class="toast-btn-purple" @click="showToast">삭제</button> -->
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
		async showToast() {
			// await deleteMyStories(this.storyId);
			this.open = false;
		},
	},
	created() {
		bus.$on('show:musicModal', this.openMethod);
	},
	beforeDestroy() {
		bus.$off('show:delete', this.openMethod);
	},
	watch: {
		$route() {
			this.open = false;
		},
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
		.toast-search {
			margin: 20px 20px 50px;
			position: relative;
			.toast-search__input {
				width: 90%;
				font-size: 14px;
				line-height: 2.3;
				border: none;
				border-bottom: 1px solid rgba(151, 151, 151, 0.5);
			}
			.toast-search__btn {
				position: absolute;
				top: 5px;
				right: 20px;
				border: none;
				background: none;
			}
		}
		.toast-musics {
			.toast-musics__item {
				color: #646464;
				line-height: 2.3;
			}
		}
	}
}
.toast.none {
	display: none;
}
.toast-btn-white {
	border: none;
	border-radius: 3px;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	background: white;
	color: black;
	height: 2rem;
	margin-top: 1.5rem;
	margin-right: 0.5rem;
}
.toast-btn-purple {
	border: none;
	border-radius: 3px;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	background: purple;
	color: white;
	height: 2rem;
	margin-top: 1.5rem;
	margin-left: 0.5rem;
}
</style>
