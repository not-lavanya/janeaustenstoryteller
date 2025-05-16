"""
Jane Austen Quote Generator with Contextual Insights
This module provides authentic Jane Austen quotes with background information.
"""

import random

class AustenQuoteGenerator:
    def __init__(self):
        """Initialize the quote database with authentic Jane Austen quotes and insights"""
        
        # Dictionary of quotes from Jane Austen's major works
        # Each quote includes:
        # - text: The actual quote
        # - source: Book name
        # - context: Background information about the quote
        # - theme: Thematic category
        self.quotes = [
            # Pride and Prejudice
            {
                "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
                "source": "Pride and Prejudice (1813)",
                "context": "The famous opening line that ironically establishes the marriage theme while subtly mocking social expectations.",
                "theme": "marriage"
            },
            {
                "text": "I could easily forgive his pride, if he had not mortified mine.",
                "source": "Pride and Prejudice (1813)",
                "context": "Elizabeth Bennet speaking about Mr. Darcy after their first meeting, highlighting the novel's exploration of pride as a character flaw.",
                "theme": "pride"
            },
            {
                "text": "In vain have I struggled. It will not do. My feelings will not be repressed. You must allow me to tell you how ardently I admire and love you.",
                "source": "Pride and Prejudice (1813)",
                "context": "Mr. Darcy's first proposal to Elizabeth Bennet, showing his internal conflict between love and social considerations.",
                "theme": "love"
            },
            {
                "text": "I was in the middle before I knew that I had begun.",
                "source": "Pride and Prejudice (1813)",
                "context": "Mr. Darcy explaining to Elizabeth how he fell in love with her, illustrating how love often develops unconsciously.",
                "theme": "love"
            },
            {
                "text": "For what do we live, but to make sport for our neighbours, and laugh at them in our turn?",
                "source": "Pride and Prejudice (1813)",
                "context": "Mr. Bennet's cynical yet humorous philosophy on life, showing Austen's wit and social commentary.",
                "theme": "society"
            },
            
            # Sense and Sensibility
            {
                "text": "The more I know of the world, the more I am convinced that I shall never see a man whom I can really love.",
                "source": "Sense and Sensibility (1811)",
                "context": "Marianne Dashwood expressing her romantic idealism, which will be challenged throughout the novel.",
                "theme": "love"
            },
            {
                "text": "Know your own happiness. You want nothing but patience—or give it a more fascinating name, call it hope.",
                "source": "Sense and Sensibility (1811)",
                "context": "Mrs. Dashwood's advice, representing the novel's theme of finding a balance between emotional sensibility and rational sense.",
                "theme": "wisdom"
            },
            {
                "text": "I will be calm. I will be mistress of myself.",
                "source": "Sense and Sensibility (1811)",
                "context": "Elinor Dashwood demonstrating her commitment to self-control and social propriety despite emotional turmoil.",
                "theme": "self-control"
            },
            
            # Emma
            {
                "text": "I may have lost my heart, but not my self-control.",
                "source": "Emma (1815)",
                "context": "Emma's internal struggle between romantic feelings and maintaining her composure, showing Austen's focus on balance.",
                "theme": "self-control"
            },
            {
                "text": "Seldom, very seldom, does complete truth belong to any human disclosure; seldom can it happen that something is not a little disguised or a little mistaken.",
                "source": "Emma (1815)",
                "context": "The narrator's insight on human communication, reflecting the novel's theme of misunderstanding and limited perception.",
                "theme": "perception"
            },
            {
                "text": "There are people, who the more you do for them, the less they will do for themselves.",
                "source": "Emma (1815)",
                "context": "Mr. Woodhouse's observation that ironically applies to Emma herself, who meddles in others' lives.",
                "theme": "character"
            },
            
            # Persuasion
            {
                "text": "You pierce my soul. I am half agony, half hope. Tell me not that I am too late.",
                "source": "Persuasion (1817)",
                "context": "Captain Wentworth's passionate letter to Anne Elliot, considered one of literature's most romantic declarations.",
                "theme": "love"
            },
            {
                "text": "All the privilege I claim for my own sex is that of loving longest, when existence or when hope is gone!",
                "source": "Persuasion (1817)",
                "context": "Anne Elliot defending women's constancy in love during a discussion about literature, reflecting her own situation.",
                "theme": "gender"
            },
            {
                "text": "Time will explain it all. He is a talker, and needs no questioning before he speaks.",
                "source": "Persuasion (1817)",
                "context": "A comment on patience and how truth reveals itself naturally, a central theme as Anne waits for resolution.",
                "theme": "patience"
            },
            
            # Mansfield Park
            {
                "text": "Let other pens dwell on guilt and misery.",
                "source": "Mansfield Park (1814)",
                "context": "The narrator rejecting prolonged suffering in favor of resolution, showing Austen's narrative approach.",
                "theme": "writing"
            },
            {
                "text": "We have all a better guide in ourselves, if we would attend to it, than any other person can be.",
                "source": "Mansfield Park (1814)",
                "context": "Fanny Price's insight on moral guidance, emphasizing the novel's focus on personal integrity over social pressure.",
                "theme": "integrity"
            },
            {
                "text": "A large income is the best recipe for happiness I ever heard of.",
                "source": "Mansfield Park (1814)",
                "context": "Mary Crawford's materialistic view that Austen presents ironically to contrast with Fanny's moral values.",
                "theme": "wealth"
            },
            
            # Northanger Abbey
            {
                "text": "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
                "source": "Northanger Abbey (1817)",
                "context": "The narrator defending novel reading, showing Austen's self-awareness as a novelist and her critique of literary snobbery.",
                "theme": "literature"
            },
            {
                "text": "There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.",
                "source": "Northanger Abbey (1817)",
                "context": "Isabella Thorpe claiming loyalty while actually behaving opportunistically, demonstrating Austen's irony.",
                "theme": "friendship"
            },
            {
                "text": "If adventures will not befall a young lady in her own village, she must seek them abroad.",
                "source": "Northanger Abbey (1817)",
                "context": "The narrator commenting on Catherine Morland's desire for gothic excitement, gently mocking romantic imagination.",
                "theme": "imagination"
            },
            
            # Letters and General Wisdom
            {
                "text": "I do not want people to be very agreeable, as it saves me the trouble of liking them a great deal.",
                "source": "Letter to Cassandra Austen (1798)",
                "context": "Jane Austen's personal correspondence revealing her witty and sometimes cynical approach to social relationships.",
                "theme": "society"
            },
            {
                "text": "One half of the world cannot understand the pleasures of the other.",
                "source": "Emma (1815)",
                "context": "A reflection on how different people find happiness in different things, showing Austen's understanding of human diversity.",
                "theme": "human nature"
            },
            {
                "text": "Happiness in marriage is entirely a matter of chance.",
                "source": "Pride and Prejudice (1813)",
                "context": "Charlotte Lucas's pragmatic view of marriage that contrasts with the novel's ultimate emphasis on compatibility and respect.",
                "theme": "marriage"
            },
            {
                "text": "Run mad as often as you choose, but do not faint.",
                "source": "Letter to Martha Lloyd (1804)",
                "context": "Austen's humorous advice reflecting her preference for active emotional expression over passive helplessness.",
                "theme": "self-expression"
            },
            {
                "text": "Life seems but a quick succession of busy nothings.",
                "source": "Mansfield Park (1814)",
                "context": "A commentary on the mundane social activities that nonetheless form the fabric of Regency life.",
                "theme": "society"
            }
        ]
        
        # Organize quotes by theme for targeted retrieval
        self.theme_index = {}
        for i, quote in enumerate(self.quotes):
            theme = quote["theme"]
            if theme not in self.theme_index:
                self.theme_index[theme] = []
            self.theme_index[theme].append(i)
    
    def get_random_quote(self):
        """Return a random Jane Austen quote with context"""
        return random.choice(self.quotes)
    
    def get_quote_by_theme(self, theme):
        """Return a quote related to a specific theme"""
        if theme in self.theme_index and self.theme_index[theme]:
            quote_idx = random.choice(self.theme_index[theme])
            return self.quotes[quote_idx]
        else:
            # Fallback if theme not found
            return self.get_random_quote()
    
    def get_quote_by_source(self, source):
        """Return a quote from a specific Jane Austen work"""
        matching_quotes = [q for q in self.quotes if source.lower() in q["source"].lower()]
        if matching_quotes:
            return random.choice(matching_quotes)
        else:
            # Fallback if source not found
            return self.get_random_quote()
    
    def get_thematic_quote_for_narrative(self, narrative_text, default_theme="love"):
        """
        Analyze a narrative and return a thematically relevant quote
        
        Args:
            narrative_text: The story text to analyze
            default_theme: Fallback theme if no clear match is found
        
        Returns:
            A quote dictionary with text, source, and context
        """
        # Simple keyword matching for themes
        theme_keywords = {
            "love": ["love", "affection", "heart", "ardent", "admire", "attachment"],
            "marriage": ["marriage", "matrimony", "proposal", "wedded", "husband", "wife", "match"],
            "pride": ["pride", "vanity", "conceit", "superiority", "dignity", "honor"],
            "society": ["society", "manners", "propriety", "reputation", "status", "connections"],
            "self-control": ["control", "compose", "restrain", "patience", "temper", "discipline"],
            "wisdom": ["wisdom", "sense", "prudence", "judgment", "understanding", "knowledge"],
            "perception": ["perceive", "observe", "notice", "discern", "impression", "opinion"],
            "character": ["character", "disposition", "nature", "temperament", "quality", "virtue"],
            "integrity": ["integrity", "principle", "moral", "honest", "upright", "conscience"],
            "wealth": ["wealth", "fortune", "money", "income", "rich", "poor", "poverty"],
            "friendship": ["friend", "companion", "acquaintance", "intimacy", "connection"],
            "gender": ["woman", "man", "lady", "gentleman", "feminine", "masculine", "female", "male"],
            "patience": ["patience", "wait", "endure", "persevere", "forbearance"],
            "imagination": ["imagination", "fancy", "dream", "envision", "conjure"]
        }
        
        # Count theme keyword occurrences
        theme_counts = {theme: 0 for theme in theme_keywords}
        narrative_lower = narrative_text.lower()
        
        for theme, keywords in theme_keywords.items():
            for keyword in keywords:
                theme_counts[theme] += narrative_lower.count(keyword)
        
        # Find the dominant theme(s)
        max_count = max(theme_counts.values())
        if max_count > 0:
            # Get all themes with the maximum count
            dominant_themes = [theme for theme, count in theme_counts.items() if count == max_count]
            selected_theme = random.choice(dominant_themes)
        else:
            # No clear theme detected, use default
            selected_theme = default_theme
        
        # Get a quote matching the selected theme
        return self.get_quote_by_theme(selected_theme)
    
    def format_quote_with_insight(self, quote, include_context=True):
        """Format a quote with its contextual information"""
        formatted = f"\n\"{quote['text']}\"\n— {quote['source']}"
        
        if include_context:
            formatted += f"\n\nInsight: {quote['context']}"
            
        return formatted
    
    def get_available_themes(self):
        """Return a list of all available quote themes"""
        return sorted(list(self.theme_index.keys()))
    
    def get_available_sources(self):
        """Return a list of all available Jane Austen works"""
        sources = set()
        for quote in self.quotes:
            # Extract just the book title without the year
            book_title = quote["source"].split("(")[0].strip()
            sources.add(book_title)
        return sorted(list(sources))


