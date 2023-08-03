<script>
    import { videoData, videoURL } from "./stores";

    let videoSRC;

    videoURL.subscribe(data => {
        videoSRC = data;
    });

    console.log(typeof videoSRC[0],'**')
    console.log(videoSRC,'------** --', videoData);

</script>

<center>
<br><br>


<div class="grid-container">
    <br>
    <center>
    <h2>
        Candidate proctoring report
    </h2>
    </center>
    <div class="grid-item">
        <p>
            Total off tab activity - {videoData.length}
        </p>
        {#each videoData as dataItem,index}
        <ul>
        <li>
            <button on:click={()=>{
                let videoElement = document.querySelector('video');
                videoElement.src = videoSRC+'#t=' +dataItem.startTime + ',' + dataItem.endTime;
                videoElement.play();
                console.log(videoElement.src);
            }}> 
            Click to view - Off tab activity {index+1}</button>
        </li>
        </ul>

        {/each}
    </div>
    <div class="grid-item">
        <video src="{videoSRC}" width="800" height="650" controls>
            <track kind="captions">
        </video>
    </div>

</div>

</center>


<style>

.grid-container {
  display: grid;
  grid-template-columns: auto auto;
  background-color: #2196F3;
  padding: 10px;
  margin:20%;
}

.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;

}

</style>