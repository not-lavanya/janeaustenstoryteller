"""
Regency Name Dictionary
A comprehensive collection of period-appropriate names from Jane Austen's era.
"""

import os
import time
import sys
import random
import textwrap

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, delay=0.03, variance=0.01):
    """Print text with a typewriter effect"""
    import random
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Random variation in typing speed for natural effect
        typing_delay = max(0.001, delay + random.uniform(-variance, variance))
        time.sleep(typing_delay)
    print()

class RegencyNameDictionary:
    def __init__(self):
        """Initialize the Regency era name collections"""
        # Female first names common in the Regency era
        self.female_first_names = [
            "Anne", "Augusta", "Cassandra", "Catherine", "Charlotte", "Clara", 
            "Dorothea", "Eleanor", "Elizabeth", "Eliza", "Emma", "Fanny", "Frances",
            "Georgiana", "Harriet", "Isabella", "Jane", "Kitty", "Louisa", "Lucy",
            "Lydia", "Margaret", "Maria", "Mary", "Marianne", "Penelope", "Sarah",
            "Sophia", "Susan", "Victoria"
        ]
        
        # Male first names common in the Regency era
        self.male_first_names = [
            "Alexander", "Arthur", "Benjamin", "Charles", "Christopher", "Edmund",
            "Edward", "Frederick", "George", "Henry", "Hugh", "James", "John",
            "Joseph", "Matthew", "Nathaniel", "Philip", "Richard", "Robert",
            "Samuel", "Thomas", "William"
        ]
        
        # Family names (surnames) common in the Regency era
        self.family_names = [
            "Allen", "Austen", "Bennet", "Bertram", "Bingley", "Bowles", "Brandon",
            "Churchill", "Collins", "Crawford", "Darcy", "Dashwood", "Elton",
            "Fairfax", "Ferrars", "Fitzwilliam", "Gardiner", "Harville", "Kingsley",
            "Knightley", "Lucas", "Morland", "Norris", "Palmer", "Price", "Tilney",
            "Vernon", "Wentworth", "Willoughby", "Woodhouse", "Wickham"
        ]
        
        # Titles used in the Regency era
        self.titles = {
            "male": ["Mr.", "Sir", "Lord", "Captain", "Colonel", "Major", "The Honorable", "Dr."],
            "female": ["Miss", "Mrs.", "Lady", "The Honorable Miss"]
        }
        
        # Name origins and meanings
        self.name_origins = {
            "Anne": "Hebrew origin, meaning 'grace' or 'favor'",
            "Elizabeth": "Hebrew origin, meaning 'God is my oath'",
            "Jane": "Hebrew origin, meaning 'God is gracious'",
            "Emma": "Germanic origin, meaning 'whole' or 'universal'",
            "Charlotte": "French origin, feminine form of 'Charles', meaning 'free man'",
            "Georgiana": "Greek origin, feminine form of 'George', meaning 'farmer'",
            "Darcy": "French origin, meaning 'from Arcy' (a place in France)",
            "Bennet": "Latin origin, meaning 'blessed'",
            "Woodhouse": "English origin, meaning 'one who lives by a wood'",
            "Knightley": "English origin, meaning 'knight's meadow'"
        }
        
        # Notable Austen characters by name
        self.austen_character_names = {
            "Elizabeth Bennet": "The spirited and intelligent protagonist of Pride and Prejudice",
            "Fitzwilliam Darcy": "The wealthy, reserved gentleman who falls in love with Elizabeth Bennet",
            "Emma Woodhouse": "The privileged, matchmaking protagonist of Emma",
            "George Knightley": "The sensible gentleman who is a friend and critic of Emma",
            "Anne Elliot": "The overlooked, reflective protagonist of Persuasion",
            "Frederick Wentworth": "The naval captain who returns to Anne Elliot's life in Persuasion",
            "Marianne Dashwood": "The emotionally expressive sister in Sense and Sensibility",
            "Elinor Dashwood": "The reserved, sensible sister in Sense and Sensibility",
            "Fanny Price": "The modest, moral protagonist of Mansfield Park",
            "Edmund Bertram": "The principled clergyman in Mansfield Park"
        }
    
    def get_random_name(self, gender=None):
        """
        Generate a random Regency era name with optional title
        
        Args:
            gender: 'male', 'female', or None (random)
            
        Returns:
            A tuple of (full_name, details)
        """
        # Determine gender if not specified
        if gender is None:
            gender = random.choice(['male', 'female'])
            
        # Select first name
        if gender.lower() == 'male':
            first_name = random.choice(self.male_first_names)
        else:
            first_name = random.choice(self.female_first_names)
            
        # Select family name
        family_name = random.choice(self.family_names)
        
        # Decide whether to include a title (30% chance)
        if random.random() < 0.3:
            title = random.choice(self.titles[gender])
            full_name = f"{title} {first_name} {family_name}"
        else:
            full_name = f"{first_name} {family_name}"
            
        # Gather details about the name
        details = []
        if first_name in self.name_origins:
            details.append(f"Origin: {self.name_origins[first_name]}")
            
        # Check if it matches an Austen character
        character_name = f"{first_name} {family_name}"
        if character_name in self.austen_character_names:
            details.append(f"Austen Character: {self.austen_character_names[character_name]}")
            
        return (full_name, details)
    
    def get_name_by_letter(self, letter, gender=None):
        """
        Get names starting with a specific letter
        
        Args:
            letter: Starting letter
            gender: Optional filter by gender
            
        Returns:
            List of names starting with the letter
        """
        letter = letter.upper()
        
        if gender is None or gender.lower() == 'female':
            female_names = [name for name in self.female_first_names if name.startswith(letter)]
        else:
            female_names = []
            
        if gender is None or gender.lower() == 'male':
            male_names = [name for name in self.male_first_names if name.startswith(letter)]
        else:
            male_names = []
            
        surnames = [name for name in self.family_names if name.startswith(letter)]
        
        result = []
        
        if female_names:
            result.append("Female Names:")
            result.extend(female_names)
            result.append("")
            
        if male_names:
            result.append("Male Names:")
            result.extend(male_names)
            result.append("")
            
        if surnames:
            result.append("Family Names:")
            result.extend(surnames)
            
        return result
    
    def get_austen_character_names(self):
        """
        Get the list of Austen character names with descriptions
        
        Returns:
            Dictionary of character names and descriptions
        """
        return self.austen_character_names
    
    def suggest_name_combinations(self, count=5):
        """
        Suggest authentic name combinations from the Regency era
        
        Args:
            count: Number of suggestions to generate
            
        Returns:
            List of name suggestions with details
        """
        suggestions = []
        
        for _ in range(count):
            gender = random.choice(['male', 'female'])
            name, details = self.get_random_name(gender)
            suggestions.append((name, gender, details))
            
        return suggestions
    
    def get_name_meanings(self, name=None):
        """
        Get the meaning and origin of a specific name or a random one
        
        Args:
            name: Name to look up, or None for a random name
            
        Returns:
            Tuple of (name, meaning) or None if not found
        """
        if name is None:
            # Return a random name with known meaning
            available_names = list(self.name_origins.keys())
            if available_names:
                selected_name = random.choice(available_names)
                return (selected_name, self.name_origins[selected_name])
            return None
            
        # Look for exact match
        if name in self.name_origins:
            return (name, self.name_origins[name])
            
        # Look for case-insensitive match
        for key in self.name_origins:
            if key.lower() == name.lower():
                return (key, self.name_origins[key])
                
        return None

