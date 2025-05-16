"""
Jane Austen Interactive Experience - Text-Only Version
Main menu for accessing various Jane Austen inspired features with enhanced text animations.
This version doesn't depend on Kivy and works in all environments.
"""

import os
import time
import sys
import random
from jane_austen_storyteller import JaneAustenStoryGenerator
from austen_quotes_demo import run_quote_demo
from custom_theme_storyteller import run_custom_storyteller
from letter_writing_assistant import run_letter_assistant
from regency_name_dictionary import run_name_dictionary
from regency_text_animations import RegencyTextAnimator
from text_animations_demo import run_text_animations_demo

# Initialize the text animator
text_animator = RegencyTextAnimator()

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

def print_with_animation(text, style="standard"):
    """Print text with Regency-era animation style"""
    if style == "formal":
        text_animator.formal_writing_transition(text)
    elif style == "quill":
        text_animator.simulate_quill_writing(text)
    elif style == "narration":
        text_animator.animated_narration(text)
    else:
        # Default to simple typing effect
        print_with_typing_effect(text)

def display_decorative_header(title, width=70):
    """Display a decorative header with the given title"""
    border = "═" * width
    print("\n" + border)
    print(title.center(width))
    print(border + "\n")

def main_menu():
    """Display and handle the main menu"""
    while True:
        clear_screen()
        
        # ASCII Art Main Title - displayed with animation
        display_decorative_header("THE JANE AUSTEN INTERACTIVE EXPERIENCE")
        
        text_animator.simulate_quill_writing(
            '"The person, be it gentleman or lady, who has not pleasure in '
            'this program, must be intolerably stupid."'
        )
        print("\n")
        
        time.sleep(0.5)
        
        print("\nSelect an experience:")
        print("1. Jane Austen Storytelling Experience")
        print("2. Custom Theme Storyteller (Create a story on any theme)")
        print("3. Jane Austen Quote Generator with Contextual Insights")
        print("4. Regency Letter Writing Assistant")
        print("5. Regency Name Dictionary")
        print("6. Regency Text Animations Demonstration")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            # Run the story generator
            story_generator = JaneAustenStoryGenerator()
            story_generator.run_story_generator()
            
        elif choice == '2':
            # Run the custom theme storyteller
            run_custom_storyteller()
            
        elif choice == '3':
            # Run the quote generator demo
            run_quote_demo()
            
        elif choice == '4':
            # Run the letter writing assistant
            run_letter_assistant()
            
        elif choice == '5':
            # Run the Regency name dictionary
            run_name_dictionary()
            
        elif choice == '6':
            # Text Animations Demo
            clear_screen()
            display_decorative_header("Regency-Era Text Animations")
            
            print_with_typing_effect("Launching the text animation demonstration...")
            time.sleep(1)
            run_text_animations_demo()
            
        elif choice == '7':
            # Exit
            print_with_animation("\nAdieu! We hope you enjoyed your Jane Austen experience.", style="formal")
            time.sleep(1)
            return
            
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
        
        # Pause after returning from a feature
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()