<svelte:head>
    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    
</svelte:head>


<button class="exclude-from-print right-floated" on:click={generatePdf}>Download Report</button>
{#if reportLoading}
<div class="panel-disabled i-loader">
  <div class="animate__animated animate__zoomIn loader-item-new">
    <img
      src="https://xobinteam.xobin.com/wc/static/assets/images/new-loader.gif"
      alt="xobin_loader"
      class="loader-new"
    />
  </div>
  <h4
    id="atext"
    class="animate__animated animate__zoomIn text-center text-uppercase font-bold m-b-0"
  >
    Please Hold On...
  </h4>
</div>

{:else if reportNotFound} 

<div class="panel-disabled i-loader">
    <div class="animate__animated animate__zoomIn loader-item-new">
      <img src="https://xobinteam.xobin.com/wc/static/assets/images/error_gif.gif" alt="xobin_loader" class="loader-new">
    </div>
    <h4 id="atext" class="animate__animated animate__zoomIn text-center text-uppercase font-bold m-b-0"><b>Broken Link</b>: Please contact your recruiter to get a new link.</h4>
  </div>

{:else}        
<div class="report justify-content-center" style="height:max-content; margin:10%;">
    <div class="page1">
        <footer>
        <div class="pdf-nav" style="background-color: #929192;">
            <img src="/xobin.png" width="10%" class="company-logo left-floated" alt="CompanyName">
            <span class="nav-head right-floated"> <h3 class="font-weight-bold"> Sample Report </h3><span>Assessment : Leadership</span>
        </div>
    </footer>

        <div class="report-body">
            <div class="report-header left-floated">
                <span><h3> Sample Report </h3></span>
                
                <span> <h4> Assessment: Leadership </h4></span>
                
                <span> Assessment Answered On: 20/03/2018 </span>
            </div>

            <div class="report-result right-floated">
                <table class="larger-text table">
                    <tr>
                        <td class="bg-dark text-white">
                            <b>Aggregate Score</b>
                        </td>
                        <td class="bg-secondary">
                            Average (Low)
                        </td>
                    </tr>
                    
                    <tr>
                        <td class="bg-dark text-white">
                            <b>Score Rating</b>
                        </td>
                        <td class="bg-success">
                            AMBER
                        </td>
                    </tr>
                </table>
            </div>

            <div class="report-overview">
                <div class="table-div">
                <table class="table table-striped">
                    <thead>
                        <th class="table-header table-column" style="color:orange">
                            Overview of Competencies / Value Measured
                        </th>
                        <th>
                            <div class="scale" style="margin-top: 0%;">
                                <div class="dot" data-label="Bad"></div>
                                <div class="dot" data-label="Average"></div>
                                <div class="dot" data-label="Good"></div>
                                <div class="dot" data-label="Excellent"></div>
                                <div class="line"></div>
                                <div class="label"></div>
                            </div>
                        </th>
                    </thead>
                    <tbody>
                        

                    <tr>
                            <td class="table-column">
                                Strategic Agility
                            </td>
                            

                            <td>
                                <div class="scale">
                                    <span class="dot" data-label="Bad"></span>
                                    <span class="dot" data-label="Average"></span>
                                    <span class="dot active" data-label="Good"></span>
                                    <span class="dot" data-label="Excellent"></span>
                                    <div class="line"></div>
                                </div>
                                
                            </td>
                        </tr>


                        <tr>
                            <td class="table-column">
                                Stakeholder Management
                            </td>
                            

                            <td>
                                <div class="scale">
                                    <span class="dot active" data-label="Bad"></span>
                                    <span class="dot" data-label="Average"></span>
                                    <span class="dot" data-label="Good"></span>
                                    <span class="dot" data-label="Excellent"></span>
                                    <div class="line"></div>
                                </div>
                                
                            </td>
                        </tr>



                        <tr>
                            <td class="table-column">
                                Execution Agility
                            </td>
                            

                            <td>
                                <div class="scale">
                                    <span class="dot" data-label="Bad"></span>
                                    <span class="dot" data-label="Average"></span>
                                    <span class="dot active" data-label="Good"></span>
                                    <span class="dot active" data-label="Excellent"></span>
                                    <div class="line"></div>
                                </div>
                                
                            </td>
                        </tr>




                        <tr>
                            <td class="table-column">
                                Collaberation and Influencing
                            </td>
                            

                            <td>
                                <div class="scale">
                                    <span class="dot" data-label="Bad"></span>
                                    <span class="dot active" data-label="Average"></span>
                                    <span class="dot active" data-label="Good"></span>
                                    <span class="dot" data-label="Excellent"></span>
                                    <div class="line"></div>
                                </div>
                                
                            </td>
                        </tr>




                    
                        


                        

                    
                    </tbody>
                </table>
            
            
                
                </div>
            </div>

        </div>
        </div>



        



        <div class="page3 report-body">

            <span> 
                <span style="color:blueviolet; "> <h4>Score of Factors measured under different Competencies / Values </h4></span> &nbsp; 
                <span style="color:#929192"> <img class="icon" width="40" height="10" src="/expectedScore.png" alt="Expected Score icon"> Expected Score </span> &nbsp; &nbsp;
                <span style="color:#929192"> <img class="icon" width="30" src="/favourable_icon.png" alt="favourable icon"> Favourable </span> &nbsp; &nbsp;
                <span style="color:#929192"> <img class="icon" width="30" src="/LessFavourable_icon.png" alt="LessFavourable icon"> <u> Less Favourable </u></span> 
            </span>

            <div class="detail-comment">

                <div class="comment-header">
                    <div class="left-floated" style="height:13%;background-color: #929192; color:white">&nbsp;&nbsp; Strategic Agility &nbsp;&nbsp;</div>
                    <div class="right-floated" style="height:13%; background-color: #929192; color:white">&nbsp;&nbsp; Average (High) &nbsp;&nbsp;</div>
                </div>
                <br>

                <div class="trait-comment">
                    <div class="trait-name">
                        <div style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);">
                              <svg style="color: red;position:relative; top:-8px; left: 20%"  xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0  16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                            <span style="position:relative; top:-30px; left:5%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;">Average</span>                              
                        </div>
                        <img class="icon" width="20" src="/LessFavourable_icon.png" alt="LessFavourable icon">
                        <span><b>Strategic Outlook</b></span>
                        
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        Less likely to think of the future in terms of making and carrying out plans of action, might not always be prepared for foreseeable difficulties in tasks, can
                        formulate simplistic strategies to achieve attainable goals, less likely to be able to pinpoint implications of a decision
                    </p>
                </div>


                <div class="trait-comment">
                    <div class="trait-name">
                        <div style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);">
                            <svg style="color: red;position:relative; top:-8px; left: 20%"  xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0  16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                          <span style="position:relative; top:-30px; left:5%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;">Average</span>                              
                      </div>
                        <img class="icon" width="20" src="/LessFavourable_icon.png" alt="LessFavourable icon">
                        <b>Decision Making</b>
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        Might require a second opinion before making any decision, less likely to consider all available information before making a choice, may require more time to
                        zero down on a conclusion
                    </p>
                </div>


                <div class="trait-comment">
                    <div class="trait-name">
                        <div style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);">
                            <svg style="color: red;position:relative; top:-8px; left: 10%"  xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0  16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                          <span style="position:relative; top:-30px; left:0%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;">Poor</span>                              
                      </div>
                        <img class="icon" width="20" src="/LessFavourable_icon.png" alt="LessFavourable icon">
                        <b>Planning and Prioritization</b>
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        Tends to plan and organize tasks selectively; sometimes sets priorities for tasks according to their relative importance; may need a push to sort piled up tasks;
                        occasionally needs to take further efforts to systematize his/her work efficiently
                    </p>
                </div>



                <div class="trait-comment">
                    <div class="trait-name">
                        <div style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);">
                            <svg style="color: red;position:relative; top:-8px; left: 40%"  xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0  16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                          <span style="position:relative; top:-30px; left:25%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;">Average</span>                              
                      </div>
                        <img class="icon" width="20" src="/favourable_icon.png" alt="Favourable icon">
                        <b>Adaptability</b>
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        Often open to change; often flexible at work; may occasionally take time to get accustomed to changes; less likely to be uncomfortable with change
                    </p>
                </div>



                <div class="trait-comment">
                    <div class="trait-name">
                        <div style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);">
                            <svg style="color: red;position:relative; top:-8px; left: 60%"  xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0  16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                          <span style="position:relative; top:-30px; left:45%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;">Excellent</span>                              
                      </div>
                        <img class="icon" width="20" src="/LessFavourable_icon.png" alt="LessFavourable icon">
                        <b>Navigation Ambiguity</b>
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        Prefers to have a method/ structure in place for every task, less inclined towards working with vague information or absence of instructions, can find it
                        challenging to take risks in uncertain situations, might require assistance to draw the most meaning out of ambiguity
                    </p>
                </div>


                
            
            </div>
            <br><br><br>
            <!-- <div class="" style="float:right;">
                <div class="" style="position: relative;height: 20px;background-color: #4CAF50; border-color:black">
                    <div class="progress" style="position: absolute;top: 0;left: 0;height: 100%;background-color: white;width: 80%; /* Change this to set the progress percentage */"></div>
                    <div class="" style="position: absolute;top: -5px; /* Half the dot height */left: 40%; /* Change this to set the dot position */ width: 20px;height: 20px;">
                    <svg style="color: red" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                    </div>
                    <div class="text" style="position: absolute; top: -40px;left: 40%; /* Change this to set the text position */text-align: center;font-weight: bold;color: #4CAF50;font-size: 14px;z-index: 1;">Good</div>
                </div>
            </div> -->
        </div> 



    </div>

