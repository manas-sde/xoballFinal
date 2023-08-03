<svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</svelte:head>




<script>
    import Reports from '../../Reports.svelte';
    


    import axios from 'axios';


    var question,questionNo=0,lenResponses=0;
    var page1 = true,page2=false,page3=false,load1=false,load2=false;
    var responses = {};
    var reports = {};
    var allQuesData = {};
    var ndata = {};

	let questions = [
		{ id: 1, text: 'Emotional Stability' },
		{ id: 2, text: 'Integrity' },
		{ id: 3, text: 'Perfectionism' },
        { id: 4, text: 'Openness' },
		{ id: 5, text: 'Reasoning' },
		{ id: 6, text: 'Rule Consciousness' },
        { id: 7, text: 'Team Work' },
		{ id: 8, text: 'Sensitivity' }
		
	];

	let selected1=questions[0],selected2=questions[0],selected3=questions[0];

	let answer = '';

    var allData=[];

    var totalScore = {}; //totalScore per traits

   
    function submitTest() {
       // console.log('Assessment Submitted');
        load2=true;
        


        //console.log(responses);
        //console.log(reports);

        //var allTrait = Object.keys(reports);

        // for(let i=0;i<allTrait.length;i++){

        //     let trait_name1 = allTrait[i];

        //     let keysQues = Object.keys(reports[trait_name1]);
            

        //     for (let j=0;j<keysQues.length;j++){
        //         if(allTrait[i] in totalScore){
        //             totalScore[allTrait[i]] += reports[trait_name1][keysQues[j]];
        //         }
        //         else{
        //             totalScore[allTrait[i]]= reports[trait_name1][keysQues[j]];
        //         }
        //     }
        // }



        




        var dataBackend = {
            'responses' : responses,
            //'reports' : reports,
            //'totalScorePerTraits' : totalScore,
        }

       // console.log(dataBackend);
        //allData = [reports];


        let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            data: dataBackend,
        }

		//let url = 'https://psycho-assess-tlp1.vercel.app/post-responses';
        //let url = 'http://127.0.0.1:5000/post-responses';
        //let url = 'https://psycho-assess-tlp1-27ihzpqjy-omishra717-gmailcom.vercel.app/post-responses';
        

        let url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/post-responses'; //testing url
        
        
        const quesdata = axios(url,options)
                        .catch(() => {
                           console.log('Server either not connected or did not responded properly')
                        });
        

        
        quesdata.then( (response) => {
            //console.log(response['data']);
            allData = [response['data']['report']];
            totalScore = response['data']['totalScorePerTraits'];
            ndata = response['data']['allTraitScores'];
            //console.log(ndata);
            //console.log(totalScore);
            page2=false;
            page3 = true;
            load2 = false;
        });



        
        
    }

	function handleSubmit() {

        load1 = true;

        let traits = {'traits': [selected1.id,selected2.id,selected3.id]} ;
        let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            data: traits,
        }
		//let url = 'https://psycho-assess-tlp1.vercel.app/get-questions';  //main backend
        //let url = 'http://127.0.0.1:5000/get-questions';
        //let url = 'https://psycho-assess-tlp1-27ihzpqjy-omishra717-gmailcom.vercel.app/get-questions'; //for testing

        let url = 'https://psycho-assess-tlp1-git-test-omishra717-gmailcom.vercel.app/get-questions';  //for testing


        const quesdata = axios(url,options)           //api for the get request
        .then(response => {
                                //console.log(response['data']);
                                allQuesData = response['data'];
                                question = allQuesData[questionNo];
                                // question['options'][0].checked=false;
                                // question['options'][1].checked=false;
                                // question['options'][2].checked=false;
                                // question['options'][3].checked=false;
                          });

        
        quesdata.then( () => {
            //console.log(allQuesData);
            page1 = false;
            page2=true;
            load1=false;
        });
		
    }


    function navigatePrevQues() {
        questionNo -= 1;
        question = allQuesData[questionNo];
        // question['options'][0].checked=false;
        // question['options'][1].checked=false;
        // question['options'][2].checked=false;
        // question['options'][3].checked=false;
    }


    function navigateNexQues() {
        questionNo += 1;
        question = allQuesData[questionNo];
        // question['options'][0].checked=false;
        // question['options'][1].checked=false;
        // question['options'][2].checked=false;
        // question['options'][3].checked=false;
    }


    function onChangeRadio() {
        let allOp = document.getElementsByName(question['question_id']);

        var opSelected;
        let opp;

        for(let i=0;i<allOp.length;i++){
            
            if (allOp[i].checked){
                opSelected = allOp[i].value;
                //console.log('Option ',i+1,'matched',allOp[i].value);
                opp = question['options'][i]['option'];
                question['options'][i].checked = true;
                break;
            }
            
        }

        //console.log(opSelected);

       // console.log(question['question'],'*****',opp)
        


        responses[question['question_id']] = opSelected;

       // console.log(lenResponses);
        lenResponses = Object.keys(responses).length;
       // console.log(lenResponses);

        //Score in each question
        //var score_q = 0;

        // for (let op of question['options']){
        //     if (op['opID']==opSelected){
        //         score_q = op['opScore'];
        //         break;
        //     }
        // }

       // console.log('Score : ',score_q);

        
        // var trait_name = [questions[question['trait_id']-1].text];
        // if(trait_name in reports){
        //     reports[trait_name][question['question_id']]=score_q;
        // }
        // else{
        //     reports[trait_name]= {};
        //     reports[trait_name][question['question_id']]=score_q;
        // }


        
        




    }


    
</script>



{#if page1 || page3}

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    
  
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/view-reports">View all reports</a>
        </li>
        
      </ul>
     
    </div>
  </nav>



{/if}


{#if page1}
<center>

    <div class="container">
    <div class="card c1">
        <div class="card-header">
            <h3 class="h3">Choose Psychometric traits</h3>
        </div>
        <div class="card-body">
            

<form class="form-group" on:submit|preventDefault={handleSubmit}>
	<select class="btn btn-secondary dropdown-toggle" bind:value={selected1} on:change="{() => answer = ''}">
		{#each questions as question}
			<option value={question}>
				{question.text}
			</option>
		{/each}
	</select>
	<br><br>
	<select class="btn btn-secondary dropdown-toggle" bind:value={selected2} on:change="{() => answer = ''}">
		{#each questions as question}
			<option value={question}>
				{question.text}
			</option>
		{/each}
	</select>
	<br><br>
	<select class="btn btn-secondary dropdown-toggle" bind:value={selected3} on:change="{() => answer = ''}">
		{#each questions as question}
			<option value={question}>
				{question.text}
			</option>
		{/each}
	</select>
	<br>
	<br>
	<button  type=submit class="btn btn-primary">
		Take Assessment
	</button>

    {#if load1}
    <br><br><br><br><b>Please wait, Working on it.................</b>
    {/if}
</form>
        </div>
    </div>
</div>

</center>
{/if}


<!-- ------------Assessment Page--------------- -->

{#if page2}

<div class="container-fluid">

    <div class="jumbotron">
      <h3>Psychometric Assessment!</h3>
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



<!-- ------------Reports Page--------------- -->

{#if page3}
   <Reports totalScore={totalScore} allData={allData} ndata={ndata}/>
{/if}




<style>

    div.container{
        margin-top: 4%;
    }
	
    
</style>





