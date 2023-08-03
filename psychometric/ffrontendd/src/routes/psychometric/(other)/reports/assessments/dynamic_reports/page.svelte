

<script>
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import Reports from '../../../Reports.svelte'; 

    var allReportsData=[],benchmarkScores={},individualReportData,url,allReportPage=true,individualReportPage=false,loading=true;
    var assessmentID='',assessmentName='';

    url = '/fetch-assessment-reports';
    //url = 'https://psycho-assess-tlp1-27ihzpqjy-omishra717-gmailcom.vercel.app/fetch-all-reports'
    //url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/fetch-all-reports'; 


    if (typeof window !== "undefined") {
            assessmentID = window.location.pathname.split('/')[3];
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








{#if !loading && allReportPage}
<br><br><br>
<div class="container">



<div class="jumbotron">
    <h3>{assessmentName}</h3>
</div>

    
    <div class="card-header">
        <h3 class="h3">List of candidates along with their reports on psychometric assessment.</h3>
    </div>
    <div class="card-body">
        <table class="table table-striped table-hover">
            <thead>
              <tr>
                <th scope="col">Candidate ID</th>
                <th scope="col">Emotional Stability</th>
                <th scope="col">Integrity</th>
                <th scope="col">Perfectionism</th>
                <th scope="col">Openness</th>
                <th scope="col">Reasoning</th>
                <th scope="col">Rule Consciousness</th>
                <th scope="col">Team Work</th>
                <th scope="col">Sensitivity</th>
              </tr>
            </thead>
            <tbody>
            {#each allReportsData as report}
              <tr class="table-row" on:click={getIndividualReport(report.scorePerTraits)}>
                <th scope="row">{report.candID}</th>
                <td>{#if report.scorePerTraits['Emotional Stability'] != undefined }{report.scorePerTraits['Emotional Stability']} {/if} </td>
                <td>{#if report.scorePerTraits['Integrity'] != undefined }{report.scorePerTraits['Integrity']} {/if}</td>
                <td>{#if report.scorePerTraits['Perfectionism'] != undefined }{report.scorePerTraits['Perfectionism']} {/if}</td>
                <td>{#if report.scorePerTraits['Openness'] != undefined }{report.scorePerTraits['Openness']} {/if}</td>
                <td>{#if report.scorePerTraits['Reasoning'] != undefined }{report.scorePerTraits['Reasoning']} {/if}</td>
                <td>{#if report.scorePerTraits['Rule consciousness'] != undefined }{report.scorePerTraits['Rule consciousness']} {/if}</td>
                <td>{#if report.scorePerTraits['Team Work'] != undefined }{report.scorePerTraits['Team Work']} {/if}</td>
                <td>{#if report.scorePerTraits['Sensitivity'] != undefined }{report.scorePerTraits['Sensitivity']} {/if}</td>
              </tr>
            {/each}
          </table>
    </div>
</div>


{/if}



{#if loading}
<center><h3 style="vertical-align: center;">Please wait loading all reports .......</h3></center>
{/if}






{#if individualReportPage}
<Reports ndata={benchmarkScores} totalScore={individualReportData}/>
{/if}














<style>
    .table-row{
cursor:pointer;
}

</style>