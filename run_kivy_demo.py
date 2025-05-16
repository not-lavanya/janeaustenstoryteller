"""
Kivy Visual Imagery Demo for Jane Austen Storytelling Experience
This script runs the Kivy-based visual imagery demonstration.
"""

import os
import sys
import time

def check_kivy_available():
    """Check if Kivy is available and properly configured"""
    try:
        # Try to import Kivy
        import kivy
        from kivy.app import App
        
        # If we get here, basic imports are working
        print("Kivy is installed.")
        
        # Check for display availability
        if "DISPLAY" not in os.environ and "WAYLAND_DISPLAY" not in os.environ:
            print("WARNING: No display detected. Kivy may not work properly.")
            return False
        
        return True
    except ImportError:
        print("Kivy is not installed or cannot be imported.")
        return False
    except Exception as e:
        print(f"Error checking Kivy: {e}")
        return False

def run_kivy_visual_demo():
    """Run the Kivy visual imagery demo"""
    # First check if Kivy is available
    if not check_kivy_available():
        print("\nKivy visual elements cannot be displayed in this environment.")
        print("Please run this demo on a system with graphical capabilities.")
        print("You can still use the text animations demo with:")
        print("python text_animations_demo.py\n")
        return False
    
    # If Kivy is available, run the demo
    try:
        # Import the Kivy visual imagery module
        from kivy_visual_imagery import main
        
        # Run the demo
        print("Starting Kivy Visual Imagery Demo...")
        time.sleep(1)
        main()
        return True
    except Exception as e:
        print(f"Error running Kivy demo: {e}")
        return False

if __name__ == "__main__":
    # Run the Kivy visual imagery demo
    print("Jane Austen Storytelling Experience - Kivy Visual Imagery Demo")
    print("=" * 70)
    run_kivy_visual_demo()