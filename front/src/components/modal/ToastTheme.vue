<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-themes">
				<div class="toast-themes__box">
					<input
						class="toast-themes__input"
						type="radio"
						name="theme"
						id="toast-theme__bg"
						value="bg"
						v-model="selectedTheme"
					/>
					<label class="toast-themes__label" for="toast-theme__bg">
						<div class="toast-themes__indicator"></div>
						<span class="toast-themes__text">테마</span>
					</label>
				</div>
				<div class="toast-themes__box">
					<input
						class="toast-themes__input"
						type="radio"
						name="theme"
						id="toast-theme__font"
						value="font"
						v-model="selectedTheme"
					/>
					<label class="toast-themes__label" for="toast-theme__font">
						<div class="toast-themes__indicator"></div>
						<span class="toast-themes__text">폰트</span>
					</label>
				</div>
			</div>
			<div class="toast-theme">
				<div v-if="selectedTheme === 'bg'" class="toast-theme__bg">
					<ul>
						<li>
							<label for="toast-theme__color1" class="color1">Gaegu</label>
							<input
								type="radio"
								name="themeColor"
								id="toast-theme__color1"
								value="Gaegu"
								v-model="selectedFont"
							/>
						</li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
						<li></li>
					</ul>
				</div>
				<div v-else class="toast-theme__fonts">
					<p class="toast-theme__example">
						오늘 하루의 폰트를 골라주세요
					</p>
					<ul>
						<li>
							<label for="toast-theme__font1" class="example1">Gaegu</label>
							<input
								type="radio"
								name="font"
								id="toast-theme__font1"
								value="Gaegu"
								v-model="selectedFont"
							/>
						</li>
						<li>
							<label for="toast-theme__font2" class="example2"
								>Nanum Gothic</label
							>
							<input
								type="radio"
								name="font"
								id="toast-theme__font2"
								value="NanumGothic"
								v-model="selectedFont"
							/>
						</li>
						<li>
							<label for="toast-theme__font3" class="example3"
								>Nanum Myeongjo</label
							>
							<input
								type="radio"
								name="font"
								id="toast-theme__font3"
								value="NanumMyeongjo"
								v-model="selectedFont"
							/>
						</li>
						<li>
							<label for="toast-theme__font4" class="example4"
								>Nanum Pen Script</label
							>
							<input
								type="radio"
								name="font"
								id="toast-theme__font4"
								value="NanumPenScript"
								v-model="selectedFont"
							/>
						</li>
						<li>
							<label for="toast-theme__font5" class="example5"
								>Poor Story</label
							>
							<input
								type="radio"
								name="font"
								id="toast-theme__font5"
								value="PoorStory"
								v-model="selectedFont"
							/>
						</li>
					</ul>
				</div>
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
	data() {
		return {
			selectedTheme: 'bg',
			selectedFont: null,
		};
	},
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
	watch: {
		selectedFont: function() {
			const sentence = document.querySelector('.toast-theme__example');
			if (this.selectedFont === 'Gaegu') {
				sentence.style.fontFamily = 'Gaegu, cursive';
			} else if (this.selectedFont === 'NanumMyeongjo') {
				sentence.style.fontFamily = 'Nanum Myeongjo, serif';
			} else if (this.selectedFont === 'NanumPenScript') {
				sentence.style.fontFamily = 'Nanum Pen Script, cursive';
			} else if (this.selectedFont === 'PoorStory') {
				sentence.style.fontFamily = 'Poor Story, cursive';
			} else {
				sentence.style.fontFamily = 'Nanum Gothic, cursive';
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.toast-theme__fonts {
	.toast-theme__example {
		font-family: 'Nanum Gothic', sans-serif;
	}
	.example1 {
		font-family: 'Gaegu, cursive';
	}
	.example2 {
		font-family: 'Nanum Gothic, cursive';
	}
	.example3 {
		font-family: 'Nanum Myeongjo, serif';
	}
	.example4 {
		font-family: 'Nanum Pen Script, cursive';
	}
	.example5 {
		font-family: 'Poor Story, cursive';
	}
}
.toast-themes {
	display: flex;
	justify-content: center;
	align-items: center;
}
.toast-themes__box {
}
.toast-themes__input {
	position: absolute;
	top: 0;
	right: 0;
	opacity: 0;
	pointer-events: none;
}
.toast-themes__label {
	display: inline-flex;
	align-items: center;
	cursor: pointer;
	color: #394a56;
}
.toast-themes__indicator {
	position: relative;
	border-radius: 50%;
	height: 20px;
	width: 20px;
	box-shadow: -8px -4px 8px 0px #ffffff, 8px 4px 12px 0px #d1d9e6;
	overflow: hidden;
}
.toast-themes__text {
	margin-left: 8px;
	margin-right: 16px;
	opacity: 0.6;
	transition: opacity 0.2s linear, transform 0.2s ease-out;
}
.toast-themes__rightzero {
	margin-right: 0;
}
.toast-themes__indicator::before,
.toast-themes__indicator::after {
	content: '';
	position: absolute;
	top: 10%;
	left: 10%;
	height: 80%;
	width: 80%;
	border-radius: 50%;
}
.toast-themes__indicator::before {
	box-shadow: -4px -2px 4px 0px #d1d9e6, 4px 2px 8px 0px #fff;
}
.toast-themes__indicator::after {
	background-color: #ecf0f3;
	box-shadow: -4px -2px 4px 0px #fff, 4px 2px 8px 0px #d1d9e6;
	transform: scale3d(1, 1, 1);
	transition: opacity 0.25s ease-in-out, transform 0.25s ease-in-out;
}
.toast-themes__input:checked
	~ .toast-themes__label
	.toast-themes__indicator::after {
	transform: scale3d(0.975, 0.975, 1) translate3d(0, 10%, 0);
	opacity: 0;
}
.toast-themes__label:hover .toast-themes__text {
	opacity: 1;
}
</style>
