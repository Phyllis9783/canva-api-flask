from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Canva API Integration</h1><p>This is a simple Flask app for Canva API integration.</p>"

@app.route('/api/status')
def status():
    return jsonify({"status": "running", "message": "Flask app is working for Canva API."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
