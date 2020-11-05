<template>
	<div class="wrapper">
		<div class="player__comment">
			<p>오늘 하루를 음악으로 마무리 하는 건 어때요?</p>
		</div>
		<div class="player">
			<div class="player__top">
				<div class="player-cover">
					<transition-group :name="transitionName">
						<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
						<div
							class="player-cover__item"
							v-if="$index === currentTrackIndex"
							:style="{ backgroundImage: `url(${track.cover})` }"
							v-for="(track, $index) in tracks"
							:key="$index"
						></div>
					</transition-group>
				</div>
				<div class="player-controls">
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
			</div>
			<div class="progress" ref="progress">
				<div class="progress__top">
					<div class="album-info" v-if="currentTrack">
						<div class="album-info__name">{{ currentTrack.artist }}</div>
						<div class="album-info__track">{{ currentTrack.name }}</div>
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
		</div>
		<video-wrapper
			ref="player"
			:player="'youtube'"
			:videoId="currentTrack.videoId"
			@ended="nextTrack"
		/>
	</div>
</template>

<script>
export default {
	data() {
		return {
			audio: null,
			circleLeft: null,
			barWidth: null,
			duration: null,
			currentTime: null,
			isTimerPlaying: false,
			tracks: [
				{
					name: '야작시',
					artist: '적재',
					cover:
						'https://image.bugsm.co.kr/album/images/500/203478/20347883.jpg',
					videoId: 'jXylepYfpk0',
					url: 'https://youtu.be/26YwXUcUf4I',
					favorited: false,
				},
				{
					name: '블루밍',
					artist: '아이유',
					cover: 'https://i.ytimg.com/vi/D1PvIWdJ8xo/maxresdefault.jpg',
					videoId: 'D1PvIWdJ8xo',
					url: 'https://youtu.be/26YwXUcUf4I',
					favorited: false,
				},
			],
			currentTrack: null,
			currentTrackIndex: 0,
			transitionName: null,
		};
	},
	methods: {
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
		prevTrack() {
			this.transitionName = 'scale-in';
			this.isShowCover = false;
			if (this.currentTrackIndex > 0) {
				this.currentTrackIndex--;
			} else {
				this.currentTrackIndex = this.tracks.length - 1;
			}
			this.currentTrack = this.tracks[this.currentTrackIndex];
			this.resetPlayer();
		},
		nextTrack() {
			this.transitionName = 'scale-out';
			this.isShowCover = false;
			if (this.currentTrackIndex < this.tracks.length - 1) {
				this.currentTrackIndex++;
			} else {
				this.currentTrackIndex = 0;
			}
			this.currentTrack = this.tracks[this.currentTrackIndex];
			this.resetPlayer();
		},
		resetPlayer() {
			this.circleLeft = 0;
			setTimeout(() => {
				if (this.isTimerPlaying) {
					// this.audio.play();
					this.$refs.player.player.playVideo();
				} else {
					// this.audio.pause();
					this.$refs.player.player.pauseVideo();
				}
			}, 300);
		},
		favorite() {
			this.tracks[this.currentTrackIndex].favorited = !this.tracks[
				this.currentTrackIndex
			].favorited;
		},
	},
	created() {
		// let vm = this;
		this.currentTrack = this.tracks[0];
		// this.audio = new Audio();
		// this.audio.src = this.currentTrack.source;
		// this.audio.ontimeupdate = function() {
		// 	vm.generateTime();
		// };
		// this.audio.onloadedmetadata = function() {
		// 	vm.generateTime();
		// };
		// this.audio.onended = function() {
		// 	vm.nextTrack();
		// 	this.isTimerPlaying = true;
		// };

		// this is optional (for preload covers)
		for (let index = 0; index < this.tracks.length; index++) {
			const element = this.tracks[index];
			let link = document.createElement('link');
			link.rel = 'prefetch';
			link.href = element.cover;
			link.as = 'image';
			document.head.appendChild(link);
		}
	},
};
</script>

<style lang="scss">
.icon {
	display: inline-block;
	width: 1em;
	height: 1em;
	stroke-width: 0;
	stroke: currentColor;
	fill: currentColor;
}

.wrapper {
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: 100%;
	background-size: cover;
	@media screen and (max-width: 700px), (max-height: 500px) {
		flex-wrap: wrap;
		flex-direction: column;
	}
	.player__comment {
		margin: 50px 0 40px;
	}
}

