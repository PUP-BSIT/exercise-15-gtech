import random
from unique_names_generator import get_random_name as get_monster_name
from unique_names_generator.data import (ADJECTIVES, 
                                         COUNTRIES, 
                                         ANIMALS, 
                                         STAR_WARS)

class RoleplayGame():
    VALID_WEAPONS = {
                    "sword": {
                            "defense": 3, 
                            "attack": 12
                            },
                    "bow": {
                            "defense": 3, 
                            "attack": 12},
                    "shield": {
                            "defense": 14, 
                            "attack": 1
                            },
                    "spear": {
                            "defense": 5, 
                            "attack": 10
                            },
                    "axe": {
                            "defense": 7, 
                            "attack": 8
                            },
                    "dagger": {
                            "defense": 2, 
                            "attack": 13
                            },
                    "staff": {
                            "defense": 1, 
                            "attack": 14
                            }
                }
    VALID_ROLES = {
                    "warrior": {
                            "defense": (20, 30), 
                            "attack": (30, 40),
                            "health": 80
                            },
                    "tank": {
                            "defense": (40, 50),
                            "attack": (20, 30),
                            "health": 100
                            },
                    "mage": {
                            "defense": (10, 20),
                            "attack": (50, 60),
                            "health": 60
                            },
                }
    STAT_INCREASE = {
                    "level": 1,
                    "health": 5,
                    "defense": 3,
                    "attack": 3
                }
    MONSTER_STAT = {
                    "monster": {
                                "health": (100, 150),
                                "attack": (40, 50),
                                "defense": (20,30)
                                },
                    "boss": {
                                "health": (150, 200),
                                "attack": (60, 70),
                                "defense": (40, 50)
                            }
                    }
    ZERO_HEALTH = 0
    def __init__(
                self,
                name = None,
                health = 0,
                role = None,
                defense = 0,
                attack = 0,
                weapon = None,
                level = 0,
                original_health = 0,
                monster_name = None,
                monster_health = None,
                monster_attack = 0,
                monster_defense = 0
                 ):
        
        """Initialize the RoleplayGame character and monster attributes with 
        optional defaults."""
        
        self.name = name
        self.health = health
        self.role = role
        self.defense = defense
        self.attack = attack
        self.weapon = weapon
        self.level = level
        self.original_health = original_health
        self.monster_name = monster_name
        self.monster_health = monster_health
        self.monster_attack = monster_attack
        self.monster_defense = monster_defense
        
    def character_profile(self):
        """Display the current character's stats and profile details."""
        
        if self.role == None:
            print("You do not have a character yet")
            return
        
        print("=" * 30)
        print(f"{'Character Profile':^30}")
        print("=" * 30)
        print(f"Name:     {self.name}")
        print(f"Level:    {self.level}")
        print(f"Health:   {self.health}")
        print(f"Role:     {self.role}")
        print(f"Defense:  {self.defense}")
        print(f"Attack:   {self.attack}")
        print(f"Weapon:   {self.weapon}")
        print("=" * 30)

    def set_character(self):
        """Prompt the user to create a new character by choosing a name, 
        role, and weapon."""
        
        self.name = input("Enter a name: ")
        
        while self.is_valid(self.role, self.VALID_ROLES) == False:
            self.role = input("What is your role "
                              f"{list(self.VALID_ROLES.keys())}? ").lower()
            
        self.role_stats()
        
        while self.is_valid(self.weapon, self.VALID_WEAPONS) == False:
            self.weapon = input("Choose your weapon "
                                f"{list(self.VALID_WEAPONS.keys())}: ").lower()
            
        self.weapon_stats()
            
    def role_stats(self):
        """Assign random defense and attack stats based on the selected role."""
        
        initial_stats = self.VALID_ROLES[self.role]

        if initial_stats:
            self.defense = random.randint(*initial_stats["defense"])
            self.attack = random.randint(*initial_stats["attack"])
            self.health = initial_stats["health"]
            self.original_health = self.health 
        
    def weapon_stats(self):
        """Apply weapon stat bonuses to the character's base defense 
        and attack."""
        
        stat_boost = self.VALID_WEAPONS[self.weapon]

        if stat_boost:
            self.defense += stat_boost["defense"]
            self.attack += stat_boost["attack"]
    
    def level_up(self):
        """Increase the character's level and boost health, defense, 
        and attack stats."""
        
        get_stat = self.STAT_INCREASE

        self.clear_screen()

        self.level += get_stat["level"]
        self.health += get_stat["health"]
        self.original_health += get_stat["health"]
        self.defense += get_stat["defense"]
        self.attack += get_stat["attack"]

        print("YOU HAVE LEVELED UP!")
        self.character_profile()

    def generate_monster(self):
        """Create a new monster with randomly generated stats and 
        a random name."""
        
        monster_stats = self.MONSTER_STAT["monster"]

        self.monster_name = get_monster_name(combo=[
                                                    COUNTRIES,
                                                    ADJECTIVES,
                                                    ANIMALS
                                                    ])

        if monster_stats:
            self.monster_defense = random.randint(*monster_stats["defense"])
            self.monster_attack = random.randint(*monster_stats["attack"])
            self.monster_health = random.randint(*monster_stats["health"])
            
    def generate_boss(self):
        """Create a boss monster with stronger randomly generated 
        stats and a themed name."""
        
        boss_stats = self.MONSTER_STAT["boss"]

        self.monster_name = get_monster_name(combo=[
                                                    COUNTRIES,
                                                    ADJECTIVES,
                                                    STAR_WARS
                                                    ])

        if boss_stats:
            self.monster_defense = random.randint(*boss_stats["defense"])
            self.monster_attack = random.randint(*boss_stats["attack"])
            self.monster_health = random.randint(*boss_stats["health"])
    
    def monster_profile(self):
        """Display the current monster's stats and name."""
        
        print("=" * 30)
        print(f"{'Monster Profile':^30}")
        print("=" * 30)
        print(f"Name:     {self.monster_name}")
        print(f"Health:   {self.monster_health}")
        print(f"Defense:  {self.monster_defense}")
        print(f"Attack:   {self.monster_attack}")
        print("=" * 30)
        
    def attack_monster(self):
        """Run the battle sequence against a regular monster, including 
        user interaction and outcome handling."""
        
        ACTION_OPTIONS = {
            "attack": self.action_attack,
            "run": self.action_run
        }
        MONSTER_ACTIONS = {
            1: self.action_monster_attack,
            2: self.action_monster_defend
        }

        if self.role is None:
            print("You do not have a character yet. Please create one "
                  "before battling.")
            input("Press Enter to return to the menu...")
            return

        self.generate_monster()
        print("\n" + "-" * 50)
        print(f"A {self.monster_name} has appeared!")
        print("-" * 50)

        while (self.health > self.ZERO_HEALTH 
               and self.monster_health > self.ZERO_HEALTH):
            self.clear_screen()
            self.monster_profile()
            print("\n" + "=" * 50)
            print(f"Your Health     : {self.health}")
            print(f"{self.monster_name}'s Health : {self.monster_health}")
            print("=" * 50)

            print("Note: A mistake in what you type can lead to consequences.")
            print("Be careful when making a decision.\n")

            choice = input("Your turn! Choose an action "
                           f"{list(ACTION_OPTIONS.keys())}: ").lower()
            self.option_logic(choice, ACTION_OPTIONS)

            if self.is_monster_defeated():
                break

            print("\n" + "-" * 50)
            print(f"{self.monster_name}'s turn!")
            print("-" * 50)
            MONSTER_ACTIONS[random.randint(1, 2)]()

            if self.is_player_defeated():
                break

    def action_attack(self):
        """Calculate and apply damage to the monster based on the player's 
        attack and monster's defense."""
        
        damage = max(self.attack - self.monster_defense, 0)
        self.monster_health -= damage
        print(f"You attacked {self.monster_name} for {damage} damage.")

    def action_run(self):
        """Handle logic when the player decides to flee from battle 
        and reset health."""
        
        print("You chose to run away from the battle.")
        input("Press Enter to return to the menu...")
        self.health = self.original_health
        return self.menu()

    def is_monster_defeated(self):
        """Check if the monster has been defeated and process victory events."""
        
        if self.monster_health <= 0:
            self.clear_screen()
            print("\n" + "-" * 50)
            print(f"You have defeated {self.monster_name}!")
            print("-" * 50)
            input("Press Enter to continue...")
            self.level_up()
            self.health = self.original_health
            self.menu()
            return True
        return False

    def is_player_defeated(self):
        """Check if the player has been defeated and handle game over logic."""
        
        if self.health <= 0:
            self.clear_screen()
            print("\n" + "-" * 50)
            print("You have been defeated! Game over.")
            print("-" * 50)
            input("Press Enter to return to the menu...")
            self.health = self.original_health
            self.menu()
            return True
        return False

    def action_monster_attack(self):
        """Handle the monster's attack action during its turn in battle."""
        
        damage = max(self.monster_attack - self.defense, 0)
        self.health -= damage
        print(f"{self.monster_name} attacked you for {damage} damage.")
        input("Press Enter to continue...")

    def action_monster_defend(self):
        """Increase the monster's defense during its turn as a 
        defensive move."""
        
        boost = random.randint(2, 5)
        self.monster_defense += boost
        print(f"{self.monster_name} increased its defense by {boost}.")
        input("Press Enter to continue...")
    
    def attack_boss(self):
        """Run the battle sequence against a boss monster, including 
        combat and turn logic."""
        
        ACTION_OPTIONS = {
            "attack": self.action_attack,
            "run": self.action_run
        }
        BOSS_ACTIONS = {
            1: self.action_monster_attack,
            2: self.action_monster_defend
        }

        if self.role is None:
            print("You do not have a character yet. Please create one "
                  "before battling.")
            input("Press Enter to return to the menu...")
            return

        self.generate_boss()
        print("\n" + "-" * 50)
        print(f"The {self.monster_name} has appeared!")
        print("-" * 50)

        while (self.health > self.ZERO_HEALTH 
               and self.monster_health > self.ZERO_HEALTH):
            self.clear_screen()
            self.monster_profile()
            print("\n" + "=" * 50)
            print(f"Your Health     : {self.health}")
            print(f"{self.monster_name}'s Health : {self.monster_health}")
            print("=" * 50)

            print("Note: A mistake in what you type can lead to consequences.")
            print("Be careful when making a decision.\n")

            choice = input("Your turn! Choose an action "
                           f"{list(ACTION_OPTIONS.keys())}: ").lower()
            self.option_logic(choice, ACTION_OPTIONS)

            if self.is_monster_defeated():
                break

            print("\n" + "-" * 50)
            print(f"{self.monster_name}'s turn!")
            print("-" * 50)
            BOSS_ACTIONS[random.randint(1, 2)]()

            if self.is_player_defeated():
                break
            
    def train(self):
        """Allow the player to improve their character by selecting a 
        training intensity, resulting in stat gains."""
        
        if self.role is None:
            print("You do not have a character yet. Please create one "
                  "before training.")
            input("Press Enter to return to the menu...")
            return

        self.clear_screen()
        print("\n" + "=" * 50)
        print("           Welcome to the Training Grounds")
        print("=" * 50)

        training_options = {
            "light": 1,
            "moderate": 2,
            "intense": 3
        }

        print("Choose your training intensity:")
        for level, multiplier in training_options.items():
            print(f"- {level.capitalize()} Training")

        choice = input("\nEnter your training type "
                       "(light/moderate/intense): ").lower()

        if choice not in training_options:
            print("Invalid training type. Returning to menu...")
            return

        old_level = self.level
        old_health = self.health
        old_attack = self.attack
        old_defense = self.defense

        for _ in range(training_options[choice]):
            self.level_up()

        self.clear_screen()
        print("\nTraining Complete!")
        print("=" * 50)
        print(f"Training Type : {choice.capitalize()}")
        print(f"Level Gained  : {self.level - old_level}")
        print(f"Health Gained : {self.health - old_health}")
        print(f"Attack Gained : {self.attack - old_attack}")
        print(f"Defense Gained: {self.defense - old_defense}")
        print("=" * 50)

    @staticmethod
    def clear_screen():
        """Clear the console screen output using an ANSI escape sequence."""
        
        return print("\033c", end="")

    @staticmethod
    def is_valid(value, valid_set):
        """Check if the provided value exists in the given set or dictionary."""
        if value in valid_set:
            return True
        return False
    
    def option_logic(self, choice, OPTIONS, condition = None):
        """Safely invoke the function associated with a menu or action 
        choice, if valid."""
        
        if not self.is_valid(choice, OPTIONS):
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")
            return
        
        try:
            OPTIONS[choice](condition)
        except TypeError:
            OPTIONS[choice]()
            
        input("\nPress Enter to return...")
        
    def exit_to_main_menu(self):
        """Exit the game and return to the main program 
        (currently exits Python entirely)."""
        exit()
        
    def menu(self):
        """Display the main game menu and handle user input for 
        navigation and actions."""
        
        MENU_OPTIONS = {
            "1": self.set_character,
            "2": self.character_profile,
            "3": self.attack_monster,
            "4": self.attack_boss,
            "5": self.train,
            "0": self.exit_to_main_menu,
        }

        while True:
            self.clear_screen()

            print("=" * 30)
            print(f"{'Mini RPG - Menu':^30}")
            print("=" * 30)
            print(f"[1] Create Character")
            print(f"[2] Character Profile")
            print(f"[3] Attack a Monster")
            print(f"[4] Attack the Boss")
            print(f"[5] Train at Dojo")
            print(f"[0] Exit to Main Menu")
            print("=" * 30)

            choice = input("Enter a choice: ").strip()

            self.option_logic(choice, MENU_OPTIONS, None)
        