from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("license_data.json", "r") as f:
    license_data = json.load(f)

@app.route("/validate", methods=["POST"])
def validate_license():
    data = request.json
    license_key = data.get("license_key")
    device_id = data.get("device_id")

    if license_key not in license_data:
        return jsonify({"status": "invalid", "message": "License key not found"}), 403

    license_entry = license_data[license_key]
    used_devices = license_entry["devices"]

    if device_id in used_devices:
        return jsonify({"status": "valid", "message": "Device already registered"})

    if len(used_devices) >= license_entry["max_devices"]:
        return jsonify({"status": "invalid", "message": "Device limit exceeded"}), 403

    # Register this device
    license_entry["devices"].append(device_id)
    with open("license_data.json", "w") as f:
        json.dump(license_data, f, indent=4)

    return jsonify({"status": "valid", "message": "Device registered successfully"})

if __name__ == "__main__":
    app.run(debug=True)
