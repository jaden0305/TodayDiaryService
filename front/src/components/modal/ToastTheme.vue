<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-wrap">
			<div class="toast-themes">
				<label for="toast-theme__bg">테마</label>
				<input
					type="radio"
					name="theme"
					id="toast-theme__bg"
					value="bg"
					v-model="selectedTheme"
				/>
				<label for="toast-theme__font">폰트</label>
				<input
					type="radio"
					name="theme"
					id="toast-theme__font"
					value="font"
					v-model="selectedTheme"
				/>
			</div>
			<div class="toast-theme">
				<div v-if="selectedTheme === 'bg'" class="toast-theme__bg">
					테마
				</div>
				<div v-else class="toast-theme__font">
					<ul>
						<li>font1</li>
						<li>font2</li>
						<li>font3</li>
					</ul>
				</div>
			</div>
			<div class="toast-close">
				<button class="toast-close__btn" @click="closeTheme">
					<img src="@/assets/images/delete.svg" alt="" />
				</button>
			</div>
		</section>
	</section>
</template>

<script>
export default {
	data() {
		return {
			selectedTheme: 'bg',
		};
	},
	props: {
		open: Boolean,
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		closeTheme() {
			this.$emit('close-theme');
		},
	},
};
</script>

<style lang="scss" scoped></style>
