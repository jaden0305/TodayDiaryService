<template>
	<div class="calendar-day" :style="{ height: `${weekWidth}px` }">
		<img
			v-if="
				!day.post &&
					todayYear === day.year &&
					(toDay === day.day || toDay - 1 === day.day) &&
					todayMonth === day.month
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="emoticon"
			src="@/assets/images/pencil.png"
			alt=""
		/>
		<img
			v-else-if="
				nowDay < new Date(`${year}-${lastTwo(day.month)}-${lastTwo(day.day)}`)
			"
			class="calendar-day emoticon display-none"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-else-if="
				(!(toDay === day.day) ||
					!(toDay - 1 === day.day) ||
					!(todayMonth === day.month)) &&
					!day.post
			"
			class="emoticon"
			src="@/assets/images/emotion/normal.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 1 || day.post.emotion === 1)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/happy.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 2 || day.post.emotion === 2)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/sad.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 3 || day.post.emotion === 3)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/smile.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 4 || day.post.emotion === 4)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/boring.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 5 || day.post.emotion === 5)
			"
			@click="readDiary(day.post.id)"
			class="calendar-day emoticon"
			src="@/assets/images/emotion/angry.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 6 || day.post.emotion === 6)
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			src="@/assets/images/emotion/surprise.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post && (day.post.user_emotion === 7 || day.post.emotion === 7)
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
		todayYear: Number,
		nowDay: Date,
		weekWidth: Number,
	},
	methods: {
		writeDiary(dayString) {
			console.log(dayString);
			this.$router.push({ name: 'diary', query: { day: dayString } });
		},
		readDiary(diary_pk) {
			this.$router.push(`/diary/${diary_pk}`);
		},
		lastTwo(month) {
			// console.log(('0' + month).slice(-2));
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
