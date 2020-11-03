<template>
	<section>
		<div class="diary-wrap">
			<div class="diary-header">
				<input id="diary-header__title" type="text" v-model="diaryData.title" />
				<img
					src="@/assets/images/menu.svg"
					class="diary-header__menu"
					alt="메뉴"
					@click="onOpenMenu"
				/>
				<ul class="diary-header__func">
					<li>
						<img
							src="@/assets/images/pencil.svg"
							alt="편집"
							@click="openThemeModal"
						/>
					</li>
					<li>
						<img
							src="@/assets/images/sticker.svg"
							alt="스티커"
							@click="openStickerModal"
						/>
					</li>
					<li>
						<img
							src="@/assets/images/bgm.svg"
							alt="음악추가"
							@click="openMusicModal"
						/>
					</li>
				</ul>
			</div>
			<ToastMusic :open="openMusic" @close-music="openMusic = false" />
			<ToastSticker :open="openSticker" @close-sticker="openSticker = false" />
			<ToastTheme :open="openTheme" @close-theme="openTheme = false" />
			<div class="diary-image">
				<img
					class="diary-image__value"
					v-if="diaryImageUrl"
					:src="diaryImageUrl"
					alt="일기사진"
				/>
				<label for="diary-image__input" v-if="diaryImageFile">
					<img
						class="diary-image__value"
						:src="contentImg"
						alt="일기사진수정하기"
					/>
				</label>
				<input
					type="file"
					id="diary-image__input"
					ref="inputImage"
					name="diaryImage"
					@change="onChangeDiaryImage"
				/>
			</div>
			<div class="diary-text">
				<textarea
					name="diary-content"
					class="diary-text__content"
					rows="6"
					v-model="diaryData.content"
				></textarea>
			</div>
			<button class="diary-complete-btn" @click="onSaveDiary">
				오늘 하루 다시 기록할게요
			</button>
		</div>
	</section>
</template>

<script>
import bus from '@/utils/bus';
import ToastMusic from '@/components/modal/ToastMusic.vue';
import ToastSticker from '@/components/modal/ToastSticker.vue';
import ToastTheme from '@/components/modal/ToastTheme.vue';
import { fetchDiary, updateDiary } from '@/api/diary';

export default {
	data() {
		return {
			diaryImage: null,
			diaryImageUrl: null,
			diaryImageFile: true,
			openMusic: false,
			openSticker: false,
			openTheme: false,
			diaryData: {
				image: null,
				title: null,
				content: null,
				fontsize: 14,
				music_name: null,
				music_artist: null,
				postcolor: 1,
				font: 1,
				pattern: 1,
				emotion: 1,
				created: '2020-10-27',
			},
		};
	},
	props: {
		diaryId: Number,
	},
	components: {
		ToastMusic,
		ToastSticker,
		ToastTheme,
	},
	computed: {
		diaryDataImage() {
			return `${this.diaryData.image}`.substr(1);
		},
		contentImg() {
			if (this.diaryData.image) {
				return `${process.env.VUE_APP_API_URL}${this.diaryDataImage}`;
			} else {
				return `@/assets/images/logo3.png`;
			}
		},
	},
	methods: {
		onChangeDiaryImage() {
			this.diaryImage = this.$refs.inputImage.files[0];
			this.diaryImageUrl = URL.createObjectURL(this.diaryImage);
			this.diaryData.image = this.$refs.inputImage.files[0];
			this.diaryImageFile = false;
		},
		onOpenMenu() {
			const menu = document.querySelector('.diary-header__menu');
			const menus = document.querySelector('.diary-header__func');
			menu.style.display = 'none';
			menus.style.right = '0px';
			menus.style.transition = '.5s';
		},
		openMusicModal() {
			this.openMusic = true;
			this.openSticker = false;
			this.openTheme = false;
			bus.$emit('show:musicModal', '추천 음악입니다:)');
		},
		openStickerModal() {
			this.openMusic = false;
			this.openSticker = true;
			this.openTheme = false;
			bus.$emit('show:stickerModal', '스티커입니다:)');
		},
		openThemeModal() {
			this.openMusic = false;
			this.openSticker = false;
			this.openTheme = true;
			bus.$emit('show:themeModal', '테마 및 폰트입니다:)');
		},
		async onfetchDiary() {
			try {
				const { data } = await fetchDiary(this.diaryId);
				this.diaryData = data;
			} catch (error) {
				// bus.$emit('show:warning', '정보를 불러오는데 실패했어요 :(');
				console.log(error.response);
			}
		},
		async onSaveDiary() {
			try {
				const { data } = await updateDiary(this.diaryData, this.diaryId);
				this.$router.push(`/diary/${data.id}`);
			} catch (error) {
				// bus.$emit('show:warning', '정보를 불러오는데 실패했어요 :(');
				console.log(error.response);
			}
		},
	},
	created() {
		this.onfetchDiary();
	},
};
</script>

<style lang="scss">
.diary-wrap {
	display: flex;
	flex-direction: column;
	justify-content: center;
	padding: 18px;
	.diary-header {
		width: 100%;
		display: flex;
		justify-content: space-between;
		margin: 10px 0;
		position: relative;
		overflow: hidden;
		.diary-header__menu {
			width: 18px;
		}
		.diary-header__func {
			display: flex;
			margin: 0;
			padding: 0;
			position: absolute;
			top: 0;
			right: -110px;
			list-style-type: none;
			li {
				img {
					width: 18px;
					margin: 0 6px;
				}
			}
		}
		label {
			color: rgb(61, 61, 61);
			font-size: 14px;
		}
		#diary-header__title {
			width: 60%;
			margin-left: 8px;
			padding-bottom: 5px;
			border: none;
			border-bottom: 1px solid rgba(151, 151, 151, 0.5);
			background: #f0f0f0;
		}
	}
	.diary-image {
		display: flex;
		justify-content: center;
		height: 28vh;
		border-radius: 4px;
		background: rgba(151, 151, 151, 0.3);
		.diary-image__value {
			width: 100%;
			object-fit: cover;
		}
		label {
			display: flex;
			justify-content: center;
			&:hover {
				cursor: pointer;
			}
			.diary-image__file {
				height: 10vh;
				margin: 50px;
			}
		}
		#diary-image__input {
			position: absolute;
			width: 0;
			height: 0;
			padding: 0;
			overflow: hidden;
			border: 0;
		}
	}
	.diary-text {
		margin-top: 10px;
		.diary-text__content {
			width: 100%;
			padding: 5px 10px;
			line-height: 2;
			font-size: 15.5px;
			box-sizing: border-box;
			border: none;
			resize: none;
			background-attachment: local;
			background-image: linear-gradient(
					to right,
					#f0f0f0 10px,
					transparent 10px
				),
				linear-gradient(to left, #f0f0f0 10px, transparent 10px),
				repeating-linear-gradient(
					#f0f0f0,
					#f0f0f0 30px,
					#ccc 30px,
					#ccc 31px,
					#f0f0f0 31px
				);
		}
	}
	.diary-complete-btn {
		width: 75%;
		margin: 25px auto 0;
		padding: 12px;
		border: none;
		color: rgba(53, 53, 53, 1);
		border-radius: 20px;
		background: #f0f0f0;
		box-shadow: 5px 5px 9px #cccccc, -5px -5px 9px #ffffff;
	}
}
</style>
