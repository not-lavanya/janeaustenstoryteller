"""
Visual Imagery Implementation Using Kivy for Jane Austen Storytelling Experience
Provides enhanced visual elements for storytelling, including:
- Character portraits
- Location illustrations
- Seasonal imagery
- Ornamental frames for quotes and letters
- Decorative story headers
- Animated text transitions
"""

import os
import random
import math
from functools import partial
import threading
import time

# Kivy imports
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.graphics.instructions import InstructionGroup
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

# Set window size for development
Window.size = (800, 600)

# Custom color palette for Regency era aesthetics
REGENCY_COLORS = {
    "parchment": "#F5F2E9",
    "ink": "#2D2926",
    "sepia": "#704214",
    "azure": "#007BA7",
    "forest": "#1B4D3E",
    "burgundy": "#8C1C13",
    "gold": "#D4AF37",
    "cream": "#FFF8E7",
    "lavender": "#E6E6FA",
    "sage": "#BCB88A",
    "rose": "#C08081",
    "navy": "#000080",
}

# Theme-specific color schemes
THEME_COLORS = {
    "love": {"primary": "#C08081", "secondary": "#E6E6FA", "accent": "#D4AF37"},
    "marriage": {"primary": "#007BA7", "secondary": "#FFF8E7", "accent": "#D4AF37"},
    "social_class": {"primary": "#8C1C13", "secondary": "#F5F2E9", "accent": "#1B4D3E"},
    "family": {"primary": "#1B4D3E", "secondary": "#BCB88A", "accent": "#704214"},
    "self_discovery": {"primary": "#000080", "secondary": "#E6E6FA", "accent": "#C08081"},
    "reputation": {"primary": "#704214", "secondary": "#F5F2E9", "accent": "#8C1C13"},
    "prejudice": {"primary": "#2D2926", "secondary": "#FFF8E7", "accent": "#007BA7"},
    "wealth": {"primary": "#D4AF37", "secondary": "#000080", "accent": "#F5F2E9"},
}

# Season-specific color schemes
SEASON_COLORS = {
    "spring": {"primary": "#BCB88A", "secondary": "#E6E6FA", "accent": "#C08081"},
    "summer": {"primary": "#007BA7", "secondary": "#FFF8E7", "accent": "#D4AF37"},
    "autumn": {"primary": "#704214", "secondary": "#F5F2E9", "accent": "#8C1C13"},
    "winter": {"primary": "#000080", "secondary": "#F5F2E9", "accent": "#007BA7"},
}


class CharacterPortraitWidget(Widget):
    """Widget for rendering Regency-era character portraits"""
    
    character_name = StringProperty("")
    character_gender = StringProperty("female")
    character_class = StringProperty("upper")
    character_age = NumericProperty(25)
    
    def __init__(self, **kwargs):
        super(CharacterPortraitWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 400)
        
        # Schedule the drawing after the widget is fully initialized
        Clock.schedule_once(self._draw_portrait, 0)
        
    def _draw_portrait(self, dt):
        """Draw the character portrait"""
        self.canvas.clear()
        
        # Background frame
        with self.canvas:
            # Oval frame with regency styling
            Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
            frame_border = 10
            Rectangle(pos=(frame_border, frame_border), 
                      size=(self.width - 2*frame_border, self.height - 2*frame_border))
            
            # Inner oval frame
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            inner_border = 20
            Ellipse(pos=(inner_border, inner_border), 
                   size=(self.width - 2*inner_border, self.height - 2*inner_border))
            
            # Draw the silhouette based on gender
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            
            # Head position
            head_size = min(self.width, self.height) * 0.3
            head_x = self.center_x - head_size/2
            head_y = self.center_y + head_size * 0.5
            
            # Draw head
            Ellipse(pos=(head_x, head_y), size=(head_size, head_size))
            
            # Draw body based on gender and class
            if self.character_gender.lower() == "female":
                self._draw_female_silhouette(head_x, head_y, head_size)
            else:
                self._draw_male_silhouette(head_x, head_y, head_size)
            
            # Add decorative elements based on class
            self._add_class_elements(head_x, head_y, head_size)
            
            # Add age-appropriate details
            self._add_age_elements(head_x, head_y, head_size)
            
            # Add name caption
            self._add_name_caption()
    
    def _draw_female_silhouette(self, head_x, head_y, head_size):
        """Draw a female silhouette"""
        with self.canvas:
            # Neck
            Rectangle(
                pos=(head_x + head_size/3, head_y - head_size * 0.2),
                size=(head_size/3, head_size * 0.3)
            )
            
            # Shoulders and dress
            shoulder_width = head_size * 1.5
            dress_top_y = head_y - head_size * 0.1
            
            # Upper dress (bodice)
            points = [
                head_x + head_size/2 - shoulder_width/2, dress_top_y,  # left shoulder
                head_x + head_size/2 + shoulder_width/2, dress_top_y,  # right shoulder
                head_x + head_size/2 + shoulder_width/2.5, dress_top_y - head_size * 1.5,  # right bottom
                head_x + head_size/2 - shoulder_width/2.5, dress_top_y - head_size * 1.5  # left bottom
            ]
            
            Color(*get_color_from_hex(REGENCY_COLORS["burgundy"] 
                                      if self.character_class == "upper" 
                                      else REGENCY_COLORS["sage"]))
            Line(points=points, width=2, close=True)
            
            # Draw the Regency high-waisted dress
            if self.character_class == "upper":
                # Full skirt for upper class
                skirt_points = [
                    points[4], points[5],  # left bottom of bodice
                    points[6], points[7],  # right bottom of bodice
                    head_x + head_size/2 + shoulder_width/1.5, self.y + head_size * 0.5,  # right bottom
                    head_x + head_size/2 - shoulder_width/1.5, self.y + head_size * 0.5   # left bottom
                ]
                Line(points=skirt_points, width=2, close=True)
            else:
                # Simpler skirt for lower/middle class
                skirt_points = [
                    points[4], points[5],  # left bottom of bodice
                    points[6], points[7],  # right bottom of bodice
                    head_x + head_size/2 + shoulder_width/2, self.y + head_size * 0.7,  # right bottom
                    head_x + head_size/2 - shoulder_width/2, self.y + head_size * 0.7   # left bottom
                ]
                Line(points=skirt_points, width=2, close=True)
    
    def _draw_male_silhouette(self, head_x, head_y, head_size):
        """Draw a male silhouette"""
        with self.canvas:
            # Neck
            Rectangle(
                pos=(head_x + head_size/3, head_y - head_size * 0.2),
                size=(head_size/3, head_size * 0.2)
            )
            
            # Shoulders and coat
            shoulder_width = head_size * 1.8
            coat_top_y = head_y - head_size * 0.2
            
            # Upper coat
            points = [
                head_x + head_size/2 - shoulder_width/2, coat_top_y,  # left shoulder
                head_x + head_size/2 + shoulder_width/2, coat_top_y,  # right shoulder
                head_x + head_size/2 + shoulder_width/2, coat_top_y - head_size * 1.6,  # right bottom
                head_x + head_size/2 - shoulder_width/2, coat_top_y - head_size * 1.6   # left bottom
            ]
            
            # Choose coat color based on class
            if self.character_class == "upper":
                Color(*get_color_from_hex(REGENCY_COLORS["navy"]))
            elif self.character_class == "middle":
                Color(*get_color_from_hex(REGENCY_COLORS["forest"]))
            else:
                Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
                
            Line(points=points, width=2, close=True)
            
            # Add waistcoat
            waistcoat_width = shoulder_width * 0.6
            waistcoat_points = [
                head_x + head_size/2 - waistcoat_width/2, coat_top_y - head_size * 0.3,
                head_x + head_size/2 + waistcoat_width/2, coat_top_y - head_size * 0.3,
                head_x + head_size/2 + waistcoat_width/2, coat_top_y - head_size * 1.2,
                head_x + head_size/2 - waistcoat_width/2, coat_top_y - head_size * 1.2
            ]
            
            # Waistcoat in a contrasting color
            Color(*get_color_from_hex(REGENCY_COLORS["cream"] 
                                      if self.character_class == "upper" 
                                      else REGENCY_COLORS["parchment"]))
            Line(points=waistcoat_points, width=1.5, close=True)
            
            # Add trousers or breeches
            if self.character_class == "upper":
                # Breeches for upper class
                leg_points = [
                    points[4], points[5],  # left bottom of coat
                    points[6], points[7],  # right bottom of coat
                    head_x + head_size/2 + shoulder_width/3, self.y + head_size * 0.8,  # right knee
                    head_x + head_size/2 - shoulder_width/3, self.y + head_size * 0.8   # left knee
                ]
                Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
                Line(points=leg_points, width=2, close=True)
            else:
                # Trousers for lower/middle class
                leg_points = [
                    points[4], points[5],  # left bottom of coat
                    points[6], points[7],  # right bottom of coat
                    head_x + head_size/2 + shoulder_width/3, self.y + head_size * 0.5,  # right bottom
                    head_x + head_size/2 - shoulder_width/3, self.y + head_size * 0.5   # left bottom
                ]
                Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
                Line(points=leg_points, width=2, close=True)
    
    def _add_class_elements(self, head_x, head_y, head_size):
        """Add class-specific decorative elements"""
        with self.canvas:
            if self.character_class == "upper":
                # Upper class elements
                if self.character_gender.lower() == "female":
                    # Add decorative hair arrangement with jewels
                    Color(*get_color_from_hex(REGENCY_COLORS["gold"]))
                    for i in range(5):
                        Ellipse(
                            pos=(head_x + head_size/4 + i*head_size/10, head_y + head_size*0.8),
                            size=(head_size/20, head_size/20)
                        )
                else:
                    # Add cravat for upper class men
                    Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
                    Rectangle(
                        pos=(head_x + head_size/3, head_y - head_size * 0.1),
                        size=(head_size/3, head_size * 0.1)
                    )
            elif self.character_class == "middle":
                # Middle class elements
                if self.character_gender.lower() == "female":
                    # Add simpler hair arrangement
                    Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
                    Line(
                        circle=(head_x + head_size/2, head_y + head_size*0.7, head_size/10),
                        width=1.5
                    )
                else:
                    # Add simpler neckwear for middle class men
                    Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
                    Rectangle(
                        pos=(head_x + head_size/3, head_y - head_size * 0.1),
                        size=(head_size/3, head_size * 0.08)
                    )
            else:
                # Lower class elements
                pass  # Simpler silhouette for lower class
    
    def _add_age_elements(self, head_x, head_y, head_size):
        """Add age-appropriate details to the portrait"""
        with self.canvas:
            if self.character_age > 50:
                # Add wrinkles or age lines for older characters
                Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
                Line(
                    points=[
                        head_x + head_size/3, head_y + head_size/2,
                        head_x + head_size/4, head_y + head_size/2 - head_size/20
                    ],
                    width=1
                )
                Line(
                    points=[
                        head_x + 2*head_size/3, head_y + head_size/2,
                        head_x + 3*head_size/4, head_y + head_size/2 - head_size/20
                    ],
                    width=1
                )
            elif self.character_age < 20:
                # Younger appearance
                pass  # Simplified features for youth
    
    def _add_name_caption(self):
        """Add the character name as a caption"""
        with self.canvas:
            # Add a decorative name plate
            plate_height = 40
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            Rectangle(
                pos=(20, 20),
                size=(self.width - 40, plate_height)
            )
            
            # Add border for name plate
            Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
            Line(
                rectangle=(20, 20, self.width - 40, plate_height),
                width=2
            )


