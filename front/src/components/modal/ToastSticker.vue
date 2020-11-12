<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-stickers">
				<div class="toast-sticker__box">
					<ul>
						<li v-for="sticker in stickers" :key="sticker.id">
							<input
								class="toast-sticker__input"
								type="radio"
								name="sticker"
								:id="`toast-sticker__${sticker.id}`"
								:value="sticker"
								v-model="selectedSticker"
							/>
							<label
								class="toast-sticker__label"
								:for="`toast-sticker__${sticker.id}`"
								><div class="toast-sticker__indicator"></div>
								<span class="toast-sticker__text">{{
									sticker.name
								}}</span></label
							>
						</li>
					</ul>
				</div>
				<!-- <div class="toast-sticker__box">
					<input
						class="toast-sticker__input"
						type="radio"
						name="sticker"
						id="toast-sticker__animal"
						value="animal"
						v-model="selectedSticker"
					/>
					<label class="toast-sticker__label" for="toast-sticker__animal"
						><div class="toast-sticker__indicator"></div>
						<span class="toast-sticker__text">동물</span></label
					>
				</div>
				<div class="toast-sticker__box">
					<input
						class="toast-sticker__input"
						type="radio"
						name="sticker"
						id="toast-sticker__figure"
						value="figure"
						v-model="selectedSticker"
					/>
					<label class="toast-sticker__label" for="toast-sticker__figure"
						><div class="toast-sticker__indicator"></div>
						<span class="toast-sticker__text toast-sticker__rightzero"
							>도형</span
						></label
					>
				</div> -->
			</div>
			<div class="toast-sticker">
				<div class="toast-sticker__view">
					<ul>
						<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
						<li
							v-if="sticker.name == selectedSticker.name"
							v-for="sticker in stickers"
							:key="sticker.id"
						>
							<ul class="toast-sticker-item__ul">
								<li v-for="item in sticker.stickers" :key="item.id">
									<!-- <p>{{ item }}</p> -->
									<label
										:for="`toast-sticker__${item.id}`"
										@click.prevent="
											submitSticker(item.path, item.id, item.emotion)
										"
									>
										<img
											:src="`${setUrl}${item.path.replace('images', 'media')}`"
											class="toast-sticker-item__image"
											:alt="`${item.name}`"
										/>
									</label>
									<input
										type="radio"
										name="sticker"
										:id="`toast-sticker__${item.id}`"
										:value="item.id"
										hidden
									/>
									<!-- <img
										:src="`${setUrl}${item.path.replace('images', 'media')}`"
										@click.prevent="submitSticker"
										class="toast-sticker-item__image"
										:alt="`${item.name}`"
										v-model="selectedItem"
									/> -->
								</li>
							</ul>
						</li>
					</ul>
				</div>
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="closeSticker">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
		</section>
	</section>
</template>

<script>
import { fetchStickers } from '@/api/diary';
export default {
	data() {
		return {
			stickers: [],
			selectedSticker: {
				id: 1,
				name: '동물',
				stickers: [],
			},
			selectedItem: null,
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
		async onFetchStickers() {
			const { data } = await fetchStickers();
			this.stickers = data;
			// this.stickers = data.slice(0, 3);
			console.log(data);
		},
		closeSticker() {
			this.$emit('close-sticker');
		},
		submitSticker(path, id, emotion) {
			this.selectedItem = this.setUrl + path.replace('images', 'media');
			this.$emit('submit-sticker', this.selectedItem, id, emotion);
		},
	},
	created() {
		this.onFetchStickers();
	},
};
</script>

<style lang="scss" scoped>
.toast-sticker__view {
	.toast-sticker-item__ul {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		margin-top: 20px;
		.toast-sticker-item__image {
			width: 70px;
			max-height: 90px;
			margin-top: 10px;
		}
	}
}
.toast-stickers {
	display: flex;
	justify-content: center;
	align-items: center;
}
.toast-sticker__box {
	ul {
		display: flex;
		flex-wrap: wrap;
	}
}
.toast-sticker__input {
	position: absolute;
	top: 0;
	right: 0;
	opacity: 0;
	pointer-events: none;
}
.toast-sticker__label {
	display: inline-flex;
	align-items: center;
	cursor: pointer;
	color: #394a56;
}
.toast-sticker__indicator {
	position: relative;
	border-radius: 50%;
	height: 20px;
	width: 20px;
	box-shadow: -8px -4px 8px 0px #ffffff, 8px 4px 12px 0px #d1d9e6;
	overflow: hidden;
}
.toast-sticker__text {
	margin-left: 8px;
	margin-right: 16px;
	opacity: 0.6;
	transition: opacity 0.2s linear, transform 0.2s ease-out;
}
.toast-sticker__rightzero {
	margin-right: 0;
}
.toast-sticker__indicator::before,
.toast-sticker__indicator::after {
	content: '';
	position: absolute;
	top: 10%;
	left: 10%;
	height: 80%;
	width: 80%;
	border-radius: 50%;
}
.toast-sticker__indicator::before {
	box-shadow: -4px -2px 4px 0px #d1d9e6, 4px 2px 8px 0px #fff;
}
.toast-sticker__indicator::after {
	background-color: #ecf0f3;
	box-shadow: -4px -2px 4px 0px #fff, 4px 2px 8px 0px #d1d9e6;
	transform: scale3d(1, 1, 1);
	transition: opacity 0.25s ease-in-out, transform 0.25s ease-in-out;
}
.toast-sticker__input:checked
	~ .toast-sticker__label
	.toast-sticker__indicator::after {
	transform: scale3d(0.975, 0.975, 1) translate3d(0, 10%, 0);
	opacity: 0;
}
.toast-sticker__label:hover .toast-sticker__text {
	opacity: 1;
}
</style>
