# Microservice-A - A Sound Notification Service
This microservice provides sound file paths based on a requested sound notification. It is designed to support integration with web applications or other services to allow them to request and recieve data (in this case sound file paths) from the service.
# Requesting Data
To request data from this microservice, send a POST request to the "/get_sound" endpoint with a JSON body containing the key "sound_notification" and a valid sound identifier (sound_notification1, 2, or 3) as the value.
**Example Request:**

```JavaScript
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
