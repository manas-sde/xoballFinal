<script>
    import axios from 'axios';
    import { Modal, Content, Trigger}  from "sv-popup"
    // var resizefunc = [];
    var html_editor = true,
        css_editor = true,
        js_editor = true,
        preview_pane = true,
        output_code='',
        htmlCode="<div id='root'></div>",
        cssCode='',
        jsCode=`/*Do NOT use import statement. \n//React,ReactDOM, useState are already imported.\n//Write a function with name 'Counter' of this component, which return the required output to solve this question.*/\n\nfunction Counter() {\n}`,
        starter_code='',
        questionType='react',
        testResults=[],
        reportID=201,
        evaluateButtonDisabled=false;

    function toggled(element) {
        
        if (element == "html") {
            if (html_editor){
                document.getElementById(element).classList.remove("btn-interact");
                document.getElementById(element).classList.add("btn-ash");
            }
            else{
                document.getElementById(element).classList.remove("btn-ash");
                document.getElementById(element).classList.add("btn-interact");
            }
            html_editor = !html_editor;
        } 
        
        else if (element == "css") {
            if (css_editor){
                document.getElementById(element).classList.remove("btn-interact");
                document.getElementById(element).classList.add("btn-ash");
            }
            else{
                document.getElementById(element).classList.remove("btn-ash");
                document.getElementById(element).classList.add("btn-interact");
            }
            css_editor = !css_editor;
        } 
        
        else if (element == "js") {
            if (js_editor){
                document.getElementById(element).classList.remove("btn-interact");
                document.getElementById(element).classList.add("btn-ash");
            }
            else{
                document.getElementById(element).classList.remove("btn-ash");
                document.getElementById(element).classList.add("btn-interact");
            }
            js_editor = !js_editor;
        }   
    }

    var react_cdn1 = '<script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin\></script\>';
    var react_cdn2 = '<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin\></script\>';
    var babel_script = '<script src="https://unpkg.com/@babel/standalone/babel.min.js" crossorigin\></script\>';
    var renderStatement = `
                            const root = ReactDOM.createRoot(document.getElementById("root"));

                            root.render(<Counter />);
                            const rootElement = document.getElementById("root");
                            console.log('Breakpoint 1');`
    var importStatement = 'const {useState} = React;'

    starter_code = '<!DOCTYPE html><html><head>';
    
    var console_text =`
    <script>
        // console.debug = console.log.bind(console);
        // console.logs = [];
        // console.log = function(){
        //     console.logs.push(Array.from(arguments));
        //     console.stdlog.apply(console, arguments);

        console.log = console.debug;
        <\/script>`

    function saveNPreview() {

        output_code = starter_code + react_cdn1 + react_cdn2 + babel_script + '<style>' + cssCode + '</style>' + '</head>' + '<body>' +  htmlCode + '</body>' + console_text + '<script type="text/babel">' + importStatement + jsCode + renderStatement + '</script\>'   + '</html\>'; 

        console.log(output_code);
        // output_code = htmlCode;

        
    }

    async function evaluateTestCases(){
            evaluateButtonDisabled = true;
            let url = "/frametest/compile-and-evaluate";
            let host;
            if (typeof window !== "undefined") {
                host = window.location.host;
                if (host == "localhost:5173") {
                    url = "http://127.0.0.1:5000" + url;
                } else {
                    url =
                        "https://frametest-backend-aw54llemya-uc.a.run.app" +
                        url;
                }
            }

            let options = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                },
                code: jsCode,
                questionType: questionType,
                reportID: reportID
            };

            var apiResponse = await axios
                .post(url, options)
                .then((response) => {
                    testResults = response.data;
                    console.log(testResults);
                }
            );

            evaluateButtonDisabled = false;

    }

    export let submit = () => {}
    
    function submitCode(){
        submit();

    }


</script>

