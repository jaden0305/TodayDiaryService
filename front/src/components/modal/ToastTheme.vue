<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-themes">
				<label for="toast-theme__bg">테마</label>
				<input
					type="radio"
					name="theme"
					id="toast-theme__bg"
					value="bg"
					v-model="selectedTheme"
				/>
				<label for="toast-theme__font">폰트</label>
				<input
					type="radio"
					name="theme"
					id="toast-theme__font"
					value="font"
					v-model="selectedTheme"
				/>
			</div>
			<div class="toast-theme">
				<div v-if="selectedTheme === 'bg'" class="toast-theme__bg">
					테마
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
</style>
