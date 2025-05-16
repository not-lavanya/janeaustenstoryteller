"""
Story templates and themes for the Jane Austen storytelling experience.
"""

def get_story_themes():
    """Return the list of available story themes"""
    return [
        'Romantic Courtship in Bath',
        'Social Intrigue in Country Estate',
        'Marriage Prospects in Regency England',
        'Inheritance and Social Mobility',
        'Family Honor and Reputation',
        'Provincial Life and London Society',
        'Lost Love Rekindled',
        'Secret Engagement Revealed'
    ]

def get_story_templates():
    """Return the dictionary of story templates for each theme"""
    return {
        'Romantic Courtship in Bath': """
In {season} of {time_period}, {protagonist_name}, a {protagonist_personality} {protagonist_social_class}, arrives in Bath for the social season. 
The routine of taking the waters and attending assemblies seems mundane until a chance encounter with {character1_name}, a {character1_personality} {character1_occupation}.

Their initial meeting at the Pump Room sparks both intrigue and misunderstanding. {protagonist_name}'s {protagonist_personality} nature clashes with {character1_name}'s {character1_personality} demeanor, creating a tension that neither can ignore.

As they continue to cross paths at various social gatherings, {protagonist_name} begins to see beyond the social facade that {character1_name} presents to the world. Meanwhile, well-meaning but misguided friends and relatives attempt to direct {protagonist_name}'s attention elsewhere, unaware of the growing attachment.

When a rival appears and threatens to separate them, both must overcome pride and prejudice to recognize their true feelings. The question remains: will societal expectations triumph over the whispers of the heart?
""",
        
        'Social Intrigue in Country Estate': """
At {location}, {protagonist_name}, a {protagonist_personality} {protagonist_social_class}, navigates complex social dynamics during the {season} gathering of notable families. 

The arrival of {character1_name}, rumored to possess a fortune from {character1_occupation}, sets the neighborhood abuzz with speculation. When {character1_name} brings along the mysterious {character2_name}, whispers of scandal from the past begin to circulate.

{protagonist_name}, with a keen sense of observation, notices subtle interactions that others miss. A dropped letter, a hushed conversation in the library, meaningful glances exchanged across the drawing room - all suggest that someone at {location} harbors a secret that could ruin reputations.

As {protagonist_name} pieces together the truth, moral questions arise: Should past indiscretions define one's future? Is protecting family honor worth the sacrifice of individual happiness? And most importantly, who can be trusted when appearances so often deceive?
""",
        
        'Marriage Prospects in Regency England': """
In {time_period}, during a particularly eventful {season}, {protagonist_name} faces mounting pressure to secure an advantageous match. As a {protagonist_social_class} with {protagonist_personality} inclinations, the marriage market seems more a battlefield than a path to happiness.

The arrival of {character1_name} to the neighborhood presents an opportunity that {protagonist_name}'s family eagerly encourages. With connections to {character1_occupation} and considerable property, {character1_name} represents security and respectability.

However, {protagonist_name}'s heart is drawn to the less conventional {character2_name}, whose {character2_personality} spirit and modest position as a {character2_occupation} make them an unsuitable match in the eyes of society.

As balls and dinner parties unfold at {location}, {protagonist_name} must navigate family expectations, financial realities, and the quiet longings of the heart. Will prudence triumph over passion, or can {protagonist_name} find a way to reconcile duty with desire?
""",
        
        'Inheritance and Social Mobility': """
{protagonist_name}, a {protagonist_personality} {protagonist_social_class}, receives unexpected news of an inheritance from a distant relative, altering their status and relationships forever.

Before this windfall, {protagonist_name}'s prospects as a {protagonist_occupation} seemed limited, particularly during the harsh economic realities of {season} in {time_period}. The inheritance brings not only financial security but also the attention of {character1_name}, who had previously overlooked {protagonist_name}'s existence.

As {protagonist_name} adjusts to new circumstances at {location}, suspicions arise about the sudden friendship offered by those who once showed indifference. The {character2_personality} {character2_name}, who showed kindness before fortune smiled, now appears distant.

The inheritance carries conditions that test {protagonist_name}'s principles. As social doors open and invitations flood in, the question becomes: was the former life of obscurity, though humble, more authentic than this newfound prominence built on material wealth?
""",
        
        'Family Honor and Reputation': """
In the closely connected society of {time_period}, {protagonist_name} guards the reputation of the family with vigilance. As a {protagonist_personality} {protagonist_social_class} responsible for younger siblings, every social interaction at {location} carries weight.

When rumors begin to circulate about {character1_name}'s inappropriate association with a {character1_occupation} of questionable character, {protagonist_name} fears the scandal may taint their own family by association.

The situation grows more complex when {protagonist_name}'s beloved sibling develops an attachment to {character2_name}, a relation of the very person causing such social concern. Torn between protecting the family name and allowing genuine affection to flourish, {protagonist_name} attempts to navigate the perilous waters of {time_period} society during a particularly gossipy {season}.

A crisis erupts when a midnight elopement is discovered and prevented only by {protagonist_name}'s quick thinking. But the intervention comes at a personal cost, leaving {protagonist_name} to wonder if preserving appearances is worth the sacrifice of authentic happiness.
""",
        
        'Provincial Life and London Society': """
{protagonist_name} has lived contentedly as a {protagonist_social_class} in the peaceful rhythms of provincial life near {location}. With {protagonist_personality} sensibilities and modest expectations as a {protagonist_occupation}, the small pleasures of country living have always seemed sufficient.

An unexpected invitation from {character1_name}, a distant relation with connections to high society, draws {protagonist_name} to London for the {season}. The glittering world of the capital, with its operas, exhibitions, and fashionable gatherings, presents a stark contrast to the familiar routines of home.

In London, {protagonist_name} catches the attention of the sophisticated {character2_name}, whose {character2_personality} wit and worldly experience prove both attractive and disorienting. Meanwhile, letters from home remind {protagonist_name} of simpler values and sincere attachments left behind.

As {protagonist_name} becomes increasingly comfortable in society, an unexpected revelation about {character1_name}'s motivations forces a choice: embrace the exciting but perhaps hollow pleasures of fashionable life, or return to the authentic but limited world of the provinces?
""",
        
        'Lost Love Rekindled': """
Eight years ago, {protagonist_name}, a young and {protagonist_personality} {protagonist_social_class}, was persuaded to end an engagement with the then-unestablished {character1_name}. Now, as {season} brings them unexpectedly together at {location}, both carry the scars of that separation.

In the intervening years, {protagonist_name} has maintained a quiet dignity as a {protagonist_occupation}, while {character1_name} has achieved success and recognition in {character1_occupation}, returning with both fortune and confidence.

Their circles increasingly overlap as mutual connections, unaware of their history, continuously bring them into company. {character1_name} shows particular attention to the {character2_personality} {character2_name}, perhaps as a pointed reminder of what {protagonist_name} once rejected.

As they cautiously navigate shared spaces and conversations, old feelings resurface alongside painful memories. When a moment of crisis reveals that hearts have remained constant despite time and circumstance, can pride be set aside to embrace a second chance at happiness?
""",
        
        'Secret Engagement Revealed': """
In the close-knit community surrounding {location}, {protagonist_name} has maintained a secret engagement to {character1_name} for nearly six months. As a {protagonist_personality} {protagonist_social_class} with responsibilities as a {protagonist_occupation}, public announcement has been delayed for practical reasons.

The arrival of the {character2_personality} {character2_name} during {season} threatens to complicate matters. Misinterpreting {protagonist_name}'s friendly reception as romantic interest, {character2_name} begins to pay particular attention that does not go unnoticed by the community.

When {character1_name} witnesses an innocent but apparently intimate conversation between {protagonist_name} and {character2_name}, jealousy and doubt cloud judgment, leading to a private quarrel that is overheard by the worst possible person—the neighborhood gossip.

As rumors spread and misunderstandings multiply, the secret engagement becomes public in the most mortifying way. {protagonist_name} must navigate damaged trust, family disapproval, and social scrutiny while determining if the engagement itself remains viable after such a trial.
"""
    }
