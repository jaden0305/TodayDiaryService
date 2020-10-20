<template>
	<section class="calendar-wrap">
		<div class="calendar-header">
			<button class="calendar-header__prev">
				<i class="icon ion-ios-arrow-back"></i>
			</button>
			<span class="calendar-header__month">10월</span>
			<button class="calendar-header__next">
				<i class="icon ion-ios-arrow-forward"></i>
			</button>
		</div>
		<div class="calendar-weekdays">
			<span class="calendar-weekday sunday">일</span>
			<span class="calendar-weekday monday">월</span>
			<span class="calendar-weekday tuesday">화</span>
			<span class="calendar-weekday wednesday">수</span>
			<span class="calendar-weekday thursday">목</span>
			<span class="calendar-weekday friday">금</span>
			<span class="calendar-weekday saturday">토</span>
		</div>
		<div class="calendar-days">
			<span class="calendar-day">27</span>
			<span class="calendar-day">28</span>
			<span class="calendar-day">29</span>
			<span class="calendar-day">30</span>
			<span class="calendar-day">1</span>
			<span class="calendar-day">2</span>
			<span class="calendar-day">3</span>
			<span class="calendar-day">4</span>
			<span class="calendar-day">5</span>
			<span class="calendar-day">6</span>
			<span class="calendar-day">7</span>
			<span class="calendar-day">8</span>
			<span class="calendar-day">9</span>
			<span class="calendar-day">10</span>
			<span class="calendar-day">11</span>
			<span class="calendar-day">12</span>
			<span class="calendar-day">13</span>
			<span class="calendar-day">14</span>
			<span class="calendar-day">15</span>
			<span class="calendar-day">16</span>
			<span class="calendar-day">17</span>
			<span class="calendar-day">18</span>
			<span class="calendar-day">19</span>
			<span class="calendar-day">20</span>
			<span class="calendar-day">21</span>
			<span class="calendar-day">22</span>
			<span class="calendar-day">23</span>
			<span class="calendar-day">24</span>
			<span class="calendar-day">25</span>
			<span class="calendar-day">26</span>
			<span class="calendar-day">27</span>
			<span class="calendar-day">28</span>
			<span class="calendar-day">29</span>
			<span class="calendar-day">30</span>
			<span class="calendar-day">31</span>
			<span class="calendar-day">1</span>
			<span class="calendar-day">2</span>
			<span class="calendar-day">3</span>
			<span class="calendar-day">4</span>
			<span class="calendar-day">5</span>
			<span class="calendar-day">6</span>
			<span class="calendar-day">7</span>
		</div>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss">
.calendar-wrap {
	width: 100%;
	height: 70vh;
}
.calendar-header {
	display: flex;
	justify-content: center;
	align-items: center;
	text-align: center;

	.calendar-header__month {
		font-size: 2rem;
	}
	.calendar-header__prev {
		margin-right: 1.5rem;
		font-size: 1rem;
		border: none;
	}
	.calendar-header__next {
		margin-left: 1.5rem;
		font-size: 1rem;
		border: none;
	}
}

.calendar-weekdays {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	.calendar-weekday {
		width: 100 / 7 * 1%;
		text-align: center;
	}
}

.calendar-days {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	flex-wrap: wrap;
	.calendar-day {
		width: 100 / 7 * 1%;
		text-align: center;
	}
}
</style>
