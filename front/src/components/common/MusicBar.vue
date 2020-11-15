<template>
	<div class="toast1" :class="toastAnimationClass">
		<youtube
			v-if="tracks"
			:player-vars="playerVars"
			:video-id="currentTrack.videoId"
			ref="player"
			@ended="nextTrack"
		></youtube>
		<div class="player slide-out-bottom" v-if="currentTrack">
			<div class="player__title" v-hammer:swipe.down="swipeDown">
				<span class="player__title__text">플레이어</span>
			</div>
			<div class="player__top">
				<div class="player-cover">
					<section class="player-cover__content">
						<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
						<div
							class="player-cover__item"
							:style="{ backgroundImage: `url(${currentTrack.cover})` }"
						></div>
					</section>
				</div>
				<div class="player-controls">
					<div
						class="player-controls__item -favorite"
						:class="{ active: currentTrack.favorited }"
						@click="favorite"
					>
						<svg class="icon">
							<use xlink:href="#icon-heart-o"></use>
						</svg>
					</div>
					<a
						:href="currentTrack.url"
						target="_blank"
						class="player-controls__item"
					>
						<svg class="icon">
							<use xlink:href="#icon-link"></use>
						</svg>
					</a>
					<div class="player-controls__item -xl js-play" @click="play">
						<i class="player-font icon ion-md-play" v-if="!isTimerPlaying"></i>
						<div class="player-font" v-else>
							<i class="icon ion-md-pause player-pause"></i>
						</div>
					</div>
				</div>
				<div class="progress" ref="progress">
					<div class="progress__top">
						<div class="album-info" v-if="currentTrack">
							<div class="album-info__name">{{ currentTrack.artist }}</div>
							<div class="album-info__track">{{ currentTrack.name }}</div>
						</div>
					</div>
				</div>
			</div>
			<div v-cloak></div>
			<symbol id="icon-link" viewBox="0 0 32 32">
				<title>link</title>
				<path
					d="M23.584 17.92c0 0.864 0 1.728 0 2.56 0 1.312 0 2.656 0 3.968 0 0.352 0.032 0.736-0.032 1.12 0.032-0.16 0.032-0.288 0.064-0.448-0.032 0.224-0.096 0.448-0.16 0.64 0.064-0.128 0.128-0.256 0.16-0.416-0.096 0.192-0.192 0.384-0.32 0.576 0.096-0.128 0.16-0.224 0.256-0.352-0.128 0.16-0.288 0.32-0.48 0.48 0.128-0.096 0.224-0.16 0.352-0.256-0.192 0.128-0.352 0.256-0.576 0.32 0.128-0.064 0.256-0.128 0.416-0.16-0.224 0.096-0.416 0.16-0.64 0.16 0.16-0.032 0.288-0.032 0.448-0.064-0.256 0.032-0.512 0.032-0.768 0.032-0.448 0-0.896 0-1.312 0-1.472 0-2.976 0-4.448 0-1.824 0-3.616 0-5.44 0-1.568 0-3.104 0-4.672 0-0.736 0-1.44 0-2.176 0-0.128 0-0.224 0-0.352-0.032 0.16 0.032 0.288 0.032 0.448 0.064-0.224-0.032-0.448-0.096-0.64-0.16 0.128 0.064 0.256 0.128 0.416 0.16-0.192-0.096-0.384-0.192-0.576-0.32 0.128 0.096 0.224 0.16 0.352 0.256-0.16-0.128-0.32-0.288-0.48-0.48 0.096 0.128 0.16 0.224 0.256 0.352-0.128-0.192-0.256-0.352-0.32-0.576 0.064 0.128 0.128 0.256 0.16 0.416-0.096-0.224-0.16-0.416-0.16-0.64 0.032 0.16 0.032 0.288 0.064 0.448-0.032-0.256-0.032-0.512-0.032-0.768 0-0.448 0-0.896 0-1.312 0-1.472 0-2.976 0-4.448 0-1.824 0-3.616 0-5.44 0-1.568 0-3.104 0-4.672 0-0.736 0-1.44 0-2.176 0-0.128 0-0.224 0.032-0.352-0.032 0.16-0.032 0.288-0.064 0.448 0.032-0.224 0.096-0.448 0.16-0.64-0.064 0.128-0.128 0.256-0.16 0.416 0.096-0.192 0.192-0.384 0.32-0.576-0.096 0.128-0.16 0.224-0.256 0.352 0.128-0.16 0.288-0.32 0.48-0.48-0.128 0.096-0.224 0.16-0.352 0.256 0.192-0.128 0.352-0.256 0.576-0.32-0.128 0.064-0.256 0.128-0.416 0.16 0.224-0.096 0.416-0.16 0.64-0.16-0.16 0.032-0.288 0.032-0.448 0.064 0.48-0.064 0.96-0.032 1.44-0.032 0.992 0 1.952 0 2.944 0 1.216 0 2.432 0 3.616 0 1.056 0 2.112 0 3.168 0 0.512 0 1.024 0 1.536 0 0 0 0 0 0.032 0 0.448 0 0.896-0.192 1.184-0.48s0.512-0.768 0.48-1.184c-0.032-0.448-0.16-0.896-0.48-1.184s-0.736-0.48-1.184-0.48c-0.64 0-1.28 0-1.92 0-1.408 0-2.816 0-4.224 0-1.44 0-2.848 0-4.256 0-0.672 0-1.344 0-2.016 0-0.736 0-1.472 0.192-2.112 0.576s-1.216 0.96-1.568 1.6c-0.384 0.64-0.544 1.376-0.544 2.144 0 0.672 0 1.376 0 2.048 0 1.28 0 2.56 0 3.84 0 1.504 0 3.040 0 4.544 0 1.408 0 2.848 0 4.256 0 0.992 0 1.952 0 2.944 0 0.224 0 0.448 0 0.64 0 0.864 0.224 1.76 0.768 2.464 0.16 0.192 0.288 0.384 0.48 0.576s0.384 0.352 0.608 0.512c0.32 0.224 0.64 0.384 1.024 0.512 0.448 0.16 0.928 0.224 1.408 0.224 0.16 0 0.32 0 0.48 0 0.896 0 1.792 0 2.72 0 1.376 0 2.784 0 4.16 0 1.536 0 3.040 0 4.576 0 1.312 0 2.656 0 3.968 0 0.768 0 1.536 0 2.336 0 0.416 0 0.832-0.032 1.248-0.128 1.504-0.32 2.784-1.6 3.104-3.104 0.128-0.544 0.128-1.056 0.128-1.568 0-0.608 0-1.184 0-1.792 0-1.408 0-2.816 0-4.224 0-0.256 0-0.512 0-0.768 0-0.448-0.192-0.896-0.48-1.184s-0.768-0.512-1.184-0.48c-0.448 0.032-0.896 0.16-1.184 0.48-0.384 0.384-0.576 0.768-0.576 1.248v0z"
				></path>
				<path
					d="M32 11.232c0-0.8 0-1.568 0-2.368 0-1.248 0-2.528 0-3.776 0-0.288 0-0.576 0-0.864 0-0.896-0.768-1.696-1.696-1.696-0.8 0-1.568 0-2.368 0-1.248 0-2.528 0-3.776 0-0.288 0-0.576 0-0.864 0-0.448 0-0.896 0.192-1.184 0.48s-0.512 0.768-0.48 1.184c0.032 0.448 0.16 0.896 0.48 1.184s0.736 0.48 1.184 0.48c0.8 0 1.568 0 2.368 0 1.248 0 2.528 0 3.776 0 0.288 0 0.576 0 0.864 0-0.576-0.576-1.12-1.12-1.696-1.696 0 0.8 0 1.568 0 2.368 0 1.248 0 2.528 0 3.776 0 0.288 0 0.576 0 0.864 0 0.448 0.192 0.896 0.48 1.184s0.768 0.512 1.184 0.48c0.448-0.032 0.896-0.16 1.184-0.48 0.352-0.256 0.544-0.64 0.544-1.12v0z"
				></path>
				<path
					d="M15.040 21.888c0.16-0.16 0.288-0.288 0.448-0.448 0.384-0.384 0.8-0.8 1.184-1.184 0.608-0.608 1.184-1.184 1.792-1.792 0.704-0.704 1.44-1.44 2.176-2.176 0.8-0.8 1.568-1.568 2.368-2.368s1.6-1.6 2.4-2.4c0.736-0.736 1.504-1.504 2.24-2.24 0.64-0.64 1.248-1.248 1.888-1.888 0.448-0.448 0.896-0.896 1.344-1.344 0.224-0.224 0.448-0.416 0.64-0.64 0 0 0.032-0.032 0.032-0.032 0.32-0.32 0.48-0.768 0.48-1.184s-0.192-0.896-0.48-1.184c-0.32-0.288-0.736-0.512-1.184-0.48-0.512 0.032-0.928 0.16-1.248 0.48-0.16 0.16-0.288 0.288-0.448 0.448-0.384 0.384-0.8 0.8-1.184 1.184-0.608 0.608-1.184 1.184-1.792 1.792-0.704 0.704-1.44 1.44-2.176 2.176-0.8 0.8-1.568 1.568-2.368 2.368s-1.6 1.6-2.4 2.4c-0.736 0.736-1.504 1.504-2.24 2.24-0.64 0.64-1.248 1.248-1.888 1.888-0.448 0.448-0.896 0.896-1.344 1.344-0.224 0.224-0.448 0.416-0.64 0.64 0 0-0.032 0.032-0.032 0.032-0.32 0.32-0.48 0.768-0.48 1.184s0.192 0.896 0.48 1.184c0.32 0.288 0.736 0.512 1.184 0.48 0.48 0 0.928-0.16 1.248-0.48v0z"
				></path>
			</symbol>
			<symbol id="icon-heart-o" viewBox="0 0 32 32">
				<title>icon-heart-o</title>
				<path
					d="M22.88 1.952c-2.72 0-5.184 1.28-6.88 3.456-1.696-2.176-4.16-3.456-6.88-3.456-4.48 0-9.024 3.648-9.024 10.592 0 7.232 7.776 12.704 15.072 17.248 0.256 0.16 0.544 0.256 0.832 0.256s0.576-0.096 0.832-0.256c7.296-4.544 15.072-10.016 15.072-17.248 0-6.944-4.544-10.592-9.024-10.592zM16 26.56c-4.864-3.072-12.736-8.288-12.736-14.016 0-5.088 3.040-7.424 5.824-7.424 2.368 0 4.384 1.504 5.408 4.032 0.256 0.608 0.832 0.992 1.472 0.992s1.248-0.384 1.472-0.992c1.024-2.528 3.040-4.032 5.408-4.032 2.816 0 5.824 2.304 5.824 7.424 0.064 5.728-7.808 10.976-12.672 14.016z"
				></path>
				<path
					d="M16 30.144c-0.32 0-0.64-0.096-0.896-0.256-7.296-4.576-15.104-10.048-15.104-17.344 0-7.008 4.576-10.688 9.12-10.688 2.656 0 5.152 1.216 6.88 3.392 1.728-2.144 4.224-3.392 6.88-3.392 4.544 0 9.12 3.68 9.12 10.688 0 7.296-7.808 12.768-15.104 17.344-0.256 0.16-0.576 0.256-0.896 0.256zM9.12 2.048c-4.448 0-8.928 3.616-8.928 10.496 0 7.168 7.744 12.64 15.008 17.152 0.48 0.288 1.12 0.288 1.568 0 7.264-4.544 15.008-9.984 15.008-17.152 0-6.88-4.48-10.496-8.928-10.496-2.656 0-5.088 1.216-6.816 3.392l-0.032 0.128-0.064-0.096c-1.696-2.176-4.192-3.424-6.816-3.424zM16 26.688l-0.064-0.032c-3.808-2.4-12.768-8.032-12.768-14.112 0-5.152 3.072-7.52 5.952-7.52 2.432 0 4.48 1.536 5.504 4.096 0.224 0.576 0.768 0.928 1.376 0.928s1.152-0.384 1.376-0.928c1.024-2.56 3.072-4.096 5.504-4.096 2.848 0 5.952 2.336 5.952 7.52 0 6.080-8.96 11.712-12.768 14.112l-0.064 0.032zM9.12 5.248c-2.752 0-5.728 2.304-5.728 7.328 0 5.952 8.8 11.488 12.608 13.92 3.808-2.4 12.608-7.968 12.608-13.92 0-5.024-2.976-7.328-5.728-7.328-2.336 0-4.32 1.472-5.312 3.968-0.256 0.64-0.864 1.056-1.568 1.056s-1.312-0.416-1.568-1.056c-0.992-2.496-2.976-3.968-5.312-3.968z"
				></path>
				<path
					d="M6.816 20.704c0.384 0.288 0.512 0.704 0.48 1.12 0.224 0.256 0.384 0.608 0.384 0.96 0 0.032 0 0.032 0 0.064 0.16 0.128 0.32 0.256 0.48 0.384 0.128 0.064 0.256 0.16 0.384 0.256 0.096 0.064 0.192 0.16 0.256 0.224 0.8 0.576 1.632 1.12 2.496 1.664 0.416 0.128 0.8 0.256 1.056 0.32 1.984 0.576 4.064 0.8 6.112 0.928 2.688-1.92 5.312-3.904 8-5.792 0.896-1.088 1.92-2.080 2.912-3.104v-7.552c-0.096-0.128-0.192-0.288-0.32-0.416-0.768-1.024-1.184-2.176-1.6-3.296-0.768-0.416-1.536-0.8-2.336-1.12-0.128-0.064-0.256-0.096-0.384-0.16h-21.568v12.992c1.312 0.672 2.496 1.6 3.648 2.528z"
				></path>
			</symbol>
			<symbol id="icon-heart" viewBox="0 0 32 32">
				<title>icon-heart</title>
				<path
					d="M22.88 1.952c-2.72 0-5.184 1.28-6.88 3.456-1.696-2.176-4.16-3.456-6.88-3.456-4.48 0-9.024 3.648-9.024 10.592 0 7.232 7.776 12.704 15.072 17.248 0.256 0.16 0.544 0.256 0.832 0.256s0.576-0.096 0.832-0.256c7.296-4.544 15.072-10.016 15.072-17.248 0-6.944-4.544-10.592-9.024-10.592zM16 26.56c-4.864-3.072-12.736-8.288-12.736-14.016 0-5.088 3.040-7.424 5.824-7.424 2.368 0 4.384 1.504 5.408 4.032 0.256 0.608 0.832 0.992 1.472 0.992s1.248-0.384 1.472-0.992c1.024-2.528 3.040-4.032 5.408-4.032 2.816 0 5.824 2.304 5.824 7.424 0.064 5.728-7.808 10.976-12.672 14.016z"
				></path>
				<path
					d="M16 30.144c-0.32 0-0.64-0.096-0.896-0.256-7.296-4.576-15.104-10.048-15.104-17.344 0-7.008 4.576-10.688 9.12-10.688 2.656 0 5.152 1.216 6.88 3.392 1.728-2.144 4.224-3.392 6.88-3.392 4.544 0 9.12 3.68 9.12 10.688 0 7.296-7.808 12.768-15.104 17.344-0.256 0.16-0.576 0.256-0.896 0.256zM9.12 2.048c-4.448 0-8.928 3.616-8.928 10.496 0 7.168 7.744 12.64 15.008 17.152 0.48 0.288 1.12 0.288 1.568 0 7.264-4.544 15.008-9.984 15.008-17.152 0-6.88-4.48-10.496-8.928-10.496-2.656 0-5.088 1.216-6.816 3.392l-0.032 0.128-0.064-0.096c-1.696-2.176-4.192-3.424-6.816-3.424zM16 26.688l-0.064-0.032c-3.808-2.4-12.768-8.032-12.768-14.112 0-5.152 3.072-7.52 5.952-7.52 2.432 0 4.48 1.536 5.504 4.096 0.224 0.576 0.768 0.928 1.376 0.928s1.152-0.384 1.376-0.928c1.024-2.56 3.072-4.096 5.504-4.096 2.848 0 5.952 2.336 5.952 7.52 0 6.080-8.96 11.712-12.768 14.112l-0.064 0.032zM9.12 5.248c-2.752 0-5.728 2.304-5.728 7.328 0 5.952 8.8 11.488 12.608 13.92 3.808-2.4 12.608-7.968 12.608-13.92 0-5.024-2.976-7.328-5.728-7.328-2.336 0-4.32 1.472-5.312 3.968-0.256 0.64-0.864 1.056-1.568 1.056s-1.312-0.416-1.568-1.056c-0.992-2.496-2.976-3.968-5.312-3.968z"
				></path>
			</symbol>
		</div>
		<div
			id="player-back-container"
			class="player-back slide-in-top"
			v-hammer:swipe.up="swipeUp"
			v-if="currentTrack"
		>
			<div class="back-wrap">
				<div class="back-playbar">
					<div
						v-hammer:tap="swipeUp"
						class="back-playbar__img"
						:style="{ backgroundImage: `url(${currentTrack.cover})` }"
					></div>
					<div class="back-playbar__content">
						<div class="back-playbar__info" v-hammer:tap="swipeUp">
							<span class="back-playbar__name">{{
								currentTrack.name | truncate
							}}</span>
							<span class="back-playbar__artist">{{
								currentTrack.artist | truncate
							}}</span>
						</div>
						<div class="back-playbar__bar">
							<img
								v-if="isTimerPlaying"
								@click="play"
								class="back-playbar__button"
								src="@/assets/images/pause.svg"
								alt="정지"
							/>
							<img
								v-else
								@click="play"
								class="back-playbar__button"
								src="@/assets/images/play.svg"
								alt="재생"
							/>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { likeMusic } from '@/api/auth';
