# Jane Austen Storytelling Experience

A sophisticated Python-powered storytelling application that recreates Jane Austen's narrative style through advanced generative and interactive technologies.

## 📖 Overview

This project provides an immersive Jane Austen-inspired storytelling experience with the following features:

- **Interactive Storytelling**: Generate custom narratives in the style of Jane Austen
- **Character Generation**: Create period-appropriate characters with detailed backgrounds
- **Visual Story Timeline**: Track key events in your generated stories with a visual timeline
- **Narrative Complexity Slider**: Adjust the complexity of generated narratives (1-3 levels)
- **Jane Austen Quote Generator**: Access authentic quotes with contextual insights
- **Visual Imagery**: ASCII art representations of locations, characters, events, and decorative frames
- **Enhanced Quote Display**: Multiple quote display styles including themed frames and animated text
- **Regency Letter Writing Assistant**: Compose letters in the style of Jane Austen's era
- **Regency Name Dictionary**: Explore period-appropriate names with meanings and context

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Required packages: (No external dependencies required for core functionality)

### Installation

1. Clone this repository or download the files:
   ```
   git clone https://github.com/yourusername/jane-austen-storyteller.git
   ```
   
2. Navigate to the project directory:
   ```
   cd jane-austen-storyteller
   ```

3. Run the main experience (text-only version, works in all environments):
   ```
   python text_only_experience.py
   ```
   
   Or run with enhanced visual elements (requires graphical environment):
   ```
   python run_kivy_demo.py
   ```

## 📚 Main Features

### 1. Jane Austen Storytelling Experience

Generate complete narratives in the style of Jane Austen with:

- 8 different story themes (or create your own)
- Customizable characters
- Multiple settings and seasons
- Three levels of narrative complexity
- Visual timeline of story events
- Character portraits

To run just the storyteller:
```
python jane_austen_storyteller.py
```

### 2. Custom Theme Storyteller

Create stories based on any theme you provide:

- Enter any custom theme (e.g., "unexpected inheritance", "mistaken identity")
- Select narrative complexity level
- Generate a complete story with characters, setting, and plot
- See visual representations of locations and characters

To run the custom theme storyteller:
```
python custom_theme_storyteller.py
```

### 3. Jane Austen Quote Generator

Access a collection of authentic Jane Austen quotes with:

- Contextual insights about each quote
- Thematic organization
- Source information
- Visual presentation with three display styles:
  - Standard decorative frames
  - Theme-specific ornamental frames
  - Animated text display (character-by-character)
- Ability to match quotes to specific narrative themes

To run just the quote generator:
```
python austen_quotes_demo.py
```

### 4. Visual Imagery Features

The application includes rich visual elements:

- Location illustrations for different settings and seasons
- Character portraits based on gender and personality
- Event illustrations for key moments in stories
- Decorative story headers with thematic styling
- Ornamental dividers in various styles (classic, floral, simple)
- Themed quote frames with motifs matching the quote's theme
- Animated text effects for immersive storytelling

These visual elements enhance the storytelling experience by creating an immersive Regency-era atmosphere.

### 5. Regency-Era Text Animations

The application features animated text transitions that mimic Regency-era writing styles:

- **Quill Writing Effect**: Simulates the variable pace and ink saturation of writing with a quill pen
- **Formal Writing Transitions**: Mimics the deliberate pace and flourishes of Regency-era handwritten correspondence
- **Animated Scene Transitions**: Creates visual breaks between narrative locations with period-appropriate phrasing
- **Animated Chapter Headings**: Displays chapter numbers in Roman numerals with decorative frames
- **Animated Dialogue**: Presents character speech with appropriate pacing and action descriptions
- **Social Commentary Animation**: Presents Austen-style social observations with distinctive formatting
- **Narration Styles**: Multiple narration styles (standard, dramatic, reflective) with appropriate pacing
- **Regency Letter Formatting**: Animated display of period-appropriate letter writing conventions