{/if}





<script>
    import html2canvas from 'html2canvas';
    import jsPDF from 'jspdf';
    import { onMount } from 'svelte';
    import axios from 'axios';

    export let data;

    var element,canvas,imgData,imgProps,pdfWidth=215,pdfHeight=180;

    var reportID,host,url,reportData;
    var reportLoading=true,reportNotFound=false;
    

    onMount( () => {
    async function loaded () {

        reportID = data.slug;

        url = '/psychometric/get-candidate-report';
        //console.log('I am here');
        if (typeof window !== "undefined") {
              host = window.location.host;
              if(host == 'localhost:5173'){
                url='http://127.0.0.1:5000' + url;
              }
              else {
                url = 'https://psychometric-backend-aw54llemya-uc.a.run.app' + url;
              }
        }


        let options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                reportID:reportID, 
            }
    
        var apiResponse = axios.post(url,options)
                                .then((response) => {
                                    reportData = response.data;
                                    reportLoading=false;
                                    reportNotFound=false;
                                })
                                .catch((error) => {
                                    reportLoading=false;
                                    reportNotFound=true;
                                    console.log('Some error occured while connectng with backend. Please contact administrator.');
                                });
    
        

        element = document.getElementsByClassName('page2')[0];
        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        canvas = await html2canvas(element, { scale: 1 });

        document.getElementsByClassName('page2')[0].innerHTML = "<img src='" + canvas.toDataURL() + "' style='width:100%;'>";

        
    }
    
    loaded();
    });
    const generatePdf = async () => {
        const pdf = new jsPDF();
        

        element = document.getElementsByClassName('page1')[0];

        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        imgProps = pdf.getImageProperties(imgData);
        //pdfWidth = pdf.internal.pageSize.getWidth();
        //pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, 'PNG', 0, 0, 215, 175);
        pdf.addPage();


        var headerElement = document.getElementsByClassName('pdf-nav')[0];
        console.log(headerElement);
        canvas = await html2canvas(headerElement, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth,pdfHeight);
        
        element = document.getElementsByClassName('page2')[0];
        
        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, 'PNG', 8, 20, 195, 200);
        pdf.addPage();


        var headerElement = document.getElementsByClassName('pdf-nav')[0];
        console.log(headerElement);
        canvas = await html2canvas(headerElement, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth,pdfHeight);
        
        element = document.getElementsByClassName('page3')[0];
        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL('image/png');
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, 'PNG', 8, 20, 195, 200);
        

        pdf.save('my-pdf-document.pdf');
    };
  
    // function printScale (){

    //     const pdf = new jsPDF();
    //     const element = document.getElementsByClassName('report')[0];
    //     console.log(element);
    //     pdf.html(element);
    //     pdf.save('my-pdf-document.pdf');

    // //   html2canvas(document.querySelector(".report")).then(canvas => {
        
    // //     // var win = window.open();
    // //     // win.document.write("<img src='" + canvas.toDataURL() + "' style='width:100%;'>");
    // //     // win.print();
    // //     // win.close();

    // //     const pdf = new jsPDF('p', 'mm', 'a4');
    // //     const imgData = canvas.toDataURL('image/png');
    // //     pdf.addImage(imgData, 'PNG', 0, 0, 210, 170); // adjust width and height as necessary (x,y,width,height)
    // //     pdf.save('scale.pdf');
    // //  });

    // }
  </script>
 
 




