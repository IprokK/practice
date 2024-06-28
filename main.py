from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

emotions = {
    'happy': {'eyes': 'happy', 'mouth': 'smile', 'eyebrows': 'normal'},
    'sad': {'eyes': 'normal', 'mouth': 'frown', 'eyebrows': 'down'},
    'surprised': {'eyes': 'wide', 'mouth': 'open', 'eyebrows': 'raised'},
    'angry': {'eyes': 'normal', 'mouth': 'tight', 'eyebrows': 'angry'},
    'joy_narrow_eyes': {'eyes': 'narrow', 'mouth': 'smile', 'eyebrows': 'normal'},
    'calm': {'eyes': 'half_closed', 'mouth': 'neutral', 'eyebrows': 'relaxed'},
    'squinting': {'eyes': 'squint', 'mouth': 'neutral', 'eyebrows': 'normal'},
    'sleepy': {'eyes': 'closed', 'mouth': 'neutral', 'eyebrows': 'relaxed'},
    'disappointed': {'eyes': 'normal', 'mouth': 'frown', 'eyebrows': 'down'}
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('change_emotion')
def handle_change_emotion(message):
    emotion = message['emotion']
    if emotion in emotions:
        emit('update_face', emotions[emotion], broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
