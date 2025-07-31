<script lang="ts">
	import { Room } from 'livekit-client';
	import { setError, clearError } from '$lib/stores/errorStore';

	let fetchedtoken: any = $state({});
	let wsUrl: string = $state('');
	let connectToRoom = $state(false);

	// Asynchronously attempts to connect to the LiveKit room by requesting a token and WebSocket URL from the backend.
	// On success, updates the connection state and stores the token and URL for later use.
	const handleConnectToRoom = async () => {
		try {
			const res = await fetch('/api/Laboratory', {
				method: 'POST',
				body: JSON.stringify({ data: 'Hallo from frontend' }),
				headers: {
					'content-type': 'application/json'
				}
			});

			// Declearing the data
			const data = await res.json();

			if (data.statuscode === 200) {
				fetchedtoken = data.token.token;
				wsUrl = data.wsURLData;
				connectToRoom = true;
			} else {
				alert('LiveKit connection Issue, check authToken or wsUrl');
			}
		} catch (error) {
			if (error instanceof Error) {
				setError({
					message: error.message || 'An unexpected error occurred',
					type: 'Authentication',
					code: (error as any).code ?? null,
					details: error
				});
			} else {
				setError({
					message: 'An unexpected error occurred',
					type: 'network',
					code: null,
					details: error
				});
			}
		}
	};

	$effect(() => {
		// connect to the LiveKit room
		const handleConnectToliveKit = async () => {
			try {
				const room = new Room();
				await room.connect(wsUrl, fetchedtoken);
				console.log('connected to room', room.name);

				// Publish local camera and mic tracks
				await room.localParticipant.enableCameraAndMicrophone();
			} catch (error) {
				if (error instanceof Error) {
					setError({
						message: error.message || 'An unexpected error occurred',
						type: 'connection', // or whatever type fits
						code: (error as any).code ?? null, // if error.code might exist
						details: error
					});
				} else {
					setError({
						message: 'An unexpected error occurred',
						type: 'connnection',
						code: null,
						details: error
					});
				}
			}
		};

		// If the connection state is true, initiate the process to connect to the LiveKit room.
		if (connectToRoom) {
			handleConnectToliveKit();
		}
	});
</script>

<div class="aiSection">
	<div class="aiSectionContent">
		
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
