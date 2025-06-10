import random

class Main():
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
                            "attack": (20, 30),
                            "health": 80
                            },
                    "tank": {
                            "defense": (40, 50),
                            "attack": (10, 20),
                            "health": 100
                            },
                    "mage": {
                            "defense": (10, 20),
                            "attack": (40, 50),
                            "health": 60
                            },
                }
    STAT_INCREASE = {
                    "level": 1,
                    "health": 5,
                    "defense": 3,
                    "attack": 3
                }
    
    def __init__(self,
                 name = "None",
                 health = 0,
                 role = "None",
                 defense = 0,
                 attack = 0,
                 weapon = "None",
                 level = 0):
        
        self.name = name
        self.health = health
        self.role = role
        self.defense = defense
        self.attack = attack
        self.weapon = weapon
        self.level = level
        
    def character_profile(self):
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
        
        self.name = input("Enter a name: ")
        
        while self.is_valid(self.role, self.VALID_ROLES) == False:
            self.role = input("What is your role "
                              f"{list(self.VALID_ROLES.keys())}? ").lower()
            
        self.role_stats()
        
        while self.is_valid(self.weapon, self.VALID_WEAPONS) == False:
            self.weapon = input("Choose your weapon "
                                f"{list(self.VALID_WEAPONS.keys())}: ").lower()
            
        self.weapon_stats()

    def is_valid(self, value, valid_set):
        if value in valid_set:
            return True
        return False
            
    def role_stats(self):
        initial_stats = self.VALID_ROLES[self.role]

        if initial_stats:
            self.defense = random.randint(*initial_stats["defense"])
            self.attack = random.randint(*initial_stats["attack"])
            self.health = initial_stats["health"]
        
    def weapon_stats(self):
        stat_boost = self.VALID_WEAPONS[self.weapon]

        if stat_boost:
            self.defense += stat_boost["defense"]
            self.attack += stat_boost["attack"]
    
    def level_up(self):
        get_stat = self.STAT_INCREASE
        
        print("You have leveled up!")
        self.level += get_stat["level"]
        self.health += get_stat["health"]
        self.defense += get_stat["defense"]
        self.attack += get_stat["attack"]

    def menu(self):
        OPTIONS = {
            "1": self.set_character,
        }
        
        choice = None
        while self.is_valid(choice, OPTIONS) == False:
            
            print("=" * 30)
            print(f"{'Mini RPG - Menu':^30}")
            print("=" * 30)
            print(f"[1] Create Character")
            print(f"[2] ")
            print(f"[3] ")
            print(f"[4] ")
            print(f"[5] ")
            print(f"[0] Exit to Main Menu")
            print("=" * 30)
            
            choice = input("Choose an option: ")
            
        OPTIONS[choice]()

character = Main()
character.menu()
        
        