
    <svelte:head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="shortcut icon" href="https://xobinteam.xobin.com/static/assets/images/favicon.png">

        <!-- App title -->
        <title>Live HTML Editor | Interact</title>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
        <link rel="stylesheet" type="text/css" href="https://xobinteam.xobin.com/static/assets/plugins/codemirror/lib/codemirror.css">
        <link rel="stylesheet" href="https://xobinteam.xobin.com/static/assets/plugins/codemirror/addon/scroll/simplescrollbars.css">

        <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
        <link href="https://xobinteam.xobin.com/static/assets/plugins/toastr/toastr.min.css" rel="stylesheet" type="text/css" />

        <!-- App CSS -->
        <link href="https://xobinteam.xobin.com/static/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/core.css?v=5.0" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/components.css?v=1.0" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/icons.css" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/pages.css" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/menu.css" rel="stylesheet" type="text/css" />
        <link href="https://xobinteam.xobin.com/static/assets/css/responsive.css" rel="stylesheet" type="text/css" />

       
        
        <script src="https://xobinteam.xobin.com/static/assets/js/modernizr.min.js"></script>
        <style>
        html,body{
          overflow-y: hidden;
        }
        .modal-sign{
          width: 600px !important;
        }

        #options{
          display: flex;
          flex-flow: row wrap;
        }

        #rep{
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

        #atext{
          margin-top: 35vh;
        }

        .topbar-left .company-logo img{
          width: auto;
          height: auto;
          max-width: 200px;
          max-height: 95%;
          vertical-align: middle;
        }

        #wrapper.enlarged .topbar-left .company-logo img{
          max-width: 70px;
        }

        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li > ul {
          display: none;
        }
        #wrapper.enlarged .topbar .logo.n-e{
          display: none;
        }
        #wrapper .topbar .logo.d-e,#wrapper.enlarged .topbar .logo.n-e{
          display: none;
        }
        #wrapper .topbar .logo.n-e,#wrapper.enlarged .topbar .logo.d-e{
          display: block;
        }
        #wrapper .left.side-menu #sidebar-menu ul > li > a.menu-toggle {
          display: none;
        }
        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li > a.menu-toggle {
          display: block;
        }
        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li:hover > a.menu-toggle,#wrapper.enlarged .left.side-menu #sidebar-menu ul > li > a.menu-toggle.subdrop {
          position: relative;
          width: 70px;
          background-color: #F6F6F6 !important;
          color: #71b6f9;
          border-left: 3px solid #F6F6F6;
        }
        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li > a.menu-toggle.subdrop{
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
        #wrapper.enlarged .left.side-menu .label{
          position: relative;
          left: 0px;
          top: 0px;
          padding: .6em .6em .4em !important;
        }

        #wrapper.enlarged .left.side-menu #sidebar-menu ul > li:hover > a:hover{
          width: 70px;
        }

        li h4{
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
          display: block;
        }

        .btn-end{
          padding: 5px 10px !important;
        }

        .CodeMirror{
          width: 100%;
          height: 55vh;
          margin-top: 15px;
          border-top: 1px solid #dddddd;
          border-bottom: 1px solid #dddddd;
        }

        .CodeMirror-vscrollbar{
          z-index: 1;
        }

        #userLiveVideo{
          transform: rotateY(180deg);
          -webkit-transform:rotateY(180deg); /* Safari and Chrome */
          -moz-transform:rotateY(180deg); /* Firefox */
        }

        .p-t-20{
          padding-top: 20px !important;
          font-size: 14px;
          padding-bottom: 15px !important;
        }

        table.fixed{
          table-layout: fixed;
        }

        .text-ellipsis{
          max-width: 100%;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          width: 90%;
        }

        .section-progress{
          margin-top: 74px;
          margin-bottom: 0px;
          z-index: 99;
          width: 100%;
          position: fixed;
        }

        .progress-indicator{
          margin-top: 22px;
          font-size: 16px;
        }

        .progress-indicator .label{
          padding: 1em .9em 1em;
        }

        .topbar .topbar-left, .navbar-default{
          border-top: none !important;
        }

        .side-menu, #sidebar-menu > ul > li > a {
          background-color: #ffffff !important;
        }

        #sidebar-menu > ul > li > a.active,#sidebar-menu > ul > li > a.active:focus,
        #sidebar-menu > ul > li > a.active:hover,#sidebar-menu > ul > li > a.active:active,
        #wrapper.enlarged .left.side-menu #sidebar-menu > ul > li > a.active:active,
        #wrapper.enlarged .left.side-menu #sidebar-menu > ul > li > a.active:focus{
          background-color: #e8ecef !important;
        }

        #sidebar-menu > ul > li > a.menu-toggle.active,#sidebar-menu > ul > li > a.menu-toggle.active:focus,
        #wrapper.enlarged .left.side-menu #sidebar-menu > ul > li > a.menu-toggle.active:active,
        #wrapper.enlarged .left.side-menu #sidebar-menu > ul > li > a.menu-toggle.active:focus{
          background-color: #f4f8fb !important;
        }

        .page-title {
          font-size: 16px;
        }

        .problem-stmt,.problem-stmt span, .problem-stmt p, .problem-stmt ul, .problem-stmt li{
          color: #3b3e47 !important;
          font-size: 16px !important;
          font-weight: 400 !important;
          line-height: 24px !important;
          font-family: 'Roboto', sans-serif !important;
        }

        .problem-stmt h1, .problem-stmt h2, .problem-stmt h3, .problem-stmt h4, .problem-stmt h5, .problem-stmt h6,
        .problem-stmt h1 span, .problem-stmt h2 span, .problem-stmt h3 span, .problem-stmt h4 span, .problem-stmt h5 span, .problem-stmt h6 span{
          color: #3b3e47 !important;
          font-weight: 600 !important;
          font-family: 'Roboto', sans-serif !important;
          font-size: 18px !important;
        }

        section .CodeMirror{
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

        .code-wrapper{
          position: relative;
          height: 100%;
          margin: 0;
          padding: 0
        }

        .code-label,.q-label{
          background: #f5f5f5;
          color: #333;
          font-size: 14px;
          z-index: 99;
          width: 100%;
          font-weight: 600;
          padding: 0px 10px;
        }

        .code-label{
          position: absolute;
          top: -20px;
          height: 20px;
          line-height: 22px;
          font-size: 12px;
          width: 101%;
        }

        .divider{
          height: 100%;
          padding-left: 0px;
          padding-right: 0px;
          border-right: 1px solid #f5f5f5;
          border-left: 1px solid #f5f5f5;
        }

        .holder{
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

        .bottom{
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

        #output{
          background-color: #fff;
        }

        .sep-mark{
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


    <body class="fixed-left p-b-0">
        <div class="panel-disabled i-loader">
          <div class="loader-item fa fa-spin text-interact-1"></div>
          <h4 id="atext" class="animated zoomIn text-center text-uppercase font-bold m-b-0">Preparing your assessment</h4>
        </div>
        <!-- Begin page -->
        <div id="wrapper" class="enlarged">

            <!-- Top Bar Start -->
            <div class="topbar">

              <!-- LOGO -->
              <div class="topbar-left">
              
                <a href="" class="logo"><img src="https://xobinteam.xobin.com/static/dashboardv2/base/images/XobinLogo.png" style="width:65%" /></a>
              
              </div>

              <!-- Button mobile view to collapse sidebar menu -->
              <div class="navbar navbar-default" role="navigation">
                  <div class="container">
                    <div class="row">
                      <div class="col-md-6">
                        <ul class="nav navbar-nav navbar-left" style="width:100%;">
                            <li class="p-l-0" style="width:30%;">
                                <h4 class="page-title">Live HTML Editor</h4>
                            </li>
                            <li class="text-center task-timer-holder">
                              <a href="" id="task-timer" class="m-t-10 animated flash" style="font-size:16px;">
                                <i class="zmdi zmdi-timer text-inverse"></i>&nbsp;&nbsp;
                                <timer max-time-unit="'minute'" interval="1000" class="font-600">25 m : 30s</timer>
                                &nbsp;elapsed
                              </a>
                            </li>
                            <li>
                              <a href="" class="text-interact-1 m-t-10 font-600" data-toggle="modal" data-target="#qmodal">View Question</a>
                            </li>
                        </ul>
                      </div>
                      <div>

                        <!-- Right(Notification and Searchbox -->
                        <ul ng-cloak class="nav navbar-nav navbar-right">
                            <li class="m-r-10 m-t-20">
                              <div class="btn-group">
                                <button type="button" ng-click="toggle('html')" class="btn btn-ash btn-sm waves-effect waves-light" ng-class="{ 'btn-ash':  e_html==false, 'btn-interact': e_html==true  }">HTML</button>
                                <button type="button" ng-click="toggle('css')" class="btn btn-ash btn-sm waves-effect waves-light" ng-class="{ 'btn-ash':  e_css==false, 'btn-interact': e_css==true  }">CSS</button>
                                <button type="button" ng-click="toggle('js')" class="btn btn-interact btn-sm waves-effect waves-light" ng-class="{ 'btn-ash':  e_js==false, 'btn-interact': e_js==true  }">Javascript</button>
                                <button type="button" ng-click="toggle('output')" class="btn btn-interact btn-sm waves-effect waves-light" ng-class="{ 'btn-ash':  e_output==false, 'btn-interact': e_output==true  }">Output</button>
                              </div>
                            </li>
                            <li class="m-r-10">
                              <a href="" ng-click="render($event)" class="btn btn-ash btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600">Run</a>
                            </li>
                            <li class="m-r-10">
                              <a href="" ng-click="check($event)" class="btn btn-ash btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600">Check</a>
                            </li>
                            <li class="m-r-10">
                              <a href="" ng-click="submit($event)" class="btn btn-ash btn-end btn-sm waves-effect waves-light m-t-20 w-xs m-b-0 font-600">Submit</a>
                            </li>
                        </ul>
                      </div>
                    </div>
                  </div><!-- end container -->
              </div><!-- end navbar -->
            </div>
            <!-- ========== Left Sidebar Start ========== -->
            <div class="left side-menu">
                <div class="sidebar-inner slimscrollleft">
                  <div class="panel-disabled1 question-holder" style="display:none"><div class="loader-1"></div></div>
                  <!--- Sidemenu -->
                    <div id="sidebar-menu">
                        <ul ng-cloak>

                        </ul>
                        <div class="clearfix"></div>
                    </div>
                    <!-- Sidebar -->
                    <div class="clearfix"></div>

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
                          <div class="col-lg-4 divider" ng-show="e_html==true">
                            <section id="html" class="code-wrapper" ng-show="e_html==true">
                              <div class="code-label">HTML</div>
                              <textarea id="html_editor" class="code-editor m-t-20">
<script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>

<div class="appContainer"></div>
<div class="spacer" style="clear: both;"></div>
<div class="input">
	<p id="bWidth">Width: <span></span></p>
  <p id="bHeight">Height: <span></span></p>
</div>
<div class="output">
	<p id="marioMoves">Total Moves: <span>0</span></p>
</div>
                              </textarea>
                            </section>
                          </div>
                          <div class="col-lg-4 divider" ng-show="e_css==true">
                            <section id="css" class="code-wrapper" ng-show="e_css==true">
                              <div class="code-label">CSS</div>
                              <textarea id="css_editor" class="code-editor m-t-20"></textarea>
                            </section>
                          </div>
                          <div class="col-lg-4 divider" ng-show="e_js==true">
                            <section id="js" class="code-wrapper" ng-show="e_js==true">
                              <div class="code-label">Javascript</div>
                              <textarea id="js_editor" class="code-editor m-t-20"></textarea>
                            </section>
                          </div>
                        </div>
                        <div class="row m-b-10 bottom">
                          <div class="col-xs-12 p-0" style="border: 1px solid #f5f5f5;height:100%">
                            <section id="output" class="code-wrapper" ng-show="e_output==true">
                              <div class="q-label m-t-5">Result</div>
                        		  <iframe></iframe>
                        	  </section>
                          </div>
                        </div>
                      </div>
                    </div> <!-- container -->
                </div> <!-- content -->

            </div>
            <!-- End content-page -->



        </div>
        <!-- END wrapper -->

        <div id="qmodal" class="modal fade br-r-0" tabindex="-1" role="dialog" aria-labelledby="qmodal" aria-hidden="true" style="display: none;">
          <div class="modal-dialog" style="width:95%;">
              <div class="modal-content p-20" style="border-color: transparent !important;">
                <div class="row">
                  <div class="col-md-4 col-xs-12">
                    <p class="lead font-600 text-inverse">Problem Statement:</p>
                    <p class="text-justify">
                    <strong>Design a maze with following rules,</strong><br>

                    1. Maze is divided into cells with custom width and height (Already Implemented).

                    2. Each cell of the maze can be either empty or Food for Mario (Already Implemented).
                    </p>
                    <p class="text-justify">
                    <strong>To Be Implemented:</strong><br>

                    1. Mario will be starting from a random cell once any of the direction arrow is pressed.

                    2. Mario should start moving cell by cell in the current direction.

                    3. If he hits the boundary of the maze he will get reflected in the opposite direction from which he is coming from.

                    4. He eats the food when he visits a cell which is having food.

                    5. The food will vanish once he collects it. Use arrows to change the direction. Count the total number of moves to collect all the food.
                    </p>
                    <p class="text-justify">
                    <strong>Constraints</strong><br>

                    A. 2 <= boardWidth, boardHeight <= 20.

                    B. Cells with food is generated automatically.

                    C. Not a single line to be changed from the existing code.
                    </p>
                  </div>
                  <div class="col-md-8 col-xs-12">
                    <p class="lead font-600 text-inverse m-l-10">Required Output:</p>
                    <center>
                      <iframe width="560" height="315" src="https://www.youtube.com/embed/tYBIeFLRCsc?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
                      <br><button data-dismiss="modal" class="btn btn-interact btn-lg w-lg waves-effect waves-dark m-t-20">Solve Challenge</button>
                    </center>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div id="omodal" class="modal fade br-r-0" tabindex="-1" role="dialog" aria-labelledby="omodal" aria-hidden="true" style="display: none;">
            <div class="modal-dialog" style="width:65%;">
                <div class="modal-content p-20" style="border-color: transparent !important;">
                  <div class="row">
                    <div class="col-xs-12">
                      <p class="lead font-600 text-inverse">Result</p>
                      <table id="testcases" class="table nowrap dataTable no-footer" cellspacing="0" width="100%" role="grid" style="width: 100%;">
                        <thead>
                          <tr role="row">
                            <th class="sorting_disabled" rowspan="1" colspan="1" >#</th>
                            <th class="sorting_disabled" rowspan="1" colspan="1" >Name</th>
                            <th class="sorting_disabled" rowspan="1" colspan="1" >Condition Checked</th>
                            <th class="sorting_disabled" rowspan="1" colspan="1" >Status</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr role="row" ng-if="!equals({}, tresult)" ng-repeat="(condition, status) in tresult track by $index">
                            <td class="p-t-15">
                              {a $index+1 a}
                            </td>
                            <td class="p-t-15">
                              Test Case {a $index a}
                            </td>
                            <td class="p-t-15">
                              <span class="text-capitalize">{a condition a}</span>
                            </td>
                            <td class="p-t-15">
                              <span class="text-interact-1 font-600" ng-if="status=='p'"><i class="fa-spin zmdi zmdi-refresh-sync"></i> Processing</span>
                              <span class="text-success font-600" ng-if="status==true"><i class="zmdi zmdi-check"></i> Passed</span>
                              <span class="text-danger font-600" ng-if="status==false"><i class="zmdi zmdi-close"></i> Failed</span>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <center>
                        <button ng-click="submit($event)" ng-if="checking==false" class="btn btn-ash btn-lg w-lg waves-effect waves-light">Submit</button>
                      </center>
                    </div>
                  </div>
                </div>
              </div>
            </div>

        <script>
            var resizefunc = [];
        </script>

        <!-- jQuery  -->
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.min.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/bootstrap.min.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/detect.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/fastclick.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.slimscroll.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.blockUI.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/waves.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.nicescroll.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.scrollTo.min.js"></script>

        <!-- App js -->
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.core.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/jquery.app.js"></script>

        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/toastr/toastr.min.js"></script>

        <script src="https://xobinteam.xobin.com/static/angular/angular.min.js" type="text/javascript"></script>
        <script src="https://xobinteam.xobin.com/static/assets/js/angular-timer-all.min.js" type="text/javascript"></script>
        <script type="text/javascript" src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/lib/codemirror.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/xml/xml.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/htmlmixed/htmlmixed.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/css/css.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/mode/javascript/javascript.js"></script>
        <script src="https://xobinteam.xobin.com/static/assets/plugins/codemirror/addon/scroll/simplescrollbars.js"></script>

        