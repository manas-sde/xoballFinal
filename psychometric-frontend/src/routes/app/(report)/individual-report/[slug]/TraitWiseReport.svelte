{#each Object.entries(allReportData) as [categoryName,categoryData]}
<div class="trait-wise-report">
    <div class="trait-report-header">
        <div class="core-trait-header-box">
            <span class="core-trait-header">
                CORE TRAIT :
            </span>

            <span class="core-trait-name">
                {categoryName}
            </span>            
        </div>

        <div class="sub-trait-count-box">
            SUB TRAITS - {Object.keys(allReportData[categoryName]["categoryTraits"]).length}
        </div>
    </div>

    {#each Object.entries(allReportData[categoryName]["categoryTraits"]) as [traitName,traitData],index}
    <div class="mini-trait-descriptor-outer-box">
        <div class="mini-trait-descriptor-inner-box">
            <div class="mini-trait-report-header-box">
                <span class="mini-trait-name">{traitName}</span>
                <div class="separator-circle"></div>
                <div class="job-fit-box">
                    <img src="/psychometric-staticfiles/reportIcons/{traitData["scoreBucket"].toLowerCase()}_smile.svg" alt="" srcset="">
                </div>
                <div class="trait-bucket">
                    
                        {traitData["scoreBucket"]}
                </div>

                <div class="trait-percent-score">
                    {traitData["scorePercentage"]}%
                </div>
            </div>

            <div class="mini-trait-report-body-box">
                <div class="mini-trait-comment">
                    {traitData["traitComment"]}
                </div>
                <div class="mini-trait-detailed-comment">
                    {traitData["traitDescription"]}
                </div>
            </div>
        </div>
    </div>

    {#if index != Object.keys(allReportData[categoryName]["categoryTraits"]).length-1}
    <div class="trait-report-separator-line"></div>
    {/if}
    {/each}
</div>


<div class="pagebreak"> </div>
{/each}





<script>
    export let allReportData;
</script>