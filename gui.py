import tkinter as tk
from tkinter import messagebox
from license_checker import validate_license

def start_app():
    def on_submit():
        key = license_input.get()
        result = validate_license(key)
        if result["status"] == "valid":
            root.destroy()
            open_notes()
        else:
            messagebox.showerror("Error", result["message"])

    root = tk.Tk()
    root.title("License Validation")

    tk.Label(root, text="Enter your License Key:").pack(pady=10)
    license_input = tk.Entry(root, width=30)
    license_input.pack(pady=5)

    submit_btn = tk.Button(root, text="Validate", command=on_submit)
    submit_btn.pack(pady=10)

    root.mainloop()

def open_notes():
    app = tk.Tk()
    app.title("Secure Notes")

    text_area = tk.Text(app, width=60, height=20)
    text_area.pack()

    app.mainloop()