.player {
	background: #eef3f7;
	width: 410px;
	min-height: 480px;
	background: #f0f0f0;
	box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
	border-radius: 15px;
	padding: 30px;
	@media screen and (max-width: 576px), (max-height: 500px) {
		width: 95%;
		padding: 20px;
		min-height: initial;
		padding-bottom: 30px;
		max-width: 400px;
	}
	&__top {
		display: flex;
		align-items: flex-start;
		position: relative;
		z-index: 4;
		@media screen and (max-width: 576px), (max-height: 500px) {
			flex-wrap: wrap;
		}
	}

	&-cover {
		margin-bottom: 25px;
		width: 250px;
		height: 250px;
		margin-left: auto;
		margin-right: auto;
		flex-shrink: 0;
		/* position: relative; */
		z-index: 2;
		border-radius: 15px;
		// transform: perspective(512px) translate3d(0, 0, 0);
		// transition: all .4s cubic-bezier(.125, .625, .125, .875);
		z-index: 1;

		@media screen and (max-width: 340px) {
			width: 200px;
			height: 200px;
		}

		&__item {
			background-repeat: no-repeat !important;
			background-position: center !important;
			background-size: cover !important;
			width: 100%;
			height: 100%;
			border-radius: 15px;
			/* position: absolute;
            left: 0;
            top: 0; */
			background: #f0f0f0;
			box-shadow: 6px 6px 12px #b4b4b4, -6px -6px 12px #ffffff;
			/* &:before {
                content: '';
                background: inherit;
                width: 100%;
                height: 100%;
                box-shadow: 0px 10px 40px 0px rgba(76, 70, 124, 0.5);
                display: block;
                z-index: 1;
                position: absolute;
                top: 30px;
                transform: scale(0.9);
                filter: blur(10px);
                opacity: 0.9;
                border-radius: 15px;
            }

            &:after {
                content: '';
                background: inherit;
                width: 100%;
                height: 100%;
                box-shadow: 0px 10px 40px 0px rgba(76, 70, 124, 0.5);
                display: block;
                z-index: 2;
                position: absolute;
                border-radius: 15px;
            } */
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
		flex: 1;
		padding-left: 20px;
		display: flex;
		flex-direction: column;
		align-items: center;

		@media screen and (max-width: 576px), (max-height: 500px) {
			flex-direction: row;
			padding-left: 0;
			width: 100%;
			flex: unset;
		}

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
				// filter: drop-shadow(0 2px 8px rgba(172, 184, 204, 0.3));
				// filter: drop-shadow(0 9px 6px rgba(172, 184, 204, 0.35));
				filter: drop-shadow(0 11px 6px rgba(172, 184, 204, 0.45));
				color: #fff;
				width: auto;
				height: auto;
				display: inline-flex;
				@media screen and (max-width: 576px), (max-height: 500px) {
					margin-left: auto;
					font-size: 75px;
					margin-right: 0;
				}
				&:before {
					display: none;
				}
			}

			&.-favorite {
				&.active {
					color: red;
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
.progress {
	width: 100%;
	margin-top: -15px;
	user-select: none;
	&__top {
		display: flex;
		align-items: flex-end;
		justify-content: space-between;
	}

	&__duration {
		color: #71829e;
		font-weight: 700;
		font-size: 20px;
		opacity: 0.5;
	}
	&__time {
		margin-top: 2px;
		color: #71829e;
		font-weight: 700;
		font-size: 16px;
		opacity: 0.7;
	}
}
.progress__bar {
	height: 6px;
	width: 100%;
	cursor: pointer;
	background-color: #d0d8e6;
	display: inline-block;
	border-radius: 10px;
}
.progress__current {
	height: inherit;
	width: 0%;
	background-color: #a3b3ce;
	border-radius: 10px;
}

.album-info {
	color: #71829e;
	flex: 1;
	padding-right: 60px;
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
		min-height: 52px;
		@media screen and (max-width: 576px), (max-height: 500px) {
			font-size: 18px;
			min-height: 50px;
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

//scale out

.scale-out-enter-active {
	transition: all 0.35s ease-in-out;
}
.scale-out-leave-active {
	transition: all 0.35s ease-in-out;
}
.scale-out-enter {
	transform: scale(0.55);
	pointer-events: none;
	opacity: 0;
}
.scale-out-leave-to {
	transform: scale(1.2);
	pointer-events: none;
	opacity: 0;
}

//scale in

.scale-in-enter-active {
	transition: all 0.35s ease-in-out;
}
.scale-in-leave-active {
	transition: all 0.35s ease-in-out;
}
.scale-in-enter {
	transform: scale(1.2);
	pointer-events: none;
	opacity: 0;
}
.scale-in-leave-to {
	transform: scale(0.55);
	pointer-events: none;
	opacity: 0;
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
#embed-youtube-video-1 {
	position: absolute;
	top: -500vh;
	left: -500vw;
}
</style>