class LocationIllustrationWidget(Widget):
    """Widget for rendering Regency-era location illustrations"""
    
    location_type = StringProperty("estate")  # estate, cottage, park, ballroom, etc.
    season = StringProperty("spring")
    time_of_day = StringProperty("day")  # day, evening, night
    
    def __init__(self, **kwargs):
        super(LocationIllustrationWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (400, 300)
        
        # Schedule the drawing after the widget is fully initialized
        Clock.schedule_once(self._draw_location, 0)
    
    def _draw_location(self, dt):
        """Draw the location illustration"""
        self.canvas.clear()
        
        # Background based on time of day
        with self.canvas:
            if self.time_of_day == "day":
                # Day sky
                Color(*get_color_from_hex("#87CEEB"))  # Light blue
            elif self.time_of_day == "evening":
                # Evening sky
                Color(*get_color_from_hex("#FF7F50"))  # Coral sunset
            else:  # night
                # Night sky
                Color(*get_color_from_hex("#191970"))  # Midnight blue
            
            Rectangle(pos=(0, 0), size=self.size)
            
            # Draw location based on type
            if self.location_type == "estate":
                self._draw_estate()
            elif self.location_type == "cottage":
                self._draw_cottage()
            elif self.location_type == "park":
                self._draw_park()
            elif self.location_type == "ballroom":
                self._draw_ballroom()
            else:
                self._draw_generic_landscape()
            
            # Add seasonal elements
            self._add_seasonal_elements()
            
            # Add decorative frame
            self._add_decorative_frame()
    
    def _draw_estate(self):
        """Draw a Regency estate"""
        with self.canvas:
            # Main building
            Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
            building_width = self.width * 0.7
            building_height = self.height * 0.5
            building_x = self.center_x - building_width/2
            building_y = self.height * 0.2
            
            # Main structure
            Rectangle(
                pos=(building_x, building_y),
                size=(building_width, building_height)
            )
            
            # Roof
            Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
            roof_points = [
                building_x, building_y + building_height,  # Bottom left
                building_x + building_width, building_y + building_height,  # Bottom right
                building_x + building_width + building_width * 0.1, building_y + building_height + building_height * 0.3,  # Top right
                building_x - building_width * 0.1, building_y + building_height + building_height * 0.3   # Top left
            ]
            Line(points=roof_points, width=2, close=True)
            
            # Windows
            Color(*get_color_from_hex(REGENCY_COLORS["azure"]))
            window_width = building_width * 0.1
            window_height = building_height * 0.3
            window_spacing = (building_width - 5 * window_width) / 6
            
            for i in range(5):
                x = building_x + window_spacing + i * (window_width + window_spacing)
                y = building_y + building_height * 0.15
                Rectangle(pos=(x, y), size=(window_width, window_height))
                
                # Upper floor windows
                y_upper = building_y + building_height * 0.6
                Rectangle(pos=(x, y_upper), size=(window_width, window_height))
            
            # Grand entrance
            Color(*get_color_from_hex(REGENCY_COLORS["navy"]))
            door_width = building_width * 0.15
            door_height = building_height * 0.4
            door_x = self.center_x - door_width/2
            door_y = building_y
            Rectangle(pos=(door_x, door_y), size=(door_width, door_height))
            
            # Columns
            Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
            column_width = door_width * 0.3
            column_spacing = door_width * 1.5
            
            for i in range(2):
                column_x = door_x - column_spacing + i * column_spacing * 2
                Rectangle(pos=(column_x, building_y), size=(column_width, building_height * 0.6))
            
            # Estate grounds
            Color(*get_color_from_hex("#556B2F"))  # Dark olive green
            Rectangle(pos=(0, 0), size=(self.width, building_y))
    
    def _draw_cottage(self):
        """Draw a Regency cottage"""
        with self.canvas:
            # Main building
            Color(*get_color_from_hex("#F5DEB3"))  # Wheat color
            building_width = self.width * 0.5
            building_height = self.height * 0.4
            building_x = self.center_x - building_width/2
            building_y = self.height * 0.2
            
            # Main structure
            Rectangle(
                pos=(building_x, building_y),
                size=(building_width, building_height)
            )
            
            # Thatched roof
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown
            roof_points = [
                building_x, building_y + building_height,  # Bottom left
                building_x + building_width, building_y + building_height,  # Bottom right
                building_x + building_width/2, building_y + building_height + building_height * 0.6   # Top center
            ]
            Line(points=roof_points, width=3, close=True)
            
            # Door
            Color(*get_color_from_hex("#8B4513"))  # Brown
            door_width = building_width * 0.2
            door_height = building_height * 0.6
            door_x = building_x + building_width * 0.4
            door_y = building_y
            Rectangle(pos=(door_x, door_y), size=(door_width, door_height))
            
            # Windows
            Color(*get_color_from_hex(REGENCY_COLORS["azure"]))
            window_size = building_width * 0.15
            
            # Left window
            window_x = building_x + building_width * 0.15
            window_y = building_y + building_height * 0.3
            Rectangle(pos=(window_x, window_y), size=(window_size, window_size))
            
            # Right window
            window_x = building_x + building_width * 0.7
            Rectangle(pos=(window_x, window_y), size=(window_size, window_size))
            
            # Garden
            Color(*get_color_from_hex("#556B2F"))  # Dark olive green
            Rectangle(pos=(0, 0), size=(self.width, building_y))
            
            # Garden flowers
            if self.season in ["spring", "summer"]:
                Color(*get_color_from_hex("#FF69B4"))  # Pink
                for i in range(10):
                    x = random.uniform(building_x - building_width/2, building_x + building_width * 1.5)
                    y = random.uniform(building_y/2, building_y * 0.9)
                    size = random.uniform(5, 10)
                    Ellipse(pos=(x, y), size=(size, size))
    
    def _draw_park(self):
        """Draw a Regency park or garden"""
        with self.canvas:
            # Grass
            Color(*get_color_from_hex("#7CFC00"))  # Lawn green
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.6))
            
            # Path
            Color(*get_color_from_hex("#F5DEB3"))  # Wheat
            points = [
                0, self.height * 0.3 - 10,
                0, self.height * 0.3 + 10,
                self.width, self.height * 0.3 + 15,
                self.width, self.height * 0.3 - 15
            ]
            Line(points=points, width=1, close=True)
            
            # Trees
            self._draw_tree(self.width * 0.2, self.height * 0.4, self.height * 0.3)
            self._draw_tree(self.width * 0.8, self.height * 0.45, self.height * 0.35)
            self._draw_tree(self.width * 0.5, self.height * 0.5, self.height * 0.25)
            
            # Garden fountain
            Color(*get_color_from_hex("#B0C4DE"))  # Light steel blue
            Ellipse(pos=(self.center_x - 30, self.height * 0.2 - 30), size=(60, 30))
            
            # Bench
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown
            Rectangle(pos=(self.width * 0.15, self.height * 0.25), size=(self.width * 0.1, 5))
            Rectangle(pos=(self.width * 0.15, self.height * 0.20), size=(5, self.height * 0.05))
            Rectangle(pos=(self.width * 0.15 + self.width * 0.1 - 5, self.height * 0.20), size=(5, self.height * 0.05))
    
    def _draw_ballroom(self):
        """Draw a Regency ballroom interior"""
        with self.canvas:
            # Floor
            Color(*get_color_from_hex("#CD853F"))  # Peru (wooden floor)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.3))
            
            # Walls
            Color(*get_color_from_hex("#FFF8DC"))  # Cornsilk
            Rectangle(pos=(0, self.height * 0.3), size=(self.width, self.height * 0.7))
            
            # Grand windows
            Color(*get_color_from_hex(REGENCY_COLORS["azure"]))
            window_width = self.width * 0.15
            window_height = self.height * 0.4
            window_spacing = (self.width - 3 * window_width) / 4
            
            for i in range(3):
                x = window_spacing + i * (window_width + window_spacing)
                y = self.height * 0.35
                Rectangle(pos=(x, y), size=(window_width, window_height))
            
            # Chandelier
            Color(*get_color_from_hex(REGENCY_COLORS["gold"]))
            Ellipse(pos=(self.center_x - 30, self.height * 0.7), size=(60, 30))
            
            # For evening/night scenes, add chandelier glow
            if self.time_of_day in ["evening", "night"]:
                Color(1, 1, 0.7, 0.3)  # Soft yellow glow
                Ellipse(pos=(self.center_x - 40, self.height * 0.66), size=(80, 40))
    
    def _draw_generic_landscape(self):
        """Draw a generic Regency-era landscape"""
        with self.canvas:
            # Sky already drawn in _draw_location
            
            # Hills
            Color(*get_color_from_hex("#228B22"))  # Forest green
            
            # First hill
            hill_points = []
            for x in range(0, self.width + 10, 10):
                hill_points.extend([x, self.height * 0.6 + math.sin(x/50) * 20])
            hill_points.extend([self.width, 0, 0, 0])  # Complete the shape
            Line(points=hill_points, width=1, close=True)
            
            # Second hill
            hill2_points = []
            for x in range(0, self.width + 10, 10):
                hill2_points.extend([x, self.height * 0.5 + math.sin(x/70 + 2) * 15])
            hill2_points.extend([self.width, 0, 0, 0])  # Complete the shape
            Line(points=hill2_points, width=1, close=True)
            
            # Draw a distant country house
            self._draw_distant_building(self.width * 0.7, self.height * 0.55, self.width * 0.15, self.height * 0.08)
            
            # Draw trees
            self._draw_tree(self.width * 0.2, self.height * 0.4, self.height * 0.15)
            self._draw_tree(self.width * 0.3, self.height * 0.45, self.height * 0.1)
            self._draw_tree(self.width * 0.85, self.height * 0.42, self.height * 0.12)
    
    def _draw_tree(self, x, y, size):
        """Helper to draw a tree"""
        with self.canvas:
            # Tree trunk
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown
            trunk_width = size * 0.2
            trunk_height = size * 0.4
            Rectangle(pos=(x - trunk_width/2, y - trunk_height), size=(trunk_width, trunk_height))
            
            # Tree foliage depends on season
            if self.season == "autumn":
                Color(*get_color_from_hex("#FFA500"))  # Orange
            elif self.season == "winter":
                if random.random() > 0.7:  # Some trees keep foliage
                    Color(*get_color_from_hex("#2F4F4F"))  # Dark slate gray
                else:
                    return  # Bare tree, just trunk
            else:  # spring or summer
                Color(*get_color_from_hex("#228B22"))  # Forest green
            
            # Tree crown
            Ellipse(pos=(x - size/2, y), size=(size, size))
    
    def _draw_distant_building(self, x, y, width, height):
        """Draw a distant building silhouette"""
        with self.canvas:
            # Main structure
            Color(*get_color_from_hex("#708090"))  # Slate gray
            Rectangle(pos=(x, y), size=(width, height))
            
            # Roof
            roof_points = [
                x, y + height,  # Bottom left
                x + width, y + height,  # Bottom right
                x + width/2, y + height + height * 0.5  # Top
            ]
            Line(points=roof_points, width=1, close=True)
    
    def _add_seasonal_elements(self):
        """Add season-specific elements to the illustration"""
        with self.canvas:
            if self.season == "winter":
                # Snow effects
                Color(1, 1, 1, 0.7)  # White with transparency
                for i in range(30):
                    x = random.uniform(0, self.width)
                    y = random.uniform(self.height * 0.4, self.height)
                    size = random.uniform(2, 5)
                    Ellipse(pos=(x, y), size=(size, size))
                    
            elif self.season == "autumn":
                # Falling leaves
                autumn_colors = ["#FFA500", "#FF8C00", "#FF4500", "#CD5C5C"]
                for i in range(20):
                    Color(*get_color_from_hex(random.choice(autumn_colors)))
                    x = random.uniform(0, self.width)
                    y = random.uniform(self.height * 0.3, self.height)
                    size = random.uniform(3, 7)
                    Ellipse(pos=(x, y), size=(size, size))
                    
            elif self.season == "spring":
                # Flowers and blossoms
                flower_colors = ["#FF69B4", "#BA55D3", "#FFC0CB", "#FFFF00"]
                for i in range(15):
                    Color(*get_color_from_hex(random.choice(flower_colors)))
                    x = random.uniform(0, self.width)
                    y = random.uniform(0, self.height * 0.4)
                    size = random.uniform(3, 8)
                    Ellipse(pos=(x, y), size=(size, size))
                    
            elif self.season == "summer":
                # Bright sunshine
                if self.time_of_day == "day":
                    Color(1, 1, 0, 0.3)  # Yellow with transparency
                    Ellipse(pos=(self.width * 0.8, self.height * 0.8), size=(60, 60))
    
    def _add_decorative_frame(self):
        """Add a decorative period-appropriate frame"""
        with self.canvas:
            # Frame border
            Color(*get_color_from_hex(REGENCY_COLORS["gold"]))
            frame_width = 10
            Line(rectangle=(0, 0, self.width, self.height), width=frame_width)
            
            # Corner ornaments
            corner_size = 20
            
            # Top-left corner
            Line(
                points=[
                    0, self.height,
                    corner_size, self.height,
                    corner_size, self.height - corner_size,
                    0, self.height - corner_size
                ],
                width=2, close=True
            )
            
            # Top-right corner
            Line(
                points=[
                    self.width, self.height,
                    self.width - corner_size, self.height,
                    self.width - corner_size, self.height - corner_size,
                    self.width, self.height - corner_size
                ],
                width=2, close=True
            )
            
            # Bottom-left corner
            Line(
                points=[
                    0, 0,
                    corner_size, 0,
                    corner_size, corner_size,
                    0, corner_size
                ],
                width=2, close=True
            )
            
            # Bottom-right corner
            Line(
                points=[
                    self.width, 0,
                    self.width - corner_size, 0,
                    self.width - corner_size, corner_size,
                    self.width, corner_size
                ],
                width=2, close=True
            )


