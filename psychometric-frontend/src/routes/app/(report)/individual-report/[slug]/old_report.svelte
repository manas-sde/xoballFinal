<script>
    import html2canvas from "html2canvas";
    import jsPDF from "jspdf";
    import { onMount } from "svelte";
    import axios from "axios"; 
    import Report from "../../../(other)/Report.svelte";

    export let data;

    var element,
        canvas,
        imgData,
        imgProps,
        pdfWidth = 215,
        pdfHeight = 180;

    var reportID, host, url, reportData;
    var reportLoading = true,
        reportNotFound = false;

    onMount(() => {
        async function loaded() {
            reportID = data.slug;

            url = "/psychometric/get-candidate-report";
            //console.log('I am here');
            if (typeof window !== "undefined") {
                host = window.location.host;
                if (host == "localhost:5173") {
                    url = "http://127.0.0.1:5000" + url;
                } else {
                    url =
                        "https://psychometric-backend-aw54llemya-uc.a.run.app" +
                        url;
                }
            }

            let options = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                },
                reportID: reportID,
            };

            var apiResponse = axios
                .post(url, options)
                .then((response) => {
                    reportData = response.data;
                    // var categPercentage;

                    // for (var keyy in reportData){
                    //     categPercentage = reportData[keyy]["ObtainedScore"]*100/reportData[keyy]["TotalScore"];

                    //     if (categPercentage<=25){
                    //         reportData[keyy]["categoryBucket"] = "active";
                    //     }

                    //     else if (categPercentage<=50){
                    //         reportData[keyy]["categoryBucket"] = "active";
                    //     }

                    // }
                    reportLoading = false;
                    reportNotFound = false;
                })
                .catch((error) => {
                    reportLoading = false;
                    reportNotFound = true;
                    console.log(
                        "Some error occured while connectng with backend. Please contact administrator."
                    );
                });

            // element = document.getElementsByClassName('page2')[0];
            // canvas = await html2canvas(element, { scale: 1 });
            // imgData = canvas.toDataURL('image/png');
            // canvas = await html2canvas(element, { scale: 1 });

            // document.getElementsByClassName('page2')[0].innerHTML = "<img src='" + canvas.toDataURL() + "' style='width:100%;'>";
        }

        loaded();
    });
    const generatePdf = async () => {
        const pdf = new jsPDF();

        element = document.getElementsByClassName("page1")[0];

        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL("image/png");
        imgProps = pdf.getImageProperties(imgData);
        //pdfWidth = pdf.internal.pageSize.getWidth();
        //pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, "PNG", 0, 0, 215, 175);
        pdf.addPage();

        var headerElement = document.getElementsByClassName("pdf-nav")[0];
        console.log(headerElement);
        canvas = await html2canvas(headerElement, { scale: 1 });
        imgData = canvas.toDataURL("image/png");
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, "PNG", 0, 0, pdfWidth, pdfHeight);

        element = document.getElementsByClassName("page3")[0];
        canvas = await html2canvas(element, { scale: 1 });
        imgData = canvas.toDataURL("image/png");
        imgProps = pdf.getImageProperties(imgData);
        pdfWidth = pdf.internal.pageSize.getWidth();
        pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
        pdf.addImage(imgData, "PNG", 8, 20, 195, 180);

        pdf.save("my-pdf-document.pdf");
    };

    // function printScale (){

    //     const pdf = new jsPDF();
    //     const element = document.getElementsByClassName('report')[0];
    //     console.log(element);
    //     pdf.html(element);
    //     pdf.save('my-pdf-document.pdf');

    // //   html2canvas(document.querySelector(".report")).then(canvas => {

    // //     // var win = window.open();
    // //     // win.document.write("<img src='" + canvas.toDataURL() + "' style='width:100%;'>");
    // //     // win.print();
    // //     // win.close();

    // //     const pdf = new jsPDF('p', 'mm', 'a4');
    // //     const imgData = canvas.toDataURL('image/png');
    // //     pdf.addImage(imgData, 'PNG', 0, 0, 210, 170); // adjust width and height as necessary (x,y,width,height)
    // //     pdf.save('scale.pdf');
    // //  });

    // }
</script>