<svelte:head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
        rel="shortcut icon"
        href="https://xobinteam.xobin.com/static/assets/images/favicon.png"
    />

    <!-- App title -->
    <title>Framework Testing | Frontend</title>

    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css"
    />
    <link
        rel="stylesheet"
        type="text/css"
        href="https://xobinteam.xobin.com/static/assets/plugins/codemirror/lib/codemirror.css"
    />
    <link
        rel="stylesheet"
        href="https://xobinteam.xobin.com/static/assets/plugins/codemirror/addon/scroll/simplescrollbars.css"
    />

    <link
        rel="stylesheet"
        href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/plugins/toastr/toastr.min.css"
        rel="stylesheet"
        type="text/css"
    />

    <!-- App CSS -->
    <link
        href="https://xobinteam.xobin.com/static/assets/css/bootstrap.min.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/core.css?v=5.0"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/components.css?v=1.0"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/icons.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/pages.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/menu.css"
        rel="stylesheet"
        type="text/css"
    />
    <link
        href="https://xobinteam.xobin.com/static/assets/css/responsive.css"
        rel="stylesheet"
        type="text/css"
    />

    <script
        src="https://xobinteam.xobin.com/static/assets/js/modernizr.min.js"
    ></script>

    <!-- jQuery  -->
    <!-- jQuery  -->
    <!-- <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.min.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/bootstrap.min.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/detect.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/fastclick.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.slimscroll.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.blockUI.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/waves.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.nicescroll.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.scrollTo.min.js"
    ></script>
    -->

    <!-- App js -->
    <!-- App js -->
    <!-- <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.core.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/jquery.app.js"
    ></script> -->

    <!-- <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> -->
    <!-- <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script> -->
    <!-- <script
        src="https://xobinteam.xobin.com/static/assets/plugins/toastr/toastr.min.js"
    ></script>  -->

    <!-- <script
        src="https://xobinteam.xobin.com/static/angular/angular.min.js"
        type="text/javascript"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/js/angular-timer-all.min.js"
        type="text/javascript"
    ></script>
    <script
        type="text/javascript"
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/lib/codemirror.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/xml/xml.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/htmlmixed/htmlmixed.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/css/css.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/javascript/javascript.js"
    ></script>
    <script
        src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/addon/scroll/simplescrollbars.js"
    ></script> -->
    <style>
        html,
        body {
            overflow-y: hidden;
        }
        .modal-sign {
            width: 600px !important;
        }

        #options {
            display: flex;
            flex-flow: row wrap;
        }

        #rep {
            flex: 1 1 40%;
            width: 50%;
        }

        #sidebar-menu > ul > li > a.active {
            border-left: 3px solid #71b6f9;
        }

        .i-loader {
            position: fixed;
            left: 0px;
            top: 0px;
            width: 100%;
            height: 100%;
            z-index: 9999;
            background: #fff;
        }

        #atext {
            margin-top: 35vh;
        }

        .topbar-left .company-logo img {
            width: auto;
            height: auto;
            max-width: 200px;
            max-height: 95%;
            vertical-align: middle;
        }

        #wrapper.enlarged .topbar-left .company-logo img {
            max-width: 70px;
        }

        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li > ul {
            display: none;
        }
        #wrapper.enlarged .topbar .logo.n-e {
            display: none;
        }
        #wrapper .topbar .logo.d-e,
        #wrapper.enlarged .topbar .logo.n-e {
            display: none;
        }
        #wrapper .topbar .logo.n-e,
        #wrapper.enlarged .topbar .logo.d-e {
            display: block;
        }
        #wrapper .left.side-menu #sidebar-menu ul > li > a.menu-toggle {
            display: none;
        }
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            ul
            > li
            > a.menu-toggle {
            display: block;
        }
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            ul
            > li:hover
            > a.menu-toggle,
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            ul
            > li
            > a.menu-toggle.subdrop {
            position: relative;
            width: 70px;
            background-color: #f6f6f6 !important;
            color: #71b6f9;
            border-left: 3px solid #f6f6f6;
        }
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            ul
            > li
            > a.menu-toggle.subdrop {
            color: #435966 !important;
        }
        #wrapper.enlarged .user-box .user-img {
            height: 36px;
            width: 36px;
        }
        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li:hover a span {
            animation: none;
        }

        #wrapper.enlarged .left.side-menu #sidebar-menu > ul > li > a {
            padding: 20px 20px;
        }
        #wrapper.enlarged .left.side-menu .label {
            position: relative;
            left: 0px;
            top: 0px;
            padding: 0.6em 0.6em 0.4em !important;
        }

        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            ul
            > li:hover
            > a:hover {
            width: 70px;
        }

        li h4 {
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
            display: block;
        }

        .btn-end {
            padding: 5px 10px !important;
        }

        .CodeMirror {
            width: 100%;
            height: 55vh;
            margin-top: 15px;
            border-top: 1px solid #dddddd;
            border-bottom: 1px solid #dddddd;
        }

        .CodeMirror-vscrollbar {
            z-index: 1;
        }

        #userLiveVideo {
            transform: rotateY(180deg);
            -webkit-transform: rotateY(180deg); /* Safari and Chrome */
            -moz-transform: rotateY(180deg); /* Firefox */
        }

        .p-t-20 {
            padding-top: 20px !important;
            font-size: 14px;
            padding-bottom: 15px !important;
        }

        table.fixed {
            table-layout: fixed;
        }

        .text-ellipsis {
            max-width: 100%;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            width: 90%;
        }

        .section-progress {
            margin-top: 74px;
            margin-bottom: 0px;
            z-index: 99;
            width: 100%;
            position: fixed;
        }

        .progress-indicator {
            margin-top: 22px;
            font-size: 16px;
        }

        .progress-indicator .label {
            padding: 1em 0.9em 1em;
        }

        .topbar .topbar-left,
        .navbar-default {
            border-top: none !important;
        }

        .side-menu,
        #sidebar-menu > ul > li > a {
            background-color: #ffffff !important;
        }

        #sidebar-menu > ul > li > a.active,
        #sidebar-menu > ul > li > a.active:focus,
        #sidebar-menu > ul > li > a.active:hover,
        #sidebar-menu > ul > li > a.active:active,
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            > ul
            > li
            > a.active:active,
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            > ul
            > li
            > a.active:focus {
            background-color: #e8ecef !important;
        }

        #sidebar-menu > ul > li > a.menu-toggle.active,
        #sidebar-menu > ul > li > a.menu-toggle.active:focus,
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            > ul
            > li
            > a.menu-toggle.active:active,
        #wrapper.enlarged
            .left.side-menu
            #sidebar-menu
            > ul
            > li
            > a.menu-toggle.active:focus {
            background-color: #f4f8fb !important;
        }

        .page-title {
            font-size: 16px;
        }

        .problem-stmt,
        .problem-stmt span,
        .problem-stmt p,
        .problem-stmt ul,
        .problem-stmt li {
            color: #3b3e47 !important;
            font-size: 16px !important;
            font-weight: 400 !important;
            line-height: 24px !important;
            font-family: "Roboto", sans-serif !important;
        }

        .problem-stmt h1,
        .problem-stmt h2,
        .problem-stmt h3,
        .problem-stmt h4,
        .problem-stmt h5,
        .problem-stmt h6,
        .problem-stmt h1 span,
        .problem-stmt h2 span,
        .problem-stmt h3 span,
        .problem-stmt h4 span,
        .problem-stmt h5 span,
        .problem-stmt h6 span {
            color: #3b3e47 !important;
            font-weight: 600 !important;
            font-family: "Roboto", sans-serif !important;
            font-size: 18px !important;
        }

        section .CodeMirror {
            width: 100%;
            height: 100%;
            margin-top: 0px;
        }

        #output iframe {
            margin-top: 0px;
            width: 100%;
            height: 100%;
            border: none;
        }

        .code-wrapper {
            position: relative;
            height: 100%;
            margin: 0;
            padding: 0;
        }

        .code-label,
        .q-label {
            background: #f5f5f5;
            color: #333;
            font-size: 14px;
            z-index: 99;
            width: 100%;
            font-weight: 600;
            padding: 0px 10px;
        }

        .code-label {
            position: absolute;
            top: -20px;
            height: 20px;
            line-height: 22px;
            font-size: 12px;
            width: 101%;
        }

        .divider {
            height: 100%;
            padding-left: 0px;
            padding-right: 0px;
            border-right: 1px solid #f5f5f5;
            border-left: 1px solid #f5f5f5;
        }

        .holder {
            display: flex;
            flex-direction: column;
            height: 90vh;
            overflow: hidden;
        }

        .top {
            flex: 0 0 auto;
            margin: 0px;
            padding: 0px;
            height: 60vh;
            max-height: 85vh;
            width: 100%;
        }

        .bottom {
            flex: 1 1 auto;
            padding: 0px 10px;
            min-height: 30vh;
            height: 100%;
            z-index: 999;
        }

        .ui-resizable-s {
            cursor: row-resize;
            background: #333;
            height: 10px;
            z-index: 9999 !important;
        }

        #output {
            background-color: #fff;
        }

        .sep-mark {
            border-width: 1px 0;
            left: 50%;
            margin: 3px 0 0 -10px;
            width: 20px;
            height: 4px;
            position: absolute;
            box-sizing: border-box;
            display: block;
            border-top: 1px solid #ccc;
            border-bottom: 1px solid #ccc;
        }
    </style>
