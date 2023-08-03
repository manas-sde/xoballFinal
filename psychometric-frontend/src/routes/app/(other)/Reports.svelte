<svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" rel="stylesheet"/>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.0.1/chart.min.js"></script>
</svelte:head>


<br>
<button type="button" class="btn btn-info" style="margin-left:5%;" on:click={loc_rel}>&larr; Back</button>
<br><br>

<div class="container text-center" style="float: center;">
    <div class="card c1">

        <div class="card-header">
            <h3 class="h3">
                Reports on Psychometric Assessments
            </h3>
        </div>

        <div class="card-body my-auto">
            <table class="table center" align="center">
                <thead>
                  <tr>
                    <th scope="col"></th>
                    <th scope="col" class="h5">Psychometric Traits</th>
                    <th scope="col" class="h5">Score Obtained</th>
                    <th scope="col"></th>
                  </tr>
                </thead>
                <tbody>

                    {#each Object.entries(totalScore) as [trait,score], index}
                        <tr>
                            <th class="colTab" scope="row">{index+1}</th>
                            <td class="colTab">{trait}</td>
                            <td class="colTab">{score} / 30</td>
                            <td>
                                <canvas bind:this={portfolio[index]} id="myChart" width="500" height="300"/>
                            </td>
                        </tr>
                    {/each}
                </tbody>
              </table>
        </div>

    </div>

</div>



<script>
    export let totalScore;
    export let allData;
    export let ndata;
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';


    function loc_rel() {
        location.reload();
    }




    let allTraitScore = ndata;

    let allCandID = {};
    ndata = {};


    allTraitScore = Object.entries(allTraitScore);

    let key,value;
    for([key,value] of  allTraitScore){
        for(let i=0;i<value.length;i++){

            if (allCandID[key]){
                allCandID[key].push('ID : ' + value[i]['candID']);
            }

            else{
                allCandID[key] = ['ID : ' + value[i]['candID']]
            }

            if (ndata[key]){
                ndata[key].push(value[i]['score']);
            }

            else{
                ndata[key] = [value[i]['score']]
            }


            // console.log('vd',allCandID[key]);
            // allCandID[key] = allCandID[key] ? allCandID[key].push(value[i]['candID']) : [value[i]['candID']];
            // console.log('nd',ndata[key]);
            // ndata[key] = ndata[key] ? ndata[key].push(value[i]['score']) : [value[i]['score']];
            // console.log('---');
        }
    }

    console.log(allCandID,ndata);








    //console.log('Total Score : ',totalScore);

    // Calculating mean for normal curve
    function calcMean(data, useY) {
        const sum = data.reduce((a, b) => a + (useY ? b.y : b), 0);
        return sum / data.length;
    }


    //console.log(totalScore);

    var port;

    // var ndata =
    //             {
    //                 "Emotional Stability" : [30,30,30,5],
    //                 "Integrity" : [30,15,20,10,30],
    //                 "Openness": [30,15,20,10,30],
    //                 "Reasoning": [30,15,20,10,30],
    //                 "Perfectionism": [30,15,20,10,30],
    //                 "Rule Consciousness" : [30,15,20,10,30]
    //             };



    var lendata = Object.keys(totalScore).length;

    //console.log(lendata);

    const portfolio=new Array(lendata);
    //console.log(portfolio);
    var curdata;

    for (let i=0;i<lendata;i++){



        //console.log(i);


        //console.log(allData);
        curdata = ndata[Object.keys(totalScore)[i]];
        //console.log(totalScore);
        //console.log(curdata);
        //curdata = [80,20,80];
        let data = new Array();
        //console.log(ndata);
        //console.log(allData);
        //console.log(curdata);
        for(let i=0;i<curdata.length;i++){
            let tempdata = {
                x:i,
                y:curdata[i]*100/30,
            };
            data[data.length] = tempdata;
            //console.log(tempdata);
        }
        //const data = new Array(5).fill(0).map((v, i) => ({x: i, y: 100 + Math.random() * 100}));
        //console.log(data);



        const mean = calcMean(data, true);
        //console.log('Data : ',data);
        //console.log('Mean : ',mean);

        const tmp = data.map(p => Math.pow(p.y - mean, 2));
        const variance = calcMean(data.map(p => Math.pow(p.y - mean, 2)));
        const stddev = Math.sqrt(variance);
        const pdf = (x) => {
        const m = stddev * Math.sqrt(2 * Math.PI);
        const e = Math.exp(-Math.pow(x - mean, 2) / (2 * variance));
        return e / m;
        };
        const bell = [];
        const startX = 0; mean - 3.5 * stddev;
        const endX = 100; mean + 3.5 * stddev;
        const step = 5;Math.round(stddev/10);
        let x;
        for(x = startX; x <= mean; x += step) {
        bell.push({x, y: pdf(x)});
        }

        for(; x <= endX; x += step) {
        bell.push({x, y: pdf(x)});
        }
        x = 100;
        bell.push({x, y: pdf(x)});

        //console.log('allData',allData[0]);
        let scatterData = new Array();

        let multiplier = 20;

        let countPoints = ndata[Object.keys(totalScore)[i]].length;

        if(countPoints>20){
            multiplier = countPoints;
        }

        for(let kk=0;kk<ndata[Object.keys(totalScore)[i]].length;kk++){
            let temp1 = ndata[Object.keys(totalScore)[i]][kk]*100/30;
            
            
            if (temp1==0){
                scatterData.push({x:temp1,y:5});
            }
            else{
                scatterData.push({x:temp1,y:(kk+1)*175/countPoints});
            }
            //allCandID.push('ID : '+(kk+1));
        }



       //console.log('ndata : ',ndata[Object.keys(allData[0])[i]]);
       //console.log(scatterData);
        //console.log(bell);

        //portfolio = document.getElementById('myChart');

        //const ctx = portfolio[i].getContext('2d');
        //console.log('-**********');


        const footer = (tooltipItems) => {

        return '';
        };


        const config =
        {
        type: 'scatter',
        data: {
            labels: allCandID[Object.keys(totalScore)[i]],

            datasets: [

                {
            type: 'bubble',
            label: 'John : '+Math.round(totalScore[Object.keys(totalScore)[i]]*100/30,2) + '%',
            data: [{x:Math.round(totalScore[Object.keys(totalScore)[i]]*100/30,2),y:100}],
            xAxisID: 'x2',
            yAxisID: 'y',
            barPercentage:2,
            //fill: true,
            //   tension: 0.4,
            radius: 20,
            backgroundColor: 'rgb(255,255,0)',
            },

            {
            type: 'bar',
            label: '',
            data: [{x:25,y:250},{x:50,y:300},{x:75,y:250}],
            xAxisID: 'x2',
            yAxisID: 'y',
            barPercentage:0.1,

            backgroundColor: 'white',
            },
            
            {
            type: 'scatter',
            label: 'Scores ',
            data: scatterData,
            xAxisID: 'x2',
            yAxisID: 'y',
            //fill: true,
            //   tension: 0.4,
            //   radius: 0,
            backgroundColor: 'blue',
            },

                {
            type: 'line',
            label: 'Scores (in %)',
            data: bell,
            xAxisID: 'x2',
            yAxisID: 'y2',
            fill: true,

            tension: 0.4,
            radius: 0,
            backgroundColor: 'rgb(152,251,152)',
            },

        ]
        },
        options: {
            tooltips: {
         callbacks: {
            label: function(tooltipItem, data) {
               var label = data.labels[tooltipItem.index];
               return label + ': (' + tooltipItem.xLabel + ', ' + tooltipItem.yLabel + ')';
            }
         }
      },
            interaction: {
            //mode: '',
            intersect: false
            },
            plugins: {
                legend: {
                    labels: {
                filter: function(item, chart) {
                    // Logic to remove a particular legend item goes here
                    return !item.text.includes('Scores (in %)');
                },
                },

                },
                tooltip: {
                    callbacks: {
                    footer: footer,
                    },

                }
                },


            scales: {
            x: {min: 0, max: 100,display: false},
            y: {min: 0, max: 300, title: {display: false, text: 'Data'},display: false},
            x2: {
                position: 'bottom',
                type: 'linear',
                display: true,
                grid: {
                display: false
                },
                title: {display: 'false',text:'Scores (in %)'},

                ticks: {
                maxRotation: 0
                },
                min: startX,
                max: endX
            },
            y2: {
                type: 'linear',
                position: 'right',
                display: false,
                grid: {
                display: false
                },
                title: {display: false, text: 'Bell Curve'}
            }
            }
        }};

        //console.log('---------------------------------------');
        onMount(()=> {
            var ctx = portfolio[i].getContext('2d');
            // Initialize chart using default config set
            var myChart = new Chart(ctx, config);
          })
        };

      /*
      const data = {
            labels: ['Expenses', 'Savings', 'Investments'],
            datasets: [
                {
                    label: 'My First Dataset',
                    data: [300, 50, 100],
                    backgroundColor: ['#7000e1', '#fc8800', '#00b0e8'],
                    // hoverOffset: 4,
                    borderWidth: 0
                }
            ]
        };
        const config = {
            type: 'doughnut',
            data: data,
            options: {
                borderRadius: '30',
                responsive: false,
                cutout: '95%',
                spacing: 2,
                plugins: {
                    legend: {
                        position: 'bottom',
                        display: true,
                        labels: {
                            usePointStyle: true,
                            padding: 20,
                            font: {
                                size: 14
                            }
                        }
                    },
                    title: {
                        display: true,
                        text: 'My Personal Portfolio'
                    }
                }
            }
        };
      onMount(()=> {
        var ctx = portfolio[i].getContext('2d');
        // Initialize chart using default config set
        var myChart = new Chart(ctx, config);
      })

    }


	*/



</script>








<style>
    .container{
        margin-left: auto;
        margin-right: auto;
        margin-top : 5%;
    }

    table,td{
        align-items: center;
    }

    .colTab{
        vertical-align: middle;
    }

    .center {
        margin-left: auto;
        margin-right: auto;
    }


</style>