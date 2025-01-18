import { marked } from './libs/marked.esm.js';

document.addEventListener("DOMContentLoaded", () => {
    let extractedText = ""; // Variable to store the extracted text
    let description = ""; // Variable to store the description

    document.getElementById("analyseButton").addEventListener("click", () => {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.runtime.sendMessage({ action: "executeScript", tabId: tabs[0].id }, (response) => {
                if (response && response.result) {
                    extractedText = response.result;
                    let resultDiv = document.getElementById("result");
                    let initialInfo = document.getElementById("initialInfo");
                    let analyseButton = document.getElementById("analyseButton");
                    let alternativesButton = document.getElementById("alternativesButton");

                    // Hide initial information and button
                    initialInfo.style.display = "none";
                    analyseButton.style.display = "none";
                    resultDiv.style.display = "block"; // Show the result div

                    // Show loading animation
                    resultDiv.innerHTML = `
                        <div class="loader"></div>
                        <p>Please wait a few seconds, your product is being analysed</p>
                    `;

                    fetch('https://shift-extension.onrender.com/analyse', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ extractedText: extractedText })
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Analysis result received:', data.result);

                        // Parse the result to extract rating, summary, detail, and description
                        const result = JSON.parse(data.result);
                        const rating = result.rating;
                        const summary = result.summary;
                        const detail = result.detail;
                        description = result.description; // Store the description for later use

                        // Log the description for later use
                        console.log("Description at frontend: ", description);

                        // Display the result in the popup
                        resultDiv.innerHTML = `
                            <div class="rating">Rating: ${rating}</div>
                            <div class="summary">Summary: ${summary}</div>
                            <div class="detail">Detail: ${detail}</div>
                        `;

                        // Show the alternatives button
                        alternativesButton.style.display = "block";
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                        resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
                    });
                }
            });
        });
    });

    document.getElementById("alternativesButton").addEventListener("click", () => {
        let resultDiv = document.getElementById("result");
        // Show loading animation while fetching alternatives
        resultDiv.innerHTML = `
            <div class="loader"></div>
            <p>Please give me a minute - just fetching some cool eco-friendly alternatives for you!</p>
        `;

        alternativesButton.style.display = "none";

        // Call the backend API to get alternatives
        fetch('https://shift-extension.onrender.com/alternatives', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: description })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Alternatives received:', data.alternatives);
            // Convert markdown to HTML using marked
            const alternativesHtml = marked(data.alternatives);
            // Display the alternatives in the result div
            resultDiv.innerHTML = `<div class="alternatives">${alternativesHtml}</div>`;
        })
        .catch((error) => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
    });
});