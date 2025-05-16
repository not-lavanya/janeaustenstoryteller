"""
Custom Theme Storyteller for Jane Austen Experience
Allows users to create stories with their own themes and settings
"""

import os
import time as import_time
import sys
import random
import time
from jane_austen_storyteller import JaneAustenStoryGenerator
from visual_imagery import VisualImageryGenerator
from austen_quotes import AustenQuoteGenerator

# Import display_images module if available
try:
    from display_images import open_storyboard as _open_storyboard
    STORYBOARD_AVAILABLE = True
    
    # Create a safe wrapper function
    def open_storyboard(story_title, theme, characters, settings):
        """Wrapper for the open_storyboard function from display_images"""
        _open_storyboard(story_title, theme, characters, settings)
except ImportError:
    STORYBOARD_AVAILABLE = False
    
    # Create a dummy function to avoid errors
    def open_storyboard(story_title, theme, characters, settings):
        """Dummy function when storyboard is unavailable"""
        print("Storyboard viewing is not available on this system.")

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

class CustomThemeStoryGenerator(JaneAustenStoryGenerator):
    """Extended story generator that allows for custom themes"""
    
    def __init__(self):
        # Initialize the parent class
        super().__init__()
        
        # Custom theme attributes
        self.custom_themes = []
        self.custom_settings = {}
        
    def add_custom_theme(self, theme_name, theme_description):
        """Add a custom theme with description"""
        self.custom_themes.append({
            'name': theme_name,
            'description': theme_description
        })
        return len(self.custom_themes) - 1  # Return the index of the added theme
        
    def _open_custom_storyboard(self, theme, characters, settings, story):
        """
        Open a custom storyboard for the generated story.
        This function creates a temporary file with story data and then
        redirects to a Python file that you can create later.
        
        Args:
            theme: The theme dictionary with name and description
            characters: List of character dictionaries
            settings: Dictionary with location, season, time_period
            story: The generated or edited story text
        """
        # Create a temporary file with story data for the custom storyboard viewer
        import json
        import os
        
        # Prepare story data
        story_data = {
            "theme": theme,
            "characters": characters,
            "settings": settings,
            "story_text": story,
            "timestamp": import_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Create temp directory if it doesn't exist
        if not os.path.exists('temp'):
            os.makedirs('temp')
            
        # Save story data to a temporary JSON file
        temp_file = os.path.join('temp', 'storyboard_data.json')
        with open(temp_file, 'w') as f:
            json.dump(story_data, f, indent=2)
            
        print(f"\nStory data saved to {temp_file}")
        print("Redirecting to custom storyboard viewer...")
        
        try:
            # Check if the custom storyboard viewer exists
            if os.path.exists('custom_storyboard_viewer.py'):
                # Use subprocess to run the viewer
                import subprocess
                subprocess.Popen(['python', 'custom_storyboard_viewer.py'])
                print("\nCustom storyboard viewer launched.")
                print("You can create 'custom_storyboard_viewer.py' to implement your own viewer.")
            else:
                print("\nCustom storyboard viewer not found.")
                print("You can create 'custom_storyboard_viewer.py' to implement your own viewer.")
                print("The story data has been saved to a temporary file for you to use.")
        except Exception as e:
            print(f"\nError launching custom storyboard viewer: {e}")
            print("You can manually run 'custom_storyboard_viewer.py' to view the storyboard.")
        
    def create_enhanced_characters(self):
        """
        Create characters with enhanced customization options
        Allows for more detailed character development with specific traits, 
        virtues, flaws, and personal goals
        
        Returns:
            List of character dictionaries with enhanced details
        """
        print("\nEnhanced Character Creation")
        print("This mode allows you to craft more nuanced characters with specific traits.")
        
        num_characters = input("How many characters would you like to create? (2-4): ")
        try:
            num_chars = int(num_characters)
            num_chars = max(2, min(4, num_chars))  # Ensure between 2-4
        except ValueError:
            print("Invalid input. Defaulting to 3 characters.")
            num_chars = 3
            
        characters = []
        
        # Define character role templates
        role_templates = {
            "protagonist": {
                "name": "Protagonist",
                "description": "The central character of your story"
            },
            "confidant": {
                "name": "Confidant/Friend",
                "description": "A trusted friend or family member"
            },
            "romantic_interest": {
                "name": "Romantic Interest",
                "description": "A potential or established love interest"
            },
            "rival": {
                "name": "Rival/Antagonist",
                "description": "Someone who opposes or creates conflict"
            },
            "mentor": {
                "name": "Mentor/Guardian",
                "description": "An older, wiser guide"
            },
            "comic_relief": {
                "name": "Comic Relief",
                "description": "A humorous or eccentric character"
            }
        }
        
        # Virtues and flaws - typical of Austen characters
        virtues = [
            "honesty", "compassion", "intelligence", "wit", "propriety", 
            "loyalty", "prudence", "resilience", "patience", "modesty",
            "temperance", "kindness", "generosity", "humility", "diligence"
        ]
        
        flaws = [
            "pride", "prejudice", "vanity", "impetuousness", "insecurity",
            "jealousy", "stubbornness", "naivety", "imprudence", "gossip",
            "snobbery", "excessive sensibility", "indiscretion", "selfishness", 
            "quick temper"
        ]
        
        # Personal goals common in Austen's works
        personal_goals = [
            "securing a favorable marriage", 
            "maintaining family reputation",
            "achieving financial security",
            "pursuing intellectual growth",
            "finding true companionship",
            "advancing in society",
            "preserving family estate",
            "breaking free of social constraints",
            "reconciling personal desires with duty",
            "proving oneself worthy of esteem"
        ]
        
        # Create each character with enhanced traits
        for i in range(num_chars):
            print(f"\n--- Creating Character {i+1} ---")
            
            # Choose a role if it's the first few characters
            if i == 0:
                role = "protagonist"
                role_name = "Protagonist"
            elif i == 1 and num_chars >= 2:
                print("\nWhat role should the second character play?")
                print("1. Romantic Interest")
                print("2. Confidant/Friend")
                print("3. Rival/Antagonist")
                role_choice = input("Select role (1-3): ")
                if role_choice == "1":
                    role = "romantic_interest"
                elif role_choice == "3":
                    role = "rival"
                else:
                    role = "confidant"
                role_name = role_templates[role]["name"]
            else:
                print("\nSelect a role for this character:")
                available_roles = list(role_templates.keys())
                # Remove protagonist as an option for non-first characters
                if "protagonist" in available_roles and i > 0:
                    available_roles.remove("protagonist")
                
                for j, role_key in enumerate(available_roles, 1):
                    print(f"{j}. {role_templates[role_key]['name']} - {role_templates[role_key]['description']}")
                
                role_idx = input(f"Select role (1-{len(available_roles)}): ")
                try:
                    role = available_roles[int(role_idx)-1]
                    role_name = role_templates[role]["name"]
                except (ValueError, IndexError):
                    # Default to confidant if invalid selection
                    role = "confidant" if i != 0 else "protagonist"
                    role_name = role_templates[role]["name"]
                    print(f"Invalid selection. Defaulting to {role_name}.")
            
            # Get custom name or generate one
            custom_name = input(f"\nWould you like to name this {role_name}? (yes/no): ")
            gender_preference = None
            
            if custom_name.lower().startswith('y'):
                name = input("Enter character name: ")
                
                # Ask for gender preference if name provided
                gender_query = input("Specify character gender (male/female) or press Enter for random: ")
                if gender_query.lower().startswith('m'):
                    gender_preference = 'male'
                elif gender_query.lower().startswith('f'):
                    gender_preference = 'female'
                
                # Create base character
                character = self.create_character(gender=gender_preference, custom_name=name)
            else:
                # For romantic interest, ask about gender preference
                if role == "romantic_interest" and i > 0:
                    first_char_gender = characters[0].get('gender', 'unknown')
                    opposite = 'male' if first_char_gender == 'female' else 'female'
                    same = first_char_gender
                    
                    print(f"\nThe protagonist is {first_char_gender}. What gender should the romantic interest be?")
                    print(f"1. {opposite.capitalize()} (traditional pairing)")
                    print(f"2. {same.capitalize()} (same-gender pairing)")
                    print("3. Random")
                    
                    gender_choice = input("Select gender (1-3): ")
                    if gender_choice == "1":
                        gender_preference = opposite
                    elif gender_choice == "2":
                        gender_preference = same
                
                # Create base character
                character = self.create_character(gender=gender_preference)
            
            # Add the role to the character
            character['role'] = role_name
            
            # Let user select character virtues
            print(f"\nSelect a primary virtue for {character['name']}:")
            for j, virtue in enumerate(virtues[:10], 1):  # Show first 10 virtues
                print(f"{j}. {virtue.capitalize()}")
            print("11. Other/Custom")
            
            virtue_choice = input("Select virtue (1-11): ")
            if virtue_choice == "11":
                character['virtue'] = input("Enter custom virtue: ").lower()
            else:
                try:
                    virtue_idx = int(virtue_choice) - 1
                    character['virtue'] = virtues[virtue_idx]
                except (ValueError, IndexError):
                    # Choose random virtue if invalid selection
                    character['virtue'] = random.choice(virtues)
                    print(f"Invalid selection. Assigned virtue: {character['virtue'].capitalize()}")
            
            # Let user select character flaws
            print(f"\nSelect a primary flaw for {character['name']}:")
            for j, flaw in enumerate(flaws[:10], 1):  # Show first 10 flaws
                print(f"{j}. {flaw.capitalize()}")
            print("11. Other/Custom")
            
            flaw_choice = input("Select flaw (1-11): ")
            if flaw_choice == "11":
                character['flaw'] = input("Enter custom flaw: ").lower()
            else:
                try:
                    flaw_idx = int(flaw_choice) - 1
                    character['flaw'] = flaws[flaw_idx]
                except (ValueError, IndexError):
                    # Choose random flaw if invalid selection
                    character['flaw'] = random.choice(flaws)
                    print(f"Invalid selection. Assigned flaw: {character['flaw'].capitalize()}")
            
            # Let user select personal goal
            print(f"\nSelect a personal goal for {character['name']}:")
            for j, goal in enumerate(personal_goals, 1):
                print(f"{j}. {goal.capitalize()}")
            print(f"{len(personal_goals)+1}. Other/Custom")
            
            goal_choice = input(f"Select goal (1-{len(personal_goals)+1}): ")
            if goal_choice == str(len(personal_goals)+1):
                character['goal'] = input("Enter custom goal: ")
            else:
                try:
                    goal_idx = int(goal_choice) - 1
                    character['goal'] = personal_goals[goal_idx]
                except (ValueError, IndexError):
                    # Choose random goal if invalid selection
                    character['goal'] = random.choice(personal_goals)
                    print(f"Invalid selection. Assigned goal: {character['goal']}")
            
            # Custom backstory option
            backstory_choice = input(f"\nWould you like to provide a custom backstory for {character['name']}? (yes/no): ")
            if backstory_choice.lower().startswith('y'):
                character['backstory'] = input("Enter backstory: ")
                
            # Add character to list
            characters.append(character)
            
            # Display character summary
            print(f"\nCharacter {i+1} Summary:")
            print(f"Name: {character['name']}")
            print(f"Role: {character['role']}")
            print(f"Gender: {character['gender']}")
            print(f"Social Class: {character['social_class']}")
            print(f"Occupation: {character['occupation']}")
            print(f"Personality: {character['personality']}")
            print(f"Primary Virtue: {character['virtue'].capitalize()}")
            print(f"Primary Flaw: {character['flaw'].capitalize()}")
            print(f"Personal Goal: {character['goal']}")
            if 'backstory' in character:
                print(f"Backstory: {character['backstory']}")
                
        # Return the enhanced characters
        return characters
        
    def generate_custom_story_template(self, theme, settings, template_style="classic"):
        """
        Generate a story template for a custom theme
        
        Args:
            theme: Theme dictionary with name and description
            settings: Dictionary with location, season, time_period
            template_style: The narrative style to use (classic, dramatic, comedic, etc.)
            
        Returns:
            A template string for the custom theme
        """
        # Extract theme details
        theme_name = theme['name']
        theme_description = theme['description']
        
        # Get template style if stored in theme
        if 'style' in theme:
            template_style = theme['style']
            
        # Extract settings with fallbacks for any setting imaginable
        location = settings.get('location', 'this remarkable setting')
        season = settings.get('season', 'this time')
        time_period = settings.get('time_period', 'this era')
        
        # Create the appropriate template based on style
        if template_style == "dramatic":
            template = f"""
In the {season} of {time_period}, a most remarkable tale unfolds at {location}. The atmosphere is charged with anticipation as our narrative of "{theme_name}" commences.

{theme_description}

Amidst conflict and heightened emotions, our dramatis personae emerges:
- {'{protagonist_name}'}: A {'{protagonist_personality}'} {'{protagonist_social_class}'} whose passionate nature drives our tale forward.
- {'{character1_name}'}: A {'{character1_personality}'} {'{character1_occupation}'} harboring secrets that threaten the established order.
- {'{character2_name}'}: A {'{character2_personality}'} individual serving as {'{character2_occupation}'}, whose loyalties remain to be tested.

The constraints of society clash violently with the fervent desires of the heart. A tense atmosphere permeates every interaction, every meeting, every momentary connection between our characters.

The oppressive weight of {time_period}'s expectations casts long shadows over {location}, particularly poignant in the {season} when all seems poised for dramatic transformation.

What terrible sacrifices must be made? What cherished principles will be compromised? When personal passion confronts duty, what devastating choices await our characters?
"""

        elif template_style == "comedic":
            template = f"""
The {season} at {location} during {time_period} brings with it a most amusing arrangement of circumstances. Our delightful tale of "{theme_name}" promises endless entertainment.

{theme_description}

Let us acquaint ourselves with the most colorful personalities of our comedy:
- {'{protagonist_name}'}: A {'{protagonist_personality}'} {'{protagonist_social_class}'} whose well-meaning endeavors inevitably lead to the most charming of disasters.
- {'{character1_name}'}: A {'{character1_personality}'} {'{character1_occupation}'} possessing an uncanny talent for appearing at precisely the wrong moment.
- {'{character2_name}'}: A {'{character2_personality}'} individual employed as {'{character2_occupation}'}, dispensing wisdom that is consistently misinterpreted.

Misunderstandings abound as messages are delivered to incorrect recipients, conversations are overheard but only in part, and social blunders are committed with the best of intentions.

The particular quirks of {season} at {location} only add to the confusion, while the customs of {time_period} provide abundant opportunity for the most delightful of misapprehensions.

Will our well-intentioned characters navigate this labyrinth of social errors? Or will their follies lead to unexpected but perfectly matched alliances of the heart?
"""

        elif template_style == "romantic":
            template = f"""
The tender {season} air of {time_period} envelops {location} as our heart-stirring tale of "{theme_name}" begins its gentle unfolding.

{theme_description}

The affairs of the heart center around these souls yearning for connection:
- {'{protagonist_name}'}: A {'{protagonist_personality}'} {'{protagonist_social_class}'} whose tender heart has known both joy and sorrow.
- {'{character1_name}'}: A {'{character1_personality}'} {'{character1_occupation}'} whose mere presence causes a certain quickening of pulse.
- {'{character2_name}'}: A {'{character2_personality}'} individual serving as {'{character2_occupation}'}, who understands the language of unspoken sentiments.

Stolen glances across crowded rooms, hands briefly touching during fleeting moments, and walks where words fail but hearts speak volumes.

The romantic atmosphere of {season} enhances the beauty of {location}, while the customs of {time_period} provide both sweet anticipation and agonizing restraint.

When two souls recognize in each other something profound and true, what convention could possibly stand in the way of such a divine connection?
"""

        elif template_style == "mystery":
            template = f"""
A shroud of intrigue descends upon {location} during the {season} of {time_period}. Our tale of "{theme_name}" conceals secrets within its every paragraph.

{theme_description}

The players in this game of secrets and half-truths include:
- {'{protagonist_name}'}: A {'{protagonist_personality}'} {'{protagonist_social_class}'} with uncommonly keen powers of observation.
- {'{character1_name}'}: A {'{character1_personality}'} {'{character1_occupation}'} whose past contains details that do not align with their present narrative.
- {'{character2_name}'}: A {'{character2_personality}'} individual employed as {'{character2_occupation}'}, privy to conversations never meant for public discussion.

Unexplained occurrences, missing items, unusual patterns of behavior, and conversations that cease abruptly when certain parties enter the room.

The mists and shadows of {season} cloak {location} in an atmosphere of uncertainty, while the codes of {time_period} provide perfect cover for those with something to hide.

What truths lie buried beneath the surface? When all is revealed, will anyone remain untouched by the revelations?
"""

        # Default classic style
        else:
            template = f"""
In {season} of {time_period}, our story unfolds at {location}. The theme of our narrative centers around "{theme_name}".

{theme_description}

Our cast of characters includes:
- {'{protagonist_name}'}: A {'{protagonist_personality}'} {'{protagonist_social_class}'} who serves as our central figure.
- {'{character1_name}'}: A {'{character1_personality}'} {'{character1_occupation}'} who plays a significant role.
- {'{character2_name}'}: A {'{character2_personality}'} individual known as {'{character2_occupation}'}.

As expectations and personal desires intertwine, each character must navigate the complexities of their position while true natures are revealed through the course of events.

The particular atmosphere of {season} at {location} colors the interactions, while the values of {time_period} provide both structure and challenge.

Will our characters find resolution within the bounds of propriety, or will the heart's inclinations prove stronger than expectations?
"""
        return template
        
    def run_custom_story_generator(self):
        """Main workflow for generating stories with custom themes"""
        clear_screen()
        
        print("""
█████████████████████████████████████████████████████████████████████
█                                                                 █
█        JANE AUSTEN CUSTOM THEME STORYTELLING EXPERIENCE         █
█                                                                 █
█  "I declare after all there is no enjoyment like reading! How   █
█   much sooner one tires of any thing than of a book!"           █
█                                                                 █
█████████████████████████████████████████████████████████████████████
        """)
        
        # Get custom theme from user with unlimited possibilities
        print("\n✨ CREATE YOUR OWN JANE AUSTEN STORY ON ANY THEME ✨")
        print("This storyteller allows you to craft a tale on absolutely any theme you wish.")
        print("Your imagination is the only limit - be it historical, magical, philosophical, or anything else!")
        
        theme_name = input("\nEnter ANY theme title for your story: ")
        
        print("\nNow, share a brief description of your theme:")
        print("(Feel free to be as creative, unconventional, or imaginative as you like)")
        theme_description = input("\nTheme description: ")
        
        # Select narrative style
        print("\nSelect a narrative style for your story:")
        print("1. Classic Austen (balanced narrative)")
        print("2. Dramatic (intense emotional conflicts)")
        print("3. Comedic (misunderstandings and social humor)")
        print("4. Romantic (focus on matters of the heart)")
        print("5. Mystery (secrets and intrigue)")
        
        style_choice = input("\nEnter style choice (1-5): ")
        
        # Map the choice to a style name
        style_mapping = {
            "1": "classic",
            "2": "dramatic",
            "3": "comedic", 
            "4": "romantic",
            "5": "mystery"
        }
        
        selected_style = style_mapping.get(style_choice, "classic")
        
        # Add the custom theme with the selected style
        theme_idx = self.add_custom_theme(theme_name, theme_description)
        custom_theme = self.custom_themes[theme_idx]
        
        # Add the style to the theme dictionary
        custom_theme['style'] = selected_style
        
        print(f"\nYou've selected the {selected_style.title()} narrative style.")
        
        # Setting Selection
        print("\nNow, let's create a setting for your story:")
        print("You can choose from traditional Austen-era settings or create any setting imaginable!")
        
        # Define traditional options for those who want them
        locations = [
            "Pemberley", "Longbourn", "Netherfield Park", 
            "Mansfield Park", "Kellynch Hall", "Bath", "London"
        ]
        seasons = ["spring", "summer", "autumn", "winter"]
        time_periods = [
            "the early Regency era", 
            "the height of the Regency period",
            "the late Regency era", 
            "the year 1810",
            "the aftermath of the Napoleonic Wars"
        ]
        
        # Location selection with custom option prominently featured
        print("\n📍 LOCATION:")
        print("You can select a traditional Austen location or create your own unique setting.")
        print("Traditional locations:")
        for i, location in enumerate(locations, 1):
            print(f"{i}. {location}")
        print("0. Create your own location (anywhere real or imaginary)")
        
        location_choice = input("\nEnter your choice (0-7): ")
        
        if location_choice == "0":
            selected_location = input("Enter the name of your location: ")
        else:
            try:
                location_idx = int(location_choice) - 1
                selected_location = locations[location_idx]
            except (ValueError, IndexError):
                # User entered something else, treat as custom location
                selected_location = location_choice
        
        print(f"\nLocation selected: {selected_location}")
        
        # Season or atmospheric condition
        print("\n🌤️ SEASON/ATMOSPHERE:")
        print("You can choose a traditional season or describe any atmosphere for your setting.")
        print("Traditional seasons:")
        for i, season in enumerate(seasons, 1):
            print(f"{i}. {season}")
        print("0. Create your own atmospheric condition")
        
        season_choice = input("\nEnter your choice (0-4): ")
        
        if season_choice == "0":
            selected_season = input("Describe the atmosphere or seasonal condition: ")
        else:
            try:
                season_idx = int(season_choice) - 1
                selected_season = seasons[season_idx]
            except (ValueError, IndexError):
                # Default to spring if invalid but not custom
                print("Invalid selection. Defaulting to spring.")
                selected_season = "spring"
        
        print(f"\nAtmospheric condition selected: {selected_season}")
        
        # Time period selection with custom option
        print("\n⏳ TIME PERIOD:")
        print("You can select a traditional Austen-era time period or create any time period of your choosing.")
        print("Traditional time periods:")
        for i, period in enumerate(time_periods, 1):
            print(f"{i}. {period}")
        print("0. Create your own time period (any era, real or imaginary)")
        
        period_choice = input("\nEnter your choice (0-5): ")
        
        if period_choice == "0":
            selected_period = input("Enter your desired time period: ")
        else:
            try:
                period_idx = int(period_choice) - 1
                selected_period = time_periods[period_idx]
            except (ValueError, IndexError):
                # User entered something else, treat as custom time period
                selected_period = period_choice if period_choice else "the Regency era"
        
        print(f"\nTime period selected: {selected_period}")
        
        # Store settings
        settings = {
            'location': selected_location,
            'season': selected_season,
            'time_period': selected_period
        }
        
        # Character creation
        print("\nNow, let's create characters for your story.")
        print("Would you like the standard character creation process or enhanced character development?")
        print("1. Standard (quick character generation)")
        print("2. Enhanced (more detailed character traits and backstories)")
        
        char_creation_choice = input("\nEnter your choice (1-2): ")
        enhanced_characters = char_creation_choice == "2"
        
        if enhanced_characters:
            characters = self.create_enhanced_characters()
        else:
            num_characters = input("How many characters would you like to create? (2-4): ")
            
            try:
                num_chars = int(num_characters)
                num_chars = max(2, min(4, num_chars))  # Ensure between 2-4
            except ValueError:
                print("Invalid input. Defaulting to 3 characters.")
                num_chars = 3
                
            characters = self.create_characters(num_chars)
        
        # Generate a template for the custom theme using the selected style
        template = self.generate_custom_story_template(custom_theme, settings, custom_theme.get('style', 'classic'))
        
        # Add the template to the story_templates dict temporarily
        self.story_templates[custom_theme['name']] = template
        
        # Generate complexity level
        print("\nSelect storytelling complexity level:")
        print("1. Simple, straightforward narrative")
        print("2. Moderate complexity with some literary embellishments")
        print("3. Complex narrative with rich details and Austen-like prose")
        
        complexity_choice = input("\nEnter complexity level (1-3): ")
        try:
            complexity_level = int(complexity_choice)
            complexity_level = max(1, min(3, complexity_level))  # Ensure between 1-3
        except ValueError:
            print("Invalid selection. Defaulting to moderate complexity.")
            complexity_level = 2
            
        print(f"\nGenerated story will use complexity level {complexity_level}.")
            
        # Generate the story
        print("\nGenerating your custom Austen-inspired story...")
        initial_story = self.generate_story(custom_theme['name'], characters, settings, complexity_level)
        
        # Allow user to edit the storyline
        print("\nYour initial story has been generated. Would you like to edit it before continuing?")
        edit_choice = input("Edit story? (yes/no): ").lower()
        
        if edit_choice.startswith('y'):
            print("\n=== STORY EDITING MODE ===")
            print("Your current story is displayed below. You can now make modifications.")
            print("When you're done editing, enter 'DONE' on a new line.")
            print("\n--- CURRENT STORY ---\n")
            print(initial_story)
            print("\n--- ENTER YOUR EDITED VERSION BELOW ---\n")
            
            edited_lines = []
            while True:
                line = input()
                if line == "DONE":
                    break
                edited_lines.append(line)
            
            if edited_lines:
                story = "\n".join(edited_lines)
                print("\nStory has been updated with your edits.")
            else:
                story = initial_story
                print("\nNo changes made, keeping the original story.")
        else:
            story = initial_story
            print("\nContinuing with the generated story.")
        
        # Ask about including a Jane Austen quote
        include_quote = input("\nWould you like to include a thematic Jane Austen quote with your story? (yes/no): ").lower().startswith('y')
        
        # Add thematic quote if requested
        if include_quote:
            # Ask for quote style preference
            print("\nSelect quote display style:")
            print("1. Standard frame")
            print("2. Themed frame (based on quote theme)")
            print("3. Animated display (text appears letter by letter)")
            
            style_choice = input("Enter choice (1-3): ")
            
            # Determine quote style based on user choice
            if style_choice == "2":
                quote_style = "themed"
            elif style_choice == "3":
                quote_style = "animated"
            else:
                quote_style = "standard"
                
            # Add the quote with selected style
            story_with_quote = self.add_thematic_quote(story, quote_style=quote_style)
            
            # Special handling for animated quotes
            if quote_style == "animated" and hasattr(self, 'last_quote'):
                # We'll animate the quote during display later
                self.will_animate_quote = True
            else:
                self.will_animate_quote = False
        else:
            story_with_quote = story
            self.will_animate_quote = False
        
        # Display Story with Visual Elements
        print("\n" + "="*80)
        
        # Display story header with visual imagery
        story_header = self.imagery_generator.create_story_header(custom_theme['name'], selected_location, selected_season)
        print(story_header)
        
        print("\nYOUR CUSTOM JANE AUSTEN STORY:\n")
        
        # Handle animated quotes differently
        if hasattr(self, 'will_animate_quote') and self.will_animate_quote and hasattr(self, 'last_quote') and self.last_quote:
            # Print the story without the quote (which will be animated)
            print(story)
            
            # Print a divider before the animated quote
            divider = self.imagery_generator.create_ornamental_divider(style="floral")
            print("\n" + divider)
            print("JANE AUSTEN WISDOM:")
            
            # Animate the quote
            if 'text' in self.last_quote and 'source' in self.last_quote:
                self.imagery_generator.create_animated_quote(
                    self.last_quote['text'],
                    self.last_quote['source']
                )
            
                # Add quote context if available
                if 'context' in self.last_quote:
                    print(f"\nInsight: {self.last_quote['context']}")
                
            print(divider)
        else:
            # Print the story with the quote normally
            print(story_with_quote)
        
        # Display character portraits
        print("\nCHARACTER PORTRAITS:")
        for character in characters:
            print(self.generate_character_portrait(character))
            print()
            
        print("\n" + "="*80)
        
        # Generate and display the story timeline
        print("\nGenerating Story Timeline...")
        timeline = self.generate_story_timeline(story, characters, settings)
        print(timeline)
        
        # Display options after story generation
        print("\nWhat would you like to do next?")
        print("1. Save this story")
        print("2. Open custom storyboard (redirects to a custom Python viewer)")
        
        if STORYBOARD_AVAILABLE:
            print("3. View basic story images")
            print("4. Return to main menu")
        else:
            print("3. Return to main menu")
            
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            # Save story option
            format_types = ['txt', 'json', 'html']
            
            print("\nAvailable formats:")
            for i, format_type in enumerate(format_types, 1):
                print(f"{i}. {format_type}")
                
            format_choice = input("\nSelect a format number: ")
            
            try:
                format_idx = int(format_choice) - 1
                selected_format = format_types[format_idx]
            except (ValueError, IndexError):
                print("Invalid selection. Defaulting to txt format.")
                selected_format = "txt"
                
            custom_filename = input("\nEnter a filename (or press Enter for auto-generated): ")
            # Use the version with quote if quote was added
            story_to_save = story_with_quote if include_quote else story
            
            if custom_filename:
                self.save_story(story_to_save, selected_format, custom_filename)
            else:
                self.save_story(story_to_save, selected_format)
                
            # After saving, ask if they want to do something else
            print("\nStory saved successfully!")
            next_action = input("\nWould you like to open the custom storyboard? (yes/no): ")
            
            if next_action.lower().startswith('y'):
                # Redirect to custom storyboard
                self._open_custom_storyboard(custom_theme, characters, settings, story)
                
        elif choice == '2':
            # Open custom storyboard directly
            self._open_custom_storyboard(custom_theme, characters, settings, story)
                
        elif choice == '3' and STORYBOARD_AVAILABLE:
            # View basic story images with default viewer
            if STORYBOARD_AVAILABLE and 'open_storyboard' in globals():
                story_title = f"{custom_theme['name']} - A Jane Austen Tale"
                open_storyboard(story_title, custom_theme['name'], characters, settings)
                print("\nClosing image viewer will return you to the main menu.")
            else:
                print("\nBasic storyboard viewing is not available on this system.")
            
        print("\nThank you for using the Jane Austen Custom Theme Storytelling Experience!")

def run_custom_storyteller():
    """Run the custom theme storyteller"""
    storyteller = CustomThemeStoryGenerator()
    storyteller.run_custom_story_generator()
    
if __name__ == "__main__":
    run_custom_storyteller()