<textarea bind:value={inputCode} on:input={renderOutput}></textarea>

<iframe src="" title="VueCode" srcdoc={htmlcode} frameborder="2">

</iframe>


<script>
    var htmlcode='',inputCode='';
    // inputCode=htmlcode;
    // console.log(inputCode);

    function renderOutput(){
        htmlcode = inputCode;
    console.log(inputCode);

    }
</script>