class ThematicQuoteFrameWidget(Widget):
    """Widget for displaying thematically-framed Jane Austen quotes"""
    
    quote_text = StringProperty("")
    quote_source = StringProperty("")
    quote_theme = StringProperty("love")
    include_context = ObjectProperty(True)
    context_text = StringProperty("")
    
    def __init__(self, **kwargs):
        super(ThematicQuoteFrameWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (500, 300)
        
        # Schedule the drawing after the widget is fully initialized
        Clock.schedule_once(self._draw_quote_frame, 0)
    
    def _draw_quote_frame(self, dt):
        """Draw the thematic quote frame"""
        self.canvas.clear()
        
        # Get theme colors
        theme = self.quote_theme.lower()
        if theme not in THEME_COLORS:
            theme = "love"  # Default theme
            
        theme_colors = THEME_COLORS[theme]
        
        # Background
        with self.canvas:
            Color(*get_color_from_hex(theme_colors["secondary"]))
            Rectangle(pos=(0, 0), size=self.size)
            
            # Decorative border based on theme
            self._draw_thematic_border(theme)
            
            # Quote text and attribution
            self._draw_quote_text()
            
            # Context if included
            if self.include_context and self.context_text:
                self._draw_context()
    
    def _draw_thematic_border(self, theme):
        """Draw a border with thematic elements"""
        with self.canvas:
            # Main border
            Color(*get_color_from_hex(THEME_COLORS[theme]["primary"]))
            border_width = 5
            Line(rectangle=(border_width, border_width, 
                           self.width - 2*border_width, 
                           self.height - 2*border_width), 
                width=border_width)
            
            # Theme-specific decorative elements at corners
            corner_size = 30
            
            # Choose symbols based on theme
            symbols = self._get_theme_symbols(theme)
            
            # Draw symbols at corners
            for i, symbol_pos in enumerate([
                (border_width*2, self.height - border_width*2 - corner_size),  # Top left
                (self.width - border_width*2 - corner_size, self.height - border_width*2 - corner_size),  # Top right
                (border_width*2, border_width*2),  # Bottom left
                (self.width - border_width*2 - corner_size, border_width*2)  # Bottom right
            ]):
                with self.canvas.after:
                    Color(*get_color_from_hex(THEME_COLORS[theme]["accent"]))
                    
                    # Get symbol from list, cycling if needed
                    symbol_index = i % len(symbols)
                    symbol = symbols[symbol_index]
                    
                    # Draw symbol (simplified representation)
                    if symbol == "heart":
                        self._draw_heart(symbol_pos[0], symbol_pos[1], corner_size)
                    elif symbol == "scroll":
                        self._draw_scroll(symbol_pos[0], symbol_pos[1], corner_size)
                    elif symbol == "flower":
                        self._draw_flower(symbol_pos[0], symbol_pos[1], corner_size)
                    elif symbol == "book":
                        self._draw_book(symbol_pos[0], symbol_pos[1], corner_size)
                    else:  # Default to a simple circle
                        Ellipse(pos=symbol_pos, size=(corner_size, corner_size))
    
    def _draw_quote_text(self):
        """Draw the quote text and attribution"""
        # This will be implemented through Kivy labels in the actual application
        # Here we just show the graphical frame representation
        with self.canvas:
            # Quote area
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            quote_area_margin = 40
            Rectangle(
                pos=(quote_area_margin, quote_area_margin),
                size=(self.width - 2*quote_area_margin, self.height - 2*quote_area_margin)
            )
            
            # Quotation marks
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            quote_mark_size = 20
            
            # Opening quote mark
            Line(
                points=[
                    quote_area_margin + 10, self.height - quote_area_margin - 30,
                    quote_area_margin + 10 + quote_mark_size, self.height - quote_area_margin - 30,
                    quote_area_margin + 10 + quote_mark_size, self.height - quote_area_margin - 30 - quote_mark_size,
                    quote_area_margin + 10, self.height - quote_area_margin - 30 - quote_mark_size
                ],
                width=2
            )
            
            # Closing quote mark
            Line(
                points=[
                    self.width - quote_area_margin - 10 - quote_mark_size, quote_area_margin + 30,
                    self.width - quote_area_margin - 10, quote_area_margin + 30,
                    self.width - quote_area_margin - 10, quote_area_margin + 30 + quote_mark_size,
                    self.width - quote_area_margin - 10 - quote_mark_size, quote_area_margin + 30 + quote_mark_size
                ],
                width=2
            )
    
    def _draw_context(self):
        """Draw the contextual information section"""
        with self.canvas:
            # Context area at bottom
            Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
            context_height = 60
            Rectangle(
                pos=(40, 40),
                size=(self.width - 80, context_height)
            )
            
            # Divider between quote and context
            Color(*get_color_from_hex(THEME_COLORS[self.quote_theme]["primary"]))
            Line(
                points=[40, 40 + context_height, self.width - 40, 40 + context_height],
                width=2
            )
    
    def _get_theme_symbols(self, theme):
        """Get symbolic decorative elements based on quote theme"""
        theme_symbols = {
            "love": ["heart", "flower"],
            "marriage": ["heart", "ring"],
            "social_class": ["crown", "book"],
            "family": ["house", "tree"],
            "self_discovery": ["mirror", "path"],
            "reputation": ["crown", "scroll"],
            "prejudice": ["mask", "book"],
            "wealth": ["coin", "crown"]
        }
        
        return theme_symbols.get(theme, ["heart", "flower"])  # Default to love symbols
    
    def _draw_heart(self, x, y, size):
        """Draw a heart symbol"""
        with self.canvas:
            points = []
            for i in range(30):
                angle = i * 2 * math.pi / 30
                if angle < math.pi:
                    px = x + size/2 + size/2 * math.sin(angle)
                    py = y + size/2 + size/2 * math.cos(angle)
                else:
                    # Create the bottom point of the heart
                    t = (angle - math.pi) / math.pi  # 0 to 1
                    px = x + size/2 + size/2 * math.sin(angle)
                    py = y + size/2 - size/2 * (0.8 + 0.2 * math.cos(angle))
                points.extend([px, py])
            Line(points=points, width=2, close=True)
    
    def _draw_scroll(self, x, y, size):
        """Draw a scroll symbol"""
        with self.canvas:
            # Main scroll body
            Rectangle(pos=(x, y + size/4), size=(size, size/2))
            
            # Rolled ends
            Ellipse(pos=(x - size/8, y + size/6), size=(size/4, size*2/3))
            Ellipse(pos=(x + size - size/8, y + size/6), size=(size/4, size*2/3))
    
    def _draw_flower(self, x, y, size):
        """Draw a flower symbol"""
        with self.canvas:
            # Flower center
            Ellipse(pos=(x + size/3, y + size/3), size=(size/3, size/3))
            
            # Petals
            for angle in range(0, 360, 60):
                rad = math.radians(angle)
                px = x + size/2 + size/3 * math.cos(rad)
                py = y + size/2 + size/3 * math.sin(rad)
                Ellipse(pos=(px - size/6, py - size/6), size=(size/3, size/3))
    
    def _draw_book(self, x, y, size):
        """Draw a book symbol"""
        with self.canvas:
            # Book cover
            Rectangle(pos=(x, y), size=(size*0.8, size))
            
            # Book spine
            Rectangle(pos=(x + size*0.8, y + size*0.1), size=(size*0.2, size*0.8))
            
            # Pages
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            for i in range(5):
                Line(
                    points=[
                        x + size*0.1, y + size*0.2 + i*size*0.15,
                        x + size*0.7, y + size*0.2 + i*size*0.15
                    ],
                    width=1
                )


class EventIllustrationWidget(Widget):
    """Widget for illustrating Regency-era story events"""
    
    event_type = StringProperty("meeting")  # meeting, ball, proposal, journey, etc.
    description = StringProperty("")
    
    def __init__(self, **kwargs):
        super(EventIllustrationWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (400, 300)
        
        # Schedule the drawing after the widget is fully initialized
        Clock.schedule_once(self._draw_event, 0)
    
    def _draw_event(self, dt):
        """Draw the event illustration"""
        self.canvas.clear()
        
        # Background
        with self.canvas:
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            Rectangle(pos=(0, 0), size=self.size)
            
            # Add decorative frame
            self._add_decorative_frame()
            
            # Draw based on event type
            if self.event_type == "meeting":
                self._draw_meeting_scene()
            elif self.event_type == "ball":
                self._draw_ball_scene()
            elif self.event_type == "proposal":
                self._draw_proposal_scene()
            elif self.event_type == "journey":
                self._draw_journey_scene()
            elif self.event_type == "letter":
                self._draw_letter_scene()
            else:
                self._draw_generic_scene()
            
            # Add caption
            self._add_caption()
    
    def _draw_meeting_scene(self):
        """Draw a Regency-era first meeting scene"""
        with self.canvas:
            # Scene elements: floor, wall, room
            Color(*get_color_from_hex("#CD853F"))  # Peru (wooden floor)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.3))
            
            Color(*get_color_from_hex("#FFF8DC"))  # Cornsilk (wall)
            Rectangle(pos=(0, self.height * 0.3), size=(self.width, self.height * 0.7))
            
            # Window
            Color(*get_color_from_hex(REGENCY_COLORS["azure"]))
            window_x = self.width * 0.6
            window_y = self.height * 0.4
            window_width = self.width * 0.3
            window_height = self.height * 0.4
            Rectangle(pos=(window_x, window_y), size=(window_width, window_height))
            
            # Characters
            # Female silhouette
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            female_size = self.height * 0.4
            female_x = self.width * 0.3
            female_y = self.height * 0.25
            
            # Head
            Ellipse(pos=(female_x - female_size*0.1, female_y + female_size*0.7), 
                   size=(female_size*0.2, female_size*0.2))
            
            # Dress triangular silhouette
            points = [
                female_x, female_y + female_size*0.7,  # neck
                female_x - female_size*0.3, female_y,  # left bottom
                female_x + female_size*0.3, female_y   # right bottom
            ]
            Line(points=points, width=2, close=True)
            
            # Male silhouette
            male_size = self.height * 0.45
            male_x = self.width * 0.5
            male_y = self.height * 0.25
            
            # Head
            Ellipse(pos=(male_x - male_size*0.1, male_y + male_size*0.7), 
                   size=(male_size*0.2, male_size*0.2))
            
            # Body rectangular silhouette
            Rectangle(pos=(male_x - male_size*0.15, male_y), 
                     size=(male_size*0.3, male_size*0.7))
    
    def _draw_ball_scene(self):
        """Draw a Regency ballroom scene"""
        with self.canvas:
            # Ballroom floor
            Color(*get_color_from_hex("#CD853F"))  # Peru (wooden floor)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.3))
            
            # Ballroom walls
            Color(*get_color_from_hex("#FFF8DC"))  # Cornsilk
            Rectangle(pos=(0, self.height * 0.3), size=(self.width, self.height * 0.7))
            
            # Chandelier
            Color(*get_color_from_hex(REGENCY_COLORS["gold"]))
            chandelier_x = self.width * 0.5
            chandelier_y = self.height * 0.8
            chandelier_size = self.width * 0.15
            Ellipse(pos=(chandelier_x - chandelier_size/2, chandelier_y - chandelier_size/4), 
                   size=(chandelier_size, chandelier_size/2))
            
            # Hanging elements
            for i in range(6):
                angle = i * 2 * math.pi / 6
                px = chandelier_x + chandelier_size/2 * math.cos(angle)
                py = chandelier_y - chandelier_size/4 + chandelier_size/4 * math.sin(angle)
                Line(
                    points=[chandelier_x, chandelier_y - chandelier_size/4, px, py - chandelier_size*0.3],
                    width=1
                )
            
            # Dancing couples
            couple_size = self.height * 0.25
            couple_spacing = self.width / 4
            
            for i in range(3):
                couple_x = couple_spacing + i * couple_spacing
                couple_y = self.height * 0.25
                
                # Female silhouette
                Color(*get_color_from_hex("#FFB6C1"))  # Light pink
                Ellipse(pos=(couple_x - couple_size*0.3, couple_y + couple_size*0.6), 
                       size=(couple_size*0.15, couple_size*0.15))  # Head
                
                # Dress
                points = [
                    couple_x - couple_size*0.22, couple_y + couple_size*0.6,  # neck
                    couple_x - couple_size*0.4, couple_y,  # left bottom
                    couple_x - couple_size*0.05, couple_y   # right bottom
                ]
                Line(points=points, width=2, close=True)
                
                # Male silhouette
                Color(*get_color_from_hex("#000080"))  # Navy
                Ellipse(pos=(couple_x + couple_size*0.1, couple_y + couple_size*0.6), 
                       size=(couple_size*0.15, couple_size*0.15))  # Head
                
                # Coat
                Rectangle(pos=(couple_x + couple_size*0.05, couple_y), 
                         size=(couple_size*0.25, couple_size*0.6))
    
    def _draw_proposal_scene(self):
        """Draw a Regency-era proposal scene"""
        with self.canvas:
            # Garden setting
            Color(*get_color_from_hex("#228B22"))  # Forest green (garden)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.4))
            
            Color(*get_color_from_hex("#87CEEB"))  # Sky blue
            Rectangle(pos=(0, self.height * 0.4), size=(self.width, self.height * 0.6))
            
            # Garden path
            Color(*get_color_from_hex("#F5DEB3"))  # Wheat
            Ellipse(pos=(self.width * 0.1, self.height * 0.05), 
                   size=(self.width * 0.8, self.height * 0.3))
            
            # Tree
            self._draw_tree(self.width * 0.8, self.height * 0.5, self.height * 0.4)
            
            # Characters
            # Female standing
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            female_size = self.height * 0.4
            female_x = self.width * 0.4
            female_y = self.height * 0.15
            
            # Head
            Ellipse(pos=(female_x - female_size*0.1, female_y + female_size*0.7), 
                   size=(female_size*0.2, female_size*0.2))
            
            # Dress
            points = [
                female_x, female_y + female_size*0.7,  # neck
                female_x - female_size*0.25, female_y,  # left bottom
                female_x + female_size*0.25, female_y   # right bottom
            ]
            Line(points=points, width=2, close=True)
            
            # Male kneeling
            male_size = self.height * 0.3
            male_x = self.width * 0.6
            male_y = self.height * 0.1
            
            # Head
            Ellipse(pos=(male_x - male_size*0.1, male_y + male_size*0.6), 
                   size=(male_size*0.2, male_size*0.2))
            
            # Kneeling body
            Rectangle(pos=(male_x - male_size*0.15, male_y), 
                     size=(male_size*0.3, male_size*0.5))
    
    def _draw_journey_scene(self):
        """Draw a Regency-era journey scene with carriage"""
        with self.canvas:
            # Sky
            Color(*get_color_from_hex("#87CEEB"))  # Sky blue
            Rectangle(pos=(0, self.height * 0.4), size=(self.width, self.height * 0.6))
            
            # Ground
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown (dirt road)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.4))
            
            Color(*get_color_from_hex("#228B22"))  # Forest green (grass on sides)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.1))
            
            # Road
            Color(*get_color_from_hex("#D2B48C"))  # Tan
            points = [
                0, self.height * 0.15,
                self.width, self.height * 0.15,
                self.width, self.height * 0.35,
                0, self.height * 0.35
            ]
            Line(points=points, width=2, close=True)
            
            # Carriage
            carriage_x = self.width * 0.4
            carriage_y = self.height * 0.2
            carriage_width = self.width * 0.3
            carriage_height = self.height * 0.15
            
            # Carriage body
            Color(*get_color_from_hex("#000000"))  # Black
            Rectangle(pos=(carriage_x, carriage_y), size=(carriage_width, carriage_height))
            
            # Wheels
            wheel_size = carriage_height * 0.8
            Ellipse(pos=(carriage_x + carriage_width * 0.15 - wheel_size/2, carriage_y - wheel_size/2), 
                   size=(wheel_size, wheel_size))
            Ellipse(pos=(carriage_x + carriage_width * 0.85 - wheel_size/2, carriage_y - wheel_size/2), 
                   size=(wheel_size, wheel_size))
            
            # Horse
            horse_width = carriage_width * 0.8
            horse_height = carriage_height * 0.7
            horse_x = carriage_x - horse_width
            horse_y = carriage_y + carriage_height * 0.1
            
            # Horse body
            Rectangle(pos=(horse_x, horse_y), size=(horse_width * 0.7, horse_height))
            
            # Horse head
            head_size = horse_height * 0.6
            Ellipse(pos=(horse_x - head_size * 0.5, horse_y + horse_height * 0.5), 
                   size=(head_size, head_size * 0.5))
            
            # Horse legs
            leg_width = horse_width * 0.05
            for i in range(4):
                leg_x = horse_x + i * horse_width * 0.2
                Rectangle(pos=(leg_x, horse_y - horse_height * 0.5), 
                         size=(leg_width, horse_height * 0.5))
    
    def _draw_letter_scene(self):
        """Draw a Regency-era letter writing or reading scene"""
        with self.canvas:
            # Room interior
            Color(*get_color_from_hex("#FFF8DC"))  # Cornsilk (wall)
            Rectangle(pos=(0, 0), size=(self.width, self.height))
            
            # Writing desk
            desk_width = self.width * 0.4
            desk_height = self.height * 0.2
            desk_x = self.width * 0.3
            desk_y = self.height * 0.25
            
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown (wooden desk)
            Rectangle(pos=(desk_x, desk_y), size=(desk_width, desk_height))
            
            # Letter on desk
            letter_width = desk_width * 0.6
            letter_height = desk_height * 0.8
            letter_x = desk_x + desk_width * 0.2
            letter_y = desk_y + desk_height * 0.1
            
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            Rectangle(pos=(letter_x, letter_y), size=(letter_width, letter_height))
            
            # Letter lines
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            for i in range(5):
                Line(
                    points=[
                        letter_x + letter_width * 0.1,
                        letter_y + letter_height * (0.2 + 0.15 * i),
                        letter_x + letter_width * 0.9,
                        letter_y + letter_height * (0.2 + 0.15 * i)
                    ],
                    width=1
                )
            
            # Ink pot and quill
            inkpot_size = desk_height * 0.3
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            Ellipse(pos=(desk_x + desk_width * 0.1, desk_y + desk_height * 0.6), 
                   size=(inkpot_size, inkpot_size))
            
            # Quill
            quill_length = desk_width * 0.2
            Line(
                points=[
                    desk_x + desk_width * 0.1 + inkpot_size/2,
                    desk_y + desk_height * 0.6 + inkpot_size/2,
                    desk_x + desk_width * 0.1 + inkpot_size/2 + quill_length,
                    desk_y + desk_height * 0.6 + inkpot_size/2 + quill_length * 0.3
                ],
                width=2
            )
            
            # Person at desk (silhouette)
            person_x = desk_x + desk_width * 0.5
            person_y = desk_y + desk_height
            
            # Head
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            head_size = desk_height * 0.5
            Ellipse(pos=(person_x - head_size/2, person_y + head_size * 0.5), 
                   size=(head_size, head_size))
            
            # Upper body
            body_width = head_size * 1.2
            body_height = desk_y + desk_height - (person_y + head_size * 0.5)
            Rectangle(pos=(person_x - body_width/2, person_y), 
                     size=(body_width, body_height))
    
    def _draw_generic_scene(self):
        """Draw a generic scene based on event description"""
        with self.canvas:
            # Parse description for keywords to determine scene elements
            description = self.description.lower()
            
            # Default to drawing room scene
            indoor = True
            has_characters = True
            time_of_day = "day"
            
            if any(word in description for word in ["garden", "park", "outside", "outdoor", "walk"]):
                indoor = False
            
            if any(word in description for word in ["night", "evening", "dark"]):
                time_of_day = "night"
            elif any(word in description for word in ["sunset", "dusk", "afternoon"]):
                time_of_day = "evening"
                
            # Draw basic setting
            if indoor:
                self._draw_indoor_setting(time_of_day)
            else:
                self._draw_outdoor_setting(time_of_day)
                
            # Add characters if needed
            if has_characters:
                self._add_generic_characters(indoor)
    
    def _draw_indoor_setting(self, time_of_day):
        """Draw a generic indoor Regency setting"""
        with self.canvas:
            # Floor
            Color(*get_color_from_hex("#CD853F"))  # Peru (wooden floor)
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.3))
            
            # Walls
            Color(*get_color_from_hex("#FFF8DC"))  # Cornsilk
            Rectangle(pos=(0, self.height * 0.3), size=(self.width, self.height * 0.7))
            
            # Window
            window_width = self.width * 0.25
            window_height = self.height * 0.4
            window_x = self.width * 0.7
            window_y = self.height * 0.4
            
            Color(*get_color_from_hex(REGENCY_COLORS["azure"]))
            Rectangle(pos=(window_x, window_y), size=(window_width, window_height))
            
            # Window light based on time of day
            if time_of_day == "day":
                Color(0.9, 0.9, 1, 0.3)  # Light blue, transparent
            elif time_of_day == "evening":
                Color(1, 0.8, 0.6, 0.3)  # Sunset orange, transparent
            else:  # night
                Color(0.1, 0.1, 0.3, 0.3)  # Dark blue, transparent
            
            Rectangle(pos=(window_x, window_y), size=(window_width, window_height))
            
            # Furniture - sofa
            sofa_width = self.width * 0.4
            sofa_height = self.height * 0.15
            sofa_x = self.width * 0.2
            sofa_y = self.height * 0.2
            
            Color(*get_color_from_hex("#8B0000"))  # Dark red
            Rectangle(pos=(sofa_x, sofa_y), size=(sofa_width, sofa_height))
            
            # Sofa back
            Rectangle(pos=(sofa_x, sofa_y + sofa_height), 
                     size=(sofa_width, sofa_height * 0.3))
            
            # Sofa arms
            arm_width = sofa_width * 0.1
            Rectangle(pos=(sofa_x - arm_width, sofa_y), 
                     size=(arm_width, sofa_height * 1.3))
            Rectangle(pos=(sofa_x + sofa_width, sofa_y), 
                     size=(arm_width, sofa_height * 1.3))
    
    def _draw_outdoor_setting(self, time_of_day):
        """Draw a generic outdoor Regency setting"""
        with self.canvas:
            # Sky based on time of day
            if time_of_day == "day":
                Color(*get_color_from_hex("#87CEEB"))  # Sky blue
            elif time_of_day == "evening":
                Color(*get_color_from_hex("#FF7F50"))  # Coral sunset
            else:  # night
                Color(*get_color_from_hex("#191970"))  # Midnight blue
                
            Rectangle(pos=(0, self.height * 0.3), size=(self.width, self.height * 0.7))
            
            # Ground
            Color(*get_color_from_hex("#228B22"))  # Forest green
            Rectangle(pos=(0, 0), size=(self.width, self.height * 0.3))
            
            # Path
            Color(*get_color_from_hex("#F5DEB3"))  # Wheat
            Ellipse(pos=(self.width * 0.1, self.height * 0.05), 
                   size=(self.width * 0.8, self.height * 0.2))
            
            # Trees
            self._draw_tree(self.width * 0.8, self.height * 0.4, self.height * 0.3)
            self._draw_tree(self.width * 0.2, self.height * 0.45, self.height * 0.25)
            
            # Add distant house if evening/day
            if time_of_day != "night":
                house_width = self.width * 0.25
                house_height = self.height * 0.15
                house_x = self.width * 0.4
                house_y = self.height * 0.5
                
                Color(*get_color_from_hex(REGENCY_COLORS["cream"]))
                Rectangle(pos=(house_x, house_y), size=(house_width, house_height))
                
                # Roof
                Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
                points = [
                    house_x, house_y + house_height,
                    house_x + house_width, house_y + house_height,
                    house_x + house_width/2, house_y + house_height + house_height * 0.5
                ]
                Line(points=points, width=2, close=True)
    
    def _add_generic_characters(self, indoor):
        """Add generic characters to the scene"""
        with self.canvas:
            # Determine character positions based on setting
            if indoor:
                # Characters in drawing room
                char1_x = self.width * 0.3
                char1_y = self.height * 0.25
                
                char2_x = self.width * 0.5
                char2_y = self.height * 0.25
            else:
                # Characters on garden path
                char1_x = self.width * 0.4
                char1_y = self.height * 0.15
                
                char2_x = self.width * 0.6
                char2_y = self.height * 0.15
            
            # Draw female character
            self._draw_simple_character(char1_x, char1_y, self.height * 0.3, "female")
            
            # Draw male character
            self._draw_simple_character(char2_x, char2_y, self.height * 0.35, "male")
    
    def _draw_simple_character(self, x, y, size, gender):
        """Draw a simple character silhouette"""
        with self.canvas:
            # Head
            Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
            head_size = size * 0.2
            Ellipse(pos=(x - head_size/2, y + size * 0.7), size=(head_size, head_size))
            
            if gender == "female":
                # Female dress triangular silhouette
                points = [
                    x, y + size*0.7,  # neck
                    x - size*0.3, y,  # left bottom
                    x + size*0.3, y   # right bottom
                ]
                Line(points=points, width=2, close=True)
            else:
                # Male rectangular silhouette
                Rectangle(pos=(x - size*0.15, y), size=(size*0.3, size*0.7))
    
    def _draw_tree(self, x, y, size):
        """Helper to draw a tree"""
        with self.canvas:
            # Tree trunk
            Color(*get_color_from_hex("#8B4513"))  # Saddle brown
            trunk_width = size * 0.2
            trunk_height = size * 0.4
            Rectangle(pos=(x - trunk_width/2, y - trunk_height), size=(trunk_width, trunk_height))
            
            # Tree foliage
            Color(*get_color_from_hex("#228B22"))  # Forest green
            Ellipse(pos=(x - size/2, y), size=(size, size))
    
    def _add_decorative_frame(self):
        """Add a decorative frame to the illustration"""
        with self.canvas:
            # Frame border
            Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
            frame_width = 8
            Line(rectangle=(frame_width/2, frame_width/2, 
                           self.width - frame_width, 
                           self.height - frame_width), 
                width=frame_width)
            
            # Corner flourishes
            corner_size = 20
            
            # Draw corner flourishes
            for pos in [
                (frame_width, frame_width),  # Bottom left
                (frame_width, self.height - frame_width - corner_size),  # Top left
                (self.width - frame_width - corner_size, frame_width),  # Bottom right
                (self.width - frame_width - corner_size, self.height - frame_width - corner_size)  # Top right
            ]:
                # Simple corner flourish
                Color(*get_color_from_hex(REGENCY_COLORS["gold"]))
                points = []
                for i in range(8):
                    angle = i * math.pi / 4
                    px = pos[0] + corner_size/2 + corner_size/2 * math.cos(angle)
                    py = pos[1] + corner_size/2 + corner_size/2 * math.sin(angle)
                    points.extend([px, py])
                
                Line(points=points, width=1.5, close=True)
    
    def _add_caption(self):
        """Add a caption to the event illustration"""
        with self.canvas:
            # Caption area
            caption_height = 40
            Color(*get_color_from_hex(REGENCY_COLORS["parchment"]))
            Rectangle(pos=(20, 20), size=(self.width - 40, caption_height))
            
            # Caption border
            Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
            Line(rectangle=(20, 20, self.width - 40, caption_height), width=2)


