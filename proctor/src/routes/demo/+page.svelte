<script>
  // import App from "./App.svelte";

  import { onMount } from "svelte";

  import {videoURL,videoData} from './../stores.js';

  import DisplayVideoPage from "./../DisplayVideoPage.svelte";

  let permissionGranted=false;
  let stream,recorder,audioStream;
  let isDesktop;

  let manuallyEnded = false;
  let displayRes=false;

  let desktopView = false;

  let componentRef,chunks=[];


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

    let displayVideoPage = false;

  onMount(()=> {
      const userAgent = navigator.userAgent.toLowerCase();
      isDesktop = !/mobile|android|iphone|ipad|iemobile|wpdesktop/i.test(userAgent);
      // console.log(isDesktop);
      // console.log(userAgent);
      desktopView = isDesktop && isChrome;
      
  });



  async function isEntireScreenShared() {
      const videoTrack = stream.getVideoTracks()[0];
      videoTrack.addEventListener('ended', handleScreenSharingEnded);
      // console.log('Video Tracks',videoTrack);

      if (isFirefox) {

          const capabilities = videoTrack.getConstraints();
          // console.log('Capabilities',capabilities);
          // console.log(capabilities.displaySurface=='monitor');
          

          // Check if the "displaySurface" constraint is present and set to "monitor"
          if (capabilities.mediaSource && capabilities.mediaSource=='window') {
              // console.log('c1');
              return true;
          }
          return false;
      }


      const capabilities = videoTrack.getSettings();
      // console.log('Capabilities',capabilities);
      // console.log(capabilities.displaySurface=='monitor');
      

      // Check if the "displaySurface" constraint is present and set to "monitor"
      if (capabilities.displaySurface && capabilities.displaySurface=='monitor') {
          // console.log('c1');
          return true;
      }

      //it is not the entire screen
      return false;
  }


  async function shareFullScreen() {
          if (document.documentElement.requestFullscreen) {
              document.documentElement.requestFullscreen();
              } else if (document.documentElement.mozRequestFullScreen) { // Firefox
              document.documentElement.mozRequestFullScreen();
              } else if (document.documentElement.webkitRequestFullscreen) { // Chrome, Safari, Opera
              document.documentElement.webkitRequestFullscreen();
              } else if (document.documentElement.msRequestFullscreen) { // IE/Edge
              document.documentElement.msRequestFullscreen();
              }

              document.addEventListener('fullscreenchange', (event) => {
                  if (document.fullscreenElement) {
                      // console.log('Entered fullscreen:', document.fullscreenElement);
                  } else {
                      // console.log('Exited fullscreen.');
                  }
              });
  }

  async function recordScreen() {
  
      try {
          stream =  await navigator.mediaDevices.getDisplayMedia({ 
              video : {
                  displaySurface : 'screen',
                  
              },
          });

          audioStream = await navigator.mediaDevices.getUserMedia({
              // video: true,
              audio:true
          })

          isEntireScreenShared().then((returnValue) => {
              // console.log(returnValue);

              if (returnValue==true) {
              // console.log('Entire Screen shared.');

              recorder = new RecordRTC([stream,audioStream], {
                  type: 'video/mp4',
                  mimeType: 'video/mp4',
                  audio:true,
                  // disableLogs: true,
                  video: {
                      width: 1280, 
                      height: 720,
                      // frameRate: 15, 
                      // bitrate: 1024, 
                      // frameInterval:200,
                  },
                  timeSlice: 1000,
                  ondataavailable: (blob) => {
                    chunks.push(blob);
                    console.log('hiiiii');
                    console.log(blob.size);
                    }
                  
                  // quality:0.4
              });
              // shareFullScreen();
              
              recorder.startRecording();

              
              recorder.pauseRecording();

              permissionGranted = true;
              console.log('saqq',displayVideoPage);
              window.addEventListener('blur', handleWindowBlur);
              window.addEventListener('focus', handleWindowFocus);

              
          }

          else {
              alert('Share Entire screen in order to proceed with assessment.');
              if (stream) {
                  const tracks = stream.getTracks();
                  tracks.forEach(track => track.stop());
                  stream = null;
              }
          }

              
          })
          
          

      }

      catch (error) {
          console.error('Error capturing screen:', error);
          if (stream) {
              const videoTrack = stream.getVideoTracks()[0];
              videoTrack.removeEventListener('ended', handleScreenSharingEnded);
              const tracks = stream.getTracks();
              tracks.forEach(track => track.stop());
              stream = null;
          }
      }
  }

 

  async function stopRecording () {
      await recorder.stopRecording(() => {
          let blob = recorder.getBlob();
          invokeSaveAsDialog(blob,'recording.mp4');
          let tempp = URL.createObjectURL(blob);
          // console.log(typeof tempp.slice(5));
          videoURL.set(tempp);
          //console.log(videoURL);
          
          
          if (recorder) {
              recorder.destroy();
              recorder = null;
          }

          if (stream) {
              const videoTrack = stream.getVideoTracks()[0];
              if(videoTrack){
                videoTrack.removeEventListener('ended', handleScreenSharingEnded);
              }
              const tracks = stream.getTracks();
              tracks.forEach(track => track.stop());
              stream = null;
          }

          if (audioStream) {

              const videoTrack = audioStream.getVideoTracks()[0];
              if (videoTrack){
                videoTrack.removeEventListener('ended', handleScreenSharingEnded);
              }
              const tracks = audioStream.getTracks();
              tracks.forEach(track => track.stop());
              audioStream = null;
          }
      });
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


  async function submit() {

      // console.log('Trying submitting the assessment.');
      await stopRecording();
      // console.log(videoData);
      displayVideoPage = true;
    //   permissionGranted = false;
      // displayVideoPage.set(true);

      
      console.log(displayVideoPage,'===');
      alert('Assessment Successfully submitted.')

      
  }

  async function submitTest() {
        // console.log(timestamps);
        //videoData = timestamps;
        if (typeof window){
            window.removeEventListener('blur',handleWindowBlur);
            window.removeEventListener('focus',handleWindowFocus);
        }
        let retfubc = await submit().then(()=> {
            console.log('56');
        });
        console.log('55');
        
        // displayVideoPage=true;
    }


  async function handleScreenSharingEnded() {
      window.removeEventListener('blur',handleWindowBlur);
      window.removeEventListener('focus',handleWindowFocus);
      await submit();
      window.location.reload();
  }


</script>

<svelte:head>
  <script src="https://www.WebRTC-Experiment.com/RecordRTC.js"></script>


  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</svelte:head>

{#if desktopView}

        {#if permissionGranted }


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


               



        {:else}
                <div class="card text-center" bind:this={componentRef}>
                <div class="card-header">
                    Welcome to assessment page.
                </div>
                <div class="card-body">
                    <h5 class="card-title">Permissions required</h5>
                    <p class="card-text">You have to allow permissions for recording your screen in order to take this assessment.</p>
                    <button on:click={()=>{recordScreen()}} class="btn btn-primary">Allow permission and take assessment</button>
                </div>

                
                </div>

        {/if}

{:else}
        <center>
        <p>
            This web page can only be opened in chrome browser in desktop/laptop. 
        </p>
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