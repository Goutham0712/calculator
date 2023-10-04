function calculateBMI() {
    // Get input values
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);

    // Check if the inputs are valid
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
        alert('Please enter valid values for weight and height.');
        return;
    }

    // Calculate BMI
    const bmi = weight / ((height / 100) * (height / 100));

    // Display BMI
    document.getElementById('bmiValue').innerText = bmi.toFixed(2);
}
