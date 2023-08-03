<script>
    import App from "./App.svelte";
    // import RecordRTC from 'recordrtc';
    import { onDestroy } from 'svelte';
    import { onMount } from 'svelte';


    var permissionGranted=false;
    let recorder;
    let videoURL;
    let stream;
    let offTabCount=0;
    var recordingStarted = false;

    
    const isEntireScreenShared = () => {

        return true;
        // const videoTrack = stream.getVideoTracks()[0];
        // const capabilities = videoTrack.getCapabilities();

        // // Check if the "displaySurface" constraint is present and set to "monitor"
        // if (capabilities.displaySurface && capabilities.displaySurface.includes('monitor')) {
        // return true;
        // }

        // // Check if the "cursor" constraint is present and set to "always"
        // if (capabilities.cursor && capabilities.cursor.includes('always')) {
        // return true;
        // }

        // // If none of the above checks pass, assume it is not the entire screen
        // return false;
  };


    async function recordScreen() {
        try {
            stream =  await navigator.mediaDevices.getDisplayMedia({ 
                // video: { displaySurface:'monitor'}
            });

            
            if (isEntireScreenShared()) {
                recorder = new RecordRTC(stream, {
                    type: 'video',
                    mimeType: 'video/webm',
                });

                // if (document.documentElement.requestFullscreen) {
                // document.documentElement.requestFullscreen();
                // } else if (document.documentElement.mozRequestFullScreen) { // Firefox
                // document.documentElement.mozRequestFullScreen();
                // } else if (document.documentElement.webkitRequestFullscreen) { // Chrome, Safari, Opera
                // document.documentElement.webkitRequestFullscreen();
                // } else if (document.documentElement.msRequestFullscreen) { // IE/Edge
                // document.documentElement.msRequestFullscreen();
                // }

                // document.addEventListener('fullscreenchange', (event) => {
                //     if (document.fullscreenElement) {
                //         console.log('Entered fullscreen:', document.fullscreenElement);
                //     } else {
                //         console.log('Exited fullscreen.');
                //     }
                // });

                

                // Start recording
                console.log('Starting recording ...........')
                recorder.startRecording();
                console.log('Pausing initially ...........');
                recorder.pauseRecording();
                recordingStarted = true;
                // permissionGranted = true;
                window.addEventListener('blur', handleWindowBlur);
                window.addEventListener('focus', handleWindowFocus);
                
                // document.addEventListener('visibilitychange', handleVisibilityChange);
            }

            else {
                alert('Share Entire screen in order to proceed with assessment.')
            }
            

        }

        catch (error) {
            console.error('Error capturing screen:', error);
            if (stream) {
                const tracks = stream.getTracks();
                tracks.forEach(track => track.stop());
                stream = null;
            }
        }
    }

    async function stopRecording () {
    await recorder.stopRecording(() => {
        let blob = recorder.getBlob();
        invokeSaveAsDialog(blob);
        if (recorder) {
        recorder.destroy();
        recorder = null;
        }

        if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        stream = null;
        }
    });
    }


    function submit() {
        recordingStarted=false;
        stopRecording();
        // recordingStarted=false;
        permissionGranted = false;
        alert('Your assessment has been submitted.');
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            stream = null;
        }
        window.removeEventListener('blur',handleWindowBlur);
        window.removeEventListener('focus',handleWindowFocus);
        // if(document.exitFullscreen) {
        //     document.exitFullscreen();
        // } else if (document.mozCancelFullScreen) {
        //     document.mozCancelFullScreen();
        // } else if (document.webkitExitFullscreen) {
        //     document.webkitExitFullscreen();
        // }

        // window.removeEventListener('blur', handleWindowBlur);
        // document.removeEventListener('visibilitychange', handleVisibilityChange);
    }

    onDestroy(() => {
        if (recorder) {
        recorder.destroy();
        recorder = null;
        }

        if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        stream = null;
        }
    });

    // onMount(() => {
    //     document.addEventListener('fullscreenchange', (event) => {
    //         if (document.fullscreenElement) {
    //             console.log('Entered fullscreen:', document.fullscreenElement);
    //         } else {
    //             console.log('Exited fullscreen.');
    //         }
    //     });
    // });


    function handleWindowBlur (){

        if (recordingStarted) {
            offTabCount+=1;
            if (offTabCount==5){
                alert('You have reached the maximum bound of unusual activity. Your test have to be forcefully submitted now.')
                return submit();
            }
            alert('Unwanted activity found. (' + offTabCount + '/5)');
            console.log('Off tab activity found, resuming recording..');
            recorder.resumeRecording();
            // console.log("Recording paused");
                
                

                
                
            // captureScreenshot();
        }
    };

    const handleWindowFocus = () => {
        alert('Focussed window')
        if (recordingStarted) {
            console.log('Off tab activity ended, pausing recording..');
                recorder.pauseRecording();
            // console.log("Recording paused");
                
                // offTabCount+=1;
                
            
            // captureScreenshot();
        }
    };

    const handleVisibilityChange = () => {
        if (document.visibilityState === 'visible') {
        // isPageVisible = true;
        recorder.pauseRecording();
        // console.log("Recording resumed.")

        
        } 
        // else {
        // // isPageVisible = false;
        
        // offTabCount+=1;
        // alert('You have changed the tab. (' + offTabCount +'/3)');
        // }
    };


    // const captureScreenshot = async () => {
    //     const canvas = document.createElement("canvas");
    //     const context = canvas.getContext("2d");
    //     const screenshot = document.createElement("screenshot");
    
    //     try {
    //         const captureStream = await navigator.mediaDevices.getDisplayMedia();
    //         screenshot.srcObject = captureStream;
    //         context.drawImage(screenshot, 0, 0, window.width, window.height);
    //         const frame = canvas.toDataURL("image/png");
    //         captureStream.getTracks().forEach(track => track.stop());
    //         window.location.href = frame;
    //         console.log('Screenshot taken');
    //     } catch (err) {
    //         console.error("Error: " + err);
    //     }
    // };


        const captureScreenshot = async () => {
        const canvas = document.createElement("canvas");
        const context = canvas.getContext("2d");
        const screenshot = document.createElement("video");

        try {
        const captureStream = await navigator.mediaDevices.getDisplayMedia();
        screenshot.srcObject = captureStream;
        screenshot.onloadedmetadata = () => {
            canvas.width = screenshot.videoWidth;
            canvas.height = screenshot.videoHeight;
            context.drawImage(screenshot, 0, 0, canvas.width, canvas.height);

            const dataUrl = canvas.toDataURL("image/png");
            const link = document.createElement("a");
            link.href = dataUrl;
            link.download = "screenshot.png";
            link.click();

            captureStream.getTracks().forEach((track) => track.stop());
            console.log("Screenshot taken");
        };
        } catch (err) {
        console.error("Error: " + err);
        }
    };
    
    



            // document.addEventListener("visibilitychange", (event) => {
            // if (document.visibilityState == "visible") {
            //     console.log("tab is active")
            // } else {
            //     console.log("tab is inactive")
            //     alert('You have changed the tab.', offTabCount,'/',3);
            //     offTabCount+=1;
            // }
            // });
   



</script>

<svelte:head>
    <script src="https://www.WebRTC-Experiment.com/RecordRTC.js"></script>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</svelte:head>

{#if permissionGranted }
<App submit={submit}/>
{:else}
<div class="card text-center">
    <div class="card-header">
      Welcome to assessment page.
    </div>
    <div class="card-body">
      <h5 class="card-title">Permissions required</h5>
      <p class="card-text">You have to allow permissions for recording your screen in order to take this assessment.</p>
      <button on:click={()=>{recordScreen()}} class="btn btn-primary">Allow permission and take assessment</button>
    </div>

    <div>Number of offtab activity detected : {offTabCount}</div>
    <div class="card-footer text-muted">
        <button on:click={()=>{submit()}} class="btn btn-primary">Submit Test</button>
    </div>
  </div>



  {/if}