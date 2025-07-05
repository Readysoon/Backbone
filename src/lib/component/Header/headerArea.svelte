<script>
</script>

<div class="headerArea">
	<div class="headerContentSection">
		<div class="headerSearchContent">
			
			<input type="text" class="searchItemInput" placeholder="Enter Product Name" />
		</div>
		<div class="headerMarkContent">
			
			<select name="" id="" class="markerOptionSelect">
				<option value="Produkt">Produkt</option>
				<option value="Platten">Platten (Osteosyntheseplatten)</option>
				<option value="Schrauben">Schrauben</option>
				<option value="Marknägel">Marknägel</option>
				<option value="Knochendrähte">Knochendrähte (Kirschnerdrähte)</option>
				<option value="Endoprothesen">Endoprothesen (z.B. Hüftprothese, Knieprothese)</option>
				<option value="Knochensubstitute">Knochensubstitute</option>
				<option value="Fixateure externe">Fixateure externe</option>
				<option value="Spacer">Spacer (Platzhalter)</option>
				<option value="Knochenanker">Knochenanker</option>
				<option value="Bandscheibenprothesen">Bandscheibenprothesen</option>
				<option value="Knochenzement">Knochenzement</option>
				<option value="Orthesen">Orthesen/Schienen</option>
			</select>

			
		</div>
		<div class="alertMarkContent">
			<!-- <div class="statusOption"> -->
			<select name="" id="" class="statusOptionSelect">
				<option value="Hersteller">Hersteller</option>
				<option value="DePuy Synthes">DePuy Synthes (Johnson & Johnson)</option>
				<option value="Stryker">Stryker</option>
				<option value="Zimmer Biomet">Zimmer Biomet</option>
				<option value="Smith & Nephew">Smith & Nephew</option>
				<option value="B. Braun Aesculap">B. Braun Aesculap</option>
				<option value="Medartis">Medartis</option>
				<option value="Orthofix">Orthofix</option>
				<option value="Wright Medical">Wright Medical</option>
				<option value="Arthrex">Arthrex</option>
			</select>
		
		</div>
	</div>
</div>

<style>
	.headerArea {
		background-color: var(--leftHeaderBackground);
		width: 100%;
		height: var(--Leftheader-height);
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.headerContentSection {
		width: 97%;
		height: 100%;
		/* background-color: #282530; */
		/* border-radius: 7px; */
		/* border: 1px solid #acacae38; */
		display: flex;
		align-items: center;
		gap: 2%;
	}

	.headerSearchContent {
		/* background-color: #b11f1f; */
		width: 70%;
		height: 100%;
		display: flex;
		display: flex;
		align-items: center;
		/* border-radius: 50px; */
	}

	.searchItemInput {
		background-color: #ffffff8b;
		width: 100%;
		height: var(--leftHeaderInput-hieight);
		display: flex;
		border-radius: 50px;
		padding-left: 3%;
		font-size: var(--tabBtn-fontSize);
	}
	.headerMarkContent {
		/* background-color: pink; */
		width: 15%;
		height: 100%;
		display: flex;
		align-items: center;

		/* border-radius: 50px; */
	}

	.markerOptionSelect {
		/* background-color: pink; */
		background-color: #000000a7;
		height: 50%;
		width: 100%;
		padding-left: 5%;
		display: flex;
		align-items: center;
		color: white;
		font-size: var(--tabBtn-fontSize);
		border-radius: 7px;
		border: 2px solid #33333332;
		box-shadow: 0 0.5px 12px -4px white;
		cursor: pointer;
	}



	.alertMarkContent {
		/* background-color: green; */
		width: 15%;
		height: 100%;
		display: flex;

		align-items: center;
		/* border-radius: 50px; */
	}

	.statusOptionSelect {
		background-color: #000000a7;
		height: 50%;
		width: 100%;
		/* padding-left: 5%; */
		display: flex;
		align-items: center;
		border-radius: 7px;
		color: white;
		padding-left: 5%;
		font-size: var(--tabBtn-fontSize);;
		border: 2px solid #33333332;
		box-shadow: 0 0.5px 12px -4px white;
		cursor: pointer;
	}




    
    /* Smart Phones */
	@media (min-width: 320px) and (max-width: 460px) {

    }
    /*  ipads (e.g. 1366px - 1440px wide) */
	@media (min-width: 768px){

    }

    	/* Small laptops (e.g. 1366px - 1440px wide) */
	@media (min-width: 1280px){

    }
    	/* Mid laptops (your 1807px screen) */
	@media (min-width: 1700px) {

    }

    /* Large Screen */
    @media (min-width: 2560px){

    }
</style>
