from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Simple Flask Application!"

@app.route('/status')
def status():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(debug=True)
