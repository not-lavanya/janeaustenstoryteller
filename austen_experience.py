"""
Jane Austen Interactive Experience
Main menu for accessing various Jane Austen inspired features with enhanced visual elements.
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

# Import text animations demo (which doesn't require Kivy)
# We'll try to import this, but it's not critical if it fails
try:
    from text_animations_demo import run_text_animations_demo
except ImportError:
    # Define a fallback function if import fails
    def run_text_animations_demo():
        """Fallback function for text animations demo"""
        animator = RegencyTextAnimator()
        print("\nDemonstrating Regency-era text animations...")
        time.sleep(1)
        
        # Show a few animation examples
        animator.formal_writing_transition("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.")
        time.sleep(1)
        
        animator.animated_scene_transition(
            "The drawing room at Longbourn", 
            "The grand ballroom at Netherfield"
        )
        time.sleep(1)
        
        animator.animated_dialogue("Mr. Darcy", "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow", "looks intently at Elizabeth")
        time.sleep(1)
        
        animator.animated_chapter_heading(3, "A Most Unexpected Meeting")

# Try to import Kivy components but handle the case when they're not available
KIVY_AVAILABLE = False
try:
    # Try to import the Kivy-based demo
    from austen_visual_demo import AustenVisualDemo
    KIVY_AVAILABLE = True
except ImportError:
    # Define a placeholder for AustenVisualDemo
    AustenVisualDemo = None

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
        
        # ASCII Art Main Title
        print("""
█████████████████████████████████████████████████████████████████████
█                                                                 █
█           THE JANE AUSTEN INTERACTIVE EXPERIENCE                █
█                                                                 █
█  "The person, be it gentleman or lady, who has not pleasure in  █
█   this program, must be intolerably stupid."                    █
█                                                                 █
█████████████████████████████████████████████████████████████████████
        """)
        
        print("\nSelect an experience:")
        print("1. Jane Austen Storytelling Experience")
        print("2. Custom Theme Storyteller (Create a story on any theme)")
        print("3. Jane Austen Quote Generator with Contextual Insights")
        print("4. Regency Letter Writing Assistant")
        print("5. Regency Name Dictionary")
        print("6. Visual Imagery & Text Animation Demo")
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
            # Visual Imagery & Text Animation Demo
            clear_screen()
            display_decorative_header("Visual Imagery & Text Animation Demo")
            
            # Always run the text animations demo which works in any environment
            print_with_typing_effect("Launching the text animation demonstration...")
            time.sleep(1)
            run_text_animations_demo()
            
            # If Kivy is available, also offer the visual demo
            if KIVY_AVAILABLE and AustenVisualDemo is not None:
                clear_screen()
                display_decorative_header("Kivy Visual Imagery Demo")
                print_with_typing_effect("Would you like to also launch the Kivy visual imagery demo? (y/n)")
                if input().lower().startswith('y'):
                    AustenVisualDemo().run()
            else:
                # Just inform the user that Kivy visuals aren't available
                print_with_typing_effect("\nKivy is not available in this environment, so visual imagery features")
                print_with_typing_effect("cannot be demonstrated. The text animations you just experienced")
                print_with_typing_effect("provide the core experience of the Regency-era writing style.")
                time.sleep(2)
            
        elif choice == '7':
            # Exit
            print_with_typing_effect("\nAdieu! We hope you enjoyed your Jane Austen experience.")
            time.sleep(1)
            return
            
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
        
        # Pause after returning from a feature
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()