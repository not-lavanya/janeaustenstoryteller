"""
Custom Storyboard Viewer
A basic viewer for visualizing story data from the Simplified Storyteller.
This template can be customized to create more sophisticated visualizations.
"""

import os
import json
import tkinter as tk
from tkinter import ttk, scrolledtext

class StoryboardViewer:
    def __init__(self, root, story_data):
        self.root = root
        self.story_data = story_data
        self.setup_ui()
        
    def setup_ui(self):
        # Configure the main window
        self.root.title(f"Story Viewer: {self.story_data['theme']['name']}")
        self.root.geometry("800x600")
        
        # Create a notebook with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Story tab
        self.story_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.story_frame, text="Story")
        self.setup_story_tab()
        
        # Characters tab
        self.characters_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.characters_frame, text="Characters")
        self.setup_characters_tab()
        
        # Settings tab
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")
        self.setup_settings_tab()
    
    def setup_story_tab(self):
        # Create a frame for the story title
        title_frame = ttk.Frame(self.story_frame)
        title_frame.pack(fill='x', padx=10, pady=10)
        
        # Create a title label
        title_label = ttk.Label(
            title_frame, 
            text=self.story_data['theme']['name'].upper(),
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=10)
        
        # Add theme description
        desc_label = ttk.Label(
            title_frame,
            text=self.story_data['theme']['description'],
            font=('Arial', 10, 'italic')
        )
        desc_label.pack(pady=5)
        
        # Create a scrolled text widget for the story content
        story_text = scrolledtext.ScrolledText(
            self.story_frame,
            wrap=tk.WORD,
            width=80,
            height=25,
            font=('Courier New', 10)
        )
        story_text.pack(fill='both', expand=True, padx=10, pady=10)
        story_text.insert(tk.END, self.story_data['story_text'])
        story_text.config(state='disabled')  # Make read-only
    
    def setup_characters_tab(self):
        # Add a canvas with scrollbar for many characters
        canvas = tk.Canvas(self.characters_frame)
        scrollbar = ttk.Scrollbar(self.characters_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add characters
        for i, character in enumerate(self.story_data['characters']):
            char_frame = ttk.LabelFrame(
                scrollable_frame,
                text=f"{character['name']} - {character['role']}"
            )
            char_frame.pack(fill='x', expand=True, padx=10, pady=5)
            
            # Character details
            details = [
                f"Gender: {character['gender']}",
                f"Virtue: {character['virtue']}",
                f"Flaw: {character['flaw']}",
                f"Goal: {character['goal']}",
                f"Backstory: {character['backstory']}"
            ]
            
            for detail in details:
                detail_label = ttk.Label(char_frame, text=detail, wraplength=700)
                detail_label.pack(anchor='w', padx=10, pady=2)
    
    def setup_settings_tab(self):
        # Create a frame for settings
        settings_container = ttk.Frame(self.settings_frame)
        settings_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Settings title
        settings_title = ttk.Label(
            settings_container,
            text="Story Settings",
            font=('Arial', 14, 'bold')
        )
        settings_title.pack(pady=10)
        
        # Settings details
        settings = self.story_data['settings']
        
        setting_details = [
            f"Location: {settings['location']}",
            f"Season: {settings['season']}",
            f"Time Period: {settings['time_period']}",
            f"Created: {self.story_data['timestamp']}"
        ]
        
        for detail in setting_details:
            detail_label = ttk.Label(
                settings_container,
                text=detail,
                font=('Arial', 12)
            )
            detail_label.pack(anchor='w', pady=5)
        
        # Additional information
        theme_frame = ttk.LabelFrame(settings_container, text="Theme Details")
        theme_frame.pack(fill='x', pady=20)
        
        theme_name = ttk.Label(
            theme_frame,
            text=f"Name: {self.story_data['theme']['name']}",
            font=('Arial', 11)
        )
        theme_name.pack(anchor='w', padx=10, pady=5)
        
        theme_desc = ttk.Label(
            theme_frame,
            text=f"Description: {self.story_data['theme']['description']}",
            font=('Arial', 11),
            wraplength=700
        )
        theme_desc.pack(anchor='w', padx=10, pady=5)


def load_story_data():
    """Load story data from the JSON file"""
    temp_file = os.path.join('temp', 'storyboard_data.json')
    
    if not os.path.exists(temp_file):
        print(f"Error: Story data file not found at {temp_file}")
        return None
    
    try:
        with open(temp_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading story data: {e}")
        return None


def main():
    # Load story data
    story_data = load_story_data()
    
    if not story_data:
        print("Could not load story data. Please generate a story first.")
        return
    
    # Create the main window
    root = tk.Tk()
    app = StoryboardViewer(root, story_data)
    
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()