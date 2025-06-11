import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Constants
MAX_RECOMMENDATIONS = 6
MIN_MENU_OPTION = 1 
INDEX_SET = 1 
EXIT_OPTION = "5"

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
            "You must always have faith in people and most"
            " importantly, in yourself.",
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

CHARACTERS = {
    "romantic": [
        "Noah Calhoun (The Notebook)",
        "Andie Anderson (How to Lose a Guy in 10 Days)",
        "Anna Scott (Notting Hill)",
        "Kat Stratford (10 Things I Hate About You)",
        "Juliet (Letters to Juliet)",
        "Vivian Ward (Pretty Woman)"
    ],
    "empowered": [
        "Elle Woods (Legally Blonde)",
        "Annie (The First Wives Club)",
        "Miranda Priestly (The Devil Wears Prada)",
        "Katherine Johnson (Hidden Figures)"
    ],
    "feel-good": [
        "Donna Sheridan (Mamma Mia!)",
        "Cher Horowitz (Clueless)",
        "Jenna Rink (13 Going on 30)",
        "Mia Thermopolis (The Princess Diaries)",
        "Annie Walker (Bridesmaids)"
    ],
    "comedy": [
        "Regina George (Mean Girls)",
        "Olive Penderghast (Easy A)",
        "Viola Hastings (She's the Man)",
        "Ray Schleine (Uptown Girls)"
    ]
}

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main class for the Chick Flick Recommender system
class ChickFlickRecommender:
    def __init__(self):
        self.movies = MOVIES
        self.characters = CHARACTERS
        self.user_mood = None
        self.recommendations = []

    # Lists all available moods that the user can choose from
    def list_moods(self):
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

    # Allows user to select their mood from the available options
    def set_mood(self):
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

    # Asks user to input a mood choice and validates 
    def get_user_mood(self, moods):
        user_input = console.input(
        f"Select your mood ({MIN_MENU_OPTION}-{len(moods)}): ").strip()
        try:
            choice = int(user_input)
        except ValueError:
            console.print("\n\n[red]Invalid input. Please enter " 
                            " a whole number.[/red]")
            return None
        if not (MIN_MENU_OPTION <= choice <= len(moods)):
            console.print(f"\n\n[red]Enter a number between {MIN_MENU_OPTION}"
                          f" and {len(moods)}.[/red]")
            return None
        return choice

    # Confirms and displays the selected mood
    def confirm_mood(self, choice, moods):
        self.user_mood = moods[choice - INDEX_SET]

        mood_text = Text("Mood set to '")
        mood_text.append(self.user_mood, style="magenta bold")
        mood_text.append("'.")
        console.print(Panel(mood_text, title="⋆˚࿔ Mood Confirmed ⋆˚࿔", 
                      border_style="magenta"))
        input("\nPress ENTER to return to MENU.")

    # Displays recommended movies based on the selected mood
    def recommend_movies(self):
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

    # Generate random quote based on the user's selected mood
    def get_quote(self):
        clear()
        if not self.user_mood:
            self.prompt_mood()
            return
        
        mood_data = self.movies.get(self.user_mood, {})
        quotes_list = mood_data.get("quotes", [])

        quote = random.choice(quotes_list) 
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

    # Prompts the user to set a mood before accessing certain features
    def prompt_mood(self):
        console.print(Panel(
            "[bold red]Please set your mood first.[/bold red]",
            title="⋆˚࿔ Action Needed ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    # Displays an error message when no movies are found 
    def no_movies_found(self):
        console.print(Panel(
            f"No movies found for the mood '{self.user_mood}'.",
            title="⋆˚࿔ No Movies ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    # Displays a list of movie recommendations for the current mood
    def display_movie_reco(self):
        text = Text()
        text.append("Based on your '", style="")
        text.append(f"{self.user_mood}", style="magenta bold")
        text.append("' mood, here are your recommendations:\n\n", style="")

        for index_movie, movie in enumerate(self.recommendations, INDEX_SET):
            text.append(f"{index_movie}. {movie}\n")
        console.print(Panel(text, title="⋆˚࿔ Movie Recommendations ⋆˚࿔", 
                      border_style="magenta", expand=True))
        input("\nPress ENTER to return to MENU.")

    # Allows to generate a random character based on the user's mood
    def generate_character(self):
        clear()
        if not self.user_mood:
            self.prompt_mood()
            return
        
        # Get characters list based on the user's mood
        mood_characters = self.characters.get(self.user_mood, [])

        if not mood_characters:
            console.print(Panel(
            f"No characters found for the mood '{self.user_mood}'.",
            title="⋆˚࿔ No Characters ⋆˚࿔", border_style="magenta", expand=True)
            )
            input("\nPress ENTER to return to MENU.")
            return
        
        # Randomly choose a character from the list
        character = random.choice(mood_characters)

        text = Text()
        text.append("You are chick flick character is..\n\n", style="bold")
        text.append(f" {character} ", style="magenta bold italic")
        console.print(Panel(
                text, title="⋆˚࿔ Your Chick Flick Character ⋆˚࿔", 
                border_style="magenta", expand=True))
        input("\nPress ENTER to return to MENU.")

    # Handles return to team menu
    def return_team(self):
        clear()
        console.print("[blue]Thank you for using the Chick Flick Movie" 
                    " Recommender! Returning to Team Menu...[/blue]")
        input("\nPress ENTER to return to TEAM MENU.")

    # Displays menu options
    def display_main_menu(self):
        menu_text = Text()
        menu_text.append("1. Set Mood\n")
        menu_text.append("2. Get Movie Recommendations\n")
        menu_text.append("3. Get a Chick Flick Quote\n")
        menu_text.append("4. Get a Chick Flick Character\n")
        menu_text.append("5. Return to Team Menu\n")
        console.print(Panel(menu_text, title="⋆˚࿔ Main Menu ⋆˚࿔", 
                    border_style="magenta", expand=True))

    # Executes the selected menu option
    def handle_choice(self, choice, options):
        if choice in options:
            options[choice]()
            return choice == EXIT_OPTION
        self.invalid_choice()
        return False

    # Notifies when the user makes an invalid choice
    def invalid_choice(self):
        console.print("[red]Invalid option. Please try again.[/red]")
        input("\nPress ENTER to continue.")

    # Displays main menu and handles user input
    def menu(self):
        options = {
            "1": self.set_mood,
            "2": self.recommend_movies,
            "3": self.get_quote,
            "4": self.generate_character,
            EXIT_OPTION: self.return_team
        }
        while True:
            clear()
            self.display_main_menu()
            choice = console.input("Enter your choice: ").strip()
            if self.handle_choice(choice, options):
                break