"""
Display Images for Storyteller

This file is opened by the simplified_storyteller.py when the user selects
the "Open Storyboard" option. It reads story data from a JSON file and
displays it in a visual format.
"""

import os
import json
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox
from tkinter import font as tkfont

class DisplayImages:
    def __init__(self, root, story_data):
        self.root = root
        self.story_data = story_data
        self.root.title(f"Story Visualization: {story_data['theme']['name']}")
        self.root.geometry("900x700")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Georgia", 11))
        self.style.configure("Header.TLabel", font=("Georgia", 16, "bold"))
        self.style.configure("Subhead.TLabel", font=("Georgia", 14))
        self.style.configure("Title.TLabel", font=("Georgia", 20, "bold"))
        
        # Create the main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_storyboard()
    
    def create_storyboard(self):
        """Create the storyboard visualization"""
        # Story title
        ttk.Label(
            self.main_frame, 
            text=self.story_data['theme']['name'].upper(),
            style="Title.TLabel"
        ).pack(pady=(0, 20))
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        story_tab = ttk.Frame(notebook, padding=10)
        characters_tab = ttk.Frame(notebook, padding=10)
        settings_tab = ttk.Frame(notebook, padding=10)
        
        notebook.add(story_tab, text="Story")
        notebook.add(characters_tab, text="Characters")
        notebook.add(settings_tab, text="Settings")
        
        # Fill story tab
        self.create_story_tab(story_tab)
        
        # Fill characters tab
        self.create_characters_tab(characters_tab)
        
        # Fill settings tab
        self.create_settings_tab(settings_tab)
    
    def create_story_tab(self, parent):
        """Create the story visualization tab"""
        # Theme description
        desc_frame = ttk.Frame(parent)
        desc_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(
            desc_frame, 
            text="Theme Description:",
            style="Subhead.TLabel"
        ).pack(anchor=tk.W)
        
        ttk.Label(
            desc_frame, 
            text=self.story_data['theme']['description'],
            wraplength=800
        ).pack(anchor=tk.W, padx=10)
        
        # Story text with scrollbars
        story_frame = ttk.LabelFrame(parent, text="Story")
        story_frame.pack(fill=tk.BOTH, expand=True)
        
        story_text = scrolledtext.ScrolledText(
            story_frame,
            wrap=tk.WORD,
            font=("Georgia", 11),
            padx=10,
            pady=10
        )
        story_text.pack(fill=tk.BOTH, expand=True)
        story_text.insert(tk.END, self.story_data['story_text'])
        story_text.config(state=tk.DISABLED)  # Read-only
    
    def create_characters_tab(self, parent):
        """Create the characters visualization tab"""
        characters = self.story_data['characters']
        
        # Create a canvas with scrollbar for many characters
        canvas_frame = ttk.Frame(parent)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create a frame inside the canvas for content
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)
        
        # Add characters to the content frame
        for i, character in enumerate(characters):
            char_frame = ttk.LabelFrame(
                content_frame,
                text=character['name']
            )
            char_frame.pack(fill=tk.X, padx=5, pady=10, ipady=5)
            
            # Character visualization
            self.create_character_box(char_frame, character)
        
        # Update scroll region when content size changes
        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
    def create_character_box(self, parent, character):
        """Create a visual box for a character"""
        # Role
        ttk.Label(
            parent, 
            text=f"Role: {character['role']}",
            font=("Georgia", 12, "bold")
        ).pack(anchor=tk.W, padx=10, pady=(5, 0))
        
        # Portrait "frame"
        portrait_frame = ttk.Frame(parent, borderwidth=2, relief="solid")
        portrait_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Add character details in a grid
        grid_frame = ttk.Frame(portrait_frame)
        grid_frame.pack(padx=10, pady=10, fill=tk.X)
        
        # Row 1: Gender
        ttk.Label(grid_frame, text="Gender:", width=10).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Label(grid_frame, text=character['gender']).grid(row=0, column=1, sticky=tk.W, pady=2)
        
        # Row 2: Virtue
        ttk.Label(grid_frame, text="Virtue:", width=10).grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(grid_frame, text=character['virtue']).grid(row=1, column=1, sticky=tk.W, pady=2)
        
        # Row 3: Flaw
        ttk.Label(grid_frame, text="Flaw:", width=10).grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Label(grid_frame, text=character['flaw']).grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Row 4: Goal
        ttk.Label(grid_frame, text="Goal:", width=10).grid(row=3, column=0, sticky=tk.W, pady=2)
        ttk.Label(grid_frame, text=character['goal']).grid(row=3, column=1, sticky=tk.W, pady=2)
        
        # Row 5: Backstory
        ttk.Label(grid_frame, text="Backstory:", width=10).grid(row=4, column=0, sticky=tk.NW, pady=2)
        backstory_label = ttk.Label(grid_frame, text=character['backstory'], wraplength=500)
        backstory_label.grid(row=4, column=1, sticky=tk.W, pady=2)
    
    def create_settings_tab(self, parent):
        """Create the settings visualization tab"""
        settings = self.story_data['settings']
        
        # Create a frame for settings
        settings_frame = ttk.Frame(parent)
        settings_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add settings header
        ttk.Label(
            settings_frame, 
            text="Story Settings",
            style="Header.TLabel"
        ).pack(anchor=tk.W, pady=(0, 20))
        
        # Create a stylized frame for settings
        details_frame = ttk.Frame(settings_frame, borderwidth=2, relief="groove")
        details_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Location
        location_frame = ttk.Frame(details_frame)
        location_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(
            location_frame, 
            text="Location:",
            width=15,
            font=("Georgia", 12, "bold")
        ).pack(side=tk.LEFT)
        
        ttk.Label(
            location_frame, 
            text=settings['location'],
            font=("Georgia", 12)
        ).pack(side=tk.LEFT)
        
        # Season
        season_frame = ttk.Frame(details_frame)
        season_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(
            season_frame, 
            text="Season:",
            width=15,
            font=("Georgia", 12, "bold")
        ).pack(side=tk.LEFT)
        
        ttk.Label(
            season_frame, 
            text=settings['season'],
            font=("Georgia", 12)
        ).pack(side=tk.LEFT)
        
        # Time Period
        period_frame = ttk.Frame(details_frame)
        period_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(
            period_frame, 
            text="Time Period:",
            width=15,
            font=("Georgia", 12, "bold")
        ).pack(side=tk.LEFT)
        
        ttk.Label(
            period_frame, 
            text=settings['time_period'],
            font=("Georgia", 12)
        ).pack(side=tk.LEFT)
        
        # Add timestamp
        timestamp_frame = ttk.Frame(settings_frame)
        timestamp_frame.pack(fill=tk.X, padx=5, pady=20)
        
        ttk.Label(
            timestamp_frame, 
            text=f"Story created: {self.story_data['timestamp']}",
            font=("Georgia", 10, "italic")
        ).pack(anchor=tk.E)
        
        # Export options
        export_frame = ttk.LabelFrame(settings_frame, text="Export Options")
        export_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(
            export_frame,
            text="Export as HTML",
            command=self.export_as_html
        ).pack(side=tk.LEFT, padx=10, pady=10)
        
        ttk.Button(
            export_frame,
            text="Export as PDF",
            command=self.export_as_pdf
        ).pack(side=tk.LEFT, padx=10, pady=10)
    
    def export_as_html(self):
        """Export story as HTML"""
        messagebox.showinfo(
            "Export Information", 
            "HTML export feature will be implemented in a future version."
        )
    
    def export_as_pdf(self):
        """Export story as PDF"""
        messagebox.showinfo(
            "Export Information", 
            "PDF export feature will be implemented in a future version."
        )


def load_story_data():
    """Load story data from the JSON file"""
    temp_file = os.path.join('temp', 'storyboard_data.json')
    
    if not os.path.exists(temp_file):
        return None
    
    try:
        with open(temp_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading story data: {e}")
        return None


def main():
    """Main function"""
    # Load story data
    story_data = load_story_data()
    
    if not story_data:
        print("No story data found. Please generate a story first.")
        return
    
    # Create the main window
    root = tk.Tk()
    app = DisplayImages(root, story_data)
    
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()