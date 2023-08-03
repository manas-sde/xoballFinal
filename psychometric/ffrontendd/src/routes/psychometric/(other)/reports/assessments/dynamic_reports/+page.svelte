

    <svelte:head>
      <link rel="stylesheet" href="https://unpkg.com/placeholder-loading/dist/css/placeholder-loading.min.css">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
      <script type="text/javascript" src="https://xobinteam.xobin.com/static/assets/plugins/selectize/selectize.min.js" defer></script>
      <script type="text/javascript" src="https://xobinteam.xobin.com/static/dashboardv2/config.js"></script>
      <link rel="stylesheet" href="https://xobinteam.xobin.com/static/assets/css/pages.css">
      <link rel="stylesheet" href="https://xobinteam.xobin.com/static/assets/plugins/selectize/selectize.css" />
      <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.0/css/all.min.css" rel="stylesheet">
      <link rel="stylesheet" href="https://xobinteam.xobin.com/static/assets/plugins/flatpickr/flatpickr.min.css">
      <link href="https://xobinteam.xobin.com/static/assets/css/n_r_.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
      <link href="https://xobinteam.xobin.com/static/assets/css/skeleton.css" rel="stylesheet" type="text/css" />
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js"></script>
      <script crossorigin="anonymous" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js"></script>
      <script crossorigin="anonymous" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/js/toastr.min.js"></script>
      <script src="https://xobinteam.xobin.com/static/xobin-challenges/jquery.twbsPagination.js"></script>
      <script src="https://xobinteam.xobin.com/static/dashboardv2/candidates/candidate_details_controller.js" defer></script>
      <script type="text/javascript" src="https://xobinteam.xobin.com/static/assets/plugins/flatpickr/flatpickr.js" defer></script>
      <link
        href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap"
        rel="stylesheet">
        <script src="https://code.jquery.com/jquery-3.4.1.min.js">  </script>
        <script type="text/javascript" src="https://xobinteam.xobin.com/static/angular/angular182.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular-route/1.8.3/angular-route.min.js"
          integrity="sha512-y1qD3hz/IAf8W4+/UMLZ+CN6LIoUGi7srWJ3r1R17Hid8x0yXe+1B5ZelkaL1Mjzedzu0Cg3HBvDG02SAgSzBw=="
          crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/twbs-pagination/1.4.2/jquery.twbsPagination.js"></script>
      <style media="screen">
        :root {
          --main-bg-color: #0056FF;
          --main-bg-color-rgb: 0, 86, 255;
          --box-bg-color: #f6f6f6;
          --secondary-font-color: #565656;
          --bs-body-font-family: "Open Sans", sans-serif !important;
          --plyr-video-background: transparent !important;
        }
    
        html,
        body {
          font-family: 'Open Sans', sans-serif;
          letter-spacing: 0.03em;
        }
    
        .page-item.active>.page-link:hover {
          color: white !important;
        }
    
        .btn-transparent {
          color: grey !important;
        }
    
        .candidate-offcanvas-btn {
          text-decoration: none !important;
        }
    
        .candidate-offcanvas-btn:hover {
          text-decoration: underline !important;
        }
    
        .dimgrey {
          margin: 0 20px;
        }
    
        .border {
          border-color: #efefef !important;
        }
    
        .txtarea {
          width: 85%;
          height: 140px;
          box-shadow: -1px 0px 5px 0px rgba(0, 0, 0, 0.15);
          border: none;
          margin-left: 47px;
          padding-top: 15px;
          padding-left: 12px;
          resize: none;
        }
    
        .messaging-widget {
          margin-top: 0 !important;
          width: 100% !important;
        }
    
        #message {
          width: 800px !important;
          left: calc(100% - 800px) !important;
          z-index: 1055 !important;
        }
    
        .row_p>.ms-2>* {
          padding: 3px 0;
        }
    
        .s_tb_tags {
          padding: 3px;
          font-weight: 500;
        }
    
        .s_blue {
          background-color: #fafcff;
        }
    
        #show-question-overlay {
          position: fixed;
          display: none;
          width: 100%;
          height: 100%;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: rgba(0, 0, 0, 0.5);
          z-index: 5;
          cursor: pointer;
        }
    
        .s_red {
          background-color: var(--main-bg-color-light);
          color: #585858;
        }
    
        .s_qual {
          background-color: var(--main-bg-color);
          color: #fafcff;
        }
    
        .acts {
          font-size: 16px !important;
        }
    
        .testfont2 {
          font-size: 19px !important;
    
        }
    
        .lw {
          color: #28a745 !important;
        }
    
        .s_blue_yellow {
          background-color: #ffc1071a !important;
        }
    
        .s_tb_tags2 {
          margin-bottom: .7vh !important;
        }
    
        .s_blue_green {
          background-color: #28a7452e !important;
        }
    
        .far:hover {
          color: #DE4040;
        }
    
        .color_heart {
          color: #DE4040;
        }
    
        .kkj {
          font-size: 1.5em;
          cursor: pointer;
    
        }
    
        .btn.btn-fav {
          font-size: 20px;
          transition: transform 0.2s;
        }
    
        .btn.btn-fav:hover {
          transform: scale(1.2);
        }
    
        .btn.btn-fav:hover .far {
          color: #DE4040;
        }
    
        .hidden {
          display: none !important;
        }
    
        .extra_p {
          padding-bottom: 2em;
        }
    
        .ro {
          color: grey;
        }
    
        .page-item.active .page-link {
          background-color: var(--main-bg-color);
        }
    
        
    
        button.nav-link {
          color: #bdbdbd;
          font-family: 'Lato', sans-serif;
        }
    
        div.nav-tabs {
          border-bottom: none;
          margin-bottom: 1rem;
          font-size: 16px;
        }
    
        div.nav-tabs button.nav-link {
          background: white;
          font-size: 18px;
          font-weight: 700;
          cursor: pointer;
        }
    
        div.nav-tabs button.nav-link:hover {
          color: var(--secondary-font-color);
          border-color: #fff #fff #fff;
        }
    
        div.nav-tabs button.nav-link.active {
          color: #3c403d;
          background-color: #fff;
          border-color: transparent;
          border-bottom: 4px solid var(--main-bg-color) !important;
        }
    
        div.nav-tabs button.nav-link.active:hover {
          border-color: #fff #fff var(--main-bg-color) !important;
        }
    
        .box_txt_head {
          font-family: "Open Sans", sans-serif;
          font-style: normal;
          font-weight: 700;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: 0.002em;
          /* Text/prime text colour */
          color: #3c403d;
        }
    
        .box_txt_name {
          /* number */
          font-family: "Open Sans", sans-serif;
          font-style: normal;
          font-weight: 500;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: 0.002em;
          margin-top: 5px;
          /* Text/secondary text colour */
          color: #858585;
        }
    
        .ri-icon {
          color: #858585;
          font-size: 18px;
        }
    
        span.fineprint-text {
          color: #bdbdbd;
          font-size: 16px;
          font-family: "Open Sans", sans-serif;
        }
    
        .datetime-selector.active {
          color: initial !important;
        }
    
        .form-control:disabled,
        .form-control[readonly] {
          background-color: initial !important;
        }
    
        .assessment-invite-details .messages-container {
          height: calc(100vh - 22rem) !important;
        }
    
        .no-results-message {
          width: 100%;
          height: 100%;
          font-size: 20px;
          font-weight: 700;
          font-family: 'Montserrat';
          color: #696969;
          display: flex;
          align-items: center;
          justify-content: center;
        }
    
        .i-loader {
          position: fixed;
          left: 0px;
          top: 0px;
          width: 100%;
          height: 100%;
          display: none;
          z-index: 9999999;
          backdrop-filter: blur(15px);
        }
    
        .loader-item-new {
          left: calc(50% - 30px);
          position: absolute;
          top: calc(50% - 30px);
        }
    
        .loader-new {
          width: 60px;
          height: 60px;
        }
    
        button.quick-info-nav {
          font-size: 10vmin;
          background-color: transparent;
          color: white;
          width: 80%;
          height: 100%;
          box-shadow: none !important;
          transition: color 0.2s linear;
        }
    
        .quick-info-nav:hover {
          color: #E0E0E0;
        }
    
        .thumb .btn {
          color: white !important;
        }
    
        .name_id {
          font-family: "Open Sans";
          font-style: normal;
          font-weight: 400;
          font-size: 14px;
          line-height: 19px;
          letter-spacing: 0.2px;
          color: #737373;
        }
    
        .seen-report {
          background-color: #fbfbfb;
        }
    
        .modal-lg {
          max-width: 900px;
        }
    
        .cfield-mulitmedia {
          object-fit: contain;
          width: 100%;
          border-radius: 16px;
          box-shadow: 0px 3px 16px rgb(0 0 0 / 15%);
        }
    
        .plyr__controls,
        .plyr__video-wrapper video,
        .plyr--video {
          border-radius: 16px !important;
        }
    
        .plyr__video-wrapper {
          box-shadow: 0px 3px 16px rgb(0 0 0 / 15%);
        }
      </style>
    </svelte:head>

    {#if !loading && allReportPage}   
    <body >
    
      <div id="show-question-overlay" ng-click="hideDetailedMenu()"></div>
      <div class="container-fluid h-100">
        <div class="row h-100">
          <div class="col-2 h-100 px-0 overflow-auto">
            <div class="trunc_btn dropdown w-100 border py-3">
              <a href="https://xobin.com/" class="logo"><img alt="Logo" src="https://xobinteam.xobin.com/static/assets/images/logo-nov.png"
                  style="width:70%;padding-top:1%;padding-left:20%" /></a>
    
    
            </div>
            <div class="trunc_btn dropdown w-100 border py-3">
              <div class="input-group rounded-0 border-right">
                <div class="input-group-prepend rounded-0 border-0 py-3">
                
                </div>
                
              </div>
    
            </div>
    
            <div class="">
              <div class="status border p-3">
               
                <div class="form-check">
                    <ul class="pagination" id=pagination style="margin-top: 1rem; width: 80%">
                        <li class="page-item first disabled"></li><li class="page-item prev disabled"><a href="#" class="page-link">Previous</a></li><li class="page-item active"><a href="#" class="page-link">1</a></li><li class="page-item next disabled"><a href="#" class="page-link">Next</a></li><li class="page-item last disabled"><a href="#" class="page-link">Last</a></li>
                      </ul>
                  
                </div>
                <div class="form-check">
                  
                </div>
    
    
    
              </div>
                        <div class="source border-right p-3">

              </div>
    
    
            </div>
            
          </div>
          <div class="col-10 h-100 px-0">
            <div class="border-bottom d-flex " style="padding: 1.3rem 1rem !important;">
              <div class="font-weight-bold">
    
              </div>
    
    
              <div class="td-1"></div>
    
              <div class="td-1"></div>
              
              
              
              </div>
            <div>
              <div class="font-weight-bold dimgrey p-3 d-flex align-items-center border-bottom">
                <div class="form-check" style="margin-left: 40%;">
    
                  <h4>Reports - {assessmentName}</h4>
                </div>
                
                
              </div>
            </div>
            {#each allReportsData as report}
              <div 
                class="font-weight-bold dimgrey p-3 d-flex align-items-center border-bottom row_p results">
    
                
                <div class="ms-2">
                    <div class="font-weight-bold l-1 row_n btn btn-link candidate-offcanvas-btn ng-binding">Candidate ID : {report.candID}</div>
                    <div class="light l-1 mb-2 ng-binding"></div>
                    <div class="holder_tags">
                      <div class="d-flex align-items-center">
                        <div class="sub_sec_tab_holder ">
                            

                                {#each Object.entries(report.scorePerTraits) as [traitname,score]}
                                    <span  class="s_tb_tags s_blue"> {traitname} - {score}</span>
                                {/each}
      
                        </div>
                      </div>
                    </div>
      
                  </div>
                <div class="text-center dimgrey font-weight-bold ms-auto td-2"><br /><span
                    class="progress-value acts"></span></div>
                
    
                <div class="td-1"></div>
    
                <div class="td-1"></div>

                
    
    
                <div class="td-1 kkj" ></div>
                <div class="td-1 kkj" ></div>
                <div class=""><button class="btn btn-secondary" on:click={getIndividualReport(report.scorePerTraits)}>View Full Report</div>
              </div>
              {/each}
              
             
            </div>
          </div>
        </div>
        
        
    
    
    </body>



{/if}



{#if loading}
<center><h3 style="vertical-align: center;">Please wait loading all reports .......</h3></center>
{/if}

{#if individualReportPage}
<Reports ndata={benchmarkScores} totalScore={individualReportData}/>
{/if}




    <script>
        import { goto } from '$app/navigation';
        import axios from 'axios';
        import Reports from '../../../Report.svelte'; 
    
        var allReportsData=[],benchmarkScores={},individualReportData,url,allReportPage=true,individualReportPage=false,loading=true;
        var assessmentID='',assessmentName='';
    
        url = '/psychometric/fetch-assessment-reports';
        //url = 'https://psycho-assess-tlp1-27ihzpqjy-omishra717-gmailcom.vercel.app/fetch-all-reports'
        //url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/fetch-all-reports'; 
    
    
        if (typeof window !== "undefined") {
                assessmentID = window.location.pathname.split('/')[4];
                console.log(assessmentID);
        }
    
        let options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                assessmentID:assessmentID, 
            }
    
        var apiResponse = axios.post(url,options)
                                .then((response) => {
                                    assessmentName = response.data['assessmentName']
                                    allReportsData = response.data['allReportsData'];
                                    benchmarkScores = response.data['benchmarkScores'];
    
                                    console.log('All reports Data : ',allReportsData);
                                    console.log('Benchmark Scores : ',benchmarkScores);
                                    loading=false;
    
                                })
                                .catch((error) => {
                                    console.log('Some error occured while connectng with backend. Please contact administrator.');
                                });
    
    
    
    
        
        function getIndividualReport(candScores){
            //console.log('Candidate ID requested : ');
            individualReportData = candScores;
            
            //goto("/individual-report",individualReportData);
            allReportPage = false;
            
            individualReportPage = true;
        }
    
    
        
    
    
    </script>
    
    


    