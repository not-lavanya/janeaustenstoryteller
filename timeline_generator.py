"""
Timeline generator for the Jane Austen Storytelling Experience.
Provides functions to create a visual timeline of story events.
"""

import random
import time
import re
from datetime import datetime, timedelta

class TimelineGenerator:
    def __init__(self):
        """Initialize the TimelineGenerator"""
        self.characters = []
        self.seasons = {
            'spring': {'months': ['March', 'April', 'May'], 'activities': ['garden parties', 'country walks', 'early Season events']},
            'summer': {'months': ['June', 'July', 'August'], 'activities': ['balls', 'picnics', 'visits to Bath', 'seaside excursions']},
            'autumn': {'months': ['September', 'October', 'November'], 'activities': ['harvest festivals', 'hunting parties', 'assemblies']},
            'winter': {'months': ['December', 'January', 'February'], 'activities': ['Christmas celebrations', 'indoor gatherings', 'reading parties']}
        }
        self.regency_year = random.randint(1800, 1820)
        
    def extract_story_dates(self, story, season):
        """
        Extract key dates from the story or generate reasonable ones
        based on the season and story content.
        
        Args:
            story: The generated story text
            season: The season in which the story is set
        
        Returns:
            A list of date dictionaries with format:
            [{'date': 'Month Day, Year', 'event': 'Event description'}]
        """
        # Split story into paragraphs
        paragraphs = [p for p in story.split('\n') if p.strip()]
        
        # Select 5-7 significant paragraphs for timeline events
        num_events = random.randint(5, 7)
        significant_paragraphs = self._select_significant_paragraphs(paragraphs, num_events)
        
        # Create date range for the season
        months = self.seasons[season]['months']
        start_month = months[0]
        end_month = months[-1]
        
        start_date = datetime(self.regency_year, list(calendar_map.keys())[list(calendar_map.values()).index(start_month)], 1)
        end_date = datetime(self.regency_year, list(calendar_map.keys())[list(calendar_map.values()).index(end_month)], 28)
        date_range = (end_date - start_date).days
        
        # Generate events with dates
        events = []
        for idx, para_idx in enumerate(significant_paragraphs):
            # Generate a date within the season
            event_date = start_date + timedelta(days=int(idx * date_range / (num_events - 1)) if num_events > 1 else 0)
            month_name = calendar_map[event_date.month]
            day = event_date.day
            
            # Extract event description from paragraph
            event_desc = self._extract_event_from_paragraph(paragraphs[para_idx])
            
            # Format date in Regency style
            date_str = f"{month_name} {day}{self._get_day_suffix(day)}, {self.regency_year}"
            
            events.append({
                'date': date_str,
                'event': event_desc
            })
        
        # Add 1-2 additional season-appropriate events
        additional_events = self.generate_additional_events(season, num_events=2)
        for event in additional_events:
            # Generate random date within season
            days_offset = random.randint(0, date_range)
            event_date = start_date + timedelta(days=days_offset)
            month_name = calendar_map[event_date.month]
            day = event_date.day
            
            date_str = f"{month_name} {day}{self._get_day_suffix(day)}, {self.regency_year}"
            
            events.append({
                'date': date_str,
                'event': event
            })
        
        # Sort events by date
        events.sort(key=lambda x: self._parse_date(x['date']))
        
        return events
    
    def _parse_date(self, date_str):
        """Parse Regency-style date string into a datetime object for sorting"""
        # Extract month, day, year
        pattern = r"(\w+) (\d+)[a-z]{2}, (\d{4})"
        match = re.match(pattern, date_str)
        if match:
            month_str, day_str, year_str = match.groups()
            month = list(calendar_map.values()).index(month_str) + 1
            return datetime(int(year_str), month, int(day_str))
        return datetime(1800, 1, 1)  # fallback
        
    def _select_significant_paragraphs(self, paragraphs, num_events):
        """
        Select the most significant paragraphs from the story 
        to use as timeline events.
        
        Args:
            paragraphs: List of story paragraphs
            num_events: Number of events to select
        
        Returns:
            List of paragraph indices to use for events
        """
        # Skip introduction paragraphs and character descriptions
        start_idx = min(4, len(paragraphs) - 1)
        
        # Find paragraphs with character names or significant events
        significant_indices = []
        for i in range(start_idx, len(paragraphs)):
            # Check if paragraph contains character names or keywords
            para = paragraphs[i].lower()
            has_character = any(char.get('name', '').lower() in para for char in self.characters if 'name' in char)
            has_keywords = any(keyword in para for keyword in ['met', 'arrived', 'discovered', 'realized', 'confessed', 'revealed', 'ball', 'dance', 'party', 'letter', 'visit'])
            
            if has_character or has_keywords:
                significant_indices.append(i)
        
        # If we found enough significant paragraphs, select from those
        if len(significant_indices) >= num_events:
            # Ensure we have a good distribution of events through the story
            return self._distribute_events(significant_indices, num_events, len(paragraphs))
        
        # Otherwise, just distribute events throughout the story
        return self._distribute_events(list(range(start_idx, len(paragraphs))), num_events, len(paragraphs))
    
    def _distribute_events(self, candidate_indices, num_events, story_length):
        """
        Distribute events throughout the story to create a balanced timeline
        
        Args:
            candidate_indices: List of paragraph indices that are candidates for events
            num_events: Number of events to select
            story_length: Total number of paragraphs in the story
        
        Returns:
            List of selected paragraph indices
        """
        if len(candidate_indices) <= num_events:
            return candidate_indices
            
        # Divide story into sections and pick one event from each section
        section_size = story_length / num_events
        selected_indices = []
        
        for i in range(num_events):
            section_start = int(i * section_size)
            section_end = int((i + 1) * section_size)
            
            # Find candidates in this section
            section_candidates = [idx for idx in candidate_indices 
                                 if section_start <= idx < section_end]
            
            if section_candidates:
                selected_indices.append(random.choice(section_candidates))
            else:
                # If no candidates in this section, pick the closest one
                distances = [(abs(idx - (section_start + section_end)/2), idx) 
                             for idx in candidate_indices]
                distances.sort()
                selected_indices.append(distances[0][1])
                
        return selected_indices
        
    def _extract_event_from_paragraph(self, paragraph):
        """
        Extract a concise event description from a paragraph.
        
        Args:
            paragraph: A paragraph from the story
        
        Returns:
            A short event description
        """
        # If paragraph is too long, use the first sentence or truncate
        if len(paragraph) > 200:
            # Try to find the first sentence
            match = re.search(r'^(.+?[.!?])(?:\s|$)', paragraph)
            if match:
                first_sentence = match.group(1)
                if len(first_sentence) < 150:
                    return first_sentence
            
            # Truncate with ellipsis
            return paragraph[:150] + "..."
        
        return paragraph
    
    def _get_day_suffix(self, day):
        """Return the appropriate suffix for the day"""
        if 10 <= day % 100 <= 20:
            return 'th'
        else:
            return {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    
    def set_characters(self, characters):
        """
        Set the characters to be used in timeline generation.
        
        Args:
            characters: List of character dictionaries from the story
        """
        self.characters = characters
    
    def generate_additional_events(self, season, num_events=2):
        """
        Generate additional season-appropriate events to fill the timeline.
        
        Args:
            season: The season of the story
            num_events: Number of additional events to generate
        
        Returns:
            List of event descriptions
        """
        season_activities = self.seasons[season]['activities']
        
        # Generic Regency events
        generic_events = [
            "A letter arrives with unexpected news",
            "An important visitor calls at the house",
            "A misunderstanding leads to social awkwardness",
            "Rumors circulate about a new arrival in the neighborhood",
            "A chance encounter reveals new information",
            "A dinner party with distinguished guests",
            "A private conversation overheard by accident",
            "An invitation arrives for an upcoming social event",
            "A carriage ride with surprising revelations",
            "A walk in the grounds leads to an important decision"
        ]
        
        # Character-specific events if we have characters
        character_events = []
        if self.characters:
            for char in self.characters:
                if 'name' in char:
                    character_events.append(f"{char['name']} receives an unexpected invitation")
                    character_events.append(f"A revealing conversation with {char['name']}")
                    
        # Season-specific events
        season_events = []
        for activity in season_activities:
            season_events.append(f"Preparations begin for the {activity}")
            season_events.append(f"Attendance at the {activity} leads to new acquaintances")
            
        # Combine all potential events and select
        all_events = generic_events + character_events + season_events
        selected_events = random.sample(all_events, min(num_events, len(all_events)))
        
        return selected_events
    
    def format_timeline_ascii(self, events):
        """
        Format the timeline events as ASCII art.
        
        Args:
            events: List of event dictionaries with 'date' and 'event' keys
        
        Returns:
            ASCII art timeline as a string
        """
        if not events:
            return "No events to display in timeline."
            
        # Calculate the width needed for dates
        date_width = max(len(event['date']) for event in events) + 2
        
        # Create the timeline
        timeline = []
        
        for i, event in enumerate(events):
            date_part = f"{event['date']:>{date_width}}"
            
            # Format the connector line
            if i < len(events) - 1:
                connector = "│"
            else:
                connector = " "
                
            # Add the event line
            timeline.append(f"{date_part} ┬─ {event['event']}")
            
            # Add connector line if not the last event
            if i < len(events) - 1:
                timeline.append(f"{' ' * date_width} {connector}")
        
        return "\n".join(timeline)
    
    def generate_timeline(self, story, characters, season):
        """
        Generate a complete timeline for the story.
        
        Args:
            story: The generated story text
            characters: List of character dictionaries
            season: The season in which the story is set
        
        Returns:
            Formatted timeline as a string
        """
        # Set the characters for event generation
        self.set_characters(characters)
        
        # Extract or generate events
        events = self.extract_story_dates(story, season)
        
        # Format the timeline
        timeline = self.format_timeline_ascii(events)
        
        return timeline


# Month mapping (1=January, etc.)
calendar_map = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}