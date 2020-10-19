<template>
	<StyledPhotoBlock>
		<StyledPhoto
			:width="width"
			deg="0"
			:rate="rate"
			:src="imageUrl"
		></StyledPhoto>
		<input id="file" ref="imageInput" type="file" @change="onChangeImages" />
	</StyledPhotoBlock>
</template>

<script>
import {
	StyledPhotoBlock,
	StyledPhoto,
} from '@/components/styledComponents/Photo';
export default {
	components: {
		StyledPhotoBlock,
		StyledPhoto,
	},
	data() {
		return {
			imageUrl: null,
			rate: null,
			width: '50',
		};
	},
	methods: {
		onChangeImages() {
			const file = this.$refs.imageInput.files[0];
			var reader = new FileReader();
			reader.readAsDataURL(file);
			reader.onload = e => {
				var image = new Image();
				image.src = e.target.result;
				image.onload = () => {
					var height = image.height;
					var width = image.width;
					this.rate = parseInt((height / width) * 100) * (this.width / 100);
					return true;
				};
			};
			this.imageUrl = URL.createObjectURL(file);
		},
	},
};
</script>

<style></style>
