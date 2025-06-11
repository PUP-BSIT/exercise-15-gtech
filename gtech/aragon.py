import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Constants
MAX_RECOMMENDATIONS = 6
MIN_MENU_OPTION = 1 
INDEX_SET = 1 
EXIT_OPTION = "4"
MOVIES = {
    "romantic": {
        "movies": [
            "The Notebook", 
            "How to Lose a Guy in 10 Days", 
            "Notting Hill",
            "10 Things I Hate About You", 
            "Letters to Juliet", 
            "Pretty Woman"
        ],
        "quotes": [
            "I want all of you, forever, you and me, every day.",
            "Can't lose something you never had.",
            "It was nice to meet you. Surreal but nice.",
            "You don't always have to be who they want you to be.",
            "You need only courage to follow your heart.",
            "I want the fairytale."
        ]
    },
    "empowered": {
        "movies": [
            "Legally Blonde", 
            "The First Wives Club", 
            "The Devil Wears Prada", 
            "Hidden Figures"
        ],
        "quotes": [
            "You must always have faith in people and"
            " most importantly, in yourself.",
            "Ladies, you have to be strong and independent.",
            "A driven woman navigates her own path.",
            "Separate and equal are two different things."
        ]
    },
    "feel-good": {
        "movies": [
            "Mamma Mia!", 
            "Clueless", 
            "13 Going on 30",
            "The Princess Diaries", 
            "Bridesmaids"
        ],
        "quotes": [
            "Here we go again, my, my, how can I resist you?",
            "As if!",
            "Thirty, flirty, and thriving.",
            "No one can quit being who they really are.",
            "I think if you're growing, then you're changing."
        ]
    },
    "comedy": {
        "movies": [
            "Mean Girls", 
            "Easy A", 
            "She's the Man", 
            "Uptown Girls"
        ],
        "quotes": [
            "On Wednesdays, we wear pink.",
            "My social life is a comedy of errors.",
            "Nonsense! You don't need a man to wear a"
            " beautiful dress!",
            "Fundamentals are the building blocks of fun."
        ]
    }
}

console = Console()

def clear():
# Clears terminal screen 
    os.system('cls' if os.name == 'nt' else 'clear')

