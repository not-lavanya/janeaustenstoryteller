"""
Utility functions for the Jane Austen storytelling experience.
"""

import os
import sys
import time
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, delay=0.03, variance=0.01):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Calculate a slightly variable delay for natural typing feel
        typing_delay = delay + random.uniform(-variance, variance)
        typing_delay = max(0.005, typing_delay)  # Ensure delay is not negative or too small
        
        time.sleep(typing_delay)
    
    # Add a newline at the end
    print()

def get_user_input(prompt, voice_input_func=None):
    """Get user input with optional voice input support"""
    if voice_input_func:
        return voice_input_func(prompt)
    else:
        return input(prompt)

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

def word_count(text):
    """Count words in text"""
    return len(text.split())

def get_writing_style_tips():
    """Return Austen-style writing tips"""
    tips = [
        "Use 'sensibility' to refer to emotional responsiveness.",
        "Describe characters through their manners and conversation.",
        "Include witty observations on social customs.",
        "Balance detailed descriptions with clever dialogue.",
        "Use free indirect discourse to show a character's thoughts.",
        "Include irony and understatement in narration.",
        "Reference social events like balls and dinner parties.",
        "Mention letter-writing as a key mode of communication."
    ]
    return random.sample(tips, 3)  # Return 3 random tips
