"""
Jane Austen Letter Writing Assistant
This module provides a tool for composing letters in the style of Jane Austen's era.
"""

import os
import time
import sys
import random
from datetime import datetime
import textwrap

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

class LetterWritingAssistant:
    def __init__(self):
        """Initialize the letter writing assistant"""
        self.regency_locations = [
            "Pemberley, Derbyshire", 
            "Longbourn, Hertfordshire", 
            "Mansfield Park, Northampton", 
            "Barton Cottage, Devonshire", 
            "Kellynch Hall, Somerset",
            "Bath, Somerset",
            "London",
            "Brighton",
            "Rosings Park, Kent",
            "Netherfield Park, Hertfordshire"
        ]
        
        self.letter_types = {
            "invitation": "A letter extending an invitation to an event or gathering",
            "congratulations": "A letter offering congratulations on a happy occasion",
            "gratitude": "A letter expressing thanks for a kindness or favor",
            "apology": "A letter expressing regret for an offense or misunderstanding",
            "news": "A letter sharing news or relating recent events",
            "romantic": "A letter expressing affection or romantic sentiments"
        }
    
    def _format_regency_date(self):
        """Return a date formatted in Regency style"""
        current_date = datetime.now()
        
        # Convert to Regency era (add 206 years to place us in early 1800s)
        regency_year = current_date.year - 206
        
        # Format the date in Regency style
        months = ["January", "February", "March", "April", "May", "June", 
                 "July", "August", "September", "October", "November", "December"]
        
        day = current_date.day
        month = months[current_date.month - 1]
        
        # Add appropriate suffix to day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
            
        return f"the {day}{suffix} of {month}, {regency_year}"
    
    def _generate_invitation_template(self, formal=True):
        """Generate a template for an invitation letter"""
        if formal:
            return (
                "I have the honor of requesting the pleasure of your company at "
                "[EVENT], to be held at [LOCATION] on [DATE] at [TIME]. "
                "\n\n"
                "Your presence would be most gratifying, and we anticipate an "
                "evening of refined conversation and elegant entertainment. "
                "\n\n"
                "I trust you will favor us with your attendance, and I remain, "
                "with the greatest respect, your most humble servant."
            )
        else:
            return (
                "My dear friend, I write with the happiest anticipation to invite "
                "you to [EVENT] at [LOCATION] on [DATE]. "
                "\n\n"
                "We shall have such delightful amusements, and I assure you that "
                "your company would add immeasurably to the pleasure of the occasion. "
                "\n\n"
                "Do say you will come! I shall be most disappointed if you cannot, "
                "and I remain your affectionate friend."
            )
    
    def _generate_congratulations_template(self, formal=True):
        """Generate a template for a congratulatory letter"""
        if formal:
            return (
                "Allow me to extend my most sincere congratulations on [OCCASION]. "
                "Such felicitous news brings the greatest satisfaction to all who "
                "have the honor of your acquaintance. "
                "\n\n"
                "May this happy circumstance be but the beginning of a long series "
                "of good fortune and contentment in your life. "
                "\n\n"
                "I remain, with the warmest regards, your most obedient servant."
            )
        else:
            return (
                "My dear friend, what joyous news has reached me of [OCCASION]! "
                "I could not delay in writing to express my delight and to offer "
                "my heartfelt congratulations. "
                "\n\n"
                "How clever and deserving you are! I declare I have not felt such "
                "pleasure in many weeks as when I learned of your good fortune. "
                "\n\n"
                "Yours with the warmest affection and highest esteem."
            )
    
    def _generate_gratitude_template(self, formal=True):
        """Generate a template for a letter of gratitude"""
        if formal:
            return (
                "I must express my profound gratitude for [FAVOR/KINDNESS] which "
                "you so generously bestowed. Your consideration has placed me "
                "greatly in your debt. "
                "\n\n"
                "Such exemplary benevolence speaks to the excellence of your "
                "character, and I shall endeavor to prove worthy of your kindness. "
                "\n\n"
                "I have the honor to remain, with the deepest appreciation, "
                "your most grateful servant."
            )
        else:
            return (
                "My dear friend, how can I begin to thank you for [FAVOR/KINDNESS]? "
                "Your thoughtfulness has touched me deeply. "
                "\n\n"
                "I have always known your generosity of spirit, but you have "
                "exceeded even my high estimation of your character. "
                "\n\n"
                "I remain your eternally grateful and affectionate friend."
            )
    
    def _generate_apology_template(self, formal=True):
        """Generate a template for a letter of apology"""
        if formal:
            return (
                "I write with the greatest contrition regarding [INCIDENT], and "
                "must beg your forgiveness for any distress or inconvenience "
                "this may have caused. "
                "\n\n"
                "I assure you that it was entirely unintentional, and I deeply "
                "regret that my conduct has fallen short of what is due to one "
                "of your standing and character. "
                "\n\n"
                "I remain, with sincere apologies and the highest respect, "
                "your most humble servant."
            )
        else:
            return (
                "My dear friend, I cannot rest easy until I have begged your "
                "pardon for [INCIDENT]. How thoughtless I have been! "
                "\n\n"
                "I value your good opinion too highly to bear the thought that "
                "I have diminished myself in your eyes. I can only hope that "
                "your generous nature will allow you to forgive my foolishness. "
                "\n\n"
                "Your repentant and affectionate friend."
            )
    
    def _generate_news_template(self, formal=True):
        """Generate a template for a letter sharing news"""
        if formal:
            return (
                "I trust this letter finds you in good health and spirits. I "
                "write to inform you of [NEWS/EVENT] which has recently occurred. "
                "\n\n"
                "The particulars of the matter are as follows: [DETAILS]. I "
                "believed this intelligence would be of interest to you due to "
                "your connection to the affair. "
                "\n\n"
                "I have the honor to remain your most obedient servant."
            )
        else:
            return (
                "My dearest friend, I simply must share with you the news of "
                "[NEWS/EVENT]! You cannot imagine the sensation it has created "
                "in our little circle. "
                "\n\n"
                "[DETAILS] - is it not the most extraordinary thing? I knew "
                "you would wish to hear of it directly, rather than through "
                "the usual channels of gossip. "
                "\n\n"
                "Write to me soon with your thoughts on the matter. Your devoted friend."
            )
    
    def _generate_romantic_template(self, formal=True):
        """Generate a template for a romantic letter"""
        if formal:
            return (
                "I hope you will pardon the liberty I take in addressing you on "
                "a matter of great personal significance. I find myself unable "
                "to suppress the depth of my admiration for your character and person. "
                "\n\n"
                "Your [QUALITIES] have impressed themselves upon my mind in a "
                "manner that I cannot adequately express. My esteem for you has "
                "grown with each meeting, until I can no longer conceal the "
                "strength of my attachment. "
                "\n\n"
                "I remain, with the most ardent regard, your devoted servant."
            )
        else:
            return (
                "My dearest, most beloved friend, I can no longer keep contained "
                "within my heart the feelings that overflow whenever I think of you. "
                "\n\n"
                "Your [QUALITIES] have captured my affections entirely. From the "
                "moment we first met, I have felt a connection that grows stronger "
                "with each passing day. Every hour away from your company seems "
                "an eternity. "
                "\n\n"
                "With all the love my heart can hold, I remain forever yours."
            )
    
    def format_as_letter(self, sender, recipient, content, location="Pemberley", date=None):
        """Format text as a Regency-era letter"""
        # Use provided date or generate a Regency-style date
        if date is None:
            date = self._format_regency_date()
            
        # Format the letter with proper structure
        letter = f"""
╔{'═' * 70}╗
║{' ' * 70}║
║  {location}{' ' * (68 - len(location))}║
║  {date}{' ' * (68 - len(date))}║
║{' ' * 70}║
║  Dear {recipient},{' ' * (64 - len(recipient))}║
║{' ' * 70}║
"""

        # Format the content with proper line wrapping
        wrapped_content = textwrap.wrap(content, width=66)
        for line in wrapped_content:
            letter += f"║  {line}{' ' * (68 - len(line))}║\n"
            
        # Add the closing
        letter += f"""
║{' ' * 70}║
║  I remain, your faithful servant,{' ' * 40}║
║  {sender}{' ' * (68 - len(sender))}║
║{' ' * 70}║
╚{'═' * 70}╝
"""
        return letter
    
    def create_letter(self):
        """Interactive function to create a Regency-style letter"""
        clear_screen()
        
        # Display decorative header
        print("╔" + "═" * 70 + "╗")
        print("║" + " " * 70 + "║")
        print("║     JANE AUSTEN LETTER WRITING ASSISTANT" + " " * 33 + "║")
        print("║" + " " * 70 + "║")
        print("║  \"The distance is nothing when one has a motive.\"" + " " * 23 + "║")
        print("║                                   — Pride and Prejudice" + " " * 14 + "║")
        print("║" + " " * 70 + "║")
        print("╚" + "═" * 70 + "╝")
        
        print("\nWelcome to the Regency Letter Writing Assistant!")
        print("This tool will help you compose a letter in the style of Jane Austen's era.")
        
        # Get the letter type
        print("\nWhat type of letter would you like to write?")
        for i, (letter_type, description) in enumerate(self.letter_types.items(), 1):
            print(f"{i}. {letter_type.capitalize()} - {description}")
            
        letter_choice = input("\nEnter your choice (1-6): ")
        
        try:
            letter_idx = int(letter_choice) - 1
            letter_types = list(self.letter_types.keys())
            selected_type = letter_types[letter_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to 'news'.")
            selected_type = "news"
            
        print(f"\nYou've selected a {selected_type} letter.")
        
        # Ask if the letter should be formal or informal
        formality = input("\nWould you like the letter to be formal or informal? (f/i): ").lower()
        formal = formality != 'i'  # Default to formal unless specifically chosen as informal
        
        # Get sender and recipient information
        sender_name = input("\nEnter your name (the sender): ")
        if not sender_name:
            sender_name = "Jane Austen"
            
        recipient_name = input("Enter the recipient's name: ")
        if not recipient_name:
            recipient_name = "Cassandra Austen"
            
        # Get location
        print("\nSelect a location or enter your own:")
        for i, location in enumerate(self.regency_locations, 1):
            print(f"{i}. {location}")
            
        location_choice = input("\nEnter a number or type your own location: ")
        
        try:
            location_idx = int(location_choice) - 1
            selected_location = self.regency_locations[location_idx]
        except (ValueError, IndexError):
            if location_choice:
                selected_location = location_choice
            else:
                selected_location = "Pemberley, Derbyshire"
                
        print(f"\nYou'll be writing from: {selected_location}")
        
        # Generate the appropriate template
        if selected_type == "invitation":
            template = self._generate_invitation_template(formal)
        elif selected_type == "congratulations":
            template = self._generate_congratulations_template(formal)
        elif selected_type == "gratitude":
            template = self._generate_gratitude_template(formal)
        elif selected_type == "apology":
            template = self._generate_apology_template(formal)
        elif selected_type == "romantic":
            template = self._generate_romantic_template(formal)
        else:  # Default to news
            template = self._generate_news_template(formal)
            
        # Display the template and guide the user to fill it in
        print("\nHere is a template for your letter. Replace the [BRACKETED] parts:")
        print("\n" + "=" * 70)
        print(template)
        print("=" * 70)
        
        # Let the user compose their letter
        print("\nEnter your letter text below. Press Enter twice on an empty line when finished.")
        print("You can use the template above as a guide, or write your own content.")
        
        content_lines = []
        while True:
            line = input("> ")
            if not line and content_lines and not content_lines[-1]:
                break  # Two consecutive empty lines
            content_lines.append(line)
            
        content = "\n".join(content_lines).strip()
        
        # Default content if user didn't enter anything
        if not content:
            if selected_type == "invitation":
                content = template.replace("[EVENT]", "a small dinner party").replace("[LOCATION]", "my humble abode").replace("[DATE]", "Tuesday next").replace("[TIME]", "six o'clock")
            elif selected_type == "congratulations":
                content = template.replace("[OCCASION]", "your recent engagement")
            elif selected_type == "gratitude":
                content = template.replace("[FAVOR/KINDNESS]", "the lovely book you sent")
            elif selected_type == "apology":
                content = template.replace("[INCIDENT]", "my regrettable lateness to your gathering")
            elif selected_type == "news":
                content = template.replace("[NEWS/EVENT]", "the arrival of new neighbors").replace("[DETAILS]", "They appear to be a family of good fortune and excellent breeding")
            elif selected_type == "romantic":
                content = template.replace("[QUALITIES]", "kind heart and lively intelligence")
            
        # Format as a proper letter
        formatted_letter = self.format_as_letter(sender_name, recipient_name, content, selected_location)
        
        # Display the final letter
        clear_screen()
        print("\nYour Regency Era Letter:")
        print(formatted_letter)
        
        # Offer to save the letter
        save_option = input("\nWould you like to save this letter? (y/n): ")
        
        if save_option.lower().startswith('y'):
            filename = input("Enter a filename (or press Enter for default): ")
            
            if not filename:
                filename = f"regency_letter_{selected_type}_{int(time.time())}.txt"
            elif not filename.endswith('.txt'):
                filename += '.txt'
                
            with open(filename, 'w') as file:
                file.write(formatted_letter)
                
            print(f"\nLetter saved as {filename}")
        
        return formatted_letter

def run_letter_assistant():
    """Run the letter writing assistant"""
    assistant = LetterWritingAssistant()
    assistant.create_letter()
    
    # Ask if the user wants to write another letter
    another = input("\nWould you like to write another letter? (y/n): ")
    
    if another.lower().startswith('y'):
        run_letter_assistant()

if __name__ == "__main__":
    run_letter_assistant()