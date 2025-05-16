# Simplified Storyteller

A streamlined storytelling application that allows you to create stories on any theme with custom characters and settings.

## Features

- **Create stories on ANY theme**: Complete creative freedom to choose your theme
- **Enhanced character development**: Create detailed characters with virtues, flaws, and personal goals
- **Multiple narrative styles**: Choose from classic, dramatic, comedic, romantic, or mystery styles
- **Customizable settings**: Select or create custom locations, time periods, and seasons
- **Story editing**: Edit generated stories to add your personal touch
- **Multiple save formats**: Save stories as TXT, JSON, or HTML files
- **Custom storyboard support**: Save story data for future visualization

## How to Use

1. Run the storyteller:
   ```
   python simplified_storyteller.py
   ```

2. Follow the interactive prompts to:
   - Enter your story theme and description
   - Choose a narrative style
   - Select story settings (location, season, time period)
   - Create characters with specific traits
   - Set the story complexity level

3. The system will generate an initial story based on your inputs

4. You can edit the generated story if desired

5. Save your story in your preferred format (TXT, JSON, HTML)

6. Optionally export story data for custom visualization

## Custom Storyboard Viewer

The storyteller includes support for a custom storyboard viewer. When you choose the "Open custom storyboard" option, the system will:

1. Save your story data to a JSON file in the `temp` directory
2. Look for a file named `custom_storyboard_viewer.py` in the root directory
3. Launch the viewer if found

You can create your own `custom_storyboard_viewer.py` file to implement a custom visualization of your stories. The viewer should read from `temp/storyboard_data.json`.

## Saved Stories

All stories are saved in the `stories` directory with either:
- An auto-generated filename based on the current timestamp
- A custom filename that you provide

## Requirements

- Python 3.6 or later
- No external dependencies required

---

Enjoy creating your custom stories on any theme you can imagine!