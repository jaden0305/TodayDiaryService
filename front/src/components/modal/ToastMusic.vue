<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div id="player-back-container1">
				<div class="back-wrap__music">
					<div class="toast-search">
						<input
							class="toast-search__input"
							placeholder="음악을 검색하세요"
							type="text"
							v-model="searchMusic"
							@keypress.enter="searchYoutube"
						/>
						<button class="toast-search__btn">
							<img
								@click="searchYoutube"
								src="@/assets/images/search.svg"
								alt=""
							/>
						</button>
					</div>
					<div class="back-playlist">
						<div
							class="back-song"
							:key="i"
							v-for="(music, i) in musicList"
							@click="musicSelect(music)"
						>
							<div
								class="back-song__img"
								:style="{
									backgroundImage: `url(${music.snippet.thumbnails.default.url})`,
								}"
							></div>
							<div class="back-song__info">
								<span class="back-song__name">{{
									music.snippet.title | musicTruncate
								}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<div class="toast-close">
			<button class="toast-close__btn" @click="closeMusic">
				<img @click="closeMusic" src="@/assets/images/delete.svg" alt="" />
			</button>
		</div>
	</section>
</template>

<script>
import _ from 'lodash';
import { youtubeSearch } from '@/api/youtube';
export default {
	props: {
		open: Boolean,
	},
	data() {
		return {
			searchMusic: '',
			musicList: [],
			selectMusic: {
				name: null,
				artist: null,
				cover: null,
				videoId: null,
				emotion: 8,
			},
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		closeMusic() {
			this.$emit('close-music');
		},
		async searchYoutube() {
			const { data } = await youtubeSearch(this.searchMusic);
			console.log(data);
			this.musicList = data.items;
			this.musicList = this.musicList.map(music => {
				music.snippet.title = _.unescape(music.snippet.title, 'text/html');
				return music;
			});
		},
		musicSelect(music) {
			this.selectMusic.name = music.snippet.title;
			this.selectMusic.artist = null;
			this.selectMusic.cover = music.snippet.thumbnails.high.url;
			this.selectMusic.videoId = music.id.videoId;
			this.selectMusic.emotion = 8;
			// this.searchMusic.favorited = false;
			this.$emit('selectMusic', this.selectMusic);
			this.$emit('close-music');
		},
	},
};
</script>

<style lang="scss">
.toast {
	width: 85%;
	height: 550px;
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	top: 53%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: #646464;
	border-radius: 1rem;
	background: #f0f0f0;
	box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
	z-index: 100;
	.toast-wrap {
		width: 90%;
		height: 85%;
		position: relative;
		.toast-search {
			margin: 20px 20px 50px;
			position: relative;
			.toast-search__input {
				width: 100%;
				padding: 5px 10px;
				font-size: 14px;
				line-height: 2.3;
				border: none;
				border-radius: 5px;
				background: #f0f0f0;
				box-shadow: inset 5px 5px 5px #d3d3d3, inset -5px -5px 5px #ffffff;
			}
			.toast-search__btn {
				position: absolute;
				top: 12px;
				right: 6px;
				border: none;
				background: none;
				img {
					width: 20px;
				}
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
.toast-close {
	position: absolute;
	bottom: 10px;
	left: 50%;
	z-index: 10;
	transform: translate(-50%, 0);
	/* margin-top: 30px; */
	text-align: center;
	.toast-close__btn {
		border: none;
		background: none;
		img {
			width: 30px;
		}
	}
}
.toast.none {
	display: none;
}
#player-back-container1 {
	position: absolute;
	top: 0;
	right: 0;
	left: 0;
	bottom: 0;
	background: #f0f0f0;
	z-index: 10;
	border-radius: 12px;
}
.back-wrap__music {
	position: relative;
	width: 100%;
	height: 100%;
	overflow: hidden;
	.back-playlist {
		width: 100%;
		height: calc(100% - 70px);
		overflow-y: scroll;
		.back-song {
			width: 100%;
			height: 64px;
			display: flex;
			padding: 8px 0 8px;
			border-bottom: 1px solid rgba(#71829e, 0.1);
			.back-song__img {
				width: 48px;
				height: 48px;
				background-repeat: no-repeat !important;
				background-position: center !important;
				background-size: cover !important;
				border-radius: 3px;
				margin-left: 1rem;
			}
			.back-song__info {
				display: flex;
				flex-direction: column;
				justify-content: space-around;
				margin-left: 1rem;
				/* overflow: hidden;
				white-space: nowrap;
				text-overflow: ellipsis; */
				.back-song__name {
					/* overflow: hidden;
					white-space: nowrap;
					text-overflow: ellipsis; */
					font-size: 1.1rem;
					font-weight: 600;
					margin-bottom: 4px;
				}
				.back-song__artist {
					font-size: 0.8rem;
					color: rgba(#71829e, 0.7);
				}
			}
		}
	}
}
</style>
