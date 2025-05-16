"""
Kivy Visual Imagery for Jane Austen Storytelling Experience
Provides enhanced visual elements using Kivy GUI framework instead of ASCII art
"""

import os
import random
import math
from datetime import datetime

# Kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line, Ellipse, Bezier
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.text import Label as CoreLabel
from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# Default window size (can be adjusted)
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

# Define a palette of colors appropriate for Regency-era aesthetics
REGENCY_COLORS = {
    'parchment': (0.98, 0.94, 0.84, 1),  # Light cream color for backgrounds
    'ink': (0.1, 0.1, 0.1, 1),           # Dark color for text
    'faded_ink': (0.3, 0.3, 0.3, 1),     # Lighter ink color for secondary text
    'navy': (0.05, 0.15, 0.3, 1),        # Deep blue for accents
    'royal_blue': (0.1, 0.2, 0.6, 1),    # Rich blue for decorative elements
    'burgundy': (0.5, 0.0, 0.1, 1),      # Deep red for accents
    'forest_green': (0.0, 0.3, 0.1, 1),  # Dark green for nature elements
    'sky_blue': (0.6, 0.8, 0.9, 1),      # Light blue for skies and water
    'gold': (0.8, 0.6, 0.1, 1),          # Gold for ornate decorations
    'silver': (0.8, 0.8, 0.8, 1),        # Silver for metallic elements
    'blush': (0.9, 0.7, 0.7, 1),         # Soft pink for feminine elements
    'lavender': (0.8, 0.6, 0.8, 1),      # Light purple for floral elements
    'olive': (0.5, 0.5, 0.2, 1),         # Olive green for nature
    'cream': (0.95, 0.9, 0.8, 1),        # Cream for lighter backgrounds
    'shadow': (0.2, 0.2, 0.2, 0.3)       # Transparent black for shadows
}

# KV Language string for styling
KV_STRING = '''
<RegencyLabel>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    color: root.text_color
    font_size: root.font_size
    italic: root.italic
    bold: root.bold
    font_name: root.font_name
    text_size: self.width, None
    halign: 'center'
    valign: 'middle'
    markup: True

<ScriptScrollLabel>:
    canvas.before:
        Color:
            rgba: app.theme_cls.bg_normal if hasattr(app, 'theme_cls') else (0.95, 0.9, 0.8, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    effect_cls: "ScrollEffect"
    bar_width: '10dp'
    scroll_type: ['bars']
    bar_color: app.theme_cls.primary_color if hasattr(app, 'theme_cls') else (0.3, 0.3, 0.3, 1)
    bar_inactive_color: app.theme_cls.primary_light if hasattr(app, 'theme_cls') else (0.5, 0.5, 0.5, 0.5)
    
<AnimatedQuoteBox>:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(10)
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
        
<CharacterPortrait>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)
    canvas.before:
        Color:
            rgba: root.bg_color if hasattr(root, 'bg_color') else (0.95, 0.9, 0.8, 1)
        Rectangle:
            pos: self.pos
            size: self.size
'''

# Load the KV language string
Builder.load_string(KV_STRING)


class RegencyLabel(Label):
    """A styled label with Regency-era aesthetic"""
    bg_color = ListProperty(REGENCY_COLORS['parchment'])
    text_color = ListProperty(REGENCY_COLORS['ink'])
    font_size = NumericProperty(18)
    font_name = StringProperty('fonts/GentiumBookBasic-Regular.ttf')
    italic = BooleanProperty(False)
    bold = BooleanProperty(False)


class AnimatedCharacter(Label):
    """A label that animates each character of text like handwriting"""
    duration = NumericProperty(3.0)  # Total duration of animation
    full_text = StringProperty('')   # The complete text to animate
    display_text = StringProperty('') # Current displayed text
    
    def __init__(self, **kwargs):
        super(AnimatedCharacter, self).__init__(**kwargs)
        self.markup = True
        self.char_index = 0
        self.full_text = kwargs.get('text', '')
        self.text = ''
        self.display_text = ''
    
    def start_animation(self):
        """Start animating the text"""
        self.char_index = 0
        self.text = ''
        Clock.schedule_interval(self._animate_text, 0.05)
    
    def _animate_text(self, dt):
        """Add one character at a time"""
        if self.char_index < len(self.full_text):
            self.char_index += 1
            self.text = self.full_text[:self.char_index]
            return True
        return False


class AnimatedQuoteBox(BoxLayout):
    """A decorative box for animated Jane Austen quotes"""
    quote_text = StringProperty('')
    source_text = StringProperty('')
    context_text = StringProperty('')
    bg_color = ListProperty(REGENCY_COLORS['cream'])
    
    def __init__(self, **kwargs):
        super(AnimatedQuoteBox, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20, 20, 20, 20]
        self.spacing = 10
        
        # Add decorative elements and quote text
        self._build_quote_box()
    
    def _build_quote_box(self):
        """Build the quote box with all elements"""
        # Top decorative element
        self.add_widget(self._create_decorative_element())
        
        # Quote text with animation
        self.quote_label = AnimatedCharacter(
            text=self.quote_text,
            font_size=22,
            italic=True,
            color=REGENCY_COLORS['ink'],
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=100
        )
        self.add_widget(self.quote_label)
        
        # Source text
        if self.source_text:
            source_label = Label(
                text=f"— {self.source_text}",
                font_size=18,
                italic=True,
                color=REGENCY_COLORS['faded_ink'],
                halign='right',
                valign='middle',
                size_hint_y=None,
                height=30
            )
            self.add_widget(source_label)
        
        # Context information if available
        if self.context_text:
            context_label = Label(
                text=self.context_text,
                font_size=16,
                color=REGENCY_COLORS['faded_ink'],
                halign='center',
                valign='top',
                size_hint_y=None,
                height=80,
                text_size=(self.width - 40, None)
            )
            self.add_widget(context_label)
        
        # Bottom decorative element
        self.add_widget(self._create_decorative_element())
    
    def _create_decorative_element(self):
        """Create a decorative flourish for the quote box"""
        decorative_widget = Widget(size_hint_y=None, height=30)
        
        with decorative_widget.canvas:
            # Draw decorative flourish
            Color(*REGENCY_COLORS['burgundy'])
            
            # Create curved line with multiple points
            points = []
            width = 300  # Width of the flourish
            height = 20  # Height of the flourish
            num_points = 20
            
            for i in range(num_points):
                x = (i / (num_points - 1)) * width
                y = height/2 * math.sin(i * math.pi / (num_points/2))
                points.extend([x, y])
            
            # Center the flourish
            center_x = decorative_widget.width / 2 - width / 2
            center_y = decorative_widget.height / 2
            
            # Adjust all points to be centered
            adjusted_points = []
            for i in range(0, len(points), 2):
                adjusted_points.extend([points[i] + center_x, points[i+1] + center_y])
            
            # Create the bezier curve
            Line(bezier=adjusted_points, width=1.5)
            
            # Add decorative elements at the ends and middle
            Color(*REGENCY_COLORS['gold'])
            Ellipse(pos=(adjusted_points[0] - 5, adjusted_points[1] - 5), size=(10, 10))
            Ellipse(pos=(adjusted_points[-2] - 5, adjusted_points[-1] - 5), size=(10, 10))
            
            # Add a decorative element in the middle
            mid_index = len(adjusted_points) // 2
            Color(*REGENCY_COLORS['burgundy'])
            Ellipse(pos=(adjusted_points[mid_index] - 7, adjusted_points[mid_index+1] - 7), size=(14, 14))
            
        return decorative_widget
    
    def start_animation(self):
        """Start the quote text animation"""
        self.quote_label.start_animation()


