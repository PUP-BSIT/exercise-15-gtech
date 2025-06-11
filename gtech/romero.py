from rich.console import Console
from rich.panel import Panel

console = Console()

class SmartRefrigerator:
    def __init__(self, owner_name):
        # Initialize refrigerator with owner name,
        #  default temperature, and empty item list
        self.owner = owner_name
        self.temperature = 4
        self.items = []

    def add_item(self):
         # Prompt user to add an item to the fridge
        item = input("🔤 Item to add: ")
        self.items.append(item)
        console.print(f"✅ [bold magenta]{item}[/bold magenta] added.")

    def remove_item(self):
        # Prompt user to remove an item from the fridge
        item = input("🔤 Item to remove: ")
        if item in self.items:
            self.items.remove(item)
            console.print(f"🗑️ [bold magenta]{item}[/bold magenta] removed.")
        else:
            console.print(f"⚠️ [bold magenta]{item}[/bold magenta] not found.")

    def list_items(self):
        #Display all current items in the refrigerator
        if self.items:
            console.print("📦 [bold magenta]Items:"
            "[/bold magenta] " + ", ".join(self.items))

        else:
            console.print("📦 [bold magenta]The refrigerator is empty."
            "[/bold magenta]")

    def set_temperature(self):
        #Let user set a new temperature for the refrigerator
        try:
            temp = int(input("🌡️ New temperature (°C): "))
            self.temperature = temp
            console.print(f"🌡️ Set to [bold magenta]{temp}°C[/bold magenta].")
        except ValueError:
            console.print("❌ Enter a valid number.")

    def show_status(self):
        #Display the current status of the refrigerator
        status = f"👤 {self.owner}\n🌡️ {self.temperature}°C\n📦" 
        "{len(self.items)} item(s)"
        console.print(Panel(status, title="📊 Status", style="magenta"))

    def handle_choice(self, choice):
        # Handle the menu selection using match-case
        match choice:
            case "1":
                self.add_item()
            case "2":
                self.remove_item()
            case "3":
                self.list_items()
            case "4":
                self.set_temperature()
            case "5":
                self.show_status()
            case "6":
                console.print("👋 Goodbye!", style="magenta")
                return False
            case _:
                console.print("❗ Try again.", style="magenta")
        return True

def menu():
    # Program entry point and menu loop
    console.print(Panel("Smart Fridge 1.0", style="magenta", expand=False))
    fridge = SmartRefrigerator(input("👤 Your name: "))

    while True:
      # Display menu options line by line
        console.print("[bold magenta]1.[/bold magenta] Add")
        console.print("[bold magenta]2.[/bold magenta] Remove")
        console.print("[bold magenta]3.[/bold magenta] List")
        console.print("[bold magenta]4.[/bold magenta] Temp")
        console.print("[bold magenta]5.[/bold magenta] Status")
        console.print("[bold magenta]6.[/bold magenta] Exit")
        choice = input("👉 Option: ")
        if not fridge.handle_choice(choice):
            break

menu()
