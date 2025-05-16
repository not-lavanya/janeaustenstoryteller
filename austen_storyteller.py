"""
Jane Austen Storytelling Experience
A command-line interactive storytelling system inspired by Jane Austen's works.
"""

import os
import random
import json
import time
from timeline_generator import TimelineGenerator

# Character generation
class CharacterGenerator:
    def __init__(self):
        # Initialize character traits dictionaries
        self.first_names = {
            'female': [
                'Elizabeth', 'Jane', 'Emma', 'Anne', 'Catherine', 'Elinor',
                'Marianne', 'Charlotte', 'Caroline', 'Georgiana', 'Harriet',
                'Lydia', 'Mary', 'Fanny', 'Isabella', 'Eleanor', 'Sophia'
            ],
            'male': [
                'Fitzwilliam', 'Charles', 'George', 'Henry', 'Edward', 'William',
                'Frederick', 'John', 'Thomas', 'James', 'Edmund', 'Robert',
                'Christopher', 'Frank', 'Philip', 'Richard', 'Arthur'
            ]
        }
        
        self.last_names = [
            'Bennet', 'Darcy', 'Bingley', 'Woodhouse', 'Knightley', 'Wentworth',
            'Elliot', 'Crawford', 'Bertram', 'Dashwood', 'Ferrars', 'Willoughby',
            'Brandon', 'Collins', 'Lucas', 'Tilney', 'Morland', 'Churchill',
            'Elton', 'Fairfax', 'Musgrove', 'Croft', 'Wickham', 'Thorpe'
        ]
        
        self.social_classes = {
            'upper': [
                'wealthy landowner', 'aristocrat', 'baronet', 'heir to a large estate',
                'person of noble birth', 'member of the peerage', 'lady of rank',
                'gentleman of fortune', 'distinguished lady of society'
            ],
            'middle': [
                'country gentleman', 'refined lady', 'respected tradesman',
                'gentleman of modest means', 'daughter of a merchant',
                'professional man', 'wife of a professional man', 'governess from a good family'
            ],
            'lower': [
                'tenant farmer', 'shopkeeper', 'craftsman', 'servant in a great house',
                'person of humble birth but good connections', 'tradesperson',
                'farmer with a small holding', 'lady\'s companion'
            ]
        }
        
        self.occupations = {
            'male': [
                'clergyman', 'naval officer', 'estate manager', 'physician',
                'barrister', 'military officer', 'magistrate', 'scholar',
                'landowner', 'merchant', 'banker', 'architect', 'gentleman farmer'
            ],
            'female': [
                'governess', 'lady\'s companion', 'accomplished musician',
                'skilled painter', 'estate mistress', 'household manager',
                'charitable worker', 'writer of letters and journals',
                'needlework expert', 'housekeeper', 'hostess of social gatherings'
            ],
            'neutral': [
                'guardian of younger siblings', 'caretaker of elderly relatives',
                'correspondent with distant connections', 'reader and intellectual',
                'manager of family affairs', 'local benefactor', 'traveler'
            ]
        }
        
        self.personality_traits = {
            'positive': [
                'witty', 'intelligent', 'amiable', 'sensible', 'charming',
                'composed', 'elegant', 'gracious', 'kind-hearted', 'refined',
                'accomplished', 'spirited', 'thoughtful', 'affectionate', 'dutiful'
            ],
            'neutral': [
                'reserved', 'private', 'contemplative', 'traditional', 'careful',
                'proper', 'conventional', 'practical', 'deliberate', 'methodical',
                'observant', 'attentive', 'modest', 'temperate', 'moderate'
            ],
            'negative': [
                'proud', 'prejudiced', 'vain', 'impulsive', 'indiscreet',
                'fanciful', 'gossiping', 'imposing', 'scheming', 'calculating',
                'envious', 'pompous', 'frivolous', 'flirtatious', 'insolent'
            ]
        }
        
        self.backstories = [
            "raised in a large family with little fortune but much affection",
            "educated abroad and recently returned to England",
            "orphaned at a young age and raised by a distant relative",
            "from a family fallen on hard times after previous prosperity",
            "seeking to restore family honor after a scandal",
            "the unexpected inheritor of a modest but comfortable property",
            "connected to influential people but personally of limited means",
            "having survived a serious illness that altered their perspective on life",
            "returned from the colonies with experiences but diminished fortune",
            "well-traveled but now settling into provincial society",
            "recovering from a broken engagement that caused much distress",
            "new to the neighborhood and subject to much speculation",
            "a childhood friend of an important local figure",
            "possessing a talent that sets them apart from typical society",
            "bearing a resemblance to someone of notorious reputation"
        ]

    def generate_regency_name(self, gender=None):
        """Generate a typical Regency era name"""
        if gender is None:
            gender = random.choice(['male', 'female'])
            
        first_name = random.choice(self.first_names[gender])
        last_name = random.choice(self.last_names)
        
        return f"{first_name} {last_name}"

    def create_character(self, gender=None, custom_name=None, include_backstory=True):
        """Generate a period-appropriate character"""
        # Randomly select gender if not specified
        if gender is None:
            gender = random.choice(['male', 'female'])
            
        # Generate name if not provided
        if custom_name:
            name = custom_name
        else:
            name = self.generate_regency_name(gender)
            
        # Select social class and appropriate occupation
        social_class_category = random.choice(['upper', 'middle', 'lower'])
        social_class = random.choice(self.social_classes[social_class_category])
        
        # Select occupation based on gender or use a neutral one
        if random.random() < 0.7:  # 70% chance of gender-specific occupation
            if gender in self.occupations:
                occupation = random.choice(self.occupations[gender])
            else:
                occupation = random.choice(self.occupations['neutral'])
        else:
            occupation = random.choice(self.occupations['neutral'])
            
        # Select personality traits
        personality_category = random.choice(['positive', 'neutral', 'negative'])
        personality = random.choice(self.personality_traits[personality_category])
        
        # Create the character dictionary
        character = {
            'name': name,
            'gender': gender,
            'social_class': social_class,
            'occupation': occupation,
            'personality': personality
        }
        
        # Add backstory if requested
        if include_backstory:
            character['backstory'] = random.choice(self.backstories)
            
        return character

