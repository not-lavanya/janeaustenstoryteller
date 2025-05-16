"""
Enhanced Jane Austen Interactive Experience
Main menu for accessing various Jane Austen inspired features with custom theme support.
"""

import os
import time
import sys
import random
from austen_quotes import AustenQuoteGenerator
from austen_quotes_demo import run_quote_demo
from visual_imagery import VisualImageryGenerator

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, delay=0.03, variance=0.01):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Random variation in typing speed for natural effect
        typing_delay = max(0.001, delay + random.uniform(-variance, variance))
        time.sleep(typing_delay)
    print()

def display_austen_quote():
    """Display a random Jane Austen quote with decorative frame"""
    quotes = [
        {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
            "source": "Pride and Prejudice"
        },
        {
            "text": "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
            "source": "Northanger Abbey"
        },
        {
            "text": "I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book!",
            "source": "Pride and Prejudice"
        },
        {
            "text": "There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.",
            "source": "Northanger Abbey"
        },
        {
            "text": "A lady's imagination is very rapid; it jumps from admiration to love, from love to matrimony, in a moment.",
            "source": "Pride and Prejudice"
        }
    ]
    
    quote = random.choice(quotes)
    
    # Create decorative frame for the quote
    imagery_generator = VisualImageryGenerator()
    decorated_quote = imagery_generator.create_quote_illustration(quote["text"], quote["source"])
    print(decorated_quote)
    
    # Small pause for reader to appreciate the quote
    time.sleep(1)

