import os
from rich.console import Console
from rich.panel import Panel
from rich import box

# Constants
TICKET_PRICE = 300
PANEL_WIDTH = 35
MENU_EXIT_OPTION = 6
TICKET_QUANTI = 0

STYLE_PANEL = "green"
STYLE_MENU = "magenta"
STYLE_ERROR = "red"
STYLE_EXIT = "bold red"

MOVIE_LIST = {
   "1": "Inception",
   "2": "The Matrix",
   "3": "Interstellar",
   "4": "Wicked",
   "5": "Citizen Kane"
}

MENU_OPTIONS = [
   "1. Show Movies",
   "2. Book Ticket",
   "3. Cancel Ticket",
   "4. View Bookings",
   "5. Purchased Tickets",
   "6. Exit"
]

console = Console()

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

class MovieTicket:
    #Constructor
    def __init__(self):
        # Properties
        # Initializes movie list, booking storage, and ticket price
        self.available_movies = MOVIE_LIST
        self.booked_tickets = {}
        self.ticket_price = TICKET_PRICE

    # Displays all available movies
    def show_movies(self):
        clear_screen()
        self.print_panel("Available Movies:", STYLE_PANEL)
        for key, movie in self.available_movies.items():
            console.print(f"[bold]{key}.[/bold] {movie}")

    # Handles the booking process
    def book_ticket(self):
        clear_screen()
        self.show_movies()
        self.print_panel("Booking Ticket:", STYLE_PANEL)
        choice = input("Enter movie number: ")
        if choice not in self.available_movies:
            console.print("Invalid movie selection.", style=STYLE_ERROR)
            return
        name = input("Enter your name: ")
        quantity = self.get_ticket_quantity()
        if quantity:
            self.booked_tickets[name] = (self.available_movies[choice], quantity)
            movie = self.available_movies[choice]
            console.print(f"Ticket(s) booked for [bold magenta]{name} to watch"
                       f" [yellow]{movie}[/yellow]. Quantity: {quantity}")

    # Gets and validates ticket quantity
    def get_ticket_quantity(self):
        #Error Handling of Ticket Quantity
        try:
         qty = int(input("Enter number of tickets: "))
         if qty > TICKET_QUANTI:
            return qty
        except ValueError:
         pass
        console.print("Invalid number of tickets.", style=STYLE_ERROR)
        return None

    # Cancels a booked ticket/s
    def cancel_ticket(self):
        clear_screen()
        self.print_panel("Ticket Cancellation:", STYLE_PANEL)
        name = input("Name for cancellation: ")
        if name in self.booked_tickets:
            movie, _ = self.booked_tickets.pop(name)
            console.print(f"Cancelled ticket for [bold magenta]{name}"
                       f" to watch [bold yellow]{movie}[/bold yellow].")
        else:
         console.print("No ticket found for this name.", style=STYLE_ERROR)

    # Displays all current bookings
    def view_bookings(self):
        clear_screen()
        self.print_panel("View Bookings:", STYLE_PANEL)
        if not self.booked_tickets:
            console.print("No tickets booked.")
            return
        console.print("[bold magenta]Bookings:[/bold magenta]")
        for name, (movie, qty) in self.booked_tickets.items():
         console.print(f"{name} -> {movie} (x{qty})")

    # Calculates and displays total cost for each user
    def calculate_total(self):
        clear_screen()
        self.print_panel("Purchased Tickets:", STYLE_PANEL)
        if not self.booked_tickets:
            console.print("No tickets have been purchased.")
            return
        for name, (movie, qty) in self.booked_tickets.items():
            total_price = qty * self.ticket_price
            console.print(f"[bold]{name}[/bold] --- [yellow]{movie}[/yellow]"
                       f" --- ₱{total_price:.2f}")

    # Shows the main menu options
    def display_menu(self):
        console.print()
        self.print_panel("Movies Menu:", STYLE_MENU)
        for opt in MENU_OPTIONS:
            console.print(f"[cyan]{opt}[/cyan]")

    # Matches user's menu choice to the right option
    def evaluate_choice(self, choice):
        actions = {
            1: self.show_movies,
            2: self.book_ticket,
            3: self.cancel_ticket,
            4: self.view_bookings,
            5: self.calculate_total,
            6: self.exit_program
        }
        action = actions.get(choice)
        if action:
            action()
            return choice != MENU_EXIT_OPTION
        console.print("Invalid option. Try again.", style=STYLE_MENU)
        return True

    # Handles program exit/return to main menu
    def exit_program(self):
        clear_screen()
        console.print("Exiting the program... Goodbye!", style=STYLE_EXIT)
        input("Press Enter to return to the main menu...")

    # Method for consistent panel design
    def print_panel(self, text, style=STYLE_PANEL):
        panel = Panel(f"[bold red]{text}[/bold red]", box=box.ROUNDED,
                    style=style, width=PANEL_WIDTH)
        console.print(panel)

    # Controls the main loop of the movie ticketing system
    def menu(self):
        clear_screen()
        self.print_panel("Hello! Welcome to the Movies!", STYLE_PANEL)
        while True:
         self.display_menu()
         
         #Error Handling of Menu Input/s
         try:
            choice = int(input("Enter your choice: "))
         except ValueError:
            console.print("Please enter a number.", style=STYLE_ERROR)
            continue
         if not self.evaluate_choice(choice):
            break