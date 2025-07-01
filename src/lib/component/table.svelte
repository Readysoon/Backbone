<script lang="ts" module>
     import * as ProductData from '../../../static/product.json'


   
//      $: if (optionStateOnArr) {
//     console.log('optionStateOnArr updated:', optionStateOnArr);
//     // You can also trigger filtering or other logic here
//   }
         

</script>

 <script lang="ts">
      let {selectedOptionState} = $props()

      console.log('selectedOptionState', selectedOptionState);
 </script>
<!-- <script lang="ts">


     
     $effect(() => {
      if(optionStateOnArr){
            console.log('clicked');
      }
     })
</script> -->

<main>
     
      {#if ProductData}
      {#each ProductData.productHeader as itemHead (itemHead)}

            <div class="productHeadSection">
                  <div class="boxId">
                        {itemHead.IdHead}
                  </div>
                  <div class="boxName">
                        {itemHead.NameHead}
                  </div>
                  <div class="boxBestand">
                        {itemHead.StockHead}
                  </div>
                  <div class="boxStatus">
                        {itemHead.StatusHead}
                  </div>
                  
                  
                   
            </div>

            <div class="productContentSection">

                 
                  {#each ProductData.productContent as itemContent (itemContent)}


                
                  {#if selectedOptionState && itemContent.productzustand == selectedOptionState}
                  <div class="boxContentObj">

                        <div class="contentId">
                              {itemContent.Id}
                        </div>
                       

                        <div class="contentName">
                              {itemContent.name}
                        </div>

                        <div class="contentBestand">
                              {itemContent.stock}
                        </div>

                        <div class="contentStatus">
                              <!-- {itemContent.stock} -->
                              <div class="backBar">
                                    <div class="loadBar"
                                    style="
                                    background-color: { itemContent.status <= 25 ? "red" :  itemContent.status <= 50 ? "orange" : "green"};
                                    width:  { itemContent.status &&  `${itemContent.status}%`};
                                    "

                                    >

                                    </div>
                              </div>
                        </div>

                  </div>
                 
                 {:else if selectedOptionState == "Gesamt"}
                 
                 <div class="boxContentObj">

                  <div class="contentId">
                        {itemContent.Id}
                  </div>
                 

                  <div class="contentName">
                        {itemContent.name}
                  </div>

                  <div class="contentBestand">
                        {itemContent.stock}
                  </div>

                  <div class="contentStatus">
                        <!-- {itemContent.stock} -->
                        <div class="backBar">
                              <div class="loadBar"
                              style="
                              background-color: { itemContent.status <= 25 ? "red" :  itemContent.status <= 50 ? "orange" : "green"};
                              width:  { itemContent.status &&  `${itemContent.status}%`};
                              "

                              >

                              </div>
                        </div>
                  </div>

            </div>
                  {/if}
            
                  {/each}
            </div>
            
      {/each}
      {/if}
</main>

<style>
      main{
            height: 100%;
            width: 100%;        
      }

      .productHeadSection{
            background-color: rgb(30, 31, 30);
            height: 5%;
            width: 100%;
            border-bottom: 1px solid rgba(255, 255, 255, 0.397);;
            display: flex;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            

      }

      .productContentSection{
            height: 95%;
            width: 100%;
            gap: 3.5%;
            display: flex;
            flex-direction: column;
            padding-top: 2%;
            overflow: auto;
            /* Scrollbar Styling */
            scrollbar-width: thin;
            scrollbar-color: #444 #232323;
      }

      .productContentSection::-webkit-scrollbar {
            width: 10px;
            background: #232323;
            border-radius: 8px;
      }
      .productContentSection::-webkit-scrollbar-thumb {
            background: linear-gradient(120deg, #444 40%, #2369f6dd 100%);
            border-radius: 8px;
            min-height: 40px;
            transition: background 0.3s;
      }
      .productContentSection::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(120deg, #2369f6dd 40%, #444 100%);
      }
      .productContentSection::-webkit-scrollbar-corner {
            background: #232323;
      }

      .boxId{
            width: 7%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px;
      }

      .boxName{
            width: 39.4%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px;
      }


      .boxBestand{
            width: 23%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px;
      }

     
      .boxStatus{
            /* background-color: pink; */
            width: 30%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            /* border-right: 1px solid rgba(255, 255, 255, 0.397); */
            color: white;
            font-size: 19px;
      }


      .boxContentObj{
            width: 100%;
            height: 60px;
            min-height: 53px;
            background-color: #f8f9f91d;
            display: flex;
            /* justify-content: center; */
            align-items: center;
            /* border-right: 1px solid rgba(255, 255, 255, 0.397); */
            color: white;
            font-size: 19px;
            border-top: 1px solid  rgba(255, 255, 255, 0.397);
            border-bottom: 1px solid  rgba(255, 255, 255, 0.397);
      }

      .boxContentObj:hover{
        background-color: #2369f652;
        border: 2px solid #004cff8f;
        cursor: pointer;

      }


      .contentId{
            width: 7%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px;
      }

      
      .contentName{
            width: 40%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px;
      }

      .contentBestand{
            width: 23%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-right: 1px solid rgba(255, 255, 255, 0.397);
            color: white;
            font-size: 19px; 
      }

      
      .contentStatus{
            width: 30%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            /* border-right: 1px solid rgba(255, 255, 255, 0.397); */
            color: white;
            font-size: 19px;
      }

      .backBar{
        background: rgb(178, 177, 177);
        width: 70%;
        height: 25%;
        border-radius: 50px;

      }

      .loadBar{
        background: rgb(243, 20, 20);
        width: 70%;
        height: 100%;
        border-radius: 50px;
      }
</style>