import bus from '@/utils/bus';
export default {
	created() {
		bus.$on('show:musicplayer', this.openMethod);
	},

	beforeDestroy() {
		bus.$off('show:musicplayer', this.openMethod);
	},
	data() {
		return {
			open: false,
			tracks: null,
			playerVars: {
				autoplay: 0,
				playsinline: 1,
				controls: 0,
				autohide: 1,
				wmode: 'opaque',
				origin: 'https://k3d104.p.ssafy.io',
			},
			isTimerPlaying: false,
			currentTrack: null,
			currentTrackIndex: 0,
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		async favorite() {
			try {
				this.tracks[this.currentTrackIndex].favorited = !this.tracks[
					this.currentTrackIndex
				].favorited;
				this.currentTrack = this.tracks[this.currentTrackIndex];
				await likeMusic(this.tracks[0].id, this.tracks[0].search);
			} catch (error) {
				bus.$emit('show:error', '좋아요 요청을 실패했습니다 :(');
			}
		},
		swipeUp() {
			const BAR = document.querySelector('.player-back');
			const PLAYER = document.querySelector('.player');
			PLAYER.classList.remove('slide-out-bottom');
			PLAYER.classList.add('slide-in-bottom');
			PLAYER.style.display = 'block';
			BAR.classList.remove('slide-in-top');
			BAR.classList.add('slide-out-top');
			BAR.style.display = 'none';
		},
		swipeDown() {
			const BAR = document.querySelector('.player-back');
			const PLAYER = document.querySelector('.player');
			BAR.classList.remove('slide-out-top');
			BAR.classList.add('slide-in-top');
			BAR.style.display = 'block';
			PLAYER.classList.remove('slide-in-bottom');
			PLAYER.classList.add('slide-out-bottom');
			PLAYER.style.display = 'none';
		},
		closePlayer() {
			this.open = false;
		},
		openMethod(tracks) {
			this.open = true;
			this.tracks = tracks;
			this.currentTrack = this.tracks[0];
		},
		play() {
			this.$refs.player.player.getPlayerState().then(response => {
				if (
					response === -1 ||
					response === 2 ||
					response === 5 ||
					response === 0
				) {
					this.$refs.player.player.playVideo();
					this.isTimerPlaying = true;
				} else {
					this.$refs.player.player.pauseVideo();
					this.isTimerPlaying = false;
				}
			});
		},
		nextTrack() {
			if (this.currentTrackIndex < this.tracks.length - 1) {
				this.currentTrackIndex++;
			} else {
				this.currentTrackIndex = 0;
			}
			this.currentTrack = this.tracks[this.currentTrackIndex];
			setTimeout(() => {
				this.$refs.player.player.playVideo();
				this.isTimerPlaying = true;
			}, 300);
		},
	},
};
</script>

<style lang="scss" scoped>
.toast1 {
	z-index: 100;
	position: fixed;
	width: 100%;
	bottom: 0;
	left: 50%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	border-radius: 12px;
	transform: translateX(-50%);
	transition: all 1s ease-in-out 0.1s;
	border-top: 1px solid rgba(#adb5bd, 0.2);
	font-family: 'Poor Story';
}
.toast1.none {
	display: none !important;
}
#player-back-container {
	position: fixed;
	left: 2.5%;
	right: 2.5%;
	bottom: 0;
	width: 95%;
	background: #f0f0f0;
	z-index: 10;
	border-radius: 12px;
	height: 80px;
}
.back-wrap {
	width: 100%;
	height: 100%;
}
.back-playbar {
	height: 80px;
	background-color: rgb(240, 240, 240);
	box-shadow: 6px 6px 5px #c7c7c7, -6px -6px 5px #ffffff;
	padding: 10px 0 10px;
	border-radius: 12px;
	display: flex;
	.back-playbar__img {
		width: 60px;
		height: 60px;
		background-repeat: no-repeat !important;
		background-position: center !important;
		background-size: cover !important;
		border-radius: 8px;
		margin-left: 1.5rem;
		@media (max-width: 320px) {
			margin-left: 0.5rem !important;
		}
	}
	.back-playbar__content {
		flex: 1;
		height: 100%;
		margin-left: 1rem;
		display: flex;
		align-items: center;
		@media (max-width: 320px) {
			margin-left: 0.7rem;
		}
		.back-playbar__info {
			flex: 1;
			height: 100%;
			display: flex;
			flex-direction: column;
			justify-content: space-around;
			.back-playbar__name {
				font-size: 1.3rem;
				color: #71829e;
				@media (max-width: 320px) {
					font-size: 1rem;
				}
			}
			.back-playbar__artist {
				color: rgba(#71829e, 0.7);
				font-size: 1rem;
				@media (max-width: 320px) {
					font-size: 0.8rem;
				}
			}
		}
		.back-playbar__bar {
			flex: 1;
			margin-right: 0.5rem;
			height: 100%;
			display: flex;
			justify-content: center;
			align-items: center;
			@media (max-width: 320px) {
				flex: 0.7;
			}
		}
		.back-playbar__button {
			height: 100%;
			box-sizing: border-box;
			cursor: pointer;
		}
	}
}
.back-song__select {
	background-color: #dbe4ff;
}
.back-song__last {
	margin-bottom: 80px;
}
.player-cover__content {
	height: 100%;
}
.back-header {
	position: relative;
	text-align: center;
	padding: 20px;
	border-bottom: 1px solid rgba(#71829e, 0.3);
	font-weight: 600;
	font-size: 24px;
}
.player__title {
	text-align: center;
	margin-bottom: 1.5rem;
	font-weight: 600;
	font-size: 24px;
	color: #71829e;
	position: relative;
	.player__title__text {
		padding-top: 6px;
		border-top: 3px solid #71829e;
	}
}
.player-swap {
	position: absolute;
	top: 0;
	right: 0;
	width: 30px;
	height: 30px;
	cursor: pointer;
}
.player-swap__back {
	position: absolute;
	top: 0px;
	right: 0px;
	width: 25px;
	height: 25px;
	cursor: pointer;
}
.icon {
	display: inline-block;
	width: 1em;
	height: 1em;
	stroke-width: 0;
	stroke: currentColor;
	fill: currentColor;
}
.opacity-on {
	opacity: 1;
}
.opacity-off {
	opacity: 0;
}

.player {
	position: relative;
	display: none;
	width: 410px;
	background: #f0f0f0;
	box-shadow: 5px 5px 10px #e2e2e2, -5px -5px 10px #e2e2e2;
	color: #71829e;
	border-radius: 12px;
	padding: 1.5rem;
	@media screen and (max-width: 576px), (max-height: 500px) {
		width: 95%;
		padding: 20px;
		padding-bottom: 30px;
		max-width: 410px;
	}
	&__top {
		display: flex;
		align-items: flex-start;
		position: relative;
		z-index: 4;
		flex-wrap: wrap;
	}

	&-cover {
		margin-bottom: 25px;
		width: 300px;
		height: 300px;
		margin-left: auto;
		margin-right: auto;
		flex-shrink: 0;
		z-index: 2;
		border-radius: 15px;

		@media screen and (max-width: 340px) {
			width: 210px;
			height: 210px;
		}

		&__item {
			background-repeat: no-repeat !important;
			background-position: center !important;
			background-size: cover !important;
			width: 100%;
			height: 100%;
			border-radius: 15px;
			background: #f0f0f0;
			box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
		}

		&__img {
			width: 100%;
			height: 100%;
			object-fit: cover;
			border-radius: 15px;
			box-shadow: 0px 10px 40px 0px rgba(76, 70, 124, 0.5);
			user-select: none;
			pointer-events: none;
		}
	}

	&-controls {
		display: flex;
		align-items: center;
		flex-direction: row;
		padding-left: 10px;
		padding-right: 10px;
		width: 100%;
		flex: unset;
		&__item {
			display: inline-flex;
			font-size: 30px;
			padding: 5px;
			margin-bottom: 10px;
			color: #acb8cc;
			cursor: pointer;
			width: 50px;
			height: 50px;
			align-items: center;
			justify-content: center;
			position: relative;
			transition: all 0.3s ease-in-out;

			@media screen and (max-width: 576px), (max-height: 500px) {
				font-size: 26px;
				padding: 5px;
				margin-right: 10px;
				color: #acb8cc;
				cursor: pointer;
				width: 40px;
				height: 40px;
				margin-bottom: 0;
			}

			&::before {
				content: '';
				position: absolute;
				width: 100%;
				height: 100%;
				border-radius: 50%;
				background: #fff;
				transform: scale(0.5);
				opacity: 0;
				box-shadow: 0px 5px 10px 0px rgba(76, 70, 124, 0.2);
				transition: all 0.3s ease-in-out;
				transition: all 0.4s cubic-bezier(0.35, 0.57, 0.13, 0.88);
			}

			@media screen and (min-width: 500px) {
				&:hover {
					color: #532ab9;

					&::before {
						opacity: 1;
						transform: scale(1.3);
					}
				}
			}

			@media screen and (max-width: 576px), (max-height: 500px) {
				&:active {
					color: #532ab9;

					&::before {
						opacity: 1;
						transform: scale(1.3);
					}
				}
			}

			.icon {
				position: relative;
				z-index: 2;
			}

			&.-xl {
				margin-bottom: 0;
				font-size: 95px;
				filter: drop-shadow(0 11px 6px rgba(172, 184, 204, 0.45));
				color: #fff;
				width: auto;
				height: auto;
				display: inline-flex;
				margin-left: auto;

				@media screen and (max-width: 576px), (max-height: 500px) {
					font-size: 75px;
					margin-right: 0;
				}
				&:before {
					display: none;
				}
			}

			&.-favorite {
				&.active {
					color: red !important;
				}
			}
		}
	}
}
[v-cloak] {
	display: none;
}
[v-cloak] > * {
	display: none;
}

.album-info {
	color: #71829e;
	flex: 1;
	padding-left: 10px;
	user-select: none;

	@media screen and (max-width: 576px), (max-height: 500px) {
		padding-right: 30px;
	}

	&__name {
		font-size: 20px;
		font-weight: bold;
		margin-bottom: 12px;
		line-height: 1.3em;
		@media screen and (max-width: 576px), (max-height: 500px) {
			font-size: 18px;
			margin-bottom: 9px;
		}
	}
	&__track {
		font-weight: 400;
		font-size: 20px;
		opacity: 0.7;
		line-height: 1.3em;
		@media screen and (max-width: 576px), (max-height: 500px) {
			font-size: 18px;
		}
	}
}

.github-btn {
	position: absolute;
	right: 40px;
	bottom: 50px;
	text-decoration: none;
	padding: 15px 25px;
	border-radius: 4px;
	box-shadow: 0px 4px 30px -6px rgba(36, 52, 70, 0.65);
	background: #24292e;
	color: #fff;
	font-weight: bold;
	letter-spacing: 1px;
	font-size: 16px;
	transition: all 0.3s ease-in-out;

	@media screen and (min-width: 500px) {
		&:hover {
			transform: scale(1.1);
			box-shadow: 0px 17px 20px -6px rgba(36, 52, 70, 0.36);
		}
	}

	@media screen and (max-width: 700px) {
		position: relative;
		bottom: auto;
		right: auto;
		margin-top: 20px;

		&:active {
			transform: scale(1.1);
			box-shadow: 0px 17px 20px -6px rgba(36, 52, 70, 0.36);
		}
	}
}

.player-font {
	color: #71829e;
	width: 4rem;
	height: 4rem;
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 2.5rem;
	border-radius: 16px;
	background: #f0f0f0;
	box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
}
.ion-md-play:before {
	padding: 0 0.2rem 0 0.5rem;
}
.player-pause {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 1.8rem;
	font-size: 2rem;
	border-radius: 12px;
	background: #f0f0f0;
	box-shadow: inset 5px 5px 10px #d8d8d8, inset -5px -5px 10px #ffffff;
}
.slide-in-top {
	-webkit-animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
	animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.slide-in-bottom {
	-webkit-animation: slide-in-bottom 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)
		both;
	animation: slide-in-bottom 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
@-webkit-keyframes slide-in-top {
	0% {
		-webkit-transform: translateY(-50px);
		transform: translateY(-50px);
		opacity: 0;
	}
	100% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
}
@keyframes slide-in-top {
	0% {
		-webkit-transform: translateY(-50px);
		transform: translateY(-50px);
		opacity: 0;
	}
	100% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
}
@-webkit-keyframes slide-in-bottom {
	0% {
		-webkit-transform: translateY(80px);
		transform: translateY(80px);
		opacity: 0;
	}
	100% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
}
@keyframes slide-in-bottom {
	0% {
		-webkit-transform: translateY(80px);
		transform: translateY(80px);
		opacity: 0;
	}
	100% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
}
.slide-out-top {
	-webkit-animation: slide-out-top 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53)
		both;
	animation: slide-out-top 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53) both;
}
@-webkit-keyframes slide-out-top {
	0% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
	100% {
		-webkit-transform: translateY(-20px);
		transform: translateY(-20px);
		opacity: 0;
	}
}
@keyframes slide-out-top {
	0% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
	100% {
		-webkit-transform: translateY(-20px);
		transform: translateY(-20px);
		opacity: 0;
	}
}
.slide-out-bottom {
	-webkit-animation: slide-out-bottom 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53)
		both;
	animation: slide-out-bottom 0.5s cubic-bezier(0.55, 0.085, 0.68, 0.53) both;
}
@-webkit-keyframes slide-out-bottom {
	0% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
	100% {
		-webkit-transform: translateY(20px);
		transform: translateY(20px);
		opacity: 0;
	}
}
@keyframes slide-out-top {
	0% {
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1;
	}
	100% {
		-webkit-transform: translateY(20px);
		transform: translateY(20px);
		opacity: 0;
	}
}
</style>
