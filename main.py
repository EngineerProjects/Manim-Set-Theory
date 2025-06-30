#!/usr/bin/env python3
"""
Main script to build the complete Set Theory video from all chapters.
Renders chapters 1-8 and concatenates them into a single video.
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# Import all scene classes
from voice import (
    BasicsWithVoiceover,
    SubsetsWithVoiceover,
    EmptySetWithVoiceover,
    UnionAndIntersectionWithVoiceover,
    TheComplementWithVoiceover,
    DeMorganLawsWithVoiceover,
    SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover,
    RussellsParadoxWithVoiceover
)

class FullSetTheoryVideo(VoiceoverScene):
    def construct(self):
        """Main construct method that combines all 8 chapters into one video."""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color
        self.camera.background_color = "#F0F0F0"
        
        # List of all chapter scene classes in order
        chapter_scenes = [
            BasicsWithVoiceover,
            SubsetsWithVoiceover,
            EmptySetWithVoiceover,
            UnionAndIntersectionWithVoiceover,
            TheComplementWithVoiceover,
            DeMorganLawsWithVoiceover,
            SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover,
            RussellsParadoxWithVoiceover
        ]
        
        # Execute each chapter's construct method in sequence
        for i, scene_class in enumerate(chapter_scenes, 1):
            print(f"🎬 Rendering Chapter {i}: {scene_class.__name__}")
            
            # Create an instance and copy its methods to this scene
            chapter_instance = scene_class()
            
            # Copy the TTS service to the chapter instance
            chapter_instance.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
            chapter_instance.camera.background_color = "#F0F0F0"
            
            # Execute the chapter's construct method in the context of this main scene
            # We need to bind the chapter's methods to this scene's context
            original_self = chapter_instance
            
            # Temporarily replace the chapter's scene methods with this scene's methods
            chapter_instance.add = self.add
            chapter_instance.remove = self.remove
            chapter_instance.play = self.play
            chapter_instance.wait = self.wait
            chapter_instance.clear = self.clear
            chapter_instance.camera = self.camera
            chapter_instance.renderer = self.renderer
            chapter_instance.mobjects = self.mobjects
            chapter_instance.foreground_mobjects = self.foreground_mobjects
            
            # Call the chapter's construct method
            chapter_instance.construct()
            
            # Add a brief pause between chapters
            if i < len(chapter_scenes):
                self.wait(1)
                
        print("✅ All chapters rendered successfully into single video!")

# To render this scene, run:
# manim main.py FullSetTheoryVideo -pqh