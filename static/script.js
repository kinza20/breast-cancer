document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predict-form');
    const inputsContainer = document.querySelector('.inputs');
    const resultDiv = document.getElementById('result');

    // Create input fields dynamically
    featureNames.forEach(name => {
        const label = document.createElement('label');
        label.textContent = name;
        const input = document.createElement('input');
        input.type = 'number';
        input.name = name;
        input.required = true;
        inputsContainer.appendChild(label);
        inputsContainer.appendChild(input);
    });

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {};
        featureNames.forEach(name => {
            data[name] = parseFloat(form.elements[name].value);
        });

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.prediction !== undefined) {
            resultDiv.innerHTML = `
                <h3>Prediction: ${result.prediction === 1 ? "Malignant" : "Benign"}</h3>
                <p>Probability: ${result.probability.map(p => p.toFixed(4)).join(' / ')}</p>
            `;
        } else {
            resultDiv.innerHTML = `<p class="error">${result.error}</p>`;
        }
    });
});
