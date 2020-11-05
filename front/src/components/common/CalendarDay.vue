<template>
	<div class="calendar-day" :style="{ height: `${weekWidth}px` }">
		<img
			v-if="
				!day.post &&
					(toDay === day.day || toDay - 1 === day.day) &&
					todayMonth === day.month
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="emoticon"
			src="@/assets/images/pencil-c.svg"
			alt=""
		/>
		<img
			v-if="
				nowDay < new Date(`${year}-${lastTwo(day.month)}-${lastTwo(day.day)}`)
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="calendar-day emoticon display-none"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-else-if="
				(!day.post && !(toDay === day.day || toDay - 1 === day.day)) ||
					!(todayMonth === day.month)
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="emoticon"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-if="
				day.post &&
					(day.post.user_emotion.id === 1 || day.post.emotion.id === 1)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/happy.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 2 || day.post.emotion.id === 2)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/sad.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 3 || day.post.emotion.id === 3)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/smile.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 4 || day.post.emotion.id === 4)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 5 || day.post.emotion.id === 5)
			"
			@click="readDiary(day.post.id)"
			class="calendar-day emoticon"
			src="@/assets/images/emotion/angry.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 6 || day.post.emotion.id === 6)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/surprise.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion.id === 7 || day.post.emotion.id === 7)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/dislike.png"
			alt=""
		/>
		<p class="calendar-day__title">{{ day.day }}</p>
	</div>
</template>

<script>
export default {
	props: {
		day: Object,
		year: Number,
		toDay: Number,
		todayMonth: Number,
		nowDay: Date,
		weekWidth: Number,
	},
	methods: {
		writeDiary(dayString) {
			console.log(dayString);
			this.$router.push({ name: 'diary' });
		},
		readDiary(diary_pk) {
			this.$router.push(`/diary/${diary_pk}`);
		},
		lastTwo(month) {
			console.log(('0' + month).slice(-2));
			return ('0' + month).slice(-2);
		},
	},
	mounted() {
		// const day = document.querySelectorAll('.calendar-day');
		// day.style.height = `${this.weekWidth}px`;
		// console.log(this.weekWidth, day.clientHeight);
	},
};
</script>

<style></style>