<svelte:head>
    <script
        src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"
    ></script>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous"
    />
    <script
        src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"
    ></script>
    <script
        src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"
    ></script>
    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"
    ></script>

    <title>Xobin</title>
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.min.css"> -->
    <!-- <link rel="stylesheet" -->
    <!-- href="https://cdnjs.cloudflare.com/ajax/libs/jquery-timepicker/1.13.18/jquery.timepicker.min.css" -->
    <!-- integrity="sha512-GgUcFJ5lgRdt/8m5A0d0qEnsoi8cDoF0d6q+RirBPtL423Qsj5cI9OxQ5hWvPi5jjvTLM/YhaaFuIeWCLi6lyQ==" -->
    <!-- crossorigin="anonymous" referrerpolicy="no-referrer" /> -->
    <!-- <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.9.0/css/bootstrap-datepicker.min.css"
    integrity="sha512-mSYUmp1HYZDFaVKK//63EcZq4iFWFjxSL+Z3T/aCt4IO9Cejm03q3NKKYN6pFQzY0SBOr8h+eCIAZHPXcpZaNw=="
    crossorigin="anonymous" referrerpolicy="no-referrer" /> -->
    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    />
    <!-- <link rel="stylesheet" -->
    <!-- href="https://cdnjs.cloudflare.com/ajax/libs/offline-js/0.7.19/themes/offline-theme-chrome.min.css" -->
    <!-- integrity="sha512-gOD2ba2jNUv2wNDy03UaG2/l0U27ewq1R+Eiz9tpwad6RaIknfKKzb5jT4Dm8zZgr/qeTqs4hI2dJ8vEhyyM6g==" -->
    <!-- crossorigin="anonymous" referrerpolicy="no-referrer" /> -->
    <!-- App css -->
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" -->
    <!-- integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/core.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link rel="stylesheet" href="https://xobinteam.xobin.com/wc/static/assets/css/countdown-timer.css"> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/components.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/icons.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/pages.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/menu.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/responsive.css" rel="stylesheet" type="text/css" /> -->
    <!-- <link href="https://xobinteam.xobin.com/wc/static/assets/css/pagex.css" rel="stylesheet" type="text/css" /> -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <!-- <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin /> -->
    <!-- <link rel="stylesheet" href="https://unpkg.com/plyr@3/dist/plyr.css" /> -->
    <!-- <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/css/video-js-add.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/css/race-timer.css"
    /> -->
    <link
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400;500;600;700;900&family=Open+Sans:wght@300;400;500;600;700;800&display=swap"
        rel="stylesheet"
    />
    <!-- <link
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/toastr/toastr.min.css"
        rel="stylesheet"
        type="text/css"
    /> -->

    <!-- <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/jobTask-new-template/index_new.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/animate/animate.min.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/jquery-ui/jquery-ui.css"
    />
    <!-- Codemirror -->
    <!-- <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/lib/codemirror.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/theme/3024-night.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/theme/monokai.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/theme/ttcn.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/addon/hint/show-hint.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/addon/fold/foldgutter.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/addon/dialog/dialog.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/addon/search/matchesonscrollbar.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/codemirror/addon/scroll/simplescrollbars.css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/toastr/toastr.min.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/plugins/font-awesome/css/all.css"
    /> --> 

    <!-- App CSS -->
    <!-- <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/bootstrap.min.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/core.css?v=5.0"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/components.css?v=1.0"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/icons.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/pages.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/menu.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/wc/static/assets/css/responsive.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://cdn.jsdelivr.net/npm/remixicon@2.2.0/fonts/remixicon.css"
        rel="stylesheet"
    />
    <link rel="stylesheet" href="https://unpkg.com/plyr@3/dist/plyr.css" />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/wc/static/assets/css/video-js-add.css"
    /> -->
</svelte:head>



