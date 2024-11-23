# Backup and Restore Utility

A user-friendly **Backup and Restore Utility** built with **Python** and **Flask**, featuring a simple web interface for creating, restoring, and managing backups. The utility supports versioning, making it ideal for both personal and professional data management.

---

## Features
- **Backup Creation**:
  - Compresses a directory into a `.tar.gz` file for storage efficiency.
  - Supports optional versioning to prevent overwriting of previous backups.
- **Restore Functionality**:
  - Extracts data from a backup file to a specified directory.
- **Web Interface**:
  - Intuitive web interface built with HTML and CSS.
  - Allows users to input source and destination directories, enable versioning, and restore backups easily.
- **Logging**:
  - Tracks all backup and restore operations in a `backup_restore.log` file for transparency and debugging.

---

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, and JavaScript
- **Compression**: Python's `tarfile` module for `.tar.gz` operations

---

## Project Structure
```php
backup_restore_project/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── static/
│   └── styles.css        # Styling for the web interface
├── logs/
│   └── backup_restore.log # Log file for operations
└── README.md             # Project documentation
```

## Getting Started

### 1. Prerequisites
- Python 3.8+ installed.
- Flask library installed. Install Flask by running:
  ```bash
  pip install flask
### 2. Clone the Repository
```bash
git clone https://github.com/your-username/backup-restore-utility.git
cd backup-restore-utility
```
### 3. Run the Application
- Start the Flask server:
```bash
python app.py
```
### 4. Access the Web Interface
Open your browser and navigate to:
http://127.0.0.1:5000


