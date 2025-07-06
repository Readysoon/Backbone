<script lang="ts">
	import HeaderArea from '$lib/component/Header/headerArea.svelte';
	import SkeletenArea from '$lib/component/skeletonComponent/skeletenArea.svelte';

	let innerWidth: any;

	//   import * as productJson from '../../static/product.json';
	import Table from '$lib/component/tableComponent/table.svelte';
	import Tab from '$lib/component/TabOption/tab.svelte';
	import { RingLoader } from 'svelte-loading-spinners';
	let selectedOptionState = $state('Gesamt');
	let isMobile = $state(false);
	let loadingPage = $state(true);

	const handleTableOptionUpdate = (event: any) => {
		selectedOptionState = event.detail;
	};

	$effect(() => {
		const handleDeviceCheck = () => {
			loadingPage = false;
			if (innerWidth <= 1400) {
			
				isMobile = true;
			} else {
				isMobile = false;
			}
		};

		if (loadingPage) {
			handleDeviceCheck();
		}
	});
</script>

<svelte:window bind:innerWidth />



{#if loadingPage}
	<div class="laodingPageSection">
		<RingLoader size="100" color="orange" unit="px" duration="1s" />
		
	</div>
{:else}
	
		{#if isMobile}
			<div class="mobilePage">
				<p>Unfortunately, the app is not available on this screen size. Please switch to a different device and try again later.</p>
			</div>
		{:else}
		<main>
			<div class="mainContent">
				<div class="skeletArea">
					<SkeletenArea />
				</div>
				<div class="invetarArea">
					<HeaderArea />

					<Tab on:optionUpdate={handleTableOptionUpdate} {selectedOptionState} />

					<Table {selectedOptionState} />
				</div>
			</div>
		</main>
		{/if}
	
{/if}

<style>
	main {
		/* background-color: rgb(186, 107, 5); */
		/* margin: 0;
        padding: 0;
        width: 100%;
        height: 99vh;
        overflow: hidden;
        overflow-y: hidden; */
		width: 100%;
		/* background-color: rgb(105, 104, 104); */
		background-color: #cacaca;
		height: 100vh;
		padding: 10px;
	}

	.laodingPageSection {
		width: 100%;
		height: 100vh;
		display: flex;
		background-color: rgba(0, 0, 0, 0.097);
		/* color: rgb(15, 14, 14); */
		color: white;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 4%;
	}
	.mobilePage {
		width: 100%;
		height: 100vh;
		display: flex;
		color: rgb(255, 255, 255);
		display: flex;
		justify-content: center;
		align-items: center;
	    text-align: center;
		font-family: system-ui;
		padding: 5%;
	
	}

	.mainContent {
		/* background-color: green; */
		width: 100%;
		height: 100%;
		display: flex;

		/* gap: 2%; */
	}

	.invetarArea {
		/* background-color: pink; */
		height: 100%;
		width: 50%;
		display: flex;
		flex-direction: column;
		gap: 1%;
		/* border-right: 1px solid #acacae; */
	}

	.skeletArea {
		/* background-color: black; */
		height: 100%;
		width: 50%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
