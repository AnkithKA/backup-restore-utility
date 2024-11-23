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
```
backup_restore_web/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── backup_restore.log    # Log file for operations
├── README.md             # Project documentation
├── backup_restore.py     # Backup and restore logic
├── main.py               # Main program or additional logic
└── requirements.txt      # Required Python packages
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

## How to Use

### Backup
1. Enter the **source directory** and **destination directory**.
2. Enable **versioning** if needed (optional).
3. Click the **Backup** button.
4. Check the **destination directory** for the `.tar.gz` backup file.

### Restore
1. Enter the **path to the backup file**.
2. Enter the **restore directory**.
3. Click the **Restore** button.
4. Verify the **restored files** in the specified directory.

## Logs

All operations (success and failure) are logged in `logs/backup_restore.log`.

To view the logs, run the following command:

```bash
cat logs/backup_restore.log
```
## Conclusion

Thank you for checking out the Backup and Restore Utility project. This tool simplifies the process of backing up and restoring your files with a user-friendly web interface.

Feel free to contribute, report issues, or fork the project to customize it to your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Flask for the lightweight web framework.
- Inspired by simple file management utilities.
