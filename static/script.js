// Timer 
document.getElementById('startTimerButton').addEventListener('click', function() {
    var countdown = 5;  // 5 seconds timer
    var timerElement = document.getElementById('timer');
    
    // Update the countdown every second
    var timerInterval = setInterval(function() {
        countdown--;
        timerElement.textContent = countdown;  // Display the current countdown

        // When countdown reaches 0, stop the timer and play the sound
        if (countdown <= 0) {
            clearInterval(timerInterval);  // Stop the countdown
            playSound();
        }
    }, 1000);  // Update every 1000ms (1 second)
});

function playSound() {
    var selectedSound = document.getElementById('soundSelect').value;  // Get the selected sound option

    // Tells the program to send a request to the microservice
    fetch('http://localhost:5000/get_sound', {
        method: 'POST', // Use POST to request data
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            sound_notification: selectedSound 
        })
    })
    .then(response => response.json()) // Convert response to JSON
    .then(data => {
        if (data.file_path) {
            // Play the audio from the returned file path
            var audio = new Audio(data.file_path);
            audio.play();
        } else {
            console.error('Error:', data.error);
        }
    })
    .catch(error => console.error('Request failed', error));
}