class AnimatedTextWidget(Label):
    """Widget for displaying animated text in Regency style"""
    
    text_to_display = StringProperty("")
    animation_style = StringProperty("quill")  # quill, ink, fade
    animation_speed = NumericProperty(0.05)
    
    def __init__(self, **kwargs):
        super(AnimatedTextWidget, self).__init__(**kwargs)
        self.text = ""
        self.char_index = 0
        self.animation_event = None
        
    def animate_text(self):
        """Start the text animation"""
        self.char_index = 0
        self.text = ""
        
        # Cancel any existing animation
        if self.animation_event:
            Clock.unschedule(self.animation_event)
            
        # Schedule animation based on style
        if self.animation_style == "quill":
            self.animation_event = Clock.schedule_interval(self._animate_quill_style, self.animation_speed)
        elif self.animation_style == "ink":
            self.animation_event = Clock.schedule_interval(self._animate_ink_style, self.animation_speed)
        elif self.animation_style == "fade":
            self._prepare_fade_animation()
        else:
            # Default to quill style
            self.animation_event = Clock.schedule_interval(self._animate_quill_style, self.animation_speed)
    
    def _animate_quill_style(self, dt):
        """Animate text appearance character by character, quill style"""
        if self.char_index < len(self.text_to_display):
            self.text += self.text_to_display[self.char_index]
            self.char_index += 1
            
            # Variable timing for punctuation
            if self.char_index < len(self.text_to_display) and self.text_to_display[self.char_index-1] in ".,:;!?":
                return self.animation_speed * 3  # Longer pause for punctuation
        else:
            # Animation complete
            Clock.unschedule(self.animation_event)
            self.animation_event = None
            
        return self.animation_speed
    
    def _animate_ink_style(self, dt):
        """Animate text appearance with ink saturation effect"""
        if self.char_index < len(self.text_to_display):
            # Add character
            self.text += self.text_to_display[self.char_index]
            self.char_index += 1
            
            # Simulate ink drying effect by temporarily changing color
            # (this would require custom rendering in a real implementation)
            
            # For demonstration, we'll just add characters with variable timing
            if self.char_index % 10 == 0:
                return self.animation_speed * 1.5  # Pause as if dipping quill in ink
        else:
            # Animation complete
            Clock.unschedule(self.animation_event)
            self.animation_event = None
            
        return self.animation_speed
    
    def _prepare_fade_animation(self):
        """Prepare and start a fade-in animation for text"""
        # Set full text immediately but with opacity 0
        self.text = self.text_to_display
        self.opacity = 0
        
        # Create fade-in animation
        anim = Animation(opacity=1, duration=2)
        anim.start(self)