def custom_theme_storyteller():
    """Interactive storyteller that works with custom themes"""
    clear_screen()
    
    print("█████████████████████████████████████████████████████████████████████")
    print("█                                                                 █")
    print("█     JANE AUSTEN CUSTOM THEME STORYTELLING EXPERIENCE           █")
    print("█                                                                 █")
    print("█     \"It is a truth universally acknowledged, that a reader      █")
    print("█      with a theme in mind, must be in want of a story\"          █")
    print("█                                                                 █")
    print("█████████████████████████████████████████████████████████████████████")
    
    # Let the user input a custom theme
    print("\nPlease enter your custom theme for the Jane Austen style story:")
    print("(Examples: unrequited love, social advancement, family obligations, etc.)")
    theme = input("> ")
    
    if not theme:
        theme = "unexpected connections"
        print(f"\nUsing default theme: {theme}")
    
    # Select narrative complexity
    print("\nSelect the narrative complexity level:")
    print("1. Simple and straightforward")
    print("2. Moderate with social commentary")
    print("3. Complex with multiple perspectives")
    
    complexity_choice = input("\nEnter complexity level (1-3): ")
    try:
        complexity_level = int(complexity_choice)
        if complexity_level < 1 or complexity_level > 3:
            complexity_level = 2
    except ValueError:
        complexity_level = 2
    
    print(f"\nGenerating a level {complexity_level} narrative on the theme of '{theme}'...")
    print("This may take a moment...")
    
    # Simulate story generation with typing effect
    time.sleep(1)
    
    # Display a location illustration (placeholder)
    imagery_generator = VisualImageryGenerator()
    location = random.choice(["Pemberley", "Bath", "London", "Brighton"])
    season = random.choice(["spring", "summer", "autumn", "winter"])
    location_image = imagery_generator.create_location_illustration(location, season)
    
    clear_screen()
    print("\n" + "=" * 80)
    print(f"YOUR CUSTOM JANE AUSTEN STORY ON THE THEME OF: {theme.upper()}")
    print("=" * 80 + "\n")
    
    # Show location imagery
    print(location_image)
    print("\n" + "-" * 80 + "\n")
    
    # Generate a story about the custom theme
    print(f"In the Regency era, during {season} at {location}, the following tale unfolds...\n")
    
    # Generate characters
    character_types = [
        {"name": "Elizabeth Woodhouse", "class": "gentlewoman", "occupation": "accomplished lady", "character": "spirited"},
        {"name": "Mr. Henry Crawford", "class": "gentleman of fortune", "occupation": "landowner", "character": "charming"},
        {"name": "Lady Catherine Vernon", "class": "member of the peerage", "occupation": "patroness", "character": "haughty"},
        {"name": "Colonel James Brandon", "class": "military officer", "occupation": "retired colonel", "character": "honorable"}
    ]
    
    print("Our cast of characters includes:")
    for character in character_types:
        print(f"- {character['name']}: A {character['character']} {character['class']} who works as a {character['occupation']}.")
    
    # Generate the story with theme incorporated
    story_parts = [
        f"The matter of {theme} was much discussed in {location} society that {season}. Elizabeth Woodhouse had long held that {theme} was a subject best approached with both sense and sensibility.",
        f"While attending a gathering at the home of Lady Catherine Vernon, Mr. Henry Crawford expressed views on {theme} that surprised the assembled company. \"It is curious,\" he remarked, \"how society views {theme} through a lens of propriety while overlooking the more fundamental questions of character.\"",
        f"Colonel Brandon, having observed the exchange with his characteristic reserve, later confided to Elizabeth, \"In my experience, {theme} reveals more about one's true nature than all the carefully constructed appearances of polite society.\"",
        f"As the {season} progressed, the various perspectives on {theme} created subtle divisions among the residents of {location}. Lady Catherine maintained that tradition must be respected, while Elizabeth increasingly found herself questioning whether conventional wisdom on {theme} truly led to happiness.",
        f"By the season's end, a new understanding had emerged. That in matters of {theme}, as in matters of the heart, the path to contentment lay not in rigid adherence to social expectations, but in the honest examination of one's own principles and desires."
    ]
    
    # Print story with typing effect for immersion
    for part in story_parts:
        print_with_typing_effect(part)
        print()
    
    # Display character portraits
    print("\n" + "=" * 80)
    print("CHARACTER PORTRAITS:")
    
    for character in character_types[:2]:  # Show first two characters
        portrait = imagery_generator.create_character_illustration(character)
        print(portrait)
    
    # Generate an event illustration related to the theme
    print("\n" + "=" * 80)
    print("THEMATIC ILLUSTRATION:")
    event_image = imagery_generator.create_event_illustration(theme)
    print(event_image)
    
    # Add a thematically appropriate quote
    quote_generator = AustenQuoteGenerator()
    themes = quote_generator.get_available_themes()
    matched_theme = "love"  # Default theme
    
    # Try to match the custom theme to available quote themes
    for t in themes:
        if t.lower() in theme.lower() or theme.lower() in t.lower():
            matched_theme = t
            break
    
    quote = quote_generator.get_quote_by_theme(matched_theme)
    print("\n" + "=" * 80)
    print("RELEVANT JANE AUSTEN QUOTE:")
    
    quote_display = imagery_generator.create_quote_illustration(quote['text'], quote['source'])
    print(quote_display)
    
    # Offer to create another story
    print("\nThank you for using the Jane Austen Custom Theme Storyteller!")
    another = input("\nWould you like to create another story with a different theme? (y/n): ")
    
    if another.lower().startswith('y'):
        custom_theme_storyteller()
    else:
        main_menu()

def main_menu():
    """Display and handle the main menu"""
    while True:
        clear_screen()
        
        # Display a random quote to set the mood
        display_austen_quote()
        
        print("█████████████████████████████████████████████████████████████████████")
        print("█                                                                 █")
        print("█           THE JANE AUSTEN INTERACTIVE EXPERIENCE                █")
        print("█                                                                 █")
        print("█  \"The person, be it gentleman or lady, who has not pleasure in  █")
        print("█   this program, must be intolerably stupid.\"                    █")
        print("█                                                                 █")
        print("█████████████████████████████████████████████████████████████████████")
        
        print("Select an experience:")
        print("1. Jane Austen Storytelling Experience")
        print("2. Jane Austen Quote Generator with Contextual Insights")
        print("3. Custom Theme Storyteller")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            # Run the standard storyteller
            os.system('python jane_austen_storyteller.py')
        elif choice == "2":
            # Run the quote generator
            run_quote_demo()
        elif choice == "3":
            # Run the custom theme storyteller
            custom_theme_storyteller()
        elif choice == "4":
            print("\nThank you for exploring the world of Jane Austen.")
            print("\"Till we meet again, may your happiness be as constant as my regard for you.\"")
            break
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()