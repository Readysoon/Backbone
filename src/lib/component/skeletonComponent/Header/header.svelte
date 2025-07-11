<script>
	import { handleEditOption } from '$lib/component/tableComponent/table.svelte';
	let menuToggle = $state(true);
	let aibotSectionToggle = $state(false);
	let editSectionToggle = $state(false);
	let editToggle = $state(false);
	let deleteToggle = $state(false);

	function resetEditAndDelete() {
		editToggle = false;
		deleteToggle = false;
		handleEditOption();
	}

	const handleMenutToggle = () => {
		menuToggle = !menuToggle;
		editSectionToggle = false;

		if (editToggle && deleteToggle) {
			resetEditAndDelete();
		} else if (!editToggle) {
			editToggle = false;
		}
	};

	const handleAiToggle = () => {
		aibotSectionToggle = !aibotSectionToggle;
		menuToggle = false;

		if (editToggle && !deleteToggle) {
			editToggle = false;
			editSectionToggle = false;
			deleteToggle = false;
		} else if (editToggle) {
			handleEditOption();
		}
	};

	const handleEditMode = () => {
		editToggle = true;
		editSectionToggle = !editSectionToggle;
	};

	const handleEditToggleCall = () => {
		editToggle = true;
		editSectionToggle = !editSectionToggle;
		if (deleteToggle) {
			deleteToggle = false;
			handleEditOption();
		}
	};

	const handleDeleteProduct = () => {
		editSectionToggle = false;
		if (!deleteToggle) {
			deleteToggle = true;
			handleEditOption();
		}
	};
</script>

<div class="scanlyticsHeader">
	<div class="navBarMenu">
		<div class="navBarMenuHeader">
			<div
				class="NavBarSectionHead"
				style="background-color: {(menuToggle && !editToggle) || aibotSectionToggle
					? ' rgba(249, 87, 6, 0.988)'
					: '#000000a7'};"
				on:click={handleMenutToggle}
			>
				<!-- <img src="/logoww.png" alt="Logo" class="scanlyticsLogo" /> -->
			{#if aibotSectionToggle}
					<img src="robo.png" alt="roboIcon" class="roboIcon" />
				{:else}
					<img src="/logoww.png" alt="Logo" class="scanlyticsLogo" />
			{/if}
			</div>

			{#if menuToggle}
				<div class="navBarMenuContent">
					<div class="NavBarSection">
						<img src="plus1.png" alt="plusIcon" class="plusIcon" />
					</div>

					<div
						class="NavBarSection"
						style="background-color: {editToggle ? ' rgba(249, 87, 6, 0.988)' : '#000000a7'};"
						on:click={handleEditMode}
					>
						{#if deleteToggle}
							<img src="del.png" alt="deleteIcon" class="deleteIcon" />
						{:else}
							<img src="edit2.png" alt="editIcon" class="editIcon" />
						{/if}
					</div>

					<div
						class="NavBarSection"
						style="background-color: {aibotSectionToggle
							? ' rgba(249, 87, 6, 0.988)'
							: '#000000a7'};"
						on:click={handleAiToggle}
					>
						<img src="robo.png" alt="emailIcon" class="roboIcon" />
					</div>
					<div class="NavBarSection">
						<img src="sOut1.png" alt="signOutIcon" class="signOutIcon" />
					</div>
				</div>
			{/if}

			{#if editSectionToggle}
				<div class="editToggleSectionContainer">
					<div class="editContentArea">
						<div
							class="editContent"
							style="background-color: {editToggle && !deleteToggle && ' rgba(249, 87, 6, 0.988)'};"
							on:click={handleEditToggleCall}
						>
							Bearbeiten
						</div>
						<div
							class="editContent"
							style="background-color: {deleteToggle && ' rgba(249, 87, 6, 0.988)'};"
							on:click={handleDeleteProduct}
						>
							Löschen
						</div>
					</div>
				</div>
			{/if}

			{#if aibotSectionToggle}
				<!-- <div class="navBarMenuContentAI">
                    <div class="aiVisualizer">
                        
                    </div>
                </div> -->
			{/if}
		</div>
	</div>
	<div class="scanlyticsTitle">
		<h2>Scanlytics</h2>
	</div>
</div>

<style>
	.scanlyticsHeader {
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
		width: var(--navBarIconSectionWidth);
		height: var(--navBarIconSectionHeight);
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
		height: 400%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		flex-direction: column;
		/* background-color: rgb(187, 202, 21); */
		z-index: 5;
	}

	.editToggleSectionContainer {
		position: absolute;
		top: 240%;
		left: 100%;
		width: 250%;
		height: 200%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		flex-direction: column;
		/* background-color: rgb(187, 202, 21); */
		z-index: 5;
	}

	.editContentArea {
		width: 95%;
		height: 95%;
		/* background: rgba(31, 30, 30, 0.755); */
		/* background-color: #000000a7; */
		background-color: #585858;
		border-radius: 2px;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 5%;

		/* border: 1px solid white; */
		gap: 10px;
		/* justify-content: center; */
	}

	.editContent {
		width: 100%;
		height: 16%;
		/* background-color: rgb(251, 246, 247);  */
		/* background-color: rgb(255, 255, 255); */
		font-size: var(--editFontSize);
		padding-left: 2%;
		/* border-top: 1px solid rgb(1, 1, 1);
		border-bottom: 1px solid rgb(1, 1, 1); */
		cursor: pointer;
		color: white;
	}

	.editContent:hover {
		width: 100%;
		height: 16%;
		/* background-color: rgb(251, 246, 247);  */
		/* background-color: rgb(223, 245, 249);  */
		background-color: rgba(249, 87, 6, 0.988);
		color: white;
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

	.NavBarSectionHead {
		width: var(--scanlyticsLogoWidthSection);
		height: var(--scanlyticsLogoHighSectiont);
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

	.scanlyticsLogo {
		width: var(--scanlyticsLogoWidth);
		height: var(--scanlyticsLogoHeight);
	}

	.scanlyticsLogo:hover {
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

	.editIcon {
		width: 50%;
		height: 50%;
	}

	.deleteIcon {
		width: 57%;
		height: 59%;
	}
	.plusIcon {
		width: 50%;
		height: 50%;
	}

	.roboIcon {
		width: 70%;
		height: 75%;
	}
</style>
