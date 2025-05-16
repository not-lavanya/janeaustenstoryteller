"""
Audio management for the Jane Austen storytelling experience.
Handles playback of narration, background music, and sound effects.
"""

import os
import time
import pygame
import tempfile
import threading

class AudioManager:
    def __init__(self):
        # Initialize pygame mixer if not already initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        # Define paths for stock sound effects and music
        # These are placeholder descriptions - the actual files would need to be provided
        self.sound_effects = {
            'welcome': None,  # "Welcome" sound
            'selection': None,  # "Selection made" sound
            'character': None,  # "Character created" sound
            'writing': None,  # "Quill writing" sound
            'save': None,  # "Document saved" sound
            'goodbye': None  # "Farewell" sound
        }
        
        self.background_music = {
            'romantic': None,  # Light classical piece for romantic themes
            'dramatic': None,  # More intense piece for dramatic themes
            'general': None  # Default background music
        }
        
        # Create sound effects using pygame tones as placeholders
        self._generate_placeholder_sounds()
        
        # Playback control
        self.currently_playing = None
        self.playback_thread = None
        self.stop_playback_flag = False

    def _generate_placeholder_sounds(self):
        """Generate placeholder sound effects using pygame.mixer"""
        try:
            # Generate welcome sound (ascending notes)
            welcome_buffer = self._generate_tone_buffer(frequency=440, duration=300)  # A4
            welcome_buffer += self._generate_tone_buffer(frequency=523, duration=300)  # C5
            welcome_buffer += self._generate_tone_buffer(frequency=659, duration=500)  # E5
            self.sound_effects['welcome'] = pygame.mixer.Sound(buffer=welcome_buffer)
            
            # Generate selection sound (short bell-like tone)
            selection_buffer = self._generate_tone_buffer(frequency=587, duration=200)  # D5
            self.sound_effects['selection'] = pygame.mixer.Sound(buffer=selection_buffer)
            
            # Generate character sound (two-note motif)
            character_buffer = self._generate_tone_buffer(frequency=392, duration=200)  # G4
            character_buffer += self._generate_tone_buffer(frequency=494, duration=300)  # B4
            self.sound_effects['character'] = pygame.mixer.Sound(buffer=character_buffer)
            
            # Generate writing sound (rapid soft taps)
            writing_buffer = self._generate_tone_buffer(frequency=220, duration=50)  # A3
            writing_buffer *= 5  # Repeat 5 times for writing effect
            self.sound_effects['writing'] = pygame.mixer.Sound(buffer=writing_buffer)
            
            # Generate save sound (descending arpeggio)
            save_buffer = self._generate_tone_buffer(frequency=523, duration=150)  # C5
            save_buffer += self._generate_tone_buffer(frequency=440, duration=150)  # A4
            save_buffer += self._generate_tone_buffer(frequency=349, duration=300)  # F4
            self.sound_effects['save'] = pygame.mixer.Sound(buffer=save_buffer)
            
            # Generate goodbye sound (gentle descending notes)
            goodbye_buffer = self._generate_tone_buffer(frequency=523, duration=300)  # C5
            goodbye_buffer += self._generate_tone_buffer(frequency=440, duration=300)  # A4
            goodbye_buffer += self._generate_tone_buffer(frequency=349, duration=300)  # F4
            goodbye_buffer += self._generate_tone_buffer(frequency=262, duration=500)  # C4
            self.sound_effects['goodbye'] = pygame.mixer.Sound(buffer=goodbye_buffer)
            
            # Generate background music placeholders (repeating patterns)
            # Romantic music (gentle chord progression)
            romantic_buffer = self._generate_tone_buffer(frequency=262, duration=500)  # C4
            romantic_buffer += self._generate_tone_buffer(frequency=330, duration=500)  # E4
            romantic_buffer += self._generate_tone_buffer(frequency=392, duration=500)  # G4
            romantic_buffer += self._generate_tone_buffer(frequency=330, duration=500)  # E4
            romantic_buffer *= 2  # Repeat the pattern
            self.background_music['romantic'] = pygame.mixer.Sound(buffer=romantic_buffer)
            
            # Dramatic music (minor chord progression)
            dramatic_buffer = self._generate_tone_buffer(frequency=262, duration=400)  # C4
            dramatic_buffer += self._generate_tone_buffer(frequency=311, duration=400)  # D#4
            dramatic_buffer += self._generate_tone_buffer(frequency=392, duration=400)  # G4
            dramatic_buffer += self._generate_tone_buffer(frequency=466, duration=600)  # A#4
            dramatic_buffer *= 2  # Repeat the pattern
            self.background_music['dramatic'] = pygame.mixer.Sound(buffer=dramatic_buffer)
            
            # General music (pleasant major scale)
            general_buffer = self._generate_tone_buffer(frequency=262, duration=300)  # C4
            general_buffer += self._generate_tone_buffer(frequency=294, duration=300)  # D4
            general_buffer += self._generate_tone_buffer(frequency=330, duration=300)  # E4
            general_buffer += self._generate_tone_buffer(frequency=349, duration=300)  # F4
            general_buffer += self._generate_tone_buffer(frequency=392, duration=300)  # G4
            general_buffer += self._generate_tone_buffer(frequency=440, duration=300)  # A4
            general_buffer += self._generate_tone_buffer(frequency=494, duration=300)  # B4
            general_buffer += self._generate_tone_buffer(frequency=523, duration=500)  # C5
            self.background_music['general'] = pygame.mixer.Sound(buffer=general_buffer)
            
        except Exception as e:
            print(f"Error generating placeholder sounds: {e}")
            # If sound generation fails, create empty sounds
            for key in self.sound_effects:
                if self.sound_effects[key] is None:
                    self.sound_effects[key] = pygame.mixer.Sound(buffer=bytearray())
            for key in self.background_music:
                if self.background_music[key] is None:
                    self.background_music[key] = pygame.mixer.Sound(buffer=bytearray())

    def _generate_tone_buffer(self, frequency=440, duration=100, volume=0.5):
        """Generate a simple tone as a bytes buffer for pygame.mixer.Sound
        
        Args:
            frequency: Tone frequency in Hz
            duration: Duration in milliseconds
            volume: Volume level (0.0 to 1.0)
            
        Returns:
            Bytes buffer containing the generated tone
        """
        # Parameters for tone generation
        bits = 16
        sample_rate = 44100
        amplitude = 2**(bits-1) - 1
        period = int(sample_rate / frequency)
        
        # Generate a simple sine wave
        import math
        import array
        
        # Calculate number of samples
        num_samples = int(sample_rate * (duration / 1000.0))
        
        # Generate buffer using a sine wave
        buf = array.array('h')
        for i in range(num_samples):
            sample = int(amplitude * volume * math.sin(2 * math.pi * i / period))
            buf.append(sample)
        
        # Apply fade in/out to avoid clicks
        fade_samples = min(int(num_samples * 0.1), 1000)  # 10% of samples or 1000, whichever is smaller
        for i in range(fade_samples):
            # Fade in
            buf[i] = int(buf[i] * (i / fade_samples))
            # Fade out
            buf[num_samples - 1 - i] = int(buf[num_samples - 1 - i] * (i / fade_samples))
        
        return buf.tobytes()

    def play_sound_effect(self, effect_name):
        """Play a sound effect"""
        if effect_name in self.sound_effects and self.sound_effects[effect_name]:
            try:
                self.sound_effects[effect_name].play()
            except:
                print(f"Could not play sound effect: {effect_name}")

    def play_background_music(self, music_type, loops=-1, volume=0.3):
        """Play background music with looping"""
        if music_type in self.background_music and self.background_music[music_type]:
            try:
                # Stop any currently playing background music
                pygame.mixer.music.stop()
                
                # Set volume and play
                self.background_music[music_type].set_volume(volume)
                self.background_music[music_type].play(loops=loops)
            except:
                print(f"Could not play background music: {music_type}")

    def _playback_thread_func(self, narration_file, background_music=None):
        """Thread function for playing narration with background music"""
        try:
            # Set up channels
            pygame.mixer.set_num_channels(2)
            narration_channel = pygame.mixer.Channel(0)
            music_channel = pygame.mixer.Channel(1)
            
            # Load and play narration
            narration_sound = pygame.mixer.Sound(narration_file)
            narration_channel.play(narration_sound)
            
            # Play background music if specified
            if background_music and background_music in self.background_music:
                music_sound = self.background_music[background_music]
                if music_sound:
                    music_sound.set_volume(0.15)  # Lower volume for background
                    music_channel.play(music_sound, loops=-1)  # Loop continuously
            
            # Wait for narration to finish or stop flag to be set
            while narration_channel.get_busy() and not self.stop_playback_flag:
                time.sleep(0.1)
                
            # Stop all audio when done
            narration_channel.stop()
            music_channel.stop()
            
        except Exception as e:
            print(f"Error in audio playback: {e}")
        finally:
            self.currently_playing = None
            self.stop_playback_flag = False

    def play_narration_with_background(self, narration_file, background_music=None):
        """Play narration with optional background music"""
        # Stop any currently playing audio
        self.stop_playback()
        
        # Start playback in a separate thread
        self.stop_playback_flag = False
        self.currently_playing = narration_file
        self.playback_thread = threading.Thread(
            target=self._playback_thread_func,
            args=(narration_file, background_music)
        )
        self.playback_thread.daemon = True
        self.playback_thread.start()

    def stop_playback(self):
        """Stop any currently playing audio"""
        if self.playback_thread and self.playback_thread.is_alive():
            self.stop_playback_flag = True
            self.playback_thread.join(timeout=1.0)
        
        # Ensure all channels are stopped
        pygame.mixer.stop()
        self.currently_playing = None

    def combine_audio_files(self, input_files, output_file):
        """
        Simple utility to concatenate multiple audio files.
        Note: This is a basic implementation that assumes files have compatible formats.
        
        Args:
            input_files: List of input MP3 file paths
            output_file: Output MP3 file path
        """
        try:
            # For a real implementation, we would use pydub or another library
            # that properly handles audio concatenation. This is a simple approach
            # that just combines the binary data of the files.
            with open(output_file, 'wb') as outfile:
                for file_path in input_files:
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as infile:
                            outfile.write(infile.read())
            return True
        except Exception as e:
            print(f"Error combining audio files: {e}")
            return False
