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
					<ul class="toast-theme__ul">
						<li v-for="paper in papers" :key="paper.id">
							<label
								:for="`toast-theme__${paper.id}`"
								class="preview-paper-wrap"
							>
								<img
									:src="`${setUrl}${paper.preview_path}`"
									alt="속지디자인"
									class="preview-paper"
									@click="selectPaper(paper.id)"
								/>
							</label>
							<input
								type="radio"
								name="paper"
								:id="`toast-theme__${paper.id}`"
								:value="paper"
								v-model="selectedPaper"
								hidden
							/>
						</li>
					</ul>
				</div>
				<div v-else class="toast-theme__fonts">
					<p class="toast-theme__example">
						오늘 하루의 폰트를 골라주세요
					</p>
					<ul>
						<li v-for="font in fonts" :key="font.id">
							<input
								type="radio"
								name="font"
								:id="`toast-theme__${font.name}`"
								:value="font"
								v-model="selectedFont"
							/>
							<label
								:for="`toast-theme__${font.name}`"
								:style="`font-family:${font.name}`"
								>{{ font.name }}</label
							>
						</li>
					</ul>
				</div>
			</div>
			<div class="toast-theme__complete">
				<button @click.prevent="submitTheme">
					선택한 거 적용할래요
				</button>
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
import bus from '@/utils/bus';
import { fetchFonts, fetchPapers } from '@/api/diary';
export default {
	data() {
		return {
			selectedTheme: 'bg',
			fonts: [],
			papers: [],
			selectedFont: {
				id: 1,
				name: 'Poor Story',
			},
			selectedPaper: {
				id: 1,
				path: 'media/paper/1.png',
			},
		};
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
		closeTheme() {
			this.$emit('close-theme');
		},
		submitTheme() {
			this.$emit('submit-theme', this.selectedFont, this.selectedPaper);
		},
		async onFetchFonts() {
			try {
				const { data } = await fetchFonts();
				this.fonts = data;
			} catch (err) {
				bus.$emit('show:error', '폰트를 불러오는데 실패했어요 :(');
			}
		},
		async onFetchPapers() {
			try {
				const { data } = await fetchPapers();
				this.papers = data;
			} catch (err) {
				bus.$emit('show:error', '테마를 불러오는데 실패했어요 :(');
			}
		},
		selectPaper(id) {
			const papers = document.querySelectorAll('.preview-paper');

			papers.forEach(paper => {
				if (paper.classList.contains('select-paper')) {
					paper.classList.remove('select-paper');
				}
			});
			papers[id - 1].classList.add('select-paper');
		},
	},
	watch: {
		selectedFont: function() {
			const sentence = document.querySelector('.toast-theme__example');

			sentence.style.fontFamily = this.selectedFont.name;
		},
	},
	created() {
		this.onFetchFonts();
		this.onFetchPapers();
	},
};
</script>

<style lang="scss" scoped>
.toast-theme__fonts {
	.toast-theme__example {
		margin: 40px 0 30px;
		text-align: center;
		font-family: 'Nanum Gothic', sans-serif;
	}
	li {
		margin: 8px 0;
	}
}
.toast-theme {
	margin-top: 20px;
}
.toast-themes {
	display: flex;
	justify-content: center;
	align-items: center;
}
.toast-theme__ul {
	display: flex;
	flex-wrap: wrap;
}
.preview-paper-wrap {
	.preview-paper {
		width: 70px;
		height: 100px;
		margin: 10px;
		object-fit: cover;
		cursor: pointer;
		&:active {
			border-radius: 4px;
			border: 3px solid rgb(168, 168, 168);
		}
	}
}
.select-paper {
	border-radius: 4px;
	border: 3px solid rgb(185, 185, 185);
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
.toast-theme__complete {
	text-align: center;
	button {
		width: 75%;
		margin: 50px auto 0;
		padding: 12px;
		border: none;
		color: rgba(53, 53, 53, 1);
		border-radius: 20px;
		background: var(--default-color);
		box-shadow: 5px 5px 9px #cccccc, -5px -5px 9px #ffffff;
	}
}
</style>
