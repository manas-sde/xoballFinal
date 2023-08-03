
<svelte:head>
    
    <title>{reportData["candidateName"]} - Report</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="shortcut icon" href="{reportData["companyLogo"]}" type="image/x-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400;500;600;700;900&family=Open+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <link rel="stylesheet" href="/psychometric-staticfiles/css/report.css">
    <link href="https://xobinteam.xobin.com/wc/static/assets/css/pagex.css" rel="stylesheet" type="text/css" />




</svelte:head>



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
            <img
                src="https://xobinteam.xobin.com/wc/static/assets/images/error_gif.gif"
                alt="xobin_loader"
                class="loader-new"
            />
        </div>
        <h4
            id="atext"
            class="animate__animated animate__zoomIn text-center text-uppercase font-bold m-b-0"
        >
            <b>Broken Link</b>: Report you are trying to get doesn't exist.
        </h4>
    </div>
{:else}

    <div class="overall-report">
        <ReportNav assessmentName={reportData["assessmentName"]}/>

        <CandidateInfo reportData={reportData}/>

        <TraitWiseReport allReportData={reportData["categoryWiseResult"]} />
    </div>

{/if}

<script>
    import { onMount } from "svelte";
    import axios from "axios";
    import ReportNav from "./ReportNav.svelte";
    import TraitWiseReport from "./TraitWiseReport.svelte";
    import CandidateInfo from "./CandidateInfo.svelte";

    export let data;

    var reportID, host, url, reportData={};
    var reportLoading = true, reportNotFound = false;

    var candidateName='';

    
    onMount(() => {
        async function loaded() {

            reportID = data.slug;

            url = "/psychometric/get-candidate-report";
            if (typeof window !== "undefined") {
                host = window.location.host;
                if (host == "localhost:5173") {
                    url = "http://127.0.0.1:5000" + url;
                } else {
                    url =
                        "https://psychometric-backend-aw54llemya-uc.a.run.app" +
                        url;
                }
            }

            let options = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                },
                reportID: reportID,
            };

            var apiResponse = axios
                .post(url, options)
                .then((response) => {
                    reportData = response.data;

                    var allCoreTraits=Object.keys(reportData["categoryWiseResult"]);
                    var categoryTraits;
                    for(let i=0;i<allCoreTraits.length;i++){
                        categoryTraits = reportData["categoryWiseResult"][allCoreTraits[i]]["categoryTraits"];
                        let categoryTraitNames = Object.keys(categoryTraits)
                        let lenCategoryTraits = Object.keys(categoryTraits).length;
                        for(let j=0;j<lenCategoryTraits;j++){
                            categoryTraits[categoryTraitNames[j]]["scorePercentage"] = ((categoryTraits[categoryTraitNames[j]]["traitObtainedScore"]*100) / categoryTraits[categoryTraitNames[j]]["traitTotalScore"]).toFixed(2);
                            
                            if (categoryTraits[categoryTraitNames[j]]["scorePercentage"] <=25){
                                categoryTraits[categoryTraitNames[j]]["scoreBucket"] = "Bad";
                            }

                            else if (categoryTraits[categoryTraitNames[j]]["scorePercentage"] <=50){
                                categoryTraits[categoryTraitNames[j]]["scoreBucket"] = "Average";
                            }

                            else if (categoryTraits[categoryTraitNames[j]]["scorePercentage"] <=75){
                                categoryTraits[categoryTraitNames[j]]["scoreBucket"] = "Good";
                            }

                            else {
                                categoryTraits[categoryTraitNames[j]]["scoreBucket"] = "Excellent";                            }
                            }

                        
                    }
                  
                    reportLoading = false;
                    reportNotFound = false;
                    // console.log(reportData);
                })
                .catch((error) => {
                    reportLoading = false;
                    reportNotFound = true;
                    console.log(
                        "Some error occured while connectng with backend. Please contact administrator."
                    );
                });
        }

        loaded();
    });

</script>