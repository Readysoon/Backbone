<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	const dispath = createEventDispatcher();

	let { selectedOptionState } = $props();

	const handleTableOptionUpdate = (selectedObj: string) => {
		dispath('optionUpdate', selectedObj);
	};
</script>

<div class="navArea">
	<div
		class="navBox"
		style="background-color: {selectedOptionState == 'Gesamt' ? '#2369f6dd' : '#000000a7'};
border:{selectedOptionState == 'Gesamt' ? '2px solid #004cff8f;' : ' 2px solid #33333332'}
"
		on:click={() => handleTableOptionUpdate('Gesamt')}
	>
		Gesamt
	</div>
	<div
		class="navBox"
		style="background-color: {selectedOptionState == 'Verfügbar' ? '#2369f6dd' : '#000000a7'};
border:{selectedOptionState == 'Verfügbar' ? '2px solid #004cff8f;' : ' 2px solid #33333332'}
"
		on:click={() => handleTableOptionUpdate('Verfügbar')}
	>
		Verfügbar
	</div>
	<div
		class="navBox"
		style="background-color: {selectedOptionState == 'Nicht vorrätig' ? '#2369f6dd' : '#000000a7'};
border:{selectedOptionState == 'Nicht vorrätig' ? '2px solid #004cff8f;' : ' 2px solid #33333332'}
"
		on:click={() => handleTableOptionUpdate('Nicht vorrätig')}
	>
		Nicht vorrätig
	</div>
	<div
		class="navBox"
		style="background-color: {selectedOptionState == 'Warnung' ? '#2369f6dd' : '#000000a7'};
border:{selectedOptionState == 'Warnung' ? '2px solid #004cff8f;' : ' 2px solid #33333332'}
"
		on:click={() => handleTableOptionUpdate('Warnung')}
	>
		Warnung
	</div>
</div>

<style>
	.navArea {
		background-color: var(--tabBackground);
		width: 100%;
		height: 7%;
		display: flex;
		justify-content: space-around;
		align-items: center;
		gap: 2%;
	}
	.navBox {
		/* background-color: #22c4e47e; */
		background-color: #000000a7;
		width: 20%;
		height: 60%;
		border-radius: 50px;
		/* border: 2px solid #22c4e4a9; */
		border: 2px solid #33333332;
		display: flex;
		justify-content: center;
		align-items: center;
		color: white;
		cursor: pointer;

		font-size: var(--tabBtn-fontSize);
	}

/*     
	.navBox1 {
		background-color: #2369f6dd;
		
		width: 20%;
		height: 60%;
		border-radius: 50px;
		border: 2px solid #004cff8f;
		display: flex;
		justify-content: center;
		align-items: center;
		color: white;

		font-size: 22px;
	} */
</style>
