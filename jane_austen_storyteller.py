"""
Jane Austen Storytelling Experience
A Python script for generating narratives in the style of Jane Austen.
"""

import os
import random
import json
import time
import re
from timeline_generator import TimelineGenerator
from story_templates import get_story_themes, get_story_templates
from enhanced_story_templates import get_enhanced_story_themes, get_enhanced_story_templates, add_enhanced_templates_to_classic
from austen_quotes import AustenQuoteGenerator
from visual_imagery import VisualImageryGenerator

# Try to import the display_images module if available
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

class JaneAustenStoryGenerator:
    def __init__(self):
        # Initialize the timeline generator
        self.timeline_generator = TimelineGenerator()
        
        # Initialize the quote generator
        self.quote_generator = AustenQuoteGenerator()
        
        # Initialize the visual imagery generator
        self.imagery_generator = VisualImageryGenerator()
        
        # Initialize properties for quote handling
        self.last_quote = None
        self.quote_style = "standard"
        self.will_animate_quote = False
        
        # Load available story themes
        self.story_themes = get_story_themes()
        
        # Character data
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
        
        # Story data
        self.story_themes = [
            'Romantic Courtship in Bath',
            'Social Intrigue in Country Estate',
            'Marriage Prospects in Regency England',
            'Inheritance and Social Mobility',
            'Family Honor and Reputation',
            'Provincial Life and London Society',
            'Lost Love Rekindled',
            'Secret Engagement Revealed'
        ]
        
        self.story_templates = self._get_story_templates()

    def _get_story_templates(self):
        """Return the dictionary of story templates for each theme"""
        # Get the original templates
        classic_templates = get_story_templates()
        
        # Get the enhanced templates
        try:
            enhanced_templates = get_enhanced_story_templates()
            # Combine classic and enhanced templates
            combined_templates = add_enhanced_templates_to_classic(classic_templates, enhanced_templates)
            
            # Update story themes list with new themes
            self.story_themes = get_enhanced_story_themes()
            
            return combined_templates
        except:
            # If there's any issue with enhanced templates, fall back to classic
            return classic_templates

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

    def create_characters(self, num_characters):
        """Create multiple characters"""
        characters = []
        for i in range(num_characters):
            print(f"\nCreating Character {i+1}:")
            
            # Get name input
            custom_name = input("Would you like to name this character? (yes/no): ")
            
            if custom_name.lower().startswith('y'):
                name = input("Enter character name: ")
                character = self.create_character(custom_name=name)
            else:
                character = self.create_character()
            
            characters.append(character)
            print(f"\nCharacter {i+1}: {character['name']}")
            print(f"Class: {character['social_class']}")
            print(f"Occupation: {character['occupation']}")
            print(f"Personality: {character['personality']}")
            if 'backstory' in character:
                print(f"Backstory: {character['backstory']}")
            
        return characters

    def generate_story(self, theme, characters, settings=None, complexity_level=2):
        """
        Generate a narrative based on selected theme and characters
        
        Args:
            theme: Story theme
            characters: List of character dictionaries
            settings: Dictionary of story settings
            complexity_level: Narrative complexity level (1-3)
                1 = Simple, straightforward narrative
                2 = Moderate complexity with some literary embellishments
                3 = Complex narrative with rich details and Austen-like prose
        """
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
        
        # Simplify the template for lower complexity levels
        if complexity_level == 1:
            template = self._simplify_template(template)
        
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
        
        # Generate a more elaborate story by adding context based on complexity level
        expanded_story = self.expand_story(story, characters, settings, theme, complexity_level)
        return expanded_story
        
    def _simplify_template(self, template):
        """Simplify a template for lower complexity levels"""
        # Split into paragraphs
        paragraphs = template.strip().split('\n\n')
        
        # Keep only essential paragraphs (first and last)
        if len(paragraphs) > 2:
            essential = [paragraphs[0], paragraphs[-1]]
            simplified = '\n\n'.join(essential)
        else:
            simplified = template
            
        # Replace complex phrases with simpler ones
        simplifications = [
            (r'navigates complex social dynamics', 'deals with society'),
            (r'mounting pressure to secure an advantageous match', 'needs to find a good match'),
            (r'whispers of scandal from the past begin to circulate', 'old rumors start to spread'),
            (r'the quiet longings of the heart', 'personal feelings'),
            (r'altering their status and relationships forever', 'changing their life'),
            (r'initial meeting at the Pump Room sparks both intrigue and misunderstanding', 
             'first meeting causes confusion')
        ]
        
        for complex_phrase, simple_phrase in simplifications:
            simplified = re.sub(complex_phrase, simple_phrase, simplified)
            
        return simplified

    def expand_story(self, base_story, characters, settings, theme, complexity_level=2):
        """
        Expand the base story with more narrative details.
        
        Args:
            base_story: The base story template
            characters: List of character dictionaries
            settings: Dictionary of story settings
            theme: Story theme
            complexity_level: Narrative complexity level (1-3)
                1 = Simple, straightforward narrative
                2 = Moderate complexity with some literary embellishments
                3 = Complex narrative with rich details and Austen-like prose
        """
        # Create an introduction
        intro = f"In {settings['time_period']}, during a {settings['season']} at {settings['location']}, "
        intro += f"the following tale unfolds...\n\n"
        
        # Create character introductions
        char_intros = "Our cast of characters includes:\n"
        for i, char in enumerate(characters):
            role = "protagonist" if i == 0 else "supporting character"
            char_intros += f"- {char['name']}: A {char['personality']} {char['social_class']} "
            char_intros += f"who works as a {char['occupation']}.\n"
            
            # Add backstory for higher complexity levels
            if complexity_level >= 2 and 'backstory' in char:
                char_intros += f"  ({char['backstory']})\n"
        
        # Generate a narrative based on the theme
        narrative = base_story
        
        # Add theme-specific elaboration based on complexity level
        theme_elaboration = ""
        if complexity_level >= 2:
            if "Romantic Courtship" in theme:
                theme_elaboration += f"\n\nThe social gatherings at {settings['location']} have become the talk of the county. "
                theme_elaboration += f"As {characters[0]['name']} navigates the expectations of society, "
                theme_elaboration += f"the heart yearns for deeper connections beyond mere social standing."
            
            elif "Social Intrigue" in theme:
                theme_elaboration += f"\n\nBehind the elegant façades of {settings['location']}, whispers and secrets "
                theme_elaboration += f"circulate like the evening breeze. {characters[0]['name']} must discern "
                theme_elaboration += f"truth from falsehood as alliances form and dissolve with each passing day."
            
            elif "Marriage Prospects" in theme:
                theme_elaboration += f"\n\nThe question of matrimony weighs heavily on {characters[0]['name']}'s mind. "
                theme_elaboration += f"A good match could secure comfort and status, but at what cost to personal happiness? "
                theme_elaboration += f"The season's balls and gatherings become a chessboard of strategic introductions."
                
            elif "Inheritance" in theme:
                theme_elaboration += f"\n\nThe letter that arrived at {settings['location']} has changed everything. "
                theme_elaboration += f"Now {characters[0]['name']} must reconsider every relationship and opportunity "
                theme_elaboration += f"in the light of this newfound circumstance."
        
        # Add additional complexity for level 3
        additional_details = ""
        if complexity_level >= 3:
            # Add detailed description of the setting
            additional_details += self._generate_setting_description(settings)
            
            # Add social commentary (classic Austen element)
            additional_details += self._generate_social_commentary(characters, settings, theme)
            
            # Add inner thoughts of the protagonist
            additional_details += self._generate_inner_thoughts(characters[0], theme)
        
        # Add a conclusion appropriate to the complexity level
        conclusion = ""
        if complexity_level == 1:
            # Simple conclusion
            conclusion = f"\n\nThe events at {settings['location']} during this {settings['season']} "
            conclusion += f"changed the lives of all involved."
        else:
            # More literary conclusion
            conclusion = f"\n\nAs the {settings['season']} days pass at {settings['location']}, "
            conclusion += f"the true character of each person is gradually revealed, "
            conclusion += f"demonstrating that in {settings['time_period']}, just as today, "
            conclusion += f"the human heart remains a complex mystery, guided by both reason and sentiment."
        
        # Combine all parts according to complexity level
        if complexity_level == 1:
            # Simplified narrative
            full_story = intro + char_intros + "\n\n" + narrative + conclusion
        elif complexity_level == 2:
            # Standard narrative with some elaboration
            full_story = intro + char_intros + "\n\n" + narrative + theme_elaboration + conclusion
        else:
            # Complex narrative with rich details
            full_story = intro + char_intros + "\n\n" + additional_details + narrative + theme_elaboration + conclusion
        
        return full_story
    
    def _generate_setting_description(self, settings):
        """Generate a detailed description of the story setting"""
        descriptions = {
            'Pemberley': f"\n\n{settings['location']}, with its stately elegance and well-maintained grounds, "
                        f"reflected the refined sensibilities of its inhabitants. The {settings['season']} air "
                        f"carried the scent of roses from the garden, where gravel paths wound between "
                        f"carefully tended hedgerows and statuary of classical design. The grand house itself "
                        f"stood as a monument to good taste rather than ostentation, its windows gleaming in "
                        f"the {settings['season']} light.\n\n",
                        
            'Longbourn': f"\n\n{settings['location']}, though modest in comparison to the great houses of the county, "
                        f"possessed a comfortable charm that spoke of generations of genteel living. The {settings['season']} "
                        f"brought new colors to the small but well-kept gardens, where the family often gathered "
                        f"in fine weather for conversation or the reading of letters.\n\n",
                        
            'Netherfield Park': f"\n\n{settings['location']} stood impressive against the {settings['season']} sky, "
                               f"its recent renovation making it the most fashionable residence in the area. "
                               f"The ornate gates opened to a sweeping drive, lined with trees that rustled "
                               f"gently in the {settings['season']} breeze, their sound mixing with the distant "
                               f"laughter of those fortunate enough to be invited to partake in its pleasures.\n\n",
                               
            'Bath': f"\n\nIn {settings['season']}, {settings['location']} became a hive of social activity, "
                   f"its Pump Room and Assembly Rooms filled with visitors seeking health, diversion, and "
                   f"advantageous connections. The honey-colored stone buildings gleamed in the changing light, "
                   f"while inside, behind lace curtains, fortunes and reputations hung in the balance of a "
                   f"glance or a whispered word.\n\n",
                   
            'London': f"\n\nThe season in {settings['location']} brought the fashionable world together in a "
                     f"whirl of carriages, calling cards, and carefully orchestrated encounters. The parks "
                     f"provided a venue for seeing and being seen, while drawing rooms became stages where "
                     f"the intricate dance of society played out against a backdrop of gilt mirrors and "
                     f"imported silk.\n\n"
        }
        
        # Return description if available, otherwise generic description
        if settings['location'] in descriptions:
            return descriptions[settings['location']]
        else:
            return f"\n\n{settings['location']} presented an idyllic scene in {settings['season']}, the perfect backdrop for the unfolding drama of human relations and societal expectations that would soon play out within its bounds.\n\n"
    
    def _generate_social_commentary(self, characters, settings, theme):
        """Generate Austen-like social commentary relevant to the story"""
        protagonist = characters[0]
        
        commentaries = [
            f"Society's expectations weighed differently upon men and women in {settings['time_period']}. "
            f"While a {protagonist['occupation']} like {protagonist['name']} might find certain doors closed, "
            f"others would open through the exercise of wit and the careful observation of human folly.\n\n",
            
            f"The distinction between pride and dignity, so often confused in {settings['time_period']}, "
            f"formed an invisible boundary that few crossed with impunity. Those who possessed true understanding "
            f"of this difference, like the more perceptive residents of {settings['location']}, recognized "
            f"that one elevated character while the other diminished it.\n\n",
            
            f"The rituals of {settings['time_period']} society—the calling cards, the careful gradations of "
            f"bowing and curtseying, the precise timing of visits—all served as a language that communicated "
            f"far more than words. In this language, {protagonist['name']} had become increasingly fluent, "
            f"reading between the lines of social protocol to discern true intent and character.\n\n",
            
            f"Money and marriage were inextricably linked in the calculations of {settings['time_period']}, "
            f"yet among the inhabitants of {settings['location']}, a silent acknowledgment existed that "
            f"happiness rarely resulted from equations that excluded affection and respect.\n\n"
        ]
        
        return random.choice(commentaries)
    
    def _generate_inner_thoughts(self, protagonist, theme):
        """Generate the inner thoughts of the protagonist"""
        thoughts = {
            'Romantic Courtship': f"{protagonist['name']}'s thoughts often turned to matters of the heart, "
                                f"though outwardly maintaining the composure expected of a {protagonist['social_class']}. "
                                f"Privately, questions arose: Was attraction built merely on first impressions, "
                                f"or did it require the foundations of character and compatibility to flourish "
                                f"into something more lasting?\n\n",
                                
            'Social Intrigue': f"Behind a carefully composed expression, {protagonist['name']} catalogued the "
                             f"inconsistencies in word and deed that suggested deeper currents beneath the "
                             f"placid surface of society. A {protagonist['personality']} nature proved both "
                             f"blessing and curse in such observations, revealing truths that others missed "
                             f"while sometimes burdening the observer with unwelcome knowledge.\n\n",
                             
            'Marriage Prospects': f"In quiet moments, {protagonist['name']} contemplated the nature of matrimony "
                                f"with both hope and trepidation. Was there a middle path between romantic "
                                f"idealism and cold pragmatism? Perhaps the wisdom lay in finding a companion "
                                f"whose character complemented one's own, creating a harmony greater than "
                                f"either could achieve alone.\n\n",
                                
            'Inheritance': f"The question of inheritance brought to {protagonist['name']}'s mind the arbitrary "
                         f"nature of fortune. Merit and wealth so rarely aligned in perfect proportion, and yet "
                         f"society insisted on judging the former by the latter. Perhaps true character revealed "
                         f"itself most clearly in how one handled both adversity and sudden prosperity.\n\n"
        }
        
        # Find matching theme or default to generic thoughts
        for theme_key, thought in thoughts.items():
            if theme_key in theme:
                return thought
                
        # Default thoughts if no specific theme match
        return f"{protagonist['name']}, though outwardly conforming to the expectations placed upon a {protagonist['social_class']}, harbored thoughts that sometimes surprised even personal confidants. The balance between societal duty and personal inclination required constant navigation, especially for one with a {protagonist['personality']} disposition.\n\n"
        
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

    def generate_story_imagery(self, theme, location, season):
        """
        Generate visual imagery for the story setting
        
        Args:
            theme: The story theme
            location: The story location
            season: The story season
            
        Returns:
            ASCII art representation of the story setting
        """
        return self.imagery_generator.create_story_header(theme, location, season)
    
    def generate_character_portrait(self, character):
        """
        Generate a text-based portrait for a character
        
        Args:
            character: Character dictionary with name, class, occupation, etc.
            
        Returns:
            ASCII art portrait of the character
        """
        return self.imagery_generator.create_character_portrait(character)
    
    def generate_event_illustration(self, event_description):
        """
        Generate an illustration for a story event
        
        Args:
            event_description: Text description of the event
            
        Returns:
            ASCII art illustration related to the event
        """
        return self.imagery_generator.create_event_illustration(event_description)
    
    def add_thematic_quote(self, story, include_context=True, quote_style="themed"):
        """
        Add a thematically relevant Jane Austen quote to the story
        
        Args:
            story: The generated story text
            include_context: Whether to include contextual information about the quote
            quote_style: Quote display style ("standard", "themed", "animated")
            
        Returns:
            The story text with an added thematic quote
        """
        # Get a thematically appropriate quote
        quote = self.quote_generator.get_thematic_quote_for_narrative(story)
        
        # Create a decorative quote display using the imagery generator based on style
        if quote_style == "themed":
            # Use themed frame based on the quote's theme
            quote_display = self.imagery_generator.get_quote_with_themed_frame(quote)
        elif quote_style == "animated":
            # Note: For animated quotes, we'll directly print it when displaying the story
            # Just create a standard frame here for the return value
            quote_display = self.imagery_generator.create_quote_illustration(
                quote['text'], 
                quote['source']
            )
        else:  # standard
            quote_display = self.imagery_generator.create_quote_illustration(
                quote['text'], 
                quote['source']
            )
        
        # Add insight if requested
        if include_context:
            insight_text = f"\nInsight: {quote['context']}"
        else:
            insight_text = ""
        
        # Add an ornamental divider and the quote to the end of the story
        divider = self.imagery_generator.create_ornamental_divider(style="floral")
        story_with_quote = story + "\n\n" + divider + "\nJANE AUSTEN WISDOM:\n" + quote_display + insight_text + "\n" + divider
        
        # Store the quote for possible animation later
        self.last_quote = quote
        self.quote_style = quote_style
        
        return story_with_quote
    
    def get_quote_by_theme(self, theme, include_context=True):
        """
        Get a quote related to a specific theme
        
        Args:
            theme: The theme to match (e.g., 'love', 'marriage', 'society')
            include_context: Whether to include contextual information
            
        Returns:
            Formatted quote with optional context
        """
        quote = self.quote_generator.get_quote_by_theme(theme)
        
        # Create a decorative quote display
        quote_display = self.imagery_generator.create_quote_illustration(
            quote['text'], 
            quote['source']
        )
        
        # Add insight if requested
        if include_context:
            quote_display += f"\nInsight: {quote['context']}"
            
        return quote_display
    
    def get_random_quote(self, include_context=True):
        """
        Get a random Jane Austen quote
        
        Args:
            include_context: Whether to include contextual information
            
        Returns:
            Formatted quote with optional context
        """
        quote = self.quote_generator.get_random_quote()
        
        # Create a decorative quote display
        quote_display = self.imagery_generator.create_quote_illustration(
            quote['text'], 
            quote['source']
        )
        
        # Add insight if requested
        if include_context:
            quote_display += f"\nInsight: {quote['context']}"
            
        return quote_display
    
    def get_available_quote_themes(self):
        """
        Get a list of available quote themes
        
        Returns:
            List of theme strings
        """
        return self.quote_generator.get_available_themes()
    
    def get_available_quote_sources(self):
        """
        Get a list of available Jane Austen works
        
        Returns:
            List of source strings
        """
        return self.quote_generator.get_available_sources()
    
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
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        
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
        
        # Display visual examples
        print("\nSample Location Imagery:")
        print(self.imagery_generator.get_location_imagery("Bath"))
        
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
        
        # Display location-specific imagery
        print(f"\nVisual representation of {selected_location}:")
        print(self.imagery_generator.get_location_imagery(selected_location))
        
        print("\nSample Season Imagery:")
        print(self.imagery_generator.get_season_imagery("spring"))
        
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
        
        # Character Creation
        num_characters = int(input("\nHow many characters would you like in your story? (1-4): ") or "2")
        num_characters = max(1, min(4, num_characters))  # Ensure between 1 and 4
        
        characters = self.create_characters(num_characters)
        
        # Story Settings
        settings = {
            'location': selected_location,
            'season': selected_season,
            'time_period': 'the Regency era'
        }
        
        # Narrative Complexity Selection
        print("\nSelect Narrative Complexity Level:")
        print("1. Simple - Straightforward narrative with basic language")
        print("2. Standard - Moderate complexity with some literary embellishments (default)")
        print("3. Complex - Rich narrative with detailed settings and Austen-like social commentary")
        
        complexity_choice = input("\nEnter complexity level (1-3): ")
        
        try:
            complexity_level = int(complexity_choice)
            if complexity_level < 1 or complexity_level > 3:
                print("Invalid selection. Using standard complexity (level 2).")
                complexity_level = 2
        except (ValueError, TypeError):
            print("Invalid input. Using standard complexity (level 2).")
            complexity_level = 2
            
        print(f"\nGenerated story will use complexity level {complexity_level}.")
            
        # Generate Story
        print("\nGenerating your Austen-inspired story...")
        story = self.generate_story(selected_theme, characters, settings, complexity_level)
        
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
        story_header = self.imagery_generator.create_story_header(selected_theme, selected_location, selected_season)
        print(story_header)
        
        print("\nYOUR JANE AUSTEN STORY:\n")
        
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
        
        # Text file saving option
        txt_choice = input("\nWould you like to save the story as a simple text file too? (yes/no): ")
        if txt_choice.lower().startswith('y'):
            txt_file = "story_narration.txt"
            success = self.text_to_speech(story, txt_file)
            if success:
                print(f"Story saved as {txt_file}")
        
        # Display options after story generation
        print("\nWhat would you like to do next?")
        print("1. Save this story")
        
        if STORYBOARD_AVAILABLE:
            print("2. View story images")
            print("3. Return to main menu")
        else:
            print("2. Return to main menu")
            
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
            if STORYBOARD_AVAILABLE:
                next_action = input("\nStory saved successfully! Would you like to view story images? (yes/no): ")
                
                if next_action.lower().startswith('y'):
                    # Show storyboard
                    # Show storyboard with the theme from run_story_generator
                    theme_to_display = getattr(self, 'selected_theme', 'Jane Austen Story') 
                    story_title = f"{theme_to_display} - A Jane Austen Tale"
                    open_storyboard(story_title, theme_to_display, characters, settings)
                    print("\nClosing image viewer will return you to the main menu.")
                
        elif choice == '2' and STORYBOARD_AVAILABLE:
            # View story images
            if STORYBOARD_AVAILABLE and 'open_storyboard' in globals():
                # Show storyboard with the theme from run_story_generator
                theme_to_display = getattr(self, 'selected_theme', 'Jane Austen Story') 
                story_title = f"{theme_to_display} - A Jane Austen Tale"
                open_storyboard(story_title, theme_to_display, characters, settings)
                print("\nClosing image viewer will return you to the main menu.")
            else:
                print("\nStoryboard viewing is not available on this system.")
            
        print("\nThank you for using the Jane Austen Storytelling Experience!")

def main():
    story_generator = JaneAustenStoryGenerator()
    story_generator.run_story_generator()

if __name__ == "__main__":
    main()