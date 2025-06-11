import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()

# Constants
TEAM_MEMBERS_LIST = {
   1: ("Aragon", None),
   2: ("Dimayuga", None),
   3: ("Lopez", None),
   4: ("Lim", None),
   5: ("Romero", None)
}

EXIT_OPTION = max(TEAM_MEMBERS_LIST.keys()) + 1

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

def display_menu():
      print_title("[bold yellow]Welcome to GTech's Main Menu![/bold yellow]")
      for key, (name, _) in TEAM_MEMBERS_LIST.items():
         console.print(f"[green]{key}. {name}")
      console.print(f"[green]{EXIT_OPTION}. Exit")

def handle_choice(choice):
   # Guard clause for exit option
    if choice == EXIT_OPTION:
      clear_screen()
      console.print("[bold red]Exiting program... Goodbye![/bold red]")
      return False

   # Handle valid team member selections
    if choice in TEAM_MEMBERS_LIST:
      name, instance = TEAM_MEMBERS_LIST[choice]

      if not instance:
         console.print(f"[blue]{name} has no module linked yet.[/blue]")
         input("Press Enter to return to the menu...")
         return True

      instance.menu()
      return True

   # Default case for invalid input
    console.print("[red]Invalid option. Try again.[/red]")
    input("Press Enter to continue...")
    return True

def main():
   running = True
   while running:
      clear_screen()
      display_menu()
      try:
         user_input = int(input("Select a team member or exit: "))
      except ValueError:
         console.print("[red]Please enter a valid number.[/red]")
         input("Press Enter to continue...")
         continue
      running = handle_choice(user_input)

main()

# TO DO:
# Create a module with your last name as the module name.
# - dimayuga
# - lim
# - lopez

# TO DO:
# Create a class with at least 5 methods (excluding constructor) and
# 3 properties. The implementation is up to you.

# TO DO:
# Add an additional method called 'menu()' that will display and access all
# the 5 methods. Make sure it goes back to the main menu.

# TO DO:
# Keep in mind the Coding Guidelines.