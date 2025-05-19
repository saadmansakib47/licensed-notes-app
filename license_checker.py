import requests
from utils import get_device_fingerprint

LICENSE_SERVER_URL = "http://localhost:5000/validate"


def validate_license(license_key):
    device_id = get_device_fingerprint()
    payload = {
        "license_key": license_key,
        "device_id": device_id
    }

    try:
        response = requests.post(LICENSE_SERVER_URL, json=payload)
        data = response.json()
        return data
    except Exception as e:
        return {"status": "error", "message": str(e)}
