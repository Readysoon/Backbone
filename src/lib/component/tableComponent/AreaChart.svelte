

<script >

// import { chart } from "svelte-apexcharts";
// import {chart} from 'svelte-apexcharts'
//   let options = {
//     chart: {
//       type: "bar",
//     },
//     series: [
//       {
//         name: "sales",
//         data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
//       },
//     ],
//     xaxis: {
//       categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999],
//     },
//   };
</script>


<script  lang="ts" module>
    import { chart } from 'svelte-apexcharts?client';
    import { onMount } from 'svelte'

      let options = {
    chart: {
      type: "area",
      height: 270,  // z. B. 400px
    //   width: 1000,
      toolbar: { show: false },
    },
    stroke: {
      curve: 'smooth',
      width: 5
    },
    series: [
      {
        name: "Inventar",
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
      },
    ],
    xaxis: {
      categories: [2018, 2019, 2020, 2021, 2022, 2023, 2023, 2024, 2025],
    },
  };
 
</script>


<div class="charArea">
    <!-- djsd -->
    <div use:chart={options}  />
</div>


<style>
    .charArea{
        height: 100%;
        width: 100%;
        /* background-color: #fff; */
    }

</style>