<template>
	<section class="toast" v-if="diaryData" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="save-diary">
				<p class="save-diary-comment">당신의 오늘 하루는</p>
				<p class="save-diary-comment">{{ diaryData.user_emotion }}이군요 :)</p>
				<p class="save-diary-comment">
					{{ diaryData.recommend_music.artist }}의
					{{ diaryData.recommend_music.name }}으로 마무리하는 건 어때요?
				</p>
				<div class="save-diary-emotion">
					<img
						v-if="diaryData.user_emotion"
						:src="
							require(`@/assets/images/emotion/${diaryData.user_emotion}.png`)
						"
						alt="감정상태"
					/>
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
				<div
					v-for="(value, idx) in emotionList(diaryData.user_emotion)"
					:key="idx"
					class="itemMenuBox"
					:class="emotionDesign[idx]"
				>
					<img
						:src="require(`@/assets/images/emotion/${idx + 1}.png`)"
						class="itemMenu "
						alt="감정상태"
						@click="onReselectEmotion(idx + 1)"
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
import { reselectEmotion } from '@/api/analysis';

export default {
	data() {
		return {
			emotion: ['행복', '슬픔', '기쁨', '무료함', '화남', '놀람', '공포'],
			emotionDesign: [
				'bills',
				'tarsheed',
				'employees',
				'location',
				'eservices',
				'contact',
			],
		};
	},
	props: {
		open: Boolean,
		diaryData: Object,
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

			// for (let key in this.emotion) {
			// 	if (key != this.diaryData.user_emotion) {
			// 		const itemMenuBox = document.createElement('div');
			// 		const emotionImage = document.createElement('img');
			// 		itemMenuBox.classList.add('itemMenuBox');
			// 		itemMenuBox.classList.add(this.emotionDesign[key - 1]);
			// 		emotionImage.src = `@/assets/images/emotion/${key}.png`;
			// 		emotionImage.alt = '감정이모티콘';
			// 		emotionImage.classList.add('itemMenu');
			// 		itemMenuBox.appendChild(emotionImage);
			// 		mainMenu.appendChild(itemMenuBox);
			// 	}
			// }
		},
		onCloseEmotion() {
			const mainMenu = document.querySelector('#mainMenu');
			mainMenu.classList.remove('open');
		},
		closeTheme() {
			this.$emit('close-theme');
		},
		async onSaveDiary() {
			try {
				this.diaryData.created = this.$route.query.day;
				const { data } = await createDiary(this.diaryData);
				this.$router.push(`/diary/${data.id}`);
			} catch (err) {
				console.log(err.response);
			}
		},
		async onReselectEmotion(id) {
			try {
				const { data } = await reselectEmotion(id);
				this.diaryData.user_emotion = data.emotion;
				this.diaryData.recommend_music.artist = data.recommend_music.artist;
				this.diaryData.recommend_music.name = data.recommend_music.name;

				this.onCloseEmotion();
			} catch (err) {
				console.log(err.response);
			}
		},
		emotionList(idx) {
			let emotion = [...this.emotion];
			emotion.splice(idx - 1, 1);
			return emotion;
		},
	},
	created() {
		console.log(this.diaryData);
	},
};
</script>

<style lang="scss">
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
