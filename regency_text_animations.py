"""
Regency Text Animations for Jane Austen Storytelling Experience
Provides animated text transitions and effects mimicking Regency-era writing styles
"""

import sys
import time
import random
import os
import textwrap
import re

class RegencyTextAnimator:
    """Class for creating Regency-era text animations and transitions"""
    
    def __init__(self):
        """Initialize the animator with default settings"""
        # Animation speeds
        self.slow_speed = 0.08  # For formal, deliberate writing
        self.medium_speed = 0.04  # For standard narration
        self.fast_speed = 0.02  # For dialogue or quick notes
        
        # Default text styling
        self.use_italic = False
        self.use_formal_style = True
        self.use_quill_effect = True
        
        # Default width for text wrapping
        self.text_width = 70
        
        # Decorative elements
        self.pen_flourishes = [
            "~", "~•~", "❦", "❧", "⁂", "☙", "♡", "♔", "⚜", "✧", "✵"
        ]
        
        # Ink effects (simulating ink drying on paper)
        self.ink_saturation = 1.0  # Full ink saturation by default
        
        # Terminal dimensions
        self.term_width = 80
        self.term_height = 24
        self._update_terminal_size()
    
    def _update_terminal_size(self):
        """Update terminal dimensions if possible"""
        try:
            self.term_width, self.term_height = os.get_terminal_size()
        except (AttributeError, OSError, IOError):
            # Use default values if can't determine terminal size
            pass
    
    def simulate_quill_writing(self, text, speed=None, include_ink_effects=True):
        """
        Simulate the quill writing process with varying speed and authentic pen flourishes
        
        Args:
            text: The text to be animated
            speed: Animation speed (None for default medium speed)
            include_ink_effects: Whether to include ink drying and saturation effects
            
        Returns:
            The complete text after animation is done
        """
        if speed is None:
            speed = self.medium_speed
        
        # Wrap text to appropriate width
        wrapped_text = textwrap.fill(text, width=self.text_width)
        
        # Break into lines for animation
        lines = wrapped_text.split('\n')
        
        # For each line, animate character by character
        for line in lines:
            # Simulate the quill dipping in ink at the start of each line
            if include_ink_effects and self.use_quill_effect:
                ink_level = 1.0  # Full ink at start of line
                
                # Subtle pause as if dipping quill in ink
                time.sleep(0.2)
                
                # Small gesture like dipping motion
                sys.stdout.write("✒ ")
                sys.stdout.flush()
                time.sleep(0.3)
                sys.stdout.write("\b\b  \b\b")  # Erase the dip gesture
                sys.stdout.flush()
            
            # Calculate variable speed based on punctuation and formatting
            for i, char in enumerate(line):
                # Determine character-specific delay
                char_delay = speed
                
                # Slower for punctuation (as if writer is pausing to think)
                if char in ".,;:!?":
                    char_delay = speed * 3
                
                # Slower at the beginning of sentences
                if i > 0 and line[i-1] in ".!?" and char != " ":
                    char_delay = speed * 2
                
                # Faster for spaces (natural quick hand movement)
                if char == " ":
                    char_delay = speed * 0.5
                
                # If ink effects enabled, simulate ink fading as quill moves along
                if include_ink_effects and self.use_quill_effect:
                    # Ink gradually fades as the line progresses
                    ink_level = max(0.4, 1.0 - (i / len(line)) * 0.7)
                    
                    # Simulate ink saturation affecting character brightness
                    if ink_level < 0.6 and char != " ":
                        # Use lighter color for "faded" ink
                        sys.stdout.write(f"\033[38;5;250m{char}\033[0m")
                    else:
                        # Full black for strong ink
                        sys.stdout.write(char)
                else:
                    sys.stdout.write(char)
                
                sys.stdout.flush()
                
                # Small random variation in timing for natural effect
                time.sleep(char_delay + random.uniform(-0.01, 0.01))
            
            # Newline after each line
            print()
        
        return wrapped_text
    
    def formal_writing_transition(self, text, formal_speed=0.05):
        """
        Display text with a formal Regency-style writing transition
        
        Args:
            text: The text to display
            formal_speed: Speed for formal handwriting simulation
            
        Returns:
            The fully displayed text
        """
        # Add a decorative header with a period-appropriate style
        self._print_decorative_header()
        
        # Count the number of sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Display text with formal writing style
        current_text = ""
        
        for i, sentence in enumerate(sentences):
            if not sentence.strip():
                continue
                
            # For Regency formality, add an appropriate pause between sentences
            if i > 0:
                time.sleep(0.7)
            
            # Add proper capitalization for formal writing if needed
            if sentence and sentence[0].islower():
                sentence = sentence[0].upper() + sentence[1:]
            
            # Ensure sentences end with proper punctuation
            if not sentence.strip().endswith(('.', '!', '?')):
                sentence += '.'
            
            # Add the sentence with quill writing effect
            current_text += sentence + " "
            self.simulate_quill_writing(sentence, speed=formal_speed)
        
        # Add a decorative footer
        self._print_decorative_footer()
        
        return text
    
    def animated_regency_letter(self, sender, recipient, content, location="Pemberley", date=None):
        """
        Display an animated Regency-era letter being written
        
        Args:
            sender: The letter sender's name
            recipient: The letter recipient's name
            content: The letter content
            location: Origin location (default: "Pemberley")
            date: Letter date (default: generated period-appropriate date)
            
        Returns:
            The complete letter text
        """
        # Clear the screen for the letter
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # If no date provided, generate a period-appropriate one
        if date is None:
            date = self._generate_regency_date()
        
        # Format the header parts
        location_date = f"{location}, {date}"
        
        # Center align the header information
        print()
        self._center_text(location_date)
        print("\n")
        
        # Letter greeting with proper period styling
        greeting = f"My dear {recipient},"
        print(greeting)
        print()
        
        # Animate the content with quill writing effect
        # Use slower speed for letter writing - more formal and deliberate
        wrapped_content = textwrap.fill(content, width=self.text_width)
        self.simulate_quill_writing(wrapped_content, speed=self.slow_speed)
        
        # Letter closing
        print("\n")
        closing = "I remain, your most humble and obedient servant,"
        self.simulate_quill_writing(closing, speed=self.slow_speed)
        print("\n")
        
        # Signature with flourish
        signature = sender
        print(" " * 40, end="")
        self.simulate_quill_writing(signature, speed=self.slow_speed * 1.5)
        
        # Add a signature flourish
        print("\n")
        flourish = random.choice([
            "~ ~ ~",
            "⁂",
            "❦ ❦ ❦",
            "✧ ✦ ✧"
        ])
        self._center_text(flourish)
        
        # Build complete letter text for return
        letter_text = (
            f"{location_date}\n\n"
            f"{greeting}\n\n"
            f"{wrapped_content}\n\n"
            f"{closing}\n\n"
            f"{signature}\n\n"
            f"{flourish}"
        )
        
        return letter_text
    
    def animated_scene_transition(self, from_scene, to_scene):
        """
        Create an animated transition between story scenes
        
        Args:
            from_scene: Description of the scene transitioning from
            to_scene: Description of the scene transitioning to
            
        Returns:
            The full transition text
        """
        # Get terminal width for visual flourish
        self._update_terminal_size()
        
        # Calculate frames for animation
        max_width = min(self.term_width - 4, 70)  # Allow for margins
        
        # Display opening scene
        print("\n" + "═" * max_width)
        print(f"Scene: {from_scene}")
        print("═" * max_width)
        
        # Create transition animation
        time.sleep(1)
        
        # Fading out effect
        for i in range(10):
            # Clear previous line
            sys.stdout.write("\r" + " " * max_width + "\r")
            
            # Create fading dots
            dots = "•" * (10 - i) + " " * i
            centered_dots = dots.center(max_width)
            
            sys.stdout.write(centered_dots)
            sys.stdout.flush()
            time.sleep(0.15)
        
        # Display transitional phrases with quill effect
        transition_phrases = [
            "Time passes...",
            "Meanwhile...",
            "The following day...",
            "Later that evening...",
            "After some time...",
            "As the sun moved across the sky...",
            "After a fortnight had passed...",
            "Upon the next day's light..."
        ]
        
        # Select an appropriate phrase
        chosen_phrase = random.choice(transition_phrases)
        
        # Print the transition phrase
        print("\n")
        self._center_text(chosen_phrase)
        time.sleep(1.5)
        
        # Display new scene with animated entrance
        print("\n" + "═" * max_width)
        print(f"Scene: {to_scene}")
        print("═" * max_width + "\n")
        
        transition_text = (
            f"Scene: {from_scene}\n\n"
            f"{chosen_phrase}\n\n"
            f"Scene: {to_scene}"
        )
        
        return transition_text
    
    def animated_chapter_heading(self, chapter_number, chapter_title=None):
        """
        Display an animated chapter heading in Regency style
        
        Args:
            chapter_number: Chapter number (as int or Roman numeral string)
            chapter_title: Optional chapter title
            
        Returns:
            The formatted chapter heading
        """
        # Get terminal width for centering
        self._update_terminal_size()
        
        # Convert to Roman numerals if a number was provided
        if isinstance(chapter_number, int):
            chapter_roman = self._to_roman_numeral(chapter_number)
        else:
            chapter_roman = chapter_number
            
        # Format with Regency styling
        heading = f"CHAPTER {chapter_roman}"
        
        # Create decorative frame
        width = max(len(heading) + 20, 40)
        
        # Animate the chapter heading appearing
        print("\n")
        print("\n")
        
        # Top border animation
        top_border = "╔" + "═" * (width - 2) + "╗"
        self._animated_text(top_border, delay=0.01)
        
        # Sides and empty space
        for _ in range(2):
            side_line = "║" + " " * (width - 2) + "║"
            self._animated_text(side_line, delay=0.01)
        
        # Chapter heading
        padding = (width - 2 - len(heading)) // 2
        chapter_line = "║" + " " * padding + heading + " " * (width - 2 - padding - len(heading)) + "║"
        self._animated_text(chapter_line, delay=0.02)
        
        # Display title if provided
        if chapter_title:
            # Empty line
            side_line = "║" + " " * (width - 2) + "║"
            self._animated_text(side_line, delay=0.01)
            
            # Title with padding
            padding = max(2, (width - 2 - len(chapter_title)) // 2)
            title_line = "║" + " " * padding + chapter_title + " " * (width - 2 - padding - len(chapter_title)) + "║"
            self._animated_text(title_line, delay=0.02)
        else:
            # No title provided
            title_line = ""
        
        # Sides and empty space
        for _ in range(2):
            side_line = "║" + " " * (width - 2) + "║"
            self._animated_text(side_line, delay=0.01)
        
        # Bottom border animation
        bottom_border = "╚" + "═" * (width - 2) + "╝"
        self._animated_text(bottom_border, delay=0.01)
        
        print("\n")
        
        # Format the full heading for return
        chapter_heading = (
            f"\n{top_border}\n"
            f"║{' ' * (width - 2)}║\n"
            f"║{' ' * (width - 2)}║\n"
            f"{chapter_line}\n"
        )
        
        if chapter_title:
            chapter_heading += (
                f"║{' ' * (width - 2)}║\n"
                f"{title_line}\n"
            )
            
        chapter_heading += (
            f"║{' ' * (width - 2)}║\n"
            f"║{' ' * (width - 2)}║\n"
            f"{bottom_border}\n"
        )
        
        return chapter_heading
    
    def animated_narration(self, text, style="standard"):
        """
        Display text with a narration effect suited to Jane Austen's style
        
        Args:
            text: The narration text to display
            style: Narration style - "standard", "dramatic", or "reflective"
            
        Returns:
            The formatted text after animation
        """
        # Determine speed based on style
        if style == "dramatic":
            base_speed = self.medium_speed * 1.2  # Slightly slower for dramatic effect
        elif style == "reflective":
            base_speed = self.slow_speed  # Slowest for philosophical reflections
        else:  # standard
            base_speed = self.medium_speed
        
        # Analyze text for sentence structure
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Animate each sentence with appropriate variations
        for i, sentence in enumerate(sentences):
            if not sentence.strip():
                continue
                
            # Establish sentence type
            is_dialogue = '"' in sentence or "'" in sentence
            is_question = '?' in sentence
            is_exclamation = '!' in sentence
            
            # Modify speed based on sentence type
            sentence_speed = base_speed
            if is_dialogue:
                # Dialogue flows a bit faster
                sentence_speed = base_speed * 0.8
            elif is_question:
                # Questions with a slight pause at the end
                sentence_speed = base_speed * 1.1
            elif is_exclamation:
                # Exclamations with emphasis
                sentence_speed = base_speed * 0.9
                
            # Add appropriate pause between sentences
            if i > 0:
                time.sleep(0.5)
                
            # Animate the sentence with quill effect
            self.simulate_quill_writing(sentence, speed=sentence_speed)
            
            # For dramatic style, add extra pauses after key sentences
            if style == "dramatic" and (is_question or is_exclamation or len(sentence) > 80):
                time.sleep(0.8)  # Extra dramatic pause
                
        # Return the complete text
        return text
    
    def animated_social_commentary(self, text):
        """
        Display Austen-style social commentary with animation
        
        Args:
            text: The social commentary text
            
        Returns:
            The formatted text after animation
        """
        # Add a decorative separator before commentary
        self._print_decorative_divider()
        
        # Title for commentary section
        commentary_title = "Observations on Society"
        self._center_text(commentary_title)
        print("\n")
        
        # Split into paragraphs for more natural reading
        paragraphs = text.split("\n\n")
        
        # Animate each paragraph with the formal writing style
        for i, paragraph in enumerate(paragraphs):
            if i > 0:
                print()  # Space between paragraphs
                
            # Social commentary is more formal and reflective
            self.simulate_quill_writing(paragraph, speed=self.slow_speed)
            
            # Pause between paragraphs
            if i < len(paragraphs) - 1:
                time.sleep(1.0)
                
        # Add a decorative separator after commentary
        print("\n")
        self._print_decorative_divider()
        
        # Format complete text for return
        formatted_text = (
            f"{commentary_title}\n\n"
            f"{text}\n"
        )
        
        return formatted_text
    
    def animated_dialogue(self, speaker, text, action=None):
        """
        Display animated dialogue in Regency style
        
        Args:
            speaker: Character speaking
            text: The dialogue text
            action: Optional action description
            
        Returns:
            The formatted dialogue after animation
        """
        # Format dialogue with period quotation style
        if not text.strip().endswith(('.', '!', '?')):
            text = text + "."
            
        # Ensure quotation marks
        if not text.startswith('"'):
            text = f'"{text}'
        if not text.endswith('"'):
            if text[-1] in '.!?':
                text = text[:-1] + '."'
            else:
                text = text + '"'
        
        # Display speaker
        speaker_text = f"{speaker}:"
        print(speaker_text, end=" ")
        
        # Display dialogue with faster animation (speech is quicker than narration)
        self.simulate_quill_writing(text, speed=self.fast_speed)
        
        # Display action if provided
        if action:
            print()
            action_text = f"[{action}]"
            # Slower and italicized for action description
            # ANSI escape code for italic: \033[3m
            print('\033[3m', end='')
            self.simulate_quill_writing(action_text, speed=self.medium_speed)
            print('\033[0m', end='')  # Reset formatting
        
        # Format complete dialogue for return
        formatted_dialogue = f"{speaker}: {text}"
        if action:
            formatted_dialogue += f"\n[{action}]"
            
        return formatted_dialogue
    
    def _animated_text(self, text, delay=0.03):
        """Display text with character-by-character animation"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def _center_text(self, text):
        """Center text in the terminal"""
        centered = text.center(self.term_width)
        print(centered)
    
    def _print_decorative_header(self):
        """Print a decorative header in Regency style"""
        width = min(self.term_width - 4, 70)
        
        # Select a decorative pattern
        decorative_patterns = [
            "~ ⁂ ~ ⁂ ~ ⁂ ~",
            "❦ ❧ ❦ ❧ ❦",
            "~ ~ ~ ~ ~ ~ ~",
            "⚜ ⚜ ⚜ ⚜ ⚜",
        ]
        pattern = random.choice(decorative_patterns)
        
        # Display centered pattern
        print("\n")
        self._center_text(pattern)
        print("\n")
    
    def _print_decorative_footer(self):
        """Print a decorative footer in Regency style"""
        self._print_decorative_header()  # Reuse header style for consistency
    
    def _print_decorative_divider(self):
        """Print a decorative divider line"""
        width = min(self.term_width - 4, 70)
        
        # Select a divider style
        dividers = [
            "~" * width,
            "•" + ("~•" * (width // 2)),
            "❦ " * (width // 2),
            "☙" + ("━" * (width - 2)) + "❧",
        ]
        divider = random.choice(dividers)
        
        print(divider)
    
    def _generate_regency_date(self):
        """Generate a Regency-era formatted date"""
        months = [
            "January", "February", "March", "April", "May", "June", "July", 
            "August", "September", "October", "November", "December"
        ]
        
        # Random date in Regency era (1811-1820)
        year = random.randint(1811, 1820)
        month = random.choice(months)
        day = random.randint(1, 28)
        
        # Get day suffix (st, nd, rd, th)
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        
        # Format in Regency style
        return f"{month} {day}{suffix}, {year}"
    
    def _to_roman_numeral(self, num):
        """Convert integer to Roman numeral"""
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num


def demo_regency_animations():
    """Demonstrate the Regency text animations"""
    # Create animator
    animator = RegencyTextAnimator()
    
    print("Jane Austen Storytelling Experience - Regency Text Animations Demo")
    print("=" * 70)
    print("\nDemonstrating various Regency-era text animations and transitions...")
    time.sleep(2)
    
    # Demo 1: Chapter Heading
    print("\n\nDEMONSTRATION 1: CHAPTER HEADING")
    animator.animated_chapter_heading(3, "A Most Unexpected Meeting")
    time.sleep(2)
    
    # Demo 2: Formal writing transition
    print("\n\nDEMONSTRATION 2: FORMAL WRITING TRANSITION")
    formal_text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    animator.formal_writing_transition(formal_text)
    time.sleep(2)
    
    # Demo 3: Scene transition
    print("\n\nDEMONSTRATION 3: SCENE TRANSITION")
    animator.animated_scene_transition(
        "The drawing room at Longbourn", 
        "The grand ballroom at Netherfield"
    )
    time.sleep(2)
    
    # Demo 4: Regency letter
    print("\n\nDEMONSTRATION 4: REGENCY LETTER")
    letter_content = "I hope this letter finds you in good health and spirits. We have had quite the eventful week at Pemberley, with visitors arriving from as far as London and Bath. The gardens are in full bloom, and the weather has been most agreeable."
    animator.animated_regency_letter("Elizabeth Darcy", "Jane Bingley", letter_content)
    time.sleep(2)
    
    # Demo 5: Dialogue
    print("\n\nDEMONSTRATION 5: DIALOGUE")
    animator.animated_dialogue("Mr. Darcy", "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow", "looks intently at Elizabeth")
    time.sleep(1)
    animator.animated_dialogue("Elizabeth Bennet", "Are you so severe upon your own sex as to doubt the possibility of all this?", "raises an eyebrow")
    time.sleep(2)
    
    # Demo 6: Social commentary
    print("\n\nDEMONSTRATION 6: SOCIAL COMMENTARY")
    commentary = "Society's expectations of young women often disregard their intellectual capabilities, focusing instead on accomplishments designed merely to attract a suitable match. Such narrow constraints do a disservice not only to the women themselves but to society as a whole."
    animator.animated_social_commentary(commentary)
    
    print("\n\nRegency Text Animations Demo Complete")
    print("=" * 70)


if __name__ == "__main__":
    # Run the demonstration if this module is executed directly
    demo_regency_animations()