# Story templates
def get_story_themes():
    """Return the list of available story themes"""
    return [
        'Romantic Courtship in Bath',
        'Social Intrigue in Country Estate',
        'Marriage Prospects in Regency England',
        'Inheritance and Social Mobility',
        'Family Honor and Reputation',
        'Provincial Life and London Society',
        'Lost Love Rekindled',
        'Secret Engagement Revealed'
    ]

def get_story_templates():
    """Return the dictionary of story templates for each theme"""
    return {
        'Romantic Courtship in Bath': """
In {season} of {time_period}, {protagonist_name}, a {protagonist_personality} {protagonist_social_class}, arrives in Bath for the social season. 
The routine of taking the waters and attending assemblies seems mundane until a chance encounter with {character1_name}, a {character1_personality} {character1_occupation}.

Their initial meeting at the Pump Room sparks both intrigue and misunderstanding. {protagonist_name}'s {protagonist_personality} nature clashes with {character1_name}'s {character1_personality} demeanor, creating a tension that neither can ignore.

As they continue to cross paths at various social gatherings, {protagonist_name} begins to see beyond the social facade that {character1_name} presents to the world. Meanwhile, well-meaning but misguided friends and relatives attempt to direct {protagonist_name}'s attention elsewhere, unaware of the growing attachment.

When a rival appears and threatens to separate them, both must overcome pride and prejudice to recognize their true feelings. The question remains: will societal expectations triumph over the whispers of the heart?
""",
        
        'Social Intrigue in Country Estate': """
At {location}, {protagonist_name}, a {protagonist_personality} {protagonist_social_class}, navigates complex social dynamics during the {season} gathering of notable families. 

The arrival of {character1_name}, rumored to possess a fortune from {character1_occupation}, sets the neighborhood abuzz with speculation. When {character1_name} brings along the mysterious {character2_name}, whispers of scandal from the past begin to circulate.

{protagonist_name}, with a keen sense of observation, notices subtle interactions that others miss. A dropped letter, a hushed conversation in the library, meaningful glances exchanged across the drawing room - all suggest that someone at {location} harbors a secret that could ruin reputations.

As {protagonist_name} pieces together the truth, moral questions arise: Should past indiscretions define one's future? Is protecting family honor worth the sacrifice of individual happiness? And most importantly, who can be trusted when appearances so often deceive?
""",
        
        'Marriage Prospects in Regency England': """
In {time_period}, during a particularly eventful {season}, {protagonist_name} faces mounting pressure to secure an advantageous match. As a {protagonist_social_class} with {protagonist_personality} inclinations, the marriage market seems more a battlefield than a path to happiness.

The arrival of {character1_name} to the neighborhood presents an opportunity that {protagonist_name}'s family eagerly encourages. With connections to {character1_occupation} and considerable property, {character1_name} represents security and respectability.

However, {protagonist_name}'s heart is drawn to the less conventional {character2_name}, whose {character2_personality} spirit and modest position as a {character2_occupation} make them an unsuitable match in the eyes of society.

As balls and dinner parties unfold at {location}, {protagonist_name} must navigate family expectations, financial realities, and the quiet longings of the heart. Will prudence triumph over passion, or can {protagonist_name} find a way to reconcile duty with desire?
""",
        
        'Inheritance and Social Mobility': """
{protagonist_name}, a {protagonist_personality} {protagonist_social_class}, receives unexpected news of an inheritance from a distant relative, altering their status and relationships forever.

Before this windfall, {protagonist_name}'s prospects as a {protagonist_occupation} seemed limited, particularly during the harsh economic realities of {season} in {time_period}. The inheritance brings not only financial security but also the attention of {character1_name}, who had previously overlooked {protagonist_name}'s existence.

As {protagonist_name} adjusts to new circumstances at {location}, suspicions arise about the sudden friendship offered by those who once showed indifference. The {character2_personality} {character2_name}, who showed kindness before fortune smiled, now appears distant.

The inheritance carries conditions that test {protagonist_name}'s principles. As social doors open and invitations flood in, the question becomes: was the former life of obscurity, though humble, more authentic than this newfound prominence built on material wealth?
""",
        
        'Family Honor and Reputation': """
In the closely connected society of {time_period}, {protagonist_name} guards the reputation of the family with vigilance. As a {protagonist_personality} {protagonist_social_class} responsible for younger siblings, every social interaction at {location} carries weight.

When rumors begin to circulate about {character1_name}'s inappropriate association with a {character1_occupation} of questionable character, {protagonist_name} fears the scandal may taint their own family by association.

The situation grows more complex when {protagonist_name}'s beloved sibling develops an attachment to {character2_name}, a relation of the very person causing such social concern. Torn between protecting the family name and allowing genuine affection to flourish, {protagonist_name} attempts to navigate the perilous waters of {time_period} society during a particularly gossipy {season}.

A crisis erupts when a midnight elopement is discovered and prevented only by {protagonist_name}'s quick thinking. But the intervention comes at a personal cost, leaving {protagonist_name} to wonder if preserving appearances is worth the sacrifice of authentic happiness.
""",
        
        'Provincial Life and London Society': """
{protagonist_name} has lived contentedly as a {protagonist_social_class} in the peaceful rhythms of provincial life near {location}. With {protagonist_personality} sensibilities and modest expectations as a {protagonist_occupation}, the small pleasures of country living have always seemed sufficient.

An unexpected invitation from {character1_name}, a distant relation with connections to high society, draws {protagonist_name} to London for the {season}. The glittering world of the capital, with its operas, exhibitions, and fashionable gatherings, presents a stark contrast to the familiar routines of home.

In London, {protagonist_name} catches the attention of the sophisticated {character2_name}, whose {character2_personality} wit and worldly experience prove both attractive and disorienting. Meanwhile, letters from home remind {protagonist_name} of simpler values and sincere attachments left behind.

As {protagonist_name} becomes increasingly comfortable in society, an unexpected revelation about {character1_name}'s motivations forces a choice: embrace the exciting but perhaps hollow pleasures of fashionable life, or return to the authentic but limited world of the provinces?
""",
        
        'Lost Love Rekindled': """
Eight years ago, {protagonist_name}, a young and {protagonist_personality} {protagonist_social_class}, was persuaded to end an engagement with the then-unestablished {character1_name}. Now, as {season} brings them unexpectedly together at {location}, both carry the scars of that separation.

In the intervening years, {protagonist_name} has maintained a quiet dignity as a {protagonist_occupation}, while {character1_name} has achieved success and recognition in {character1_occupation}, returning with both fortune and confidence.

Their circles increasingly overlap as mutual connections, unaware of their history, continuously bring them into company. {character1_name} shows particular attention to the {character2_personality} {character2_name}, perhaps as a pointed reminder of what {protagonist_name} once rejected.

As they cautiously navigate shared spaces and conversations, old feelings resurface alongside painful memories. When a moment of crisis reveals that hearts have remained constant despite time and circumstance, can pride be set aside to embrace a second chance at happiness?
""",
        
        'Secret Engagement Revealed': """
In the close-knit community surrounding {location}, {protagonist_name} has maintained a secret engagement to {character1_name} for nearly six months. As a {protagonist_personality} {protagonist_social_class} with responsibilities as a {protagonist_occupation}, public announcement has been delayed for practical reasons.

The arrival of the {character2_personality} {character2_name} during {season} threatens to complicate matters. Misinterpreting {protagonist_name}'s friendly reception as romantic interest, {character2_name} begins to pay particular attention that does not go unnoticed by the community.

When {character1_name} witnesses an innocent but apparently intimate conversation between {protagonist_name} and {character2_name}, jealousy and doubt cloud judgment, leading to a private quarrel that is overheard by the worst possible person—the neighborhood gossip.

As rumors spread and misunderstandings multiply, the secret engagement becomes public in the most mortifying way. {protagonist_name} must navigate damaged trust, family disapproval, and social scrutiny while determining if the engagement itself remains viable after such a trial.
"""
    }

