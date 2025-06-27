from manim import *

class RussellsParadox(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
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
        self.wait(0.5)
        self.play(Create(underline), run_time=1)
        self.wait(2)

class RussellsParadoxVisualization(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
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
        self.wait(1)
        
        # Create SVG objects and position them inside the circle
        statue = SVGMobject("images/statue-of-liberty-svgrepo-com.svg", height=0.8, color=BLUE)
        statue.move_to(UP * 1.7 + LEFT * 0.2)
        
        carrot = SVGMobject("images/carrot-svgrepo-com.svg", height=0.6, color=ORANGE)
        carrot.move_to(UP * 0.8 + LEFT * 1.8)
        
        bicycle = SVGMobject("images/bycicle-svgrepo-com.svg", height=0.6, color=BLACK)
        bicycle.move_to(DOWN * 0.2 + LEFT * 1.5)
        
        piano = SVGMobject("images/piano-svgrepo-com.svg", height=0.6, color="#8B4513")
        piano.move_to(UP * 0.7 + RIGHT * 0.6)
        
        books = SVGMobject("images/books-svgrepo-com.svg", height=0.6, color=GRAY)
        books.move_to(UP * 1.3 + RIGHT * 1.8)
        
        palm_tree = SVGMobject("images/coconut-tree-svgrepo-com.svg", height=1.0, color=GREEN)
        palm_tree.move_to(DOWN * 1.5 + RIGHT * 0.8)
        
        # Show objects one by one
        self.play(FadeIn(statue), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(carrot), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(bicycle), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(piano), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(books), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(palm_tree), run_time=1)
        self.wait(3)

        # Add Omega label outside the circle
        omega_label = MathTex(r'\mathbf{\Omega}', font_size=60, color="#00396B")
        omega_label.move_to(RIGHT * 3.5 + UP * 1.5)
        
        # Show omega label
        self.play(Write(omega_label), run_time=1.5)
        self.wait(2)
        
        # Add "Ω ∈ Ω" text at the bottom first
        omega_in_omega = MathTex(r'\mathbf{\Omega \in \Omega}', font_size=48, color=BLACK)
        omega_in_omega.move_to(DOWN * 3.2 + LEFT * 4.0)
        
        # Show the paradox statement
        self.play(Write(omega_in_omega), run_time=2)
        self.wait(1)
        
        # Create smaller circle inside the large circle - moved to bottom left empty space
        small_circle = Circle(
            radius=0.8,
            color="#00396B",
            stroke_width=4,
            fill_opacity=0
        )
        small_circle.move_to(DOWN * 1.5 + LEFT * 0.6)
        
        # Create a copy of the large circle to transform into small circle
        large_circle_copy = large_circle.copy()
        
        # Create miniature versions of all objects for the small circle
        mini_statue = SVGMobject("images/statue-of-liberty-svgrepo-com.svg", height=0.25, color=BLUE)
        mini_statue.move_to(small_circle.get_center() + UP * 0.4 + LEFT * 0.1)
        
        mini_carrot = SVGMobject("images/carrot-svgrepo-com.svg", height=0.2, color=ORANGE)
        mini_carrot.move_to(small_circle.get_center() + UP * 0.1 + LEFT * 0.5)
        
        mini_bicycle = SVGMobject("images/bycicle-svgrepo-com.svg", height=0.2, color=BLACK)
        mini_bicycle.move_to(small_circle.get_center() + DOWN * 0.2 + LEFT * 0.4)
        
        mini_piano = SVGMobject("images/piano-svgrepo-com.svg", height=0.2, color="#8B4513")
        mini_piano.move_to(small_circle.get_center() + UP * 0.05 + RIGHT * 0.25)
        
        mini_books = SVGMobject("images/books-svgrepo-com.svg", height=0.2, color=GRAY)
        mini_books.move_to(small_circle.get_center() + UP * 0.25 + RIGHT * 0.45)
        
        mini_palm_tree = SVGMobject("images/coconut-tree-svgrepo-com.svg", height=0.3, color=GREEN)
        mini_palm_tree.move_to(small_circle.get_center() + DOWN * 0.4 + RIGHT * 0.15)
        
        # Create copies of all original objects to transform into mini versions
        statue_copy = statue.copy()
        carrot_copy = carrot.copy()
        bicycle_copy = bicycle.copy()
        piano_copy = piano.copy()
        books_copy = books.copy()
        palm_tree_copy = palm_tree.copy()
        
        # Transform large circle and objects into small versions using ReplacementTransform
        self.play(
            ReplacementTransform(large_circle_copy, small_circle),
            ReplacementTransform(statue_copy, mini_statue),
            ReplacementTransform(carrot_copy, mini_carrot),
            ReplacementTransform(bicycle_copy, mini_bicycle),
            ReplacementTransform(piano_copy, mini_piano),
            ReplacementTransform(books_copy, mini_books),
            ReplacementTransform(palm_tree_copy, mini_palm_tree),
            run_time=2.5
        )
        self.wait(1)
        
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
        self.wait(3)


class RussellsParadoxDefinition(Scene):
    def construct(self):
        self.camera.background_color = "#F0F0F0"
        
        # Definition text at top
        definition = Text(
            "Let Ω be the set containing all sets that do not contain \nthemselves",
            font_size=32, color=BLACK
        ).to_edge(UP, buff=0.5)
        
        # Mathematical notation below definition
        math_def = MathTex(r"\Omega = \{x \mid x \notin x\}", font_size=50, color=BLACK)
        math_def.next_to(definition, DOWN, buff=0.8)
        
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
        
        # Animation sequence
        self.play(Write(definition), run_time=2)
        self.play(Write(math_def), run_time=1.5)
        self.wait(1)
        
        self.play(Create(small_circle), Write(not_in_label), run_time=1.5)
        self.play(Create(arrow), run_time=1)
        self.play(Create(large_circle), Write(omega_label), run_time=1.5)
        self.wait(1)
        
        # Show the contradiction
        self.play(
            ReplacementTransform(small_circle.copy(), inner_circle),
            Write(in_label),
            run_time=2
        )
        self.wait(1)
        
        # Reveal the paradox with blue underline
        self.play(Write(paradox_text), run_time=2)
        self.play(Create(paradox_underline), run_time=1)
        self.wait(3)


class NaiveVsAxiomaticSetTheory(Scene):
    def construct(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        self.wait(5)