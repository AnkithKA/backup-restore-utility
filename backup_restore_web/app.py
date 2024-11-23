from flask import Flask, render_template, request, jsonify
import os
import tarfile
from datetime import datetime

app = Flask(__name__)


# Function to perform the backup
def backup(source_dir, dest_dir, versioning=False):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(dest_dir, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as backup_file:
            backup_file.add(source_dir, arcname=os.path.basename(source_dir))
        return backup_path
    except Exception as e:
        return str(e)


# Function to perform the restore
def restore(backup_file, restore_dir):
    try:
        with tarfile.open(backup_file, "r:gz") as tar:
            tar.extractall(path=restore_dir)
        return "Restore completed successfully"
    except Exception as e:
        return str(e)


# Define route for homepage
@app.route("/")
def index():
    return render_template("index.html")


# Define route to handle backup request
@app.route("/backup", methods=["POST"])
def backup_route():
    source_dir = request.form["source_dir"]
    dest_dir = request.form["dest_dir"]
    versioning = request.form["versioning"] == "yes"

    result = backup(source_dir, dest_dir, versioning)
    return jsonify({"message": result})


# Define route to handle restore request
@app.route("/restore", methods=["POST"])
def restore_route():
    backup_file = request.form["backup_file"]
    restore_dir = request.form["restore_dir"]

    result = restore(backup_file, restore_dir)
    return jsonify({"message": result})


if __name__ == "__main__":
    app.run(debug=True)
