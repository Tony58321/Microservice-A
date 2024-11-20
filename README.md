# Microservice-A - A Sound Notification Service
This microservice provides sound file paths based on a requested sound notification. It is designed to support integration with web applications or other services to allow them to request and recieve data (in this case sound file paths) from the service.
# Requesting Data
To request data from this microservice, send a POST request to the "/get_sound" endpoint with a JSON body containing the key "sound_notification" and a valid sound identifier (sound_notification1, 2, or 3) as the value.
# Example Request:
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

```
# Receiving Data:
The microservice will then respond with a JSON file path.
``` json
{
    "file_path": "/static/sounds/alert-sound.mp3"
}
```
