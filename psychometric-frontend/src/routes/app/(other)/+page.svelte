


<script>

    import axios from 'axios';
    
    var host= '';
    let questions = [
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

	let selected1=questions[0],selected2=questions[1],selected3=questions[2],selected4=questions[3],selected5=questions[4],assessmentBeingCreated = false, assessmentCreated = false;

    var assessmentName,assessmentLink,assessmentID;



    function createAssessment() {

        assessmentBeingCreated = true;
        assessmentName = document.getElementById('assessmentName').value;
        let choosenTraits = [selected1.id,selected2.id,selected3.id,selected4.id,selected5.id];

        
        
        
        // Calling backend API for creating assessment
        let dataBackend = {
            'assessmentName' : assessmentName,
            'choosenTraits' : choosenTraits
        };

        let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            data: dataBackend,
        }

		
        
        let url = '/psychometric/create-assessment';

        if (typeof window !== "undefined") {
              host = window.location.host
              if(host == 'localhost:5173'){
                url='http://127.0.0.1:5000' + url;
              }
              else {
                url = 'https://psychometric-backend-aw54llemya-uc.a.run.app' + url;
              }
            }

        
        
        
        const quesdata = axios(url,options)
                        .then((response) => {
                            assessmentID = response['data']['assessmentID'];
                            
                            
                            //assessmentLink = window.location.protocol + '//' + window.location.hostname + '/assessment/' + assessmentID;
                            assessmentLink = window.location.origin + '/app/' + 'assessment/' + assessmentID;
                            assessmentCreated = true;
                        })
                        .catch(() => {
                           console.log('Server either not connected or did not responded properly')
                        });
      
    }



    function createAnotherAssessment() {
        assessmentCreated = false;
        assessmentBeingCreated = false;
    }

</script>


<html lang="en">
    <body>
        <div class="container">
            <div class="card c1">
                <div class="card-header">
                    <h2 class="h2 center">
                        Psychometric assessment
                    </h2>
                </div>
                <div class="card-body">
                    
                        <ul>
                            <li>Give a name for your assessment</li>
                            <li>Choose psychometric traits from below dropdown</li>
                            <li>Click on create assessment button</li>
                            <li>Get the link of assessment and send it to candidates for attempting it.</li>
                        </ul>
                    
                </div>

            {#if !assessmentBeingCreated}
            <form class="form-group" on:submit|preventDefault={createAssessment}>



                <div class="card c2">
                    <div class="card-header">
                        <h2 class="h2 center">
                            Name your assessment 
                        </h2>
                    </div>
                    <div class="card-body center">

                        <div class="form-group">
                            
                            <input required type="text" class="form-control" id="assessmentName"  placeholder="Name of your assessment" title="Please enter name of the assessment">
                            
                          </div>


                    </div>
                </div>



                <div class="card c2">
                    <div class="card-header">
                        <h2 class="h2 center">
                            Choose Psychometric Traits 
                        </h2>
                    </div>
                    <div class="card-body center">
                            
                            <select class="btn btn-secondary dropdown-toggle" bind:value={selected1}>
                                {#each questions as question}
                                    <option value={question}>
                                        {question.text}
                                    </option>
                                {/each}
                            </select>
                            <br><br>
                            <select class="btn btn-secondary dropdown-toggle" bind:value={selected2}>
                                {#each questions as question}
                                    <option value={question}>
                                        {question.text}
                                    </option>
                                {/each}
                            </select>
                            <br><br>
                            <select class="btn btn-secondary dropdown-toggle" bind:value={selected3}>
                                {#each questions as question}
                                    <option value={question}>
                                        {question.text}
                                    </option>
                                {/each}
                            </select>
                            <br><br>
                            <select class="btn btn-secondary dropdown-toggle" bind:value={selected4}>
                                {#each questions as question}
                                    <option value={question}>
                                        {question.text}
                                    </option>
                                {/each}
                            </select>
                            <br><br>
                            <select class="btn btn-secondary dropdown-toggle" bind:value={selected5}>
                                {#each questions as question}
                                    <option value={question}>
                                        {question.text}
                                    </option>
                                {/each}
                            </select>
                            <br>
                            <br>
                            <button  type=submit class="btn btn-primary">
                                Create Assessment
                            </button>

                        
                        
                    </div>
                </div>
            </form>
            {/if}

            {#if assessmentBeingCreated || assessmentCreated}
            <div class="card c2">
                <div class="card-header">
                    <h2 class="h2 center">
                        
                    </h2>
                    <button class="btn btn-primary" style="float: right;" on:click={createAnotherAssessment}>Create another assessment</button>
                </div>
                <div class="card-body center">

                    {#if assessmentBeingCreated}
                    <div class="alert alert-warning alert-dismissible fade show" role="alert">
                        <strong>Please wait,</strong> your assessment is being created .. ... .....
                    
                    <button type="button" class="close" disabled={!assessmentCreated} data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    </div>
                    {/if}

                    {#if assessmentCreated}

                      <div class="alert alert-warning alert-dismissible fade show" role="alert">
                        Your assessment is successfully created
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>

                    <h4 class="h4">You can find the link of the assessment below</h4>
                    <div class="alert alert-primary" role="alert">
                        <a href={assessmentLink} target="_blank" rel="noreferrer" class="alert-link">{assessmentLink}</a>
                    </div>
                    
                    {/if}

                </div>
            </div>
            {/if}


            </div>





            
        </div>
    </body>
</html>



<style>
    .container{
        margin-top: 5%;
        margin-bottom: 2%;
        max-width: 90%;
    }
    .c2 {
        margin: 5%;
    }
    .h2{
        text-align: center;
    }
    .center{
        text-align: center;
    }
</style>