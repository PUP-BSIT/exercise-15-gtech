import os
from rich.console import Console
from rich.panel import Panel
from rich import box

# Constants
EXIT_OPTION = 6
STYLE_PANEL = "green"
STYLE_MENU = "magenta"
STYLE_ERROR = "red"
STYLE_EXIT = "bold red"

MENU_OPTIONS = [
    "1. Add Item",
    "2. Remove Item",
    "3. List Items",
    "4. Set Temperature",
    "5. Show Status",
    "6. Exit"
]

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class SmartRefrigerator:
    def __init__(self, owner_name = None):
        self.owner = owner_name
        self.temperature = None  # No default temperature
        self.items = []

    def add_item(self):
        clear_screen()
        self.print_panel("Add Item", STYLE_PANEL)
        item = input("Item to add: ")
        self.items.append(item)
        console.print(f"[bold magenta]{item}[/bold magenta] added.")

    def remove_item(self):
        clear_screen()
        self.print_panel("Remove Item", STYLE_PANEL)
        item = input("Item to remove: ")
        if item in self.items:
            self.items.remove(item)
            console.print(f"[bold magenta]{item}[/bold magenta] removed.")
        else:
            console.print(f"[bold magenta]{item}[/bold magenta] not found.",
                           style=STYLE_ERROR)

    def list_items(self):
        clear_screen()
        self.print_panel("List Items", STYLE_PANEL)
        if self.items:
            console.print("[bold magenta]Items:[/bold magenta] " + ", ".
                          join(self.items))
        else:
            console.print("[bold magenta]The refrigerator is empty."
                            "[/bold magenta]")

    def set_temperature(self):
        clear_screen()
        self.print_panel("Set Temperature", STYLE_PANEL)
        try:
            temp = int(input("New temperature (°C): "))
            self.temperature = temp
            console.print(f"Temperature is already set! [bold magenta]")

        except ValueError:
            console.print("Enter a valid number.", style=STYLE_ERROR)

    def show_status(self):
        clear_screen()
        self.print_panel("Fridge Status", STYLE_PANEL)
        temp_display = (
            f"{self.temperature}°C"
            if self.temperature is not None
            else "Not Set"
        )
        status = (
            f"Owner: {self.owner}\n"
            f"Current Temperature: {temp_display}\n"
            f"Items: {len(self.items)}"
        )
        console.print(Panel(status, title="Status", style=STYLE_PANEL))

    def display_menu(self):
        console.print()
        self.print_panel("Fridge Menu", STYLE_MENU)
        for opt in MENU_OPTIONS:
            console.print(f"[cyan]{opt}[/cyan]")

    def evaluate_choice(self, choice):
        actions = {
            1: self.add_item,
            2: self.remove_item,
            3: self.list_items,
            4: self.set_temperature,
            5: self.show_status,
            6: self.exit_program
        }
        action = actions.get(choice)
        if action:
            action()
            return choice != EXIT_OPTION
        console.print("Invalid option. Try again.", style=STYLE_MENU)
        return True

    def exit_program(self):
        clear_screen()
        console.print("Exiting the program... Goodbye!", style=STYLE_EXIT)
        input("Press Enter to return to the main menu...")

    def print_panel(self, text, style=STYLE_PANEL):
        panel = Panel(f"[bold red]{text}[/bold red]", 
                      box=box.ROUNDED, style=style)
        console.print(panel)

    def menu(self):
        clear_screen()
        self.print_panel("Welcome to Smart Fridge", STYLE_PANEL)
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                console.print("Please enter a number.", style=STYLE_ERROR)
                continue
            if not self.evaluate_choice(choice):
                break