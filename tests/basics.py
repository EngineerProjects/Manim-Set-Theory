from manim import *

class SetTheoryIntroExact(Scene):
    def construct(self):
        self.camera.background_color = "#F0F0F0"
        
        main_title = Text(
            "Set Theory",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        main_title.shift(UP * 2)
        
        underline = Line(
            start=main_title.get_corner(DOWN + LEFT),
            end=main_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        
        self.play(AddTextLetterByLetter(main_title), run_time=2)
        self.wait(0.5)
        self.play(Create(underline), run_time=1)
        self.wait(1)
        
        youtube_blue = "#1853A2"
        
        youtube_bg = RoundedRectangle(
            height=0.4,
            width=0.6,
            corner_radius=0.12,
            color=youtube_blue,
            fill_opacity=0.1,
        )
        
        play_triangle = Triangle(color=youtube_blue, fill_opacity=1)
        play_triangle.scale(0.12)
        play_triangle.rotate(-90 * DEGREES)
        play_triangle.move_to(youtube_bg.get_center())
        
        youtube_logo = VGroup(youtube_bg, play_triangle)
        
        full_name = "Stephane KPOVIESSI"
        author_name = Text(
            full_name,
            font_size=20,
            color=BLACK,
            font="DejaVu Serif",
            slant=ITALIC
        )
        
        # Position the logo and text in bottom right
        author_name.to_corner(DR, buff=0.6)
        
        # Position logo to the left of text
        youtube_logo.next_to(author_name, LEFT, buff=0.2)
        
        # Save initial positions for reference
        initial_text_bottom = author_name.get_bottom()
        initial_text_right = author_name.get_right()
        final_logo_pos = author_name.get_right() + LEFT * (youtube_logo.width/2)
        
        # Initial animation
        self.play(
            FadeIn(youtube_logo),
            Write(author_name),
            run_time=1.5
        )
        self.wait(1.5)
        
        # Deletion animation
        for i in range(len(full_name)):
            if i < len(full_name) - 1:  # Not the last character
                new_text = Text(
                    full_name[i+1:],
                    font_size=20,
                    color=BLACK,
                    font="DejaVu Serif",
                    slant=ITALIC
                )
                
                # Maintain the right and bottom alignment
                new_text.align_to(author_name, RIGHT)
                new_text.align_to(author_name, DOWN)
                
                # Calculate where the logo should be
                logo_pos = new_text.get_left() + LEFT * (youtube_logo.width/2 + 0.2)
                
                self.play(
                    Transform(author_name, new_text),
                    youtube_logo.animate.move_to(logo_pos).align_to(new_text, DOWN),
                    run_time=0.06  # Very fast animation
                )
        
        # Final animation - remove the last character and position logo correctly
        self.play(
            FadeOut(author_name),
            youtube_logo.animate.move_to(final_logo_pos).align_to(initial_text_bottom, DOWN),
            run_time=0.1
        )
        
        self.wait(2)

class SetDefinition(Scene):
    def construct(self):
        # Same background color as previous scene
        self.camera.background_color = "#F0F0F0"
        
        # Create the definition text
        definition = Text(
            "A set is a collection of objects (elements).",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        
        # Shift the text more to the left
        definition.to_edge(UP, buff=2.0)
        definition.shift(LEFT * 1)
        
        # Create a circle with dark blue outline
        circle = Circle(
            radius=2.5,  
            color="#00396B",  
            stroke_width=3.0,
            fill_opacity=0
        )
        
        # Position the circle below the text
        circle.next_to(definition, DOWN, buff=0.5)

        # Group everything and shift up
        group = VGroup(definition, circle)
        group.shift(UP * 1.0)

        # Load the car SVG from file - position on the LEFT side of the circle
        car = SVGMobject("images/car-svgrepo-com.svg")
        # Keep original colors - don't set color
        car.scale(0.3)  # Make it smaller
        # Position on the left side of the circle
        car.move_to(circle.get_center() + LEFT * 1.5)
        
        # Load the atom SVG from file - position at the BOTTOM of the circle
        atom = SVGMobject("images/atom-symbol-svgrepo-com.svg")
        atom.set_color(BLACK)
        atom.set_fill(BLACK, 1)
        atom.scale(0.4)  # Make it smaller
        # Position at the bottom of the circle
        atom.move_to(circle.get_center() + DOWN * 1.5)
        
        # Create the equation - position on the RIGHT side of the circle
        equation = MathTex(r"\mathbf{1 + 1 = 2}", color=BLACK)
        equation.scale(0.8)
        # Position on the right side of the circle
        equation.move_to(circle.get_center() + RIGHT * 1.0)
        
        # Animation sequence
        # 1. Initial text and circle
        self.play( 
            Write(definition),
            Create(circle),
            run_time=2
        )
        self.wait(1)
        
        # 2. Add the car
        self.play(FadeIn(car), run_time=1)
        self.wait(2)
        
        # 3. Add the atom
        self.play(FadeIn(atom), run_time=1)
        self.wait(3)
        
        # 4. Add the equation
        self.play(Write(equation), run_time=1)
        
        # Hold the final scene
        self.wait(2)


class SetOfTriangles(Scene):
    def construct(self):
        # Same background color as previous scene
        self.camera.background_color = "#F0F0F0"
        
        # Create a circle with dark blue outline
        circle = Circle(
            radius=2,  
            color="#00396B",  
            stroke_width=3.0,
            fill_opacity=0
        )
        
        # Position the circle in the center
        circle.shift(RIGHT * 1)
        
        # Create the text "The set of all triangles"
        set_text = Text(
            "The set of all\ntriangles",
            font_size=36,
            color=BLACK,
            font="sans-serif",
            weight=BOLD
        )
        
        # Position the text to the left of the circle
        set_text.move_to(LEFT * 4.5 + UP * 2)
        
        arrow = CurvedArrow(
            start_point=set_text.get_right() + RIGHT * 0.5 + UP * 0.1,
            end_point=circle.get_left() + UP * 0.8,
            color=BLACK,
            angle=-0.7,
            tip_length=0.2 
        )
        
        # Create the first green triangle (small equilateral) - BOLDER
        small_triangle = Triangle(color="#008000", stroke_width=4.0)
        small_triangle.scale(0.4)
        small_triangle.move_to(circle.get_center() + UP * 0.7) 
        
        # Create the second green triangle (right triangle) - BOLDER
        right_triangle = Polygon(
            [0, 0, 0],
            [1.5, 0, 0],
            [0, 0.8, 0],
            color="#008000", 
            stroke_width=4.0
        )
        right_triangle.move_to(circle.get_center() + DOWN * 0.4)
        
        # Create the red pentagon - BOLDER
        pentagon = RegularPolygon(5, color="#FF0000", stroke_width=4.0)
        pentagon.scale(0.7) 
        pentagon.move_to(RIGHT * 5 + UP * 1.2)
        
        # Create the "3 sides" text with checkmark - MOVED COMPLETELY TO THE LEFT
        sides_text = Text(
            "3 sides",
            font_size=30,
            color="#666666",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        sides_text.move_to(LEFT * 4.5 + DOWN * 2.5)  # Moved to the far left
        
        # Load the checkmark SVG from file - POSITIONED CLOSER
        check = SVGMobject("images/check.svg")
        check.set_color("#008000")  # Ensure it's green
        check.scale(0.3)
        check.next_to(sides_text, RIGHT, buff=0.2)  # Reduced buffer to 0.2
        
        # Create the "sum of internal angles is 360°" text with X mark - BOLD
        angles_text = Text(
            "sum of internal\nangles is 360°",
            font_size=30,
            color="#666666",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        angles_text.move_to(RIGHT * 4 + DOWN * 2.5)
        
        # Load the X mark SVG from file - POSITIONED CLOSER
        x_mark = SVGMobject("images/cross.svg")
        x_mark.set_color("#FF0000")  # Ensure it's red
        x_mark.scale(0.3)
        x_mark.next_to(angles_text, RIGHT, buff=0.2)  # Reduced buffer to 0.2

        # Start of animation
        self.play(Create(circle), run_time=1.5)
        self.wait(1)
        
        self.play(Write(set_text), run_time=1.5)
        self.play(Create(arrow), run_time=1)
        self.wait(1)
        
        self.play(Create(small_triangle), run_time=1)
        self.wait(1.5)
        
        self.play(Create(right_triangle), run_time=1)
        self.wait(3)
        
        self.play(Create(pentagon), run_time=1)
        self.wait(2)
        
        # Add the "3 sides" text with checkmark
        self.play(
            Write(sides_text),
            FadeIn(check),
            run_time=1.5
        )
        self.wait(3.5)
        
        # Add the "sum of internal angles" text with X mark
        self.play(
            Write(angles_text),
            FadeIn(x_mark),
            run_time=1.5
        )
        
        # Hold the final scene
        self.wait(2)

class SetNotation(Scene):
    def construct(self):
        # Same background color as previous scene
        self.camera.background_color = "#F0F0F0"
        
        # First text explaining set notation
        explanation1 = Text(
            "A set containing the numbers 1, 2, 3\nwould be written",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        # Position more towards the top and align left
        explanation1.to_edge(UP, buff=1.0)
        explanation1.to_edge(LEFT, buff=2.0)
        
        # The set notation in mathematical format
        set_notation = MathTex(
            r"\{ 1, 2, 3 \}",
            font_size=48,
            color=BLACK
        )
        # Center horizontally, place below the first explanation
        set_notation.next_to(explanation1, DOWN, buff=1.0)
        
        # The second explanatory text
        explanation2 = Text(
            "We can also name the set.",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        # Align with the first explanation on the left
        explanation2.next_to(set_notation, DOWN, buff=1.5)
        explanation2.to_edge(LEFT, buff=2.0)
        
        # The named set notation
        named_set = MathTex(
            r"A = \{ 1, 2, 3 \}",
            font_size=48,
            color=BLACK
        )
        # Center horizontally, place below the second explanation
        named_set.next_to(explanation2, DOWN, buff=1.0)
        
        # Animation sequence
        # 1. Show the first explanation
        self.play(Write(explanation1), run_time=2)
        self.wait(2.5)  # Wait between animations
        
        # 2. Show the set notation
        self.play(Write(set_notation), run_time=1.5)
        self.wait(2.5)  # Wait between animations
        
        # 3. Show the second explanation
        self.play(Write(explanation2), run_time=1.5)
        self.wait(2.5)  # Wait between animations
        
        # 4. Show the named set
        self.play(Write(named_set), run_time=1.5)
        
        # Hold the final scene
        self.wait(3)


class ElementOfSymbol(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Create first line
        line1 = MarkupText(
            '<b><i>To express symbolically that an element</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Create second line (without symbol)
        line2 = MarkupText(
            '<b><i>belongs to a set we use </i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Create the symbol
        symbol_part = MarkupText(
            '<b><i> ∈</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position everything correctly
        line1.to_edge(UP, buff=1.0)
        line1.to_edge(LEFT, buff=0.5)
        
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.1)
        symbol_part.next_to(line2, RIGHT, buff=0.2)
        
        # Group them for initial animation
        full_text = VGroup(line1, line2, symbol_part)
        
        self.play(Write(full_text), run_time=1)
        self.wait(1.5)
        
        # Create highlight effect
        dimmed_line1 = line1.copy().set_opacity(0.15)
        dimmed_line2 = line2.copy().set_opacity(0.15)
        
        self.play(
            ReplacementTransform(line1, dimmed_line1),
            ReplacementTransform(line2, dimmed_line2),
            run_time=1
        )
        
        self.wait(2)  
        
        # Continue with examples
        # "For example:"
        example_text = MarkupText(
            '<b><i>For example:</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        example_text.next_to(dimmed_line2, DOWN, aligned_edge=LEFT, buff=0.8)
        
        self.play(Write(example_text), run_time=1)
        self.wait(1)
        
        # "If A = {1, 2, 3},"
        set_definition = MarkupText(
            '<b><i>If A = {1, 2, 3},</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        set_definition.next_to(example_text, DOWN, aligned_edge=LEFT, buff=0.5)
        set_definition.shift(RIGHT * 1.5)  # Indent slightly
        
        self.play(Write(set_definition), run_time=1)
        self.wait(1)
        
        # "then 1 ∈ A, 2 ∈ A" - LEFT SIDE FIRST
        membership_math = MarkupText(
            '<b><i>then 1 ∈ A, 2 ∈ A</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        membership_math.next_to(set_definition, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # "1 in A, 2 in A" - RIGHT SIDE
        membership_english = MarkupText(
            '<b><i>"1 in A, 2 in A"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        membership_english.move_to(RIGHT * 3 + membership_math.get_center()[1] * UP)
        
        # Write left side first
        self.play(Write(membership_math), run_time=1)
        self.wait(0.3)  # Short pause
        # Then write right side
        self.play(Write(membership_english), run_time=1)
        self.wait(1)
        
        # "but 4 ∉ A" - LEFT SIDE FIRST
        non_membership_math = MarkupText(
            '<b><i>but 4 ∉ A</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        non_membership_math.next_to(membership_math, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # "4 not in A" - RIGHT SIDE
        non_membership_english = MarkupText(
            '<b><i>"4 not in A"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        non_membership_english.move_to(RIGHT * 3 + non_membership_math.get_center()[1] * UP)
        
        # Write left side first
        self.play(Write(non_membership_math), run_time=1)
        self.wait(0.3)  # Short pause
        # Then write right side
        self.play(Write(non_membership_english), run_time=1)
        
        # Hold the final scene
        self.wait(3)

class SetBuilderNotation(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # First sentence with underlined "set builder notation"
        intro_line1 = MarkupText(
            '<b><i>In most cases we don\'t write out all the</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line2 = MarkupText(
            '<b><i>elements in a set but will write a shorthand</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line3 = MarkupText(
            '<b><i>description using </i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Underlined "set builder notation"
        underlined_text = MarkupText(
            '<b><i><u>set builder notation</u>.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the first paragraph
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        intro_line3.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.1)
        underlined_text.next_to(intro_line3, RIGHT, buff=0.1)
        
        # Show first paragraph
        self.play(
            Write(VGroup(intro_line1, intro_line2, intro_line3, underlined_text)), 
            run_time=2
        )
        self.wait(3) 
        
        # Second sentence
        example_intro = MarkupText(
            '<b><i>For example the set of prime numbers</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        example_intro2 = MarkupText(
            '<b><i>could be written as</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position below first paragraph with more space
        example_intro.next_to(intro_line3, DOWN, aligned_edge=LEFT, buff=0.8)
        example_intro2.next_to(example_intro, DOWN, aligned_edge=LEFT, buff=0.1)
        
        self.play(
            Write(VGroup(example_intro, example_intro2)), 
            run_time=1.5
        )
        self.wait(2)  # 2 second wait
        
        # Mathematical notation - LEFT SIDE
        math_notation = MarkupText(
            '<b><i>P = {p | p is a prime}</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        math_notation.next_to(example_intro2, DOWN, buff=0.8)
        math_notation.shift(RIGHT * 1.5)  # Center it more
        
        # English explanation - RIGHT SIDE  
        english_explanation = MarkupText(
            '<b><i>"p such that p is a prime"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        english_explanation.next_to(math_notation, DOWN, buff=0.6)
        english_explanation.shift(RIGHT * 0.5)  # Center it more
        
        self.play(Write(math_notation), run_time=1.5)
        self.wait(0.3)
 
        self.play(Write(english_explanation), run_time=1.5)
        self.wait(2) 
        
        # Add arrow pointing to the predicate part and label
        predicate_label = MarkupText(
            '<b><i>Predicate</i></b>',
            color="#1853A2",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the label to the right of the math notation
        predicate_label.move_to(math_notation.get_right() + RIGHT * 1.5 + UP * 1.2)
        
        # Create curved arrow pointing from label to the "p is a prime" part
        arrow = CurvedArrow(
            start_point=predicate_label.get_bottom() + DOWN * 0.1 + LEFT * 0.3,
            end_point=math_notation.get_center() + RIGHT * 1.2, 
            color="#1853A2",  
            angle=0.6,  
            tip_length=0.1
        )
        # Animate the arrow and label
        self.play(
            Create(arrow),
            Write(predicate_label),
            run_time=1.5
        )

        self.wait(4)


class NumberSetsDeclaration(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Introduction text - split into lines for better positioning
        intro_line1 = MarkupText(
            '<b><i>Its good practice when dealing with sets of</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line2 = MarkupText(
            '<b><i>numbers to declare explicitly which sets you</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line3 = MarkupText(
            '<b><i>are starting with</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the introduction text
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        intro_line3.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show introduction text
        self.play(
            Write(VGroup(intro_line1, intro_line2, intro_line3)), 
            run_time=2
        )
        self.wait(3)  # 3 second wait
        
        # Mathematical comparison using MathTex for proper symbol rendering
        natural_set = MathTex(
            r'\{p \in \mathbb{N} \mid p < 5\}',
            font_size=42,
            color="#505050"
        )
        
        # Not equal symbol
        not_equal = MathTex(
            r'\neq',
            font_size=42,
            color="#505050"
        )
        
        # Right side: Real numbers
        real_set = MathTex(
            r'\{r \in \mathbb{R} \mid r < 5\}',
            font_size=42,
            color="#505050"
        )
        
        # Position the mathematical notation in the center
        math_group = VGroup(natural_set, not_equal, real_set)
        math_group.arrange(RIGHT, buff=0.3)
        math_group.move_to(ORIGIN)
        
        # Show the mathematical notation
        self.play(Write(natural_set), run_time=1.5)
        self.wait(0.5)
        
        self.play(Write(not_equal), run_time=1)
        self.wait(0.5)
        
        self.play(Write(real_set), run_time=1.5)
        
        # Hold the final scene
        self.wait(4)

class SetEquality(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Introduction text - split into lines for better positioning
        intro_line1 = MarkupText(
            '<b><i>Two sets are equal if they both contain</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line2 = MarkupText(
            '<b><i>the same elements.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the introduction text
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show introduction text
        self.play(
            Write(VGroup(intro_line1, intro_line2)), 
            run_time=2
        )
        self.wait(0.5)  # Short wait
        
        # Create A and B labels positioned lower and with more separation
        label_A = MarkupText(
            '<b><i>A</i></b>',
            color="#00396B",  # Blue color
            font_size=28,
            font="sans-serif"
        )
        
        label_B = MarkupText(
            '<b><i>B</i></b>',
            color="#008000",  # Green color
            font_size=28,
            font="sans-serif"
        )
        
        # Position A and B labels lower and higher within future circles
        label_A.move_to(LEFT * 2.5 + DOWN * 1.2)  
        label_B.move_to(RIGHT * 2.5 + DOWN * 1.2) 
        
        # Show A and B labels at the same time
        self.play(
            Write(label_A),
            Write(label_B),
            run_time=1
        )
        
        # Create circles around A and B
        circle_A = Circle(
            radius=1.5,
            color="#00396B",  
            stroke_width=3.0,
            fill_opacity=0
        )
        # Position circle so A appears in upper part
        circle_A.move_to(label_A.get_center() + DOWN * 0.8)
        
        circle_B = Circle(
            radius=1.5,
            color="#008000", 
            stroke_width=3.0,
            fill_opacity=0
        )
        # Position circle so B appears in upper part
        circle_B.move_to(label_B.get_center() + DOWN * 0.8)
        
        # Show circles at the same time
        self.play(
            Create(circle_A),
            Create(circle_B),
            run_time=1.5
        )
        self.wait(1)
        
        # Now add the mathematical definition text in the middle
        def_line1 = MarkupText(
            '<b><i>If for all a ∈ A, a ∈ B and for all b ∈ B, b ∈</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        
        def_line2 = MarkupText(
            '<b><i>A, then A = B.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        
        # Position the definition text between intro and circles
        def_line1.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.8)
        def_line2.next_to(def_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show definition text
        self.play(
            Write(VGroup(def_line1, def_line2)), 
            run_time=2.5
        )
        self.wait(1)
        
        # Add lowercase "a" and "b" inside both circles
        element_a_in_A = MarkupText(
            '<b><i>a</i></b>',
            color="#505050",
            font_size=24,
            font="sans-serif"
        )
        
        element_b_in_A = MarkupText(
            '<b><i>b</i></b>',
            color="#505050",
            font_size=24,
            font="sans-serif"
        )
        
        element_a_in_B = MarkupText(
            '<b><i>a</i></b>',
            color="#505050",
            font_size=24,
            font="sans-serif"
        )
        
        element_b_in_B = MarkupText(
            '<b><i>b</i></b>',
            color="#505050",
            font_size=24,
            font="sans-serif"
        )
        
        # Position elements inside the circles
        element_a_in_A.move_to(circle_A.get_center() + LEFT * 0.5 + UP * 0.3)
        element_b_in_A.move_to(circle_A.get_center() + LEFT * 0.5 + DOWN * 0.3)
        element_a_in_B.move_to(circle_B.get_center() + LEFT * 0.5 + UP * 0.3)
        element_b_in_B.move_to(circle_B.get_center() + LEFT * 0.5 + DOWN * 0.3)
        
        # Show elements at the same time
        self.play(
            Write(VGroup(element_a_in_A, element_b_in_A, element_a_in_B, element_b_in_B)),
            run_time=1
        )
        self.wait(0.5)
        
        # Add first arrow from element_a in A to element_a in B
        arrow_a = CurvedArrow(
            start_point=element_a_in_A.get_right() + RIGHT * 0.2,
            end_point=element_a_in_B.get_left() + LEFT * 0.2,
            color="#505050",
            angle=0.15,
            tip_length=0.2
        )
        
        # Show the first arrow
        self.play(Create(arrow_a), run_time=1)
        self.wait(1)
        
        # Underline "and" in blue
        and_underline = Line(
            start=def_line1.get_center() + RIGHT * 0.1 + DOWN * 0.3,
            end=def_line1.get_center() + RIGHT * 1 + DOWN * 0.3,
            color="#1853A2",  # Blue color
            stroke_width=3
        )
        
        # Show the underline
        self.play(Create(and_underline), run_time=1)
        self.wait(1)
        
        # Add second arrow from element_b in B to element_b in A (reverse direction)
        arrow_b = CurvedArrow(
            start_point=element_b_in_B.get_left() + LEFT * 0.2,
            end_point=element_b_in_A.get_right() + RIGHT * 0.2,
            color="#505050",
            angle=0.15,
            tip_length=0.2
        )
        
        # Show the second arrow
        self.play(Create(arrow_b), run_time=1)
        
        # Hold the final scene
        self.wait(4)


class OrderDoesntMatter(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Introduction text
        intro_line1 = MarkupText(
            '<b><i>This definition means that the order of the</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line2 = MarkupText(
            '<b><i>elements doesn\'t matter</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the introduction text
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show introduction text
        self.play(Write(VGroup(intro_line1, intro_line2)), run_time=2)
        self.wait(1)
        
        # Create set A and set B with better indexing
        set_A = MathTex(r'A', r'=', r'\{', r'1', r',', r'2', r',', r'3', r'\}', font_size=48, color="#505050")
        set_B = MathTex(r'B', r'=', r'\{', r'2', r',', r'3', r',', r'1', r'\}', font_size=48, color="#505050")
        
        # Position the sets
        set_A.move_to(LEFT * 3 + DOWN * 0.5)
        set_B.move_to(RIGHT * 3 + DOWN * 0.5)
        
        # Show sets
        self.play(Write(set_A), run_time=1.5)
        self.wait(0.5)
        self.play(Write(set_B), run_time=1.5)
        self.wait(1)
        
        # Create arrows from A to B (curving downward) - starting from bottom of elements
        # Arrow from "1" in A to "1" in B
        arrow_A_to_B_1 = CurvedArrow(
            start_point=set_A[3].get_bottom(),  # Bottom of "1" in A
            end_point=set_B[7].get_bottom(),    # Bottom of "1" in B (last position)
            color="#505050",
            angle=PI/3,  # Negative angle for downward curve
            tip_length=0.15
        )
        
        # Arrow from "2" in A to "2" in B  
        arrow_A_to_B_2 = CurvedArrow(
            start_point=set_A[5].get_bottom(),  # Bottom of "2" in A
            end_point=set_B[3].get_bottom(),    # Bottom of "2" in B (first position)
            color="#505050",
            angle=PI/2.5,  # Negative angle for downward curve
            tip_length=0.15
        )
        
        # Arrow from "3" in A to "3" in B
        arrow_A_to_B_3 = CurvedArrow(
            start_point=set_A[7].get_bottom(),  # Bottom of "3" in A
            end_point=set_B[5].get_bottom(),    # Bottom of "3" in B (middle position)
            color="#505050",
            angle=PI/2,  # Negative angle for downward curve
            tip_length=0.15
        )
        
        # Show arrows A to B sequentially
        self.play(Create(arrow_A_to_B_1), run_time=1)
        self.wait(1)
        self.play(Create(arrow_A_to_B_2), run_time=1)
        self.wait(1)
        self.play(Create(arrow_A_to_B_3), run_time=1)
        self.wait(2)
        
        # Now create reverse arrows from B to A (curving upward) - starting from top of elements
        # Arrow from "2" in B to "2" in A
        arrow_B_to_A_2 = CurvedArrow(
            start_point=set_B[3].get_top(),     # Top of "2" in B (first position)
            end_point=set_A[5].get_top(),       # Top of "2" in A
            color="#FF6B6B",  # Different color to distinguish
            angle=PI/2.5,  # Positive angle for upward curve
            tip_length=0.15
        )
        
        # Arrow from "3" in B to "3" in A
        arrow_B_to_A_3 = CurvedArrow(
            start_point=set_B[5].get_top(),     # Top of "3" in B (middle position)
            end_point=set_A[7].get_top(),       # Top of "3" in A
            color="#FF6B6B",  # Different color to distinguish
            angle=PI/2,  # Positive angle for upward curve
            tip_length=0.15
        )
        
        # Arrow from "1" in B to "1" in A
        arrow_B_to_A_1 = CurvedArrow(
            start_point=set_B[7].get_top(),     # Top of "1" in B (last position)
            end_point=set_A[3].get_top(),       # Top of "1" in A
            color="#FF6B6B",  # Different color to distinguish
            angle=PI/3,  # Positive angle for upward curve
            tip_length=0.15
        )
        
        # Show reverse arrows B to A sequentially
        self.play(Create(arrow_B_to_A_2), run_time=1)
        self.wait(1)
        self.play(Create(arrow_B_to_A_3), run_time=1)
        self.wait(1)
        self.play(Create(arrow_B_to_A_1), run_time=1)
        self.wait(2)
        
        # Show conclusion: A = B
        conclusion = MathTex(r'A = B', font_size=48, color="#505050")
        conclusion.move_to(DOWN * 2.5)
        
        self.play(Write(conclusion), run_time=1.5)
        self.wait(3)


class RepeatedElementsDontMatter(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Introduction text
        intro_line1 = MarkupText(
            '<b><i>It also doesn\'t matter if elements are</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line2 = MarkupText(
            '<b><i>repeated</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the introduction text
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show introduction text
        self.play(Write(VGroup(intro_line1, intro_line2)), run_time=2)
        self.wait(1)
        
        # Create set A and set B with repeated elements in B
        set_A = MathTex(r'A', r'=', r'\{', r'1', r',', r'2', r',', r'3', r'\}', font_size=48, color="#505050")
        set_B = MathTex(r'B', r'=', r'\{', r'2', r',', r'3', r',', r'3', r',', r'3', r',', r'1', r'\}', font_size=48, color="#505050")
        
        # Position the sets
        set_A.move_to(LEFT * 3 + DOWN * 0.5)
        set_B.move_to(RIGHT * 3 + DOWN * 0.5)
        
        # Show sets
        self.play(Write(set_A), run_time=1.5)
        self.wait(0.5)
        self.play(Write(set_B), run_time=1.5)
        self.wait(1)
        
        # Create arrows from A to B (curving downward)
        # Arrow from "1" in A to "1" in B (last element)
        arrow_A_to_B_1 = CurvedArrow(
            start_point=set_A[3].get_bottom(),  # Bottom of "1" in A
            end_point=set_B[11].get_bottom(),   # Bottom of "1" in B (last position)
            color="#505050",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        # Arrow from "2" in A to "2" in B (first element)
        arrow_A_to_B_2 = CurvedArrow(
            start_point=set_A[5].get_bottom(),  # Bottom of "2" in A
            end_point=set_B[3].get_bottom(),    # Bottom of "2" in B (first position)
            color="#505050",
            angle=PI/3,
            tip_length=0.15
        )
        
        # Arrow from "3" in A to first "3" in B
        arrow_A_to_B_3 = CurvedArrow(
            start_point=set_A[7].get_bottom(),  # Bottom of "3" in A
            end_point=set_B[5].get_bottom(),    # Bottom of first "3" in B
            color="#505050",
            angle=PI/4,
            tip_length=0.15
        )
        
        # Show arrows A to B sequentially
        self.play(Create(arrow_A_to_B_1), run_time=1)
        self.wait(1)
        self.play(Create(arrow_A_to_B_2), run_time=1)
        self.wait(1)
        self.play(Create(arrow_A_to_B_3), run_time=1)
        self.wait(2)
        
        # Create reverse arrows from B to A (curving upward)
        # Arrow from "2" in B to "2" in A
        arrow_B_to_A_2 = CurvedArrow(
            start_point=set_B[3].get_top(),     # Top of "2" in B
            end_point=set_A[5].get_top(),       # Top of "2" in A
            color="#FF6B6B",
            angle=PI/3,
            tip_length=0.15
        )
        
        # Arrow from first "3" in B to "3" in A
        arrow_B_to_A_3_1 = CurvedArrow(
            start_point=set_B[5].get_top(),     # Top of first "3" in B
            end_point=set_A[7].get_top(),       # Top of "3" in A
            color="#FF6B6B",
            angle=PI/4,
            tip_length=0.15
        )
        
        # Arrow from second "3" in B to "3" in A
        arrow_B_to_A_3_2 = CurvedArrow(
            start_point=set_B[7].get_top(),     # Top of second "3" in B
            end_point=set_A[7].get_top(),       # Top of "3" in A
            color="#FF6B6B",
            angle=PI/3.5,
            tip_length=0.15
        )
        
        # Arrow from third "3" in B to "3" in A
        arrow_B_to_A_3_3 = CurvedArrow(
            start_point=set_B[9].get_top(),     # Top of third "3" in B
            end_point=set_A[7].get_top(),       # Top of "3" in A
            color="#FF6B6B",
            angle=PI/3,
            tip_length=0.15
        )
        
        # Arrow from "1" in B to "1" in A
        arrow_B_to_A_1 = CurvedArrow(
            start_point=set_B[11].get_top(),    # Top of "1" in B
            end_point=set_A[3].get_top(),       # Top of "1" in A
            color="#FF6B6B",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        # Show reverse arrows B to A sequentially
        self.play(Create(arrow_B_to_A_2), run_time=1)
        self.wait(1)
        # Show all three arrows from the 3's in B to the single 3 in A
        self.play(
            Create(arrow_B_to_A_3_1), 
            Create(arrow_B_to_A_3_2), 
            Create(arrow_B_to_A_3_3), 
            run_time=1.5
        )
        self.wait(1)
        self.play(Create(arrow_B_to_A_1), run_time=1)
        self.wait(2)
        
        # Show conclusion: A = B with checkmark
        conclusion_text = MathTex(r'A = B', font_size=48, color="#505050")
        conclusion_text.move_to(DOWN * 2.5 + LEFT * 0.5)
        
        # Load the checkmark SVG
        checkmark = SVGMobject("images/check.svg")
        checkmark.set_color("#008000")  # Green color
        checkmark.scale(0.4)
        checkmark.next_to(conclusion_text, RIGHT, buff=0.3)
        
        self.play(Write(conclusion_text), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(checkmark), run_time=1)
        self.wait(4)


class SetCardinality(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
        # Title text
        title_line1 = MarkupText(
            '<b><i>The size or cardinality of a set is the</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        title_line2 = MarkupText(
            '<b><i>number of elements it contains.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the title text
        title_line1.to_edge(UP, buff=1.0)
        title_line1.to_edge(LEFT, buff=0.5)
        title_line2.next_to(title_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show title text
        self.play(Write(VGroup(title_line1, title_line2)), run_time=2)
        self.wait(2)
        
        # First example: A = {1, 2, 3}
        set_A = MathTex(r'A = \{1, 2, 3\}', font_size=48, color="#505050")
        set_A.move_to(LEFT * 2.5 + DOWN * 0.5)
        
        # Show A = {1, 2, 3}
        self.play(Write(set_A), run_time=1.5)
        self.wait(1)  # 1 second wait as requested
        
        # Cardinality of A
        cardinality_A = MathTex(r'|A| = 3', font_size=48, color="#505050")
        cardinality_A.move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        # Show |A| = 3
        self.play(Write(cardinality_A), run_time=1.5)
        self.wait(2)
        
        # Second example: P = {p | p is a prime}
        set_P = MathTex(r'P = \{p \mid p \text{ is a prime}\}', font_size=48, color="#505050")
        set_P.move_to(LEFT * 2.5 + DOWN * 2.5)
        
        # Show P = {p | p is a prime}
        self.play(Write(set_P), run_time=1.5)
        self.wait(1)  # 1 second wait as requested
        
        # Cardinality of P (infinity)
        cardinality_P = MathTex(r'|P| = \infty', font_size=48, color="#505050")
        cardinality_P.move_to(RIGHT * 2.5 + DOWN * 2.5)
        
        # Show |P| = ∞
        self.play(Write(cardinality_P), run_time=1.5)
        
        # Hold the final scene
        self.wait(3)