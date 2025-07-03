



<script  lang="ts" module>
   
 

 
</script>

<script>

  import { getApexChart } from "./chartUtils";
  import { chart } from 'svelte-apexcharts?client';


  let {selectedItem} = $props()

  let options = getApexChart(`${selectedItem.name}`, selectedItem.chartData)
  
</script>


<div class="charArea">
   
    <div use:chart={options}  />

</div>


<style>
    .charArea{
        height: 100%;
        width: 100%;
        /* background-color: #fff; */
    }

</style>