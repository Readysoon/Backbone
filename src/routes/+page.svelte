

<script>

</script>

<main>
 <div class="mainContent">
    <div class="skeletArea">
        <div class="scanlyticsHader">
            <img src="/logow.jpg" alt="Logo" height="35" width="34" />
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
                  <div class="searchItem">
                    search 
                  </div>
                </div>
                <div class="headerMarkContent">
                    <div class="markOption">
                        Marker
                    </div>
                </div>
                <div class="alertMarkContent">
                    <div class="alertOption">
                        Status
                    </div>
                </div>

            </div>
        </div>

        <div class="listArea">
            <div class="listContectSection">

            </div>
        </div>

        <div class="navArea">
            <div class="navContentSection">

            </div>
        </div>
     </div>
    

 </div>
</main>

<style>
    html, body, main{
        background-color: rgb(186, 107, 5);
        /* margin: 0;
        padding: 0;
        width: 100%;
        height: 99vh;
        overflow: hidden;
        overflow-y: hidden; */
        width: 100%;
        background-color: rgb(0, 0, 0);
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
        height: 10%;
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

    .searchItem{
        background-color: #fff;
        width: 100%;
        height: 40%;
        display: flex;
        border-radius: 50px;
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
        width: 100%;
        height: 40%;
        display: flex;
        border-radius: 7px;
        border: 1px solid #acacae;
        color: white;
        display: flex;
        align-items: center;
        /* justify-content: center; */
        font-size: 22px;
        padding-left: 5%;
        cursor: pointer;

    }

    .alertMarkContent{
        /* background-color: green; */
        width: 15%;
        height: 100%;
        display: flex;

        align-items: center;
        /* border-radius: 50px; */
    }

    .alertOption{
        width: 100%;
        height: 40%;
        display: flex;
        border-radius: 7px;
        border: 1px solid #acacae;
        color: white;
        display: flex;
        align-items: center;
        /* justify-content: center; */
        font-size: 22px;
        padding-left: 5%;
        cursor: pointer;
    }
    .listArea{
        background-color: black;
        width: 100%;
        height: 83%;
        display: flex;
        justify-content: center;
        align-items: center;
        /* border: 1px solid #acacae; */

    }
    .listContectSection{
        width: 97%;
        height: 100%;
        background-color: #282530;
        border-radius: 7px;
        border: 1px solid #acacae38;
    }

    .navArea{
        background-color: black;
        width: 100%;
        height: 7%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .navContentSection{
        width: 97%;
        height: 70%;
        background-color: #282530;
        border-radius: 7px;
        border: 1px solid #acacae38;

    }

 

    .skeletArea{
        background-color: black;
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
        color: white;
        display: flex;
        align-items: center;
        padding-left: 1%;
        font-size: 32px;
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