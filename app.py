from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
import uuid

app = Flask(__name__)

# Local data paths
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.json")
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")

# Ensure necessary directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Initialize inventory.json if it doesn't exist
if not os.path.exists(INVENTORY_FILE):
    with open(INVENTORY_FILE, "w") as file:
        json.dump({"items": []}, file, indent=4)

# Route to serve the frontend
@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

# API: Fetch inventory items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    with open(INVENTORY_FILE, "r") as file:
        inventory = json.load(file)
    return jsonify(inventory), 200

# API: Add a new inventory item
@app.route("/inventory", methods=["POST"])
def add_inventory():
    new_item = request.json
    new_item["id"] = str(uuid.uuid4())  # Generate a unique ID for the item
    with open(INVENTORY_FILE, "r+") as file:
        inventory = json.load(file)
        inventory["items"].append(new_item)
        file.seek(0)
        json.dump(inventory, file, indent=4)
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

# API: Update an existing inventory item
@app.route("/inventory/<item_name>", methods=["PUT"])
def update_inventory(item_name):
    updated_data = request.json
    with open(INVENTORY_FILE, "r+") as file:
        inventory = json.load(file)
        for item in inventory["items"]:
            if item["name"] == item_name:
                item.update(updated_data)
                file.seek(0)
                json.dump(inventory, file, indent=4)
                return jsonify({"message": f"{item_name} updated successfully"}), 200
    return jsonify({"error": "Item not found"}), 404

# API: Delete an inventory item
@app.route("/inventory/<item_name>", methods=["DELETE"])
def delete_inventory(item_name):
    with open(INVENTORY_FILE, "r+") as file:
        inventory = json.load(file)
        inventory["items"] = [item for item in inventory["items"] if item["name"] != item_name]
        file.seek(0)
        file.truncate()  # Clear the file before writing new data
        json.dump(inventory, file, indent=4)
    return jsonify({"message": f"{item_name} deleted successfully"}), 200

# API: Upload contract
@app.route("/upload", methods=["POST"])
def upload_contract():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_DIR, filename))
    return jsonify({"message": f"{filename} uploaded successfully to local storage"}), 201

# API: Download contract
@app.route("/download/<filename>", methods=["GET"])
def download_contract(filename):
    try:
        return send_from_directory(directory=UPLOAD_DIR, path=filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
