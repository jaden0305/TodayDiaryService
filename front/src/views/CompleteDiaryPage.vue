<template>
	<section class="save-diary-wrap">
		<div class="save-diary">
			<p class="save-diary-comment">당신의 오늘 하루는</p>
			<p class="save-diary-comment">행복이군요 :)</p>
			<div class="save-diary-emotion">
				<img src="@/assets/images/emotion/happy.png" alt="감정상태" />
			</div>
			<button class="save-diary-nextBtn">
				다음으로
				<span class="save-diary-nextBtn__span"></span>
			</button>
		</div>
		<button class="save-diary-change">아니에요:(</button>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss">
.save-diary-wrap {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-between;
	height: 80vh;
	padding: 18px;
	.save-diary {
		margin-top: 8vh;
		text-align: center;
		.save-diary-comment {
			margin-bottom: 13px;
		}
		.save-diary-emotion {
			margin: 5vh;
		}
		.save-diary-nextBtn {
			border: none;
			background: none;
			position: relative;
			cursor: pointer;
			.save-diary-nextBtn__span {
				position: absolute;
				bottom: -4px;
				left: 0;
				width: 100%;
				height: 12px;
				background: linear-gradient(to right, #9200b9 8%, #6c23c0 75%, #5600c7);
				opacity: 0.5;
			}
		}
	}
	.save-diary-change {
		width: 120px;
		height: 40px;
		border: none;
		border-radius: 50px;
		background: #f0f0f0;
		box-shadow: 7px 7px 15px #cccccc, -7px -7px 15px #ffffff;
	}
}
</style>
