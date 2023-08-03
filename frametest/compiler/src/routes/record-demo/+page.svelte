<script>
    import { onMount } from 'svelte';
  
    let recorder;
  
    onMount(() => {
      const startCapture = async () => {
        try {
          const stream = await navigator.mediaDevices.getDisplayMedia({
            video: {
              mediaSource: 'screen',
            },
          });
  
          // Create a new RecordRTC instance with the captured stream
          recorder = new RecordRTC(stream, {
            type: 'video',
            mimeType: 'video/webm',
          });
  
          // Start recording
          recorder.startRecording();
  
          // Optionally, you can stop recording after a certain duration
          // setTimeout(() => recorder.stopRecording(), 5000); // Stop recording after 5 seconds
        } catch (error) {
          console.error('Error capturing screen:', error);
        }
      };
  
      startCapture();
    });
  
    const stopRecording = () => {
      // Stop the recording
      recorder.stopRecording((videoURL) => {
        // `videoURL` contains the recorded video as a Blob
        console.log('Recording stopped:', videoURL);
        
        // Call a function to handle the conversion and upload of the recorded video
        convertAndUpload(videoURL);
      });
    };
  
    const convertAndUpload = (videoBlob) => {
      // Convert the Blob to a file object
      const videoFile = new File([videoBlob], 'screen_recording.webm', {
        type: 'video/webm',
      });
  
      // Implement the upload logic to Google Cloud Storage here
      // Use the Google Cloud Storage API or a library like `@google-cloud/storage`
      // to upload the `videoFile` to your desired storage bucket
      // Example: uploadToGoogleCloudStorage(videoFile);
    };
  </script>
  
  <button on:click={stopRecording}>Stop Recording</button>
  