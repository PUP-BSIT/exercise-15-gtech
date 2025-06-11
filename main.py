import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
from gtech.aragon import ChickFlickRecommender
from gtech.dimayuga import RoleplayGame
from gtech.lim import StudentManager
from gtech.lopez import MovieTicket
from gtech.romero import SmartRefrigerator

console = Console()

# Team members list with menu instances
TEAM_MEMBERS_LIST = {
   1: ("Aragon", ChickFlickRecommender()),
   2: ("Dimayuga", RoleplayGame()),
   3: ("Lopez", MovieTicket()),
   4: ("Lim", StudentManager()),
   5: ("Romero", SmartRefrigerator())
}

# Exit option is one number after the last team member
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

      # Call the selected member's menu() method
      instance.menu()
      return True

    console.print("[red]Invalid option. Try again.[/red]")
    input("Press Enter to continue...")
    return True

# Main Menu loop that runs until user chooses to exit
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