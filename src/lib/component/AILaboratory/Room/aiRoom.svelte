<script>
	const handleConnectToRoom = async () => {
		const res = await fetch('/api/Laboratory', {
			method: 'POST',
			body: JSON.stringify({ data: 'Hallo from frontend' }),
			headers: {
				'content-type': 'application/json'
			}
		});

		const data = await res.json();

		console.log('data message', data.message);
	};
</script>

<div class="aiSection">
	<div class="aiSectionContent">
		halolo
		<button on:click={handleConnectToRoom} class="handleConnectionToRoomBtn"> Call Server </button>
	</div>
</div>

<style>
	.aiSection {
		width: 70%;
		height: 100%;
		/* background-color: green; */
		display: flex;
		flex-direction: column;
		border-right: 1px solid rgba(255, 255, 255, 0.567);
		padding: 1%;
	}

	.aiSectionContent {
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.478);
		display: flex;
		flex-direction: column;
	}

	.handleConnectionToRoomBtn {
		height: 5%;
		width: 10%;
	}
</style>
