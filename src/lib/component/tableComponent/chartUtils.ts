
// chartUtils.ts
export function getApexChart(productName: string, chartData: number) {
  
    // let  charArrValue: number[]= Number




    // let arrNumber=  stringArray.map(chartData);

    

    console.log('chartData', chartData );
    return {
      chart: {
        type: "area",
        height: "100%",
        width: "100%",
        toolbar: { show: false },
      },
      title: {
        text: "Verlaufsübersicht (2018 - 2025)", // This will show the name as the chart title
        align: 'center', 
        offsetY: 18, 
          // You can use 'left', 'center', or 'right'
        style: {
         
          color: '#fff',   // Optional: set title color
          fontSize: '18px', 
          
          
        }
      },
    //   colors: ["red"],
      stroke: {
        curve: 'smooth',
        width: 5
      },
      series: [
        {
          name: productName,
          data: chartData,
        },
      ],
      xaxis: {
        categories: [2018, 2019, 2020, 2021, 2022, 2023, 2023, 2024, 2025],
        labels: {
          style: {
            colors: "#fff"
          }
        },
        axisBorder: {
          show: true,
          color: "#fff"
        },
        axisTicks: {
          show: true,
          color: "#fff"
        }
      },
      yaxis: {
        labels: {
          style: {
            colors: "#fff"
          }
        },
        axisBorder: {
          show: true,
          color: "#fff"
        },
        axisTicks: {
          show: true,
          color: "#fff"
        }
      }
    };
  }