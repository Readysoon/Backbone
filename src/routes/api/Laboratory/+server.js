import { json } from '@sveltejs/kit';
import { Room } from 'livekit-client';

const room = new Room();
const wsURL = 'wss://scanlyticsvoiceagentbot-jaea2320.livekit.cloud';

const handleFetchToken = async () => {
	try {
		const res = await fetch('http://127.0.0.1:8000/getToken', {
			method: 'GET'
		});

		const data = await res.json();
		return data;
		//  console.log('data', data);
	} catch (error) {
		console.error('Error on handleFetchToken', error);
	}
	return 'assas';
};
const handleConnectToRoom = async () => {
	const token = await handleFetchToken();

	console.log('token', token);

	// if (token) {
	// 	await room.connect(wsURL, token);
	// 	console.log('connected to room', room.name);

	// 	// Publish local camera and mic tracks
	// 	await room.localParticipant.enableCameraAndMicrophone();
	// }
};

/** @type {import('./$types').RequestHandler} */
export async function POST({ request }) {
	const { data } = await request.json();

	const token = handleConnectToRoom();
	// console.log('data', data);
	return json({ message: 'successful connected' });
}