class DecorationManager:
    """Utility class for generating and managing decorative elements"""
    
    @staticmethod
    def get_ornamental_divider(style="classic", width=400):
        """
        Return a widget with an ornamental divider in the specified style
        
        Args:
            style: Divider style ("classic", "floral", "simple")
            width: Width of the divider
            
        Returns:
            Widget containing the divider
        """
        widget = Widget(size=(width, 30), size_hint=(None, None))
        
        with widget.canvas:
            if style == "floral":
                # Floral divider
                Color(*get_color_from_hex(REGENCY_COLORS["burgundy"]))
                
                # Center flower
                center_x = width / 2
                Ellipse(pos=(center_x - 10, 5), size=(20, 20))
                
                # Tendrils extending left and right
                points_left = []
                points_right = []
                
                for i in range(11):
                    x_left = center_x - 15 - i * (width/2 - 20) / 10
                    x_right = center_x + 15 + i * (width/2 - 20) / 10
                    
                    # Oscillating y-values for tendrils
                    y = 15 + math.sin(i * math.pi / 5) * 10
                    
                    points_left.extend([x_left, y])
                    points_right.extend([x_right, y])
                
                Line(points=points_left, width=2)
                Line(points=points_right, width=2)
                
                # Small flowers along the tendrils
                for i in range(2, 11, 3):
                    x_left = center_x - 15 - i * (width/2 - 20) / 10
                    x_right = center_x + 15 + i * (width/2 - 20) / 10
                    y = 15 + math.sin(i * math.pi / 5) * 10
                    
                    # Small flower blossoms
                    Color(*get_color_from_hex(REGENCY_COLORS["rose"]))
                    Ellipse(pos=(x_left - 5, y - 5), size=(10, 10))
                    Ellipse(pos=(x_right - 5, y - 5), size=(10, 10))
                
            elif style == "simple":
                # Simple line divider
                Color(*get_color_from_hex(REGENCY_COLORS["ink"]))
                Line(points=[10, 15, width - 10, 15], width=2)
                
                # Small dots at ends
                Ellipse(pos=(5, 10), size=(10, 10))
                Ellipse(pos=(width - 15, 10), size=(10, 10))
                
            else:  # classic
                # Classic ornamental divider
                Color(*get_color_from_hex(REGENCY_COLORS["sepia"]))
                
                # Central ornament
                center_x = width / 2
                rect_width = 50
                Rectangle(pos=(center_x - rect_width/2, 5), size=(rect_width, 20))
                
                # Lines extending left and right
                Line(points=[10, 15, center_x - rect_width/2, 15], width=2)
                Line(points=[center_x + rect_width/2, 15, width - 10, 15], width=2)
                
                # Ornate ends
                for x in [10, width - 10]:
                    points = []
                    for i in range(8):
                        angle = i * math.pi / 4
                        px = x + 5 * math.cos(angle)
                        py = 15 + 5 * math.sin(angle)
                        points.extend([px, py])
                    
                    Line(points=points, width=1, close=True)
        
        return widget
    
    @staticmethod
    def get_story_header(title, theme=None, width=500):
        """
        Return a widget with a decorative story header
        
        Args:
            title: Story title text
            theme: Optional theme name for styling
            width: Width of the header
            
        Returns:
            Widget containing the header
        """
        widget = Widget(size=(width, 100), size_hint=(None, None))
        
        # Get theme colors
        if theme and theme in THEME_COLORS:
            primary_color = THEME_COLORS[theme]["primary"]
            secondary_color = THEME_COLORS[theme]["secondary"]
            accent_color = THEME_COLORS[theme]["accent"]
        else:
            primary_color = REGENCY_COLORS["sepia"]
            secondary_color = REGENCY_COLORS["parchment"]
            accent_color = REGENCY_COLORS["gold"]
        
        with widget.canvas:
            # Background band
            Color(*get_color_from_hex(secondary_color))
            Rectangle(pos=(0, 20), size=(width, 60))
            
            # Decorative border
            Color(*get_color_from_hex(primary_color))
            Line(rectangle=(0, 20, width, 60), width=3)
            
            # Title placeholder (in a real implementation, this would be a Label)
            # Here we just draw the frame for visualization
            title_width = min(width - 40, len(title) * 15)
            title_x = (width - title_width) / 2
            
            Color(*get_color_from_hex(secondary_color))
            Rectangle(pos=(title_x, 30), size=(title_width, 40))
            
            Color(*get_color_from_hex(primary_color))
            Line(rectangle=(title_x, 30, title_width, 40), width=2)
            
            # Decorative embellishments
            Color(*get_color_from_hex(accent_color))
            
            # Left embellishment
            Ellipse(pos=(title_x - 20, 40), size=(15, 15))
            Line(points=[title_x - 30, 47.5, title_x - 5, 47.5], width=2)
            
            # Right embellishment
            Ellipse(pos=(title_x + title_width + 5, 40), size=(15, 15))
            Line(points=[title_x + title_width + 5, 47.5, title_x + title_width + 30, 47.5], width=2)
        
        return widget
    
    @staticmethod
    def get_seasonal_imagery(season, width=400, height=300):
        """
        Return a widget with seasonal imagery
        
        Args:
            season: Season name ("spring", "summer", "autumn", "winter")
            width: Width of the image
            height: Height of the image
            
        Returns:
            Widget containing the seasonal imagery
        """
        # Create a location illustration with the appropriate season
        widget = LocationIllustrationWidget(
            size=(width, height),
            size_hint=(None, None),
            location_type="park",
            season=season,
            time_of_day="day"
        )
        
        return widget


