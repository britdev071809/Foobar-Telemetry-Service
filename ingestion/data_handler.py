import json
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles incoming telemetry data from IoT devices."""
    
    def __init__(self):
        self.telemetry_store = []
    
    def process_payload(self, payload_str):
        """Parse and store telemetry payload.
        
        Args:
            payload_str (str): JSON string containing telemetry data.
        
        Returns:
            dict: Parsed telemetry data if successful, None otherwise.
        """
        try:
            # Potential vulnerability: No schema validation, accepts any JSON structure
            data = json.loads(payload_str)
            # No validation of required fields (device_id, timestamp, sensor_values)
            self.telemetry_store.append(data)
            logger.info(f"Processed telemetry from device {data.get('device_id', 'unknown')}")
            return data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON payload: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error processing payload: {e}")
            return None

    def get_telemetry_count(self):
        """Return count of processed telemetry records."""
        return len(self.telemetry_store)

# Global instance for simplicity
data_handler = DataHandler()
