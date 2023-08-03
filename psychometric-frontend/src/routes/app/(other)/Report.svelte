<svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" rel="stylesheet"/>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.0.1/chart.min.js"></script>

</svelte:head>


<div class="text-right" style="position:absolute; right:1px;top:30px">
<span><img  src="https://xobinstore.blob.core.windows.net/web/new-xobin.png" style="width:15%"></span>
</div>
<div class="text-left hidden-print" style="margin-top: 2%;">
<button type="button" class="btn btn-info" style="margin-left:5%;float:left" on:click={loc_rel}>&larr; Back</button>

<button type="button" class="btn btn-secondary" style="margin-right:5%;float:right" on:click={download_report}>&darr;Download Report</button>
</div>



<br><br>
  <div class="show-print" id="report_page" style="margin-bottom: 5%;">
<div class="container text-center" >
    <div class="card c1 card-box" style="margin-bottom: 1%;">

        <div class="card-header">
            <h5 class="page-title text-interact-1 text-left">John Doe</h5>
            <h6 class=" text-left ">johndoe32@gmail.com</h6>
        </div>
    </div>
    <div class="card c1 card-box">

        <div class="card-header">
            <h4 class="page-title text-interact-1 text-center">Overall Performance</h4>
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

    <div class="card c1 card-box" style="margin-top: 50px;">

        <div class="card-header">
            <h4 class="page-title text-interact-1 text-center">Overall Summary</h4>
        </div>

        <div class="card-body my-auto">
            {#each candidateReport as traitReport}
    
            <div class="text-dark text-left">
                <span style="font-size: large; font-weight:bold;">{traitReport.traitComment}</span>
                
                <span style="float: right;"><b>{traitReport.trait} : </b> {traitReport.score} %</span>

                <br>
                <br>
                <span>{traitReport.description}</span>
                     
            </div>
            <br><br>
            
    {/each}

        </div>
    </div>

</div>
</div>



<script>
    export let totalScore;
    export let allData;
    export let ndata;
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';


    var allTraitReports = 
        {

            'Emotional Stability' : 
            {
                'bucket1': {
                    
                    'comment' : 'Zero Emotional Stability ',
                    'description' : 'The candidate has very low emotional stability, he may be susceptible to high-pressure situations, that might put his emotions and associated decisions to the test. '
                },
                'bucket2' : {
                    'comment' : 'Low Emotional Stability',
                    'description': 'The candidate possesses very low emotional stability, where they cave into most situations apart from certain situations that are not a great concern to them. They might not be a good fit for top-level managerial positions but might fit into situations which does not involve human interaction.  '
                },
                'bucket3' : {
                    'comment' : 'Medium Emotional Stability ',
                    'description' : 'The candidate possesses a medium emotional stability state, where he would be productive in most situations, but in extreme situations, where it is tough to manage emotions, the candidate might cave in. This may cause a slight glitch in the productivity of the candidate. '
                },
                'bucket4' : {
                    'comment' : 'High Emotional Stability',
                    'description' : 'The candidate has very high emotional stability. they would be able to differentiate between personal emotions and professional decisions with utmost care. They are people who can handle any given tough situation with ease and result in increased productivity for the organization'
                }
            },
    

            'Integrity' :
            {
                'bucket1': {
                    'comment' : 'Zero Integrity  ',
                    'description' : 'Since the candidate has scored very low in integrity, they are not dependable people for a high level of confidential work. They possess very low to no work ethic.'
                },
                'bucket2' : {
                    'comment' : 'Low Integrity',
                    'description': 'The candidate has a low level of integrity, which might cloud his judgemental ability at times of crisis.'
                },
                'bucket3' : {
                    'comment' : 'Medium Integrity ',
                    'description' : ' The candidate has a medium integrity towards situations, which might be beneficial or not beneficial depending upon the situations that are given to them. they might be good decision-makers but not ideal decision-makers.'
                },
                'bucket4' : {
                    'comment' : 'High Integrity',
                    'description' : 'The candidate has a highly integrated approach to all the problems that are given to them. They are excellent decision-makers coupled with high emotional stability and will be an ideal fit for the organization. '
                }
            },

            'Openness' : 
            {
                'bucket1': {
                    'comment' : 'Zero openness',
                    'description' : ' The candidate has scored nil in this section, which shows the candidate is an introvert and does not talk openly about problems and situations. '
                },
                'bucket2' : {
                    'comment' : 'Low openness',
                    'description': 'The candidate has very low openness in talking out their mind, which may be good in places where the candidate is not required to talk openly but not suitable for places that involves people management. '
                },
                'bucket3' : {
                    'comment' : 'Medium openness',
                    'description' : 'The candidate has a medium open approach towards situations and people. This is a good personality trait when recruiting people in managerial positions which involve interaction with numerous people. '
                },
                'bucket4' : {
                    'comment' : 'High openness',
                    'description' : 'The candidate is highly open in his thoughts and ideologies. they can serve as excellent leaders. the downside is that they can be arrogant at times in extreme situations. '
                }
            },


            'Perfectionism':
            {
                'bucket1': {
                    'comment' : 'Nil Perfectionism ',
                    'description' : ' The candidate has scored a very low perfectionism score. The candidate might be able to finish the tasks but expecting the candidate to be prompt and perfect is not possible is most situations. '
                },
                'bucket2' : {
                    'comment' : 'Low Perfectionism',
                    'description': 'The candidate has low perfectionism, which shows he might be a potential procrastinator.'
                },
                'bucket3' : {
                    'comment' : 'Medium Perfectionism ',
                    'description' : 'The candidate has scored a medium in perfectionism as a personality trait. The candidate can work in situations that do not involve high-stress levels.'
                },
                'bucket4' : {
                    'comment' : 'High Perfectionism',
                    'description' : 'The candidate is a highly perfectional candidate who keeps his/her word till the end. The candidate is a highly dependable person who can work under challenging circumstances. '
                }
            },

            'Reasoning' : 
            {
                'bucket1': {
                    'comment' : 'Nil Reasoning Ability  ',
                    'description' : ' The candidate has shown zero reasoning ability with the situations put in front of them. They tend to be impulsive with their actions and decisions. '
                },
                'bucket2' : {
                    'comment' : 'Low Reasoning Ability ',
                    'description': 'The candidate has scored very low reasoning ability. they might not be suitable for positions that involves analyzing and decision making.'
                },
                'bucket3' : {
                    'comment' : 'Medium Reasoning Ability ',
                    'description' : ' The candidate has displayed medium reasoning ability. they can be reasonable to mild crisis situations which involve the intervention of top-level management. '
                },
                'bucket4' : {
                    'comment' : 'High Reasoning Ability',
                    'description' : 'The candidate has displayed a high level of reasoning. the candidate might be a good fit for top-level managerial positions that involve lots of decision-making, interaction with people, and handing complex situations.'
                }
            },

            'Rule Consciousness' : 
            {
                'bucket1': {
                    'comment' : 'No Rule conciousness ',
                    'description' : ' The candidate has no adherence to the rules, they seem to be lethargic in their actions. '
                },
                'bucket2' : {
                    'comment' : 'Low Rule conciousness  ',
                    'description': 'The candidate seems to adhere to only a few rules which are stringent enough. They might be conscious to rules provided they are followed by hefty penalties.'
                },
                'bucket3' : {
                    'comment' : 'Medium Rule conciousness  ',
                    'description' : ' The candidate has a medium adherence to the rules, they mostly are conscious of the rules but tend to be off track at times when strict monitoring isn\'t available.'
                },
                'bucket4' : {
                    'comment' : 'High Rule conciousness ',
                    'description' : 'The candidate has high rule consciousness be prompt in finishing the tasks given to them. They might be too straightforward at times which might seem rude sometimes.'
                }
            },


            'Team Work' : 
            {
                'bucket1': {
                    'comment' : 'Nil teamworking ability  ',
                    'description' : ' The candidate has displayed no team working spirit. They may bring down the morale of the team if selected for the organization. '
                },
                'bucket2' : {
                    'comment' : 'Low teamworking ability ',
                    'description': 'The candidate has displayed very low team working ability. They might be not fit to an organization which demands lots of collaboration and tea work'
                },
                'bucket3' : {
                    'comment' : 'Medium teamworking ability ',
                    'description' : ' The candidate has displayed a medium team working ability. The situations of them working in a team depends on their comfortableness to the situations. They would be a good fit for organizations which involve a medium team working requirement.'
                },
                'bucket4' : {
                    'comment' : 'High teamworking ability',
                    'description' : 'The candidate is an extreme extrovert who can communicate with anyone with ease and agility. They display a high team working ability which is a good fit for organizations looking to recruit persons for marketing and customer support and would be a good fit for managerial positions involving interacting with numerous people. '
                }
            },


            'Sensitivity' : 
            {
                'bucket1': {
                    'comment' : 'Nil Sensitivity  ',
                    'description' : ' The candidate seems to be insensitive to situations, which might be a good personality trait when handling customers who are rude and in it helps the candidate to maintain their composure in harsh situations.'
                },
                'bucket2' : {
                    'comment' : 'Low Sensitivity ',
                    'description': 'The candidate is a little bit sensitive to situations that concern them. Otherwise, they are insensitive to most situations.  '
                },
                'bucket3' : {
                    'comment' : 'Medium Sensitivity ',
                    'description' : ' The candidate has medium sensitivity to situations even in situations that do not concern them. They might be considerate people but sometimes they might turn a blind eye to the situations around them though they are considerate people.  '
                },
                'bucket4' : {
                    'comment' : 'High Sensitivity',
                    'description' : 'The candidate is highly sensitive to situations around them. They might be responsive to every situation and person around them. At times this personality trait might be not good for a top-level managerial position that involves a certain level of sternness.'
                }
            },


            'Conflict Management' : 
            {
                'bucket1': {
                    'comment' : 'Nil ability to manage conflicts  ',
                    'description' : ' The candidate has nil ability to manage the conflicts arising out of tough situations. They might be skeptical about the situations around them. They are not effective communicators and not be able to manage situations that cause conflicts. '
                },
                'bucket2' : {
                    'comment' : 'Low Conflict Management Ability ',
                    'description': 'The candidate has scored very low in terms of managing conflicts. They might intervene in the situation but tend to give up on the pressure which is not good while managing conflicts. '
                },
                'bucket3' : {
                    'comment' : 'Medium Conflict Management Ability ',
                    'description' : ' The candidate has a medium conflict-managing ability, which puts him in a situation where he can manage most of the conflicts but tends to break under extreme pressure. The candidate might function to his ability under the guidance of an experienced top-level manager. '
                },
                'bucket4' : {
                    'comment' : 'High ability to manage conflicts',
                    'description' : 'The candidate has a high potential to manage conflicts. They are effective communicators and possess team working ability which makes them a natural leader. They are quick thinkers and are capable to manage situations which might cause conflict with ease. '
                }
            },


            'Inclusion' : 
            {
                'bucket1': {
                    'comment' : 'Nil inclusivity ',
                    'description' : ' The candidate possesses nil ability to include people in their day-to-day activities. They seem to be toxic to the work environment which is not good for the organization in the longer run. '
                },
                'bucket2' : {
                    'comment' : 'Low inclusivity',
                    'description': 'The candidate has a very low tendency to include people in their decisions. They are delusional in their decisions. They tend to include people of their interest which might cause conscious bias in the organization. They might cause organizational hierarchy. '
                },
                'bucket3' : {
                    'comment' : 'Medium inclusivity ',
                    'description' : 'The candidate processes medium inclusiveness in their workplace. But at times they might inculcate unconscious bias. They might be able to perform well under crisis situations under the supervision of the top level management. '
                },
                'bucket4' : {
                    'comment' : 'High inclusivity',
                    'description' : 'The candidate promotes high inclusivity in the workplace. They are excellent communicators and considerate people. They are born leaders. They do not cause bias in the organization even unconsciously. They can be good top-level managers which involves communicating with a huge number of people.'
                }
            }







        };



    console.log(allData);

    function loc_rel() {
        location.reload();
        
    }

    function download_report () {
        console.log("Downdalads");
        window.print();
    }

    function getBucket(score) {
        let count = Math.round(score/25);

        if(count==4) {
            count-=1;
        }
        
        return ('bucket'+(count+1));
    }


    var candidateReport = [];

    Object.keys(totalScore).forEach(trait => {
        
        let score = Math.round(totalScore[trait]*10000/30) / 100;

        let bucket = getBucket(score);

        let comment = '',description='';
        

        comment = allTraitReports[trait][bucket]['comment']

        description = allTraitReports[trait][bucket]['description']

        candidateReport.push({
            'trait' : trait,
            'traitComment' : comment,
            'score' : score,
            'description' : description
        });

        //console.log(candidateReport);
        
    });




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

    .card-box {
         box-shadow: 0 0px 24px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);
    }

    


</style>