class VisualImageryApp(App):
    """Demo application to showcase the visual imagery widgets"""
    
    def build(self):
        """Build the demo application UI"""
        # Create a scrollable layout
        root = ScrollView(size_hint=(1, 1))
        
        main_layout = GridLayout(cols=1, spacing=20, padding=20, size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        # Title
        title_label = Label(
            text="Jane Austen Visual Imagery Demo", 
            font_size=24,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(title_label)
        
        # Character Portrait
        section_label = Label(
            text="Character Portraits", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        portraits_layout = BoxLayout(size_hint_y=None, height=420, spacing=10)
        
        # Female upper class
        portrait1 = CharacterPortraitWidget(
            character_name="Lady Elizabeth Worthington",
            character_gender="female",
            character_class="upper",
            character_age=28
        )
        
        # Male middle class
        portrait2 = CharacterPortraitWidget(
            character_name="Mr. Thomas Harrington",
            character_gender="male",
            character_class="middle",
            character_age=35
        )
        
        portraits_layout.add_widget(portrait1)
        portraits_layout.add_widget(portrait2)
        
        main_layout.add_widget(portraits_layout)
        
        # Location Illustrations
        section_label = Label(
            text="Location Illustrations", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        locations_layout = BoxLayout(size_hint_y=None, height=320, spacing=10)
        
        # Estate scene
        location1 = LocationIllustrationWidget(
            location_type="estate",
            season="summer",
            time_of_day="day"
        )
        
        # Ballroom scene
        location2 = LocationIllustrationWidget(
            location_type="ballroom",
            season="winter",
            time_of_day="evening"
        )
        
        locations_layout.add_widget(location1)
        locations_layout.add_widget(location2)
        
        main_layout.add_widget(locations_layout)
        
        # Event Illustrations
        section_label = Label(
            text="Event Illustrations", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        events_layout = BoxLayout(size_hint_y=None, height=320, spacing=10)
        
        # Proposal scene
        event1 = EventIllustrationWidget(
            event_type="proposal",
            description="A dramatic proposal in the garden at sunset"
        )
        
        # Journey scene
        event2 = EventIllustrationWidget(
            event_type="journey",
            description="The long journey to London by carriage"
        )
        
        events_layout.add_widget(event1)
        events_layout.add_widget(event2)
        
        main_layout.add_widget(events_layout)
        
        # Thematic Quote Frames
        section_label = Label(
            text="Thematic Quote Frames", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        quotes_layout = BoxLayout(size_hint_y=None, height=320, spacing=10, orientation='vertical')
        
        # Love quote
        quote1 = ThematicQuoteFrameWidget(
            quote_text="In vain I have struggled. It will not do. My feelings will not be repressed. You must allow me to tell you how ardently I admire and love you.",
            quote_source="Pride and Prejudice",
            quote_theme="love",
            context_text="Spoken by Mr. Darcy during his first proposal to Elizabeth Bennet."
        )
        
        quotes_layout.add_widget(quote1)
        
        main_layout.add_widget(quotes_layout)
        
        # Decorative Elements
        section_label = Label(
            text="Decorative Elements", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        # Story header
        decoration_manager = DecorationManager()
        header = decoration_manager.get_story_header(
            "A Tale of Two Hearts", 
            theme="love",
            width=500
        )
        main_layout.add_widget(header)
        
        # Dividers
        dividers_layout = BoxLayout(size_hint_y=None, height=150, spacing=10, orientation='vertical')
        
        divider1 = decoration_manager.get_ornamental_divider(style="classic", width=500)
        divider2 = decoration_manager.get_ornamental_divider(style="floral", width=500)
        divider3 = decoration_manager.get_ornamental_divider(style="simple", width=500)
        
        dividers_layout.add_widget(divider1)
        dividers_layout.add_widget(divider2)
        dividers_layout.add_widget(divider3)
        
        main_layout.add_widget(dividers_layout)
        
        # Animated Text Demo
        section_label = Label(
            text="Animated Text", 
            font_size=18,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(section_label)
        
        # In a real implementation, this would show animated text
        # For the static mockup, just add a placeholder
        animated_text = Label(
            text="[Text would animate with quill writing effect in real implementation]",
            size_hint_y=None,
            height=80
        )
        main_layout.add_widget(animated_text)
        
        root.add_widget(main_layout)
        return root


# These functions provide an interface to the visual elements

def create_character_portrait(character_info):
    """
    Create a character portrait based on character information
    
    Args:
        character_info: Dictionary with character details
            - name: Character name
            - gender: Character gender
            - class: Social class (upper, middle, lower)
            - age: Character age
            
    Returns:
        CharacterPortraitWidget instance
    """
    return CharacterPortraitWidget(
        character_name=character_info.get('name', 'Unknown'),
        character_gender=character_info.get('gender', 'female'),
        character_class=character_info.get('class', 'middle'),
        character_age=character_info.get('age', 30)
    )


def create_location_illustration(location_info):
    """
    Create a location illustration based on location information
    
    Args:
        location_info: Dictionary with location details
            - type: Location type (estate, cottage, park, ballroom)
            - season: Season (spring, summer, autumn, winter)
            - time_of_day: Time of day (day, evening, night)
            
    Returns:
        LocationIllustrationWidget instance
    """
    return LocationIllustrationWidget(
        location_type=location_info.get('type', 'estate'),
        season=location_info.get('season', 'spring'),
        time_of_day=location_info.get('time_of_day', 'day')
    )


def create_event_illustration(event_info):
    """
    Create an event illustration based on event information
    
    Args:
        event_info: Dictionary with event details
            - type: Event type (meeting, ball, proposal, journey, letter)
            - description: Text description of the event
            
    Returns:
        EventIllustrationWidget instance
    """
    return EventIllustrationWidget(
        event_type=event_info.get('type', 'meeting'),
        description=event_info.get('description', '')
    )


def create_thematic_quote_frame(quote_info):
    """
    Create a thematic quote frame based on quote information
    
    Args:
        quote_info: Dictionary with quote details
            - text: Quote text
            - source: Source work
            - theme: Theme (love, marriage, social_class, etc.)
            - context: Contextual information about the quote
            - include_context: Whether to include context (boolean)
            
    Returns:
        ThematicQuoteFrameWidget instance
    """
    return ThematicQuoteFrameWidget(
        quote_text=quote_info.get('text', ''),
        quote_source=quote_info.get('source', ''),
        quote_theme=quote_info.get('theme', 'love'),
        include_context=quote_info.get('include_context', True),
        context_text=quote_info.get('context', '')
    )


def create_animated_text_widget(text, style="quill", speed=0.05):
    """
    Create an animated text widget
    
    Args:
        text: Text to animate
        style: Animation style ("quill", "ink", "fade")
        speed: Animation speed in seconds per character
            
    Returns:
        AnimatedTextWidget instance
    """
    widget = AnimatedTextWidget(
        text_to_display=text,
        animation_style=style,
        animation_speed=speed
    )
    
    # Start animation after creation
    widget.animate_text()
    return widget


def get_ornamental_divider(style="classic", width=400):
    """
    Get an ornamental divider widget
    
    Args:
        style: Divider style ("classic", "floral", "simple")
        width: Width of the divider
            
    Returns:
        Widget with the ornamental divider
    """
    return DecorationManager.get_ornamental_divider(style, width)


def get_story_header(title, theme=None, width=500):
    """
    Get a decorative story header widget
    
    Args:
        title: Story title text
        theme: Optional theme name for styling
        width: Width of the header
            
    Returns:
        Widget with the story header
    """
    return DecorationManager.get_story_header(title, theme, width)


def get_seasonal_imagery(season, width=400, height=300):
    """
    Get a seasonal imagery widget
    
    Args:
        season: Season name ("spring", "summer", "autumn", "winter")
        width: Width of the image
        height: Height of the image
            
    Returns:
        Widget with seasonal imagery
    """
    return DecorationManager.get_seasonal_imagery(season, width, height)


if __name__ == "__main__":
    # Run the demo app if this module is executed directly
    VisualImageryApp().run()