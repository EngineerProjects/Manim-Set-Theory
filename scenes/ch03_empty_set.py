from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class EmptySetWithVoiceover(VoiceoverScene):
    def construct(self):
        """Main method that orchestrates the entire video with voiceover"""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_definition()
        self.show_uniqueness()
    
    def show_title(self):
        """Display the main title: The Empty Set ∅"""
        # Create the "The Empty Set ∅" title
        empty_set_title = Text(
            "The Empty Set ∅",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        empty_set_title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=empty_set_title.get_corner(DOWN + LEFT),
            end=empty_set_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(empty_set_title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(empty_set_title, underline)), run_time=1)
    
    def show_definition(self):
        """Show empty set definition with subset theorem and proof"""
        # Definition text - first line
        definition_line1 = MarkupText(
            '<b><i>The empty set ∅ is a set which contains</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        definition_line2 = MarkupText(
            '<b><i>no elements.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the definition text at the top
        definition_line1.to_edge(UP, buff=1.0)
        definition_line1.to_edge(LEFT, buff=0.5)
        definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        with self.voiceover(text="The empty set is a set which contains no elements.") as tracker:
            # Show definition text
            self.play(Write(VGroup(definition_line1, definition_line2)), run_time=2.5)
            # Wait for remaining audio if needed
            self.safe_wait(tracker.duration - 2.5)
        
        # Theorem statement - CENTERED
        theorem_text = MarkupText(
            '<b><i>∅ is a subset of any set</i></b>',
            color="#505050",
            font_size=42,
            font="sans-serif"
        )
        theorem_text.move_to(ORIGIN + UP * 0.3)  # Centered horizontally
        
        with self.voiceover(text="Firstly, the empty set is a subset of any set.") as tracker:
            # Show theorem
            self.play(Write(theorem_text), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Proof heading
        proof_heading = MarkupText(
            '<b><i>Proof:</i></b>',
            color="#505050",
            font_size=38,
            font="sans-serif"
        )
        proof_heading.next_to(theorem_text, DOWN, buff=0.6)
        proof_heading.to_edge(LEFT, buff=0.5)
        
        # Show proof heading
        self.play(Write(proof_heading), run_time=1.5)
        
        # Proof text - first line
        proof_line1 = MarkupText(
            '<b><i>Let A be a set. Since ∅ has no elements, all the</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        proof_line2 = MarkupText(
            '<b><i>elements in ∅ must also be in A.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position proof text
        proof_line1.next_to(proof_heading, DOWN, aligned_edge=LEFT, buff=0.4)
        proof_line2.next_to(proof_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        with self.voiceover(text="Let A be a set. Since the empty set has no elements, all the elements in the empty set must also be in A.") as tracker:
            # Show proof text
            self.play(Write(proof_line1), run_time=2)
            self.play(Write(proof_line2), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        # Conclusion - positioned below the proof text
        conclusion = MathTex(
            r'\text{Therefore, } \underline{\varnothing \subseteq A}',
            font_size=50,
            color="#505050"
        )
        # Position it below proof_line2 with minimal spacing
        conclusion.next_to(proof_line2, DOWN, buff=0.6)
        conclusion.to_edge(LEFT, buff=1.5)  # Align with proof indentation
        
        with self.voiceover(text="Therefore, the empty set is a subset of A.") as tracker:
            # Show conclusion
            self.play(Write(conclusion), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                definition_line1, definition_line2, theorem_text, proof_heading,
                proof_line1, proof_line2, conclusion
            )),
            run_time=1
        )
    
    def show_uniqueness(self):
        """Show uniqueness proof for the empty set"""
        # Main statement at the top
        uniqueness_statement = MarkupText(
            '<b><i>∅ is unique</i></b>',
            color="#505050",
            font_size=48,
            font="sans-serif"
        )
        uniqueness_statement.to_edge(UP, buff=1.0)
        
        with self.voiceover(text="The second property of the empty set is that it's unique.") as tracker:
            # Show main statement
            self.play(Write(uniqueness_statement), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Proof heading
        proof_heading = MarkupText(
            '<b><i>Proof</i></b>',
            color="#505050",
            font_size=40,
            font="sans-serif"
        )
        proof_heading.next_to(uniqueness_statement, DOWN, buff=0.8)
        proof_heading.to_edge(LEFT, buff=0.5)
        
        # Show proof heading
        self.play(Write(proof_heading), run_time=1.5)
        
        # Proof line 1
        proof_line1 = MarkupText(
            '<b><i>let ∅₁ and ∅₂ be two empty sets.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        proof_line1.next_to(proof_heading, DOWN, buff=0.4)
        proof_line1.to_edge(LEFT, buff=0.5)
        
        # Proof line 2
        proof_line2 = MarkupText(
            '<b><i>Since the empty set is a subset of all sets</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        proof_line2.next_to(proof_line1, DOWN, buff=0.2)
        proof_line2.to_edge(LEFT, buff=0.5)
        
        with self.voiceover(text="Let empty set one and empty set two be two empty sets.") as tracker:
            # Show proof text
            self.play(Write(proof_line1), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        with self.voiceover(text="Since the empty set is a subset of all sets, we already can deduce that empty set one is a subset of empty set two and empty set two is a subset of empty set one.") as tracker:
            self.play(Write(proof_line2), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Subset relations - positioned below proof text
        subset_relations = MathTex(
            r'\varnothing_1 \subseteq \varnothing_2 \quad \text{and} \quad \varnothing_2 \subseteq \varnothing_1',
            font_size=50,
            color="#505050"
        )
        subset_relations.next_to(proof_line2, DOWN, buff=0.6)
        subset_relations.to_edge(LEFT, buff=0.5)
        
        with self.voiceover(text="This is the definition of equality we saw earlier.") as tracker:
            # Show subset relations
            self.play(Write(subset_relations), run_time=2.5)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.5)
        
        # Final conclusion - positioned below subset relations
        conclusion = MathTex(
            r'\text{Therefore, } \varnothing_1 = \varnothing_2 = \varnothing',
            font_size=50,
            color="#505050"
        )
        conclusion.next_to(subset_relations, DOWN, buff=0.6)
        conclusion.to_edge(LEFT, buff=0.5)
        
        with self.voiceover(text="If empty sets one and two are equal, then we only really had a single unique empty set to begin with, and so we can drop the subscripts one and two and just call them the empty set.") as tracker:
            # Show conclusion
            self.play(Write(conclusion), run_time=2)
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)