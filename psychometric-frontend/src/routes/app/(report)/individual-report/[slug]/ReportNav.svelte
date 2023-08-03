<div class="report-nav-box">
    <div class="nav-back-button d-print-none">
        <button class="nav-back-button-text" on:click={() => history.back()}>
            <div class="back-arrow-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7.82843 10.9999H20V12.9999H7.82843L13.1924 18.3638L11.7782 19.778L4 11.9999L11.7782 4.22168L13.1924 5.63589L7.82843 10.9999Z"></path></svg>
            </div>
            Back to all reports
        </button>
    </div>
    <div class="nav-assessment-name">
        {assessmentName}
    </div>

    <div class="nav-right-section d-print-none">
        <div class="print-button-box" on:click={() => window.print()} on:keyup={() => true}>
            <div class="print-button-text">
                <div class="print-button-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17 2C17.5523 2 18 2.44772 18 3V7H21C21.5523 7 22 7.44772 22 8V18C22 18.5523 21.5523 19 21 19H18V21C18 21.5523 17.5523 22 17 22H7C6.44772 22 6 21.5523 6 21V19H3C2.44772 19 2 18.5523 2 18V8C2 7.44772 2.44772 7 3 7H6V3C6 2.44772 6.44772 2 7 2H17ZM16 17H8V20H16V17ZM20 9H4V17H6V16C6 15.4477 6.44772 15 7 15H17C17.5523 15 18 15.4477 18 16V17H20V9ZM8 10V12H5V10H8ZM16 4H8V7H16V4Z"></path></svg>
                </div>
                Print report
            </div>
        </div>

        <div class="download-button-box" aria-disabled="{disabledButton}" on:click={() => window.print()} on:keyup={() => true}>
            <div class="download-button-text">
                <div class="download-button-icon">
                    <svg style="background-color: #0075FF;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 10H18L12 16L6 10H11V3H13V10ZM4 19H20V12H22V20C22 20.5523 21.5523 21 21 21H3C2.44772 21 2 20.5523 2 20V12H4V19Z"></path></svg>
                </div>
                Download report
            </div>
        </div>
    </div>
</div>



<script>
    import html2canvas from 'html2canvas';
    import jsPDF from 'jspdf';
    var disabledButton=false;
    export let assessmentName = '';
    function generatePDF() {

        disabledButton = true;
      // Create a new jsPDF instance
      const doc = new jsPDF();
  
      // Use html2canvas library to convert the HTML body to canvas
      html2canvas(document.body).then(function(canvas) {
  
        // Add the canvas image to the PDF document
        const imgData = canvas.toDataURL('image/png');
        doc.addImage(imgData, 'PNG', 0, 0, doc.internal.pageSize.width, doc.internal.pageSize.height);
  
        // Save the PDF file
        doc.save('webpage.pdf');
        disabledButton=false;
      });
    }
  </script>
  
  