class CharacterPortrait(BoxLayout):
    """A visual representation of a character using Kivy graphics"""
    character_name = StringProperty("")
    character_gender = StringProperty("female")
    character_occupation = StringProperty("")
    character_class = StringProperty("middle")
    character_personality = StringProperty("")
    bg_color = ListProperty(REGENCY_COLORS['parchment'])
    
    def __init__(self, **kwargs):
        super(CharacterPortrait, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 400)
        
        # Extract character attributes from kwargs
        self.character_name = kwargs.get('name', self.character_name)
        self.character_gender = kwargs.get('gender', self.character_gender)
        self.character_class = kwargs.get('social_class', self.character_class)
        self.character_occupation = kwargs.get('occupation', self.character_occupation)
        self.character_personality = kwargs.get('personality', self.character_personality)
        
        # Build the portrait
        self._create_portrait()
    
    def _create_portrait(self):
        """Create the visual portrait of the character"""
        # Portrait frame
        portrait_frame = Widget(size_hint=(1, 0.7))
        self.add_widget(portrait_frame)
        
        with portrait_frame.canvas:
            # Background frame
            Color(*REGENCY_COLORS['cream'])
            Rectangle(pos=(10, 10), size=(portrait_frame.width - 20, portrait_frame.height - 20))
            
            # Decorative border
            Color(*REGENCY_COLORS['gold'])
            Line(rectangle=(15, 15, portrait_frame.width - 30, portrait_frame.height - 30), width=2)
            
            # Character silhouette based on gender and personality
            self._draw_character_silhouette(portrait_frame)
            
            # Add decorative elements based on social class
            self._add_class_decorations(portrait_frame)
        
        # Add character name label
        name_label = RegencyLabel(
            text=self.character_name,
            font_size=22,
            bold=True,
            size_hint=(1, 0.1)
        )
        self.add_widget(name_label)
        
        # Add occupation label
        occupation_label = RegencyLabel(
            text=self.character_occupation,
            font_size=18,
            italic=True,
            size_hint=(1, 0.1)
        )
        self.add_widget(occupation_label)
        
        # Add personality traits in a subtle script font
        traits_label = RegencyLabel(
            text=f"[i]{self.character_personality}[/i]",
            font_size=16,
            text_color=REGENCY_COLORS['faded_ink'],
            size_hint=(1, 0.1)
        )
        self.add_widget(traits_label)
    
    def _draw_character_silhouette(self, frame_widget):
        """Draw a character silhouette based on attributes"""
        width, height = frame_widget.width - 40, frame_widget.height - 40
        x, y = 20, 20
        center_x = x + width/2
        
        # Choose color variations based on personality
        personality_traits = self.character_personality.lower()
        
        # Select appropriate colors based on personality traits
        if "reserved" in personality_traits or "serious" in personality_traits:
            primary_color = REGENCY_COLORS['navy']
            secondary_color = REGENCY_COLORS['royal_blue']
        elif "romantic" in personality_traits or "passionate" in personality_traits:
            primary_color = REGENCY_COLORS['burgundy']
            secondary_color = REGENCY_COLORS['blush']
        elif "intelligent" in personality_traits or "witty" in personality_traits:
            primary_color = REGENCY_COLORS['forest_green']
            secondary_color = REGENCY_COLORS['olive']
        else:
            # Default colors
            primary_color = REGENCY_COLORS['royal_blue']
            secondary_color = REGENCY_COLORS['navy']
        
        # Draw the silhouette differently based on gender
        if self.character_gender.lower() == "female":
            # Female silhouette with dress
            
            # Dress shape
            Color(*primary_color)
            
            # Head
            head_size = width * 0.25
            head_x = center_x - head_size/2
            head_y = y + height * 0.7
            Ellipse(pos=(head_x, head_y), size=(head_size, head_size))
            
            # Neck
            neck_height = height * 0.05
            neck_width = head_size * 0.4
            neck_x = center_x - neck_width/2
            neck_y = head_y
            Rectangle(pos=(neck_x, neck_y - neck_height), size=(neck_width, neck_height))
            
            # Shoulders and upper body
            Color(*secondary_color)
            shoulder_width = width * 0.5
            shoulder_height = height * 0.25
            shoulder_x = center_x - shoulder_width/2
            shoulder_y = head_y - neck_height - shoulder_height
            
            # Dress with triangular shape for Regency empire waistline
            dress_points = [
                shoulder_x, shoulder_y,  # Left shoulder
                shoulder_x + shoulder_width, shoulder_y,  # Right shoulder
                center_x + width * 0.3, y,  # Bottom right of dress
                center_x - width * 0.3, y   # Bottom left of dress
            ]
            Color(*primary_color)
            Line(points=dress_points, width=2)
            
            # Regency empire waistline - high waisted
            waist_y = shoulder_y - height * 0.05
            Line(points=[shoulder_x, waist_y, shoulder_x + shoulder_width, waist_y], width=1.5)
            
            # Add decorative details - small puffed sleeves
            Color(*secondary_color)
            sleeve_size = width * 0.15
            Ellipse(pos=(shoulder_x - sleeve_size * 0.5, shoulder_y - sleeve_size * 0.5), 
                    size=(sleeve_size, sleeve_size))
            Ellipse(pos=(shoulder_x + shoulder_width - sleeve_size * 0.5, shoulder_y - sleeve_size * 0.5), 
                    size=(sleeve_size, sleeve_size))
            
        else:  # Male silhouette
            # Head
            head_size = width * 0.25
            head_x = center_x - head_size/2
            head_y = y + height * 0.7
            Ellipse(pos=(head_x, head_y), size=(head_size, head_size))
            
            # Neck
            neck_height = height * 0.05
            neck_width = head_size * 0.4
            neck_x = center_x - neck_width/2
            neck_y = head_y
            Rectangle(pos=(neck_x, neck_y - neck_height), size=(neck_width, neck_height))
            
            # Shoulders and coat
            Color(*primary_color)
            shoulder_width = width * 0.6
            shoulder_x = center_x - shoulder_width/2
            shoulder_y = head_y - neck_height
            
            # Regency coat with tailcoat shape
            coat_top_width = shoulder_width
            coat_waist_width = shoulder_width * 0.8
            coat_bottom_width = shoulder_width * 1.2
            
            coat_points = [
                shoulder_x, shoulder_y,  # Left shoulder
                shoulder_x + coat_top_width, shoulder_y,  # Right shoulder
                shoulder_x + coat_top_width, shoulder_y - height * 0.2,  # Right side at waist
                shoulder_x + coat_bottom_width/2, y,  # Right coat tail
                center_x, y + height * 0.2,  # Middle indent for tailcoat
                shoulder_x + coat_bottom_width - coat_bottom_width/2, y,  # Left coat tail
                shoulder_x, shoulder_y - height * 0.2  # Left side at waist
            ]
            
            Line(points=coat_points, width=2)
            
            # Waistcoat
            Color(*secondary_color)
            waistcoat_top = shoulder_y - height * 0.05
            waistcoat_bottom = shoulder_y - height * 0.3
            waistcoat_width = coat_top_width * 0.5
            waistcoat_x = center_x - waistcoat_width/2
            
            Rectangle(pos=(waistcoat_x, waistcoat_bottom), 
                     size=(waistcoat_width, waistcoat_top - waistcoat_bottom))
            
            # Cravat
            Color(0.95, 0.95, 0.95, 1)  # White for cravat
            cravat_height = height * 0.05
            cravat_width = neck_width * 1.5
            cravat_x = center_x - cravat_width/2
            cravat_y = neck_y - neck_height - cravat_height/2
            
            Ellipse(pos=(cravat_x, cravat_y), size=(cravat_width, cravat_height))
    
    def _add_class_decorations(self, frame_widget):
        """Add decorative elements based on social class"""
        width, height = frame_widget.width - 40, frame_widget.height - 40
        x, y = 20, 20
        
        if self.character_class.lower() == "upper":
            # Ornate gold frame for upper class
            Color(*REGENCY_COLORS['gold'])
            Line(rectangle=(5, 5, frame_widget.width - 10, frame_widget.height - 10), width=3)
            
            # Additional decorative corners
            corner_size = 20
            # Top left
            Line(points=[5, 5, 5 + corner_size, 5, 5, 5 + corner_size, 5, 5], width=3)
            # Top right
            Line(points=[frame_widget.width - 5, 5, frame_widget.width - 5 - corner_size, 5, 
                         frame_widget.width - 5, 5 + corner_size, frame_widget.width - 5, 5], width=3)
            # Bottom left
            Line(points=[5, frame_widget.height - 5, 5 + corner_size, frame_widget.height - 5, 
                         5, frame_widget.height - 5 - corner_size, 5, frame_widget.height - 5], width=3)
            # Bottom right
            Line(points=[frame_widget.width - 5, frame_widget.height - 5, 
                         frame_widget.width - 5 - corner_size, frame_widget.height - 5,
                         frame_widget.width - 5, frame_widget.height - 5 - corner_size, 
                         frame_widget.width - 5, frame_widget.height - 5], width=3)
            
        elif self.character_class.lower() == "middle":
            # Simpler frame for middle class
            Color(*REGENCY_COLORS['silver'])
            Line(rectangle=(10, 10, frame_widget.width - 20, frame_widget.height - 20), width=2)
            
        else:  # lower class
            # Simple line frame for lower class
            Color(*REGENCY_COLORS['faded_ink'])
            Line(rectangle=(15, 15, frame_widget.width - 30, frame_widget.height - 30), width=1)


