<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="save-diary">
				<p class="save-diary-comment">당신의 오늘 하루는</p>
				<p class="save-diary-comment">행복이군요 :)</p>
				<p class="save-diary-comment">
					"동방신기-행복"으로 마무리하는 건 어때요?
				</p>
				<div class="save-diary-emotion">
					<img src="@/assets/images/emotion/happy.png" alt="감정상태" />
				</div>
			</div>
			<button class="save-diary-change save-diary-btn" @click="onSaveDiary">
				오늘 하루 기록할게요
			</button>
			<button class="save-diary-change" @click="onOpenEmotion">
				오늘 감정 더 살펴볼래요
			</button>

			<div id="mainMenu" class="mainMenuOverlay floating2">
				<!-- <div class="navire floating3"></div> -->
				<div class="itemMenuBox bills">
					<img
						src="@/assets/images/emotion/sad.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<div class="itemMenuBox tarsheed">
					<img
						src="@/assets/images/emotion/smile.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<div class="itemMenuBox employees">
					<img
						src="@/assets/images/emotion/boring.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<div class="itemMenuBox location">
					<img
						src="@/assets/images/emotion/surprise.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<div class="itemMenuBox eservices">
					<img
						src="@/assets/images/emotion/angry.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<div class="itemMenuBox contact">
					<img
						src="@/assets/images/emotion/dislike.png"
						class="itemMenu "
						alt="감정상태"
					/>
				</div>
				<a
					href="javascript:void(0)"
					class="toggleMenu floating"
					@click="onCloseEmotion"
					><img
						src="@/assets/images/close2.svg"
						class="emotion-close-btn"
						alt="닫기버튼"
				/></a>
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click.prevent="closeTheme">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
		</section>
	</section>
</template>

<script>
import { createDiary } from '@/api/diary';

