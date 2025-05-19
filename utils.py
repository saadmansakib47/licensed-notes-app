import hashlib
import uuid
import platform

def get_device_fingerprint():
    raw_info = f"{platform.node()}-{uuid.getnode()}"
    fingerprint = hashlib.sha256(raw_info.encode()).hexdigest()
    return fingerprint