class SceneIllustration(Widget):
    """Creates illustrated scenes with Regency-era elements"""
    location = StringProperty("")
    season = StringProperty("spring")
    time_of_day = StringProperty("day")
    weather = StringProperty("clear")
    
    def __init__(self, **kwargs):
        super(SceneIllustration, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (600, 400)
        
        # Extract scene attributes
        self.location = kwargs.get('location', self.location)
        self.season = kwargs.get('season', self.season).lower()
        self.time_of_day = kwargs.get('time_of_day', self.time_of_day).lower()
        self.weather = kwargs.get('weather', self.weather).lower()
        
        # Design the scene
        Clock.schedule_once(self._create_scene, 0.1)
    
    def _create_scene(self, dt):
        """Create the visual representation of the scene"""
        with self.canvas:
            # Clear any existing drawings
            self.canvas.clear()
            
            # Background based on time of day and weather
            self._draw_background()
            
            # Draw location elements
            self._draw_location()
            
            # Add seasonal elements
            self._add_seasonal_elements()
            
            # Weather effects if applicable
            if self.weather != "clear":
                self._add_weather_effects()
            
            # Add scene frame
            self._add_decorative_frame()
    
    def _draw_background(self):
        """Draw the sky and ground based on time and season"""
        # Sky colors based on time of day
        if self.time_of_day == "dawn" or self.time_of_day == "dusk":
            # Pinkish/orange sky for dawn/dusk
            Color(0.9, 0.6, 0.4, 1)
        elif self.time_of_day == "night":
            # Dark blue for night
            Color(0.1, 0.1, 0.3, 1)
        else:  # day
            # Blue sky for day, varied by season
            if self.season == "winter":
                Color(0.7, 0.8, 0.9, 1)  # Pale winter sky
            elif self.season == "autumn":
                Color(0.6, 0.7, 0.9, 1)  # Autumn sky
            else:
                Color(0.5, 0.7, 1.0, 1)  # Spring/summer blue sky
        
        # Draw sky (top 2/3)
        Rectangle(pos=(0, self.height/3), size=(self.width, self.height*2/3))
        
        # Ground based on season
        if self.season == "winter":
            Color(0.9, 0.9, 0.9, 1)  # Snow
        elif self.season == "autumn":
            Color(0.6, 0.4, 0.2, 1)  # Brown autumn ground
        elif self.season == "summer":
            Color(0.2, 0.6, 0.2, 1)  # Vibrant green for summer
        else:  # spring
            Color(0.3, 0.7, 0.3, 1)  # Fresh spring green
        
        # Draw ground (bottom 1/3)
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
    
    def _draw_location(self):
        """Draw elements based on the location"""
        location_lower = self.location.lower()
        
        if "ballroom" in location_lower or "assembly" in location_lower:
            self._draw_ballroom()
        elif "parlour" in location_lower or "drawing room" in location_lower:
            self._draw_drawing_room()
        elif "garden" in location_lower or "park" in location_lower:
            self._draw_garden()
        elif "estate" in location_lower or "manor" in location_lower or "hall" in location_lower:
            self._draw_estate()
        elif "village" in location_lower or "town" in location_lower:
            self._draw_village()
        elif "countryside" in location_lower or "field" in location_lower:
            self._draw_countryside()
        elif "london" in location_lower or "city" in location_lower:
            self._draw_london()
        else:
            # Default to countryside if no specific location matched
            self._draw_countryside()
    
    def _draw_ballroom(self):
        """Draw a Regency-era ballroom"""
        # Floor
        Color(0.8, 0.7, 0.5, 1)  # Wooden floor color
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
        
        # Walls
        Color(0.9, 0.85, 0.7, 1)  # Wall color
        Rectangle(pos=(0, self.height/3), size=(self.width, self.height*2/3))
        
        # Windows
        Color(0.8, 0.9, 1.0, 1)  # Window glass
        window_width = self.width / 8
        window_height = self.height / 4
        window_spacing = self.width / 6
        
        for i in range(3):
            window_x = window_spacing + i * window_spacing
            window_y = self.height/2
            
            # Window frame
            Color(0.8, 0.7, 0.5, 1)  # Frame color
            Line(rectangle=(window_x - 5, window_y - 5, 
                           window_width + 10, window_height + 10), width=2)
            
            # Window glass
            Color(0.8, 0.9, 1.0, 1)
            Rectangle(pos=(window_x, window_y), 
                     size=(window_width, window_height))
            
            # Window dividers
            Color(0.8, 0.7, 0.5, 1)
            Line(points=[window_x, window_y + window_height/2, 
                        window_x + window_width, window_y + window_height/2], width=2)
            Line(points=[window_x + window_width/2, window_y, 
                        window_x + window_width/2, window_y + window_height], width=2)
        
        # Chandelier
        Color(0.9, 0.8, 0.2, 1)  # Gold color
        chandelier_x = self.width / 2
        chandelier_y = self.height * 0.8
        chandelier_size = self.width / 10
        
        # Center piece
        Ellipse(pos=(chandelier_x - chandelier_size/2, chandelier_y - chandelier_size/2), 
               size=(chandelier_size, chandelier_size))
        
        # Hanging chain
        Line(points=[chandelier_x, chandelier_y + chandelier_size/2, 
                    chandelier_x, self.height], width=2)
        
        # Candle arms
        arm_length = chandelier_size * 1.5
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            end_x = chandelier_x + arm_length * math.cos(rad)
            end_y = chandelier_y + arm_length * math.sin(rad)
            
            Line(points=[chandelier_x, chandelier_y, end_x, end_y], width=2)
            
            # Candle at end of arm
            candle_size = chandelier_size / 4
            Ellipse(pos=(end_x - candle_size/2, end_y - candle_size/2), 
                   size=(candle_size, candle_size))
            
            # Candle flame
            Color(1.0, 0.8, 0.2, 1)  # Flame color
            flame_size = candle_size / 2
            Ellipse(pos=(end_x - flame_size/2, end_y + candle_size/2), 
                   size=(flame_size, flame_size))
    
    def _draw_drawing_room(self):
        """Draw a Regency-era drawing room or parlour"""
        # Floor
        Color(0.6, 0.4, 0.2, 1)  # Dark wood floor
        Rectangle(pos=(0, 0), size=(self.width, self.height/4))
        
        # Wallpaper
        Color(0.8, 0.75, 0.6, 1)  # Wall color
        Rectangle(pos=(0, self.height/4), size=(self.width, self.height*3/4))
        
        # Wallpaper pattern
        Color(0.7, 0.65, 0.5, 1)  # Pattern color
        pattern_size = 20
        for x in range(0, int(self.width), pattern_size*2):
            for y in range(int(self.height/4), int(self.height), pattern_size*2):
                # Draw simple damask-like pattern
                Ellipse(pos=(x, y), size=(pattern_size, pattern_size))
        
        # Fireplace
        fireplace_width = self.width / 3
        fireplace_height = self.height / 2
        fireplace_x = (self.width - fireplace_width) / 2
        fireplace_y = self.height/4 - fireplace_height/4
        
        # Fireplace mantel and surround
        Color(0.3, 0.3, 0.3, 1)  # Dark stone color
        Rectangle(pos=(fireplace_x, fireplace_y), 
                 size=(fireplace_width, fireplace_height))
        
        # Fireplace opening
        Color(0.1, 0.05, 0.0, 1)  # Dark opening
        inner_width = fireplace_width * 0.7
        inner_height = fireplace_height * 0.6
        inner_x = fireplace_x + (fireplace_width - inner_width) / 2
        inner_y = fireplace_y + fireplace_height * 0.1
        Rectangle(pos=(inner_x, inner_y), size=(inner_width, inner_height))
        
        # Fire
        if self.season == "winter" or self.season == "autumn":
            # Flames
            Color(0.9, 0.3, 0.1, 1)  # Orange flame
            flame_points = []
            flame_width = inner_width * 0.8
            flame_height = inner_height * 0.7
            flame_x = inner_x + (inner_width - flame_width) / 2
            flame_y = inner_y + inner_height * 0.1
            
            # Create flickering flame points
            num_points = 10
            for i in range(num_points + 1):
                x_pos = flame_x + (i / num_points) * flame_width
                height_var = random.uniform(0.7, 1.0) * flame_height
                y_pos = flame_y + height_var
                flame_points.extend([x_pos, y_pos])
            
            # Add bottom points to close the shape
            flame_points.extend([flame_x + flame_width, flame_y, flame_x, flame_y])
            
            # Draw filled flame
            Color(0.9, 0.4, 0.0, 0.8)
            Line(points=flame_points, width=2, close=True)
            
            # Embers
            Color(1.0, 0.5, 0.0, 0.6)
            for _ in range(5):
                ember_size = random.uniform(2, 5)
                ember_x = random.uniform(inner_x, inner_x + inner_width - ember_size)
                ember_y = random.uniform(inner_y, inner_y + inner_height/3)
                Ellipse(pos=(ember_x, ember_y), size=(ember_size, ember_size))
        
        # Furniture: chairs
        self._draw_armchair(self.width/4, self.height/3, facing="right")
        self._draw_armchair(3*self.width/4, self.height/3, facing="left")
        
        # Table
        table_width = self.width / 6
        table_height = table_width / 2
        table_x = (self.width - table_width) / 2
        table_y = self.height / 3
        
        Color(0.5, 0.35, 0.2, 1)  # Table wood color
        Ellipse(pos=(table_x, table_y), size=(table_width, table_height))
        
        # Table legs
        leg_width = table_width / 10
        Rectangle(pos=(table_x + table_width/4, table_y - table_height), 
                 size=(leg_width, table_height))
        Rectangle(pos=(table_x + table_width*3/4 - leg_width, table_y - table_height), 
                 size=(leg_width, table_height))
        
        # Tea set on table
        Color(0.9, 0.9, 0.9, 1)  # White china
        teapot_size = table_width / 4
        Ellipse(pos=(table_x + table_width/2 - teapot_size/2, table_y + table_height/4), 
               size=(teapot_size, teapot_size))
    
    def _draw_armchair(self, x, y, facing="right"):
        """Draw a Regency-era armchair"""
        chair_width = self.width / 8
        chair_height = chair_width * 1.5
        chair_depth = chair_width * 0.8
        
        # Chair body
        Color(0.7, 0.5, 0.3, 1)  # Chair wood color
        
        # Seat
        Rectangle(pos=(x - chair_width/2, y), size=(chair_width, chair_depth))
        
        # Back
        back_height = chair_height - chair_depth
        Rectangle(pos=(x - chair_width/2, y + chair_depth), 
                 size=(chair_width, back_height))
        
        # Arms
        arm_width = chair_width / 4
        arm_height = chair_depth / 2
        
        # Left arm
        left_x = x - chair_width/2 - arm_width/2 if facing == "right" else x - chair_width/2
        Rectangle(pos=(left_x, y + chair_depth/2), 
                 size=(arm_width, arm_height))
        
        # Right arm
        right_x = x + chair_width/2 - arm_width/2 if facing == "right" else x + chair_width/2 - arm_width
        Rectangle(pos=(right_x, y + chair_depth/2), 
                 size=(arm_width, arm_height))
        
        # Cushion
        Color(0.6, 0.2, 0.1, 1)  # Red upholstery
        cushion_inset = chair_width / 10
        Rectangle(pos=(x - chair_width/2 + cushion_inset, y + cushion_inset), 
                 size=(chair_width - 2*cushion_inset, chair_depth - 2*cushion_inset))
        
        # Back cushion
        Rectangle(pos=(x - chair_width/2 + cushion_inset, y + chair_depth + cushion_inset), 
                 size=(chair_width - 2*cushion_inset, back_height - 2*cushion_inset))
    
    def _draw_garden(self):
        """Draw a Regency-era garden"""
        # Sky - already drawn in background
        
        # Lawn
        Color(0.2, 0.6, 0.2, 1)  # Green grass
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
        
        # Garden paths
        Color(0.8, 0.7, 0.5, 1)  # Gravel path
        path_width = self.width / 10
        
        # Horizontal path
        Rectangle(pos=(0, self.height/6 - path_width/2), 
                 size=(self.width, path_width))
        
        # Vertical path
        Rectangle(pos=(self.width/2 - path_width/2, 0), 
                 size=(path_width, self.height/3))
        
        # Garden features based on season
        if self.season == "spring":
            # Spring flowers in beds
            self._draw_flower_beds(colors=[(0.9, 0.5, 0.9, 1), (1.0, 1.0, 0.0, 1), 
                                          (0.9, 0.0, 0.3, 1)])
        elif self.season == "summer":
            # Lush summer garden
            self._draw_flower_beds(colors=[(1.0, 0.0, 0.0, 1), (0.0, 0.0, 1.0, 1), 
                                          (1.0, 0.5, 0.0, 1)])
        elif self.season == "autumn":
            # Autumn colors
            self._draw_flower_beds(colors=[(0.8, 0.4, 0.0, 1), (0.7, 0.2, 0.0, 1), 
                                          (0.6, 0.5, 0.0, 1)])
        else:  # winter
            # Winter garden - no flowers, just structure
            self._draw_flower_beds(colors=[(0.6, 0.6, 0.6, 1)])
        
        # Garden statues
        self._draw_garden_statue(self.width/4, self.height/3 + 50)
        self._draw_garden_statue(3*self.width/4, self.height/3 + 50)
        
        # Garden bench
        bench_width = self.width / 6
        bench_height = bench_width / 3
        bench_x = (self.width - bench_width) / 2
        bench_y = self.height/6
        
        Color(0.5, 0.5, 0.5, 1)  # Stone bench color
        Rectangle(pos=(bench_x, bench_y), size=(bench_width, bench_height))
        
        # Bench legs
        leg_width = bench_width / 8
        leg_height = bench_height / 2
        Rectangle(pos=(bench_x + leg_width, bench_y - leg_height), 
                 size=(leg_width, leg_height))
        Rectangle(pos=(bench_x + bench_width - 2*leg_width, bench_y - leg_height), 
                 size=(leg_width, leg_height))
        
        # Distant mansion/house
        house_width = self.width / 3
        house_height = self.height / 4
        house_x = (self.width - house_width) / 2
        house_y = self.height * 2/3
        
        Color(0.8, 0.7, 0.5, 1)  # House color
        Rectangle(pos=(house_x, house_y), size=(house_width, house_height))
        
        # Windows
        Color(0.9, 0.9, 1.0, 1)  # Window color
        window_size = house_width / 10
        window_spacing = house_width / 5
        
        for i in range(3):
            window_x = house_x + window_spacing/2 + i * window_spacing
            window_y = house_y + house_height / 2
            Rectangle(pos=(window_x, window_y), size=(window_size, window_size))
        
        # Roof
        Color(0.5, 0.3, 0.2, 1)  # Roof color
        roof_points = [
            house_x - house_width/10, house_y + house_height,  # Left edge
            house_x + house_width + house_width/10, house_y + house_height,  # Right edge
            house_x + house_width/2, house_y + house_height + house_height/2  # Peak
        ]
        Line(points=roof_points, width=2, close=True)
    
    def _draw_flower_beds(self, colors):
        """Draw garden flower beds with seasonal colors"""
        bed_width = self.width / 6
        bed_height = self.height / 12
        
        # Four flower beds in corners
        for i, (x_pos, y_pos) in enumerate([
            (self.width/4 - bed_width/2, self.height/12),  # Bottom left
            (3*self.width/4 - bed_width/2, self.height/12),  # Bottom right
            (self.width/4 - bed_width/2, self.height/4),  # Top left
            (3*self.width/4 - bed_width/2, self.height/4)  # Top right
        ]):
            # Bed outline
            Color(0.4, 0.3, 0.2, 1)  # Soil color
            Rectangle(pos=(x_pos, y_pos), size=(bed_width, bed_height))
            
            # Flowers
            if self.season != "winter":
                color_idx = i % len(colors)
                Color(*colors[color_idx])
                
                # Draw several small flowers or plants
                for _ in range(10):
                    flower_size = random.uniform(5, 10)
                    flower_x = random.uniform(x_pos, x_pos + bed_width - flower_size)
                    flower_y = random.uniform(y_pos, y_pos + bed_height - flower_size)
                    Ellipse(pos=(flower_x, flower_y), size=(flower_size, flower_size))
    
    def _draw_garden_statue(self, x, y):
        """Draw a garden statue"""
        statue_width = self.width / 20
        statue_height = self.height / 8
        
        # Base
        Color(0.7, 0.7, 0.7, 1)  # Stone color
        base_width = statue_width * 1.5
        base_height = statue_height / 6
        Rectangle(pos=(x - base_width/2, y), size=(base_width, base_height))
        
        # Statue body
        Color(0.8, 0.8, 0.8, 1)  # Lighter stone color
        Ellipse(pos=(x - statue_width/2, y + base_height), 
               size=(statue_width, statue_height))
        
        # Details with lines
        Color(0.6, 0.6, 0.6, 1)  # Shadow color
        Line(points=[x, y + base_height, 
                    x, y + base_height + statue_height], width=1)
        
        # Arms suggestion
        arm_length = statue_width * 0.7
        Line(points=[x, y + base_height + statue_height*0.7, 
                    x - arm_length, y + base_height + statue_height*0.6], width=1)
        Line(points=[x, y + base_height + statue_height*0.7, 
                    x + arm_length, y + base_height + statue_height*0.6], width=1)
    
    def _draw_estate(self):
        """Draw a Regency-era country estate or manor house"""
        # Ground/lawn
        Color(0.3, 0.6, 0.3, 1)  # Green lawn
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
        
        # Manor house
        house_width = self.width * 0.6
        house_height = self.height * 0.5
        house_x = (self.width - house_width) / 2
        house_y = self.height/3
        
        # Main house body
        Color(0.85, 0.8, 0.7, 1)  # Stone color
        Rectangle(pos=(house_x, house_y), size=(house_width, house_height))
        
        # Windows (3 rows of 5)
        Color(0.9, 0.95, 1.0, 1)  # Window glass
        window_width = house_width / 12
        window_height = house_height / 8
        window_h_spacing = house_width / 6
        window_v_spacing = house_height / 4
        
        for row in range(3):
            for col in range(5):
                window_x = house_x + window_h_spacing/2 + col * window_h_spacing
                window_y = house_y + window_v_spacing/2 + row * window_v_spacing
                
                # Window frame
                Color(0.6, 0.6, 0.6, 1)
                Line(rectangle=(window_x, window_y, window_width, window_height), width=1)
                
                # Glass
                Color(0.9, 0.95, 1.0, 1)
                Rectangle(pos=(window_x, window_y), size=(window_width, window_height))
                
                # Window dividers
                Color(0.6, 0.6, 0.6, 1)
                Line(points=[window_x, window_y + window_height/2, 
                            window_x + window_width, window_y + window_height/2], width=1)
                Line(points=[window_x + window_width/2, window_y, 
                            window_x + window_width/2, window_y + window_height], width=1)
        
        # Grand entrance
        door_width = house_width / 10
        door_height = house_height / 4
        door_x = house_x + (house_width - door_width) / 2
        door_y = house_y
        
        # Door frame
        Color(0.6, 0.4, 0.2, 1)  # Door color
        Rectangle(pos=(door_x, door_y), size=(door_width, door_height))
        
        # Steps leading to door
        step_width = door_width * 1.5
        step_height = door_height / 10
        for i in range(3):
            step_x = door_x + (door_width - step_width)/2 + step_width/6 * i
            step_y = door_y - (i+1) * step_height
            step_w = step_width - step_width/3 * i
            
            Color(0.7, 0.7, 0.7, 1)  # Stone steps
            Rectangle(pos=(step_x, step_y), size=(step_w, step_height))
        
        # Driveway
        Color(0.7, 0.6, 0.5, 1)  # Gravel driveway
        driveway_width = step_width * 2
        driveway_points = [
            door_x + door_width/2, door_y - 3 * step_height,  # Start at bottom of steps
            door_x + door_width/2 - driveway_width/2, 0,     # Left edge at bottom
            door_x + door_width/2 + driveway_width/2, 0,     # Right edge at bottom
            door_x + door_width/2, door_y - 3 * step_height  # Back to start
        ]
        Line(points=driveway_points, width=2, close=True)
        
        # Gardens/landscaping on either side
        self._draw_simple_tree(house_x - house_width/6, house_y)
        self._draw_simple_tree(house_x + house_width + house_width/6, house_y)
        
        # Rooftop and chimneys
        # Main roof
        Color(0.4, 0.3, 0.2, 1)  # Roof color
        roof_height = house_height / 6
        roof_points = [
            house_x - house_width/20, house_y + house_height,
            house_x + house_width + house_width/20, house_y + house_height,
            house_x + house_width/2, house_y + house_height + roof_height
        ]
        Line(points=roof_points, width=2, close=True)
        
        # Chimneys
        chimney_width = house_width / 30
        chimney_height = roof_height * 1.5
        
        for x_pos in [house_x + house_width/4, house_x + house_width*3/4]:
            Color(0.5, 0.3, 0.3, 1)  # Brick color
            Rectangle(pos=(x_pos, house_y + house_height + roof_height/2), 
                     size=(chimney_width, chimney_height))
            
            # Chimney top
            chimney_top_width = chimney_width * 1.3
            chimney_top_height = chimney_height / 10
            Rectangle(pos=(x_pos - (chimney_top_width-chimney_width)/2, 
                          house_y + house_height + roof_height/2 + chimney_height), 
                     size=(chimney_top_width, chimney_top_height))
    
    def _draw_simple_tree(self, x, y):
        """Draw a simple tree"""
        trunk_width = self.width / 40
        trunk_height = self.height / 10
        
        # Tree trunk
        Color(0.5, 0.3, 0.2, 1)  # Brown trunk
        Rectangle(pos=(x - trunk_width/2, y), size=(trunk_width, trunk_height))
        
        # Tree foliage varies by season
        if self.season == "spring":
            Color(0.5, 0.8, 0.3, 1)  # Fresh spring green
        elif self.season == "summer":
            Color(0.2, 0.6, 0.2, 1)  # Deep summer green
        elif self.season == "autumn":
            Color(0.8, 0.4, 0.0, 1)  # Autumn orange
        else:  # winter
            if self.weather == "snow":
                Color(0.9, 0.9, 0.9, 1)  # Snow covered
            else:
                Color(0.5, 0.5, 0.5, 1)  # Bare winter branches
        
        # Foliage as circles
        foliage_size = trunk_width * 7
        Ellipse(pos=(x - foliage_size/2, y + trunk_height*0.8), 
               size=(foliage_size, foliage_size))
        
        # Add smaller circles for more organic shape
        smaller_size = foliage_size * 0.8
        offset = foliage_size * 0.4
        
        for dx, dy in [(offset, 0), (-offset, 0), (0, offset), (0, -offset/2)]:
            Ellipse(pos=(x - smaller_size/2 + dx, y + trunk_height*0.8 + dy), 
                   size=(smaller_size, smaller_size))
    
    def _draw_village(self):
        """Draw a Regency-era village or town"""
        # Ground/street
        Color(0.6, 0.5, 0.4, 1)  # Dirt/cobblestone street
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
        
        # Draw row of buildings
        building_width = self.width / 6
        building_spacing = self.width / 20
        total_buildings = 4
        total_width = total_buildings * building_width + (total_buildings - 1) * building_spacing
        start_x = (self.width - total_width) / 2
        
        for i in range(total_buildings):
            bldg_x = start_x + i * (building_width + building_spacing)
            bldg_height = random.uniform(self.height/4, self.height/3)
            self._draw_village_building(bldg_x, self.height/3, building_width, bldg_height)
        
        # Church or important building in background
        church_width = self.width / 5
        church_height = self.height / 3
        church_x = (self.width - church_width) / 2
        church_y = self.height * 2/3
        
        # Main church building
        Color(0.75, 0.75, 0.75, 1)  # Stone color
        Rectangle(pos=(church_x, church_y), size=(church_width, church_height))
        
        # Church tower/steeple
        tower_width = church_width / 3
        tower_height = church_height * 1.5
        tower_x = church_x + (church_width - tower_width) / 2
        tower_y = church_y
        
        Rectangle(pos=(tower_x, tower_y), size=(tower_width, tower_height))
        
        # Tower roof/spire
        spire_height = tower_height / 2
        spire_points = [
            tower_x, tower_y + tower_height,
            tower_x + tower_width, tower_y + tower_height,
            tower_x + tower_width/2, tower_y + tower_height + spire_height
        ]
        
        Color(0.4, 0.3, 0.2, 1)  # Roof color
        Line(points=spire_points, width=2, close=True)
        
        # Windows
        Color(0.9, 0.95, 1.0, 1)  # Window glass
        window_width = tower_width / 2
        window_height = tower_height / 10
        window_x = tower_x + (tower_width - window_width) / 2
        window_y = tower_y + tower_height / 2
        
        # Round church window
        Ellipse(pos=(window_x, window_y), size=(window_width, window_width))
        
        # Trees and greenery
        for x_pos in [self.width/8, self.width*7/8]:
            self._draw_simple_tree(x_pos, self.height/3)
    
    def _draw_village_building(self, x, y, width, height):
        """Draw a Regency-era village building"""
        # Main building
        r, g, b = random.uniform(0.7, 0.9), random.uniform(0.7, 0.9), random.uniform(0.7, 0.9)
        Color(r, g, b, 1)  # Varied building colors
        Rectangle(pos=(x, y), size=(width, height))
        
        # Roof
        Color(0.5, 0.3, 0.2, 1)  # Roof color
        roof_height = height / 4
        roof_points = [
            x, y + height,
            x + width, y + height,
            x + width/2, y + height + roof_height
        ]
        Line(points=roof_points, width=2, close=True)
        
        # Door
        door_width = width / 4
        door_height = height / 3
        door_x = x + (width - door_width) / 2
        door_y = y
        
        Color(0.4, 0.25, 0.1, 1)  # Door color
        Rectangle(pos=(door_x, door_y), size=(door_width, door_height))
        
        # Windows (1-2 per building)
        Color(0.9, 0.95, 1.0, 1)  # Window glass
        window_width = width / 5
        window_height = height / 5
        
        # Window positions depend on building width
        if width > self.width / 8:
            # Two windows
            window_positions = [
                (x + width/4 - window_width/2, y + height/2),
                (x + width*3/4 - window_width/2, y + height/2)
            ]
        else:
            # One window
            window_positions = [(x + width/2 - window_width/2, y + height/2)]
        
        for wx, wy in window_positions:
            # Window frame
            Color(0.8, 0.8, 0.8, 1)
            Line(rectangle=(wx, wy, window_width, window_height), width=1)
            
            # Glass panes
            Color(0.9, 0.95, 1.0, 1)
            Rectangle(pos=(wx, wy), size=(window_width, window_height))
            
            # Window divider
            Color(0.8, 0.8, 0.8, 1)
            Line(points=[wx, wy + window_height/2, wx + window_width, wy + window_height/2], width=1)
            Line(points=[wx + window_width/2, wy, wx + window_width/2, wy + window_height], width=1)
        
        # Chimney (50% chance)
        if random.random() > 0.5:
            chimney_width = width / 10
            chimney_height = roof_height
            chimney_x = x + width * random.uniform(0.2, 0.8)
            chimney_y = y + height
            
            Color(0.6, 0.4, 0.4, 1)  # Chimney color
            Rectangle(pos=(chimney_x, chimney_y), size=(chimney_width, chimney_height))
    
    def _draw_countryside(self):
        """Draw a Regency-era countryside scene"""
        # Sky already drawn
        
        # Rolling hills
        num_hills = 5
        hill_color_base = (0.2, 0.6, 0.2)  # Base green
        
        # Adjust color by season
        if self.season == "spring":
            hill_color_base = (0.3, 0.7, 0.3)  # Brighter spring green
        elif self.season == "summer":
            hill_color_base = (0.2, 0.6, 0.2)  # Deep summer green
        elif self.season == "autumn":
            hill_color_base = (0.5, 0.4, 0.2)  # Autumn brown/gold
        else:  # winter
            if self.weather == "snow":
                hill_color_base = (0.85, 0.85, 0.85)  # Snowy hills
            else:
                hill_color_base = (0.5, 0.5, 0.3)  # Winter brown
        
        for i in range(num_hills):
            # Vary hill color slightly for depth
            r, g, b = hill_color_base
            color_var = 0.1
            hill_color = (
                r + random.uniform(-color_var, color_var),
                g + random.uniform(-color_var, color_var),
                b + random.uniform(-color_var, color_var),
                1
            )
            Color(*hill_color)
            
            # Create hill shape
            hill_width = self.width * random.uniform(0.3, 0.5)
            hill_height = self.height/3 * random.uniform(0.7, 1.0)
            hill_x = random.uniform(-hill_width/4, self.width - hill_width*3/4)
            hill_y = 0
            
            # Hill points (semi-elliptical)
            points = []
            num_points = 20
            for j in range(num_points + 1):
                x_pos = hill_x + (j / num_points) * hill_width
                # Height varies along the hill with a semi-elliptical shape
                height_factor = math.sin((j / num_points) * math.pi)
                y_pos = hill_y + height_factor * hill_height
                points.extend([x_pos, y_pos])
            
            # Close the shape by adding bottom points
            points.extend([hill_x + hill_width, 0, hill_x, 0])
            
            # Draw filled hill
            Line(points=points, close=True, width=2)
        
        # Trees scattered around
        for _ in range(5):
            tree_x = random.uniform(self.width/10, self.width*9/10)
            tree_y = random.uniform(0, self.height/4)
            self._draw_simple_tree(tree_x, tree_y)
        
        # Country lane/path
        Color(0.7, 0.6, 0.4, 1)  # Dirt path
        path_width = self.width / 10
        
        # Create winding path
        path_points = []
        num_segments = 10
        start_x = random.uniform(0, self.width/5)
        end_x = random.uniform(4*self.width/5, self.width)
        
        for i in range(num_segments + 1):
            t = i / num_segments
            # Create a gentle curve
            x_pos = start_x + t * (end_x - start_x)
            y_pos = (self.height/20) * math.sin(t * math.pi * 2) + self.height/10
            path_points.extend([x_pos, y_pos])
        
        # Draw the path
        Line(points=path_points, width=path_width)
        
        # Distant village or estate
        bldg_width = self.width / 10
        bldg_height = self.height / 15
        bldg_x = random.uniform(self.width/4, 3*self.width/4 - bldg_width)
        bldg_y = self.height/3 + self.height/10
        
        Color(0.7, 0.7, 0.7, 1)  # Distant building color
        Rectangle(pos=(bldg_x, bldg_y), size=(bldg_width, bldg_height))
        
        # Small roof
        roof_height = bldg_height / 3
        roof_points = [
            bldg_x, bldg_y + bldg_height,
            bldg_x + bldg_width, bldg_y + bldg_height,
            bldg_x + bldg_width/2, bldg_y + bldg_height + roof_height
        ]
        
        Color(0.4, 0.3, 0.2, 1)  # Roof color
        Line(points=roof_points, close=True, width=1)
    
    def _draw_london(self):
        """Draw a Regency-era London scene"""
        # Sky (may have London fog)
        if self.weather == "fog" or self.weather == "rain":
            # Foggy sky
            Color(0.7, 0.7, 0.7, 1)
            Rectangle(pos=(0, self.height/3), size=(self.width, self.height*2/3))
        
        # Ground/street
        Color(0.4, 0.4, 0.4, 1)  # Cobblestone street
        Rectangle(pos=(0, 0), size=(self.width, self.height/3))
        
        # Row of Georgian townhouses
        house_width = self.width / 8
        house_height = self.height / 2
        houses_per_row = 6
        total_width = houses_per_row * house_width
        start_x = (self.width - total_width) / 2
        
        for i in range(houses_per_row):
            house_x = start_x + i * house_width
            house_y = self.height/3
            
            # Individual house
            # Use slightly different colors for variety
            house_color = (
                0.8 + random.uniform(-0.1, 0.1),
                0.8 + random.uniform(-0.1, 0.1),
                0.8 + random.uniform(-0.1, 0.1),
                1
            )
            Color(*house_color)
            Rectangle(pos=(house_x, house_y), size=(house_width, house_height))
            
            # Windows (3 rows of 2)
            window_width = house_width / 4
            window_height = house_height / 8
            window_spacing_x = (house_width - 2*window_width) / 3
            window_spacing_y = house_height / 5
            
            for row in range(3):
                for col in range(2):
                    window_x = house_x + window_spacing_x + col * (window_width + window_spacing_x)
                    window_y = house_y + window_spacing_y + row * window_spacing_y + house_height / 10
                    
                    # Window frame
                    Color(0.3, 0.3, 0.3, 1)
                    Line(rectangle=(window_x, window_y, window_width, window_height), width=1)
                    
                    # Glass
                    if random.random() < 0.7:  # Some windows lit
                        Color(0.9, 0.8, 0.5, 1)  # Warm light
                    else:
                        Color(0.8, 0.9, 1.0, 1)  # Regular glass
                    Rectangle(pos=(window_x, window_y), size=(window_width, window_height))
                    
                    # Window dividers
                    Color(0.3, 0.3, 0.3, 1)
                    Line(points=[window_x, window_y + window_height/2, 
                                window_x + window_width, window_y + window_height/2], width=1)
            
            # Door
            door_width = house_width / 3
            door_height = house_height / 6
            door_x = house_x + (house_width - door_width) / 2
            door_y = house_y
            
            Color(0.1, 0.1, 0.1, 1)  # Black door
            Rectangle(pos=(door_x, door_y), size=(door_width, door_height))
            
            # Door knocker
            knocker_size = door_width / 8
            Color(0.8, 0.7, 0.0, 1)  # Brass knocker
            Ellipse(pos=(door_x + door_width/2 - knocker_size/2, 
                        door_y + door_height/2 - knocker_size/2), 
                   size=(knocker_size, knocker_size))
            
            # Steps
            step_width = door_width * 1.2
            step_height = house_height / 30
            
            for step in range(2):
                step_y = house_y - (step + 1) * step_height
                Color(0.7, 0.7, 0.7, 1)  # Stone steps
                Rectangle(pos=(door_x + (door_width - step_width)/2, step_y), 
                         size=(step_width, step_height))
        
        # Add a landmark - simplified St. Paul's or similar
        if random.random() > 0.5:
            self._draw_london_landmark()
        
        # Street elements
        # Streetlamp
        self._draw_streetlamp(self.width/4, self.height/3)
        self._draw_streetlamp(3*self.width/4, self.height/3)
        
        # Horse and carriage
        self._draw_carriage(random.uniform(self.width/4, 3*self.width/4), self.height/6)
    
    def _draw_london_landmark(self):
        """Draw a simplified London landmark"""
        landmark_width = self.width / 4
        landmark_height = self.height / 3
        landmark_x = (self.width - landmark_width) / 2
        landmark_y = self.height * 2/3
        
        # Main building
        Color(0.9, 0.85, 0.7, 1)  # Stone color
        Rectangle(pos=(landmark_x, landmark_y), size=(landmark_width, landmark_height))
        
        # Dome or spire
        dome_width = landmark_width / 2
        dome_height = landmark_height / 2
        dome_x = landmark_x + (landmark_width - dome_width) / 2
        dome_y = landmark_y + landmark_height
        
        # Circular dome base
        Color(0.8, 0.8, 0.8, 1)
        Ellipse(pos=(dome_x, dome_y), size=(dome_width, dome_height/2))
        
        # Dome itself
        dome_points = []
        num_points = 20
        for i in range(num_points + 1):
            angle = (i / num_points) * math.pi
            x_pos = dome_x + dome_width/2 + (dome_width/2) * math.cos(angle)
            y_pos = dome_y + dome_height/2 + (dome_height/2) * math.sin(angle)
            dome_points.extend([x_pos, y_pos])
        
        Color(0.7, 0.7, 0.7, 1)
        Line(points=dome_points, width=2)
        
        # Columns
        column_width = landmark_width / 12
        column_spacing = landmark_width / 6
        column_height = landmark_height * 0.7
        column_base_y = landmark_y + (landmark_height - column_height)
        
        Color(0.85, 0.85, 0.85, 1)
        for i in range(5):
            column_x = landmark_x + column_spacing/2 + i * column_spacing
            Rectangle(pos=(column_x, column_base_y), size=(column_width, column_height))
    
    def _draw_streetlamp(self, x, y):
        """Draw a Regency-era streetlamp"""
        post_width = self.width / 80
        post_height = self.height / 6
        
        # Lamp post
        Color(0.2, 0.2, 0.2, 1)  # Black iron
        Rectangle(pos=(x - post_width/2, y), size=(post_width, post_height))
        
        # Lamp housing
        lamp_width = post_width * 3
        lamp_height = post_height / 6
        lamp_x = x - lamp_width/2
        lamp_y = y + post_height
        
        # Frame
        Color(0.2, 0.2, 0.2, 1)
        Line(rectangle=(lamp_x, lamp_y, lamp_width, lamp_height), width=2)
        
        # Glass
        Color(0.9, 0.8, 0.3, 0.7)  # Warm light
        Rectangle(pos=(lamp_x, lamp_y), size=(lamp_width, lamp_height))
        
        # Top
        top_width = lamp_width * 1.2
        top_height = lamp_height / 2
        top_x = x - top_width/2
        top_y = lamp_y + lamp_height
        
        Color(0.2, 0.2, 0.2, 1)
        Line(points=[
            top_x, top_y,
            top_x + top_width, top_y,
            x, top_y + top_height,
            top_x, top_y
        ], width=2, close=True)
    
    def _draw_carriage(self, x, y):
        """Draw a Regency-era carriage with horses"""
        carriage_width = self.width / 10
        carriage_height = self.height / 10
        
        # Carriage body
        Color(0.3, 0.15, 0.05, 1)  # Dark wood
        Rectangle(pos=(x, y), size=(carriage_width, carriage_height))
        
        # Wheels
        wheel_radius = carriage_height / 3
        
        for wheel_x in [x + wheel_radius, x + carriage_width - wheel_radius]:
            Color(0.2, 0.2, 0.2, 1)  # Dark wheel
            Ellipse(pos=(wheel_x - wheel_radius, y - wheel_radius), 
                   size=(wheel_radius*2, wheel_radius*2))
            
            # Wheel spokes
            for angle in range(0, 360, 45):
                rad = math.radians(angle)
                Line(points=[
                    wheel_x, y,
                    wheel_x + wheel_radius * 0.8 * math.cos(rad),
                    y + wheel_radius * 0.8 * math.sin(rad)
                ], width=1)
            
            # Hub
            Color(0.6, 0.4, 0.2, 1)
            Ellipse(pos=(wheel_x - wheel_radius/4, y - wheel_radius/4), 
                   size=(wheel_radius/2, wheel_radius/2))
        
        # Horse
        horse_length = carriage_width * 0.8
        horse_height = carriage_height * 0.8
        horse_x = x - horse_length * 1.2
        horse_y = y
        
        # Horse body
        Color(0.3, 0.2, 0.1, 1)  # Brown horse
        Ellipse(pos=(horse_x, horse_y), size=(horse_length, horse_height))
        
        # Horse head
        head_size = horse_height / 2
        Color(0.35, 0.25, 0.15, 1)  # Slightly different brown
        Ellipse(pos=(horse_x - head_size, horse_y + horse_height/2), 
               size=(head_size, head_size))
        
        # Legs
        leg_width = horse_length / 10
        leg_height = horse_height / 2
        
        for leg_x in [horse_x + horse_length/4, horse_x + horse_length*3/4]:
            Rectangle(pos=(leg_x, horse_y - leg_height), size=(leg_width, leg_height))
        
        # Harness connecting to carriage
        Color(0.1, 0.1, 0.1, 1)  # Black harness
        Line(points=[
            horse_x + horse_length, horse_y + horse_height/2,
            x, y + carriage_height/2
        ], width=2)
    
    def _add_seasonal_elements(self):
        """Add elements specific to the current season"""
        if self.season == "spring":
            # Spring flowers
            for _ in range(10):
                x = random.uniform(0, self.width)
                y = random.uniform(0, self.height/3)
                
                # Flower color
                r, g, b = random.choice([
                    (1.0, 1.0, 0.0),  # Yellow
                    (1.0, 0.0, 0.0),  # Red
                    (0.7, 0.0, 1.0),  # Purple
                    (1.0, 1.0, 1.0),  # White
                    (1.0, 0.5, 0.0)   # Orange
                ])
                
                Color(r, g, b, 1)
                flower_size = random.uniform(5, 10)
                Ellipse(pos=(x, y), size=(flower_size, flower_size))
        
        elif self.season == "summer":
            # Summer elements - bright sun
            sun_size = self.width / 10
            sun_x = random.uniform(sun_size, self.width - sun_size)
            sun_y = self.height * 3/4
            
            # Sun glow
            for radius in [sun_size, sun_size*0.8, sun_size*0.6]:
                alpha = 1.0 - (radius / sun_size) * 0.5
                Color(1.0, 0.9, 0.4, alpha)
                Ellipse(pos=(sun_x - radius/2, sun_y - radius/2), size=(radius, radius))
        
        elif self.season == "autumn":
            # Falling leaves
            for _ in range(15):
                x = random.uniform(0, self.width)
                y = random.uniform(self.height/3, self.height)
                
                # Leaf color
                r, g, b = random.choice([
                    (0.8, 0.4, 0.0),  # Orange
                    (0.7, 0.2, 0.0),  # Red
                    (0.6, 0.5, 0.0),  # Yellow-brown
                    (0.5, 0.3, 0.0)   # Brown
                ])
                
                Color(r, g, b, 1)
                leaf_size = random.uniform(5, 10)
                
                # Draw a simple leaf shape
                angle = random.uniform(0, 2*math.pi)
                
                # Rotate and position
                with self.canvas.before:
                    self.canvas.push()
                    self.canvas.translate(x, y)
                    self.canvas.rotate(angle * (180/math.pi))
                    
                    # Leaf shape as oval
                    Ellipse(pos=(-leaf_size/2, -leaf_size/4), size=(leaf_size, leaf_size/2))
                    
                    # Stem
                    stem_length = leaf_size / 2
                    Line(points=[0, 0, 0, -stem_length], width=1)
                    
                    self.canvas.pop()
        
        elif self.season == "winter":
            # Snow or frost
            if self.weather == "snow":
                # Snowflakes
                for _ in range(25):
                    x = random.uniform(0, self.width)
                    y = random.uniform(self.height/3, self.height)
                    
                    Color(1.0, 1.0, 1.0, 0.8)
                    flake_size = random.uniform(2, 5)
                    Ellipse(pos=(x, y), size=(flake_size, flake_size))
                    
                # Snow accumulation on horizontal surfaces
                Color(0.95, 0.95, 0.95, 1)
                
                # Find horizontal line segments based on the scene
                if "ballroom" in self.location.lower() or "drawing room" in self.location.lower():
                    # Snow on windowsills
                    for wx in [self.width/4, self.width/2, 3*self.width/4]:
                        snow_height = random.uniform(3, 7)
                        Rectangle(pos=(wx - self.width/10, self.height/2), 
                                 size=(self.width/5, snow_height))
                else:
                    # General snow accumulation
                    snow_positions = [
                        (0, self.height/3, self.width, 5),  # Line at horizon
                        (self.width/4, self.height/2, self.width/5, 3),  # Random surfaces
                        (self.width*2/3, self.height*2/5, self.width/6, 4)
                    ]
                    
                    for x, y, w, h in snow_positions:
                        Rectangle(pos=(x, y), size=(w, h))
            else:
                # Frost effect
                for _ in range(20):
                    x = random.uniform(0, self.width)
                    y = random.uniform(0, self.height)
                    
                    Color(1.0, 1.0, 1.0, 0.3)
                    
                    # Draw frost pattern
                    points = []
                    center_x, center_y = x, y
                    radius = random.uniform(5, 20)
                    
                    for i in range(6):
                        angle = math.radians(i * 60)
                        end_x = center_x + radius * math.cos(angle)
                        end_y = center_y + radius * math.sin(angle)
                        points.extend([center_x, center_y, end_x, end_y])
                    
                    Line(points=points, width=1)
    
    def _add_weather_effects(self):
        """Add weather effects based on current weather"""
        if self.weather == "rain":
            # Rain drops
            for _ in range(100):
                x = random.uniform(0, self.width)
                y = random.uniform(self.height/3, self.height)
                
                Color(0.7, 0.7, 1.0, 0.5)
                
                # Raindrop as a line
                drop_length = random.uniform(5, 15)
                Line(points=[x, y, x - drop_length*0.2, y - drop_length], width=1)
            
            # Puddles on ground
            for _ in range(5):
                x = random.uniform(self.width/10, self.width*9/10)
                y = random.uniform(0, self.height/4)
                
                puddle_width = random.uniform(20, 50)
                puddle_height = puddle_width / 2
                
                Color(0.5, 0.5, 0.7, 0.5)
                Ellipse(pos=(x - puddle_width/2, y - puddle_height/2), 
                       size=(puddle_width, puddle_height))
            
        elif self.weather == "fog" or self.weather == "mist":
            # Fog effect
            for _ in range(5):
                fog_height = random.uniform(30, 80)
                fog_y = random.uniform(0, self.height*2/3)
                
                # Horizontal fog bank
                Color(0.9, 0.9, 0.9, 0.3)
                Rectangle(pos=(0, fog_y), size=(self.width, fog_height))
            
            # Specific fog patches
            for _ in range(10):
                x = random.uniform(0, self.width)
                y = random.uniform(0, self.height*2/3)
                
                fog_size = random.uniform(50, 150)
                Color(0.9, 0.9, 0.9, 0.2)
                Ellipse(pos=(x - fog_size/2, y - fog_size/4), 
                       size=(fog_size, fog_size/2))
                
        elif self.weather == "storm":
            # Dark clouds
            for _ in range(3):
                cloud_width = random.uniform(self.width/3, self.width/2)
                cloud_height = cloud_width / 3
                cloud_x = random.uniform(0, self.width - cloud_width)
                cloud_y = random.uniform(self.height/2, self.height*5/6)
                
                Color(0.2, 0.2, 0.3, 0.8)
                
                # Cloud as a series of overlapping circles
                num_segments = 5
                for i in range(num_segments):
                    segment_x = cloud_x + (i / (num_segments-1)) * (cloud_width - cloud_height)
                    Ellipse(pos=(segment_x, cloud_y), size=(cloud_height, cloud_height))
            
            # Lightning (50% chance)
            if random.random() > 0.5:
                lightning_start_x = random.uniform(self.width/4, self.width*3/4)
                lightning_start_y = self.height*3/4
                
                # Lightning path
                points = [lightning_start_x, lightning_start_y]
                current_x, current_y = lightning_start_x, lightning_start_y
                
                segments = random.randint(3, 6)
                for _ in range(segments):
                    # Each segment has a random offset
                    current_y -= random.uniform(20, 40)
                    current_x += random.uniform(-30, 30)
                    points.extend([current_x, current_y])
                    
                    if current_y < self.height/3:
                        break
                
                Color(1.0, 1.0, 0.6, 0.8)
                Line(points=points, width=2)
                
                # Lightning glow
                Color(1.0, 1.0, 0.6, 0.3)
                Line(points=points, width=6)
            
            # Rain
            for _ in range(70):
                x = random.uniform(0, self.width)
                y = random.uniform(self.height/3, self.height)
                
                Color(0.7, 0.7, 0.8, 0.6)
                
                # Raindrop as a line
                drop_length = random.uniform(7, 20)
                Line(points=[x, y, x - drop_length*0.3, y - drop_length], width=1)
    
    def _add_decorative_frame(self):
        """Add a decorative frame around the scene illustration"""
        frame_width = 10
        
        # Outer frame
        Color(*REGENCY_COLORS['gold'])
        Line(rectangle=(frame_width/2, frame_width/2, 
                       self.width - frame_width, self.height - frame_width), width=frame_width)
        
        # Corner ornaments
        corner_size = 20
        for x, y in [
            (frame_width, frame_width),  # Bottom left
            (self.width - frame_width - corner_size, frame_width),  # Bottom right
            (frame_width, self.height - frame_width - corner_size),  # Top left
            (self.width - frame_width - corner_size, self.height - frame_width - corner_size)  # Top right
        ]:
            # Decorative corner element
            Color(*REGENCY_COLORS['burgundy'])
            Line(circle=(x + corner_size/2, y + corner_size/2, corner_size/2), width=2)
            
            Color(*REGENCY_COLORS['gold'])
            Line(circle=(x + corner_size/2, y + corner_size/2, corner_size/4), width=1)


class StoryTimeline(Widget):
    """
    Creates a visual timeline of story events using Kivy and Matplotlib
    """
    events = ListProperty([])
    
    def __init__(self, **kwargs):
        super(StoryTimeline, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (800, 400)
        self.events = kwargs.get('events', [])
        self.title = kwargs.get('title', 'Story Timeline')
        
        Clock.schedule_once(self._create_timeline, 0.1)
    
    def _create_timeline(self, dt):
        """Create the timeline visualization using matplotlib"""
        # Create a matplotlib figure
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Plot setup
        ax.set_title(self.title, fontsize=14, color='#333333')
        ax.set_xlabel('Time', fontsize=12)
        ax.set_yticks([])  # Hide y-axis ticks
        
        # Set event positions
        num_events = len(self.events)
        event_positions = list(range(num_events))
        
        # Plot event points
        ax.scatter(event_positions, [0] * num_events, s=100, 
                 color='#aa3333', zorder=5)
        
        # Add timeline
        ax.plot([0, num_events - 1], [0, 0], 'k-', linewidth=2)
        
        # Add event labels
        for i, event in enumerate(self.events):
            ax.annotate(event, 
                      xy=(i, 0), 
                      xytext=(0, 10 if i % 2 == 0 else -30),
                      textcoords='offset points',
                      ha='center',
                      va='bottom' if i % 2 == 0 else 'top',
                      fontsize=10,
                      color='#333333',
                      bbox=dict(boxstyle="round,pad=0.3", fc='#f0f0f0', ec='#cccccc'))
        
        # Remove spines
        for spine in ax.spines.values():
            spine.set_visible(False)
        
        # Hide axes
        ax.set_yticks([])
        ax.set_xticks([])
        
        # Create canvas
        canvas = FigureCanvasKivyAgg(fig)
        
        # Add to layout
        self.clear_widgets()
        self.add_widget(canvas)


class ThematicQuoteDisplay(BoxLayout):
    """
    Creates a visually engaging display for Jane Austen quotes with animations
    """
    quote_text = StringProperty("")
    source_text = StringProperty("")
    context_text = StringProperty("")
    display_style = StringProperty("themed")  # "standard", "themed", or "animated"
    theme = StringProperty("general")
    
    def __init__(self, **kwargs):
        super(ThematicQuoteDisplay, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 20, 30, 20]
        self.spacing = 15
        self.size_hint = (None, None)
        self.size = (600, 400)
        
        # Extract attributes from kwargs
        self.quote_text = kwargs.get('quote_text', self.quote_text)
        self.source_text = kwargs.get('source_text', self.source_text)
        self.context_text = kwargs.get('context_text', self.context_text)
        self.display_style = kwargs.get('display_style', self.display_style)
        self.theme = kwargs.get('theme', self.theme).lower()
        
        # Choose appropriate theme colors based on quote theme
        self._set_theme_colors()
        
        # Generate the quote display
        Clock.schedule_once(self._create_quote_display, 0.1)
    
    def _set_theme_colors(self):
        """Set colors based on quote theme"""
        theme_colors = {
            'love': {
                'primary': (0.8, 0.1, 0.2, 1),  # Deep red
                'secondary': (0.9, 0.7, 0.8, 1),  # Light pink
                'accent': (0.7, 0.0, 0.0, 1)  # Dark red
            },
            'marriage': {
                'primary': (0.6, 0.1, 0.6, 1),  # Purple
                'secondary': (0.9, 0.8, 0.9, 1),  # Light purple
                'accent': (0.4, 0.0, 0.4, 1)  # Dark purple
            },
            'pride': {
                'primary': (0.1, 0.2, 0.5, 1),  # Navy blue
                'secondary': (0.7, 0.8, 0.9, 1),  # Light blue
                'accent': (0.0, 0.1, 0.3, 1)  # Dark blue
            },
            'prejudice': {
                'primary': (0.5, 0.3, 0.0, 1),  # Brown
                'secondary': (0.8, 0.7, 0.5, 1),  # Tan
                'accent': (0.3, 0.2, 0.0, 1)  # Dark brown
            },
            'society': {
                'primary': (0.2, 0.5, 0.3, 1),  # Green
                'secondary': (0.7, 0.9, 0.7, 1),  # Light green
                'accent': (0.1, 0.3, 0.1, 1)  # Dark green
            },
            'wealth': {
                'primary': (0.8, 0.7, 0.1, 1),  # Gold
                'secondary': (0.9, 0.9, 0.7, 1),  # Light gold
                'accent': (0.6, 0.5, 0.0, 1)  # Dark gold
            },
            'happiness': {
                'primary': (1.0, 0.7, 0.0, 1),  # Orange
                'secondary': (1.0, 0.9, 0.7, 1),  # Light orange
                'accent': (0.7, 0.4, 0.0, 1)  # Dark orange
            },
            'wit': {
                'primary': (0.0, 0.6, 0.6, 1),  # Teal
                'secondary': (0.7, 0.9, 0.9, 1),  # Light teal
                'accent': (0.0, 0.4, 0.4, 1)  # Dark teal
            }
        }
        
        # Get colors for this theme, or use general colors if theme not found
        self.theme_colors = theme_colors.get(self.theme, {
            'primary': REGENCY_COLORS['burgundy'],
            'secondary': REGENCY_COLORS['cream'],
            'accent': REGENCY_COLORS['navy']
        })
    
    def _create_quote_display(self, dt):
        """Create the quote display based on selected style"""
        # Clear any existing widgets
        self.clear_widgets()
        
        # Background color based on style
        if self.display_style == "themed":
            self.canvas.before.clear()
            with self.canvas.before:
                Color(*self.theme_colors['secondary'])
                Rectangle(pos=self.pos, size=self.size)
        
        # Create layout based on display style
        if self.display_style == "animated":
            self._create_animated_display()
        elif self.display_style == "themed":
            self._create_themed_display()
        else:  # standard
            self._create_standard_display()
    
    def _create_standard_display(self):
        """Create a standard quote display with simple frame"""
        # Header
        header_label = Label(
            text="A Quote from Jane Austen",
            font_size=22,
            size_hint_y=None,
            height=40,
            color=(0.1, 0.1, 0.1, 1)
        )
        self.add_widget(header_label)
        
        # Decorative separator
        separator = Widget(size_hint_y=None, height=20)
        with separator.canvas:
            Color(0.2, 0.2, 0.2, 1)
            Line(points=[self.width*0.3, 10, self.width*0.7, 10], width=1)
        self.add_widget(separator)
        
        # Quote text
        quote_label = Label(
            text=f'"{self.quote_text}"',
            font_size=20,
            italic=True,
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=120,
            text_size=(self.width - 60, None),
            halign='center'
        )
        self.add_widget(quote_label)
        
        # Source
        if self.source_text:
            source_label = Label(
                text=f"— {self.source_text}",
                font_size=16,
                italic=True,
                color=(0.4, 0.4, 0.4, 1),
                size_hint_y=None,
                height=30,
                halign='right'
            )
            self.add_widget(source_label)
        
        # Context information
        if self.context_text:
            context_label = Label(
                text=self.context_text,
                font_size=14,
                color=(0.3, 0.3, 0.3, 1),
                size_hint_y=None,
                height=120,
                text_size=(self.width - 60, None),
                halign='center'
            )
            self.add_widget(context_label)
    
    def _create_themed_display(self):
        """Create a themed quote display with ornate frame"""
        # Ornate frame
        frame = Widget(size_hint=(1, 1))
        with frame.canvas:
            # Frame background
            Color(*self.theme_colors['secondary'])
            Rectangle(pos=(10, 10), size=(self.width - 20, self.height - 20))
            
            # Frame border
            Color(*self.theme_colors['primary'])
            Line(rectangle=(15, 15, self.width - 30, self.height - 30), width=2)
            
            # Decorative corners
            corner_size = 30
            
            # Top left corner
            Line(bezier=[
                20, self.height - 20,  # Start
                20, self.height - 20 - corner_size/2,  # Control 1
                20 + corner_size/2, self.height - 20,  # Control 2
                20 + corner_size, self.height - 20 - corner_size  # End
            ], width=2)
            
            # Top right corner
            Line(bezier=[
                self.width - 20, self.height - 20,  # Start
                self.width - 20, self.height - 20 - corner_size/2,  # Control 1
                self.width - 20 - corner_size/2, self.height - 20,  # Control 2
                self.width - 20 - corner_size, self.height - 20 - corner_size  # End
            ], width=2)
            
            # Bottom left corner
            Line(bezier=[
                20, 20,  # Start
                20, 20 + corner_size/2,  # Control 1
                20 + corner_size/2, 20,  # Control 2
                20 + corner_size, 20 + corner_size  # End
            ], width=2)
            
            # Bottom right corner
            Line(bezier=[
                self.width - 20, 20,  # Start
                self.width - 20, 20 + corner_size/2,  # Control 1
                self.width - 20 - corner_size/2, 20,  # Control 2
                self.width - 20 - corner_size, 20 + corner_size  # End
            ], width=2)
            
            # Decorative flourishes based on theme
            self._add_theme_flourishes(frame.canvas)
        
        self.add_widget(frame)
        
        # Quote content
        content_layout = BoxLayout(orientation='vertical', padding=[40, 40, 40, 40])
        
        # Quote text
        quote_label = Label(
            text=f'"{self.quote_text}"',
            font_size=20,
            italic=True,
            color=self.theme_colors['accent'],
            size_hint_y=None,
            height=120,
            text_size=(self.width - 100, None),
            halign='center'
        )
        content_layout.add_widget(quote_label)
        
        # Source
        if self.source_text:
            source_label = Label(
                text=f"— {self.source_text}",
                font_size=16,
                italic=True,
                color=self.theme_colors['primary'],
                size_hint_y=None,
                height=30,
                halign='right'
            )
            content_layout.add_widget(source_label)
        
        # Context information
        if self.context_text:
            context_label = Label(
                text=self.context_text,
                font_size=14,
                color=(0.3, 0.3, 0.3, 1),
                size_hint_y=None,
                height=120,
                text_size=(self.width - 100, None),
                halign='center'
            )
            content_layout.add_widget(context_label)
        
        self.add_widget(content_layout)
    
    def _add_theme_flourishes(self, canvas):
        """Add theme-specific decorative elements to the frame"""
        # Base motifs dictionary for themes
        theme_motifs = {
            'love': self._draw_heart_motifs,
            'marriage': self._draw_ring_motifs,
            'pride': self._draw_crown_motifs,
            'prejudice': self._draw_mask_motifs,
            'society': self._draw_column_motifs,
            'wealth': self._draw_coin_motifs,
            'happiness': self._draw_flora_motifs,
            'wit': self._draw_quill_motifs
        }
        
        # Get the appropriate drawing function for this theme
        draw_func = theme_motifs.get(self.theme, self._draw_scroll_motifs)
        
        # Execute the drawing function
        with canvas:
            Color(*self.theme_colors['primary'])
            draw_func()
    
    def _draw_heart_motifs(self):
        """Draw heart motifs for love theme"""
        # Four hearts at corners
        for x, y in [
            (40, 40),  # Bottom left
            (self.width - 40, 40),  # Bottom right
            (40, self.height - 40),  # Top left
            (self.width - 40, self.height - 40)  # Top right
        ]:
            # Heart shape
            heart_size = 20
            
            # Create bezier curves for heart shape
            bezier_points = [
                x, y - heart_size/2,  # Bottom point
                x - heart_size/2, y,  # Left control
                x - heart_size, y + heart_size,  # Left top
                x, y + heart_size/2,  # Top middle
                x + heart_size, y + heart_size,  # Right top
                x + heart_size/2, y,  # Right control
                x, y - heart_size/2  # Back to bottom
            ]
            
            Line(bezier=bezier_points, width=1.5)
    
    def _draw_ring_motifs(self):
        """Draw ring motifs for marriage theme"""
        # Four rings at corners
        for x, y in [
            (40, 40),  # Bottom left
            (self.width - 40, 40),  # Bottom right
            (40, self.height - 40),  # Top left
            (self.width - 40, self.height - 40)  # Top right
        ]:
            # Outer ring
            ring_radius = 15
            Line(circle=(x, y, ring_radius), width=2)
            
            # Inner ring
            Line(circle=(x, y, ring_radius*0.7), width=1)
    
    def _draw_crown_motifs(self):
        """Draw crown motifs for pride theme"""
        # Crown at top center
        crown_width = 100
        crown_height = 50
        crown_x = self.width / 2 - crown_width / 2
        crown_y = self.height - 70
        
        # Base of crown
        Line(points=[
            crown_x, crown_y,
            crown_x + crown_width, crown_y
        ], width=2)
        
        # Crown points
        points = []
        num_points = 5
        for i in range(num_points):
            point_x = crown_x + (i / (num_points-1)) * crown_width
            if i % 2 == 0:  # Tall points
                point_y = crown_y + crown_height
            else:  # Short points
                point_y = crown_y + crown_height * 0.6
            
            points.extend([point_x, point_y])
        
        # Connect crown points
        for i in range(len(points) // 2 - 1):
            Line(points=[
                points[i*2], points[i*2 + 1],
                points[(i+1)*2], points[(i+1)*2 + 1]
            ], width=2)
        
        # Connect points to base
        for i in range(len(points) // 2):
            Line(points=[
                points[i*2], points[i*2 + 1],
                points[i*2], crown_y
            ], width=2)
    
    def _draw_mask_motifs(self):
        """Draw mask motifs for prejudice theme"""
        # Mask at top center
        mask_width = 80
        mask_height = 40
        mask_x = self.width / 2 - mask_width / 2
        mask_y = self.height - 70
        
        # Mask outline
        Line(ellipse=(mask_x, mask_y, mask_width, mask_height), width=2)
        
        # Eye holes
        eye_width = mask_width / 4
        eye_height = mask_height / 2
        eye_y = mask_y + mask_height / 4
        
        # Left eye
        left_eye_x = mask_x + mask_width / 4 - eye_width / 2
        Line(ellipse=(left_eye_x, eye_y, eye_width, eye_height), width=1.5)
        
        # Right eye
        right_eye_x = mask_x + mask_width * 3/4 - eye_width / 2
        Line(ellipse=(right_eye_x, eye_y, eye_width, eye_height), width=1.5)
    
    def _draw_column_motifs(self):
        """Draw column motifs for society theme"""
        # Columns on sides
        column_width = 20
        column_height = self.height * 0.6
        
        for x in [40, self.width - 40 - column_width]:
            column_y = (self.height - column_height) / 2
            
            # Column base
            base_height = column_height * 0.1
            base_width = column_width * 1.3
            base_x = x - (base_width - column_width) / 2
            
            Line(rectangle=(base_x, column_y, base_width, base_height), width=1.5)
            
            # Column shaft
            Line(rectangle=(x, column_y + base_height, column_width, column_height * 0.8), width=1.5)
            
            # Column capital
            capital_height = column_height * 0.1
            capital_width = column_width * 1.3
            capital_x = x - (capital_width - column_width) / 2
            capital_y = column_y + base_height + column_height * 0.8
            
            Line(rectangle=(capital_x, capital_y, capital_width, capital_height), width=1.5)
    
    def _draw_coin_motifs(self):
        """Draw coin motifs for wealth theme"""
        # Coins in corners
        for x, y in [
            (40, 40),  # Bottom left
            (self.width - 40, 40),  # Bottom right
            (40, self.height - 40),  # Top left
            (self.width - 40, self.height - 40)  # Top right
        ]:
            # Coin outline
            coin_radius = 20
            Line(circle=(x, y, coin_radius), width=2)
            
            # Inner circle
            Line(circle=(x, y, coin_radius * 0.7), width=1)
            
            # Decorative elements inside coin
            # Crossed lines
            Line(points=[x - coin_radius*0.5, y - coin_radius*0.5, 
                         x + coin_radius*0.5, y + coin_radius*0.5], width=1)
            Line(points=[x - coin_radius*0.5, y + coin_radius*0.5, 
                         x + coin_radius*0.5, y - coin_radius*0.5], width=1)
    
    def _draw_flora_motifs(self):
        """Draw floral motifs for happiness theme"""
        # Flowers in corners
        for x, y in [
            (40, 40),  # Bottom left
            (self.width - 40, 40),  # Bottom right
            (40, self.height - 40),  # Top left
            (self.width - 40, self.height - 40)  # Top right
        ]:
            # Flower with petals
            flower_radius = 15
            num_petals = 6
            
            for i in range(num_petals):
                angle = (i / num_petals) * 2 * math.pi
                petal_x = x + flower_radius * math.cos(angle)
                petal_y = y + flower_radius * math.sin(angle)
                
                # Draw petal
                Ellipse(pos=(petal_x - flower_radius/2, petal_y - flower_radius/2), 
                       size=(flower_radius, flower_radius))
            
            # Flower center
            Color(*self.theme_colors['accent'])
            Ellipse(pos=(x - flower_radius/3, y - flower_radius/3), 
                   size=(flower_radius*2/3, flower_radius*2/3))
            
            # Return to primary color
            Color(*self.theme_colors['primary'])
    
    def _draw_quill_motifs(self):
        """Draw quill motifs for wit theme"""
        # Quill in corner
        quill_length = 60
        quill_x = 40
        quill_y = 40
        
        # Quill shaft
        Line(points=[quill_x, quill_y, quill_x + quill_length*0.7, quill_y + quill_length], width=2)
        
        # Quill feather details
        feather_width = quill_length * 0.3
        num_feathers = 8
        
        for i in range(num_feathers):
            t = i / (num_feathers - 1)
            # Point on shaft
            point_x = quill_x + t * quill_length*0.7
            point_y = quill_y + t * quill_length
            
            # Feather angle varies along shaft
            angle = math.pi/4 + t * math.pi/4
            
            # Feather length varies - shorter at tip
            feather_length = feather_width * (1 - t*0.5)
            
            # Feather end point
            end_x = point_x - feather_length * math.cos(angle)
            end_y = point_y + feather_length * math.sin(angle)
            
            Line(points=[point_x, point_y, end_x, end_y], width=1)
    
    def _draw_scroll_motifs(self):
        """Draw scroll motifs for general theme"""
        # Scrolls in corners
        for x, y in [
            (40, 40),  # Bottom left
            (self.width - 40, 40),  # Bottom right
            (40, self.height - 40),  # Top left
            (self.width - 40, self.height - 40)  # Top right
        ]:
            # Scroll shape
            scroll_width = 30
            scroll_height = 20
            
            # First curl
            Line(bezier=[
                x, y,
                x, y + scroll_height,
                x + scroll_width/2, y + scroll_height,
                x + scroll_width/2, y
            ], width=1.5)
            
            # Second curl
            Line(bezier=[
                x + scroll_width/2, y,
                x + scroll_width/2, y + scroll_height,
                x + scroll_width, y + scroll_height,
                x + scroll_width, y
            ], width=1.5)
    
    def _create_animated_display(self):
        """Create an animated quote display with character-by-character effect"""
        # Create the animated quote box
        quote_box = AnimatedQuoteBox(
            quote_text=self.quote_text,
            source_text=self.source_text,
            context_text=self.context_text,
            bg_color=REGENCY_COLORS['cream']
        )
        self.add_widget(quote_box)
        
        # Start the animation
        Clock.schedule_once(lambda dt: quote_box.quote_label.start_animation(), 0.5)


class KivyVisualImageryApp(App):
    """Main app for testing Kivy visual imagery components"""
    
    def build(self):
        """Build the test application"""
        # Create a scrollable layout
        main_layout = ScrollView(size_hint=(1, 1))
        
        # Container for all visual examples
        examples_layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=20,
            size_hint_y=None
        )
        examples_layout.bind(minimum_height=examples_layout.setter('height'))
        
        # Header
        header_label = Label(
            text="Jane Austen Storyteller - Visual Imagery Examples",
            font_size=24,
            size_hint_y=None,
            height=60
        )
        examples_layout.add_widget(header_label)
        
        # Character Portrait example
        portrait_label = Label(
            text="Character Portrait Example:",
            font_size=18,
            size_hint_y=None,
            height=40,
            halign='left'
        )
        examples_layout.add_widget(portrait_label)
        
        # Character examples
        character_row = BoxLayout(
            spacing=20,
            size_hint_y=None,
            height=450
        )
        
        # Female character
        female_character = CharacterPortrait(
            name="Elizabeth Bennet",
            gender="female",
            social_class="middle",
            occupation="Gentleman's daughter",
            personality="Intelligent, witty, playful"
        )
        character_row.add_widget(female_character)
        
        # Male character
        male_character = CharacterPortrait(
            name="Mr. Darcy",
            gender="male",
            social_class="upper",
            occupation="Gentleman of large fortune",
            personality="Reserved, proud, honorable"
        )
        character_row.add_widget(male_character)
        
        examples_layout.add_widget(character_row)
        
        # Scene Illustration example
        scene_label = Label(
            text="Scene Illustration Examples:",
            font_size=18,
            size_hint_y=None,
            height=40,
            halign='left'
        )
        examples_layout.add_widget(scene_label)
        
        # Scene examples
        scene_row = BoxLayout(
            spacing=20,
            size_hint_y=None,
            height=450
        )
        
        # Drawing room scene
        drawing_room = SceneIllustration(
            location="drawing room",
            season="winter",
            time_of_day="evening"
        )
        scene_row.add_widget(drawing_room)
        
        # Garden scene
        garden = SceneIllustration(
            location="garden",
            season="spring",
            time_of_day="day"
        )
        scene_row.add_widget(garden)
        
        examples_layout.add_widget(scene_row)
        
        # Quote Display example
        quote_label = Label(
            text="Thematic Quote Display Examples:",
            font_size=18,
            size_hint_y=None,
            height=40,
            halign='left'
        )
        examples_layout.add_widget(quote_label)
        
        # Quote examples
        quote_row = BoxLayout(
            spacing=20,
            size_hint_y=None,
            height=450
        )
        
        # Standard quote
        standard_quote = ThematicQuoteDisplay(
            quote_text="It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
            source_text="Pride and Prejudice",
            context_text="The famous opening line that sets the theme for the entire novel.",
            display_style="standard"
        )
        quote_row.add_widget(standard_quote)
        
        # Themed quote
        themed_quote = ThematicQuoteDisplay(
            quote_text="I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book!",
            source_text="Pride and Prejudice",
            context_text="Spoken by Caroline Bingley, though ironically she has little interest in reading.",
            display_style="themed",
            theme="wit"
        )
        quote_row.add_widget(themed_quote)
        
        examples_layout.add_widget(quote_row)
        
        # Timeline example
        timeline_label = Label(
            text="Story Timeline Example:",
            font_size=18,
            size_hint_y=None,
            height=40,
            halign='left'
        )
        examples_layout.add_widget(timeline_label)
        
        # Example timeline
        timeline = StoryTimeline(
            events=[
                "First meeting at Netherfield",
                "Darcy's first proposal",
                "Letter of explanation",
                "Meeting at Pemberley",
                "Lydia's elopement",
                "Darcy's intervention",
                "Bingley's return",
                "Lady Catherine's visit",
                "Second proposal"
            ],
            title="Pride and Prejudice Timeline"
        )
        examples_layout.add_widget(timeline)
        
        # Add everything to the scroll view
        main_layout.add_widget(examples_layout)
        
        return main_layout


# Main function to run standalone tests
def main():
    """Run the Kivy Visual Imagery example app"""
    # Set window size
    Window.size = (900, 700)
    Window.clearcolor = (0.97, 0.95, 0.9, 1)  # Parchment-like background
    
    # Run the app
    KivyVisualImageryApp().run()


if __name__ == "__main__":
    main()