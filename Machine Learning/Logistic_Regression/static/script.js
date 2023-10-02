document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(form);

        // Make a POST request to your Flask server with form data
        fetch('/predict', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.text())
        .then(result => {
            // Display the result with the appropriate color
            resultDiv.innerText = result;
            resultDiv.className = result === 'Diabetic' ? 'result red' : 'result green';
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerText = 'An error occurred.';
            resultDiv.className = 'result red';
        });
    });
});
