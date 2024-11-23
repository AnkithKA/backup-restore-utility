import os
import tarfile
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="logs/backup_restore.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def backup(source_dir, dest_dir, versioning=False):
    """
    Create a backup of the source directory and store it in the destination directory.

    :param source_dir: Path to the source directory
    :param dest_dir: Path to the destination directory where backup will be saved
    :param versioning: Whether to enable versioning (create different backups based on timestamp)
    :return: Path of the created backup file
    """
    # Create a timestamp for the backup file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz" if not versioning else f"backup_{timestamp}_v1.tar.gz"
    backup_path = os.path.join(dest_dir, backup_filename)

    try:
        # Create a tarball backup of the source directory
        with tarfile.open(backup_path, "w:gz") as backup_file:
            backup_file.add(source_dir, arcname=os.path.basename(source_dir))

        logging.info("Backup created successfully: %s", backup_path)  # Log the backup success
        return backup_path

    except Exception as e:
        logging.error("Error during backup: %s", str(e))  # Log any errors during backup
        raise Exception(f"Backup failed: {str(e)}")


def restore(backup_file, restore_dir):
    """
    Restore the contents of the backup file to the specified restore directory.

    :param backup_file: Path to the backup .tar.gz file
    :param restore_dir: Directory to restore the files to
    :return: None
    """
    try:
        # Check if the backup file exists
        if not os.path.exists(backup_file):
            raise Exception(f"Backup file '{backup_file}' does not exist.")

        # Check if the restore directory exists, if not create it
        if not os.path.exists(restore_dir):
            os.makedirs(restore_dir)

        # Extract the backup file into the restore directory
        with tarfile.open(backup_file, "r:gz") as tar:
            tar.extractall(path=restore_dir)

        # Log the success of the restore operation
        logging.info("Restore completed successfully from '%s' to '%s'", backup_file, restore_dir)
        return f"Restore completed successfully in: {restore_dir}"

    except Exception as e:
        # Log any errors during restore
        logging.error("Error during restore: %s", str(e))
        raise Exception(f"Restore failed: {str(e)}")
