<template>
	<section class="toast" :class="toastAnimationClass">
		<span class="toast-text"> 해당 일기를 삭제하시겠습니까 ?</span>
		<section>
			<button class="toast-btn-white" @click="open = false">취소</button>
			<button class="toast-btn-purple" @click="showToast">삭제</button>
		</section>
	</section>
</template>

<script>
import bus from '@/utils/bus.js';
import { deleteDiary } from '@/api/diary';
export default {
	data() {
		return {
			open: false,
			diaryId: null,
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		openMethod(id) {
			this.diaryId = id;
			this.open = true;
		},
		async showToast() {
			try {
				await deleteDiary(this.diaryId);
				this.$router.push('/calendar');
				this.open = false;
			} catch (error) {
				bus.$emit('show:error', '삭제를 실패했어요 :(');
			}
		},
	},
	created() {
		bus.$on('show:delete', this.openMethod);
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
	z-index: 100;
	position: fixed;
	width: 400px;
	@media screen and (max-width: 640px) {
		width: 350px;
	}
	height: 9rem;
	border-radius: 4px;
	background: #5a5a5a;
	// box-shadow: 6px 6px 12px #4d4d4d, -6px -6px 12px #686868;
	color: white;
	top: 50%;
	left: 50%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	transform: translate(-50%, -50%);
}
.toast-text {
	font-family: 'Poor Story';
}
.toast.none {
	display: none;
}
.toast-btn-white {
	border: none;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	border-radius: 4px;
	background: #5a5a5a;
	box-shadow: inset 4px 4px 4px #515151, inset -4px -4px 4px #636363;
	color: white;
	height: 2rem;
	margin-top: 1.5rem;
	margin-right: 0.5rem;
}
.toast-btn-purple {
	border: none;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	border-radius: 4px;
	// background: #5a5a5a;
	background: rgb(187, 40, 40);
	box-shadow: 7px 7px 15px #515151, -7px -7px 15px #636363;
	color: white;
	height: 2rem;
	margin-top: 1.5rem;
	margin-left: 0.5rem;
}
</style>
