<template>
	<section>
		<div class="diary-wrap" v-if="diaryData">
			<div class="diary-header">
				<p class="diary-header__dataTitle">
					{{ diaryData.title }}
				</p>
				<!-- <img
					src="@/assets/images/menu.svg"
					class="diary-header__menu"
					alt="메뉴"
					@click="onOpenMenu"
				/> -->
				<ul class="diary-header__func">
					<li>
						<img
							src="@/assets/images/trash.svg"
							alt="삭제"
							@click="onDeleteDiary"
						/>
					</li>
				</ul>
			</div>
			<div class="diary-image">
				<img class="diary-image__value" :src="contentImg" alt="일기사진" />
				<!-- <img class="diary-image__value" :src="canvasImg" alt="일기사진" /> -->
			</div>
			<div class="diary-text">
				<textarea
					class="read-diary-text__content"
					id="diaryContent"
					rows="6"
					readonly
					v-model="diaryData.content"
				>
				</textarea>
			</div>
			<MusicBar></MusicBar>
		</div>
	</section>
</template>

<script>
import MusicBar from '@/components/common/MusicBar.vue';
import bus from '@/utils/bus';
import { fetchDiary, deleteDiary } from '@/api/diary';
export default {
	components: {
		MusicBar,
	},
	data() {
		return {
			diaryData: null,
			diaryId: this.propsDiaryId ? this.propsDiaryId : this.diaryData.id,
			tracks: null,
		};
	},
	props: {
		propsDiaryId: Number,
	},
	computed: {
		diaryDataImage() {
			return `${this.diaryData.image}`.substr(1);
		},
		contentImg() {
			if (this.diaryData.image) {
				return `${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_AUTH_API_URL}${this.diaryDataImage}`;
			} else {
				return `${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_AUTH_API_URL}images/default.png`;
			}
		},
		// canvasImg() {
		// 	if (this.diaryData.sticker_image) {
		// 		return `${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_API_URL}${this.diaryDataImage}`;
		// 	}
		// },
		setUrl() {
			return `${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_API_URL}`;
		},
	},
	methods: {
		// onOpenMenu() {
		// 	const menu = document.querySelector('.diary-header__menu');
		// 	const menus = document.querySelector('.diary-header__func');
		// 	menu.style.display = 'none';
		// 	menus.style.right = '0px';
		// 	menus.style.transition = '.5s';
		// },
		async onFetchDiary() {
			try {
				const { data } = await fetchDiary(this.diaryId);
				console.log(data);
				if (data.search_music) {
					this.tracks = [
						{
							artist: data.search_music.artist,
							cover: data.search_music.cover,
							name: data.search_music.name,
							id: data.search_music.id,
							videoId: data.search_music.video_id,
							url: `https://youtube.com/watch?v=${data.search_music.video_id}`,
							emotion: data.search_music.emotion,
							favorited: data.search_music.liked,
							search: true,
						},
					];
				} else {
					this.tracks = [
						{
							artist: data.recommend_music.artist,
							cover: data.recommend_music.cover,
							name: data.recommend_music.name,
							id: data.recommend_music.id,
							videoId: data.recommend_music.video_id,
							url: `https://youtube.com/watch?v=${data.recommend_music.video_id}`,
							emotion: data.recommend_music.emotion,
							favorited: data.recommend_music.liked,
							search: false,
						},
					];
				}
				bus.$emit('show:musicplayer', this.tracks);
				this.diaryData = data;
			} catch (error) {
				bus.$emit('show:error', '정보를 불러오는데 실패했어요 :(');
				// console.log(error.response);
			}
		},
		onFetchStickers() {
			if (this.diaryData.stickers.length) {
				const stickerWrap = document.querySelector('.diary-image');
				let imgElem = document.createElement('img');
				imgElem.src = this.setUrl + this.diaryData.stickers[0].sticker.path;
				imgElem.style.width = `${this.diaryData.stickers[0].scaleX}px`;
				imgElem.style.height = `${this.diaryData.stickers[0].scaleY}px`;
				imgElem.style.position = `absolute`;
				imgElem.style.top = `${this.diaryData.stickers[0].y}px`;
				imgElem.style.left = `${this.diaryData.stickers[0].x}px`;
				imgElem.style.transform = `rotate(${this.diaryData.stickers[0].rotation}deg)`;
				console.log('sticker', this.diaryData.stickers[0]);
				stickerWrap.appendChild(imgElem);
			}
		},
		onFetchFont() {
			const title = document.querySelector('.diary-header__dataTitle');
			const content = document.querySelector('#diaryContent');

			title.style.fontFamily = this.diaryData.font.name;
			content.style.fontFamily = this.diaryData.font.name;
		},
		onFetchPaper() {
			const content = document.querySelector('#diaryContent');

			if (this.diaryData.pattern.path) {
				content.style.background = `url(${process.env.VUE_APP_SERVER_URL}${process.env.VUE_APP_API_URL}${this.diaryData.pattern.path}) center`;
			}
		},
		async onDeleteDiary() {
			try {
				await deleteDiary(this.diaryId);
				this.$router.push({ name: 'calendar' });
			} catch (error) {
				bus.$emit('show:error', '삭제를 실패했어요 :(');
				// console.log(error.response.data);
			}
		},
	},
	created() {
		this.onFetchDiary();
	},
	updated() {
		this.onFetchStickers();
		this.onFetchFont();
		this.onFetchPaper();
	},
};
</script>

<style lang="scss" scoped>
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
		.diary-header__dataTitle {
			margin-left: 10px;
		}
		// .diary-header__menu {
		// 	width: 18px;
		// }
		.diary-header__func {
			display: flex;
			margin: 0;
			padding: 0;
			position: absolute;
			top: 0;
			right: 0;
			list-style-type: none;
			li {
				img {
					width: 16px;
					margin: 0 6px;
				}
			}
		}
	}
	.diary-image {
		display: flex;
		justify-content: center;
		margin: 10px 0;
		height: 28vh;
		border-radius: 4px;
		background: rgba(151, 151, 151, 0.3);
		position: relative;
		.diary-image__value {
			width: 100%;
			border-radius: 4px;
			object-fit: cover;
		}
	}
	.diary-text {
		margin-top: 10px;
		.read-diary-text__content {
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
					var(--default-color) 10px,
					transparent 10px
				),
				linear-gradient(to left, var(--default-color) 10px, transparent 10px),
				repeating-linear-gradient(
					var(--default-color),
					var(--default-color) 30px,
					#ccc 30px,
					#ccc 31px,
					var(--default-color) 31px
				);
			&:focus {
				outline: none;
			}
		}
	}
}
</style>
