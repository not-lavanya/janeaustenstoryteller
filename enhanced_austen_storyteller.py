"""
Enhanced Jane Austen Storytelling Experience
A command-line interactive storytelling system with voice capabilities and audio features.
"""

import os
import random
import json
import time
from gtts import gTTS
import speech_recognition as sr
import pygame
from story_templates import get_story_templates, get_story_themes
from character_generator import CharacterGenerator
from audio_manager import AudioManager
from utils import clear_screen, print_with_typing_effect, get_user_input

class JaneAustenStoryGenerator:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.char_generator = CharacterGenerator()
        self.audio_manager = AudioManager()
        
        self.story_themes = get_story_themes()
        self.story_templates = get_story_templates()

        self.voice_recognition_enabled = False
        self.recognizer = sr.Recognizer()

    def initialize_voice_recognition(self):
        """Try to initialize speech recognition"""
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.voice_recognition_enabled = True
            print("Voice recognition successfully initialized.")
        except (sr.RequestError, sr.UnknownValueError, OSError) as e:
            print(f"Could not initialize voice recognition: {e}")
            self.voice_recognition_enabled = False

    def get_voice_input(self, prompt):
        """Get input from voice if available, otherwise use keyboard"""
        if not self.voice_recognition_enabled:
            return input(prompt)
        
        print(prompt)
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            print("Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again or type your response.")
            return input(prompt)
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again or type your response.")
            return input(prompt)
        except sr.RequestError:
            print("Speech recognition service unavailable. Using text input instead.")
            return input(prompt)

    def create_characters(self, num_characters):
        """Create multiple characters"""
        characters = []
        for i in range(num_characters):
            print(f"\nCreating Character {i+1}:")
            
            # Get name input
            custom_name = get_user_input(
                "Would you like to name this character? (yes/no): ", 
                self.get_voice_input if self.voice_recognition_enabled else None
            )
            
            if custom_name.lower().startswith('y'):
                name = get_user_input(
                    "Enter character name: ", 
                    self.get_voice_input if self.voice_recognition_enabled else None
                )
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

    def text_to_speech(self, text, filename='story_narration.mp3'):
        """Convert text to speech with improved settings"""
        print("Generating narration audio...")
        
        try:
            # Create chunks of text to prevent gTTS limitations
            max_chars = 5000  # gTTS has limitations on text length
            chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
            
            temp_files = []
            for i, chunk in enumerate(chunks):
                temp_filename = f"temp_chunk_{i}.mp3"
                tts = gTTS(text=chunk, lang='en', slow=False)
                tts.save(temp_filename)
                temp_files.append(temp_filename)
            
            # If there's only one chunk, just rename it
            if len(temp_files) == 1:
                os.rename(temp_files[0], filename)
            else:
                # Initialize pygame mixer to combine audio files
                pygame.mixer.init()
                
                # Load and play combined audio (this is simplified, actually merging MP3s properly
                # would require more complex audio processing)
                self.audio_manager.combine_audio_files(temp_files, filename)
                
                # Clean up temp files
                for temp_file in temp_files:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
            
            print(f"Narration saved as {filename}")
            return True
        except Exception as e:
            print(f"Error generating speech: {e}")
            return False

    def save_story(self, story, format_type='txt', filename=None):
        """Save generated story in various formats"""
        if filename is None:
            # Generate a default filename based on current time
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"austen_story_{timestamp}"
        
        # Ensure the filename doesn't have an extension already
        if '.' in filename:
            filename = filename.split('.')[0]
            
        if format_type == 'txt':
            with open(f"{filename}.txt", 'w') as file:
                file.write(story)
            print(f"Story saved as {filename}.txt")
            return f"{filename}.txt"
            
        elif format_type == 'json':
            # Create a structured JSON with story metadata
            story_data = {
                "title": f"Jane Austen Story - {time.strftime('%Y-%m-%d')}",
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "content": story,
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
        h1 {{ color: #5B3758; text-align: center; }}
        .story {{ white-space: pre-line; }}
        .footer {{ margin-top: 40px; text-align: center; font-style: italic; }}
    </style>
</head>
<body>
    <div class="story-container">
        <h1>A Tale in the Style of Jane Austen</h1>
        <div class="story">{story}</div>
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

    def play_story_narration(self, audio_file, background_music=None):
        """Play the narration with optional background music"""
        self.audio_manager.play_narration_with_background(audio_file, background_music)

    def run_story_generator(self):
        """Main story generation workflow"""
        clear_screen()
        self.audio_manager.play_sound_effect('welcome')
        
        print_with_typing_effect("""
█████████████████████████████████████████████████████████████████████
█                                                                 █
█     JANE AUSTEN INTERACTIVE STORYTELLING EXPERIENCE             █
█                                                                 █
█     "It is a truth universally acknowledged, that a reader      █
█      in possession of this program, must be in want of a story" █
█                                                                 █
█████████████████████████████████████████████████████████████████████
""")
        
        # Ask if user wants to use voice input
        voice_choice = input("Would you like to enable voice input? (yes/no): ").lower()
        if voice_choice.startswith('y'):
            self.initialize_voice_recognition()
        
        # Theme Selection
        print("\nAvailable Story Themes:")
        for i, theme in enumerate(self.story_themes, 1):
            print(f"{i}. {theme}")

        theme_choice = get_user_input(
            "\nSelect a theme number: ", 
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        try:
            theme_idx = int(theme_choice) - 1
            selected_theme = self.story_themes[theme_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to the first theme.")
            selected_theme = self.story_themes[0]
        
        print(f"\nYou've selected: {selected_theme}")
        self.audio_manager.play_sound_effect('selection')

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
            
        location_choice = get_user_input(
            "\nSelect a location number: ",
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        try:
            location_idx = int(location_choice) - 1
            selected_location = locations[location_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to Pemberley.")
            selected_location = locations[0]
            
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, 1):
            print(f"{i}. {season}")
            
        season_choice = get_user_input(
            "\nSelect a season number: ",
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        try:
            season_idx = int(season_choice) - 1
            selected_season = seasons[season_idx]
        except (ValueError, IndexError):
            print("Invalid selection. Defaulting to spring.")
            selected_season = seasons[0]
        
        settings = {
            'location': selected_location,
            'season': selected_season,
            'time_period': 'the Regency era'
        }
        
        print(f"\nYour story will take place at {selected_location} during {selected_season}.")
        self.audio_manager.play_sound_effect('selection')

        # Character Creation
        num_characters_input = get_user_input(
            "\nHow many characters would you like in your story? (1-5): ",
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        try:
            num_characters = int(num_characters_input)
            num_characters = max(1, min(5, num_characters))  # Clamp between 1 and 5
        except ValueError:
            print("Invalid number. Creating 2 characters.")
            num_characters = 2
            
        characters = self.create_characters(num_characters)
        self.audio_manager.play_sound_effect('character')

        # Story Generation
        print("\nGenerating your Jane Austen inspired story...")
        self.audio_manager.play_sound_effect('writing')
        time.sleep(2)  # Create anticipation
        
        story = self.generate_story(selected_theme, characters, settings)
        
        clear_screen()
        print("\n" + "="*80)
        print_with_typing_effect(story, delay=0.01)
        print("="*80 + "\n")

        # Audio Narration
        narration_choice = get_user_input(
            "Would you like to hear your story narrated? (yes/no): ",
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        if narration_choice.lower().startswith('y'):
            # Determine suitable background music based on theme
            if "Romantic" in selected_theme:
                bg_music = 'romantic'
            elif "Intrigue" in selected_theme:
                bg_music = 'dramatic'
            else:
                bg_music = 'general'
                
            # Create the narration
            narration_file = "current_narration.mp3"
            if self.text_to_speech(story, narration_file):
                print("\nPlaying narration with background music...\n")
                self.play_story_narration(narration_file, bg_music)
                
                # Wait for audio to finish or user to skip
                print("\nPress Enter to stop playback and continue...")
                input()
                self.audio_manager.stop_playback()

        # Save Options
        save_choice = get_user_input(
            "\nWould you like to save this story? (yes/no): ",
            self.get_voice_input if self.voice_recognition_enabled else None
        )
        
        if save_choice.lower().startswith('y'):
            print("\nAvailable formats:")
            print("1. Text file (.txt)")
            print("2. JSON file (.json)")
            print("3. HTML document (.html)")
            
            format_choice = get_user_input(
                "Select a format number: ",
                self.get_voice_input if self.voice_recognition_enabled else None
            )
            
            try:
                format_idx = int(format_choice)
                if format_idx == 1:
                    save_format = 'txt'
                elif format_idx == 2:
                    save_format = 'json'
                elif format_idx == 3:
                    save_format = 'html'
                else:
                    print("Invalid selection. Defaulting to text format.")
                    save_format = 'txt'
            except ValueError:
                print("Invalid selection. Defaulting to text format.")
                save_format = 'txt'
            
            custom_filename = get_user_input(
                "Enter a filename (without extension) or press Enter for default: ",
                self.get_voice_input if self.voice_recognition_enabled else None
            )
            
            if custom_filename:
                saved_file = self.save_story(story, save_format, custom_filename)
            else:
                saved_file = self.save_story(story, save_format)
            
            self.audio_manager.play_sound_effect('save')

        print("\nThank you for using the Jane Austen Interactive Storytelling Experience!")
        print("May your days be filled with wit, romance, and social observation.")
        self.audio_manager.play_sound_effect('goodbye')
        
        # Clean up temporary audio files
        if os.path.exists("current_narration.mp3"):
            try:
                os.remove("current_narration.mp3")
            except:
                pass

def main():
    story_generator = JaneAustenStoryGenerator()
    story_generator.run_story_generator()

if __name__ == "__main__":
    main()
