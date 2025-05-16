"""
Jane Austen Quote Generator Demo
This script demonstrates the standalone usage of the Quote Generator with Contextual Insights.
"""

import os
import time
from austen_quotes import AustenQuoteGenerator
from visual_imagery import VisualImageryGenerator

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, delay=0.02, variance=0.01):
    """Print text with a typewriter effect"""
    import random
    import sys
    import time
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Random variation in typing speed for natural effect
        typing_delay = max(0.001, delay + random.uniform(-variance, variance))
        time.sleep(typing_delay)
    print()

def display_quote_header():
    """Display a decorative header for the quote display"""
    print("\n" + "❦" * 40)
    print("❦                                                      ❦")
    print("❦       JANE AUSTEN QUOTES WITH CONTEXTUAL INSIGHTS    ❦")
    print("❦                                                      ❦")
    print("❦" * 40 + "\n")

def run_quote_demo():
    """Run the Jane Austen Quote Generator demo"""
    clear_screen()
    
    # ASCII Art Title
    print("""
█████████████████████████████████████████████████████████████████████
█                                                                 █
█     JANE AUSTEN QUOTE GENERATOR WITH CONTEXTUAL INSIGHTS        █
█                                                                 █
█     "For what do we live, but to make sport for our neighbours, █
█      and laugh at them in our turn?"                            █
█                                                                 █
█████████████████████████████████████████████████████████████████████
    """)
    
    # Initialize the quote generator
    quote_generator = AustenQuoteGenerator()
    
    # Initialize the visual imagery generator
    imagery_generator = VisualImageryGenerator()
    
    # Main demo loop
    while True:
        print("\nPlease select an option:")
        print("1. Display a random Jane Austen quote")
        print("2. Show a quote by theme")
        print("3. Show available themes")
        print("4. Display a quote from a specific book")
        print("5. Show available books")
        print("6. Generate a thematic quote for a custom narrative")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            # Random quote
            display_quote_header()
            quote = quote_generator.get_random_quote()
            
            # Ask user for display style
            print("\nSelect a display style:")
            print("1. Standard frame")
            print("2. Themed frame")
            print("3. Animated quote")
            style_choice = input("\nChoose style (1-3, default: 1): ") or "1"
            
            if style_choice == "2":
                # Create themed quote display
                quote_display = imagery_generator.get_quote_with_themed_frame(quote)
                print(quote_display)
                print(f"\nInsight: {quote['context']}")
            elif style_choice == "3":
                # Create animated quote display
                imagery_generator.create_animated_quote(
                    quote['text'], 
                    quote['source']
                )
                print(f"\nInsight: {quote['context']}")
            else:
                # Create standard decorative quote display
                quote_display = imagery_generator.create_quote_illustration(
                    quote['text'], 
                    quote['source']
                )
                print(quote_display)
                print(f"\nInsight: {quote['context']}")
            
        elif choice == '2':
            # Quote by theme
            available_themes = quote_generator.get_available_themes()
            
            print("\nAvailable themes:")
            for i, theme in enumerate(available_themes, 1):
                print(f"{i}. {theme}")
                
            theme_choice = input("\nSelect a theme number: ")
            
            try:
                theme_idx = int(theme_choice) - 1
                selected_theme = available_themes[theme_idx]
                
                display_quote_header()
                quote = quote_generator.get_quote_by_theme(selected_theme)
                
                # Ask user for display style
                print("\nSelect a display style:")
                print("1. Standard frame")
                print("2. Themed frame")
                print("3. Animated quote")
                style_choice = input("\nChoose style (1-3, default: 2): ") or "2"
                
                if style_choice == "2":
                    # Create themed quote display - default for theme-based quotes
                    quote_display = imagery_generator.get_quote_with_themed_frame(quote)
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                elif style_choice == "3":
                    # Create animated quote display
                    imagery_generator.create_animated_quote(
                        quote['text'], 
                        quote['source']
                    )
                    print(f"\nInsight: {quote['context']}")
                else:
                    # Create standard decorative quote display
                    quote_display = imagery_generator.create_quote_illustration(
                        quote['text'], 
                        quote['source']
                    )
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                
                print(f"\nTheme: {selected_theme}")
                
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
                
        elif choice == '3':
            # Show available themes
            themes = quote_generator.get_available_themes()
            print("\nAvailable Quote Themes in Jane Austen's Works:")
            for theme in themes:
                print(f"- {theme}")
                
        elif choice == '4':
            # Quote by source
            available_sources = quote_generator.get_available_sources()
            
            print("\nAvailable Jane Austen works:")
            for i, source in enumerate(available_sources, 1):
                print(f"{i}. {source}")
                
            source_choice = input("\nSelect a book number: ")
            
            try:
                source_idx = int(source_choice) - 1
                selected_source = available_sources[source_idx]
                
                display_quote_header()
                quote = quote_generator.get_quote_by_source(selected_source)
                
                # Ask user for display style
                print("\nSelect a display style:")
                print("1. Standard frame")
                print("2. Themed frame")
                print("3. Animated quote")
                style_choice = input("\nChoose style (1-3, default: 1): ") or "1"
                
                if style_choice == "2":
                    # Create themed quote display
                    quote_display = imagery_generator.get_quote_with_themed_frame(quote)
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                elif style_choice == "3":
                    # Create animated quote display
                    imagery_generator.create_animated_quote(
                        quote['text'], 
                        quote['source']
                    )
                    print(f"\nInsight: {quote['context']}")
                else:
                    # Create standard decorative quote display
                    quote_display = imagery_generator.create_quote_illustration(
                        quote['text'], 
                        quote['source']
                    )
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                
                print(f"\nSource: {selected_source}")
                
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
                
        elif choice == '5':
            # Show available sources
            sources = quote_generator.get_available_sources()
            print("\nAvailable Jane Austen Works:")
            for source in sources:
                print(f"- {source}")
                
        elif choice == '6':
            # Generate thematic quote for custom narrative
            print("\nEnter a short narrative or scenario for thematic quote matching:")
            narrative = input("> ")
            
            if narrative:
                display_quote_header()
                quote = quote_generator.get_thematic_quote_for_narrative(narrative)
                
                # Ask user for display style
                print("\nSelect a display style:")
                print("1. Standard frame")
                print("2. Themed frame")
                print("3. Animated quote")
                style_choice = input("\nChoose style (1-3, default: 2): ") or "2"
                
                if style_choice == "2":
                    # Create themed quote display - default for thematic quotes
                    quote_display = imagery_generator.get_quote_with_themed_frame(quote)
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                elif style_choice == "3":
                    # Create animated quote display
                    imagery_generator.create_animated_quote(
                        quote['text'], 
                        quote['source']
                    )
                    print(f"\nInsight: {quote['context']}")
                else:
                    # Create standard decorative quote display
                    quote_display = imagery_generator.create_quote_illustration(
                        quote['text'], 
                        quote['source']
                    )
                    print(quote_display)
                    print(f"\nInsight: {quote['context']}")
                
                print(f"\nDetected theme: {quote['theme']}")
                
                # Show a relevant activity illustration with a divider
                print("\n" + imagery_generator.create_ornamental_divider(style="floral"))
                print("\nRelevant imagery for this theme:")
                activity_image = imagery_generator.create_event_illustration(quote['theme'])
                print(activity_image)
            else:
                print("No narrative provided. Please try again.")
                
        elif choice == '7':
            # Exit
            print("\nThank you for exploring Jane Austen's wisdom and wit!")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
        # Pause before next iteration
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    run_quote_demo()