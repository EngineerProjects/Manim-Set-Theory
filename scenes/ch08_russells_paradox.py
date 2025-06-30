from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class RussellsParadoxWithVoiceover(VoiceoverScene):
    def construct(self):
        """Main method that orchestrates the entire Russell's Paradox video with voiceover"""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_visualization()
        self.show_definition()
        self.show_naive_vs_axiomatic()
    
    def show_title(self):
        """Display the main title: Russell's Paradox"""
        # Create the "Russell's Paradox" title
        title = Text(
            "Russell's Paradox",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=title.get_corner(DOWN + LEFT),
            end=title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(title, underline)), run_time=1)
        self.wait(1)
    
    def show_visualization(self):
        """Show visual demonstration of Russell's Paradox with circles and objects"""
        with self.voiceover(text="Imagine a set containing everything. Everything in the universe, everything you can imagine, all the combined knowledge of everyone on earth and more. We'll call this set omega.") as tracker:
            # Large circle to represent a set
            large_circle = Circle(
                radius=2.9,
                color="#00396B",
                stroke_width=6,
                fill_opacity=0
            )
            large_circle.move_to(ORIGIN)
            
            # Show the circle first
            self.play(Create(large_circle), run_time=2)
            
            # Create simple geometric objects instead of SVGs for better compatibility
            statue = SVGMobject("images/statue-of-liberty-svgrepo-com.svg").scale(0.3)
            statue.move_to(UP * 1.7 + LEFT * 0.2)
            statue_label = Text("🗽", font_size=20).move_to(statue.get_center())
            
            carrot = SVGMobject("images/carrot-svgrepo-com.svg").scale(0.3)
            carrot.move_to(UP * 0.8 + LEFT * 1.8)
            carrot_label = Text("🥕", font_size=20).move_to(carrot.get_center())
            
            bicycle = SVGMobject("images/bycicle-svgrepo-com.svg").scale(0.3)
            bicycle.move_to(DOWN * 0.2 + LEFT * 1.5)
            bicycle_label = Text("🚲", font_size=20).move_to(bicycle.get_center())
            
            piano = SVGMobject("images/piano-svgrepo-com.svg").scale(0.3)
            piano.move_to(UP * 0.7 + RIGHT * 0.6)
            piano_label = Text("🎹", font_size=20).move_to(piano.get_center())
            
            books = SVGMobject("images/books-svgrepo-com.svg").scale(0.3)
            books.move_to(UP * 1.3 + RIGHT * 1.8)
            books_label = Text("📚", font_size=20).move_to(books.get_center())
            
            palm_tree = SVGMobject("images/coconut-tree-svgrepo-com.svg").scale(0.3)
            palm_tree.move_to(DOWN * 1.5 + RIGHT * 0.8)
            palm_tree_label = Text("🌴", font_size=20).move_to(palm_tree.get_center())
            
            # Group objects with their labels
            objects = [
                VGroup(statue, statue_label),
                VGroup(carrot, carrot_label),
                VGroup(bicycle, bicycle_label),
                VGroup(piano, piano_label),
                VGroup(books, books_label),
                VGroup(palm_tree, palm_tree_label)
            ]
            
            # Show objects one by one
            for obj in objects:
                self.play(FadeIn(obj), run_time=0.5)
            
            # Add Omega label outside the circle
            omega_label = MathTex(r'\mathbf{\Omega}', font_size=60, color="#00396B")
            omega_label.move_to(RIGHT * 3.5 + UP * 1.5)
            
            # Show omega label
            self.play(Write(omega_label), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 7.0)

        with self.voiceover(text="Because omega contains everything and it itself is something, then we have this interesting property that omega contains itself. This leads to a kind of infinite regress of omegas within omegas.") as tracker:
            # Add "Ω ∈ Ω" text at the bottom first
            omega_in_omega = MathTex(r'\mathbf{\Omega \in \Omega}', font_size=48, color=BLACK)
            omega_in_omega.move_to(DOWN * 3.2 + LEFT * 4.0)
            
            # Show the paradox statement
            self.play(Write(omega_in_omega), run_time=2)
            
            # Create smaller circle inside the large circle
            small_circle = Circle(
                radius=0.8,
                color="#00396B",
                stroke_width=4,
                fill_opacity=0
            )
            small_circle.move_to(DOWN * 1.5 + LEFT * 0.6)
            
            # Create miniature versions of all objects for the small circle
            mini_objects = []
            for i, obj in enumerate(objects):
                mini_obj = obj.copy().scale(0.3)
                # Position mini objects in a circular pattern within the small circle
                angle = i * PI / 3
                radius = 0.4
                mini_obj.move_to(small_circle.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]))
                mini_objects.append(mini_obj)
            
            # Transform large circle and objects into small versions
            self.play(
                ReplacementTransform(large_circle.copy(), small_circle),
                *[ReplacementTransform(obj.copy(), mini_obj) for obj, mini_obj in zip(objects, mini_objects)],
                run_time=2.5
            )
            
            # Add arrow pointing from omega_in_omega to the small circle
            arrow = CurvedArrow(
                start_point=omega_in_omega.get_top() + UP * 0.2,
                end_point=small_circle.get_center() + DOWN * 0.2 + LEFT * 0.9,
                color=BLACK,
                stroke_width=3,
                tip_length=0.2,
                angle=-0.4
            )
            
            # Show arrow
            self.play(Create(arrow), run_time=1)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)
        
        # Clear everything before next section
        all_objects = [large_circle, omega_label, omega_in_omega, small_circle, arrow] + objects + mini_objects
        self.play(FadeOut(VGroup(*all_objects)), run_time=1)
        self.wait(1)
    
    def show_definition(self):
        """Show mathematical definition and paradox explanation"""
        with self.voiceover(text="To avoid this, we might change the definition of omega and let omega be the set containing all sets that do not contain themselves.") as tracker:
            # Definition text at top
            definition = Text(
                "Let Ω be the set containing all sets that do not contain \nthemselves",
                font_size=32, 
                color=BLACK
            )
            definition.to_edge(UP, buff=0.5)
            
            # Mathematical notation below definition
            math_def = MathTex(r"\Omega = \{x \mid x \notin x\}", font_size=50, color=BLACK)
            math_def.next_to(definition, DOWN, buff=0.8)
            
            # Animation sequence
            self.play(Write(definition), run_time=2)
            self.play(Write(math_def), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 3.5)

        with self.voiceover(text="Now assume omega isn't a member of itself. By definition then it must contain itself. If it does contain itself, well it can't contain itself. This is known as Russell's paradox.") as tracker:
            # Small circle (left side)
            small_circle = Circle(radius=0.7, color="#00396B", stroke_width=4)
            small_circle.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            # Large circle (right side) 
            large_circle = Circle(radius=1.4, color="#00396B", stroke_width=4)
            large_circle.move_to(RIGHT * 2.8 + DOWN * 0.5)
            
            # Labels
            not_in_label = MathTex(r"\Omega \notin \Omega", font_size=32, color=BLACK)
            not_in_label.next_to(small_circle, UP, buff=0.3)
            
            omega_label = MathTex(r"\Omega", font_size=40, color="#00396B")
            omega_label.next_to(large_circle, RIGHT, buff=0.3)
            
            # Arrow
            arrow = Arrow(small_circle.get_right(), large_circle.get_left(), 
                         color=BLACK, stroke_width=5, buff=0.3)
            
            # Elements for the contradiction
            inner_circle = Circle(radius=0.5, color="#00396B", stroke_width=3)
            inner_circle.move_to(large_circle.get_center() + DOWN * 0.3 + LEFT * 0.2)
            
            in_label = MathTex(r"\Omega \in \Omega", font_size=28, color=BLACK)
            in_label.move_to(large_circle.get_center() + UP * 0.6)
            
            # Paradox text in black with blue underline
            paradox_text = Text(
                "Russell's Paradox", 
                font_size=36, 
                color=BLACK,
                slant=ITALIC
            )
            paradox_text.to_corner(DR, buff=0.5)
            
            paradox_underline = Line(
                start=paradox_text.get_corner(DOWN + LEFT),
                end=paradox_text.get_corner(DOWN + RIGHT),
                color=BLUE,
                stroke_width=2
            )
            paradox_underline.shift(DOWN * 0.1)
            
            self.play(Create(small_circle), Write(not_in_label), run_time=1.5)
            self.play(Create(arrow), run_time=1)
            self.play(Create(large_circle), Write(omega_label), run_time=1.5)
            
            # Show the contradiction
            self.play(
                ReplacementTransform(small_circle.copy(), inner_circle),
                Write(in_label),
                run_time=2
            )
            
            # Reveal the paradox with blue underline
            self.play(Write(paradox_text), run_time=2)
            self.play(Create(paradox_underline), run_time=1)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        # Clear everything before next section
        all_elements = [
            definition, math_def, small_circle, large_circle, not_in_label,
            omega_label, arrow, inner_circle, in_label, paradox_text, paradox_underline
        ]
        self.play(FadeOut(VGroup(*all_elements)), run_time=1)
        self.wait(1)
    
    def show_naive_vs_axiomatic(self):
        """Show comparison between naive and axiomatic set theory"""
        with self.voiceover(text="In fact, this is less a problem with how we've built the set and more a problem of how we define what a set is in the first place. Naive set theory in general does not give any guidance on what constitutes a set. Mostly we don't need to worry about this, but as you've seen, it can lead to problems. Axiomatic set theory aims to navigate the paradoxes of naive set theory by providing a rigorous definition of what a set is in the form of a list of axioms - statements something must satisfy in order to be a set.") as tracker:
            # First text block about naive set theory
            naive_text = Text(
                "Naive set theory in general does not give any\nguidance on what constitutes a set",
                font_size=32,
                color=BLACK,
                line_spacing=1.2
            )
            naive_text.to_edge(UP, buff=1.5).to_edge(LEFT, buff=1)
            
            # Second text block about axiomatic set theory  
            axiomatic_text = Text(
                "Axiomatic set theory aims to navigate the paradoxes\nof naive set theory by providing a rigorous definition\nof what a set is.",
                font_size=32,
                color=BLACK,
                line_spacing=1.2
            )
            axiomatic_text.move_to(DOWN * 0.8).to_edge(LEFT, buff=1)
            
            # Write both texts line by line without pauses
            self.play(
                AddTextLetterByLetter(naive_text, run_time=3),
                AddTextLetterByLetter(axiomatic_text, run_time=4, rate_func=rate_functions.linear),
                lag_ratio=0.3
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 7.0)
        
        self.wait(2)