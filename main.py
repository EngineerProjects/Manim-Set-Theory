from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# Import all your chapter classes
from scenes import (
    BasicsWithVoiceover,
    SubsetsWithVoiceover,
    EmptySetWithVoiceover,
    UnionAndIntersectionWithVoiceover,
    TheComplementWithVoiceover,
    DeMorganLawsWithVoiceover,
    SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover,
    RussellsParadoxWithVoiceover,
)

class SetTheoryCompleteVideo(VoiceoverScene):
    """
    Complete Set Theory video combining all chapters using Manim sections.
    This creates a single video file with all chapters seamlessly connected.
    """
    
    def construct(self):
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Chapter 1: The Basics (0:00 - 4:21)
        self.run_chapter(BasicsWithVoiceover)
        self.clear()
        
        # Chapter 2: Subsets (4:21 - 7:25)
        self.run_chapter(SubsetsWithVoiceover)
        self.clear()

        # Chapter 3: The Empty Set (7:25 - 8:21)
        self.run_chapter(EmptySetWithVoiceover)
        self.clear()
        
        # Chapter 4: Union and Intersection (8:21 - 20:02)
        self.run_chapter(UnionAndIntersectionWithVoiceover)
        self.clear()
        
        # Chapter 5: The Complement (20:02 - 24:10)
        self.run_chapter(TheComplementWithVoiceover)
        self.clear()
        
        # Chapter 6: De Morgan's Laws (24:10 - 26:13)
        self.run_chapter(DeMorganLawsWithVoiceover)
        self.clear()
        
        # Chapter 7: Sets of Sets, Power Sets, Indexed Families (26:13+)
        self.run_chapter(SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover)
        self.clear()
        
        # Chapter 8: Russell's Paradox
        self.run_chapter(RussellsParadoxWithVoiceover)

    def run_chapter(self, ChapterClass):
        """
        Run a chapter by creating an instance and calling its construct method.
        This is the simplest and most reliable approach.
        """
        # Create instance of the chapter
        chapter = ChapterClass()
        
        # Set up the chapter with the same configuration as our main scene
        chapter.set_speech_service(self.speech_service)
        chapter.camera.background_color = self.camera.background_color
        
        # Store references to our scene's methods
        original_play = chapter.play
        original_add = chapter.add
        original_remove = chapter.remove
        original_clear = chapter.clear
        original_wait = chapter.wait
        
        # Replace chapter's methods with our scene's methods to capture all animations
        chapter.play = self.play
        chapter.add = self.add
        chapter.remove = self.remove
        chapter.clear = self.clear
        chapter.wait = self.wait
        
        # Add safe_wait method if it exists in the chapter
        if hasattr(chapter, 'safe_wait'):
            chapter.safe_wait = self.safe_wait
        
        try:
            # Execute the chapter's construct method
            chapter.construct()
        except Exception as e:
            print(f"Error in chapter {ChapterClass.__name__}: {e}")
            # Restore original methods in case of error
            chapter.play = original_play
            chapter.add = original_add
            chapter.remove = original_remove
            chapter.clear = original_clear
            chapter.wait = original_wait
        finally:
            # Clean up: restore original methods (good practice)
            chapter.play = original_play
            chapter.add = original_add
            chapter.remove = original_remove
            chapter.clear = original_clear
            chapter.wait = original_wait

    def safe_wait(self, duration):
        """Helper method to safely handle wait times"""
        if duration > 0:
            self.wait(duration)