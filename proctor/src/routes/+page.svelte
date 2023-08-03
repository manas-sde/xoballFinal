<script>
    import App from "./App.svelte";

    import { onMount } from "svelte";

    import {videoURL,displayVideoPage} from './stores.js';

    import DisplayVideoPage from "./DisplayVideoPage.svelte";

    let permissionGranted=false;
    let stream,recorder,audioStream;
    let isDesktop;

    let manuallyEnded = false;
    let displayRes=false;

    let desktopView = false;

    let componentRef;

    onMount(()=> {
        const userAgent = navigator.userAgent.toLowerCase();
        isDesktop = !/mobile|android|iphone|ipad|iemobile|wpdesktop/i.test(userAgent);
        console.log(isDesktop);
        console.log(userAgent);
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
                    timeSlice:1000,
                    ondataavailable : (blobb) =>  {
                        console.log('njknihilhu')
                    if (blobb && blobb.size > 0) {
                    console.log("Data received");

                    const formData = new FormData();
                        formData.append('chunk', blobb);
                        formData.append('filename', 'checkrec1.mp4');

                        fetch('http://127.0.0.1:5000/upload', {
                            method: 'POST',
                            body: formData,
                        });
                    }
                    }
                    
                    // quality:0.4
                });
                // shareFullScreen();
                
                recorder.startRecording();
                
                recorder.pauseRecording();

                permissionGranted = true;
                
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

    // if (recorder){
    // recorder.ondataavailable = (event) => {
    //     if (event.data && event.data.size > 0) {
    //        console.log("Data received");

    //        const formData = new FormData();
    //         formData.append('chunk', new Blob(event.data), 'check'+Math.round(Math.random()*1000));
    //         formData.append('filename', filename);

    //         fetch('http://127.0.0.1:5000/upload', {
    //             method: 'POST',
    //             body: formData,
    //         });
    //     }
    // };
    // }

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
                videoTrack.removeEventListener('ended', handleScreenSharingEnded);
                const tracks = stream.getTracks();
                tracks.forEach(track => track.stop());
                stream = null;
            }

            if (audioStream) {

                const videoTrack = audioStream.getVideoTracks()[0];
                videoTrack.removeEventListener('ended', handleScreenSharingEnded);
                const tracks = audioStream.getTracks();
                tracks.forEach(track => track.stop());
                audioStream = null;
            }
        });
    }


    async function submit() {

        // console.log('Trying submitting the assessment.');
        await stopRecording();
        // console.log(videoData);
        permissionGranted = false;
        displayVideoPage.set(true);

        displayVideoPage.subscribe(data => {
            console.log(data);
            displayRes=data;
        });
        console.log(displayRes,'===');
        alert('Assessment Successfully submitted.')

        
    }

    async function handleScreenSharingEnded() {
        window.removeEventListener('blur',handleWindowBlur);
        window.removeEventListener('focus',handleWindowFocus);
        await submit();
        window.location.reload();
    }

    function handleWindowBlur() {

    }

    function handleWindowFocus() {

    }


</script>

<svelte:head>
    <script src="https://www.WebRTC-Experiment.com/RecordRTC.js"></script>


    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</svelte:head>

{#if permissionGranted }
<App  submit={submit} recorder={recorder}/>

{:else if displayRes}

<DisplayVideoPage/>

{:else if desktopView}
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

  <video src="https://storage.googleapis.com/live-streaming-storage-manas/checkrec1.mp4" width="800" height="650" controls>
    <track kind="captions">
</video>



{:else}
<center>
    <p>
        This web page can only be opened in chrome browser in desktop/laptop. 
    </p>
</center>


{/if}