# Main class for the Chick Flick Recommender system
class ChickFlickRecommender:
    def __init__(self):
    # Dictionary to store movie, initializer for user mood recommended movies
        self.movies = MOVIES
        self.user_mood = None
        self.recommendations = []

    def list_moods(self):
    # Lists all available moods that the user can choose from
        if not self.movies:
            console.print("No movie categories loaded.")
            return []
    
        mood_text = Text()
        # Enumerate through each mood and append to the display text
        for index_mood, mood in enumerate(self.movies, INDEX_SET):
            mood_text.append(f"{index_mood}. {mood.capitalize()}\n")

        # Displays all the available moods
        console.print(Panel(mood_text, title="⋆˚࿔ Available Moods ⋆˚࿔",
                            border_style="magenta", expand=True))
        return list(self.movies)

    def set_mood(self):
    # Allows user to select their mood from the available options
        clear()
        available_moods = self.list_moods()
        if not available_moods:
            return

        choice = None
        while choice is None:
            # Get and validate user input until valid
            choice = self.get_user_mood(available_moods)
        # Store the selected mood
        self.confirm_mood(choice, available_moods)

    def get_user_mood(self, moods):
    # Asks user to input a mood choice and validates 
        user_input = console.input(
            f"Select your mood ({MIN_MENU_OPTION}-{len(moods)}): ").strip()
        try:
            choice = int(user_input)
        except ValueError:
            console.print("\n\n[red]Invalid input. Please enter a" 
                          " whole number.[/red]")
            return None
        if not (MIN_MENU_OPTION <= choice <= len(moods)):
            console.print(f"\n\n[red]Enter a number between {MIN_MENU_OPTION}"
                        f" and {len(moods)}.[/red]")
            return None
        return choice

    def confirm_mood(self, choice, moods):
    # Confirms and displays the selected mood
        self.user_mood = moods[choice - INDEX_SET]

        mood_text = Text("Mood set to '")
        mood_text.append(self.user_mood, style="magenta bold")
        mood_text.append("'.")
        console.print(Panel(mood_text, title="⋆˚࿔ Mood Confirmed ⋆˚࿔", 
                            border_style="magenta"))
        input("\nPress ENTER to return to MENU.")

    def recommend_movies(self):
    # Displays recommended movies based on the selected mood
        clear()
        if not self.user_mood:
            self.prompt_mood()
            return

        mood_data = self.movies.get(self.user_mood, {})
        movies = mood_data.get("movies", [])

        if not movies:
            self.no_movies_found()
            return

        # Randomly select up to MAX_RECOMMENDATIONS from the list
        num_movies = min(MAX_RECOMMENDATIONS, len(movies))
        self.recommendations = random.sample(movies, k=num_movies)
        self.display_movie_reco()

    def get_quote(self):
    # Generate random quote based on the user's selected mood
        clear()
        if not self.user_mood:
            self.prompt_mood()
            return

        mood_data = self.movies.get(self.user_mood, {})
        quotes_list = mood_data.get("quotes", [])

        if quotes_list:
            quote = random.choice(quotes_list)
        else:
            quote = "No quote available."
        
        text = Text()
        text.append(f"Here's a chick flick quote for your '", style="bold")
        text.append(f"{self.user_mood}", style="magenta bold")
        text.append("' mood:\n\n", style="bold")
        text.append(f"“{quote}”", style="yellow italic")
        console.print(Panel(text, title="⋆˚࿔ Chick Flick Quote ⋆˚࿔",
                            border_style="magenta", expand=True))
        input("\nPress ENTER to CONTINUE.")

    def prompt_mood(self):
    # Prompts the user to set a mood before accessing certain features
        console.print(Panel(
            "[bold red]Please set your mood first.[/bold red]",
            title="⋆˚࿔ Action Needed ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    def no_movies_found(self):
    # Displays an error message when no movies are found 
        console.print(Panel(
            f"No movies found for the mood '{self.user_mood}'.",
            title="⋆˚࿔ No Movies ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    def display_movie_reco(self):
    # Displays a list of movie recommendations for the current mood
        text = Text()
        text.append("Based on your '", style="")
        text.append(f"{self.user_mood}", style="magenta bold")
        text.append("' mood, here are your recommendations:\n\n", style="")

        for index_movie, movie in enumerate(self.recommendations, INDEX_SET):
            text.append(f"{index_movie}. {movie}\n")

        console.print(Panel(
            text,
            title="⋆˚࿔ Movie Recommendations ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    def return_team(self):
    # Handles return to team menu
        clear()
        console.print("[blue]Thank you for using the Chick Flick Movie "
                      "Recommender! Returning to Team Menu...[/blue]")
        input("\nPress ENTER to return to TEAM MENU.")

    def menu(self):
    # Displays main menu and handles user input
        options = {
            "1": self.set_mood,
            "2": self.recommend_movies,
            "3": self.get_quote,
            EXIT_OPTION: self.return_team
        }

        while True:
            clear()
            self.display_main_menu()
            choice = console.input("Enter your choice: ").strip()
            if self._handle_choice(choice, options):
                break

    def _handle_choice(self, choice, options):
    # Executes the selected menu option
        if choice in options:
            options[choice]()
            return choice == EXIT_OPTION
        self.invalid_choice()
        return False

    def display_main_menu(self):
    # Displays menu options
        console.print(Panel(
            "꩜ .ᐟ Set your mood to generate a chick flick movie"
            " recommendation for you! .☘︎\n\n"
            "[1] Set My Mood\n"
            "[2] Get Movie Recommendations\n"
            "[3] Get a Chick Flick Quote\n"
            "[4] Return to Team Menu",
            title="⋆˚࿔ Althea's Chick Flick Recommender ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))

    def invalid_choice(self):
    # Notifies when the user makes an invalid choice
        console.print(f"\n\n[red]Enter a number between {MIN_MENU_OPTION}"
                      f" and {EXIT_OPTION}.[/red]")
        console.input("\nPress ENTER to try again.")
