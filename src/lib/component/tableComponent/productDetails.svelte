<script lang="ts">
	let { selectedItem } = $props();
	import { createEventDispatcher } from 'svelte';
	import AreaChart from './AreaChart.svelte';
	const dispath = createEventDispatcher();
	let imgData = $state('p1.png');
	


	let images = $state([`dp1.png`, `dp3.png`, `dp4.png`]);

	const handleReturnToProductList = () => {
		dispath('returnToProduct');
	};

	const handleUpdateImage = (imgObj: any) => {
		if (!images.includes(imgData)) {
			images.push(imgData);

			images = images.filter((item: any) => item != imgObj);

			imgData = imgObj;
		}
	};


	
</script>

<div class="detailsComponentSection">
	<!-- Header Section -->
	<div class="detailsHeader">
		<div class="HeadTitleSection">
			<!-- {selectedItem.name} -->
			Produkt Information
		</div>

		<div class="HeadGoBackSection" on:click={handleReturnToProductList}>
			<div class="arrowSecion">
				<img src="leftArrow.png" alt="leftArrowIcon" class="leftArrowIcon" />
			</div>
		</div>
	</div>
	<div class="productContentSection">
		<div class="productImageSection">
			<div class="productMainImage">
				<img src={imgData} alt="ProductImage" class="productImage" />
			</div>

			<div class="productDetailedImage">
				{#if images}
					{#each images as image}
						<img
							src={image}
							alt="images"
							class="detailedImage"
							on:click={() => handleUpdateImage(image)}
						/>
					{/each}
				{/if}
			</div>
		</div>
		<div class="productMetaDataSection">
			<!-- <div class="productMetaHeader">
			
			</div> -->

            <div class="productMetaTab">
                <div>SDK:</div>

				<div>{selectedItem.sdk}</div>
			</div>

			<div class="productMetaTab">
				<div>Name:</div>

				<div>
					{selectedItem.name}
				</div>
			</div>

			<div class="productMetaTab">
				<div>Status</div>

				<div>
					{selectedItem.productzustand}
				</div>
			</div>

			<div class="productMetaTab">
				<div>Anzahl:</div>

				<div>
					{selectedItem.status}
				</div>
			</div>

			<div class="productMetaTab">
				<div>Maße:</div>

				<div>{selectedItem.masse}</div>

				
			</div>

            <div class="productMetaTab">
				<div>Hersteller:</div>

				<div>{selectedItem.hersteller}</div>

				
			</div>

            <div class="productMetaTab">
				<div>Bewarhungsort:</div>

				<div>{selectedItem.bewahrungsort}</div>

				
			</div>

            
            <div class="productMetaTab">
				<div>Bestellungtag:</div>

				<div>{selectedItem.bestellungstag}</div>

				
			</div>

             
            <div class="productMetaTab">
				<div>AnscprechPartner:</div>

				<div>{selectedItem.ansprechpartner}</div>

				
			</div>

            <div class="productMetaTab">
				<div>Beschreibung:</div>

				

				
			</div>
            <div class="productMetaDescription">
                {selectedItem.beschreibung}
            </div>





			<!-- <div class="productMetaContent"></div> -->
		</div>
	</div>
	<div class="DescriptionSection">
        <AreaChart
		{selectedItem}
		 />
    </div>
</div>

<style>
	.detailsComponentSection {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
	}

	.detailsHeader {
		width: 100%;
		height: 7%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		/* background-color: #fff; */
		border-bottom: 1px solid white;
		/* padding-left: 2%; */
		/* padding-right: 2%; */
	}

	.HeadTitleSection {
		width: 80%;
		height: 100%;
		/* background-color: #fff; */
		padding-left: 2%;
		display: flex;
		align-items: center;
		font-size: var(--productFontSize);
		color: white;
	}

	.HeadGoBackSection {
		width: 20%;
		height: 100%;
		/* background-color: #fff; */
		/* padding-left: 2%;  */
		display: flex;
		justify-content: flex-end;
		align-items: center;
		font-size: 22px;
		color: white;
		padding-right: 2%;
	}

	.arrowSecion {
		width: 22%;
		height: 60%;
		/* background-color: #fff; */
		border-radius: 7px;
		border: 2px solid white;
		display: flex;
		justify-content: center;
		align-items: center;
		/* padding: 1%; */
		cursor: pointer;
	}

	.arrowSecion:hover {
		background-color: rgb(194, 31, 31);
		border: 2px solid black;
	}

	.leftArrowIcon {
		height: 55%;
		width: 50%;
	}

	.productContentSection {
		width: 100%;
		height: 70%;
		/* background-color: green; */
		display: flex;
		flex-direction: row-reverse;
		border-bottom: 1px solid white;
	}

	.productImageSection {
		width: 50%;
		height: 100%;
		/* background-color: rgba(255, 255, 255, 0.966); */

		display: flex;
		/* justify-content: center; */
		/* align-items: center; */

		flex-direction: column;

		/* border-bottom: 1px solid white; */
	}

	.productMainImage {
		width: 100%;
		height: 70%;
		/* background-color: green; */
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}

	.productDetailedImage {
		width: 100%;
		height: 30%;
		/* background-color: rgb(243, 113, 113); */
		display: flex;
		gap: 8%;
		/* padding: 1%; */

		justify-content: space-around;
		align-items: center;
	}

	.defaultImageSelectionArea {
		width: 100%;
		height: 100%;
		background-color: blue;
		display: flex;
	}

	.detailedImage {
		width: 19%;
		height: 50%;
		/* background-color:  rgb(255, 255, 255); */
		border: 1px solid skyblue;
		border-radius: 7px;
		cursor: pointer;
		/* padding: 1%; */
	}

	.detailedImage:hover {
		background-color: #4eccfa4f;
	}
	.productImage {
		height: 60%;
		width: 80%;
		opacity: 0.9;
	}

	.productMetaDataSection {
		width: 50%;
		height: 100%;
        padding-top: 2%;
        display: flex;
        flex-direction: column;
		/* align-items: center; */
        gap: 3%;
        justify-content: center;
        /* align-items: center; */
    
		/* border-right: 1px solid white; */
		/* background-color: skyblue; */
		/* border-left: 1px solid white; */
	}

	

	.productMetaTab {
		width: 100%;
		height: 7%;
		/* background-color: #b14d4d9c; */
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-left: 4%;
		font-size: 20px;
		color: white;
	}

    .productMetaDescription{
        width: 100%;
		height: 23%;
		/* background-color: #24e250; */
		display: flex;
		justify-content: space-between;
		/* align-items: center; */
		padding-left: 4%;
		font-size: 20px;
		color: white;
    }

	.tabBox {
		width: 20%;
		height: 50%;
		background-color: rgba(25, 235, 6, 0.24);
		border-radius: 7px;
		border: 1px solid rgba(255, 255, 255, 0.236);
		cursor: pointer;
	}
	.productMetaContent {
		width: 100%;
		height: 80%;
		/* background-color: #db363652; */
	}

	.DescriptionSection {
		width: 100%;
		height: 23%;
		/* background-color: #cacaca; */
	}
</style>
