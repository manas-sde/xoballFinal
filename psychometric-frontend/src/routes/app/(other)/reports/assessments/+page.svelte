


<script>

    import axios from 'axios';
    var host= '';

    let allTraits = [
		{ id: 1, text: 'Emotional Stability' },
		{ id: 2, text: 'Integrity' },
		{ id: 3, text: 'Perfectionism' },
        { id: 4, text: 'Openness' },
		{ id: 5, text: 'Reasoning' },
		{ id: 6, text: 'Rule Consciousness' },
        { id: 7, text: 'Team Work' },
		{ id: 8, text: 'Sensitivity' },
        { id: 9, text: 'Conflict Management' },
        { id: 10, text: 'Inclusion' }
        
		
	];

    var allAssessments = [];
   
        
    let url = '/psychometric/fetch-all-assessments';

    if (typeof window !== "undefined") {
              host = window.location.host
              if(host == 'localhost:5173'){
                url='http://127.0.0.1:5000' + url;
              }
              else {
                url = 'https://psychometric-backend-aw54llemya-uc.a.run.app' + url;
              }
            }


    const quesdata = axios.get(url)
                        .then((response) => {
                            allAssessments = response['data']
                            console.log(allAssessments); 
                        })
                        .catch((e) => {
                            console.log(e);
                            console.log('URL***:',url)
                           console.log('Server either not connected or did not responded properly')
                        });


    
    function getLink(id){
        return window.location.origin +'/app/assessment/'+id;
    }


    function getReport(id){
        return window.location.origin +'/app/reports/assessments/'+id;
    }


</script>


<div class="container">
    <br><br>
    {#each allAssessments as assessment}
    <div class="card mt-3 shadow">
        <div class="card-body">
            <div class="text-dark">
                <span style="font-size: large; font-weight:bold;">{assessment.assessmentName}</span>
                
                
        
                <ul style="float: right; margin-right:1%;">
                    {#each assessment.traits as trait}
                    <li>
                        {trait}
                    </li>
                    {/each}
                </ul>
                
            </div>
            <br><br>
            <!-- <p>
            <a type="button" href={getLink(assessment._id)} target="_blank" class="btn btn-secondary" style="text-decoration: none; float:left;"> Take aseessment</a>
            </p> -->
        </div>
        
            <a type="button" href={getReport(assessment._id)} target="_blank" class="btn btn-info" style="text-decoration: none;"> View Assessment Report</a>
        
    </div>
    {/each}
</div>


<style>

    .container{
        margin-bottom: 2%;
    }

</style>