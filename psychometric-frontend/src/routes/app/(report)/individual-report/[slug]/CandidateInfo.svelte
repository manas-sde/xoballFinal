<script>
    import { each } from "svelte/internal";

    export let reportData;

    var alltraitsAssessed = [],
        allCoreTraits = Object.keys(reportData["categoryWiseResult"]);
    var excellentBucket = {},
        goodBucket = {},
        averageBucket = {},
        badBucket = {};

    for (let i = 0; i < allCoreTraits.length; i++) {
        alltraitsAssessed = alltraitsAssessed.concat(
            Object.keys(
                reportData["categoryWiseResult"][allCoreTraits[i]][
                    "categoryTraits"
                ]
            )
        );
        let traitAssessed = Object.keys(
            reportData["categoryWiseResult"][allCoreTraits[i]]["categoryTraits"]
        );
        for (let j = 0; j < traitAssessed.length; j++) {
            if (
                reportData["categoryWiseResult"][allCoreTraits[i]][
                    "categoryTraits"
                ][traitAssessed[j]]["scoreBucket"] == "Bad"
            ) {
                badBucket[traitAssessed[j]] =
                    reportData["categoryWiseResult"][allCoreTraits[i]][
                        "categoryTraits"
                    ][traitAssessed[j]]["scorePercentage"];
            } else if (
                reportData["categoryWiseResult"][allCoreTraits[i]][
                    "categoryTraits"
                ][traitAssessed[j]]["scoreBucket"] == "Average"
            ) {
                averageBucket[traitAssessed[j]] =
                    reportData["categoryWiseResult"][allCoreTraits[i]][
                        "categoryTraits"
                    ][traitAssessed[j]]["scorePercentage"];
            } else if (
                reportData["categoryWiseResult"][allCoreTraits[i]][
                    "categoryTraits"
                ][traitAssessed[j]]["scoreBucket"] == "Good"
            ) {
                goodBucket[traitAssessed[j]] =
                    reportData["categoryWiseResult"][allCoreTraits[i]][
                        "categoryTraits"
                    ][traitAssessed[j]]["scorePercentage"];
            } else {
                excellentBucket[traitAssessed[j]] =
                    reportData["categoryWiseResult"][allCoreTraits[i]][
                        "categoryTraits"
                    ][traitAssessed[j]]["scorePercentage"];
            }
        }
    }
</script>

