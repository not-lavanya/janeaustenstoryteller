"""
Visual Imagery for the Jane Austen storytelling experience.
Provides ASCII art representations of locations, characters, and events.
"""

import random
import textwrap
import time
import re

class VisualImageryGenerator:
    def __init__(self):
        """Initialize the visual imagery generator with templates"""
        # Location imagery templates
        self.location_templates = {
            "Pemberley": {
                "spring": self._pemberley_spring,
                "summer": self._pemberley_summer,
                "autumn": self._pemberley_autumn,
                "winter": self._pemberley_winter,
            },
            "Bath": {
                "spring": self._bath_spring,
                "summer": self._bath_summer,
                "autumn": self._bath_autumn,
                "winter": self._bath_winter,
            },
            "London": {
                "spring": self._london_spring,
                "summer": self._london_summer,
                "autumn": self._london_autumn,
                "winter": self._london_winter,
            },
            "Longbourn": {
                "spring": self._country_house_spring,
                "summer": self._country_house_summer,
                "autumn": self._country_house_autumn,
                "winter": self._country_house_winter,
            },
            "Netherfield Park": {
                "spring": self._country_house_spring,
                "summer": self._country_house_summer,
                "autumn": self._country_house_autumn,
                "winter": self._country_house_winter,
            },
            "Mansfield Park": {
                "spring": self._country_house_spring,
                "summer": self._country_house_summer,
                "autumn": self._country_house_autumn,
                "winter": self._country_house_winter,
            },
            "Kellynch Hall": {
                "spring": self._country_house_spring,
                "summer": self._country_house_summer,
                "autumn": self._country_house_autumn,
                "winter": self._country_house_winter,
            },
        }
        
        # Event imagery functions
        self.event_functions = {
            "ball": self._ball_scene,
            "letter": self._letter_scene,
            "garden": self._garden_scene,
            "tea": self._tea_scene,
            "walk": self._walking_scene,
            "carriage": self._carriage_scene,
            "proposal": self._proposal_scene,
            "assembly": self._assembly_room_scene,
            "drawing_room": self._drawing_room_scene,
            "dinner": self._dinner_scene,
        }

    def create_location_illustration(self, location, season):
        """
        Generate an ASCII art illustration for a location in a specific season
        
        Args:
            location: Name of the location (e.g., "Pemberley", "Bath")
            season: Season name (e.g., "spring", "summer")
            
        Returns:
            ASCII art depiction of the location
        """
        # Normalize inputs
        location = location if location in self.location_templates else "Pemberley"
        season = season.lower() if season.lower() in ["spring", "summer", "autumn", "winter"] else "summer"
        
        # Get the appropriate template function
        template_func = self.location_templates[location][season]
        
        # Generate and return the illustration
        illustration = template_func()
        return f"{location} in {season.capitalize()}\n{illustration}"
        
    def get_location_imagery(self, location, season="summer"):
        """
        Get imagery for a specific location with season
        
        Args:
            location: Name of the location (e.g., "Pemberley", "Bath")
            season: Season name (default="summer")
            
        Returns:
            ASCII art depiction of the location
        """
        return self.create_location_illustration(location, season)
        
    def get_season_imagery(self, season):
        """
        Get a generic illustration for a specific season
        
        Args:
            season: Season name (e.g., "spring", "summer", "autumn", "winter")
            
        Returns:
            ASCII art depiction of the season
        """
        # Use Pemberley as a default location to show seasonal imagery
        return self.create_location_illustration("Pemberley", season)

    def create_character_illustration(self, character):
        """
        Generate an ASCII art illustration for a character
        
        Args:
            character: Dictionary with character details (name, class, gender)
            
        Returns:
            ASCII art depiction of the character
        """
        # Default to female if no gender specified
        gender = character.get("gender", "female")
        
        if gender.lower() == "male":
            illustration = self._gentleman_portrait()
        else:
            illustration = self._lady_portrait()
            
        # Add character description
        description = f"Character: {character['name']}\n"
        if 'class' in character:
            description += f"Class: {character['class']}\n"
        if 'occupation' in character:
            description += f"Occupation: {character['occupation']}\n"
        if 'personality' in character:
            description += f"Personality: {character['personality']}\n"
            
        return f"{illustration}\n{description}"
        
    def create_character_portrait(self, character):
        """
        Alias for create_character_illustration to maintain compatibility
        
        Args:
            character: Dictionary with character details
            
        Returns:
            ASCII art portrait of the character
        """
        return self.create_character_illustration(character)

    def create_event_illustration(self, event_description):
        """
        Generate an ASCII art illustration for a story event
        
        Args:
            event_description: Text description of the event
            
        Returns:
            ASCII art illustration related to the event
        """
        # Keywords to match against the event description
        event_keywords = {
            "ball": ["ball", "dance", "dancing", "assembly"],
            "letter": ["letter", "correspondence", "write", "wrote", "written"],
            "garden": ["garden", "flowers", "grounds", "walk"],
            "tea": ["tea", "breakfast", "refreshment"],
            "walk": ["walk", "stroll", "ramble", "path"],
            "carriage": ["carriage", "travel", "journey", "ride"],
            "proposal": ["proposal", "propose", "marriage", "hand", "matrimony"],
            "assembly": ["assembly", "gathering", "society", "room"],
            "drawing_room": ["drawing room", "parlor", "parlour", "sitting room"],
            "dinner": ["dinner", "dine", "meal", "supper"],
        }
        
        # Find the best match for the event description
        best_match = "drawing_room"  # Default
        best_score = 0
        
        for event_type, keywords in event_keywords.items():
            score = sum(1 for keyword in keywords if keyword.lower() in event_description.lower())
            if score > best_score:
                best_score = score
                best_match = event_type
                
        # Get the appropriate illustration function
        illustration_func = self.event_functions.get(best_match, self._drawing_room_scene)
        
        # Generate and return the illustration
        return illustration_func()

    def create_quote_illustration(self, quote_text, source):
        """
        Create a decorative frame for a Jane Austen quote
        
        Args:
            quote_text: The text of the quote
            source: Source of the quote (e.g., "Pride and Prejudice")
            
        Returns:
            Decorated quote as ASCII art
        """
        # Wrap the quote text to fit within the frame
        max_width = 60
        wrapped_lines = textwrap.wrap(quote_text, max_width)
        
        # Build the frame
        frame = []
        frame.append("╔" + "═" * (max_width + 6) + "╗")
        frame.append("║   " + " " * max_width + "   ║")
        
        for line in wrapped_lines:
            padded_line = line.ljust(max_width)
            frame.append("║   " + padded_line + "   ║")
            
        frame.append("║   " + " " * max_width + "   ║")
        frame.append("║   " + f"— {source}".rjust(max_width) + "   ║")
        frame.append("╚" + "═" * (max_width + 6) + "╝")
        
        return "\n".join(frame)
        
    def create_animated_quote(self, quote_text, source, delay=0.05):
        """
        Create an animated display of a Jane Austen quote
        
        Args:
            quote_text: The text of the quote
            source: Source of the quote (e.g., "Pride and Prejudice")
            delay: Time delay between characters for animation effect
            
        Returns:
            Complete decorated quote as ASCII art (after animation)
        """
        # Wrap the quote text to fit within the frame
        max_width = 60
        wrapped_lines = textwrap.wrap(quote_text, max_width)
        
        # Build the frame
        frame = []
        frame.append("╔" + "═" * (max_width + 6) + "╗")
        frame.append("║   " + " " * max_width + "   ║")
        
        for line in wrapped_lines:
            padded_line = line.ljust(max_width)
            frame.append("║   " + padded_line + "   ║")
            
        frame.append("║   " + " " * max_width + "   ║")
        frame.append("║   " + f"— {source}".rjust(max_width) + "   ║")
        frame.append("╚" + "═" * (max_width + 6) + "╝")
        
        # Display the empty frame first
        empty_frame = []
        empty_frame.append("╔" + "═" * (max_width + 6) + "╗")
        empty_frame.append("║   " + " " * max_width + "   ║")
        
        for _ in wrapped_lines:
            empty_frame.append("║   " + " " * max_width + "   ║")
            
        empty_frame.append("║   " + " " * max_width + "   ║")
        empty_frame.append("║   " + " " * max_width + "   ║")
        empty_frame.append("╚" + "═" * (max_width + 6) + "╝")
        
        print("\n".join(empty_frame))
        
        # Now animate the text appearing
        full_text = ""
        for i, line in enumerate(wrapped_lines):
            for char in line:
                # Find the position of the line in the frame
                line_pos = i + 2  # +2 for the top frame borders
                
                # Update the current line with one more character
                full_text += char
                padded_line = (full_text + (" " * (max_width - len(full_text)))).ljust(max_width)
                
                # Print cursor up to the line position
                print(f"\033[{len(empty_frame) - line_pos}A", end="")
                
                # Print the updated line
                print(f"║   {padded_line}   ║")
                
                # Return cursor to bottom
                print(f"\033[{len(empty_frame) - line_pos}B", end="")
                
                time.sleep(delay)
            
            # Reset for next line
            full_text = ""
        
        # Animate the source line
        source_text = f"— {source}"
        for i in range(len(source_text) + 1):
            # Print cursor up to the source line position
            print(f"\033[2A", end="")
            
            # Print the updated source line
            partial_source = source_text[:i].rjust(max_width)
            print(f"║   {partial_source}   ║")
            
            # Return cursor to bottom
            print(f"\033[2B", end="")
            
            time.sleep(delay)
        
        return "\n".join(frame)
    
    def create_story_header(self, theme, location, season):
        """
        Create a decorative header for a story with theme and location
        
        Args:
            theme: The story theme
            location: The story location
            season: The story season
            
        Returns:
            A decorated story header with thematic imagery
        """
        # Create a decorative border
        width = 70
        
        header = []
        header.append("┏" + "━" * width + "┓")
        
        # Add the story theme in a stylized format
        theme_display = f"「 {theme.upper()} 」"
        theme_padding = (width - len(theme_display)) // 2
        header.append("┃" + " " * theme_padding + theme_display + " " * (width - theme_padding - len(theme_display)) + "┃")
        
        # Add a separator
        header.append("┃" + "─" * width + "┃")
        
        # Add location and season
        location_season = f"{location} in {season.capitalize()}"
        loc_padding = (width - len(location_season)) // 2
        header.append("┃" + " " * loc_padding + location_season + " " * (width - loc_padding - len(location_season)) + "┃")
        
        # Close the header frame
        header.append("┗" + "━" * width + "┛")
        
        # Add location-specific imagery
        try:
            # Get location imagery if available
            location_art = self.create_location_illustration(location, season)
            header.append(location_art)
        except:
            # Fallback to a generic decoration if location not found
            header.append("""
            .-~-.
           /     \\
          /       \\
         /         \\
        /           \\
        \\           /
         \\         /
          \\       /
           \\     /
            '---'
            """)
            
        return "\n".join(header)
    
    def create_ornamental_divider(self, width=70, style="classic"):
        """
        Create a decorative divider for separating story sections
        
        Args:
            width: Width of the divider
            style: Divider style ("classic", "floral", "simple")
            
        Returns:
            A decorative divider ASCII art
        """
        if style == "floral":
            return "❦" * (width // 2)
        elif style == "simple":
            return "─" * width
        else:  # classic
            return "┄┄┄" + "❧" + "┄┄┄" * ((width - 7) // 3) + "❧" + "┄┄┄"
            
    def get_quote_with_themed_frame(self, quote, theme=None):
        """
        Create a quote display with a themed decorative frame
        
        Args:
            quote: Dictionary with text, source, context, and theme
            theme: Optional theme override (uses quote's theme if None)
            
        Returns:
            A decoratively framed quote with thematic elements
        """
        # Use provided theme or extract from quote
        display_theme = theme if theme else quote.get('theme', 'general')
        
        # Theme-specific decorative elements
        theme_decorations = {
            "love": {"border": "♥", "corners": ["♥", "♥", "♥", "♥"]},
            "marriage": {"border": "♦", "corners": ["♦", "♦", "♦", "♦"]},
            "pride": {"border": "⚜", "corners": ["⚜", "⚜", "⚜", "⚜"]},
            "society": {"border": "♣", "corners": ["♣", "♣", "♣", "♣"]},
            "wisdom": {"border": "★", "corners": ["★", "★", "★", "★"]},
            "perception": {"border": "✿", "corners": ["✿", "✿", "✿", "✿"]},
            "friendship": {"border": "❀", "corners": ["❀", "❀", "❀", "❀"]},
            "imagination": {"border": "✧", "corners": ["✧", "✧", "✧", "✧"]},
        }
        
        # Default decoration if theme not found
        default_decoration = {"border": "•", "corners": ["•", "•", "•", "•"]}
        decoration = theme_decorations.get(display_theme, default_decoration)
        
        # Create themed frame
        max_width = 60
        wrapped_lines = textwrap.wrap(quote['text'], max_width)
        
        # Build the frame
        frame = []
        top_border = decoration["corners"][0] + decoration["border"] * max_width + decoration["corners"][1]
        frame.append(top_border)
        
        # Add a themed header
        theme_header = f"« {display_theme.capitalize()} »"
        theme_padding = (max_width - len(theme_header)) // 2
        frame.append(decoration["border"] + " " * theme_padding + theme_header + 
                    " " * (max_width - theme_padding - len(theme_header)) + decoration["border"])
        
        # Add separator
        frame.append(decoration["border"] + "─" * max_width + decoration["border"])
        
        # Add quote text
        for line in wrapped_lines:
            padded_line = line.ljust(max_width)
            frame.append(decoration["border"] + padded_line + decoration["border"])
        
        # Add source
        frame.append(decoration["border"] + " " * max_width + decoration["border"])
        frame.append(decoration["border"] + f"— {quote['source']}".rjust(max_width) + decoration["border"])
        
        # Close frame
        bottom_border = decoration["corners"][2] + decoration["border"] * max_width + decoration["corners"][3]
        frame.append(bottom_border)
        
        return "\n".join(frame)

    # Location Illustrations
    def _pemberley_spring(self):
        return """
            .-''-.
           /      \\
          [  PEMBERLEY ]
           \\_.-,.-,_/
           /   |    \\
          /    |     \\
         /     |      \\
        (_ _ _ | _ _ _)
       /|\\    /|\\    /|\\
      / | \\  / | \\  / | \\
     /__|__\\/__|__\\/__|__\\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~   ~~~   ~  ~~~  ~    ~~~~~  ~~
      ~~  ~~   ~   ~~ ~ ~~~   ~~~
    """

    def _pemberley_summer(self):
        return """
            .-''-.
           /      \\
          [  PEMBERLEY ]
           \\_.-,.-,_/
           /   |    \\
          /    |     \\
         /     |      \\
        (_ _ _ | _ _ _)
       /|\\    /|\\    /|\\
      / | \\  / | \\  / | \\
     /__|__\\/__|__\\/__|__\\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        \\\\  \\\\      //  //
         \\\\  \\\\____//  //
          \\\\_________//
    """

    def _pemberley_autumn(self):
        return """
            .-''-.
           /      \\
          [  PEMBERLEY ]
           \\_.-,.-,_/
           /   |    \\
          /    |     \\
         /     |      \\
        (_ _ _ | _ _ _)
       /|\\    /|\\    /|\\
      / | \\  / | \\  / | \\
     /__|__\\/__|__\\/__|__\\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       * . *  *    .  *   *
     *    *   *  .    *   .  *
       .    *    .    *   .
    """

    def _pemberley_winter(self):
        return """
            .-''-.
           / SNOW \\
          [  PEMBERLEY ]
           \\_.-,.-,_/
           /   |    \\
          /    |     \\
         /     |      \\
        (_ _ _ | _ _ _)
       /|\\    /|\\    /|\\
      / | \\  / | \\  / | \\
     /__|__\\/__|__\\/__|__\\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     * * * * * * * * * * * * * * * * *
      * * * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * * * *
    """

    def _bath_spring(self):
        return """
           .-"-"-"-.
          /         \\
         |  B A T H  |
         |  _______  |
        /|_/       \\_|\\
       / |           | \\
      /  |     o     |  \\
     /___|___________|___\\
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    ~~~~~~~~~~~~~~~~~~~~~~~~~
      ~ ~ ~ HOT SPRING ~ ~ ~
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def _bath_summer(self):
        return """
           .-"-"-"-.
          /         \\
         |  B A T H  |
         |  _______  |
        /|_/       \\_|\\
       / |           | \\
      /  |     o     |  \\
     /___|___________|___\\
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    ~~~~~~~~~~~~~~~~~~~~~~~~~
      *  *  THE PUMP  *  *
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def _bath_autumn(self):
        return """
           .-"-"-"-.
          /         \\
         |  B A T H  |
         |  _______  |
        /|_/       \\_|\\
       / |           | \\
      /  |     o     |  \\
     /___|___________|___\\
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    ~~~~~~~~~~~~~~~~~~~~~~~~~
     ) ) ) ) ) ) ) ) ) ) ) )
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def _bath_winter(self):
        return """
           .-"-"-"-.
          /  SNOW   \\
         |  B A T H  |
         |  _______  |
        /|_/       \\_|\\
       / |           | \\
      /  |     o     |  \\
     /___|___________|___\\
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    |   |=|_|_|_|_|_|=|   |
    |___|=|_|_|_|_|_|=|___|
    ~~~~~~~~~~~~~~~~~~~~~~~~~
     * * * * * * * * * * * *
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def _london_spring(self):
        return """
                 /\\
                /  \\
               /    \\
              /      \\
             /        \\
            /    BIG   \\
           /     BEN    \\
          /              \\
         /                \\
        /__________________\\
            |        |
            |        |
            |        |
            |        |
            |        |
    ~~~~~~~~|~~~~~~~~|~~~~~~~~~~
         RIVER THAMES
    """

    def _london_summer(self):
        return """
                 /\\
                /  \\
               /    \\
              /      \\
             /        \\
            /    BIG   \\
           /     BEN    \\
          /              \\
         /                \\
        /__________________\\
            |        |
            |        |
            |        |
            |        |
            |        |
    ~~~~~~~~|~~~~~~~~|~~~~~~~~~~
         RIVER THAMES
    """

    def _london_autumn(self):
        return """
                 /\\
                /  \\
               /    \\
              /      \\
             /        \\
            /    BIG   \\
           /     BEN    \\
          /              \\
         /                \\
        /__________________\\
            |        |
            |        |
            |        |
            |        |
            |        |
    ~~~~~~~~|~~~~~~~~|~~~~~~~~~~
      ~~ RIVER THAMES ~~
    """

    def _london_winter(self):
        return """
                 /\\
                /  \\
               /    \\
              /      \\
             /  SNOW  \\
            /    BIG   \\
           /     BEN    \\
          /              \\
         /                \\
        /__________________\\
            |        |
            |        |
            |        |
            |        |
            |        |
    ~~~~~~~~|~~~~~~~~|~~~~~~~~~~
      ** RIVER THAMES **
    """

    def _country_house_spring(self):
        return """
             _____________
            /             \\
           /_______________\\
           |  _        _  |
           | | |      | | |
           | |_|      |_| |
           |               |
          /|   COUNTRY    |\\
         / |     HOUSE    | \\
        /__|_______________|__\\
              |         |
              |         |
       _______|_________|_______
      /                          \\
     /____________________________\\
     |                            |
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
     <><>    <><>    <><>    <><>
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    """

    def _country_house_summer(self):
        return """
             _____________
            /             \\
           /_______________\\
           |  _        _  |
           | | |      | | |
           | |_|      |_| |
           |               |
          /|   COUNTRY    |\\
         / |     HOUSE    | \\
        /__|_______________|__\\
              |         |
              |         |
       _______|_________|_______
      /                          \\
     /____________________________\\
     |                            |
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
     \\\\      //      \\\\     //
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    """

    def _country_house_autumn(self):
        return """
             _____________
            /             \\
           /_______________\\
           |  _        _  |
           | | |      | | |
           | |_|      |_| |
           |               |
          /|   COUNTRY    |\\
         / |     HOUSE    | \\
        /__|_______________|__\\
              |         |
              |         |
       _______|_________|_______
      /                          \\
     /____________________________\\
     |                            |
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
       * . * . * . * . * . * . *
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    """

    def _country_house_winter(self):
        return """
             _____________
            /    SNOW     \\
           /_______________\\
           |  _        _  |
           | | |      | | |
           | |_|      |_| |
           |               |
          /|   COUNTRY    |\\
         / |     HOUSE    | \\
        /__|_______________|__\\
              |         |
              |         |
       _______|_________|_______
      /                          \\
     /____________________________\\
     |                            |
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
     * * * * * * * * * * * * * * * *
    ~~~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    """

    # Character Illustrations
    def _gentleman_portrait(self):
        portraits = [
            """
          ,------.
         (  o  o  )
         |   ^    |
         |  \\_/   |
          \\ ___ /
           `---'
            /|\\
           / | \\
           | | |
          _| | |_
        GENTLEMAN
            """,
            """
            _,._
           /_,-'\`-.__,
          \\.'     `--.
          /     ,--.  `
         /_,--'    `-. \\
         `--.         `'--.
            |        |\\    \\
            |  GENTN |\\\\    \\
        _.-'|________|.\\\\    \\
       <____|        |_/_____|>
        `--.`.______,'--'   /
            |       -'      |
    """]
        return random.choice(portraits)

    def _lady_portrait(self):
        portraits = [
            """
           ,---.
          (  o o )
          |  (_) |
          |      |
          |\\_____/
          |       \\
         (_)       \\
          |       (_)
          |         |
         /|         |\\
        / |         | \\
            LADY
            """,
            """
            ,----.
           (o  o  )
           |  \\/  |
           \\     /
           /`---'\\
          / /| |\\ \\
         / / | | \\ \\
        /,'  |_|  `.\\
             LADY
            """]
        return random.choice(portraits)

    # Event Illustrations
    def _ball_scene(self):
        return """
      ___________________   ________________
     /                   \\ /                \\
    |                     |                  |
    |   O           O     |     O       O    |
    |  /|\\         /|\\    |    /|\\     /|\\   |
    |  / \\         / \\    |    / \\     / \\   |
    |                     |                  |
    |                     |                  |
    |      O     O        |  O        O      |
    |     /|\\   /|\\       | /|\\      /|\\     |
    |     / \\   / \\       | / \\      / \\     |
    |_____________________|__________________|
               THE BALL
    """
    
    def _letter_scene(self):
        return """
           .-~~-.
          /      \\
        .'        '.
       (            )
        '.        .'
          '.    .'
            )  (
           /    \\
          /      \\
         /        \\
        /          \\
        
    Dear Sir/Madam,
    
    I write to inform you...
    
    Yours faithfully,
    """
        
    def _garden_scene(self):
        return """
           . . . .
        .  \\|/  .  . 
    - --@-- * -- * ---
        '  /|\\  ' ' 
          // \\\\
         //   \\\\
        @/     \\@
        |       |
        |       |
        |       |
    ~~~~~~~~~~~~~~~~~~~~~~~~~
        THE GARDEN
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """
        
    def _tea_scene(self):
        return """
            )  (
           (   ) )
            ) ( (
          _______)_
       .-'---------|  
      ( C|/\\/\\/\\/\\/|
       '-./\\/\\/\\/\\/|
         '_________'
          '-------'
    
    ~~ TEA SERVICE ~~
    """
        
    def _walking_scene(self):
        return """
              O      O
             /|\\    /|\\
             / \\    / \\
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        \\\\\\\\     THE PATH    ////
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
             |\\    /|
             |/    \\|
             |      |
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
        
    def _carriage_scene(self):
        return """
         _______________________
        |  _________________  |
        | |                 | |
        | |_________________| |
        |  ___ ___ ___ ___  | |
        | |___X___X___X___| | |
        |_______________________|
        |                       |
        | |                   | |
           o               o
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          THE CARRIAGE
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
        
    def _proposal_scene(self):
        return """
                 O
                /|\\
                / \\
               /   \\
              /     \\
                    O
                   /|
                   / \\
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
            THE PROPOSAL
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
        
    def _assembly_room_scene(self):
        return """
        +--------------------------------+
        |                                |
        |       O          O    O        |
        |      /|\\        /|\\  /|\\       |
        |      / \\        / \\  / \\       |
        |                                |
        |  O          O                  |
        | /|\\        /|\\                 |
        | / \\        / \\                 |
        |                                |
        |              O      O          |
        |             /|\\    /|\\         |
        |             / \\    / \\         |
        |                                |
        +--------------------------------+
                ASSEMBLY ROOM
    """
        
    def _drawing_room_scene(self):
        return """
        /\\                              /\\
        ||  +------------------------+  ||
        ||  |                        |  ||
        ||  |     O          O       |  ||
        ||  |    /|\\        /|\\      |  ||
        ||  |    / \\        / \\      |  ||
        ||  |                        |  ||
        ||  |                        |  ||
        ||  |   ___              ___ |  ||
        ||  |  |___|            |___||  ||
        ||  |                        |  ||
        ||  +------------------------+  ||
        ||         DRAWING ROOM         ||
        \\/                              \\/
    """
        
    def _dinner_scene(self):
        return """
        +--------------------------------+
        |                                |
        |      O         @        O      |
        |     /|\\       /|\\      /|\\     |
        |     / \\       / \\      / \\     |
        |   ================================
        |  |         DINNER TABLE         |
        |   ================================
        |    O       O         O      O   |
        |   /|\\     /|\\       /|\\    /|\\  |
        |   / \\     / \\       / \\    / \\  |
        |                                |
        +--------------------------------+
    """