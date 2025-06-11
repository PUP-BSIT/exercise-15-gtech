import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_title(text):
    panel = Panel(
        Align.center(text, vertical="middle"),
        border_style="magenta",
        width=40,
        box=box.ROUNDED
    )
    console.print(panel)


def main():
   while True:
        clear_screen()
        print_title("[bold yellow]Welcome to GTech's Main Menu![/bold yellow]")
        console.print("[green]1. Aragon")
        console.print("[green]2. Dimayuga")
        console.print("[green]3. Lopez")
        console.print("[green]4. Lim")
        console.print("[green]5. Romero")
        console.print("[green]6. Exit")

        #Error Handling of Input/s
        try:
         choice = int(input("Select a team member or exit: "))
        except ValueError:
         print("Please enter a valid number.")
         continue

        match choice:
         case 1:
            pass
         case 2:
            pass
         case 3:
            pass
         case 4:
            pass
         case 5:
            pass
         case 6:
            clear_screen()
            console.print("[bold red]Exiting program... Goodbye!")
            break
         case _:
            print("Invalid option. Try again.")

main()

# TO DO:
# Create a module with your last name as the module name.
# - aragon
# - dimayuga
# - lim
# - lopez
# - romero

# TO DO:
# Create a class with at least 5 methods (excluding constructor) and
# 3 properties. The implementation is up to you.

# TO DO:
# Add an additional method called 'menu()' that will display and access all
# the 5 methods. Make sure it goes back to the main menu.

# TO DO:
# Keep in mind the Coding Guidelines.