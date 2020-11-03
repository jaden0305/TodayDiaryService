<template>
	<span class="calendar-day">
		<img
			v-if="
				!day.hasOwnProperty('post') &&
					(toDay === day.day || toDay - 1 === day.day) &&
					todayMonth === day.month
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="emoticon"
			src="@/assets/images/pencil-c.svg"
			alt=""
		/>
		<img
			v-if="nowDay < new Date(`${year}-${day.month}-${day.day}`)"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="calendar-day emoticon display-none"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-else-if="
				(!day.hasOwnProperty('post') &&
					!(toDay === day.day || toDay - 1 === day.day)) ||
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
	</span>
</template>

<script>
export default {
	props: {
		day: Object,
		year: Number,
		toDay: Number,
		todayMonth: Number,
		nowDay: Date,
	},
};
</script>

<style></style>
