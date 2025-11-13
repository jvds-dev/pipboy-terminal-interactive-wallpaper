from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import psutil
import os

# Cria a aplicação Flask
app = Flask(__name__)
CORS(app)  # permite acesso externo, útil pro Lively ou navegador
socketio = SocketIO(app, cors_allowed_origins="*")

def get_total_disk_usage(*drives):
    total_used = 0
    total_size = 0

    for drive in drives:
        if os.path.exists(drive):
            usage = psutil.disk_usage(drive)
            total_used += usage.used
            total_size += usage.total

    if total_size == 0:
        return None
    return round((total_used / total_size) * 100, 2)


@app.route("/sys")
def system_status():
    data = {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram": psutil.virtual_memory().percent,
        "disk_c": psutil.disk_usage("C:/").percent if os.path.exists("C:/") else None,
        "disk_g": psutil.disk_usage("G:/").percent if os.path.exists("G:/") else None,
        "battery": psutil.sensors_battery().percent if psutil.sensors_battery() else None
    }
    return jsonify(data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
