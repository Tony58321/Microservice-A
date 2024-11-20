from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS

app = Flask(__name__)
# Implemented so that there would be no issues with cross origin resource sharing
CORS(app)

# Sound map with relative paths to the sound files in the static folder
sound_map = {
    "sound_notification1": "sounds/bright-electronic-loop-251871.mp3",
    "sound_notification2": "sounds/calm-ringtone-240702.mp3",
    "sound_notification3": "sounds/funny-goat-sound-106396.mp3"
}

@app.route('/')
def serve_html():
    return render_template('test.html')  # Serve/load the HTML page, put in templates folder

# Runs when client sends request to /get_sound URL using POST
@app.route('/get_sound', methods=['POST'])
def get_sound():
    # Get the JSON data from the POST request
    request_data = request.get_json()
    sound_notification = request_data.get("sound_notification") # Gets from user input

    # Fetch the corresponding sound file path
    if sound_notification in sound_map:
        # Return the relative file path to the sound
        file_path = sound_map[sound_notification]
        response = {"file_path": url_for('static', filename=file_path)}
    else:
        response = {"error": "Invalid sound notification"}

    # Return the response as JSON
    return jsonify(response)

# Only runs when this file is executed (can't be imported!)
if __name__ == '__main__':
    print("Flask server is running...")
    app.run(debug=True, host='0.0.0.0', port=5000)
