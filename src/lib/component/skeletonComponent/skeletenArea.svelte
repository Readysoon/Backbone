<script lang="ts">
	import { Application } from '@splinetool/runtime';
	import Header from './Header/header.svelte';
	import ContentBody from './Body/contentBody.svelte';

	let loading: boolean = true;
	let canvas: any;

	$effect(() => {
		const handleCallBruno = () => {
			let app = new Application(canvas);
			loading = true;
			const splineobj = app
				.load('https://prod.spline.design/gHGa7XTERPOXgvOV/scene.splinecode')
				.then(() => {
					const obj = app.findObjectByName('brunov1');
					// console.log('obj', obj);
					// if (obj?.position) {
					// Adjust position
					// 	console.log('iits in postion',obj?.position);
					// 	obj.position.x += 10;
					// 	obj.position.y = 50;
					// 	obj.position.z -= -15;
					// 	}
					loading = false;

					// }
				});
		};

		handleCallBruno();
	});
</script>

<div class="skeletSection">
	<!-- Skeleton Heaader Section -->
	<Header />

	<!-- Skeleton Body Section -->
	<ContentBody />

	<!-- <div class="aibotAvatar">
   
            <canvas bind:this={canvas} class="avater" />
       
       
    </div> -->
</div>

<style>
	.skeletSection {
		/* background-color: pink; */
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.aibotAvatar {
		/* background-color: rgba(226, 17, 52, 0.619); */
		width: 10%;
		height: 10%;
		/* margin-top: 10%; */
		position: absolute;
		top: 90%;
		left: -2%;
		z-index: 5;
	}
</style>
