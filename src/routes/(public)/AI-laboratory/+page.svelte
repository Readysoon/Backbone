<script>
    import AiRoom from "$lib/component/AILaboratory/Room/aiRoom.svelte";
    import AiEditor from "$lib/component/AILaboratory/Editor/aiEditor.svelte";




    

</script>



<main>
    <div class="mainContent">

        <!-- AI Room Component Section -->
        <AiRoom/>

        <!-- Editor Component Section -->
        <AiEditor/>
      
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
.mainContent{
    /* background-color: pink; */
    width: 100%;
	height: 100%;
	display: flex;
   
}


</style>