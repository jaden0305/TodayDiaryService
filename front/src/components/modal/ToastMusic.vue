<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-search">
				<input
					class="toast-search__input"
					placeholder="음악을 검색하세요"
					type="text"
				/>
				<button class="toast-search__btn">
					<img src="@/assets/images/search.svg" alt="" />
				</button>
			</div>
			<div class="toast-musics">
				<ol>
					<li class="toast-musics__item">DON'T TOUCH ME</li>
					<li class="toast-musics__item">취기를 빌려</li>
					<li class="toast-musics__item">오래된 노래</li>
					<li class="toast-musics__item">힘든 건 사랑이 아니다</li>
					<li class="toast-musics__item">DON'T TOUCH ME</li>
					<li class="toast-musics__item">힘든 건 사랑이 아니다</li>
					<li class="toast-musics__item">취기를 빌려</li>
					<li class="toast-musics__item">오래된 노래</li>
				</ol>
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="closeMusic">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
			<!-- <button class="toast-btn-purple" @click="showToast">삭제</button> -->
		</section>
	</section>
</template>

<script>
export default {
	props: {
		open: Boolean,
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
	},
};
</script>

<style lang="scss">
.toast {
	width: 98%;
	height: 550px;
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: #646464;
	background-color: #ffffff;
	box-shadow: 0 0 15px rgba(53, 53, 53, 0.5);
	border-radius: 4px;
	z-index: 100;
	.toast-wrap {
		width: 90%;
		height: 85%;
		.toast-search {
			margin: 20px 20px 50px;
			position: relative;
			.toast-search__input {
				width: 90%;
				font-size: 14px;
				line-height: 2.3;
				border: none;
				border-bottom: 1px solid rgba(151, 151, 151, 0.5);
			}
			.toast-search__btn {
				position: absolute;
				top: 5px;
				right: 20px;
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
		.toast-close {
			margin-top: 30px;
			text-align: center;
			.toast-close__btn {
				border: none;
				background: none;
				img {
					width: 30px;
				}
			}
		}
	}
}
.toast.none {
	display: none;
}
</style>
