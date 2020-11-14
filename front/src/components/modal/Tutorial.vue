<template>
	<section class="tutorial-wrap" :class="toastAnimationClass">
		<div class="tutorial-title">
			<img
				class="tutorial-title__arrow tutorial-arrow"
				src="@/assets/images/scribble.svg"
				alt=""
			/>
			<p>오늘 하루의 감정을 표현해주세요! 감정 분석에 많은 영향을 줘요:)</p>
		</div>
		<div class="tutorial-sticker">
			<img
				class="tutorial-sticker__arrow tutorial-arrow"
				src="@/assets/images/scribble.svg"
				alt=""
			/>
			<p>
				오늘의 감정을 스티커로 표현해보세요! 단 사진에만 스티커를 붙일 수 있어요
			</p>
		</div>
		<div class="tutorial-music">
			<img
				class="tutorial-music__arrow tutorial-arrow"
				src="@/assets/images/scribble.svg"
				alt=""
			/>
			<p>추천 음악 대신 원하는 음악을 넣을 수 있어요</p>
		</div>
		<div class="tutorial-content">
			<p>영어는 감정분석에 영향력이 없어요:(</p>
			<p>일기 내용이 많을수록 분석의 정확도가 올라갑니다:)</p>
		</div>
		<div class="tutorial-close">
			<button class="tutorial-close__btn" @click.prevent="closeTutorial">
				시작하기
			</button>
		</div>
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
		closeTutorial() {
			this.$emit('close-tutorial');
		},
	},
};
</script>

<style lang="scss">
.tutorial-wrap {
	width: 95%;
	height: 97%;
	position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	border-radius: 1rem;
	color: #fff;
	font-size: 13px;
	background: rgba(43, 43, 43, 0.7);
	line-height: 1.5;
	box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
	z-index: 100;
}
.tutorial-title {
	position: absolute;
	top: 22%;
	left: 8%;
	width: 170px;
	.tutorial-title__arrow {
		position: absolute;
		top: -10%;
		left: -10%;
		transform: rotate(20deg);
	}
}
.tutorial-sticker {
	position: absolute;
	top: 24%;
	right: 1%;
	width: 120px;
	.tutorial-sticker__arrow {
		position: absolute;
		top: -18%;
		left: 50%;
		transform: rotate(180deg);
	}
}
.tutorial-music {
	position: absolute;
	top: 10%;
	right: 10%;
	width: 120px;
	.tutorial-music__arrow {
		position: absolute;
		bottom: -5%;
		right: 3%;
		transform: rotate(175deg);
	}
}
.tutorial-content {
	position: absolute;
	top: 55%;
	left: 10%;
	line-height: 2;
}
.tutorial-arrow {
	width: 15px;
}
.tutorial-close {
	position: absolute;
	bottom: 100px;
	left: 50%;
	transform: translate(-50%, 0);
	text-align: center;
	.tutorial-close__btn {
		border: none;
		color: #fff;
		font-size: 25px;
		background: none;
		&:hover {
			cursor: pointer;
		}
	}
}
</style>
