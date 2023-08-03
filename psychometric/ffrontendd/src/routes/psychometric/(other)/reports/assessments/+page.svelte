


<script>

    import axios from 'axios';

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
    //let url = 'https://psycho-assess-tlp1.vercel.app/fetch-all-assessments';
        
    let url = '/psychometric/fetch-all-assessments';

    //let url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/fetch-all-assessments'; //testing url


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
        return window.location.origin +'/psychometric/assessment/'+id;
    }


    function getReport(id){
        return window.location.origin +'/psychometric/reports/assessments/'+id;
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
                    {#each assessment.traits as traitID}
                    <li>
                        {allTraits[traitID-1].text}
                    </li>
                    {/each}
                </ul>
                
            </div>
            <br><br>
            <p>
            <a type="button" href={getLink(assessment._id)} target="_blank" class="btn btn-secondary" style="text-decoration: none; float:left;"> Take aseessment</a>
            </p>
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