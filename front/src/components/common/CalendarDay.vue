<template>
	<div class="calendar-day" :style="{ height: `${weekWidth + 14}px` }">
		<img
			v-if="
				!day.post &&
					todayYear === day.year &&
					(toDay === day.day || toDay - 1 === day.day) &&
					todayMonth === day.month
			"
			@click="writeDiary(`${year}-${day.month}-${day.day}`)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/pencil.png"
			alt=""
		/>
		<div
			v-else-if="
				+nowDay < +new Date(`${year}-${lastTwo(day.month)}-${lastTwo(day.day)}`)
			"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
		></div>
		<img
			v-else-if="
				(!(toDay === day.day) ||
					!(toDay - 1 === day.day) ||
					!(todayMonth === day.month)) &&
					!day.post
			"
			class="emoticon cursor-none"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/normal.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 1 ||
						(!day.post.user_emotion && day.post.emotion === 1))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/1.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 2 ||
						(!day.post.user_emotion && day.post.emotion === 2))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/2.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 3 ||
						(!day.post.user_emotion && day.post.emotion === 3))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/3.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 4 ||
						(!day.post.user_emotion && day.post.emotion === 4))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/4.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 5 ||
						(!day.post.user_emotion && day.post.emotion === 5))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/5.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 6 ||
						(!day.post.user_emotion && day.post.emotion === 6))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/6.png"
			alt=""
		/>
		<img
			v-else-if="
				day.post &&
					(day.post.user_emotion === 7 ||
						(!day.post.user_emotion && day.post.emotion === 7))
			"
			@click="readDiary(day.post.id)"
			class="emoticon"
			:style="{ width: `${weekWidth}px`, height: `${weekWidth}px` }"
			src="@/assets/images/emotion/7.png"
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
			this.$router.push({ name: 'diary', query: { day: dayString } });
		},
		readDiary(diary_pk) {
			this.$router.push(`/diary/${diary_pk}`);
		},
		lastTwo(month) {
			return ('0' + month).slice(-2);
		},
	},
	mounted() {
		const emotions = document.querySelectorAll('.emoticon');
		emotions.forEach(emotion => {
			emotion.style.width = this.weekWidth;
			emotion.style.height = this.weekWidth;
		});
	},
};
</script>

<style></style>
