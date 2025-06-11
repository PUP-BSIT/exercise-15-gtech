import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Constants
MAX_RECOMMENDATIONS = 6

# Menu option constants
OPTION_SET_MOOD = '1'
OPTION_GET_RECOMMENDATIONS = '2'
OPTION_GET_QUOTE = '3'
OPTION_RETURN = '4'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main class for the Chick Flick Recommender system
class ChickFlickRecommender:
    def __init__(self):
    # Dictionaries to store movie, mood, and recommended movies
        self.movies = {}
        self.user_mood = None
        self.recommendations = []

    def load_movies(self):
    # Method 1: Loads predefined movie titles and quotes
        self.movies = {
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

    def list_moods(self):
    # Method 2: Lists all available moods that the user can choose from
        if not self.movies:
            console.print("No movie categories loaded.")
            return []

        mood_text = Text()
        for index_mood, mood in enumerate(self.movies.keys(), start=1):
            mood_text.append(f"{index_mood}. {mood.capitalize()}\n")

        # Displays all the available moods 
        console.print(Panel(mood_text, title="⋆˚࿔ Available Moods ⋆˚࿔", 
                      border_style="magenta", expand=True))
        return list(self.movies.keys())

    def set_mood(self):
    # Method 3: Allows user to select their mood from the available options
        clear()
        available_moods = self.list_moods()
        if not available_moods:
            return

        while True:
        # Prompts the user to select a mood from the list and validate input
            try:
                user_input = console.input(f"Select your mood (1-{len
                            (available_moods)}): ").strip()
                choice = int(user_input)

                # Display confirmation
                if 1 <= choice <= len(available_moods):
                    self.user_mood = available_moods[choice - 1]
                    mood_text = Text("Mood set to '", style="")
                    mood_text.append(self.user_mood, style="magenta bold")
                    mood_text.append("'.", style="")

                    console.print(Panel(
                    mood_text,
                    title="⋆˚࿔ Mood Confirmed ⋆˚࿔",
                    border_style="magenta",
                ))
                    input("\nPress ENTER to return to MENU.")
                    break
                else:
                    console.print(
                    f"\n\n[red]Enter a number between 1 and "
                    f"{len(available_moods)}.[/red]"
                )
            except ValueError:
                console.print("\n\n[red]Invalid input. Please enter a" 
                             " whole number.[/red]")
                input("Press ENTER to return to MENU.")

    def recommend_movies(self):
    # Method 4: Provides movie recommendations based on the user's mood
        clear()
        # If mood not set, prompts the user to set a mood
        if not self.user_mood:
            console.print(Panel(
                "[bold red]Please set your mood first.[/bold red]",
                title="⋆˚࿔ Action Needed ⋆˚࿔",
                border_style="magenta",
                expand=True
            ))
            input("\nPress ENTER to return to MENU.")
            return

        # Get movie list from the mood data 
        mood_data = self.movies.get(self.user_mood, {})
        movies = mood_data.get("movies", [])

        # Displays if no movies found
        if not movies:
            console.print(Panel(
                f"No movies found for the mood '{self.user_mood}'.",
                title="⋆˚࿔ No Movies ⋆˚࿔",
                border_style="magenta",
                expand=True
            ))
            input("\nPress ENTER to return to MENU.")
            return

        # Randomly selects movie recommendations up to MAX_RECOMMENDATIONS
        self.recommendations = random.sample(movies, k=min
                            (MAX_RECOMMENDATIONS, len(movies)))
        
        # Display recommended movie based on the user's mood
        text = Text()
        text.append("Based on your '", style="")
        text.append(f"{self.user_mood}", style="magenta bold")
        text.append("' mood, here are your recommendations:\n\n", style="")

        for index_reco, movie in enumerate(self.recommendations, start=1):
            text.append(f"{index_reco}. {movie}\n")
                
        console.print(Panel(
            text,
            title="⋆˚࿔ Movie Recommendations ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to return to MENU.")

    def get_chick_flick_quote(self):
    # Method 5: Displays a randomly selected chick flick quote 
    # that matches the user's mood
        clear()
        # If mood not set, prompts the user to set a mood 
        if not self.user_mood:
            console.print(Panel(
                "[bold red]Please set your mood first.[/bold red]",
                title="⋆˚࿔ Action Needed ⋆˚࿔",
                border_style="magenta",
                expand=True
            ))
            input("\nPress ENTER to return to MENU.")
            return
        
        # Generate a random quote based on the user's mood
        quotes = self.movies.get(self.user_mood, {}).get("quotes", [])
        quote = random.choice(quotes)

        text = Text()
        text.append(f"Here's a chick flick quote for your '", style="bold")
        text.append(f"{self.user_mood}", style="magenta bold")
        text.append("' mood:\n\n", style="bold")
        text.append(f"“{quote}”", style="yellow italic")

        console.print(Panel(
            text,
            title="⋆˚࿔ Chick Flick Quote ⋆˚࿔",
            border_style="magenta",
            expand=True
        ))
        input("\nPress ENTER to CONTINUE.")

    def menu(self):
    # Main menu that loops until the user decides to return to the team menu
        while True:
            clear()
            # Display menu options
            menu = (
                "꩜ .ᐟ Set your mood to generate a chick flick movie" 
                        " recommendation for you! .☘︎\n\n"
                f"[{OPTION_SET_MOOD}] Set My Mood\n"
                f"[{OPTION_GET_RECOMMENDATIONS}] Get Movie Recommendations\n"
                f"[{OPTION_GET_QUOTE}] Get a Chick Flick Quote\n"
                f"[{OPTION_RETURN}] Return to Team Menu"
            )
            console.print(
            Panel(
                menu,
                title="⋆˚࿔ Althea's Chick Flick Recommender ⋆˚࿔",
                border_style="magenta",
                expand=True
            )
        )
            # Prompts the user to input a valid choice
            user_input = input("Enter your choice: ").strip()

            # Handle menu choices using match-case
            match user_input:
                case "1":
                    self.set_mood()
                case "2":
                    self.recommend_movies()
                case "3":
                    self.get_chick_flick_quote()
                case "4":
                    clear()
                    console.print("[blue]Thank you for using the Chick Flick"
                        " Movie Recommender! Returning to Team Menu...[/blue]")
                    input("\nPress ENTER to return to TEAM MENU.")
                    break
                case _:
                    print("\n\nInvalid option. Please choose a valid number.")
                    input("Press ENTER to try again.")

recommender = ChickFlickRecommender()
recommender.load_movies()
recommender.menu()