</svelte:head>

<div class="fixed-left p-b-0">
    <!-- <div class="panel-disabled i-loader">
          <div class="loader-item fa fa-spin text-interact-1"></div>
          <h4 id="atext" class="animated zoomIn text-center text-uppercase font-bold m-b-0">Preparing your assessment</h4>
        </div> -->
    <!-- Begin page -->
    <div id="wrapper" class="enlarged">
        <!-- Top Bar Start -->
        <div class="topbar">
            <!-- LOGO -->
            <div class="topbar-left">
                <a href="#nothing" class="logo"
                    ><img
                        src="https://xobinteam.xobin.com/static/dashboardv2/base/images/XobinLogo.png"
                        alt="Company Logo"
                        style="width:65%"
                    /></a
                >
            </div>

            

            <!-- Button mobile view to collapse sidebar menu -->
            <div class="navbar navbar-default" role="navigation">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6">
                            <ul
                                class="nav navbar-nav navbar-left"
                                style="width:100%;"
                            >
                                <li class="p-l-0" style="width:30%;">
                                    <h4 class="page-title">
                                        Live React Editor
                                    </h4>
                                </li>
                                
                                <li>
                                    <Modal basic big={true}>
                                        <Content>
                                          
                                            <p class="lead font-600 text-inverse">
                                                Problem Statement:
                                            </p>
                                            <p class="text-justify">
                                                <strong>React Problem</strong
                                                ><br />
                    
                                                Write code for react component using functinal method for following functionality.
                                                <ul>
                                                    <li>
                                                        Component must conatains heading "Hello World" 
                                                    </li>
                                                    <li>
                                                        Must have one button with testid as "button" (i.e., contains attribute "data-testid="button")
                                                    </li>
                                                    <li>
                                                        Must have one element with testid as "counter" (i.e., contains attribute "data-testid="counter") with initial value as 0.
                                                    </li>
                                                    <li>
                                                        When button gets clicked, the counter element value must gets incremented by 1.
                                                    </li>
                                                    <li>
                                                        One onput field wit data-testid as "input" and one validate button with data-testid as "validate".
                                                    </li>
                                                    <li>
                                                        When validate button gets clicked, it must check if the input field contains number in the range 0 to 100 or not.
                                                    </li>
                                                    <li>
                                                        There have to be one element with data-testid as "error", which contains the error message if validation of input field fails.
                                                    </li>
                                                    <li>
                                                        If validation fails, the error message have to be "Please enter a number between 0 and 100.", otherwise it have to blank string.
                                                    </li>
                                                </ul>
                                            
                                        </Content>
                                        <Trigger>
                                          <button class="text-interact-1 m-t-10 font-600">View Question</button>
                                        </Trigger>
                                    </Modal>
                                    
                                </li>
                            </ul>
                        </div>
                        <div>
                            <!-- Right(Notification and Searchbox -->
                            <ul class="nav navbar-nav navbar-right">
                                a
                                <li class="m-r-10 m-t-20">
                                    <div class="btn-group">
                                        <button
                                            type="button"
                                            id = "html"
                                            on:click={() => toggled("html")}
                                            class="btn btn-interact btn-sm waves-effect waves-light"
                                            >HTML</button
                                        >
                                        <button
                                            type="button"
                                            id="css"
                                            on:click={() => toggled("css")}
                                            class="btn btn-interact btn-sm waves-effect waves-light"
                                            >CSS</button
                                        >
                                        <button
                                            type="button"
                                            id="js"
                                            on:click={() => toggled("js")}
                                            class="btn btn-interact btn-sm waves-effect waves-light"
                                            >Javascript</button
                                        >
                                        
                                    </div>
                                </li>
                                <li class="m-r-10">
                                    <a
                                        href="#nothing"
                                        on:click={saveNPreview}
                                        class="btn btn-success btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600"
                                        >Save & Preview</a>
                                </li>
                                <button
                                    on:click={evaluateTestCases} disabled={evaluateButtonDisabled}
                                    class="btn btn-primary btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600">
                                    Evaluate Test Cases
                                </button>
                                <button
                                        on:click={submitCode}
                                        class="btn btn-danger btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600">
                                        Submit Code
                                </button>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- end container -->
            </div>
            <!-- end navbar -->
        </div>

        <!-- ========== Left Sidebar Start ========== -->
        <div class="left side-menu">
            <div class="sidebar-inner slimscrollleft">
                <div
                    class="panel-disabled1 question-holder"
                    style="display:none"
                >
                    <div class="loader-1" />
                </div>
                <!--- Sidemenu -->
                <div id="sidebar-menu">
                    <ul />
                    <div class="clearfix" />
                </div>
                <!-- Sidebar -->
                <div class="clearfix" />
            </div>
        </div>
        <!-- Left Sidebar End -->
        <!-- Top Bar End -->

        <!-- ============================================================== -->
        <!-- Start right Content here -->
        <!-- ============================================================== -->
        <div class="content-page">
            <!-- Start content -->
            <div class="content p-0">
                <div class="container p-0">
                    <div class="holder">
                        <div class="row m-t-20 top">
                            {#if html_editor}
                                <div class="col-lg-4 divider">
                                    <section
                                        id="html"
                                        class="code-wrapper"
                                    >
                                        <div class="code-label">HTML</div>
                                        <textarea
                                            bind:value={htmlCode}
                                            id="html_editor"
                                            style="width:100%; height:100%"
                                            class="code-editor m-t-20"
                                        />
                                    </section>
                                </div>
                            {/if}

                            {#if css_editor}
                                <div
                                    class="col-lg-4 divider"
                                >
                                    <section
                                        
                                        id="css"
                                        class="code-wrapper"
                                    >
                                        <div class="code-label">CSS</div>
                                        <textarea
                                            bind:value={cssCode}
                                            id="css_editor"
                                            style="width:100%; height:100%"
                                            class="code-editor m-t-20"
                                        />
                                    </section>
                                </div>
                            {/if}

                            {#if js_editor}
                                <div
                                    class="col-lg-4 divider"

                                >
                                    <section
                                        id="js"
                                        class="code-wrapper"
                                    >
                                        <div class="code-label">
                                            React Script
                                        </div>
                                        <textarea
                                            bind:value={jsCode}
                                            id="js_editor"
                                            style="width:100%; height:100%"
                                            class="code-editor m-t-20"
                                            default = "//Do NOT use import statement. React,ReactDOM, useState are already imported.\n//Write a function with name 'Counter' of this component, which return the required output to solve this question."
                                        />
                                    </section>
                                </div>
                            {/if}
                        </div>


                        

                        {#if preview_pane}
                        <div class="row m-b-10 bottom" style="overflow:auto">
                            <div
                                class="col-xs-12 p-0"
                                style="border: 1px solid #f5f5f5;height:100%"
                            >
                                <section
                                    id="output"
                                    class="code-wrapper"

                                    
                                >
                                <div class="container">
                                    <div class="row">
                                        <div class="col-xs-6">
                                            <div class="q-label m-t-5">Test cases</div>
                                                <ul>
                                                {#each testResults as res}
                                                <li>{res}</li>
                                                {/each}
                                                </ul>
                                        </div>
                                        <div class="col-xs-6">
                                            <div class="q-label m-t-5">Output Window</div>
                                            <iframe title="Preview" srcdoc="{output_code}"/>
                                        </div>
                                    </div>
                                </div>
                                
                                    
                                </section>
                            </div>

                            

                            
                        </div>

                        
                        {/if}
                    </div>
                </div>
                <!-- container -->
            </div>
            <!-- content -->
        </div>
        <!-- End content-page -->
    </div>
    <!-- END wrapper -->

    
    <div
        id="qmodal"
        class="modal fade br-r-0"
        tabindex="-1"
        role="dialog"
        aria-labelledby="qmodal"
        aria-hidden="true"
    >
        <div class="modal-dialog" style="width:95%;">
            <div
                class="modal-content p-20"
                style="border-color: transparent !important;"
            >
                <div class="row">
                    <div class="col-md-4 col-xs-12">
                        <p class="lead font-600 text-inverse">
                            Problem Statement:
                        </p>
                        <p class="text-justify">
                            <strong>React Problem</strong
                            ><br />

                            Write component code for react that alters background color between white and orange on button click.
                        </p>
                        <p class="text-justify">
                            Instruction - You have to create a button inside an div with id "app".
                        </p>
                    </div>
                    <div class="col-md-8 col-xs-12">
                     
                        <center>
                            
                            <br /><button
                                data-dismiss="modal"
                                class="btn btn-interact btn-lg w-lg waves-effect waves-dark m-t-20"
                                >Solve Challenge</button
                            >
                        </center>
                    </div>
                </div>
            </div>
        </div>
    </div>

    </div>
