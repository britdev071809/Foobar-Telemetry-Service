"""Simple JSON parser for telemetry data."""
import json

def parse_telemetry_json(raw_json):
    """Parse raw JSON string into Python dict.
    
    Note: This function does not perform any schema validation.
    Malformed or malicious JSON could cause issues downstream.
    """
    return json.loads(raw_json)
