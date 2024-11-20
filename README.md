# Microservice-A - A Sound Notification Service
This microservice provides sound file paths based on a requested sound notification. It is designed to support integration with web applications or other services to allow them to request and recieve data (in this case sound file paths) from the service.
# Requesting Data
To request data from this microservice, send a POST request to the "/get_sound" endpoint with a JSON body containing the key "sound_notification" and a valid sound identifier (sound_notification1, 2, or 3) as the value.
**Example Request:**
import requests

url = 'http://127.0.0.1:5000/get_sound'  # Replace with the hosted URL if applicable
data = {
    "sound_notification": "sound_notification1"
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
