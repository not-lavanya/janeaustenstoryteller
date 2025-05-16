"""
Simplified Storyteller
A streamlined version of the custom theme storyteller that removes most dependencies.
"""

import os
import sys
import time
import random
import json

class SimplifiedStoryGenerator:
    """A streamlined story generator that works with any theme"""
    
    def __init__(self):
        """Initialize the story generator"""
        self.custom_themes = []
        self.custom_settings = {}
        self.imagery_generator = SimplifiedImageryGenerator()
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_with_typing_effect(self, text, delay=0.03, variance=0.01):
        """Print text with a typewriter effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            # Random variation in typing speed for natural effect
            typing_delay = max(0.001, delay + random.uniform(-variance, variance))
            time.sleep(typing_delay)
        print()
    
    def create_character(self, gender=None, custom_name=None):
        """Generate a character"""
        if custom_name:
            name = custom_name
        else:
            # Generate a random name
            male_names = ["James", "William", "Thomas", "George", "Henry", "Edward", "John", "Charles"]
            female_names = ["Elizabeth", "Jane", "Catherine", "Mary", "Anne", "Charlotte", "Emma", "Margaret"]
            
            if gender is None:
                gender = random.choice(['male', 'female'])
                
            if gender.lower() == 'male':
                name = random.choice(male_names)
            else:
                name = random.choice(female_names)
                
            # Add a surname
            surnames = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson", "Evans", "Thomas", "Johnson"]
            name = f"{name} {random.choice(surnames)}"
        
        # Create a brief character backstory
        backstories = [
            "Born to a modest family, seeking to improve their station in life.",
            "From a wealthy background, but desires more meaningful pursuits.",
            "Has traveled extensively and formed unique perspectives on life.",
            "Raised in isolation, now experiencing the wider world.",
            "Highly educated and values intellectual pursuits.",
            "Possesses a creative talent that drives their ambitions.",
            "Has overcome significant hardship, which shaped their character.",
            "Traditional in values, but open to new experiences.",
            "Has a mysterious past they prefer to keep hidden.",
            "Known for their wit and charm in social settings."
        ]
        
        character = {
            'name': name,
            'gender': gender,
            'backstory': random.choice(backstories)
        }
        
        return character
    
    def create_enhanced_characters(self):
        """
        Create characters with enhanced customization options
        
        Returns:
            List of character dictionaries with enhanced details
        """
        print("\nCharacter Creation")
        print("This mode allows you to craft nuanced characters with specific traits.")
        
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
            "love_interest": {
                "name": "Love Interest",
                "description": "A potential or established love interest"
            },
            "rival": {
                "name": "Rival/Antagonist",
                "description": "Someone who opposes or creates conflict"
            },
            "mentor": {
                "name": "Mentor/Guide",
                "description": "An older, wiser guide"
            },
            "comic_relief": {
                "name": "Comic Relief",
                "description": "A humorous or eccentric character"
            }
        }
        
        # Virtues and flaws
        virtues = [
            "honesty", "compassion", "intelligence", "wit", "loyalty", 
            "resilience", "patience", "modesty", "kindness", "generosity"
        ]
        
        flaws = [
            "pride", "vanity", "impetuousness", "insecurity", "jealousy",
            "stubbornness", "naivety", "gossip", "selfishness", "quick temper"
        ]
        
        # Personal goals
        personal_goals = [
            "finding true love", 
            "achieving recognition",
            "securing financial success",
            "gaining knowledge",
            "finding adventure",
            "making a difference",
            "finding peace",
            "seeking justice",
            "following a passion",
            "proving themselves"
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
                print("1. Love Interest")
                print("2. Confidant/Friend")
                print("3. Rival/Antagonist")
                role_choice = input("Select role (1-3): ")
                if role_choice == "1":
                    role = "love_interest"
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
                # For love interest, ask about gender preference
                if role == "love_interest" and i > 0:
                    first_char_gender = characters[0].get('gender', 'unknown')
                    opposite = 'male' if first_char_gender == 'female' else 'female'
                    same = first_char_gender
                    
                    print(f"\nThe protagonist is {first_char_gender}. What gender should the love interest be?")
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
            for j, virtue in enumerate(virtues, 1):
                print(f"{j}. {virtue.capitalize()}")
            
            virtue_choice = input(f"Select virtue (1-{len(virtues)}): ")
            try:
                virtue_idx = int(virtue_choice) - 1
                character['virtue'] = virtues[virtue_idx]
            except (ValueError, IndexError):
                # Choose random virtue if invalid selection
                character['virtue'] = random.choice(virtues)
                print(f"Invalid selection. Assigned virtue: {character['virtue'].capitalize()}")
            
            # Let user select character flaws
            print(f"\nSelect a primary flaw for {character['name']}:")
            for j, flaw in enumerate(flaws, 1):
                print(f"{j}. {flaw.capitalize()}")
            
            flaw_choice = input(f"Select flaw (1-{len(flaws)}): ")
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
            
            goal_choice = input(f"Select goal (1-{len(personal_goals)}): ")
            try:
                goal_idx = int(goal_choice) - 1
                character['goal'] = personal_goals[goal_idx]
            except (ValueError, IndexError):
                # Choose random goal if invalid selection
                character['goal'] = random.choice(personal_goals)
                print(f"Invalid selection. Assigned goal: {character['goal'].capitalize()}")
                
            # Add character to the list
            characters.append(character)
            print(f"\nCharacter {i+1} created: {character['name']}, a {character['gender']} {role_name}")
            
        return characters
    
    def generate_custom_story_template(self, theme, settings, template_style="classic"):
        """
        Generate a story template for a custom theme
        
        Args:
            theme: Theme dictionary with name and description
            settings: Dictionary with location, season, time_period
            template_style: The narrative style to use
            
        Returns:
            A template string for the custom theme
        """
        location = settings.get('location', 'a picturesque town')
        season = settings.get('season', 'spring')
        time_period = settings.get('time_period', 'contemporary')
        
        # Basic template structures for different narrative styles
        templates = {
            "classic": f"In {location}, during the {season} of {time_period}, a tale of {theme['name']} unfolds. "
                     f"The story explores {theme['description']} through the experiences of its characters. "
                     f"As events progress, relationships develop, challenges arise, and ultimately the "
                     f"characters discover profound truths about themselves and {theme['name']}.",
                     
            "dramatic": f"The {season} air in {location} carries whispers of change. Set in {time_period}, "
                      f"this intense drama explores {theme['name']} with unflinching honesty. "
                      f"Tensions rise as characters confront their deepest fears and desires related to {theme['description']}. "
                      f"Through conflict and emotional revelations, the story builds to a powerful climax.",
                      
            "comedic": f"Welcome to {location} during a particularly eventful {season} in {time_period}. "
                     f"This lighthearted tale takes a humorous look at {theme['name']}, filled with witty banter, "
                     f"comedic misunderstandings, and absurd situations surrounding {theme['description']}. "
                     f"Through laughter and ridiculous escapades, the characters stumble toward unexpected wisdom.",
                     
            "romantic": f"Against the {season} backdrop of {location} in {time_period}, a moving romance centered on "
                      f"{theme['name']} blossoms. Hearts are tested as the characters navigate the complexities of "
                      f"{theme['description']}. Through tender moments and emotional challenges, "
                      f"the story explores how love can transform understanding and heal old wounds.",
                      
            "mystery": f"The {season} fog cloaks {location} in {time_period}, hiding secrets related to {theme['name']}. "
                     f"Strange events connected to {theme['description']} lead the characters down a path of "
                     f"discovery and danger. Clues are gradually revealed, alliances are questioned, "
                     f"and nothing is quite as it first appears in this intriguing mystery."
        }
        
        return templates.get(template_style, templates["classic"])
    
    def generate_story(self, theme_name, characters, settings, complexity_level=2, template_style="classic"):
        """Generate a narrative based on selected theme, characters and settings
        
        Args:
            theme_name: Name of the theme for the story
            characters: List of character dictionaries
            settings: Dictionary with location, season, time_period
            complexity_level: Complexity level from 1-3 (simple to complex)
            template_style: Narrative style (classic, dramatic, comedic, etc.)
            
        Returns:
            A generated story string
        """
        # Create a theme dictionary
        theme = {
            'name': theme_name,
            'description': f"the exploration of {theme_name} in various contexts"
        }
        
        # Generate the basic template
        template = self.generate_custom_story_template(theme, settings, template_style)
        
        # Create a full story based on the template, theme, and characters
        character_names = [c['name'] for c in characters]
        character_info = "\n".join([f"{c['name']}: {c['role']}, virtue: {c['virtue']}, flaw: {c['flaw']}, goal: {c['goal']}" 
                                 for c in characters])
        
        # Build a more detailed story based on characters and complexity
        story_parts = []
        
        # Introduction
        introduction = f"# {theme['name'].upper()}\n\n"
        introduction += template + "\n\n"
        story_parts.append(introduction)
        
        # Character introductions
        story_parts.append("## The Characters\n")
        for character in characters:
            story_parts.append(f"{character['name']}, {character['role'].lower()}: {character['backstory']}")
            story_parts.append(f"Known for their {character['virtue']}, but sometimes hindered by {character['flaw']}.")
            story_parts.append(f"Their primary goal: {character['goal']}.\n")
        
        # Setting description
        story_parts.append(f"## The Setting\n")
        story_parts.append(f"In {settings['location']} during {settings['season']} of {settings['time_period']}.")
        story_parts.append(f"The atmosphere is filled with possibility as our story begins.\n")
        
        # Story development depends on complexity
        story_parts.append("## The Story Unfolds\n")
        
        # Main protagonist
        protagonist = next((c for c in characters if c['role'] == "Protagonist"), characters[0])
        story_parts.append(f"{protagonist['name']} contemplates their desire for {protagonist['goal']}.")
        
        # Supporting characters and their relationships to the protagonist
        for character in characters:
            if character['role'] != "Protagonist":
                relationship = ""
                if character['role'] == "Love Interest":
                    relationship = f"feels a growing attraction to"
                elif character['role'] == "Rival/Antagonist":
                    relationship = f"finds themselves in conflict with"
                elif character['role'] == "Confidant/Friend":
                    relationship = f"confides in"
                elif character['role'] == "Mentor/Guide":
                    relationship = f"seeks guidance from"
                else:
                    relationship = f"encounters"
                    
                story_parts.append(f"{protagonist['name']} {relationship} {character['name']}, which brings {theme['name']} into sharper focus.")
        
        # Add complexity based on the level
        if complexity_level >= 2:
            story_parts.append("\n## Complications Arise\n")
            
            # Add conflicts based on character flaws
            for character in characters:
                if character['role'] != "Protagonist":
                    story_parts.append(f"{character['name']}'s {character['flaw']} creates tension when they...")
                    
                    if character['role'] == "Love Interest":
                        story_parts.append(f"misinterpret {protagonist['name']}'s intentions regarding {theme['name']}.")
                    elif character['role'] == "Rival/Antagonist":
                        story_parts.append(f"challenge {protagonist['name']}'s perspective on {theme['name']}.")
                    elif character['role'] == "Confidant/Friend":
                        story_parts.append(f"accidentally reveal a secret about {protagonist['name']}'s approach to {theme['name']}.")
                    else:
                        story_parts.append(f"present an unexpected perspective on {theme['name']}.")
        
        if complexity_level >= 3:
            # Add more complex plot developments
            story_parts.append("\n## The Plot Thickens\n")
            story_parts.append(f"As {settings['season']} progresses in {settings['location']}, the situation grows more complex.")
            
            # Create a twist based on the theme
            story_parts.append(f"An unexpected revelation about {theme['name']} forces everyone to reconsider their positions.")
            
            # Character growth moments
            for character in characters:
                story_parts.append(f"{character['name']} discovers that their {character['virtue']} gives them strength to overcome challenges related to {theme['name']}.")
        
        # Resolution
        story_parts.append("\n## Resolution\n")
        story_parts.append(f"Through their experiences with {theme['name']}, the characters find new understanding.")
        
        # Character resolutions
        for character in characters:
            story_parts.append(f"{character['name']} ultimately {random.choice(['achieves', 'reconsiders', 'transforms', 'fulfills'])} their goal of {character['goal']}.")
        
        # Final thoughts on theme
        story_parts.append(f"\nIn the end, this exploration of {theme['name']} reveals that true understanding comes through personal growth and connection with others.")
        
        # Combine all parts into a cohesive story
        full_story = "\n".join(story_parts)
        return full_story
    
    def save_story(self, story, format_type='txt', filename=None):
        """Save generated story in various formats
        
        Args:
            story: The story text to save
            format_type: Output format ('txt', 'json', or 'html')
            filename: Custom filename (without extension)
        """
        if not os.path.exists('stories'):
            os.makedirs('stories')
            
        # Create a timestamp for the filename
        timestamp = time.strftime("%Y%m%d%H%M%S")
        
        if filename:
            base_filename = f"stories/{filename}"
        else:
            base_filename = f"stories/story_{timestamp}"
            
        # Save in the requested format
        if format_type == 'json':
            # Parse the story into sections
            sections = {}
            current_section = "introduction"
            current_text = []
            
            for line in story.split('\n'):
                if line.startswith('# '):
                    # Main title
                    sections['title'] = line[2:].strip()
                elif line.startswith('## '):
                    # Save previous section
                    if current_text:
                        sections[current_section] = '\n'.join(current_text)
                        current_text = []
                    # Start new section
                    current_section = line[3:].strip().lower().replace(' ', '_')
                else:
                    current_text.append(line)
                    
            # Save final section
            if current_text:
                sections[current_section] = '\n'.join(current_text)
                
            # Write to JSON file
            with open(f"{base_filename}.json", 'w') as f:
                json.dump(sections, f, indent=2)
                
            print(f"Story saved as {base_filename}.json")
            
        elif format_type == 'html':
            # Convert story to HTML
            html_content = "<html>\n<head>\n"
            html_content += "<style>\n"
            html_content += "body { font-family: Georgia, serif; line-height: 1.6; margin: 40px; }\n"
            html_content += "h1 { color: #2c3e50; text-align: center; }\n"
            html_content += "h2 { color: #34495e; margin-top: 30px; }\n"
            html_content += "p { margin-bottom: 20px; }\n"
            html_content += "</style>\n"
            html_content += "</head>\n<body>\n"
            
            # Convert Markdown-style headers to HTML
            for line in story.split('\n'):
                if line.startswith('# '):
                    html_content += f"<h1>{line[2:].strip()}</h1>\n"
                elif line.startswith('## '):
                    html_content += f"<h2>{line[3:].strip()}</h2>\n"
                elif line.strip() == "":
                    html_content += "<br>\n"
                else:
                    html_content += f"<p>{line}</p>\n"
                    
            html_content += "</body>\n</html>"
            
            # Write to HTML file
            with open(f"{base_filename}.html", 'w') as f:
                f.write(html_content)
                
            print(f"Story saved as {base_filename}.html")
            
        else:  # Default to txt
            with open(f"{base_filename}.txt", 'w') as f:
                f.write(story)
                
            print(f"Story saved as {base_filename}.txt")
    
    def generate_story_timeline(self, story, characters, settings):
        """Generate a visual timeline of events in the story
        
        Args:
            story: The story text
            characters: List of character dictionaries
            settings: Dictionary with location, season, time_period
            
        Returns:
            A formatted timeline string
        """
        # Extract key paragraphs from the story
        paragraphs = [p for p in story.split('\n') if p.strip()]
        
        # Get season for calculating dates
        season = settings.get('season', 'spring')
        location = settings.get('location', 'unknown location')
        
        # Determine the number of timeline events based on story complexity
        story_length = len(paragraphs)
        if story_length <= 10:
            num_events = 3
        elif story_length <= 20:
            num_events = 5
        else:
            num_events = 7
            
        # Select paragraphs that likely contain significant events
        # Using a simple heuristic: regularly spaced throughout the story
        significant_paragraphs = []
        
        if num_events >= len(paragraphs):
            significant_paragraphs = list(range(len(paragraphs)))
        else:
            # Distribute events throughout the story
            step = len(paragraphs) // num_events
            for i in range(0, len(paragraphs), step):
                if len(significant_paragraphs) < num_events:
                    significant_paragraphs.append(i)
        
        # Season to month mapping
        season_months = {
            'spring': ['March', 'April', 'May'],
            'summer': ['June', 'July', 'August'],
            'autumn': ['September', 'October', 'November'],
            'winter': ['December', 'January', 'February']
        }
        
        # Get months for the specified season
        months = season_months.get(season.lower(), ['January', 'February', 'March'])
        
        # Generate timeline entries
        events = []
        protagonist = next((c for c in characters if c['role'] == "Protagonist"), characters[0])
        
        # Special first event: introduction
        introduction = f"{protagonist['name']} begins the journey into {settings.get('location', 'the story setting')}."
        events.append({
            'date': f"{months[0]} 1",
            'event': introduction
        })
        
        # Process significant paragraphs to extract events
        for idx, para_idx in enumerate(significant_paragraphs):
            # Skip the first paragraph as we already created an introduction
            if idx == 0 and para_idx == 0:
                continue
                
            paragraph = paragraphs[para_idx]
            
            # Skip headers (lines starting with #)
            if paragraph.strip().startswith('#'):
                continue
                
            # Extract a meaningful event description
            # Take first sentence if paragraph is long
            if len(paragraph) > 100:
                event_text = paragraph.split('.')[0] + "."
            else:
                event_text = paragraph
                
            # Cap event text length
            if len(event_text) > 80:
                event_text = event_text[:77] + "..."
            
            # Generate a date (distribute throughout the season)
            month = months[min(idx % 3, 2)]  # Cycle through the 3 months
            day = (idx * 7 + 5) % 28 + 1  # Days between 1-28
            
            events.append({
                'date': f"{month} {day}",
                'event': event_text
            })
        
        # Add a conclusion event
        conclusion_options = [
            f"The events in {location} reach their conclusion.",
            f"The story in {location} comes to a resolution.",
            f"Our characters find resolution to their journey in {location}.",
            f"The tale of {settings.get('time_period', 'this time')} in {location} concludes."
        ]
        
        conclusion = {
            'date': f"{months[2]} 28",
            'event': random.choice(conclusion_options)
        }
        events.append(conclusion)
        
        # Format the timeline
        timeline_width = 70
        timeline = "┌" + "─" * timeline_width + "┐\n"
        timeline += "│" + "STORY TIMELINE".center(timeline_width) + "│\n"
        timeline += "├" + "─" * timeline_width + "┤\n"
        
        for event in events:
            date_str = event['date'].ljust(15)
            event_text = event['event']
            
            # If event text is too long, wrap it
            if len(date_str) + len(event_text) > timeline_width - 4:
                # First line with date
                timeline += "│ " + date_str + event_text[:timeline_width-len(date_str)-3] + "│\n"
                
                # Continuation lines
                remaining = event_text[timeline_width-len(date_str)-3:]
                while remaining:
                    line = remaining[:timeline_width-4]
                    remaining = remaining[timeline_width-4:]
                    timeline += "│ " + " " * 15 + line.ljust(timeline_width-17) + "│\n"
            else:
                timeline += "│ " + date_str + event_text.ljust(timeline_width-len(date_str)-3) + "│\n"
        
        timeline += "└" + "─" * timeline_width + "┘"
        
        return timeline

    def _open_custom_storyboard(self, theme, characters, settings, story):
        """
        Save story data for custom visualization and open displayimages.py
        
        Args:
            theme: The theme dictionary with name and description
            characters: List of character dictionaries
            settings: Dictionary with location, season, time_period
            story: The generated or edited story text
        """
        # Create a temporary file with story data
        import json
        import subprocess
        
        # Prepare story data
        story_data = {
            "theme": theme,
            "characters": characters,
            "settings": settings,
            "story_text": story,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Create temp directory if it doesn't exist
        if not os.path.exists('temp'):
            os.makedirs('temp')
            
        # Save story data to a JSON file
        temp_file = os.path.join('temp', 'storyboard_data.json')
        with open(temp_file, 'w') as f:
            json.dump(story_data, f, indent=2)
            
        print(f"\nStory data saved to {temp_file}")
        
        try:
            # Check if displayimages.py exists
            if os.path.exists('displayimages.py'):
                # Try to open with Visual Studio Code if available
                try:
                    # Try to open with VS Code
                    print("\nAttempting to open displayimages.py in Visual Studio Code...")
                    subprocess.Popen(['code', 'displayimages.py'])
                    print("displayimages.py should be opening in Visual Studio Code.")
                except FileNotFoundError:
                    # If VS Code command not found, try to run the file directly
                    print("\nVisual Studio Code not found, running displayimages.py directly...")
                    subprocess.Popen(['python', 'displayimages.py'])
                    print("displayimages.py launched.")
            else:
                print("\ndisplayimages.py file not found.")
                print("Please create a file named 'displayimages.py' to implement your storyboard viewer.")
                print("The story data has been saved to a temporary file for you to use.")
                
                # Try alternative viewer if available
                if os.path.exists('custom_storyboard_viewer.py'):
                    print("\nOpening alternative storyboard viewer...")
                    subprocess.Popen(['python', 'custom_storyboard_viewer.py'])
        except Exception as e:
            print(f"\nError opening displayimages.py: {e}")
    
    def generate_character_portrait(self, character):
        """Generate a decorative text portrait of a character"""
        # Create a more visual portrait frame
        width = max(len(character['name']) + 4, 30)
        
        # Top border
        portrait = "┌" + "─" * width + "┐\n"
        
        # Name header
        name_padding = (width - len(character['name'])) // 2
        portrait += "│" + " " * name_padding + character['name'] + " " * (width - len(character['name']) - name_padding) + "│\n"
        
        # Divider
        portrait += "├" + "─" * width + "┤\n"
        
        # Role
        role_text = f"Role: {character['role']}"
        portrait += "│ " + role_text + " " * (width - len(role_text) - 1) + "│\n"
        
        # Gender
        gender_text = f"Gender: {character['gender']}"
        portrait += "│ " + gender_text + " " * (width - len(gender_text) - 1) + "│\n"
        
        # Virtue
        virtue_text = f"Virtue: {character['virtue']}"
        portrait += "│ " + virtue_text + " " * (width - len(virtue_text) - 1) + "│\n"
        
        # Flaw
        flaw_text = f"Flaw: {character['flaw']}"
        portrait += "│ " + flaw_text + " " * (width - len(flaw_text) - 1) + "│\n"
        
        # Goal
        goal_text = f"Goal: {character['goal']}"
        portrait += "│ " + goal_text + " " * (width - len(goal_text) - 1) + "│\n"
        
        # Bottom border
        portrait += "└" + "─" * width + "┘"
        
        return portrait
    
    def run_custom_story_generator(self):
        """Main workflow for generating stories with custom themes"""
        self.clear_screen()
        
        # Display welcome header
        print("═" * 70)
        print("         CUSTOM THEME STORYTELLING EXPERIENCE        ")
        print("═" * 70)
        
        print("✨ CREATE YOUR OWN STORY ON ANY THEME ✨")
        print("This storyteller allows you to craft a tale on absolutely any theme you wish.")
        print("Your imagination is the only limit!")
        
        # Get custom theme from user
        theme_name = input("\nEnter ANY theme title for your story: ")
        theme_desc = input("Enter a brief description of this theme: ")
        
        # Create theme
        custom_theme = {
            'name': theme_name,
            'description': theme_desc
        }
        
        # Choose story style
        print("\nSelect a narrative style for your story:")
        print("1. Classic - traditional storytelling with balanced elements")
        print("2. Dramatic - intense emotional focus with conflicts")
        print("3. Comedic - humorous situations and witty dialogue")
        print("4. Romantic - focus on relationships and emotional connections")
        print("5. Mystery - suspense and gradual revelation of secrets")
        
        style_choice = input("\nEnter style (1-5): ")
        style_map = {
            "1": "classic",
            "2": "dramatic",
            "3": "comedic",
            "4": "romantic",
            "5": "mystery"
        }
        template_style = style_map.get(style_choice, "classic")
        
        # Get story settings
        print("\n--- STORY SETTINGS ---")
        
        # Location
        print("\nChoose a location for your story:")
        print("1. Enter a custom location")
        print("2. Select from common locations")
        
        location_choice = input("Enter choice (1-2): ")
        
        if location_choice == "1":
            selected_location = input("Enter custom location: ")
        else:
            locations = [
                "a bustling city", "a quiet village", "a coastal town",
                "a mountain retreat", "a university campus", "a desert oasis",
                "a tropical island", "a space station", "a medieval castle",
                "a futuristic metropolis"
            ]
            
            print("\nSelect a location:")
            for i, loc in enumerate(locations, 1):
                print(f"{i}. {loc}")
                
            loc_idx = input(f"Enter location (1-{len(locations)}): ")
            try:
                selected_location = locations[int(loc_idx) - 1]
            except (ValueError, IndexError):
                print("Invalid selection. Using a default location.")
                selected_location = "a picturesque town"
        
        # Season
        print("\nChoose a season for your story:")
        seasons = ["spring", "summer", "autumn", "winter"]
        for i, season in enumerate(seasons, 1):
            print(f"{i}. {season}")
            
        season_choice = input(f"Enter season (1-{len(seasons)}): ")
        try:
            selected_season = seasons[int(season_choice) - 1]
        except (ValueError, IndexError):
            print("Invalid selection. Using a default season.")
            selected_season = "spring"
        
        # Time period
        print("\nChoose a time period for your story:")
        print("1. Enter a custom time period")
        print("2. Select from common time periods")
        
        period_choice = input("Enter choice (1-2): ")
        
        if period_choice == "1":
            selected_period = input("Enter custom time period: ")
        else:
            periods = [
                "ancient times", "medieval era", "renaissance", "industrial revolution",
                "Victorian era", "1920s", "1950s", "modern day", "near future", "distant future"
            ]
            
            print("\nSelect a time period:")
            for i, period in enumerate(periods, 1):
                print(f"{i}. {period}")
                
            period_idx = input(f"Enter time period (1-{len(periods)}): ")
            try:
                selected_period = periods[int(period_idx) - 1]
            except (ValueError, IndexError):
                print("Invalid selection. Using a default time period.")
                selected_period = "contemporary"
        
        # Create settings dictionary
        settings = {
            'location': selected_location,
            'season': selected_season,
            'time_period': selected_period
        }
        
        # Create characters
        print("\n--- CHARACTER CREATION ---")
        characters = self.create_enhanced_characters()
        
        # Complexity level
        print("\nSelect story complexity level:")
        print("1. Simple - straightforward narrative")
        print("2. Standard - more developed plot and characters")
        print("3. Complex - detailed plot with multiple developments")
        
        complexity_choice = input("Enter complexity (1-3): ")
        try:
            complexity_level = min(3, max(1, int(complexity_choice)))
        except ValueError:
            print("Invalid input. Using standard complexity.")
            complexity_level = 2
        
        print(f"\nGenerated story will use complexity level {complexity_level}.")
            
        # Generate the story
        print("\nGenerating your custom story...")
        initial_story = self.generate_story(custom_theme['name'], characters, settings, 
                                           complexity_level, template_style)
        
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
        
        # Display Story
        self.clear_screen()
        print("\n" + "=" * 70)
        print(f"YOUR CUSTOM STORY: {custom_theme['name'].upper()}")
        print("=" * 70 + "\n")
        
        print(story)
        print("\n" + "=" * 70)
        
        # Display character portraits
        print("\nCHARACTER PORTRAITS:")
        for character in characters:
            print(self.generate_character_portrait(character))
            print()
        
        # Generate and display story timeline
        print("\nSTORY TIMELINE:")
        timeline = self.generate_story_timeline(story, characters, settings)
        print(timeline)
            
        # Display options after story generation
        print("\nWhat would you like to do next?")
        print("1. Save this story")
        print("2. Open custom storyboard (saves story data for visualization)")
        print("3. Exit")
            
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
            
            if custom_filename:
                self.save_story(story, selected_format, custom_filename)
            else:
                self.save_story(story, selected_format)
                
            # After saving, ask if they want to do something else
            print("\nStory saved successfully!")
            next_action = input("\nWould you like to open the custom storyboard? (yes/no): ")
            
            if next_action.lower().startswith('y'):
                # Redirect to custom storyboard
                self._open_custom_storyboard(custom_theme, characters, settings, story)
                
        elif choice == '2':
            # Open custom storyboard directly
            self._open_custom_storyboard(custom_theme, characters, settings, story)
            
        print("\nThank you for using the Custom Theme Storytelling Experience!")


class SimplifiedImageryGenerator:
    """A placeholder imagery generator that creates text-based visualizations"""
    
    def create_story_header(self, theme, location, season):
        """Create a text header for the story"""
        header = "╔" + "═" * 68 + "╗\n"
        header += "║" + f"{theme}".center(68) + "║\n"
        header += "║" + f"A tale set in {location} during {season}".center(68) + "║\n"
        header += "╚" + "═" * 68 + "╝"
        return header
    
    def create_ornamental_divider(self, style="standard"):
        """Create a decorative divider"""
        if style == "floral":
            return "✿" * 35
        else:
            return "─" * 70


def run_simplified_storyteller():
    """Run the simplified storyteller"""
    storyteller = SimplifiedStoryGenerator()
    storyteller.run_custom_story_generator()
    

if __name__ == "__main__":
    run_simplified_storyteller()