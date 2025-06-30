

<script>
//   import * as productJson from '../../static/product.json';
import Table from "$lib/component/table.svelte";

</script>

<main>
 <div class="mainContent">
    <div class="skeletArea">
        <div class="scanlyticsHader">
            <img src="/logo.png" alt="Logo" height="35" width="40" />
            <h2>Scanlytics</h2>
        </div>
        <div class="skeletonBodyAra">
            <img src="skelet.png" alt="skseltImage" class="skeletImage">
        </div>
       



    </div>
     <div class="invetarArea">
        <div class="headerArea">
            <div class="headerContentSection">
                <div class="headerSearchContent">
                  <!-- <div class="searchItem">
                    search
                  </div> -->
                  <input type="text" class="searchItemInput" placeholder="Enter Product Name">
                </div>
                <div class="headerMarkContent">
                    <div class="markOption">
                      
                        <div class="markerOptionTitle">
                            Marker 
                        </div>

                        <div class="markerOptionToggle">
                            <img src="down.png" alt="down" class="dropDownIcon" >
                        </div>
                    </div>
                   
                </div>
                <div class="alertMarkContent">
                    <div class="statusOption">
                        <div class="statusOptionTitle">
                            Channel 
                        </div>

                        <div class="statusOptionToggle">
                            <img src="down.png" alt="down" class="dropDownIcon">
                        </div>
                    </div>
                </div>

            </div>
        </div>
       
        <div class="navArea">
           <div class="navBox1">
            Total
           </div>
           <div class="navBox">
            Available
           </div>
           <div class="navBox">
            out of Stock
           </div>
           <div class="navBox">
            Alert
           </div>
        </div>

        <div class="listArea">
            <div class="listContectSection">
               <Table/>
            </div>
        </div>

       
     </div>
    

 </div>
</main>

<style>
    html, body, main{
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
        /* background-color: green; */
        width: 100%;
        height: 100%;
        display: flex;
       
        /* gap: 2%; */
    }


    .invetarArea{
        /* background-color: pink; */
        height: 100%;
        width: 50%;
        display: flex;
        flex-direction: column;
        gap: 1%;
        /* border-right: 1px solid #acacae; */

    }

    .headerArea{
        /* background-color: grey; */
        width: 100%;
        height: 7%;
        display: flex;
        justify-content: center;
        align-items: center;
    }


    
    .headerContentSection{
        width: 97%;
        height: 100%;
        /* background-color: #282530; */
        /* border-radius: 7px; */
        /* border: 1px solid #acacae38; */
        display: flex;
        align-items: center;
        gap: 2%;
    }


    .headerSearchContent{
        /* background-color: #b11f1f; */
        width: 70%;
        height: 100%;
        display: flex;
        display: flex;
        align-items: center;
        /* border-radius: 50px; */

    }

    .searchItemInput{
        background-color: #ffffff8b;
        width: 100%;
        height: 50%;
        display: flex;
        border-radius: 50px;
        padding-left: 3%;
        font-size: 22px;
    }
    .headerMarkContent{
        /* background-color: pink; */
        width: 15%;
        height: 100%;
        display: flex;
        align-items: center;
        
        /* border-radius: 50px; */
    }

    .markOption{
        /* background-color: #fff; */
         /* background-color: #1a0e6b; */
        background-color: #000000a7;
        width: 100%;
        height: 50%;
        display: flex;
        border-radius: 7px;
        border: 2px solid #33333332;
        color: white;
        display: flex;
        align-items: center;
        box-shadow: 0 0.5px 12px -4px white;
        /* justify-content: center; */
        font-size: 22px;
       
        cursor: pointer;

    }

    .markerOptionTitle{
        /* background-color: pink; */
        height: 100%;
        width: 75%;
        padding-left: 5%;
        display: flex;
        align-items: center;
    }


    .markerOptionToggle{
        /* background-color: rgb(192, 204, 255); */
        height: 100%;
        width: 25%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

 

    .dropDownIcon{
        height: 50%;
        width: 50%;
    }

    .alertMarkContent{
        /* background-color: green; */
        width: 15%;
        height: 100%;
        display: flex;

        align-items: center;
        /* border-radius: 50px; */
    }

    .statusOption{
        background-color: #000000a7;
        width: 100%;
        height: 50%;
        display: flex;
        border-radius: 7px;
        border: 2px solid #33333332;
        color: white;
        display: flex;
        align-items: center;
        /* justify-content: center; */
        font-size: 22px;
        padding-left: 5%;
        cursor: pointer;
        /* font-family: system-ui; */
        /* font-family:  Helvetica; */
        
    }

    .statusOptionTitle{
        height: 100%;
        width: 75%;
        padding-left: 5%;
        display: flex;
        align-items: center;
    }

    .statusOptionToggle{
        height: 100%;
        width: 25%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .listArea{
        /* background-color: black; */
        width: 100%;
        height: 85%;
        display: flex;
        justify-content: center;
        align-items: center;
        /* border: 1px solid #acacae; */

    }
    .listContectSection{
        width: 97%;
        height: 100%;
        /* background-color: #282530; */
        background-color: #1b1b1bcd;
        /* background-color: pink; */
        border-radius: 7px;
        border: 1px solid #acacae38;
    }

    .navArea{
        /* background-color: rgb(202, 20, 20); */
        width: 100%;
        height: 7%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        gap: 2%;

    }

    .navBox{
        /* background-color: #22c4e47e; */
        background-color: #000000a7;
        width: 20%;
        height: 60%;
        border-radius: 50px;
        /* border: 2px solid #22c4e4a9; */
        border: 2px solid #33333332;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        
        font-size: 22px;
    }

    .navBox1{
        background-color: #2369f6dd;
        /* background-color: rgba(255, 98, 0, 0.82); */
        /* background-color: #000000a7; */
        width: 20%;
        height: 60%;
        border-radius: 50px;
        border: 2px solid #004cff8f;
        /* border: 2px solid #a54103; */
     
        /* border: 2px solid #33333332; */
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        
        font-size: 22px;
    }

    .navContentSection{
        width: 97%;
        height: 70%;
        background-color: #282530;
        border-radius: 7px;
        border: 1px solid #acacae38;

    }

 

    .skeletArea{
        /* background-color: black; */
        height: 100%;
        width: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .scanlyticsHader{
        width: 100%;
        height: 7%;
        /* background-color: pink; */
        font-family: system-ui;
        color: black;
        display: flex;
        align-items: center;
        padding-left: 1%;
        font-size: 33px;
        gap: 1%;
    }

    .skeletonBodyAra{
        width: 100%;
        height: 90%;
        /* background-color: green; */
        display: flex;
        align-items: center;
       justify-content: center;
    }

    .skeletImage{
        width: 40%;
        height: 77%;
    }


</style>