<style>
 .hex .hex-content {
   position: absolute;
   top: 50%;
   left: 50%;

   transform: translate(-50%, -50%) rotate(90deg);

   color: white;
 }



.container {
  position: relative;
}

img.polygon-image {
  /* display: block; */
  /* margin: 2%; */
  margin-top:2%;
  width: 40%;
  height: auto;
  vertical-align: middle;
}

.text-overlay {
  position: relative;
  color:orange;
  text-align: center;
}






/* CSS styles for horozontal scales */
.scale {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 30px;
  width: 300px;
  margin: auto;
  margin-top: 5%;
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;

}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ccc;
  position: relative;
  z-index: 1;
  cursor: pointer;
}

.dot.active {
  width: 20px;
  height: 20px;
  background-color: #28a745;
}

.line {
  height: 5px;
  width: 100%;
  background-color: #ccc;
  position: absolute;
  top: 12px;
  left: 0;
  z-index: -1;
}

.dot:nth-of-type(1) {
  margin-left: 0;
}

.dot:last-of-type {
  margin-right: 0;
}

.dot.active:not(:last-of-type)::after {
  background-color: #28a745;
}

.label {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  width: 80px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.dot[data-label="Bad"]::before {
  content: "Bad";
  position: absolute;
  bottom: 20px;
  left: -10px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.dot[data-label="Average"]::before {
  content: "Average";
  position: absolute;
  bottom: 20px;
  left: -30px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.dot[data-label="Good"]::before {
  content: "Good";
  position: absolute;
  bottom: 20px;
  left: -20px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.dot[data-label="Excellent"]::before {
  content: "Excellent";
  position: absolute;
  bottom: 20px;
  left: -30px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.dot.active[data-label]::before {
  content: attr(data-label);
  position: absolute;
  top: -30px;
  left: -12px;
  font-size: 16px;
  font-weight: bold;
  color: #28a745;
}


@media print {

    @page {
  size: auto; /* Set the page size to auto */
  margin: 0; /* Set the margin to 0 */
}

.exclude-from-print {
    visibility: hidden;
  }

}


.value-measured-div{
    margin-top:1%;
    height:250px;
    /* width:100%; */
    border: 1px solid;
    align-items: center;
    text-align: center;
    vertical-align: middle;

}


.detail-comment{
    margin-top:1%;
    height:100%;
    /* width:100%; */
    border: 1px solid;
    /* align-items: center; */
    /* text-align: center; */
    /* vertical-align: middle; */

}

.trait-name{
    
    /* float: left; */
    text-decoration: solid;
    margin: 1%; 
    margin-top:3%;

}

    



    .pdf-nav{
        background-color: #929192;
        width:100%;
        max-width: 100%;
        height: 100px;
    }

    .company-logo{
        margin-left: 5%;
        margin-top: 0%;
    }

    .nav-head{
        color: #ffffff;
        margin-right: 5%;
        margin-top: 1%;
        vertical-align: auto;
    }

    .report-body{
        margin: 4%;
        /* background-color: #fffff1; */
        font-size:larger;
        
    }

    .left-floated{
        float: left;
    }

    .right-floated{
        float: right;
    } 

    .report-header{
        /* margin-left: 2%;
        margin-top:1%; */
    }

    .report-result{
        /* margin-top: 5%; */
        /* margin-right:2%; */
        font-stretch: expanded;
        width: 45%;
    }

    .larger-text{
        font-size: larger;
    }

    .report-overview{
        border: 1px dashed;
        border-color: #929192;
        /* display: flex; */
        display: inline-block;
        margin-top: 5%;
        width: 100%;
        /* outline-style:  dashed; */

        /* background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%23333' stroke-width='2' stroke-dasharray='6%2c 14' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e"); */
        

    }

    .table-div{
        margin:2%;
        /* text-align: center; */
    }

    .table{
        width: 100%;
        /* align-items: center; */
        
        
    }

    .table-header{
        height: 150px;
    }

    .table-column{
        vertical-align: middle;
    }



</style>


<!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->
    <!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->
    <!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->