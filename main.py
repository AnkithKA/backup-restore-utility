from rich.console import Console
from rich.prompt import Prompt
from backup_restore import backup, restore  # Importing the actual functions from backup_restore.py

console = Console()

def main():
    console.print("[bold green]Backup and Restore Utility[/bold green]")

    while True:
        # Ask the user for a choice
        choice = Prompt.ask(
            "Choose an option",
            choices=["1", "2", "3"],
            default="3",
        )

        # Handling the choice selection
        if choice == "1":
            source = Prompt.ask("Enter the source directory")
            dest = Prompt.ask("Enter the destination directory")
            versioning = Prompt.ask("Enable versioning? (yes/no)", choices=["yes", "no"], default="no") == "yes"

            # Call the actual backup function from backup_restore.py
            try:
                backup_file = backup(source, dest, versioning=versioning)
                console.print(f"[bold green]Backup created successfully: {backup_file}[/bold green]")
            except Exception as e:
                console.print(f"[bold red]Error: {e}[/bold red]")

        elif choice == "2":
            backup_file = Prompt.ask("Enter the path to the backup file")
            restore_dir = Prompt.ask("Enter the restore directory")

            # Call the actual restore function from backup_restore.py
            try:
                restore_msg = restore(backup_file, restore_dir)
                console.print(f"[bold green]{restore_msg}[/bold green]")
            except Exception as e:
                console.print(f"[bold red]Error: {e}[/bold red]")

        elif choice == "3":
            console.print("[bold blue]Goodbye![/bold blue]")
            break

if __name__ == "__main__":
    main()
