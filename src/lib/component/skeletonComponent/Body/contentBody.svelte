

<script module>
	let deleteMessageToggle = $state(false);
	let deleteMessage = $state('');

	export function handleDeleteMessage(itemName: string) {
		deleteMessageToggle = true;
		deleteMessage = itemName;

		const intervalId = setInterval(() => {
			deleteMessageToggle = false;
			clearInterval(intervalId);
		}, 3500);
	}
</script>

<script lang="ts">
	let completSkelet = $state(true);
	let leftArmSkelet = $state(false);

	const handleShoulderToggle = () => {
		completSkelet = false;
		leftArmSkelet = true;
	};

	const handleGoBack = () => {
		leftArmSkelet = false;
		completSkelet = true;
	};


</script>


<div class="skeletonBodyArea">
    {#if completSkelet}
        <div class="skeletSectionContent">
            <img src="/svgIcons/skelCompl.svg" alt="skseltImage" class="skeletImage" />
            <div class="red-dot" on:click={handleShoulderToggle}>+</div>
            <div class="red-dot1">+</div>
            <div class="red-dot2">+</div>

            {#if deleteMessageToggle}
                <div class="deleteMessageContainer">
                    <div class="deleteText">
                        <div class="deleteMessageIconSection">
                            <img src="remove.png" alt="deleteMessageIcon" class="deleteMessageIcon" />
                        </div>
                        The Product {deleteMessage} was successfully deleted!
                     
                    </div>
                </div>
            {/if}
        </div>
    {:else if leftArmSkelet}
        <div class="skeletShoulder">
            <img src="/svgIcons/Arm.svg" alt="skseltImage" class="skeletShoulderIcon" />
            <div class="red-dot-shoulder1">
                <div class="shoulderTitle1dot1">Shoulder</div>
                <div class="shoulderTitle1dot1Icon">+</div>
            </div>
            <div class="red-dot-shoulder2">
                <div class="shoulderTitle1dot1">forarm</div>
                <div class="shoulderTitle1dot1Icon">+</div>
            </div>
            <div class="goBackShoulderPoll" on:click={handleGoBack}>
                <div class="shoulderSection">
                    <img src="return.png" alt="returnIcon" class="returnIcon" />
                </div>
            </div>

            <!-- <div class="red-dot-shoulder3">+</div> -->
        </div>
    {/if}
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

	@keyframes shake {
		0% {
			transform: translateX(0);
		}
		20% {
			transform: translateX(-5px);
		}
		40% {
			transform: translateX(5px);
		}
		60% {
			transform: translateX(-5px);
		}
		80% {
			transform: translateX(5px);
		}
		100% {
			transform: translateX(0);
		}
	}

	.deleteMessageContainer {
		position: absolute;
		left: 20%; /* Adjust to match head position */
		top: 93%; /* Adjust to match head position */
		width: 60%;
		height: 5%;
		display: flex;
		justify-content: center;
		align-items: center;
		cursor: pointer;
		background-color: rgba(30, 29, 29, 0.855);
		border: 2px solid rgb(66, 66, 66);
		text-align: center;
		font-size: var(--deleteMessageFontSize);
		border-radius: 7px;
		color: rgb(255, 255, 255);
		animation: shake 2.4s ease-in-out infinite;
	}

	.deleteText {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		/* background-color: pink; */
	}

	.deleteMessageIconSection {
		width: 5%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin-right: 2%;
		/* background-color: green; */
        /* padding-bottom: 1%; */
	}
	.deleteMessageIcon {
		width: var(--deleteMessageIconHeight);
		height: var(--deleteMessageIconWidth);
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
		font-size: var(--bodyplusFontSize);
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

	.goBackShoulderPoll {
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

	.shoulderSection {
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

	.returnIcon {
		width: 40%;
		height: 70%;
	}

	.shoulderSection:hover {
		background-color: rgba(249, 6, 6, 0.629);
		border: none;
	}
</style>
