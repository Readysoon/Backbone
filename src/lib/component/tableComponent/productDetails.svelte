<script lang="ts">
    let { selectedItem } = $props();

</script>


<div class="detailsComponentSection">
   
    <div class="detailsHeader">
        hallo from details 

        <div>   
            {selectedItem.Name} 
        </div>

        <div>
            go back
        </div>
    </div>
    <div>
        contentArea 
    </div>
    <div>
        Description

    </div>

</div>


<style>

    .detailsComponentSection{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .detailsHeader{
        width: 100%;
        height: 7%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        /* background-color: #fff; */
        border-bottom: 1px solid white;
        padding-left: 2%;
        padding-right: 2%;
    }

</style>