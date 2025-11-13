from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import psutil
import os

# Cria a aplicação Flask
app = Flask(__name__)
CORS(app)  # permite acesso externo, útil pro Lively ou navegador
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/sys")
def system_status():
    data = {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("G:/").percent if os.path.exists("G:/") else None,
        "battery": psutil.sensors_battery().percent if psutil.sensors_battery() else None
    }
    return jsonify(data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