These animations work in any environment, including terminals without graphical capabilities.

### 6. Regency Letter Writing Assistant

Compose letters in the style of Jane Austen's era:

- Multiple letter types (invitation, congratulations, apology, etc.)
- Formal and informal options
- Period-appropriate salutations and closings
- Seasonal references
- Save as text files

To use the letter writing assistant:
```
python letter_writing_assistant.py
```

### 7. Regency Name Dictionary

Explore names from Jane Austen's era:

- First names with meanings and popularity information
- Surnames with origin and social status context
- Character name generation
- Search functionality
- Reference to usage in Austen's works

To use the name dictionary:
```
python regency_name_dictionary.py
```

## 🧩 Module Structure

### Core Modules
- `austen_experience.py` - Main menu system for accessing all features
- `text_only_experience.py` - Text-only version of the experience (works in all environments)
- `jane_austen_storyteller.py` - Comprehensive storyteller with all features
- `austen_storyteller.py` - Simplified storyteller version
- `custom_theme_storyteller.py` - Generate stories based on custom themes
- `character_generator.py` - Period-appropriate character creation
- `timeline_generator.py` - Visual story timeline generation
- `story_templates.py` - Austen-inspired story templates
- `austen_quotes.py` - Quote generator with contextual insights
- `austen_quotes_demo.py` - Standalone demo for quote generator
- `utils.py` - General utility functions

### Visual and Animation Modules
- `regency_text_animations.py` - Text animations that mimic Regency-era writing styles
- `text_animations_demo.py` - Demonstration of text animation capabilities
- `visual_imagery.py` - ASCII art for locations, characters, events, and decorative elements
- `kivy_visual_imagery.py` - Enhanced visual elements using Kivy GUI framework
- `run_kivy_demo.py` - Demonstration of Kivy-based visual imagery (requires graphics support)

### Additional Features
- `letter_writing_assistant.py` - Regency-era letter composition
- `regency_name_dictionary.py` - Period name reference and generation

## 🌟 Running the Project on Google Colab

To run the project on Google Colab:

1. Create a new Colab notebook
2. Add this code to install dependencies (only pygame is required for text-only mode):
   ```python
   !pip install pygame
   ```
   
   If you want to run with Kivy visual elements (optional):
   ```python
   !pip install pygame kivy
   ```

3. Upload all code files using this helper:
   ```python
   from google.colab import files
   import os

   # Create a function to receive uploaded files
   def upload_files():
       uploaded = files.upload()
       print("Files uploaded successfully!")
       return list(uploaded.keys())

   # Run this function to upload files
   upload_files()
   ```

4. Run the program with the text-only version (works in all environments):
   ```python
   !python text_only_experience.py
   ```

   Or try running with visual elements (may require extra configuration):
   ```python
   !python austen_experience.py
   ```

## 🎨 Customizing Themes

When using the custom theme storyteller, you can input any theme and the system will generate a coherent narrative around it. Some theme ideas:

- Social advancement
- Hidden identity
- Family obligations
- Lost inheritance
- Forbidden friendship
- Rural vs. city life
- Artistic pursuits
- Military career
- Educational aspirations
- Religious devotion

## 📝 Example Usage

### Creating a Story with a Custom Theme

```python
from custom_theme_storyteller import CustomThemeStoryGenerator

# Create the generator
generator = CustomThemeStoryGenerator()

# Generate a story with a custom theme
story, elements = generator.generate_story("unexpected inheritance", complexity_level=2)

# Print the story
print(story)
```

### Getting a Thematic Quote

```python
from austen_quotes import AustenQuoteGenerator

# Create the quote generator
quote_generator = AustenQuoteGenerator()

# Get a quote by theme
quote = quote_generator.get_quote_by_theme("love")

# Format and print the quote with context
print(quote_generator.format_quote_with_insight(quote))
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the works of Jane Austen
- Created as an homage to Regency-era literature and culture