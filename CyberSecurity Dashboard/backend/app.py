from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/logs')
def get_logs():
    logs = ["Log 1", "Log 2", "Log 3"]  # Sample logs
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
