<template>
	<section>
		<div class="diary-wrap">
			<div class="diary-header">
				<input
					id="diary-header__title"
					placeholder="이 곳에 오늘 하루를 한 줄로 말해주세요:)"
					type="text"
				/>
			</div>
			<div class="diary-image">
				<img
					class="diary-image__value"
					v-if="diaryImageUrl"
					:src="diaryImageUrl"
					alt="일기사진"
				/>
				<label for="diary-image__input" v-if="diaryImageFile">
					<img
						src="@/assets/images/photos.svg"
						class="diary-image__file"
						alt="이미지추가하기"
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
				></textarea>
			</div>
		</div>
	</section>
</template>

<script>
export default {
	data() {
		return {
			diaryImage: null,
			diaryImageUrl: null,
			diaryImageFile: true,
		};
	},
	methods: {
		onChangeDiaryImage() {
			this.diaryImage = this.$refs.inputImage.files[0];
			this.diaryImageUrl = URL.createObjectURL(this.diaryImage);
			this.diaryImageFile = false;
		},
	},
};
</script>

<style lang="scss">
.diary-wrap {
	display: flex;
	flex-direction: column;
	justify-content: center;
	.diary-header {
		margin: 10px 0;
		label {
			color: rgb(61, 61, 61);
			font-size: 14px;
		}
		#diary-header__title {
			width: 95%;
			margin-left: 5px;
			padding-bottom: 5px;
			border: none;
			border-bottom: 1px solid rgba(151, 151, 151, 0.5);
		}
	}
	.diary-image {
		display: flex;
		justify-content: center;
		border-radius: 4px;
		background: rgba(151, 151, 151, 0.3);
		.diary-image__value {
			width: 100%;
		}
		label {
			display: flex;
			justify-content: center;
			.diary-image__file {
				width: 35%;
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
			background-image: linear-gradient(to right, white 10px, transparent 10px),
				linear-gradient(to left, white 10px, transparent 10px),
				repeating-linear-gradient(
					white,
					white 30px,
					#ccc 30px,
					#ccc 31px,
					white 31px
				);
		}
	}
}
</style>