<div class="candidate-info-box">
    <div class="candidate-name-email-box">
        <div class="candidate-name">
            {reportData["candidateName"]}
        </div>
        <div class="candidate-email">
            {reportData["candidateEmail"]}
        </div>
    </div>

    <div class="full-report-basic-info">
        <span class="assessment-name-box">
            <span class="assessment-icon">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="12"
                    height="12"
                    ><path
                        d="M17 2V4H20.0066C20.5552 4 21 4.44495 21 4.9934V21.0066C21 21.5552 20.5551 22 20.0066 22H3.9934C3.44476 22 3 21.5551 3 21.0066V4.9934C3 4.44476 3.44495 4 3.9934 4H7V2H17ZM7 6H5V20H19V6H17V8H7V6ZM9 16V18H7V16H9ZM9 13V15H7V13H9ZM9 10V12H7V10H9ZM15 4H9V6H15V4Z"
                    /></svg
                >
            </span>
            <span class="assessment-name">
                {reportData["assessmentName"]}
            </span>
        </span>

        <div class="separator-circle" />

        <span class="submitted-date-box">
            <span class="submitted-date-icon">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="12"
                    height="12"
                    ><path
                        d="M9 1V3H15V1H17V3H21C21.5523 3 22 3.44772 22 4V20C22 20.5523 21.5523 21 21 21H3C2.44772 21 2 20.5523 2 20V4C2 3.44772 2.44772 3 3 3H7V1H9ZM20 11H4V19H20V11ZM7 5H4V9H20V5H17V7H15V5H9V7H7V5Z"
                    /></svg
                >
            </span>
            <span class="submitted-date">
                Submitted on {reportData["createdAt"]}
            </span>
        </span>

        <div class="separator-circle" />

        <span class="submitted-date-box">
            <span class="submitted-date-icon">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="12"
                    height="12"
                    ><path
                        d="M21.7264 2.95706L16.2732 22.0433C16.1222 22.5718 15.7976 22.5958 15.5561 22.1127L10.9998 13.0002L1.92266 9.36931C1.41298 9.16544 1.41929 8.86034 1.9567 8.6812L21.0429 2.31913C21.5714 2.14297 21.8745 2.43878 21.7264 2.95706ZM19.0351 5.0966L6.81197 9.17097L12.4486 11.4256L15.4893 17.507L19.0351 5.0966Z"
                    /></svg
                >
            </span>
            <span class="submitted-date"> Invited by - Individual email </span>
        </span>
    </div>
    <br />
    <div class="trait-assessed-box">
        <div class="trait-assessed-header">TRAITS ASSESSED</div>
        <div class="trait-assessed-names-outer-box">
            {#each alltraitsAssessed as traitName}
                <div class="trait-assessed-names-inner-box">
                    <div class="trait-assessed-names">
                        {traitName}
                    </div>
                </div>
            {/each}
        </div>
    </div>

    <div class="strength-and-weakness-outer-box">
        <div class="strength-and-weakness-header">STRENGTH & WEAKNESS</div>
        <div class="strength-and-weakness-inner-box">
            <div class="trait-bucket-box">
                <div class="trait-bucket-header-box">
                    <div class="bucket-name-box">
                        <span class="smile-icons">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 16 16"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    fill="#2DC071"
                                />
                                <path
                                    d="M5.4662 11.6603C6.23733 12.0774 7.08115 12.286 7.99766 12.286C8.9205 12.286 9.76432 12.0774 10.5291 11.6603C11.2939 11.2431 11.926 10.6711 12.4254 9.94417C12.4759 9.87464 12.4854 9.80196 12.4538 9.72611C12.4222 9.65026 12.3685 9.59653 12.2926 9.56493C12.2168 9.53332 12.1346 9.55229 12.0461 9.62181C11.6226 9.97578 11.1991 10.2539 10.7756 10.4562C10.3522 10.6521 9.91286 10.7912 9.45776 10.8733C9.00267 10.9492 8.51597 10.9871 7.99766 10.9871C7.47936 10.9871 6.99266 10.9492 6.53757 10.8733C6.08247 10.7912 5.64318 10.6521 5.21969 10.4562C4.80251 10.2539 4.37902 9.97578 3.94921 9.62181C3.86704 9.54596 3.78803 9.52384 3.71218 9.55545C3.63633 9.58705 3.58261 9.64394 3.551 9.72611C3.5194 9.80196 3.52572 9.87464 3.56996 9.94417C4.06931 10.6711 4.70138 11.2431 5.4662 11.6603Z"
                                    fill="white"
                                    stroke="white"
                                    stroke-width="0.3"
                                />
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    stroke="#2DC071"
                                />
                            </svg>
                        </span>
                        <div class="bucket-name">Excellent</div>
                    </div>
                    <div class="bucket-range-box">
                        <div class="bucket-range-text">75.1% - 100%</div>
                    </div>
                </div>

                <div class="bucket-inner-box">
                    {#each Object.entries(excellentBucket) as [traitName, traitPercentage]}
                        <div class="trait-name-box-inside-bucket">
                            <div class="trait-name-inside-bucket">
                                {traitName}
                            </div>

                            <div class="trait-score-box-inside-bucket">
                                <div class="trait-score-text-inside-bucket">
                                    {traitPercentage}%
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>

            <div class="trait-bucket-box">
                <div
                    class="trait-bucket-header-box"
                    style="background: #FFF8DD;"
                >
                    <div class="bucket-name-box" style="background: #FFF8DD;">
                        <span class="smile-icons">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 16 16"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    fill="#FFCC17"
                                />
                                <path
                                    d="M4 9.96731C4 9.84393 4.1317 9.76475 4.24198 9.82008C7.34274 11.3759 8.63549 11.2981 11.7571 9.81379C11.8691 9.76052 12 9.84136 12 9.96541V9.96541C12 10.018 11.9749 10.068 11.9329 10.0996C9.35017 12.0406 7.12705 12.4113 4.06584 10.0989C4.02485 10.0679 4 10.0187 4 9.96731V9.96731Z"
                                    fill="#3C403D"
                                    stroke="#3C403D"
                                    stroke-width="0.3"
                                />
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    stroke="#FFCC17"
                                />
                            </svg>
                        </span>
                        <div class="bucket-name" style="background: #FFF8DD;">
                            Good
                        </div>
                    </div>
                    <div class="bucket-range-box" style="background: #FFF8DD;">
                        <div
                            class="bucket-range-text"
                            style="background: #FFF8DD;"
                        >
                            50.1% - 75%
                        </div>
                    </div>
                </div>

                <div class="bucket-inner-box">
                    {#each Object.entries(goodBucket) as [traitName, traitPercentage]}
                        <div class="trait-name-box-inside-bucket">
                            <div class="trait-name-inside-bucket">
                                {traitName}
                            </div>

                            <div class="trait-score-box-inside-bucket">
                                <div class="trait-score-text-inside-bucket">
                                    {traitPercentage}%
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>

            <div class="trait-bucket-box">
                <div
                    class="trait-bucket-header-box"
                    style="background: #FFF1EE;"
                >
                    <div class="bucket-name-box" style="background: #FFF1EE;">
                        <span class="smile-icons">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 16 16"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    fill="#FF7152"
                                />
                                <path
                                    d="M11.6927 12.0189C10.1345 11.278 9.05627 10.9005 7.99029 10.8903C6.92596 10.8801 5.85388 11.2363 4.30925 12.0113C4.102 12.1152 3.85 11.968 3.85 11.73C3.85 11.6309 3.89746 11.5376 3.97543 11.4787C5.52245 10.3101 6.87679 9.80516 8.18429 9.85311C9.48961 9.90097 10.7207 10.4991 12.023 11.4778C12.1025 11.5375 12.15 11.6319 12.15 11.7319C12.15 11.9688 11.9018 12.1184 11.6927 12.0189Z"
                                    fill="white"
                                    stroke="white"
                                    stroke-width="0.3"
                                />
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    stroke="#FF7152"
                                />
                            </svg>
                        </span>
                        <div class="bucket-name" style="background: #FFF1EE;">
                            Average
                        </div>
                    </div>
                    <div class="bucket-range-box" style="background: #FFF1EE;">
                        <div
                            class="bucket-range-text"
                            style="background: #FFF1EE;"
                        >
                            25.1% - 50%
                        </div>
                    </div>
                </div>

                <div class="bucket-inner-box">
                    {#each Object.entries(averageBucket) as [traitName, traitPercentage]}
                        <div class="trait-name-box-inside-bucket">
                            <div class="trait-name-inside-bucket">
                                {traitName}
                            </div>

                            <div class="trait-score-box-inside-bucket">
                                <div class="trait-score-text-inside-bucket">
                                    {traitPercentage}%
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>

            <div class="trait-bucket-box">
                <div
                    class="trait-bucket-header-box"
                    style="background: #FFEEEE;"
                >
                    <div class="bucket-name-box" style="background: #FFEEEE;">
                        <span class="smile-icons">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 16 16"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    fill="#FF5252"
                                />
                                <rect
                                    x="4"
                                    y="10.8835"
                                    width="8.21574"
                                    height="1.2151"
                                    rx="0.607548"
                                    transform="rotate(-13.2529 4 10.8835)"
                                    fill="white"
                                />
                                <rect
                                    x="0.5"
                                    y="0.5"
                                    width="15"
                                    height="15"
                                    rx="7.5"
                                    stroke="#FF5252"
                                />
                            </svg>
                        </span>
                        <div class="bucket-name" style="background: #FFEEEE;">
                            Bad
                        </div>
                    </div>
                    <div class="bucket-range-box" style="background: #FFEEEE;">
                        <div
                            class="bucket-range-text"
                            style="background: #FFEEEE;"
                        >
                            0% - 25%
                        </div>
                    </div>
                </div>

                <div class="bucket-inner-box">
                    {#each Object.entries(badBucket) as [traitName, traitPercentage]}
                        <div class="trait-name-box-inside-bucket">
                            <div class="trait-name-inside-bucket">
                                {traitName}
                            </div>

                            <div class="trait-score-box-inside-bucket">
                                <div class="trait-score-text-inside-bucket">
                                    {traitPercentage}%
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</div>
<div class="pagebreak" />
