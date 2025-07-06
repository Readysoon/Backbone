<script lang="ts">
	let menuToggle = $state(false);
	import { Application } from '@splinetool/runtime';
	import skelletsvgIcon from '../../../../static/svgIcons/skelCompl.svg';

	let loading: boolean = true;
	let canvas: any;

	let completSkelet = $state(true);
	let leftArmSkelet = $state(false);

	const handleMenutToggle = () => {
		menuToggle = !menuToggle;
	};

	const handleShoulderToggle = () => {
		completSkelet = false;
		leftArmSkelet = true;
	};

    const handleGoBack= () => {
        leftArmSkelet = false;
        completSkelet = true;
		
    } 

	$effect(() => {
		const handleCallBruno = () => {
			let app = new Application(canvas);
			loading = true;
			const splineobj = app
				.load('https://prod.spline.design/gHGa7XTERPOXgvOV/scene.splinecode')
				.then(() => {
					const obj = app.findObjectByName('brunov1');
					// console.log('obj', obj);
					// if (obj?.position) {
					// Adjust position
					// 	console.log('iits in postion',obj?.position);
					// 	obj.position.x += 10;
					// 	obj.position.y = 50;
					// 	obj.position.z -= -15;
					// 	}
					loading = false;

					// }
				});
		};

		handleCallBruno();
	});
</script>

