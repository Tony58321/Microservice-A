# Microservice-A - A Sound Notification Service
This microservice provides sound file paths based on a requested sound notification. It is designed to support integration with web applications or other services to allow them to request and recieve data (in this case sound file paths) from the service.
## Cautions/Libraries Needed:
Make sure that your folders are formatted in the way listed in the video on the discussion post. It should follow the format:

``` text
Microservice-A/
│
├── microservice-A.py        # Main application file (entry point)
├── static/                  # Folder for static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── sounds/
│       └── audio.mp3
├── templates/               # Folder for HTML templates
│   └── index.html           # Homepage template
```
Also ensure that you install the following libraries that are imported in the Microservice.py file:
### Flask:
``` bash
pip install Flask
```
### flask-cors:
``` bash
pip install flask-cors
```
### requests:
``` bash
pip install requests
```

# Requesting Data:
To request data from this microservice, send a POST request to the "/get_sound" endpoint with a JSON body containing the key "sound_notification" and a valid sound identifier (selectedSound in this case) as the value. The sound identified "selectedSound" is based on the user's choice in a test HTML file included in the video.
## Example Request:
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
## Example Response:
The microservice will then respond with a JSON file path.
``` json
{
    "file_path": "/static/sounds/alert-sound.mp3"
}
```
## Example Call:
After sending the data, convert the response to JSON using ".then(response => response.jsom())" and play the audtio from the returned file path using "new Audio(data.file_path)", as shown below.
``` JavaScript
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
```
# UML Sequence Diagram:
![image](https://github.com/user-attachments/assets/5e10d60b-c89c-446c-8a39-3f6ddbb33866)

