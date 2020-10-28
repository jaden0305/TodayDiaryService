<template>
	<section class="calendar-wrap">
		<div class="calendar-content">
			<div class="calendar-header">
				<button class="calendar-header__prev">
					<!-- <i class="icon ion-ios-arrow-back"></i> -->
					이전달
				</button>
				<div class="calendar-header__box">
					<span class="calendar-header__month">유 월</span>
					<span class="calendar-header__span"></span>
				</div>

				<button class="calendar-header__next">
					<!-- <i class="icon ion-ios-arrow-forward"></i> -->
					다음달
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
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">27</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						28
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						29
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						30
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/pencil-c.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						1
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/happiness.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						2
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/cry.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						3
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/neutral.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						4
					</p></span
				>
				<span class="calendar-day"
					><img
						class="calendar-day emoticon"
						src="@/assets/images/sad.svg"
						alt=""
					/>
					<p class="calendar-day__title">
						5
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						6
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						7
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						8
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						9
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						10
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						11
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						12
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						13
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						14
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						15
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						16
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						17
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						18
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						19
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						20
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						21
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						22
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						23
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						24
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						25
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						26
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						27
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						28
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						29
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						30
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						31
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						1
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						2
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						3
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						4
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						5
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						6
					</p></span
				>
				<span class="calendar-day"
					><i class="icon ion-logo-snapchat"></i>
					<p class="calendar-day__title">
						7
					</p></span
				>
			</div>
		</div>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss">
.calendar-wrap {
	max-width: 100%;
	/* height: 70vh; */
	height: 100%;
	padding: 1rem;
	.calendar-content {
		border-radius: 10px;
		background: rgb(249, 249, 249);
		box-shadow: 5px 5px 80px -14px hsla(0, 0%, 70%, 0.4);
	}
}
.calendar-header {
	display: flex;
	justify-content: space-around;
	align-items: center;
	text-align: center;
	padding-top: 1rem;
	margin-bottom: 0.5rem;
	.calendar-header__box {
		display: inline-block;
		position: relative;
		.calendar-header__month {
			font-size: 1.5rem;
			font-weight: 600;
			color: #495057;
			@media (max-width: 300px) {
				font-size: 1.25rem;
			}
		}
		.calendar-header__span {
			position: absolute;
			bottom: -6px;
			left: 0;
			width: 100%;
			height: 12px;
			background: linear-gradient(to right, #9200b9 8%, #6c23c0 75%, #5600c7);
			opacity: 0.5;
		}
	}
	.calendar-header__prev {
		align-self: flex-end;
		margin-right: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #adb5bd;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-right: 3rem;

			font-size: 0.6rem;
		}
	}
	.calendar-header__next {
		align-self: flex-end;
		margin-left: 3.5rem;
		margin-bottom: -10px;
		font-weight: 600;
		font-size: 0.8rem;
		border: 0;
		outline: 0;
		color: #adb5bd;
		background: none;
		cursor: pointer;
		@media (max-width: 300px) {
			margin-left: 3rem;

			font-size: 0.6rem;
		}
	}
}

.calendar-weekdays {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	color: #495057;
	margin-top: 1.5rem;
	margin-bottom: 0.5rem;
	/* .calendar-weekday:nth-child(1) { */
	// border-top-left-radius: 8px;
	// border-bottom-left-radius: 8px;
	/* } */
	/* .calendar-weekday:nth-last-child(1) { */
	// border-top-right-radius: 8px;
	// border-bottom-right-radius: 8px;
	/* } */
	.calendar-weekday {
		padding-top: 10px;
		padding-bottom: 10px;
		width: 100 / 7 * 1%;
		text-align: center;
		font-weight: 600;
		// background: #495057;
	}

	// .calendar-weekday::after {
	// 	content: '';
	// 	display: block;
	// 	width: 100%;
	// 	padding-bottom: 10px;
	// 	border-bottom: 2px solid grey;
	// }
	// .sunday,
	// .saturday {
	// 	color: #adb5bd;
	// }
}

.calendar-days {
	width: 100%;
	display: flex;
	justify-content: space-evenly;
	flex-wrap: wrap;
	.calendar-day {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100 / 7 * 1%;
		margin-bottom: 1.25rem;
		text-align: center;
		i {
			display: flex;
			font-size: 2rem;
			justify-content: center;
			align-items: center;
		}
		.ion-ios-brush {
			color: grey;
		}
		.emoticon {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 50%;
			margin: 0;
		}
		.today {
			color: royalblue;
		}
		p {
			margin: 0;
			margin-top: 0.15rem;
			font-size: 0.5rem;
			font-weight: 600;
			color: #868e96;
		}
	}
	// .calendar-day__title {
	// 	color: ;
	// }
	// .calendar-day:nth-child(7n + 1),
	// .calendar-day:nth-child(7n) {
	// 	.calendar-day__title {
	// 		color: #868e96;
	// 	}
	// }
}
</style>
