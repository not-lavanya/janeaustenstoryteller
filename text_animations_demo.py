"""
Jane Austen Storytelling Experience - Text Animations Demo
A demonstration of Regency-era text animations without requiring Kivy
"""

import os
import time
import random
from regency_text_animations import RegencyTextAnimator

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """Display a decorative header"""
    width = 70
    border = "═" * width
    print("\n" + border)
    print(title.center(width))
    print(border + "\n")

def display_demo_options():
    """Display the available demonstration options"""
    print("\nSelect a text animation to demonstrate:")
    print("1. Formal Writing Style")
    print("2. Quill Writing Effect")
    print("3. Scene Transition")
    print("4. Regency Letter")
    print("5. Animated Dialogue")
    print("6. Chapter Heading")
    print("7. Social Commentary")
    print("8. Narration Styles")
    print("9. Run Full Demonstration")
    print("0. Return to Main Menu")

def run_full_demo(animator):
    """Run a full demonstration of all text animation features"""
    clear_screen()
    display_header("REGENCY TEXT ANIMATIONS - FULL DEMONSTRATION")
    
    print("This demonstration will showcase the various text animation styles")
    print("inspired by Jane Austen's Regency era writing.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # Demo 1: Chapter Heading
    clear_screen()
    display_header("1. CHAPTER HEADING ANIMATION")
    
    print("Chapter headings appear with decorative frames in Roman numerals:")
    time.sleep(1)
    animator.animated_chapter_heading(3, "A Most Unexpected Meeting")
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 2: Formal writing transition
    clear_screen()
    display_header("2. FORMAL WRITING TRANSITION")
    
    print("Formal writing appears with deliberate pacing and decorative elements:")
    time.sleep(1)
    formal_text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    animator.formal_writing_transition(formal_text)
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 3: Scene transition
    clear_screen()
    display_header("3. SCENE TRANSITION")
    
    print("Scene transitions create visual breaks between narrative locations:")
    time.sleep(1)
    animator.animated_scene_transition(
        "The drawing room at Longbourn", 
        "The grand ballroom at Netherfield"
    )
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 4: Regency letter
    clear_screen()
    display_header("4. REGENCY LETTER")
    
    print("Letters appear with period-appropriate formatting and flourishes:")
    time.sleep(1)
    letter_content = "I hope this letter finds you in good health and spirits. We have had quite the eventful week at Pemberley, with visitors arriving from as far as London and Bath. The gardens are in full bloom, and the weather has been most agreeable."
    animator.animated_regency_letter("Elizabeth Darcy", "Jane Bingley", letter_content)
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 5: Dialogue
    clear_screen()
    display_header("5. CHARACTER DIALOGUE")
    
    print("Character dialogue has distinct pacing and action descriptions:")
    time.sleep(1)
    animator.animated_dialogue(
        "Mr. Darcy", 
        "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow", 
        "looks intently at Elizabeth"
    )
    time.sleep(1)
    animator.animated_dialogue(
        "Elizabeth Bennet", 
        "Are you so severe upon your own sex as to doubt the possibility of all this?", 
        "raises an eyebrow"
    )
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 6: Social commentary
    clear_screen()
    display_header("6. SOCIAL COMMENTARY")
    
    print("Social commentary sections feature distinctive formatting:")
    time.sleep(1)
    commentary = "Society's expectations of young women often disregard their intellectual capabilities, focusing instead on accomplishments designed merely to attract a suitable match. Such narrow constraints do a disservice not only to the women themselves but to society as a whole."
    animator.animated_social_commentary(commentary)
    
    print("\nPress Enter to continue...")
    input()
    
    # Demo 7: Narration styles
    clear_screen()
    display_header("7. NARRATION STYLES")
    
    print("Narration can be presented in different styles:")
    
    print("\nStandard narration:")
    time.sleep(1)
    standard_narration = "The morning was fair, with a gentle breeze that stirred the leaves of the great oak trees lining the path to Pemberley."
    animator.animated_narration(standard_narration, style="standard")
    
    print("\nDramatic narration:")
    time.sleep(1)
    dramatic_narration = "The thunder crashed overhead as she ran through the storm! Would she reach shelter before the downpour worsened? Her heart pounded with each step!"
    animator.animated_narration(dramatic_narration, style="dramatic")
    
    print("\nReflective narration:")
    time.sleep(1)
    reflective_narration = "How curious it is that the human heart, in all its complexity, can be so easily misunderstood by those who claim to know it best. Perhaps it is this very mystery that compels us to seek connection."
    animator.animated_narration(reflective_narration, style="reflective")
    
    print("\nPress Enter to continue...")
    input()
    
    # Final screen
    clear_screen()
    display_header("DEMONSTRATION COMPLETE")
    
    print("You have experienced the range of text animations available")
    print("in the Jane Austen Storytelling Experience.")
    print("\nThese animations help create an immersive Regency-era atmosphere")
    print("that enhances the storytelling experience.")
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_formal_writing(animator):
    """Demonstrate formal writing style"""
    clear_screen()
    display_header("FORMAL WRITING DEMONSTRATION")
    
    print("The formal writing style mimics the deliberate pace and")
    print("flourishes of Regency-era handwritten correspondence.")
    print("\nObserve how punctuation receives special emphasis and")
    print("decorative elements frame the text.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # First example - famous Austen quote
    formal_text1 = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    animator.formal_writing_transition(formal_text1)
    
    print("\nWould you like to see another example? (y/n)")
    if input().lower().startswith('y'):
        # Second example
        formal_text2 = "The power of doing anything with quickness is always prized much by the possessor, and often without any attention to the imperfection of the performance."
        animator.formal_writing_transition(formal_text2)
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_quill_writing(animator):
    """Demonstrate quill writing effect"""
    clear_screen()
    display_header("QUILL WRITING EFFECT DEMONSTRATION")
    
    print("The quill writing effect simulates the variable pace and")
    print("ink saturation of writing with a period-appropriate quill pen.")
    print("\nNotice how the writing speed varies with punctuation and")
    print("the subtle variations in timing.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # Demonstrate with a descriptive passage
    quill_text = "The path wound its way through the gardens, passing beneath ancient oaks whose branches formed a green canopy overhead. Flowers of every description lined the walkway, their fragrance filling the air with a sweet perfume that delighted the senses."
    animator.simulate_quill_writing(quill_text)
    
    print("\nWould you like to see a faster writing pace? (y/n)")
    if input().lower().startswith('y'):
        # Second example with faster pace
        quill_text2 = "The carriage rattled along the country road at a great pace, its occupants jostled with each bump and turn. 'Do slow down!' cried Mrs. Bennet, clutching her bonnet. 'We shall all be overthrown!'"
        animator.simulate_quill_writing(quill_text2, speed=0.02)
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_scene_transition(animator):
    """Demonstrate scene transition"""
    clear_screen()
    display_header("SCENE TRANSITION DEMONSTRATION")
    
    print("Scene transitions create visual breaks between different")
    print("locations or time periods in the narrative.")
    print("\nThese transitions help guide the reader through changes")
    print("in setting with period-appropriate phrasing.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # First transition
    animator.animated_scene_transition(
        "The drawing room at Longbourn", 
        "The grand ballroom at Netherfield"
    )
    
    print("\nWould you like to see another transition? (y/n)")
    if input().lower().startswith('y'):
        # Second transition
        animator.animated_scene_transition(
            "The gardens at Pemberley, summer", 
            "The library at Pemberley, winter"
        )
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_regency_letter(animator):
    """Demonstrate Regency letter formatting"""
    clear_screen()
    display_header("REGENCY LETTER DEMONSTRATION")
    
    print("Letters were a crucial form of communication in the Regency era.")
    print("This animation simulates the experience of reading correspondence")
    print("from the period, with appropriate formatting and phrasing.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # Sample letter
    letter_content = "I hope this letter finds you in good health and spirits. We have had quite the eventful week at Pemberley, with visitors arriving from as far as London and Bath. The gardens are in full bloom, and the weather has been most agreeable. I find myself thinking often of our last conversation and look forward to when we might next meet."
    animator.animated_regency_letter("Elizabeth Darcy", "Jane Bingley", letter_content)
    
    print("\nWould you like to see another letter? (y/n)")
    if input().lower().startswith('y'):
        # Second letter
        letter_content2 = "I write to you with the most distressing news. Our cousin Mr. Collins has taken ill with a fever, and Lady Catherine de Bourgh has been most insistent in her demands for the best physicians from London to attend him. Charlotte bears the burden with remarkable fortitude, though I cannot help but think the constant presence of Lady Catherine adds rather than diminishes her trials."
        animator.animated_regency_letter("Mary Bennet", "Elizabeth Darcy", letter_content2, location="Meryton")
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_animated_dialogue(animator):
    """Demonstrate animated dialogue"""
    clear_screen()
    display_header("ANIMATED DIALOGUE DEMONSTRATION")
    
    print("Character dialogue in Austen's works carries much of the narrative weight.")
    print("This animation presents dialogue with appropriate pacing and")
    print("includes action descriptions that help convey character emotions.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # First dialogue exchange
    animator.animated_dialogue(
        "Mr. Darcy", 
        "I have been meditating on the very great pleasure which a pair of fine eyes in the face of a pretty woman can bestow", 
        "looks intently at Elizabeth"
    )
    time.sleep(0.5)
    animator.animated_dialogue(
        "Elizabeth Bennet", 
        "Are you so severe upon your own sex as to doubt the possibility of all this?", 
        "raises an eyebrow"
    )
    
    print("\nWould you like to see another dialogue exchange? (y/n)")
    if input().lower().startswith('y'):
        # Second dialogue exchange
        animator.animated_dialogue(
            "Mrs. Bennet", 
            "I do not know who is more aggravating - Mr. Bingley for his inconstancy or Mr. Darcy for his pride!", 
            "fans herself vigorously"
        )
        time.sleep(0.5)
        animator.animated_dialogue(
            "Mr. Bennet", 
            "Perhaps, my dear, they are both merely men with their own concerns that do not revolve around our daughters.", 
            "looks up briefly from his book"
        )
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_chapter_heading(animator):
    """Demonstrate chapter heading"""
    clear_screen()
    display_header("CHAPTER HEADING DEMONSTRATION")
    
    print("Chapter headings provide structure to the narrative and")
    print("create anticipation for what follows.")
    print("\nThese animated headings use Roman numerals and decorative")
    print("elements typical of books from the Regency period.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # First chapter heading
    animator.animated_chapter_heading(3, "A Most Unexpected Meeting")
    
    print("\nWould you like to see another chapter heading? (y/n)")
    if input().lower().startswith('y'):
        # Second chapter heading
        animator.animated_chapter_heading(12, "Revelations at the Ball")
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_social_commentary(animator):
    """Demonstrate social commentary"""
    clear_screen()
    display_header("SOCIAL COMMENTARY DEMONSTRATION")
    
    print("Jane Austen was known for her insightful social commentary.")
    print("These sections are presented with distinctive formatting")
    print("to highlight their importance within the narrative.")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # First social commentary
    commentary1 = "Society's expectations of young women often disregard their intellectual capabilities, focusing instead on accomplishments designed merely to attract a suitable match. Such narrow constraints do a disservice not only to the women themselves but to society as a whole."
    animator.animated_social_commentary(commentary1)
    
    print("\nWould you like to see another social commentary? (y/n)")
    if input().lower().startswith('y'):
        # Second social commentary
        commentary2 = "The distinction of rank, which is so often scorned by those who possess it not, becomes in the hands of the discerning few a tool for good rather than division. It is not the rank itself that merits respect, but the manner in which its privileges are employed for the benefit of all."
        animator.animated_social_commentary(commentary2)
    
    print("\nPress Enter to return to the demo menu...")
    input()

def demo_narration_styles(animator):
    """Demonstrate different narration styles"""
    clear_screen()
    display_header("NARRATION STYLES DEMONSTRATION")
    
    print("The pace and style of narration helps establish the")
    print("tone and atmosphere of different scenes.")
    print("\nThese animations demonstrate three distinct narration styles:")
    print("- Standard: Balanced pacing for general narrative")
    print("- Dramatic: Emphasizes action and excitement")
    print("- Reflective: Slower, more contemplative pacing")
    print("\nPress Enter to begin the demonstration...")
    input()
    
    # Standard narration
    print("\nSTANDARD NARRATION:")
    time.sleep(1)
    standard_narration = "The morning was fair, with a gentle breeze that stirred the leaves of the great oak trees lining the path to Pemberley. Elizabeth walked at a leisurely pace, enjoying the pleasant weather and anticipating her arrival."
    animator.animated_narration(standard_narration, style="standard")
    
    print("\nWould you like to see dramatic narration? (y/n)")
    if input().lower().startswith('y'):
        # Dramatic narration
        print("\nDRAMATIC NARRATION:")
        time.sleep(1)
        dramatic_narration = "The thunder crashed overhead as she ran through the storm! Would she reach shelter before the downpour worsened? Her heart pounded with each step! Lightning flashed, illuminating the path ahead for just a moment before plunging her back into darkness."
        animator.animated_narration(dramatic_narration, style="dramatic")
    
    print("\nWould you like to see reflective narration? (y/n)")
    if input().lower().startswith('y'):
        # Reflective narration
        print("\nREFLECTIVE NARRATION:")
        time.sleep(1)
        reflective_narration = "How curious it is that the human heart, in all its complexity, can be so easily misunderstood by those who claim to know it best. Perhaps it is this very mystery that compels us to seek connection, to bridge the gaps between souls with tentative understanding."
        animator.animated_narration(reflective_narration, style="reflective")
    
    print("\nPress Enter to return to the demo menu...")
    input()

def run_text_animations_demo():
    """Run the text animations demonstration"""
    # Create animator
    animator = RegencyTextAnimator()
    
    while True:
        clear_screen()
        display_header("JANE AUSTEN STORYTELLING EXPERIENCE")
        print("Text Animations Demonstration")
        print("\nThis demonstration showcases the various text animation")
        print("techniques that enhance the storytelling experience with")
        print("authentic Regency-era writing styles.")
        
        display_demo_options()
        
        choice = input("\nEnter your choice (0-9): ")
        
        if choice == '1':
            demo_formal_writing(animator)
        elif choice == '2':
            demo_quill_writing(animator)
        elif choice == '3':
            demo_scene_transition(animator)
        elif choice == '4':
            demo_regency_letter(animator)
        elif choice == '5':
            demo_animated_dialogue(animator)
        elif choice == '6':
            demo_chapter_heading(animator)
        elif choice == '7':
            demo_social_commentary(animator)
        elif choice == '8':
            demo_narration_styles(animator)
        elif choice == '9':
            run_full_demo(animator)
        elif choice == '0':
            clear_screen()
            print("Returning to main menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    run_text_animations_demo()