# Utility functions
def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, delay=0.03, variance=0.01):
    """Print text with a typewriter effect"""
    import sys
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Calculate a slightly variable delay for natural typing feel
        typing_delay = delay + random.uniform(-variance, variance)
        typing_delay = max(0.005, typing_delay)  # Ensure delay is not negative or too small
        
        time.sleep(typing_delay)
    
    # Add a newline at the end
    print()

def format_regency_date():
    """Return a date formatted in Regency style"""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    day = random.randint(1, 28)
    month = random.choice(months)
    year = random.randint(1810, 1820)
    
    return f"the {day}{_get_day_suffix(day)} of {month}, {year}"

def _get_day_suffix(day):
    """Return the appropriate suffix for the day"""
    if 10 <= day % 100 <= 20:
        return "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return suffix

def format_as_letter(sender, recipient, content, location="Pemberley", date=None):
    """Format text as a Regency-era letter"""
    if date is None:
        date = format_regency_date()
    
    letter = f"""
{location}
{date}

My dear {recipient},

{content}

I remain, yours sincerely,
{sender}
"""
    return letter

# Main story generator class
class JaneAustenStoryGenerator:
    def __init__(self):
        self.char_generator = CharacterGenerator()
        self.timeline_generator = TimelineGenerator()
        
        self.story_themes = get_story_themes()
        self.story_templates = get_story_templates()

    def create_characters(self, num_characters):
        """Create multiple characters"""
        characters = []
        for i in range(num_characters):
            print(f"\nCreating Character {i+1}:")
            
            # Get name input
            custom_name = input("Would you like to name this character? (yes/no): ")
            
            if custom_name.lower().startswith('y'):
                name = input("Enter character name: ")
                character = self.char_generator.create_character(custom_name=name)
            else:
                character = self.char_generator.create_character()
            
            characters.append(character)
            print(f"\nCharacter {i+1}: {character['name']}")
            print(f"Class: {character['social_class']}")
            print(f"Occupation: {character['occupation']}")
            print(f"Personality: {character['personality']}")
            if 'backstory' in character:
                print(f"Backstory: {character['backstory']}")
            
        return characters

    def generate_story(self, theme, characters, settings=None):
        """Generate a narrative based on selected theme and characters"""
        # Get the appropriate template
        if theme in self.story_templates:
            template = self.story_templates[theme]
        else:
            # Fallback to a simple template if theme not found
            template = "{protagonist_name}, a {protagonist_social_class}, embarks on a journey of self-discovery."
        
        # Default settings if none provided
        if not settings:
            settings = {
                'location': random.choice([
                    'Netherfield Park', 'Longbourn Estate', 'Pemberley', 
                    'Hartfield Estate', 'Kellynch Hall', 'Mansfield Park'
                ]),
                'season': random.choice(['spring', 'summer', 'autumn', 'winter']),
                'time_period': 'the Regency era'
            }
        
        # Format the protagonist information
        protagonist = characters[0]
        protagonist_info = {
            'protagonist_name': protagonist['name'],
            'protagonist_social_class': protagonist['social_class'],
            'protagonist_personality': protagonist['personality'],
            'protagonist_occupation': protagonist['occupation']
        }
        
        # Format information about supporting characters
        supporting_chars = []
        for i, char in enumerate(characters[1:], 1):
            char_info = {
                f'character{i}_name': char['name'],
                f'character{i}_social_class': char['social_class'],
                f'character{i}_personality': char['personality'],
                f'character{i}_occupation': char['occupation']
            }
            supporting_chars.append(char_info)
        
        # Combine all formatting information
        format_info = {**protagonist_info, **settings}
        for char_info in supporting_chars:
            format_info.update(char_info)
        
        # Format the template
        try:
            story = template.format(**format_info)
        except KeyError as e:
            # Fallback in case template has placeholders we didn't provide
            print(f"Warning: Template formatting error {e}. Using simplified template.")
            story = f"{protagonist['name']}, a {protagonist['social_class']} who is {protagonist['personality']}, "
            story += f"finds adventure and romance in {settings['location']} during {settings['season']} in {settings['time_period']}."
        
        # Generate a more elaborate story by adding context
        expanded_story = self.expand_story(story, characters, settings, theme)
        
        return expanded_story

    def expand_story(self, base_story, characters, settings, theme):
        """Expand the base story with more narrative details"""
        # Create an introduction
        intro = f"In {settings['time_period']}, during a {settings['season']} at {settings['location']}, "
        intro += f"the following tale unfolds...\n\n"
        
        # Create character introductions
        char_intros = "Our cast of characters includes:\n"
        for i, char in enumerate(characters):
            role = "protagonist" if i == 0 else "supporting character"
            char_intros += f"- {char['name']}: A {char['personality']} {char['social_class']} "
            char_intros += f"who works as a {char['occupation']}.\n"
        
        # Generate a narrative based on the theme
        narrative = base_story
        
        # Add some theme-specific elaboration
        if "Romantic Courtship" in theme:
            narrative += f"\n\nThe social gatherings at {settings['location']} have become the talk of the county. "
            narrative += f"As {characters[0]['name']} navigates the expectations of society, "
            narrative += f"the heart yearns for deeper connections beyond mere social standing."
        
        elif "Social Intrigue" in theme:
            narrative += f"\n\nBehind the elegant façades of {settings['location']}, whispers and secrets "
            narrative += f"circulate like the evening breeze. {characters[0]['name']} must discern "
            narrative += f"truth from falsehood as alliances form and dissolve with each passing day."
        
        elif "Marriage Prospects" in theme:
            narrative += f"\n\nThe question of matrimony weighs heavily on {characters[0]['name']}'s mind. "
            narrative += f"A good match could secure comfort and status, but at what cost to personal happiness? "
            narrative += f"The season's balls and gatherings become a chessboard of strategic introductions."
            
        elif "Inheritance" in theme:
            narrative += f"\n\nThe letter that arrived at {settings['location']} has changed everything. "
            narrative += f"Now {characters[0]['name']} must reconsider every relationship and opportunity "
            narrative += f"in the light of this newfound circumstance."
        
        # Add a conclusion
        conclusion = f"\n\nAs the {settings['season']} days pass at {settings['location']}, "
        conclusion += f"the true character of each person is gradually revealed, "
        conclusion += f"demonstrating that in {settings['time_period']}, just as today, "
        conclusion += f"the human heart remains a complex mystery, guided by both reason and sentiment."
        
        # Combine all parts
        full_story = intro + char_intros + "\n\n" + narrative + conclusion
        
        return full_story
        
    def generate_story_timeline(self, story, characters, settings):
        """Generate a visual timeline of events in the story"""
        # Use the timeline generator to create a timeline
        timeline = self.timeline_generator.generate_timeline(
            story, 
            characters, 
            settings['season']
        )
        
        return timeline

    def text_to_speech(self, text, filename='story_narration.txt'):
        """Save text to a file instead of speech"""
        print("Text-to-speech functionality has been removed.")
        print(f"Saving story as text to {filename} instead.")
        
        try:
            # Simply save the text to a file
            with open(filename, 'w') as f:
                f.write(text)
            print(f"Story saved as {filename}")
            return True
        except Exception as e:
            print(f"Error saving text: {e}")
            return False

    def save_story(self, story, format_type='txt', filename=None, include_timeline=True):
        """Save generated story in various formats"""
        if filename is None:
            # Generate a default filename based on current time
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"austen_story_{timestamp}"
        
        # Ensure the filename doesn't have an extension already
        if '.' in filename:
            filename = filename.split('.')[0]
        
        # Check if we need to add timeline
        timeline_content = ""
        if include_timeline:
            try:
                # Generate timeline for the story if characters and settings are available
                # Since we don't have direct access to characters and settings here,
                # we'll extract minimal information from the story
                from_pos = story.find("Our cast of characters includes:")
                to_pos = story.find("\n\n", from_pos) if from_pos != -1 else -1
                
                if from_pos != -1 and to_pos != -1:
                    char_section = story[from_pos:to_pos]
                    # Extract character names
                    char_names = []
                    for line in char_section.split('\n'):
                        if line.startswith('-'):
                            name_end = line.find(':')
                            if name_end != -1:
                                char_name = line[2:name_end].strip()
                                char_names.append({'name': char_name})
                    
                    # Extract season
                    season = "spring"  # default
                    for s in ["spring", "summer", "autumn", "winter"]:
                        if s in story.lower():
                            season = s
                            break
                    
                    # Generate timeline
                    if char_names:
                        timeline = self.timeline_generator.generate_timeline(story, char_names, season)
                        timeline_content = f"\n\n{'-'*80}\nSTORY TIMELINE\n{'-'*80}\n\n{timeline}"
            except Exception as e:
                print(f"Warning: Couldn't generate timeline for saved file: {e}")
            
        if format_type == 'txt':
            with open(f"{filename}.txt", 'w') as file:
                file.write(story + timeline_content)
            print(f"Story saved as {filename}.txt")
            return f"{filename}.txt"
            
        elif format_type == 'json':
            # Create a structured JSON with story metadata
            story_data = {
                "title": f"Jane Austen Story - {time.strftime('%Y-%m-%d')}",
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "content": story,
                "timeline": timeline_content.strip() if timeline_content else "",
                "word_count": len(story.split())
            }
            
            with open(f"{filename}.json", 'w') as file:
                json.dump(story_data, file, indent=2)
            print(f"Story saved as {filename}.json")
            return f"{filename}.json"
            
        elif format_type == 'html':
            # Create a simple HTML document with the story
            html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Jane Austen Inspired Story</title>
    <style>
        body {{ font-family: 'Baskerville', 'Garamond', serif; margin: 40px; line-height: 1.6; }}
        .story-container {{ max-width: 800px; margin: 0 auto; }}
        h1, h2 {{ color: #5B3758; text-align: center; }}
        .story {{ white-space: pre-line; }}
        .timeline {{ white-space: pre-line; background-color: #f8f5f0; padding: 20px; border: 1px solid #d9c9b9; margin-top: 40px; }}
        .footer {{ margin-top: 40px; text-align: center; font-style: italic; }}
        .timeline-event {{ margin-bottom: 10px; }}
        .timeline-date {{ font-weight: bold; color: #5B3758; }}
    </style>
</head>
<body>
    <div class="story-container">
        <h1>A Tale in the Style of Jane Austen</h1>
        <div class="story">{story}</div>
        
        {f'<h2>Story Timeline</h2><div class="timeline">{timeline_content}</div>' if timeline_content else ''}
        
        <div class="footer">Generated on {time.strftime("%B %d, %Y")}</div>
    </div>
</body>
</html>
"""
            with open(f"{filename}.html", 'w') as file:
                file.write(html_content)
            print(f"Story saved as {filename}.html")
            return f"{filename}.html"
        
        else:
            print(f"Unsupported format: {format_type}")
            return None

    def run_story_generator(self):
        """Main story generation workflow"""
        clear_screen()
        print("""
█████████████████████████████████████████████████████████████████████
█                                                                 █
█     JANE AUSTEN INTERACTIVE STORYTELLING EXPERIENCE             █
█                                                                 █
█     "It is a truth universally acknowledged, that a reader      █
█      in possession of this program, must be in want of a story" █
█                                                                 █
█████████████████████████████████████████████████████████████████████
""")
        
        # Theme Selection
        print("\nAvailable Story Themes:")
        for i, theme in enumerate(self.story_themes, 1):
            print(f"{i}. {theme}")

        theme_choice = input("\nSelect a theme number: ")
        
        try:
            theme_idx = int(theme_choice) - 1
            selected_theme = self.story_themes[theme_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to the first theme.")
            selected_theme = self.story_themes[0]
        
        print(f"\nYou've selected: {selected_theme}")

        # Setting Selection
        print("\nNow, let's choose a setting for your story:")
        locations = [
            "Pemberley", "Longbourn", "Netherfield Park", 
            "Mansfield Park", "Kellynch Hall", "Bath", "London"
        ]
        seasons = ["spring", "summer", "autumn", "winter"]
        
        print("\nAvailable Locations:")
        for i, location in enumerate(locations, 1):
            print(f"{i}. {location}")
            
        location_choice = input("\nSelect a location number: ")
        
        try:
            location_idx = int(location_choice) - 1
            selected_location = locations[location_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to Pemberley.")
            selected_location = "Pemberley"
        
        print(f"\nYou've selected: {selected_location}")
        
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, 1):
            print(f"{i}. {season}")
            
        season_choice = input("\nSelect a season number: ")
        
        try:
            season_idx = int(season_choice) - 1
            selected_season = seasons[season_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to spring.")
            selected_season = "spring"
        
        print(f"\nYou've selected: {selected_season}")
        
        # Settings dict
        settings = {
            'location': selected_location,
            'season': selected_season,
            'time_period': 'the Regency era'
        }
        
        # Character Creation
        print("\nLet's create some characters for your story.")
        num_characters = input("How many characters would you like in your story? (1-5): ")
        
        try:
            num_chars = int(num_characters)
            num_chars = max(1, min(5, num_chars))  # Limit between 1 and 5
        except ValueError:
            print("Invalid input. Creating 2 characters by default.")
            num_chars = 2
            
        characters = self.create_characters(num_chars)
        
        # Story Generation
        print("\nGenerating your Jane Austen inspired story...")
        story = self.generate_story(selected_theme, characters, settings)
        
        # Display the story
        print("\n" + "=" * 80)
        print("\nYOUR JANE AUSTEN STORY:\n")
        print(story)
        print("\n" + "=" * 80)
        
        # Generate and display the story timeline
        print("\nGenerating Story Timeline...")
        timeline = self.generate_story_timeline(story, characters, settings)
        print(timeline)
        
        # Save Option
        save_choice = input("\nWould you like to save this story? (yes/no): ")
        if save_choice.lower().startswith('y'):
            format_options = ["txt", "json", "html"]
            print("\nAvailable formats:")
            for i, fmt in enumerate(format_options, 1):
                print(f"{i}. {fmt}")
                
            format_choice = input("\nSelect a format number: ")
            
            try:
                format_idx = int(format_choice) - 1
                selected_format = format_options[format_idx]
            except (ValueError, IndexError):
                print("Invalid selection. Defaulting to txt format.")
                selected_format = "txt"
                
            self.save_story(story, format_type=selected_format)
        
        # Save as txt option (removed text-to-speech)
        txt_choice = input("\nWould you like to save the story as a simple text file too? (yes/no): ")
        if txt_choice.lower().startswith('y'):
            txt_file = "story_narration.txt"
            success = self.text_to_speech(story, txt_file)
            if success:
                print(f"Story saved as {txt_file}.")
        
        print("\nThank you for using the Jane Austen Storytelling Experience!")

def main():
    story_generator = JaneAustenStoryGenerator()
    story_generator.run_story_generator()

if __name__ == "__main__":
    main()