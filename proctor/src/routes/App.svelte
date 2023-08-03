<script>
    import { onMount } from "svelte";
    import {videoData} from './stores.js';

    import DisplayVideoPage from "./DisplayVideoPage.svelte";

    let componentRef;

    let offTabCount = 0;
    let recordingResumed = false;
    let offTabDurationThrehold=3000;
    var timestamps = [];
    var startTime=0,endTime=0;
    let globalStartTime=0;
    // console.log('cedsfcers',globalStartTime);
    // export let manuallyEnded;

    let currentOffTabDuration=0;
    let totalOffTabDuration = 0;

    export let submit = () => {};

    export let recorder;
    let displayVideoPage = false;


    onMount(() => {
        // recorder.resumeRecording();
        // componentRef.focus();
        window.addEventListener('blur', handleWindowBlur);
        window.addEventListener('focus', handleWindowFocus);

        

        // document.addEventListener('visibilitychange',visibilityChanged);
    });

    

    function visibilityChanged() {
        if (document.hidden){
            recorder.resumeRecording();

            offTabCount+=1
        }

        else {
            recorder.pauseRecording();
        }
    }

    async function handleWindowBlur (){
        startTime = Date.now();

        currentOffTabDuration = Date.now();

        offTabCount+=1;
        
        // console.log('Off tab activity found, resuming recording..');


        recorder.resumeRecording();
        if (offTabCount==10){
            alert('You have reached the maximum bound of unusual activity. Your test have to be forcefully submitted now.')
            return submitTest();
        }
        // console.log('Offtab for more than 3 seconds')
        // recordingResumed = true;
    
    }

    function handleWindowFocus() {
        

        if (currentOffTabDuration>0){
            totalOffTabDuration=totalOffTabDuration + (Date.now()-currentOffTabDuration);
        }
        currentOffTabDuration = 0;

        recorder.pauseRecording();
        // console.log(offTabCount);
        if (offTabCount>0) {
            let gST = endTime;
            let tpause = Date.now();
            // console.log('******00');
            // console.log(gST,tpause,startTime);
            // console.log(Math.round((tpause-startTime)/1000));
            endTime = gST+Math.round((tpause-startTime)/1000);
            // console.log('******11');

       
            videoData.push({
                'startTime' : gST,
                'endTime' : endTime
            });

        }
       
        


        if (totalOffTabDuration>60000 && offTabCount>1){
            alert('You have been inactive for more than a minute during the whole duration of test, your test will gets submitted now.');
            return submitTest();
        }
       
        
        
        //alert('Unwanted activity found. (' + offTabCount + '/5)');
    }

    async function submitTest() {
        // console.log(timestamps);
        //videoData = timestamps;
        window.removeEventListener('blur',handleWindowBlur);
        window.removeEventListener('focus',handleWindowFocus);
        let retfubc = await submit().then(()=> {
            console.log('56');
        });
        console.log('55');
        
        // displayVideoPage=true;
    }

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    
    
</script>


{#if displayVideoPage}

<DisplayVideoPage/>
{:else}

<center>
<div class="grid-container">
    <div class="grid-item">
        <p>
            <b>Functionalities implemented - <br></b>
        <ul>
            <li>
                Ask candidate to share their screen, before starting the test.
            </li>
            <li>
                If candidate share a single tab or single window, instead of sharing entire screen, they won't be able to proceed with the test.
            </li>
            <li>
                Offtab activity getting recorded along with count of offtab activity.
            </li>
            <li>
                Their screen gets recorded whenever they goes offtab.
            </li>
            <li>
                Their audio gets recorded whenever they goes offtab.
            </li>
            <li>
                If they are offtab for a total duration of more than a minute or approx 10 offtab count, whichever earlier, during the test, their tests will gets auto submitted.
            </li>
            <li>
                Able to view recording of every off tab activity separately on reports page.
            </li>
        </ul>
        
    </div>
    <div class="grid-item">
        <p>
          
            Type something below in order to check focus on assessment window and switch tab or windows in order to check off tab activity.
            <br>
            <textarea bind:this={componentRef}>
                
            </textarea>
        </p>
        <br>
    
        <div>Number of offtab activity detected : {offTabCount}</div>
        <div class="card-footer text-muted">
            <button on:click={()=>{submitTest()}} class="btn btn-primary">Submit Test</button>
        </div>
    
    </div>

</div>

</center>



<center >
    
   

</center>
{/if}


<style>

    .grid-container {
      display: grid;
      grid-template-columns: auto auto;
      background-color: whitesmoke;
      padding: 10px;
      margin:5%;
    }
    
    .grid-item {
      background-color: rgba(255, 255, 255, 0.8);
      border: 1px solid rgba(0, 0, 0, 0.8);
      padding: 20px;
      font-size: 24px;
      text-align: left;
    
    }
    
    </style>