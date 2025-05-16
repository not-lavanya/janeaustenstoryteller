"""
Character generation for the Jane Austen storytelling experience.
"""

import random

class CharacterGenerator:
    def __init__(self):
        # Initialize character traits dictionaries
        self.first_names = {
            'female': [
                'Elizabeth', 'Jane', 'Emma', 'Anne', 'Catherine', 'Elinor',
                'Marianne', 'Charlotte', 'Caroline', 'Georgiana', 'Harriet',
                'Lydia', 'Mary', 'Fanny', 'Isabella', 'Eleanor', 'Sophia'
            ],
            'male': [
                'Fitzwilliam', 'Charles', 'George', 'Henry', 'Edward', 'William',
                'Frederick', 'John', 'Thomas', 'James', 'Edmund', 'Robert',
                'Christopher', 'Frank', 'Philip', 'Richard', 'Arthur'
            ]
        }
        
        self.last_names = [
            'Bennet', 'Darcy', 'Bingley', 'Woodhouse', 'Knightley', 'Wentworth',
            'Elliot', 'Crawford', 'Bertram', 'Dashwood', 'Ferrars', 'Willoughby',
            'Brandon', 'Collins', 'Lucas', 'Tilney', 'Morland', 'Churchill',
            'Elton', 'Fairfax', 'Musgrove', 'Croft', 'Wickham', 'Thorpe'
        ]
        
        self.social_classes = {
            'upper': [
                'wealthy landowner', 'aristocrat', 'baronet', 'heir to a large estate',
                'person of noble birth', 'member of the peerage', 'lady of rank',
                'gentleman of fortune', 'distinguished lady of society'
            ],
            'middle': [
                'country gentleman', 'refined lady', 'respected tradesman',
                'gentleman of modest means', 'daughter of a merchant',
                'professional man', 'wife of a professional man', 'governess from a good family'
            ],
            'lower': [
                'tenant farmer', 'shopkeeper', 'craftsman', 'servant in a great house',
                'person of humble birth but good connections', 'tradesperson',
                'farmer with a small holding', 'lady\'s companion'
            ]
        }
        
        self.occupations = {
            'male': [
                'clergyman', 'naval officer', 'estate manager', 'physician',
                'barrister', 'military officer', 'magistrate', 'scholar',
                'landowner', 'merchant', 'banker', 'architect', 'gentleman farmer'
            ],
            'female': [
                'governess', 'lady\'s companion', 'accomplished musician',
                'skilled painter', 'estate mistress', 'household manager',
                'charitable worker', 'writer of letters and journals',
                'needlework expert', 'housekeeper', 'hostess of social gatherings'
            ],
            'neutral': [
                'guardian of younger siblings', 'caretaker of elderly relatives',
                'correspondent with distant connections', 'reader and intellectual',
                'manager of family affairs', 'local benefactor', 'traveler'
            ]
        }
        
        self.personality_traits = {
            'positive': [
                'witty', 'intelligent', 'amiable', 'sensible', 'charming',
                'composed', 'elegant', 'gracious', 'kind-hearted', 'refined',
                'accomplished', 'spirited', 'thoughtful', 'affectionate', 'dutiful'
            ],
            'neutral': [
                'reserved', 'private', 'contemplative', 'traditional', 'careful',
                'proper', 'conventional', 'practical', 'deliberate', 'methodical',
                'observant', 'attentive', 'modest', 'temperate', 'moderate'
            ],
            'negative': [
                'proud', 'prejudiced', 'vain', 'impulsive', 'indiscreet',
                'fanciful', 'gossiping', 'imposing', 'scheming', 'calculating',
                'envious', 'pompous', 'frivolous', 'flirtatious', 'insolent'
            ]
        }
        
        self.backstories = [
            "raised in a large family with little fortune but much affection",
            "educated abroad and recently returned to England",
            "orphaned at a young age and raised by a distant relative",
            "from a family fallen on hard times after previous prosperity",
            "seeking to restore family honor after a scandal",
            "the unexpected inheritor of a modest but comfortable property",
            "connected to influential people but personally of limited means",
            "having survived a serious illness that altered their perspective on life",
            "returned from the colonies with experiences but diminished fortune",
            "well-traveled but now settling into provincial society",
            "recovering from a broken engagement that caused much distress",
            "new to the neighborhood and subject to much speculation",
            "a childhood friend of an important local figure",
            "possessing a talent that sets them apart from typical society",
            "bearing a resemblance to someone of notorious reputation"
        ]

    def generate_regency_name(self, gender=None):
        """Generate a typical Regency era name"""
        if gender is None:
            gender = random.choice(['male', 'female'])
            
        first_name = random.choice(self.first_names[gender])
        last_name = random.choice(self.last_names)
        
        return f"{first_name} {last_name}"

    def create_character(self, gender=None, custom_name=None, include_backstory=True):
        """Generate a period-appropriate character"""
        # Randomly select gender if not specified
        if gender is None:
            gender = random.choice(['male', 'female'])
            
        # Generate name if not provided
        if custom_name:
            name = custom_name
        else:
            name = self.generate_regency_name(gender)
            
        # Select social class and appropriate occupation
        social_class_category = random.choice(['upper', 'middle', 'lower'])
        social_class = random.choice(self.social_classes[social_class_category])
        
        # Select occupation based on gender or use a neutral one
        if random.random() < 0.7:  # 70% chance of gender-specific occupation
            if gender in self.occupations:
                occupation = random.choice(self.occupations[gender])
            else:
                occupation = random.choice(self.occupations['neutral'])
        else:
            occupation = random.choice(self.occupations['neutral'])
            
        # Select personality traits
        personality_category = random.choice(['positive', 'neutral', 'negative'])
        personality = random.choice(self.personality_traits[personality_category])
        
        # Create the character dictionary
        character = {
            'name': name,
            'gender': gender,
            'social_class': social_class,
            'occupation': occupation,
            'personality': personality
        }
        
        # Add backstory if requested
        if include_backstory:
            character['backstory'] = random.choice(self.backstories)
            
        return character
