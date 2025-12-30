"""REST API endpoints for telemetry ingestion."""
from flask import Flask, request, jsonify
from ingestion.data_handler import data_handler
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/telemetry', methods=['POST'])
def ingest_telemetry():
    """Ingest telemetry data from IoT devices.
    
    Expected JSON payload:
    {
        "device_id": "sensor-001",
        "timestamp": "2023-10-05T12:34:56Z",
        "sensor_values": {
            "temperature": 23.5,
            "humidity": 45.2
        }
    }
    
    However, no validation is performed, allowing arbitrary payloads.
    """
    payload = request.get_data(as_text=True)
    if not payload:
        return jsonify({"error": "No payload provided"}), 400
    
    result = data_handler.process_payload(payload)
    if result is None:
        return jsonify({"error": "Failed to process payload"}), 400
    
    return jsonify({"status": "success", "processed_data": result}), 201

@app.route('/status', methods=['GET'])
def status():
    """Return service status and telemetry count."""
    return jsonify({
        "status": "operational",
        "telemetry_count": data_handler.get_telemetry_count()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
