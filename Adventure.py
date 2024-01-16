import time
import pickle
import os

# Define ANSI escape codes for text color
LIGHT_BLUE = "\033[94m"  # Light Blue color code
PURPLE = "\033[95m"      # Purple color code
YELLOW = "\033[93m"      # Yellow color code
GREEN = "\033[92m"       # Green color code
RESET = "\033[0m"        # Reset color code

def colored_print(text, color):
    print(f"{color}{text}{RESET}")

def introduction():
    colored_print("Welcome to the Epic Isekai Adventure Game!", LIGHT_BLUE)
    time.sleep(1)
    colored_print("You and your high school friends find yourselves in a magical forest.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("Your goal is to navigate through this mysterious world and uncover its secrets.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("Let the epic isekai adventure begin!\n", LIGHT_BLUE)

def save_game(player_data):
    with open("saved_game.pkl", "wb") as file:
        pickle.dump(player_data, file)

def load_game():
    if os.path.exists("saved_game.pkl"):
        with open("saved_game.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return None

def make_choice(choices):
    print("Choose your next move:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Add the following functions to handle the new choices:

def explore_forest(player_data):
    colored_print("\nYou and your high school friends find yourselves in a magical forest...", LIGHT_BLUE)
    time.sleep(1)
    colored_print("As you wander deeper, you encounter a crossroads with diverging paths.", LIGHT_BLUE)

    choices = ["Follow the sunlight path", "Enter the mysterious grove", "Investigate a strange sound", "Climb a massive tree", 
               "Confront a shadowy figure", "Cross a magical bridge", "Search for a hidden cave", "Summon a spirit guide", 
               "Challenge a guardian beast", "Explore an ancient library", "Navigate through a time-warping mist", 
               "Converse with a talking tree", "Enter a realm of illusions"]
    choice = make_choice(choices)

    if choice == 1:
        colored_print("\nYou chose to follow the path illuminated by sunlight.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("The air becomes warmer, and you discover a hidden clearing.", LIGHT_BLUE)
        magical_clearing(player_data)
    elif choice == 2:
        colored_print("\nYou chose to enter the mysterious grove.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("The trees whisper ancient secrets, and you sense a magical presence.", LIGHT_BLUE)
        magical_grove(player_data)
    elif choice == 3:
        colored_print("\nYou chose to investigate a strange sound.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("Following the sound, you find a creature in need of help.", LIGHT_BLUE)
        help_creature(player_data)
    elif choice == 4:
        colored_print("\nYou chose to climb a massive tree.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("From the treetop, you see a hidden path below.", LIGHT_BLUE)
        hidden_path(player_data)
    elif choice == 5:
        colored_print("\nYou chose to confront a shadowy figure.", PURPLE)
        time.sleep(1)
        colored_print("As you approach, the figure reveals itself as a friendly spirit.", PURPLE)
        spirit_encounter(player_data)
    elif choice == 6:
        colored_print("\nYou chose to cross a magical bridge.", PURPLE)
        time.sleep(1)
        colored_print("The bridge leads you to a floating island with ancient ruins.", PURPLE)
        ancient_island(player_data)
    elif choice == 7:
        colored_print("\nYou chose to search for a hidden cave.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("Inside the cave, you discover a portal to a different realm.", LIGHT_BLUE)
        portal_discovery(player_data)
    elif choice == 8:
        colored_print("\nYou chose to summon a spirit guide.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("A wise spirit appears, offering guidance and revealing hidden truths.", LIGHT_BLUE)
        spirit_guide(player_data)
    elif choice == 9:
        colored_print("\nYou chose to challenge a guardian beast.", LIGHT_BLUE)
        time.sleep(1)
        colored_print("The beast tests your courage and grants you its protection.", LIGHT_BLUE)
        guardian_beast(player_data)
    elif choice == 10:
        colored_print("\nYou chose to explore an ancient library.", YELLOW)
        time.sleep(1)
        colored_print("Among the dusty tomes, you uncover forgotten knowledge and ancient spells.", YELLOW)
        ancient_library(player_data)
    elif choice == 11:
        colored_print("\nYou chose to navigate through a time-warping mist.", YELLOW)
        time.sleep(1)
        colored_print("As you pass through the mist, time distorts, revealing glimpses of the past and future.", YELLOW)
        time_warp(player_data)
    elif choice == 12:
        colored_print("\nYou chose to converse with a talking tree.", GREEN)
        time.sleep(1)
        colored_print("The wise tree imparts knowledge about the balance of nature and magical energies.", GREEN)
        talking_tree(player_data)
    else:
        colored_print("\nYou chose to enter a realm of illusions.", GREEN)
        time.sleep(1)
        colored_print("Reality twists around you as illusions challenge your perceptions.", GREEN)
        illusion_realm(player_data)

def spirit_encounter(player_data):
    colored_print("\nThe spirit thanks you for not being afraid and shares ancient knowledge.", PURPLE)
    time.sleep(1)
    colored_print("It gifts you with the ability to understand the language of magical creatures.", PURPLE)
    player_data["language_ability"] = True
    colored_print("Where does this epic isekai journey end?", PURPLE)
    end_of_story(player_data)

def ancient_island(player_data):
    colored_print("\nThe ancient ruins hold a powerful artifact that enhances your magical abilities.", PURPLE)
    time.sleep(1)
    colored_print("You feel a surge of energy as you absorb the artifact's power.", PURPLE)
    player_data["enhanced_magic"] = True
    colored_print("Where does this epic isekai journey end?", PURPLE)
    end_of_story(player_data)


def portal_discovery(player_data):
    colored_print("\nThe portal transports you to a realm of challenges and rewards.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("You navigate through trials, gaining strength and resilience.", LIGHT_BLUE)
    player_data["trials_completed"] = True
    colored_print("Where does this epic isekai journey end?", LIGHT_BLUE)
    end_of_story(player_data)

def spirit_guide(player_data):
    colored_print("\nThe spirit guide imparts wisdom and shows you a path only visible to those with a pure heart.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("Following the path, you uncover the source of the magical energy.", LIGHT_BLUE)
    player_data["pure_heart"] = True
    colored_print("Where does this epic isekai journey end?", LIGHT_BLUE)
    end_of_story(player_data)

def guardian_beast(player_data):
    colored_print("\nThe guardian beast acknowledges your bravery and becomes your loyal companion.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("Together, you face challenges and overcome obstacles.", LIGHT_BLUE)
    player_data["guardian_companion"] = True
    colored_print("Where does this epic isekai journey end?", LIGHT_BLUE)
    end_of_story(player_data)

def ancient_library(player_data):
    colored_print("\nThe ancient library unveils secrets of forgotten civilizations and powerful spells.", YELLOW)
    time.sleep(1)
    colored_print("You gain knowledge that enhances your magical prowess.", YELLOW)
    player_data["arcane_knowledge"] = True
    colored_print("Where does this epic isekai journey end?", YELLOW)
    end_of_story(player_data)

def time_warp(player_data):
    colored_print("\nAs you navigate the time-warping mist, you gain glimpses of important events in the magical realm.", YELLOW)
    time.sleep(1)
    colored_print("This insight allows you to make strategic choices in your journey.", YELLOW)
    player_data["strategic_insight"] = True
    colored_print("Where does this epic isekai journey end?", YELLOW)
    end_of_story(player_data)

def talking_tree(player_data):
    colored_print("\nThe talking tree shares ancient wisdom, deepening your connection with nature.", GREEN)
    time.sleep(1)
    colored_print("You gain the ability to communicate with and command magical creatures.", GREEN)
    player_data["nature_communication"] = True
    colored_print("Where does this epic isekai journey end?", GREEN)
    end_of_story(player_data)

def illusion_realm(player_data):
    colored_print("\nThe illusions challenge your mind, enhancing your mental resilience and awareness.", GREEN)
    time.sleep(1)
    colored_print("You can now see through magical illusions and detect hidden truths.", GREEN)
    player_data["illusion_sight"] = True
    colored_print("Where does this epic isekai journey end?", GREEN)
    end_of_story(player_data)

def magical_clearing(player_data):
    colored_print("\nYou and your friends enter a magical clearing filled with glowing flowers!", PURPLE)
    time.sleep(1)
    colored_print("Congratulations! You've found a place of tranquility and enchantment.", PURPLE)
    time.sleep(1)
    colored_print("As you appreciate the beauty, a portal appears before you.", PURPLE)
    time.sleep(1)
    colored_print("You decide to step through, wondering where it might lead.", PURPLE)
    time.sleep(1)

    if player_data["completed_game"]:
        colored_print("You feel a mysterious energy surrounding you.", YELLOW)
        time.sleep(1)
        colored_print("A voice whispers, 'Your journey continues beyond the known realms.'", YELLOW)
        time.sleep(1)
        colored_print("The portal transports you to an unknown destination.", YELLOW)
        time.sleep(1)
        colored_print("Where does this mysterious journey truly end?", YELLOW)
        end_of_story(player_data)
    else:
        colored_print("Where does this epic isekai journey end?", YELLOW)
        end_of_story(player_data)

def magical_grove(player_data):
    colored_print("\nYou and your friends walk deeper into the mysterious grove.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("The air shimmers with magical energy, and you discover a hidden fountain.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("As you approach, the water sparkles with otherworldly colors.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("You take a moment to drink from the magical fountain and feel a surge of energy.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("A pathway reveals itself, leading you to an ethereal garden.", LIGHT_BLUE)
    time.sleep(1)
    colored_print("Where does this epic isekai journey end?", LIGHT_BLUE)
    end_of_story(player_data)

def end_of_story(player_data):
    colored_print("\nYou and your friends follow the magical path and find yourselves at the edge of the ethereal garden.", PURPLE)
    time.sleep(1)
    colored_print("Before you lies a portal shimmering with an otherworldly light.", PURPLE)
    time.sleep(1)
    colored_print("As you step through, the world transforms around you.", PURPLE)
    time.sleep(1)
    colored_print("A voice echoes, 'Your epic isekai adventure has just begun. What new challenges await in this magical realm?'", PURPLE)
    time.sleep(1)

    if player_data["completed_game"]:
        colored_print("The portal closes behind you, leaving you with the mystery of what lies ahead.", YELLOW)
        time.sleep(1)
        colored_print("Where does this enchanting isekai journey truly end?", YELLOW)
        colored_print("Thank you for playing the Epic Isekai Adventure Game!", YELLOW)
    else:
        colored_print("The portal transports you back to your world.", YELLOW)
        time.sleep(1)
        colored_print("You and your friends share a knowing smile, grateful for the adventures you've experienced together.", YELLOW)
        time.sleep(1)
        colored_print("The mystery of the isekai world lingers in your memories.", YELLOW)
        time.sleep(1)
        colored_print("Thank you for playing!", YELLOW)

def main():
    player_name = input("Enter your name: ")
    player_password = input("Choose a password: ")

    player_data = load_game()

    if player_data and player_data["name"] == player_name and player_data["password"] == player_password:
        colored_print(f"Welcome back, {player_name}!", GREEN)

        if player_data["completed_game"]:
            colored_print("Congratulations! You've already completed the epic isekai adventure.", GREEN)
            if input("Do you want to replay the adventure? (y/n): ").lower() == 'y':
                colored_print("Starting a new epic isekai adventure...", GREEN)
                player_data["completed_game"] = False
                introduction()
                explore_forest(player_data)
            else:
                colored_print("Thank you for playing!", GREEN)
        else:
            if input("Do you want to continue your saved epic isekai adventure? (y/n): ").lower() == 'y':
                colored_print("Loading saved game...", GREEN)
                explore_forest(player_data)
            else:
                colored_print("Starting a new epic isekai adventure...", GREEN)
                introduction()
                explore_forest(player_data)

    else:
        colored_print(f"Welcome, {player_name}!", GREEN)
        player_data = {"name": player_name, "password": player_password, "completed_game": False}
        introduction()
        explore_forest(player_data)

    save_game(player_data)

if __name__ == "__main__":
    main()


