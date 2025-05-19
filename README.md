license-notes-app/
├── app.py                 # Main app launcher
├── gui.py                 # GUI interface (Tkinter)
├── license_checker.py     # Logic for checking license and device
├── license_server/        # Flask server simulating license validation
│   ├── server.py
│   └── license_data.json  # Stores license info and device fingerprints
└── utils.py               # Common utilities (device ID, hashing, etc.)
