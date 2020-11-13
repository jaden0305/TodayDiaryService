<template>
	<nav class="nav-wrap">
		<ul class="nav-lists">
			<router-link class="nav-list" to="/report" tag="li">
				<div class="nav-list__wrap">
					<img
						class="nav-img"
						src="@/assets/images/chart-pie-slice-fill.svg"
						alt=""
					/>
				</div>
			</router-link>
			<router-link class="nav-list" to="/calendar" tag="li">
				<div class="nav-list__wrap">
					<img class="nav-img" src="@/assets/images/calendar-fill.svg" alt="" />
				</div>
			</router-link>
			<router-link class="nav-list" to="/music" tag="li">
				<div class="nav-list__wrap">
					<img
						class="nav-img"
						src="@/assets/images/music-notes-fill.svg"
						alt=""
					/>
				</div>
			</router-link>
		</ul>
	</nav>
</template>

<script>
export default {
	watch: {
		$route() {
			const selected = document.querySelector('.select-nav');
			const navList = document.querySelectorAll('.nav-list__wrap');
			if (selected) {
				selected.classList.remove('select-nav');
			}
			const routeName = this.$route.name;
			let num;
			switch (routeName) {
				case 'report':
					num = 0;
					break;
				case 'calendar':
					num = 1;
					break;
				case 'music':
					num = 2;
					break;
				default:
					num = null;
					break;
			}
			if (num !== null) {
				navList[num].classList.add('select-nav');
			}
		},
	},
	mounted() {
		const selected = document.querySelector('.select-nav');
		const navList = document.querySelectorAll('.nav-list__wrap');
		if (selected) {
			selected.classList.remove('select-nav');
		}
		const routeName = this.$route.name;
		let num;
		switch (routeName) {
			case 'report':
				num = 0;
				break;
			case 'calendar':
				num = 1;
				break;
			case 'music':
				num = 2;
				break;
			default:
				num = null;
				break;
		}
		if (num !== null) {
			navList[num].classList.add('select-nav');
		}
	},
};
</script>

<style lang="scss">
.nav-wrap {
	width: 100%;
	position: fixed;
	bottom: 0;
	left: 0;
	right: 0;
	height: 70px;
	/* background: #e6e6e6; */
	background: #ffffff;
	border-top: 1px solid rgba(#adb5bd, 0.2);
	/* box-shadow: 20px 20px 60px #c4c4c4, -20px -20px 60px #ffffff; */
	z-index: 999;
	padding-bottom: 10px;
	.nav-lists {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		.nav-list {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 100 / 3 * 1%;
			height: 100%;
			padding: 4px;
			box-sizing: border-box;
			list-style: none;
			.nav-img {
				width: 32px;
				height: 32px;
			}
			.nav-list__wrap {
				display: flex;
				justify-content: center;
				align-items: center;
				width: 100%;
				height: 100%;
			}
		}
		.select-nav {
			border-radius: 16px;
			background: #ffffff;
			box-shadow: inset 9px 9px 18px #d9d9d9, inset -9px -9px 18px #ffffff;
		}
	}
}
</style>
