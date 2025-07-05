<script lang="ts" module>
</script>

<script lang="ts">
	import * as ProductData from '../../../../static/product.json';
	import ProductDetails from './productDetails.svelte';
	import { Circle2 } from 'svelte-loading-spinners';

	let { selectedOptionState } = $props();
	let selectedItem: any = $state(null);
	let LoadPage = $state(false);

	const handleselectedObj = (itemObj: any) => {
		console.log('itemObj', itemObj);

		selectedItem = selectedItem == itemObj ? null : itemObj;
	};

	const handleReturnBackToList = () => {
		console.log('clickedReturnBack');
		selectedItem = null;
		LoadPage = false;
	};

	$effect(() => {
		const handleLoadPage = () => {
			const intervalId = setInterval(() => {
				LoadPage = true;
				clearInterval(intervalId);
			}, 2700);
		};

		if (!LoadPage) {
			handleLoadPage();
		}
	});
</script>

<div class="listArea">
	<div class="listContectSection">
		{#if ProductData}
			{#if selectedItem != null}
				{#if LoadPage}
					<div class="ProductDetails">
						<ProductDetails {selectedItem} on:returnToProduct={handleReturnBackToList} />
					</div>
				{:else}
					<div class="loadSection">
						<Circle2 size="150" colorOuter="blue" unit="px" durationInner="1s" />
					</div>
				{/if}
			{:else}
				{#each ProductData.productHeader as itemHead (itemHead)}
					<div class="productHeadSection">
						<div class="boxId">
							{itemHead.IdHead}
						</div>
						<div
							class="boxName"
							style="width: {selectedOptionState === 'Verfügbar'
								? '40%'
								: selectedOptionState === 'Nicht vorrätig'
									? '40%'
									: '39.5%'}"
						>
							{itemHead.NameHead}
						</div>
						<div class="boxBestand">
							{itemHead.StockHead}
						</div>
						<div class="boxStatus">
							{itemHead.StatusHead}
						</div>
					</div>

					<div class="productContentSection">
						{#each ProductData.productContent.filter( (item: any) => (selectedOptionState == 'Gesamt' ? item.productzustand != selectedOptionState : item.productzustand == selectedOptionState) ) as itemContent (itemContent)}
							<div class="boxContentObj" on:click={() => handleselectedObj(itemContent)}>
								<div class="contentId">
									{itemContent.Id}
								</div>

								<div class="contentName">
									{itemContent.name}
								</div>

								<div class="contentBestand">
									{itemContent.stock}
								</div>

								<div class="contentStatus">
									<!-- {itemContent.stock} -->
									<div class="backBar">
										<div
											class="loadBar"
											style="
                  background-color: {itemContent.status <= 25
												? 'red'
												: itemContent.status <= 50
													? 'orange'
													: 'green'};
                  width:  {itemContent.status && `${itemContent.status}%`};
                  "
										></div>
									</div>
								</div>
							</div>
						{/each}
					</div>
				{/each}
			{/if}
		{/if}
	</div>
</div>

<style>
	.listArea {
		/* background-color: black; */
		width: 100%;
		height: 85%;
		display: flex;
		justify-content: center;
		align-items: center;
		/* border: 1px solid #acacae; */
	}
	.listContectSection {
		width: 97%;
		height: 100%;
		/* background-color: #282530; */
		background-color: #1b1b1bcd;
		/* background-color: pink; */
		border-radius: 7px;
		border: 1px solid #acacae38;
	}
	.ProductDetails {
		width: 100%;
		height: 100%;
	}

	.loadSection {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.productHeadSection {
		background-color: rgb(30, 31, 30);
		/* background-color: var(--tableHeaderBackground); */
		height: 5%;
		width: 100%;
		border-bottom: 1px solid rgba(255, 255, 255, 0.397);
		display: flex;
		border-top-left-radius: 7px;
		border-top-right-radius: 7px;
	}

	.productContentSection {
		height: 95%;
		width: 100%;
		gap: 3.5%;
		display: flex;
		flex-direction: column;
		padding-top: 2%;
		overflow: auto;
		/* Scrollbar Styling */
		scrollbar-width: thin;
		scrollbar-color: #444 #232323;
	}

	.productContentSection::-webkit-scrollbar {
		width: 10px;
		background: #232323;
		border-radius: 8px;
	}
	.productContentSection::-webkit-scrollbar-thumb {
		background: linear-gradient(120deg, #444 40%, #2369f6dd 100%);
		border-radius: 8px;
		min-height: 40px;
		transition: background 0.3s;
	}
	.productContentSection::-webkit-scrollbar-thumb:hover {
		background: linear-gradient(120deg, #2369f6dd 40%, #444 100%);
	}
	.productContentSection::-webkit-scrollbar-corner {
		background: #232323;
	}

	.boxId {
		width: 7%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableHeaderFont-Size);
		font-weight: bold;
		font-family: system-ui;
	}

	.boxName {
		width: 39.5%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableHeaderFont-Size);
		font-weight: bold;
		font-family: system-ui;
	}

	.boxBestand {
		width: 23%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableHeaderFont-Size);
		font-weight: bold;
		font-family: system-ui;
	}

	.boxStatus {
		/* background-color: pink; */
		width: 30%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		/* border-right: 1px solid rgba(255, 255, 255, 0.397); */
		color: white;
		font-size: var(--tableHeaderFont-Size);
		font-weight: bold;
		font-family: system-ui;
	}

	.boxContentObj {
		width: 100%;
		/* height: 60px; */
		min-height: var(--tableminHeight);
		background-color: #f8f9f91d;

		display: flex;
		/* justify-content: center; */
		align-items: center;
		/* border-right: 1px solid rgba(255, 255, 255, 0.397); */
		color: white;
		font-size: 19px;
		border-top: 1px solid rgba(255, 255, 255, 0.397);
		border-bottom: 1px solid rgba(255, 255, 255, 0.397);
	}

	.boxContentObj:hover {
		background-color: #2369f652;
		border: 2px solid #004cff8f;
		cursor: pointer;
	}

	.contentId {
		width: 7%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableFont-Size);
	}

	.contentName {
		width: 40%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableFont-Size);
	}

	.contentBestand {
		width: 23%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border-right: 1px solid rgba(255, 255, 255, 0.397);
		color: white;
		font-size: var(--tableFont-Size);
	}

	.contentStatus {
		width: 30%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		/* border-right: 1px solid rgba(255, 255, 255, 0.397); */
		color: white;
		font-size: var(--tableFont-Size);
	}

	.backBar {
		background: rgb(178, 177, 177);
		width: 70%;
		height: 25%;
		border-radius: 50px;
	}

	.loadBar {
		background: rgb(243, 20, 20);
		width: 70%;
		height: 100%;
		border-radius: 50px;
	}
</style>