{#if reportLoading}
    <div class="panel-disabled i-loader">
        <div class="animate__animated animate__zoomIn loader-item-new">
            <img
                src="https://xobinteam.xobin.com/wc/static/assets/images/new-loader.gif"
                alt="xobin_loader"
                class="loader-new"
            />
        </div>
        <h4
            id="atext"
            class="animate__animated animate__zoomIn text-center text-uppercase font-bold m-b-0"
        >
            Please Hold On...
        </h4>
    </div>
{:else if reportNotFound}
    <div class="panel-disabled i-loader">
        <div class="animate__animated animate__zoomIn loader-item-new">
            <img
                src="https://xobinteam.xobin.com/wc/static/assets/images/error_gif.gif"
                alt="xobin_loader"
                class="loader-new"
            />
        </div>
        <h4
            id="atext"
            class="animate__animated animate__zoomIn text-center text-uppercase font-bold m-b-0"
        >
            <b>Broken Link</b>: Report you are trying to get doesn't exist.
        </h4>
    </div>
{:else}
    <div
        class="report justify-content-center"
        style="height:max-content; margin:10%;"
    >
    <button class=" exclude-from-print btn btn-secondary" style="margin-bottom:5%" onclick="history.back()">Back to Dashboard</button>
    <button class="exclude-from-print right-floated btn btn-success" onclick="window.print()"
    >Download Report</button>

        <div class="page1">
            <footer>
                <div class="pdf-nav" style="background-color: #929192;">
                    <img
                        src="{reportData["companyLogo"]}"
                        width="10%"
                        class="company-logo left-floated"
                        alt="CompanyName"
                    />
                    <span class="nav-head right-floated">
                        <h3 class="font-weight-bold">Psychometric Report</h3>
                        <span>Assessment : {reportData.assessmentName}</span>
                    </span>
                </div>
            </footer>

            <div class="report-body">
                <div class="report-header left-floated">
                    <span><h3>Psychometric Report</h3></span>

                    <span> <h4>Assessment: {reportData.assessmentName}</h4></span>

                    <span> Assessment Answered On: {reportData.createdAt} </span>
                </div>

                <div class="report-overview">
                    <div class="table-div">
                        <table class="table table-striped">
                            <thead>
                                <th
                                    class="table-header table-column"
                                    style="color:orange"
                                >
                                    Overview of Competencies / Value Measured
                                </th>
                                <th>
                                    <div class="scale" style="margin-top: 0%;">
                                        <div class="dot" data-label="Bad" />
                                        <div class="dot" data-label="Average" />
                                        <div class="dot" data-label="Good" />
                                        <div
                                            class="dot"
                                            data-label="Excellent"
                                        />
                                        <div class="line" />
                                        <div class="label" />
                                    </div>
                                </th>
                            </thead>
                            <tbody>
                                {#each Object.entries(reportData.categoryWiseResult) as [category, catData]}
                                    <tr>
                                        <td class="table-column">
                                            {category}
                                        </td>

                                        <td>
                                            <div class="scale">

                                                
                                                <span class="{catData.categoryObtainedScore/catData.categoryTotalScore*100<=25 ? 'dot active' : 'dot'}" data-label="Bad"
                                                />
                                                <span
                                                
                                                class="{catData.categoryObtainedScore/catData.categoryTotalScore*100>25 && catData.categoryObtainedScore/catData.categoryTotalScore*100<=50  ? 'dot active' : 'dot'}"
                                                    data-label="Average"
                                                />
                                                <span
                                                class="{catData.categoryObtainedScore/catData.categoryTotalScore*100>50 && catData.categoryObtainedScore/catData.categoryTotalScore*100<=75 ? 'dot active' : 'dot'}"
                                                    data-label="Good"
                                                />
                                                <span
                                                class="{catData.categoryObtainedScore/catData.categoryTotalScore*100>75 && catData.categoryObtainedScore/catData.categoryTotalScore*100<=100 ? 'dot active' : 'dot'}"
                                                    data-label="Excellent"
                                                />
                                                <div class="line" />
                                            </div>
                                        </td>
                                    </tr>
                                {/each}

                                
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="pagebreak"> </div>

        <div class="page3 report-body">
            <span>
                <span style="color:blueviolet; ">
                    <h4>
                        Score of Factors measured under different Competencies /
                        Values
                    </h4></span
                >
                &nbsp;
                <span style="color:#929192">
                    <img
                        class="icon"
                        width="40"
                        height="10"
                        src="https://storage.googleapis.com/svelte_psychometric_static/static/expectedScore.png"
                        alt="Expected Score icon"
                    /> Expected Score
                </span>
                &nbsp; &nbsp;
                <span style="color:#929192">
                    <img
                        class="icon"
                        width="30"
                        src="https://storage.googleapis.com/svelte_psychometric_static/static/favourable_icon.png"
                        alt="favourable icon"
                    /> Favourable
                </span>
                &nbsp; &nbsp;
                <span style="color:#929192">
                    <img
                        class="icon"
                        width="30"
                        src="https://storage.googleapis.com/svelte_psychometric_static/static/LessFavourable_icon.png"
                        alt="LessFavourable icon"
                    /> <u> Less Favourable </u></span
                >
            </span>
            
            {#each Object.entries(reportData.categoryWiseResult) as [category, catData]}
            <div class="detail-comment">
                <div class="comment-header">
                    <div
                        class="left-floated"
                        style="height:13%;background-color: #929192; color:white"
                    >
                        &nbsp;&nbsp; {category} &nbsp;&nbsp;
                    </div>
                    <div
                        class="right-floated"
                        style="height:13%; background-color: #929192; color:white"
                    >
                        &nbsp;&nbsp; 
                        {#if catData.categoryObtainedScore/catData.categoryTotalScore*100<=25}
                        Bad 
                        {:else if catData.categoryObtainedScore/catData.categoryTotalScore*100<=50}
                        Average
                        {:else if catData.categoryObtainedScore/catData.categoryTotalScore*100<=75}
                        Good 
                        {:else}
                        Excellent
                        {/if}
                        &nbsp;&nbsp;
                    </div>
                </div>
                <br />
                {#each Object.entries(catData.categoryTraits) as [traitName,traitData]}
                <div class="trait-comment">
                    <div class="trait-name">
                        <div
                            style="width:30%; margin-left: 25%;border: 1px solid;height:20px;float:right; background: linear-gradient(90deg, white 50%, #34a1eb 50%);"
                        >
                            <svg
                                style="color: red;position:relative; top:-8px; left: {traitData.traitObtainedScore/traitData.traitTotalScore*100}%"
                                xmlns="http://www.w3.org/2000/svg"
                                width="40"
                                height="30"
                                fill="currentColor"
                                class="bi bi-hexagon-fill"
                                viewBox="0 0  16 16"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z"
                                    fill="red"
                                />
                            </svg>
                            <span
                                style="position:relative; top:-30px; left:{traitData.traitObtainedScore/traitData.traitTotalScore*100 - 15}%; margin-botton:1%; font-weight: bold;color: #4CAF50;font-size: 18px;z-index: 1;"
                                >
                                {#if traitData.traitObtainedScore/traitData.traitTotalScore*100<=25}
                                Bad 
                                {:else if traitData.traitObtainedScore/traitData.traitTotalScore*100<=50}
                                Average
                                {:else if traitData.traitObtainedScore/traitData.traitTotalScore*100<=75}
                                Good 
                                {:else}
                                Excellent
                                {/if}

                                </span
                            >
                        </div>
                        <img
                            class="icon"
                            width="20"
                            src="https://storage.googleapis.com/svelte_psychometric_static/static/LessFavourable_icon.png"
                            alt="LessFavourable icon"
                        />
                        <span><b>{traitName}</b></span>
                    </div>
                    <p style="margin:2%;margin-top:1%;">
                        {traitData.traitDescription}
                    </p>
                </div>
                
                {/each}

                
            </div>
            <div class="pagebreak"> </div>
            {/each}
            <br /><br /><br />
            <!-- <div class="" style="float:right;">
                <div class="" style="position: relative;height: 20px;background-color: #4CAF50; border-color:black">
                    <div class="progress" style="position: absolute;top: 0;left: 0;height: 100%;background-color: white;width: 80%; /* Change this to set the progress percentage */"></div>
                    <div class="" style="position: absolute;top: -5px; /* Half the dot height */left: 40%; /* Change this to set the dot position */ width: 20px;height: 20px;">
                    <svg style="color: red" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-hexagon-fill" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M8.5.134a1 1 0 0 0-1 0l-6 3.577a1 1 0 0 0-.5.866v6.846a1 1 0 0 0 .5.866l6 3.577a1 1 0 0 0 1 0l6-3.577a1 1 0 0 0 .5-.866V4.577a1 1 0 0 0-.5-.866L8.5.134z" fill="red"></path> </svg>
                    </div>
                    <div class="text" style="position: absolute; top: -40px;left: 40%; /* Change this to set the text position */text-align: center;font-weight: bold;color: #4CAF50;font-size: 14px;z-index: 1;">Good</div>
                </div>
            </div> -->
        </div>
    </div>
{/if}

<!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->
<!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->
<!-- <div class="p-2 m-2 bg-info text-white shadow rounded-2">Flex item</div> -->

<style>
    .hex .hex-content {
        position: absolute;
        top: 50%;
        left: 50%;

        transform: translate(-50%, -50%) rotate(90deg);

        color: white;
    }

    .container {
        position: relative;
    }

    img.polygon-image {
        /* display: block; */
        /* margin: 2%; */
        margin-top: 2%;
        width: 40%;
        height: auto;
        vertical-align: middle;
    }

    .text-overlay {
        position: relative;
        color: orange;
        text-align: center;
    }

    /* CSS styles for horozontal scales */
    .scale {
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 30px;
        width: 300px;
        margin: auto;
        margin-top: 5%;
        position: relative;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
    }

    .dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #ccc;
        position: relative;
        z-index: 1;
        cursor: pointer;
    }

    .dot.active {
        width: 20px;
        height: 20px;
        background-color: #28a745;
    }

    .line {
        height: 5px;
        width: 100%;
        background-color: #ccc;
        position: absolute;
        top: 12px;
        left: 0;
        z-index: -1;
    }

    .dot:nth-of-type(1) {
        margin-left: 0;
    }

    .dot:last-of-type {
        margin-right: 0;
    }

    .dot.active:not(:last-of-type)::after {
        background-color: #28a745;
    }

    .label {
        position: absolute;
        top: -30px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        width: 80px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

    .dot[data-label="Bad"]::before {
        content: "Bad";
        position: absolute;
        bottom: 20px;
        left: -10px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

    .dot[data-label="Average"]::before {
        content: "Average";
        position: absolute;
        bottom: 20px;
        left: -30px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

    .dot[data-label="Good"]::before {
        content: "Good";
        position: absolute;
        bottom: 20px;
        left: -20px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

    .dot[data-label="Excellent"]::before {
        content: "Excellent";
        position: absolute;
        bottom: 20px;
        left: -30px;
        font-size: 14px;
        font-weight: bold;
        color: #333;
    }

    .dot.active[data-label]::before {
        content: attr(data-label);
        position: absolute;
        top: -30px;
        left: -12px;
        font-size: 16px;
        font-weight: bold;
        color: #28a745;
    }

    @media print {
        @page {
            size: auto; /* Set the page size to auto */
            margin: 0; /* Set the margin to 0 */
        }

        .exclude-from-print {
            visibility: hidden;
        }
    }

    .value-measured-div {
        margin-top: 1%;
        height: 250px;
        /* width:100%; */
        border: 1px solid;
        align-items: center;
        text-align: center;
        vertical-align: middle;
    }

    .detail-comment {
        margin-top: 1%;
        height: 100%;
        /* width:100%; */
        border: 1px solid;
        /* align-items: center; */
        /* text-align: center; */
        /* vertical-align: middle; */
    }

    .trait-name {
        /* float: left; */
        text-decoration: solid;
        margin: 1%;
        margin-top: 3%;
    }

    .pdf-nav {
        background-color: #929192;
        width: 100%;
        max-width: 100%;
        height: 100px;
    }

    .company-logo {
        margin-left: 5%;
        margin-top: 2%;
    }

    .nav-head {
        color: #ffffff;
        margin-right: 5%;
        margin-top: 1%;
        vertical-align: auto;
    }

    .report-body {
        margin: 4%;
        /* background-color: #fffff1; */
        font-size: larger;
    }

    .left-floated {
        float: left;
    }

    .right-floated {
        float: right;
    }

    .report-header {
        /* margin-left: 2%;
        margin-top:1%; */
    }

    .report-result {
        /* margin-top: 5%; */
        /* margin-right:2%; */
        font-stretch: expanded;
        width: 45%;
    }

    .larger-text {
        font-size: larger;
    }

    .report-overview {
        border: 1px dashed;
        border-color: #929192;
        /* display: flex; */
        display: inline-block;
        margin-top: 5%;
        width: 100%;
        /* outline-style:  dashed; */

        /* background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%23333' stroke-width='2' stroke-dasharray='6%2c 14' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e"); */
    }

    .table-div {
        margin: 2%;
        /* text-align: center; */
    }

    .table {
        width: 100%;
        /* align-items: center; */
    }

    .table-header {
        height: 150px;
    }

    .table-column {
        vertical-align: middle;
    }

    /* Xobin loader css */

    .loader-new {
        width: 60px;
        height: 60px;
    }

    .loader-item-new {
        left: calc(50% - 30px);
        position: absolute;
        top: calc(50% - 30px);
    }

    .i-loader {
        position: fixed;
        left: 0px;
        top: 0px;
        width: 100%;
        height: 100%;
        z-index: 9999999;
        background: #fff;
    }

    #atext {
        margin-top: 35vh;
    }
    .pagebreak {
        break-after: page;
      }
</style>
