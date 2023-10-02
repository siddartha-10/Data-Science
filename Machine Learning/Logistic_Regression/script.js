document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form values
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = parseFloat(value);
        });

        // Make a POST request to your Flask server
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ data }),
        })
        .then(response => response.text())
        .then(result => {
            // Display the result with the appropriate color
            resultDiv.innerText = result;
            resultDiv.className = result === 'Non-Diabetic' ? 'result green' : 'result red';
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerText = 'An error occurred.';
            resultDiv.className = 'result red';
        });
    });
});
