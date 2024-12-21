from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align
import sys

console = Console()

# Layout initialization
layout = Layout()
layout.split_column(
    Layout(name="header", size=3),
    Layout(name="body"),
    Layout(name="footer", size=3)
)

# Header
layout["header"].update(Panel("🎓 [bold blue]Welcome to CLI-LMS[/bold blue] 🎓", style="bold green"))

# Footer
layout["footer"].update(Panel("[bold]Use the menu to navigate. Type 'exit' to quit.[/bold]", style="bold green"))

def main_menu():
    table = Table(title="Main Menu")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")

    table.add_row("1", "Manage Students")
    table.add_row("2", "Manage Courses")
    table.add_row("3", "Manage Assignments")
    table.add_row("4", "View Reports")
    table.add_row("5", "Send Notifications")

    return table

def display_menu():
    layout["body"].update(Panel(main_menu(), title="Choose an Option"))
    console.print(layout)

def manage_students():
    console.clear()
    console.print(Panel("👩‍🎓 [bold cyan]Student Management[/bold cyan] 👨‍🎓", style="bold blue"))
    console.print("1. Add Student")
    console.print("2. Remove Student")
    console.print("3. List Students")
    console.print("Type 'back' to return to the main menu.")

    while True:
        choice = Prompt.ask("[bold yellow]Select an option[/bold yellow]")
        if choice == 'back':
            break
        console.print(f"[bold green]Option '{choice}' selected.[/bold green] (Not implemented yet)")
    
    console.clear()
    display_menu()

def handle_input(choice):
    if choice == "1":
        manage_students()
    elif choice == "2":
        console.print("[bold green]Manage Courses selected.[/bold green] (Not implemented yet)")
    elif choice == "3":
        console.print("[bold green]Manage Assignments selected.[/bold green] (Not implemented yet)")
    elif choice == "4":
        console.print("[bold green]View Reports selected.[/bold green] (Not implemented yet)")
    elif choice == "5":
        console.print("[bold green]Send Notifications selected.[/bold green] (Not implemented yet)")
    elif choice.lower() in ["exit", "quit"]:
        console.print("[bold red]Exiting LMS. Goodbye![/bold red]")
        sys.exit()
    else:
        console.print("[bold red]Invalid option! Please try again.[/bold red]")

# Main Loop
def run():
    console.clear()
    display_menu()
    while True:
        choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow]")
        handle_input(choice)
        console.clear()
        display_menu()

if __name__ == "__main__":
    run()
