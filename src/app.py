from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route("/api/v1/details")
def details():
    return "<h1>Hello World!</h1>"

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! I am the robot coming for you!',
        "another message": "Another message for you!",
        "third message": "More message!",
        "forth message": "yet another message",
    })

@app.route('/api/v1/healthz')
def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")