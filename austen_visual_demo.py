"""
Jane Austen Storytelling Experience - Visual Demo
A demonstration of Regency-era text animations and Kivy visual imagery
"""

import os
import time
import random
from regency_text_animations import RegencyTextAnimator
from visual_imagery_kivy import (
    create_character_portrait, 
    create_location_illustration, 
    create_event_illustration,
    create_thematic_quote_frame,
    get_ornamental_divider,
    get_story_header,
    get_seasonal_imagery
)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout


class AustenVisualDemo(App):
    """Demo application that combines Regency text animations with Kivy visual imagery"""
    
    def build(self):
        """Build the demo application UI"""
        # Set window size
        Window.size = (1000, 700)
        
        # Create root layout
        self.root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Add title
        title = Label(
            text="Jane Austen Storytelling Experience - Visual Demo",
            font_size=24,
            size_hint_y=None,
            height=50
        )
        self.root_layout.add_widget(title)
        
        # Create content area with buttons for different demos
        content_layout = BoxLayout(orientation='horizontal')
        
        # Left panel with buttons
        button_panel = BoxLayout(
            orientation='vertical', 
            spacing=10, 
            padding=10, 
            size_hint_x=0.3
        )
        
        # Add demo buttons
        demos = [
            ("Character Portrait", self.show_character_portrait),
            ("Location Scene", self.show_location_scene),
            ("Story Event", self.show_story_event),
            ("Thematic Quote", self.show_thematic_quote),
            ("Animated Letter", self.show_animated_letter),
            ("Chapter Heading", self.show_chapter_heading),
            ("Scene Transition", self.show_scene_transition),
            ("Social Commentary", self.show_social_commentary),
            ("Animated Dialogue", self.show_animated_dialogue),
            ("Seasonal Imagery", self.show_seasonal_imagery)
        ]
        
        for demo_name, demo_func in demos:
            btn = Button(
                text=demo_name,
                size_hint_y=None,
                height=40
            )
            btn.bind(on_press=demo_func)
            button_panel.add_widget(btn)
        
        content_layout.add_widget(button_panel)
        
        # Right panel for demo content
        self.demo_panel = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=10,
            size_hint_x=0.7
        )
        
        # Add initial content
        self.demo_panel.add_widget(
            Label(
                text="Select a demo from the left panel",
                font_size=20
            )
        )
        
        content_layout.add_widget(self.demo_panel)
        
        self.root_layout.add_widget(content_layout)
        
        # Initialize the text animator
        self.text_animator = RegencyTextAnimator()
        
        return self.root_layout
    
    def clear_demo_panel(self):
        """Clear the demo panel for new content"""
        self.demo_panel.clear_widgets()
    
    def show_character_portrait(self, instance):
        """Show character portrait demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Regency Era Character Portraits",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Create character portraits
        portraits_layout = BoxLayout(spacing=10)
        
        # Female upper class character
        female_char = {
            'name': 'Lady Elizabeth Darcy',
            'gender': 'female',
            'class': 'upper',
            'age': 22
        }
        
        # Male middle class character
        male_char = {
            'name': 'Mr. Thomas Harrington',
            'gender': 'male',
            'class': 'middle',
            'age': 35
        }
        
        # Create and add widgets
        portrait1 = create_character_portrait(female_char)
        portrait2 = create_character_portrait(male_char)
        
        portraits_layout.add_widget(portrait1)
        portraits_layout.add_widget(portrait2)
        
        self.demo_panel.add_widget(portraits_layout)
        
        # Add text description with animation (this would run in a terminal normally)
        description_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=100
        )
        
        text_label = Label(
            text="In a real terminal environment, the character description would appear with a quill writing effect:",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=50
        )
        
        example_text = '"Lady Elizabeth, with her fine eyes and gentle demeanor, carried herself with the poise expected of one from Pemberley."'
        example_label = Label(
            text=example_text,
            font_size=16,
            italic=True,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=50
        )
        
        description_layout.add_widget(text_label)
        description_layout.add_widget(example_label)
        
        self.demo_panel.add_widget(description_layout)
    
    def show_location_scene(self, instance):
        """Show location scene demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Regency Era Location Scenes",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Create location illustrations
        locations_layout = BoxLayout(spacing=10)
        
        # Estate in summer
        estate_location = {
            'type': 'estate',
            'season': 'summer',
            'time_of_day': 'day'
        }
        
        # Cottage in autumn
        cottage_location = {
            'type': 'cottage',
            'season': 'autumn',
            'time_of_day': 'evening'
        }
        
        # Create and add widgets
        location1 = create_location_illustration(estate_location)
        location2 = create_location_illustration(cottage_location)
        
        locations_layout.add_widget(location1)
        locations_layout.add_widget(location2)
        
        self.demo_panel.add_widget(locations_layout)
        
        # Add text description
        text_label = Label(
            text="In a real terminal environment, the location description would appear with a quill writing effect. The visual imagery enhances the storytelling experience by providing rich visual context for narrative scenes.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=100
        )
        
        self.demo_panel.add_widget(text_label)
    
    def show_story_event(self, instance):
        """Show story event demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Regency Era Story Events",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Create event illustrations
        events_layout = BoxLayout(spacing=10)
        
        # Proposal event
        proposal_event = {
            'type': 'proposal',
            'description': 'A heartfelt proposal in the garden at sunset'
        }
        
        # Ball event
        ball_event = {
            'type': 'ball',
            'description': 'The winter ball at Netherfield Park'
        }
        
        # Create and add widgets
        event1 = create_event_illustration(proposal_event)
        event2 = create_event_illustration(ball_event)
        
        events_layout.add_widget(event1)
        events_layout.add_widget(event2)
        
        self.demo_panel.add_widget(events_layout)
        
        # Add text description
        text_label = Label(
            text="Key narrative events are visualized to enhance storytelling. In the terminal, these would be accompanied by animated text transitions that mimic Regency-era writing styles, creating a more immersive reading experience.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=100
        )
        
        self.demo_panel.add_widget(text_label)
    
    def show_thematic_quote(self, instance):
        """Show thematic quote demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Thematic Jane Austen Quotes",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Create quote frames
        quotes_layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Love theme quote
        love_quote = {
            'text': 'In vain I have struggled. It will not do. My feelings will not be repressed. You must allow me to tell you how ardently I admire and love you.',
            'source': 'Pride and Prejudice',
            'theme': 'love',
            'context': 'Spoken by Mr. Darcy during his first proposal to Elizabeth Bennet.',
            'include_context': True
        }
        
        # Social class theme quote
        social_quote = {
            'text': 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.',
            'source': 'Pride and Prejudice',
            'theme': 'social_class',
            'context': 'The famous opening line establishing the novel\'s central theme of marriage as social advancement.',
            'include_context': True
        }
        
        # Create and add widgets
        quote1 = create_thematic_quote_frame(love_quote)
        quotes_layout.add_widget(quote1)
        
        # Add text description
        text_label = Label(
            text="Thematic quotes enhance the storytelling experience by connecting narrative moments to Jane Austen's authentic insights. The terminal version features animated text that appears character by character, mimicking the motion of a quill pen on parchment.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=100
        )
        
        quotes_layout.add_widget(text_label)
        
        self.demo_panel.add_widget(quotes_layout)
    
    def show_animated_letter(self, instance):
        """Show animated letter demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Regency Era Letter Animation",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Add description of the terminal animation
        text_description = Label(
            text="In the terminal, letters appear with a special quill-writing animation that simulates the handwriting process:\n\n1. The date and location appear first\n2. The greeting follows with a formal style\n3. The content is written with ink saturation effects\n4. The signature includes a personal flourish\n\nThis creates an authentic Regency-era correspondence experience.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=200
        )
        
        # Sample letter content
        letter_content = (
            "My dear Cassandra,\n\n"
            "I hope this letter finds you in good health and spirits. We have had quite the eventful week at Pemberley, "
            "with visitors arriving from as far as London and Bath. The gardens are in full bloom, "
            "and the weather has been most agreeable.\n\n"
            "I remain, your most humble and obedient servant,\n\n"
            "Jane Austen"
        )
        
        # Display sample letter
        letter_label = Label(
            text=letter_content,
            font_size=16,
            italic=True,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=300
        )
        
        # Create layout
        letter_layout = BoxLayout(orientation='vertical')
        letter_layout.add_widget(text_description)
        letter_layout.add_widget(letter_label)
        
        self.demo_panel.add_widget(letter_layout)
    
    def show_chapter_heading(self, instance):
        """Show chapter heading demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Animated Chapter Headings",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Add description of the terminal animation
        text_description = Label(
            text="Chapter headings appear with decorative frames and animation effects. In the terminal version, each element of the frame appears sequentially, creating a reveal effect:\n\n1. The top border appears first\n2. Side borders fade in\n3. Chapter number in Roman numerals fades in\n4. Optional chapter title appears\n5. Bottom border completes the frame",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=150
        )
        
        # Sample chapter heading content
        chapter_content = (
            "╔═════════════════════════════════╗\n"
            "║                                 ║\n"
            "║                                 ║\n"
            "║            CHAPTER III          ║\n"
            "║                                 ║\n"
            "║      A Most Unexpected Visit    ║\n"
            "║                                 ║\n"
            "║                                 ║\n"
            "╚═════════════════════════════════╝"
        )
        
        # Display sample chapter heading
        chapter_label = Label(
            text=chapter_content,
            font_size=16,
            font_name='monospace',  # Use monospace font for ASCII art
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=200
        )
        
        # Create layout
        chapter_layout = BoxLayout(orientation='vertical')
        chapter_layout.add_widget(text_description)
        chapter_layout.add_widget(chapter_label)
        
        self.demo_panel.add_widget(chapter_layout)
    
    def show_scene_transition(self, instance):
        """Show scene transition demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Animated Scene Transitions",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Add description of the terminal animation
        text_description = Label(
            text="Scene transitions create visual breaks between narrative locations. In the terminal version:\n\n1. The current scene fades out with decorative elements\n2. A transitional phrase appears (e.g., 'Later that evening...')\n3. The new scene fades in with its own decorative frame\n\nThis creates a cinematic effect appropriate to Regency literature.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=150
        )
        
        # Sample scene transition content
        transition_content = (
            "═════════════════════════════════════════\n"
            "Scene: The drawing room at Longbourn\n"
            "═════════════════════════════════════════\n\n"
            "     • • • • • • • • • •     \n\n"
            "      Later that evening...      \n\n"
            "═════════════════════════════════════════\n"
            "Scene: The grand ballroom at Netherfield\n"
            "═════════════════════════════════════════"
        )
        
        # Display sample scene transition
        transition_label = Label(
            text=transition_content,
            font_size=16,
            font_name='monospace',  # Use monospace font for ASCII art
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=250
        )
        
        # Create layout
        transition_layout = BoxLayout(orientation='vertical')
        transition_layout.add_widget(text_description)
        transition_layout.add_widget(transition_label)
        
        self.demo_panel.add_widget(transition_layout)
    
    def show_social_commentary(self, instance):
        """Show social commentary demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Animated Social Commentary",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Add description of the terminal animation
        text_description = Label(
            text="Social commentary sections feature unique styling to differentiate them from the main narrative. In the terminal version:\n\n1. A decorative divider signals the start of commentary\n2. The title 'Observations on Society' appears\n3. Text unfolds with a slower, more deliberate animation\n4. Another decorative divider marks the end\n\nThis recreates Austen's narrative technique of social observation.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=150
        )
        
        # Sample social commentary content
        commentary_content = (
            "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n\n"
            "           Observations on Society\n\n"
            "Society's expectations of young women often disregard their intellectual "
            "capabilities, focusing instead on accomplishments designed merely to "
            "attract a suitable match. Such narrow constraints do a disservice not "
            "only to the women themselves but to society as a whole.\n\n"
            "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"
        )
        
        # Display sample social commentary
        commentary_label = Label(
            text=commentary_content,
            font_size=16,
            italic=True,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=250
        )
        
        # Create layout
        commentary_layout = BoxLayout(orientation='vertical')
        commentary_layout.add_widget(text_description)
        commentary_layout.add_widget(commentary_label)
        
        self.demo_panel.add_widget(commentary_layout)
    
    def show_animated_dialogue(self, instance):
        """Show animated dialogue demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Animated Character Dialogue",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Add description of the terminal animation
        text_description = Label(
            text="Character dialogue animations enhance the reading experience. In the terminal version:\n\n1. Character name appears first\n2. Dialogue text unfolds at a faster pace than narration\n3. Quotation marks receive special emphasis\n4. Action descriptions appear in italics\n5. Each character's speech has distinctive timing\n\nThis creates a dynamic conversational flow.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=150
        )
        
        # Sample dialogue content
        dialogue_content = (
            'Mr. Darcy: "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow."\n'
            '[looks intently at Elizabeth]\n\n'
            'Elizabeth Bennet: "Are you so severe upon your own sex as to doubt the possibility of all this?"\n'
            '[raises an eyebrow]'
        )
        
        # Display sample dialogue
        dialogue_label = Label(
            text=dialogue_content,
            font_size=16,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=150
        )
        
        # Create layout
        dialogue_layout = BoxLayout(orientation='vertical')
        dialogue_layout.add_widget(text_description)
        dialogue_layout.add_widget(dialogue_label)
        
        self.demo_panel.add_widget(dialogue_layout)
    
    def show_seasonal_imagery(self, instance):
        """Show seasonal imagery demo"""
        self.clear_demo_panel()
        
        # Add description
        description = Label(
            text="Seasonal Imagery for Storytelling",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        self.demo_panel.add_widget(description)
        
        # Create seasonal imagery
        seasons_layout = GridLayout(cols=2, spacing=10)
        
        # Create each season
        spring_image = get_seasonal_imagery("spring", width=300, height=225)
        summer_image = get_seasonal_imagery("summer", width=300, height=225)
        autumn_image = get_seasonal_imagery("autumn", width=300, height=225)
        winter_image = get_seasonal_imagery("winter", width=300, height=225)
        
        # Add to layout
        seasons_layout.add_widget(spring_image)
        seasons_layout.add_widget(summer_image)
        seasons_layout.add_widget(autumn_image)
        seasons_layout.add_widget(winter_image)
        
        self.demo_panel.add_widget(seasons_layout)
        
        # Add text description
        text_label = Label(
            text="Seasonal imagery enhances narrative settings by providing visual context for the time of year. These visual elements work with text animations to create a complete immersive experience in the Jane Austen storytelling world.",
            font_size=14,
            text_size=(400, None),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=100
        )
        
        self.demo_panel.add_widget(text_label)


def run_text_animations_demo():
    """Run a demonstration of the Regency text animations in the terminal"""
    # Create animator
    animator = RegencyTextAnimator()
    
    # Clear screen and show title
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Jane Austen Storytelling Experience - Regency Text Animations Demo")
    print("=" * 70)
    print("\nDemonstrating various Regency-era text animations and transitions...")
    time.sleep(2)
    
    # Demo formal writing transition
    print("\n\nDEMONSTRATION: FORMAL WRITING TRANSITION")
    formal_text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    animator.formal_writing_transition(formal_text)
    time.sleep(2)
    
    # Demo scene transition
    print("\n\nDEMONSTRATION: SCENE TRANSITION")
    animator.animated_scene_transition(
        "The drawing room at Longbourn", 
        "The grand ballroom at Netherfield"
    )
    time.sleep(2)
    
    # Demo character dialogue
    print("\n\nDEMONSTRATION: CHARACTER DIALOGUE")
    animator.animated_dialogue("Mr. Darcy", "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow", "looks intently at Elizabeth")
    time.sleep(1)
    animator.animated_dialogue("Elizabeth Bennet", "Are you so severe upon your own sex as to doubt the possibility of all this?", "raises an eyebrow")
    time.sleep(2)
    
    # Demo social commentary
    print("\n\nDEMONSTRATION: SOCIAL COMMENTARY")
    commentary = "Society's expectations of young women often disregard their intellectual capabilities, focusing instead on accomplishments designed merely to attract a suitable match. Such narrow constraints do a disservice not only to the women themselves but to society as a whole."
    animator.animated_social_commentary(commentary)
    
    # Demo animated chapter heading
    print("\n\nDEMONSTRATION: CHAPTER HEADING")
    animator.animated_chapter_heading(3, "A Most Unexpected Meeting")
    time.sleep(2)
    
    # Demo letter
    print("\n\nDEMONSTRATION: REGENCY LETTER")
    letter_content = "I hope this letter finds you in good health and spirits. We have had quite the eventful week at Pemberley, with visitors arriving from as far as London and Bath. The gardens are in full bloom, and the weather has been most agreeable."
    animator.animated_regency_letter("Elizabeth Darcy", "Jane Bingley", letter_content)
    time.sleep(2)
    
    print("\n\nRegency Text Animations Demo Complete")
    print("=" * 70)
    print("\nNow launching the Kivy visual demonstration...")
    time.sleep(3)


def main():
    """Main function to run the demo"""
    # First run the text animations in the terminal
    run_text_animations_demo()
    
    # Then launch the Kivy visual demo
    AustenVisualDemo().run()


if __name__ == "__main__":
    main()