<div class="skeletSection">
	<div class="scanlyticsHader">
		<!-- <img src="/logo.png" alt="Logo" height="35" width="40" /> -->
		<!-- <h2>Scanlytics</h2> -->

		<div class="navBarMenu">
			<div class="navBarMenuHeader">
				<div
					class="NavBarSectionHead"
					style="background-color: {menuToggle ? ' rgba(249, 87, 6, 0.988)' : '#000000a7'};"
					on:click={handleMenutToggle}
				>
					<img src="/logoww.png" alt="Logo" class="scanlyticsLogo" />
				</div>
				{#if menuToggle}
					<div class="navBarMenuContent">
						<div class="NavBarSection">
							<img src="plus1.png" alt="plusIcon" class="plusIcon" />
						</div>

						<div class="NavBarSection">
							<img src="robo.png" alt="emailIcon" class="roboIcon" />
						</div>
						<div class="NavBarSection">
							<img src="sOut1.png" alt="signOutIcon" class="signOutIcon" />
						</div>
					</div>
				{/if}
			</div>
		</div>
		<div class="scanlyticsTitle">
			<h2>Scanlytics</h2>
		</div>
	</div>

	<div class="skeletonBodyArea">
		{#if completSkelet}
			<div class="skeletSectionContent">
				<img src="/svgIcons/skelCompl.svg" alt="skseltImage" class="skeletImage" />
				<div class="red-dot" on:click={handleShoulderToggle}>+</div>
				<div class="red-dot1">+</div>
				<div class="red-dot2">+</div>
			</div>
		{:else if leftArmSkelet}
			<div class="skeletShoulder">
				<img src="/svgIcons/Arm.svg" alt="skseltImage" class="skeletShoulderIcon" />
				<div class="red-dot-shoulder1">
					<div class="shoulderTitle1dot1">Left Arm Shoulder</div>
					<div class="shoulderTitle1dot1Icon">+</div>
				</div>
				<div class="red-dot-shoulder2">
					<div class="shoulderTitle1dot1">Left Under Arm Shoulder</div>
					<div class="shoulderTitle1dot1Icon">+</div>
				</div>
                <div class="goBackShoulderPoll" on:click={handleGoBack}>
                    <div class="shoulderSection">
                        <img src="return.png" alt="returnIcon" class="returnIcon">
                    </div>
               
                </div>
				<!-- <div class="red-dot-shoulder3">+</div> -->
			</div>
		{/if}
	</div>

	<!-- <div class="aibotAvatar">
   
            <canvas bind:this={canvas} class="avater" />
       
       
    </div> -->
</div>

<style>
	.skeletSection {
		/* background-color: pink; */
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.aibotAvatar {
		/* background-color: rgba(226, 17, 52, 0.619); */
		width: 10%;
		height: 10%;
		/* margin-top: 10%; */
		position: absolute;
		top: 90%;
		left: -2%;
		z-index: 5;
	}

	.scanlyticsHader {
		width: 100%;
		height: 7%;
		/* background-color: pink; */

		font-family: system-ui;
		color: black;
		display: flex;
		align-items: center;
		/* align-items: center; */
		padding-left: 1%;
		font-size: 33px;
		gap: 1%;
		position: relative;
	}

	.NavBarSection {
		width: 70%;
		height: 19.9%;
		/* background-color: green; */
		background-color: #000000a7;
		border-radius: 50px;
		display: flex;
		justify-content: center;
		align-items: center;
		border: 2px solid #33333332;
		color: white;
		/* margin-bottom: 4.5%; */

		cursor: pointer;
	}

	.NavBarSection:hover {
		background-color: rgba(249, 87, 6, 0.988);
		border: none;
	}

	.navBarMenu {
		/* background-color: #ac7373; */
		width: 6.5%;
		/* margin-top: 2%; */
		height: 100%;
		display: flex;
		justify-content: space-between;

		flex-direction: column;
		align-items: center;
		position: relative;
	}

	.navBarMenuHeader {
		/* background-color: rgb(21, 187, 202); */
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.navBarMenuContent {
		position: absolute;
		top: 100%;
		width: 100%;
		height: 300%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		flex-direction: column;
		/* background-color: rgb(187, 202, 21); */
		z-index: 5;
	}

	.NavBarSectionHead {
		width: 70%;
		height: 64.1%;
		/* background-color: green; */
		background-color: #000000a7;
		border-radius: 50px;
		display: flex;
		justify-content: center;
		align-items: center;
		border: 2px solid #33333332;
		color: white;
		/* margin-bottom: 4.5%; */

		cursor: pointer;
	}


	.NavBarSectionHead:hover {
		background-color: rgba(249, 87, 6, 0.988);
		border: none;
		
	}

	.scanlyticsLogo{
		width: var(--scanlyticsLogoWidth);
		height: var(--scanlyticsLogoHeight);
	}

	.scanlyticsLogo:hover{
		width: var(--scanlyticsLogoWidth);
		height: var(--scanlyticsLogoHeight);
	}
	.scanlyticsTitle {
		position: relative;
		left: -1%;
		color: rgb(52, 51, 51);
		font-size: var(--scanlyticsTitleFontSize);
	}
	.signOutIcon {
		width: 69%;
		height: 67%;
	}

	.plusIcon {
		width: 50%;
		height: 50%;
	}

	.emailIcon {
		width: 60%;
		height: 55%;
	}

	.roboIcon {
		width: 70%;
		height: 75%;
	}

	.skeletonBodyArea {
		width: 100%;
		height: 93%;
		/* background-color: green; */
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
	}

	.skeletSectionContent {
		width: 70%;
		height: 100%;
		/* background-color: #fff; */
		position: relative;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.skeletShoulder {
		width: 70%;
		height: 100%;
		/* background-color: #ed8181; */
		position: relative;
		display: flex;
        flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.skeletShoulderIcon {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 67%;
		/* background-color: green; */
	}

	.red-dot-shoulder1 {
		position: absolute;
		left: -1%; /* Adjust to match head position */
		top: 20%; /* Adjust to match head position */
		width: 60%;
		height: 5%;
		background: rgba(248, 244, 244, 0.799);
		border: 3px solid #2369f6dd;
		border-radius: 50px;
		z-index: 2;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		font-size: var(--bodyPointsTitleFontSize);
		cursor: pointer;
		color: black;
	}

	.shoulderLableSection {
		width: 90%;
		height: 100%;
		display: flex;
		/* background-color: pink; */
	}

	.shoulderTitle1dot1 {
		width: 90%;
		height: 100%;
		/* background-color: green; */
		border-top-left-radius: 50px;
		border-bottom-left-radius: 50px;
		padding-left: 5%;
        display: flex;
        align-items: center;
        font-size: var(--bodyPointsTitleFontSize);
	}

	.shoulderTitle1dot1Icon {
		width: 10%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		/* background-color: orage; */
		border-top-right-radius: 50px;
		border-bottom-right-radius: 50px;
		font-size: var(	--bodyplusFontSize);
		font-weight: 600;
		border-left: 3px solid #2369f6dd;
	}

	.red-dot {
		position: absolute;
	    left: var(--bodyPin1LeftPosition); /* Adjust to match head position */
		top: var(--bodyPin1TopPostion); /* Adjust to match head position */
		width: 5%;
		height: 4%;
		background: rgba(255, 0, 0, 0.59);
		border-radius: 50%;
		z-index: 2;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: var(--bodyplusFontSize);
		cursor: pointer;
	}

	.red-dot1 {
		position: absolute;
		left: var(--bodyPin2LeftPosition); /* Adjust to match head position */
		top: var(--bodyPin2TopPostion); /* Adjust to match head position */
		width: 5%;
		height: 4%;
		background: rgba(255, 0, 0, 0.59);
		border-radius: 50%;
		z-index: 2;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: var(--bodyplusFontSize);
		cursor: pointer;
	}

	.red-dot2 {
		position: absolute;
		left: var(--bodyPin3LeftPosition); /* Adjust to match head position */
		top: var(--bodyPin3TopPostion); /* Adjust to match head position */
		width: 5%;
		height: 4%;
		background: rgba(255, 0, 0, 0.59);
		border-radius: 50%;
		z-index: 2;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: var(--bodyplusFontSize);
		cursor: pointer;
	}
	.skeletImage {
		width: 100%;
		height: 77%;
	}

	.red-dot-shoulder2 {
		position: absolute;
		left: -5%; /* Adjust to match head position */
		top: 51%; /* Adjust to match head position */
		width: 60%;
		height: 5%;
		background: rgba(248, 244, 244, 0.799);
		border: 3px solid #2369f6dd;
		border-radius: 50px;
		z-index: 2;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		font-size: var(--bodyPointsTitleFontSize);
		cursor: pointer;
		color: black;
	}

    .goBackShoulderPoll{
        /* background-color: green; */
        position: absolute;
		left: 35%; /* Adjust to match head position */
		top: 92%; /* Adjust to match head position */
		width: 30%;
		height: 7%;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;

    }

    .shoulderSection{
        background-color: #000000a7;
        width: 45%;
        height: 65%;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        border-radius: 50px;
        border: 2px solid #33333332;
    }

    .returnIcon{
        width: 40%;
        height: 70%;
    }

    .shoulderSection:hover{
        background-color:  rgba(249, 6, 6, 0.629);
		border: none;
    }
</style>