# For testing purposes
if __name__ == "__main__":
    quote_gen = AustenQuoteGenerator()
    
    print("Random quote:")
    random_quote = quote_gen.get_random_quote()
    print(quote_gen.format_quote_with_insight(random_quote))
    
    print("\nLove-themed quote:")
    love_quote = quote_gen.get_quote_by_theme("love")
    print(quote_gen.format_quote_with_insight(love_quote))
    
    print("\nQuote from Emma:")
    emma_quote = quote_gen.get_quote_by_source("Emma")
    print(quote_gen.format_quote_with_insight(emma_quote))
    
    print("\nAvailable themes:")
    print(", ".join(quote_gen.get_available_themes()))
    
    print("\nAvailable sources:")
    print(", ".join(quote_gen.get_available_sources()))
    
    # Test thematic matching with a sample narrative
    test_narrative = """
    The heart that truly loves never forgets. Despite years of separation, 
    her feelings remained constant, though she had accepted that happiness in marriage
    might never be hers. Society might judge her choice harshly, but she would 
    maintain her composure and dignity regardless.
    """
    
    print("\nThematically matched quote for narrative:")
    matched_quote = quote_gen.get_thematic_quote_for_narrative(test_narrative)
    print(quote_gen.format_quote_with_insight(matched_quote))
    print(f"Detected theme: {matched_quote['theme']}")