import { json } from '@sveltejs/kit';
import { Room } from 'livekit-client';
import { env } from '$env/dynamic/private';

const wsURL = env.WSURL;

const handleFetchToken = async () => {
	try {
		const res = await fetch('http://127.0.0.1:8000/getToken', {
			method: 'GET'
		});

		const token = await res.json();
		
		return token;
	} catch (error) {
		console.error('Error on handleFetchToken', error);
	};
};

/** @type {import('./$types').RequestHandler} */
export async function POST({ request }) {
	const { data } = await request.json();

	const token = await handleFetchToken();
	if (token) {
		console.log('token', token);

		return json({ token: token, wsURLData: wsURL , statuscode: 200});
	}
	// console.log('data', data);
	return json({ message: 'Unsuccessful connection', statuscode: 400 });
}