export default {
	data() {
		return {};
	},
	props: {
		open: Boolean,
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
		setUrl() {
			return `${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_API_URL}`;
		},
	},
	methods: {
		onOpenEmotion() {
			const mainMenu = document.querySelector('#mainMenu');
			mainMenu.classList.add('open');
		},
		onCloseEmotion() {
			const mainMenu = document.querySelector('#mainMenu');
			mainMenu.classList.remove('open');
		},
		closeTheme() {
			this.$emit('close-theme');
		},
		async onSaveDiary() {
			const { data } = await createDiary(this.diaryData);
			this.$router.push(`/diary/${data.id}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.toast-save {
	display: flex;
	justify-content: center;
	align-items: center;
}
.save-diary {
	margin-top: 8vh;
	text-align: center;
	.save-diary-comment {
		margin-bottom: 13px;
	}
	.save-diary-emotion {
		margin: 5vh;
	}
}
.save-diary-change {
	display: block;
	margin: 20px auto;
	width: 200px;
	height: 40px;
	border: none;
	border-radius: 50px;
	background: #f0f0f0;
	box-shadow: inset 4px 4px 4px #e4e3e3, inset -4px -4px 4px #f7f7f7;
}
.save-diary-btn {
	box-shadow: 7px 7px 15px #cccccc, -7px -7px 15px #ffffff;
}
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:200);
// .navire {
// 	background: url(https://res.cloudinary.com/dioieuprs/image/upload/v1471359656/navire_n02z6s.png)
// 		no-repeat;
// 	background-size: 100% auto;
// 	width: 120px;
// 	height: 100px;
// 	position: absolute;
// 	top: -50px;
// 	right: -130px;
// 	-webkit-transition: right 0.2s ease;
// 	transition: right 0.2s ease;
// }

// .mainMenuOverlay.open .navire {
// 	right: 70%;
// 	-webkit-transition: right 28s ease 1s;
// 	transition: right 28s ease 1s;
// }
/* ### main Menu Overlay */
.mainMenuOverlay {
	background-color: rgb(197, 195, 179);
	position: fixed;
	left: 0;
	right: 0;
	bottom: -60%;
	z-index: 999;
	height: 60%;
	box-shadow: 0 0 15px -3px rgba(197, 191, 135, 0.3);
	border-radius: 100% 100% 0 0 / 14% 14% 0 0;
	-webkit-transition: bottom 0.5s ease;
	transition: bottom 0.5s ease;
}

.mainMenuOverlay.open {
	bottom: 0;
}

.mainMenuOverlay .toggleMenu {
	display: block;
	/*background: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/sandwich.png) no-repeat center center #65B5D0;background-size: 23px auto;*/
	// border: 1px solid #fff;
	border-radius: 80px;
	width: 62px;
	height: 62px;
	position: absolute;
	top: 100px;
	left: 50%;
	margin: -31px 0 0 -31px;
	cursor: pointer;
	font-size: 24px;
	color: #fff;
	text-align: center;
	line-height: 62px;
	box-shadow: 0 0 0 10px rgba(255, 255, 255, 0.2) inset, 0 0 16px -4px #70592f;
	-webkit-transition: box-shadow 0.5s ease, top 0.5s ease;
	transition: box-shadow 0.5s ease, top 0.5s ease;
}

.mainMenuOverlay .toggleMenu:hover,
.mainMenuOverlay .toggleMenu:active {
}

.mainMenuOverlay.open .toggleMenu {
	top: 50%;
	// background-color: rgba(197, 191, 135, 0.84);
	.emotion-close-btn {
		margin-top: 20px;
		width: 20px;
	}
}

.mainMenuOverlay .itemMenuBox {
	// background: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/go2.png)
	// 	no-repeat center center;
	background-size: 28px auto;
	position: absolute;
	top: 50%;
	left: 50%;
	margin: -31px 0 0 -31px;
	height: 62px;
	width: 142px;
	text-align: right;
	border-radius: 40px;
	-webkit-transform-origin: 31px 31px;
	-ms-transform-origin: 31px 31px;
	transform-origin: 31px 31px;
	-webkit-transition: all 1s ease 0.4s;
	transition: all 1s ease 0.4s;
}

.mainMenuOverlay.open .itemMenuBox {
	// width: 182px;
	width: 48%;
	-webkit-transition: all 1s ease 0s;
	transition: all 1s ease 0s;
}

.mainMenuOverlay .itemMenuBox.bills {
	-webkit-transform: rotate(270deg);
	-ms-transform: rotate(270deg);
	transform: rotate(270deg);
}

.mainMenuOverlay .itemMenuBox.tarsheed {
	-webkit-transform: rotate(330deg);
	-ms-transform: rotate(330deg);
	transform: rotate(330deg);
}

.mainMenuOverlay .itemMenuBox.employees {
	-webkit-transform: rotate(30deg);
	-ms-transform: rotate(30deg);
	transform: rotate(30deg);
}

.mainMenuOverlay .itemMenuBox.location {
	-webkit-transform: rotate(90deg);
	-ms-transform: rotate(90deg);
	transform: rotate(90deg);
}

.mainMenuOverlay .itemMenuBox.eservices {
	-webkit-transform: rotate(150deg);
	-ms-transform: rotate(150deg);
	transform: rotate(150deg);
}

.mainMenuOverlay .itemMenuBox.contact {
	-webkit-transform: rotate(210deg);
	-ms-transform: rotate(210deg);
	transform: rotate(210deg);
}

.mainMenuOverlay .itemMenuBox .itemMenu {
	display: inline-block;
	border: 2px solid rgba(255, 255, 255, 0.6);
	border-radius: 40px;
	background-color: rgba(238, 237, 226, 1);
	background-repeat: no-repeat;
	background-position: center center;
	width: 62px;
	height: 62px;
	border-radius: 40px;
	transition: all 0.8s ease;
	color: #fff;
	font-size: 28px;
	line-height: 64px;
	text-align: center;
}

.mainMenuOverlay .itemMenuBox.bills .itemMenu {
	/*background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/file.png);
    background-size: 20px auto;*/
	-webkit-transform: rotate(90deg);
	-ms-transform: rotate(90deg);
	transform: rotate(90deg);
}

.mainMenuOverlay .itemMenuBox.tarsheed .itemMenu {
	/* background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/tarsheed.png); 
    background-size: 38px auto;*/
	-webkit-transform: rotate(30deg);
	-ms-transform: rotate(30deg);
	transform: rotate(30deg);
}

.mainMenuOverlay .itemMenuBox.employees .itemMenu {
	/*background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/employees.png);
    background-size: 38px auto;*/
	-webkit-transform: rotate(330deg);
	-ms-transform: rotate(330deg);
	transform: rotate(330deg);
}

.mainMenuOverlay .itemMenuBox.location .itemMenu {
	/*background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/marker.png);
    background-size: 24px auto;*/
	-webkit-transform: rotate(270deg);
	-ms-transform: rotate(270deg);
	transform: rotate(270deg);
}

.mainMenuOverlay .itemMenuBox.eservices .itemMenu {
	/*background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/mouse.png);
    background-size: 32px auto;*/
	-webkit-transform: rotate(210deg);
	-ms-transform: rotate(210deg);
	transform: rotate(210deg);
}

.mainMenuOverlay .itemMenuBox.contact .itemMenu {
	/*background-image: url(https://res.cloudinary.com/dioieuprs/image/upload/v1466688705/floating-menu/phone.png);
    background-size: 19px auto;*/
	-webkit-transform: rotate(150deg);
	-ms-transform: rotate(150deg);
	transform: rotate(150deg);
}

/* Hover */
.mainMenuOverlay .itemMenuBox.bills .itemMenu:hover {
	-webkit-transform: rotate(450deg);
	-ms-transform: rotate(450deg);
	transform: rotate(450deg);
}

.mainMenuOverlay .itemMenuBox.tarsheed .itemMenu:hover {
	-webkit-transform: rotate(390deg);
	-ms-transform: rotate(390deg);
	transform: rotate(390deg);
}

.mainMenuOverlay .itemMenuBox.employees .itemMenu:hover {
	-webkit-transform: rotate(690deg);
	-ms-transform: rotate(690deg);
	transform: rotate(690deg);
}

.mainMenuOverlay .itemMenuBox.location .itemMenu:hover {
	-webkit-transform: rotate(630deg);
	-ms-transform: rotate(630deg);
	transform: rotate(630deg);
}

.mainMenuOverlay .itemMenuBox.eservices .itemMenu:hover {
	-webkit-transform: rotate(570deg);
	-ms-transform: rotate(570deg);
	transform: rotate(570deg);
}

.mainMenuOverlay .itemMenuBox.contact .itemMenu:hover {
	-webkit-transform: rotate(510deg);
	-ms-transform: rotate(510deg);
	transform: rotate(510deg);
}

.floating {
	-webkit-animation-name: Floatingx;
	-webkit-animation-duration: 3s;
	-webkit-animation-iteration-count: infinite;
	-webkit-animation-timing-function: ease-in-out;
	-moz-animation-name: Floating;
	-moz-animation-duration: 3s;
	-moz-animation-iteration-count: infinite;
	-moz-animation-timing-function: ease-in-out;
}

@-webkit-keyframes Floatingx {
	from {
		-webkit-transform: translate(0, 0px);
	}
	65% {
		-webkit-transform: translate(0, 5px);
	}
	to {
		-webkit-transform: translate(0, -0px);
	}
}

@-moz-keyframes Floating {
	from {
		-moz-transform: translate(0, 0px);
	}
	65% {
		-moz-transform: translate(0, 5px);
	}
	to {
		-moz-transform: translate(0, -0px);
	}
}

.floating2 {
	-webkit-animation-name: Floatingx2;
	-webkit-animation-duration: 3s;
	-webkit-animation-iteration-count: infinite;
	-webkit-animation-timing-function: ease-in-out;
	-moz-animation-name: Floating2;
	-moz-animation-duration: 3s;
	-moz-animation-iteration-count: infinite;
	-moz-animation-timing-function: ease-in-out;
}

@-webkit-keyframes Floatingx2 {
	from {
		-webkit-transform: translate(0, 0px);
	}
	45% {
		-webkit-transform: translate(0, 8px);
	}
	to {
		-webkit-transform: translate(0, -0px);
	}
}

@-moz-keyframes Floating2 {
	from {
		-moz-transform: translate(0, 0px);
	}
	45% {
		-moz-transform: translate(0, 8px);
	}
	to {
		-moz-transform: translate(0, -0px);
	}
}

.floating3 {
	-webkit-animation-name: Floatingx3;
	-webkit-animation-duration: 3s;
	-webkit-animation-iteration-count: infinite;
	-webkit-animation-timing-function: ease-in-out;
	-moz-animation-name: Floating3;
	-moz-animation-duration: 3s;
	-moz-animation-iteration-count: infinite;
	-moz-animation-timing-function: ease-in-out;
}

@-webkit-keyframes Floatingx3 {
	from {
		-webkit-transform: translate(0, 0px);
	}
	50% {
		-webkit-transform: translate(2px, 4px);
	}
	to {
		-webkit-transform: translate(0, -0px);
	}
}

@-moz-keyframes Floating3 {
	from {
		-moz-transform: translate(0, 0px);
	}
	50% {
		-moz-transform: translate(2px, 4px);
	}
	to {
		-moz-transform: translate(0, -0px);
	}
}
</style>
