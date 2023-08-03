

<svelte:head>
    
    <title>Xobin - Report</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="shortcut icon" href="https://storage.googleapis.com/interactapp-202211.appspot.com/icl3941NZDFSFJ09Sicl3941I34XZ4NS4MXobinLogo.png" type="image/x-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400;500;600;700;900&family=Open+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <link rel="stylesheet" href="/psychometric-staticfiles/css/report.css">
    <link href="https://xobinteam.xobin.com/wc/static/assets/css/pagex.css" rel="stylesheet" type="text/css" />




</svelte:head>


    <div class="overall-report">
        <ReportNav/>

        <CandidateInfo/>

        <TraitWiseReport/>

        

        
    </div>

<script>
    import ReportNav from "./ReportNav.svelte";
    import TraitWiseReport from "./TraitWiseReport.svelte";
    import CandidateInfo from "./CandidateInfo.svelte";
</script>