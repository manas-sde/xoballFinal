
<svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</svelte:head>




<script>
        import axios from 'axios';
        //import Reports from '/src/routes/Reports.svelte';
        
        

        
    
        var assessmentLoading = false, assessmentLoaded = false, assessmentID='', assessmentNotFound = false, assessmentFound=true, assessmentName;
        
        var question,questionNo=0,lenResponses=0;
        var page2,page3,load2=false;
        var responses = {};
        var reports = {};
        var allQuesData = {};
        var ndata = {};
        var allData,totalScore;
    
        if (typeof window !== "undefined") {
            assessmentID = window.location.pathname.split('/')[2];
            console.log(assessmentID);
        }
    
    
    
    
        if (!assessmentID){
            assessmentNotFound = true;
            assessmentLoading = false;

        }

        

        function getAssessment() {


            assessmentLoading = true;

            let dataBackend = {
                'assessmentID' : assessmentID
            };

            let options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                data: dataBackend,
            }

            //let url = 'https://psycho-assess-tlp1.vercel.app/get-assessment';

            let url = '/psychometric/get-assessment';
            //let url = 'http://127.0.0.1:5000/get-assessment';

            //let url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/get-assessment'; //testing url


            const quesdata = axios(url,options)
                            .then((response) => {

                                assessmentName = response['data']['assessmentName'];
                                allQuesData = response['data']['questionData'];
                                question = allQuesData[questionNo];
                                
                                assessmentLoading = false;
                                assessmentLoaded = true;
                            })
                            .catch((e) => {
                            console.log('Server either not connected or did not responded properly');
                            assessmentNotFound = true;
                            assessmentLoading = false;
                            });

        }
        

        function navigatePrevQues() {
            questionNo -= 1;
            question = allQuesData[questionNo];
            
        }


        function navigateNexQues() {
            questionNo += 1;
            question = allQuesData[questionNo];
            
        }



        function onChangeRadio() {
            let allOp = document.getElementsByName(question['question_id']);

            var opSelected;
            let opp;

            for(let i=0;i<allOp.length;i++){
                
                if (allOp[i].checked){
                    opSelected = allOp[i].value;
                    
                    opp = question['options'][i]['option'];
                    question['options'][i].checked = true;
                    break;
                }
                
            }
       
            responses[question['question_id']] = opSelected;

            lenResponses = Object.keys(responses).length;
        }



        function submitTest() {`-`
        
                load2=true;
            
                var dataBackend = {
                    'responses' : responses,
                    'assessmentID' : assessmentID,
                }

                let options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json;charset=utf-8'
                    },
                    data: dataBackend,
                }

                //let url = 'https://psycho-assess-tlp1.vercel.app/post-responses';
                let url = '/psychometric/post-responses';
                //let url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/post-responses'; //testing url
                
                
                const quesdata = axios(url,options)
                                .catch(() => {
                                console.log('Server either not connected or did not responded properly')
                                });
                

                
                quesdata.then( (response) => {
                    //console.log(response['data']);
                    allData = [response['data']['report']];
                    totalScore = response['data']['totalScorePerTraits'];
                    ndata = response['data']['allTraitScores'];
                    
                    assessmentLoaded=false;
                    page3 = true;
                    load2 = false;
                });



                
                
            }



    




</script>


{#if !assessmentLoading && !assessmentLoaded && !page3 && !assessmentNotFound}


<div class="card center-page" style="width: 25rem; border:none">
    <div class="card-body">
    
    <button class="btn btn-primary" on:click={getAssessment}>Start Assessment</button>
    </div>
</div>


{/if}



{#if assessmentLoading}

        <div class="card center-page" style="width: 25rem;">
            <div class="card-body">
            <h5 class="card-title" style="text-align:center">Your assessment is being loaded</h5>
            <div class="spinner-grow center-page" style="width: 3rem; height: 3rem;" role="status">
        
            </div>
            </div>
        </div>

    


    
{/if}






        

    


    


 


{#if assessmentNotFound} 

        <div class="card center-page" style="width: 25rem;">
            <div class="card-body">
            <h5 class="card-title" style="text-align:center">Invalid Link! Assessment not found</h5>
            </div>
        </div>

{/if}



{#if assessmentLoaded}

        <div class="container-fluid">

            <div class="jumbotron">
            <h3>Psychometric Assessment!</h3>
            <h5>{assessmentName}</h5>
            <p></p>
            </div>


            <div class="progress">
                <div class="progress-bar" role="progressbar" style="width: {lenResponses*100/allQuesData.length}%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"> {lenResponses} / {allQuesData.length} completed</div>
            </div>
            
            <div class="card-body">
        
        <form class="form-group" on:submit|preventDefault={submitTest}>

            
            <div class="card border-info mb-4 ">
        
            <div class="d-flex justify-content-between align-items-center card-header bg-info text-white" id="h1">
                <span>Question {questionNo + 1}</span>
                
            </div>
            <div id="q1" class="collapse show" aria-labelledby="h1">
                <div class="card-body">
                <p>{question.question}</p>
                    
                {#each question.options as op }
                <div class="form-check">
                    <input class="form-check-input" type="radio" checked={op.checked} required name={question.question_id} value={op.opID} on:change={onChangeRadio}>
                    <label for={question.question_id} class="form-check-label">
                    {op.option}
                    </label>
                </div>
                {/each}
                
        
                </div>
        
            </div>
            </div>

            <div class="card-body">
        
            <button type="button" class="btn btn-primary" on:click={navigatePrevQues} disabled={questionNo==0}>
                Previous
            </button>

            

            <button type="button" class="btn btn-primary" on:click={navigateNexQues} disabled={questionNo==allQuesData.length-1}>
                Next
            </button>


            <button style="float:right"  type="submit" class="btn btn-primary"   disabled={(lenResponses !=allQuesData.length)}>
                Submit Test
            </button>

            </div>


        
        </form>
        </div>


        {#if load2}
        <div class="card-body">
            <h4 class="h4">Please wait, Submitting your assessment ..............</h4>
        </div>


        {/if}


        </div>

{/if}




<!-- ------------Assessment Submitted--------------- -->

{#if page3}
<div class="card center-page" style="width: 30rem;">
    <div class="card-body">
    <h5 class="card-title" style="text-align:center">Thanks for taking the assessment. <br><br>Your assessment is successfully submitted.</h5>
    </div>
</div>
{/if}







<style>
    .center-page{
        align-items: center;
        margin:auto;
        margin-top: 20%;
    }
</style>