def display_decorative_header():
    """Display a decorative header for the Regency name dictionary"""
    header = """
╔═════════════════════════════════════════════════════════════════╗
║                                                                 ║
║              REGENCY ERA NAME DICTIONARY                        ║
║                                                                 ║
║  "What's in a name? That which we call a rose                   ║
║   By any other name would smell as sweet."                      ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
"""
    print(header)

def run_name_dictionary():
    """Run the interactive Regency Name Dictionary tool"""
    name_dict = RegencyNameDictionary()
    
    while True:
        clear_screen()
        display_decorative_header()
        
        print("\nWelcome to the Regency Era Name Dictionary")
        print("\nWhat would you like to do?")
        print("1. Generate random Regency era names")
        print("2. View names by starting letter")
        print("3. Search for name meanings")
        print("4. View Jane Austen character names")
        print("5. Return to main menu")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Generate random names
            clear_screen()
            display_decorative_header()
            
            print("\nRANDOM REGENCY ERA NAMES")
            print("=" * 50)
            
            try:
                count = int(input("\nHow many names would you like to generate? (1-10): "))
                count = max(1, min(10, count))
            except ValueError:
                count = 5
                
            gender_choice = input("\nPrefer male, female, or both? (m/f/b): ").lower()
            
            if gender_choice == 'm':
                gender = 'male'
            elif gender_choice == 'f':
                gender = 'female'
            else:
                gender = None
                
            print("\nGenerating names...")
            print("-" * 50)
            
            for i in range(count):
                name, details = name_dict.get_random_name(gender)
                print(f"\n{i+1}. {name}")
                
                if details:
                    for detail in details:
                        print(f"   - {detail}")
            
        elif choice == '2':
            # View names by letter
            clear_screen()
            display_decorative_header()
            
            print("\nVIEW NAMES BY STARTING LETTER")
            print("=" * 50)
            
            letter = input("\nEnter a letter to view names (A-Z): ")
            
            if letter and letter[0].isalpha():
                gender_choice = input("\nFilter by gender? (m/f/both): ").lower()
                
                if gender_choice == 'm':
                    gender = 'male'
                elif gender_choice == 'f':
                    gender = 'female'
                else:
                    gender = None
                    
                name_list = name_dict.get_name_by_letter(letter[0], gender)
                
                if name_list:
                    print("\nNames starting with", letter[0].upper())
                    print("-" * 50)
                    
                    for item in name_list:
                        print(item)
                else:
                    print(f"\nNo names found starting with {letter[0].upper()}")
            else:
                print("\nInvalid input. Please enter a valid letter.")
                
        elif choice == '3':
            # Search for name meanings
            clear_screen()
            display_decorative_header()
            
            print("\nNAME MEANINGS AND ORIGINS")
            print("=" * 50)
            
            name_input = input("\nEnter a name to look up (or leave blank for random): ")
            
            if name_input:
                result = name_dict.get_name_meanings(name_input)
                
                if result:
                    name, meaning = result
                    print(f"\n{name}:")
                    print(f"  {meaning}")
                else:
                    print(f"\nSorry, no information found for '{name_input}'")
                    print("Available names with meanings include:")
                    available_names = list(name_dict.name_origins.keys())
                    for i, name in enumerate(available_names):
                        if i % 5 == 0 and i > 0:
                            print()
                        print(f"{name}, ", end="")
                    print()
            else:
                result = name_dict.get_name_meanings()
                
                if result:
                    name, meaning = result
                    print(f"\nRandom Name: {name}")
                    print(f"  {meaning}")
                    
        elif choice == '4':
            # View Austen character names
            clear_screen()
            display_decorative_header()
            
            print("\nJANE AUSTEN CHARACTER NAMES")
            print("=" * 50)
            
            austen_characters = name_dict.get_austen_character_names()
            
            for character, description in austen_characters.items():
                print(f"\n{character}:")
                print(textwrap.fill(description, width=70, initial_indent="  ", subsequent_indent="  "))
                
        elif choice == '5':
            # Return to main menu
            return
            
        else:
            print("\nInvalid choice. Please try again.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run_name_dictionary()