<script lang="ts">
	import HeaderArea from '$lib/component/Header/headerArea.svelte';
	import SkeletenArea from '$lib/component/skeletonComponent/skeletenArea.svelte';

	//   import * as productJson from '../../static/product.json';
	import Table from '$lib/component/tableComponent/table.svelte';
	import Tab from '$lib/component/TabOption/tab.svelte';
	let selectedOptionState = $state('Gesamt');

	const handleTableOptionUpdate = (event: any) => {
		selectedOptionState = event.detail;
	};
</script>

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

	.mainContent {
		/* background-color: green; */
		width: 100%;
		height: 100%;
		display: flex;

		/* gap: 2%; */
	}

	.invetarArea {
		background-color: pink;
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
