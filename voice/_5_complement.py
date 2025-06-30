from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class TheComplementWithVoiceover(VoiceoverScene):
    def construct(self):
        """Main method that orchestrates the entire video with voiceover"""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_set_difference_introduction()
        self.show_set_difference_examples()
        self.show_complement_definition()
        self.show_universal_set_complement()
        self.show_dice_complement_example()
        self.show_complement_examples()
        self.show_complement_predicate_negation()
        self.show_properties_title()
        self.show_complement_properties_list()
        self.show_complement_property_4()
    
    def show_title(self):
        """Display the main title: The Complement"""
        # Create the "The Complement" title
        complement_title = Text(
            "The Complement",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        complement_title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=complement_title.get_corner(DOWN + LEFT),
            end=complement_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(complement_title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(complement_title, underline)), run_time=1)
        self.wait(1)
    
    def show_set_difference_introduction(self):
        """Show set difference introduction with Venn diagram"""
        with self.voiceover(text="The set-theoretic difference of two sets A and B is a set of all elements in A that aren't in B. It's usually denoted by A backslash B and can be thought of as like subtracting B from A.") as tracker:
            # Definition text at the top - split into two lines
            definition_line1 = MarkupText(
                '<b><i>The set-theoretic difference of two sets A and B</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            definition_line2 = MarkupText(
                '<b><i>is the set of all elements in A that aren\'t in B.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            # Position definition text at the top
            definition_line1.to_edge(UP, buff=1.0)
            definition_line1.to_edge(LEFT, buff=0.5)
            definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show definition text
            self.play(Write(definition_line1), run_time=2.5)
            self.play(Write(definition_line2), run_time=2)
            
            # === VENN DIAGRAM ===
            
            # Circle A (blue, overlapping)
            circle_A = Circle(
                radius=1.8,
                color="#00396B",  # Blue
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(LEFT * 1.0 + DOWN * 1.7)
            
            # Circle B (green, overlapping)
            circle_B = Circle(
                radius=1.8,
                color="#008000",  # Green
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.move_to(RIGHT * 1.0 + DOWN * 1.7)
            
            # Labels
            label_A = Text("A", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + LEFT * 0.5 + UP * 1.2)
            
            label_B = Text("B", font_size=32, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + RIGHT * 0.5 + UP * 1.2)
            
            # Create circles and labels
            self.play(
                Create(circle_A),
                Create(circle_B),
                Write(label_A),
                Write(label_B),
                run_time=2.5
            )
            
            # === FILL A \ B (A minus intersection with B) ===
            
            # Create the difference A \ B
            a_minus_b = Difference(circle_A, circle_B)
            a_minus_b.set_fill(color="#A0A0A0", opacity=0.6)
            a_minus_b.set_stroke(width=0)
            
            # Show the filled difference
            self.play(FadeIn(a_minus_b), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        with self.voiceover(text="We can write this formally as A backslash B equals the set of x in A such that x is not in B.") as tracker:
            # === ADD MATHEMATICAL FORMULA ===
            
            formula = MathTex(
                r'A \setminus B = \{ x \in A \mid x \notin B \}',
                font_size=40,
                color="#505050"
            )
            formula.move_to(UP * 1.0)
            
            # Show the formula
            self.play(Write(formula), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.5)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                definition_line1, definition_line2, circle_A, circle_B,
                label_A, label_B, a_minus_b, formula
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_set_difference_examples(self):
        """Show examples of set difference"""
        with self.voiceover(text="For example, if A equals a set containing one, two, three, four, and five, and B is the set containing two, four, six, and eight, then A minus B is the set containing one, three, and five, since we've removed the two and the four that were in B.") as tracker:
            # "For example:" header
            example_header = MarkupText(
                '<b><i>For example:</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            example_header.to_edge(UP, buff=1.5)
            example_header.to_edge(LEFT, buff=1.0)
            
            # Show example header
            self.play(Write(example_header), run_time=1.5)
            
            # Given sets
            given_sets = MathTex(
                r'\text{If } A = \{1, 2, 3, 4, 5\} \text{ and } B = \{2, 4, 6, 8\}',
                font_size=56,
                color="#505050"
            )
            given_sets.next_to(example_header, DOWN * 0.5, buff=1.5)
            given_sets.move_to([0, given_sets.get_center()[1], 0])  # Center horizontally
            
            # Show given sets
            self.play(Write(given_sets), run_time=2.5)
            
            # A \ B result
            a_minus_b = MathTex(
                r'A \setminus B = \{1, 3, 5\}',
                font_size=56,
                color="#505050"
            )
            a_minus_b.next_to(given_sets, DOWN * 0.5, buff=1.5)
            a_minus_b.move_to([0, a_minus_b.get_center()[1], 0])  # Center horizontally
            
            # Show A \ B
            self.play(Write(a_minus_b), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        with self.voiceover(text="B minus A is six and eight, since we've again removed two and four.") as tracker:
            # B \ A result
            b_minus_a = MathTex(
                r'B \setminus A = \{6, 8\}',
                font_size=56,
                color="#505050"
            )
            b_minus_a.next_to(a_minus_b, DOWN * 0.5, buff=1.5)
            b_minus_a.move_to([0, b_minus_a.get_center()[1], 0])  # Center horizontally
            
            # Show B \ A
            self.play(Write(b_minus_a), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(example_header, given_sets, a_minus_b, b_minus_a)),
            run_time=1
        )
        self.wait(1)
    
    def show_complement_definition(self):
        """Show complement definition with Venn diagram"""
        with self.voiceover(text="If B is a subset of A, the set-theoretic difference of A and B is called the complement of B with respect to A.") as tracker:
            # Definition text at the top - split into two lines
            definition_line1 = MarkupText(
                '<b><i>If B ⊆ A, the set-theoretic difference of A and B is</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            definition_line2 = MarkupText(
                '<b><i>called the </i></b><u><b><i>complement</i></b></u><b><i> of B with respect to A.</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            # Position definition text at the top
            definition_line1.to_edge(UP, buff=1.0)
            definition_line1.to_edge(LEFT, buff=0.5)
            definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show definition text
            self.play(Write(definition_line1), run_time=2.5)
            self.play(Write(definition_line2), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.0)
        
        with self.voiceover(text="It's usually denoted with a superscript c above the subset B, or as C with B in brackets like a function. Why is this important enough to give it its own name? Well, it's kind of like a background to be the things outside of B in general.") as tracker:
            # === VENN DIAGRAM (IMAGE 1) ===
            
            # Circle A (larger, blue)
            circle_A = Circle(
                radius=2.2,
                color="#00396B",  # Blue
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(DOWN * 0.8)
            
            # Circle B (smaller, green, inside A)
            circle_B = Circle(
                radius=1.0,
                color="#008000",  # Green
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.move_to(circle_A.get_center() + RIGHT * 0.5 + DOWN * 0.3)
            
            # Labels
            label_A = Text("A", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + LEFT * 1.5 + UP * 0.8)
            
            label_B = Text("B", font_size=32, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center())
            
            # Create circles and labels
            self.play(
                Create(circle_A),
                Create(circle_B),
                Write(label_A),
                Write(label_B),
                run_time=2.5
            )
            
            # Fill the complement (A \ B) with gray
            complement_region = Difference(circle_A, circle_B)
            complement_region.set_fill(color="#A0A0A0", opacity=0.9)
            complement_region.set_stroke(width=0)
            
            # Show the complement region
            self.play(FadeIn(complement_region), run_time=2)
            
            # === ADD NOTATION (IMAGE 2) ===
            
            # B^c label with arrow
            bc_label = MathTex(r'B^c', font_size=32, color="#505050")
            bc_label.move_to(circle_A.get_center() + LEFT * 4.0 + UP * 0.5)
            
            # Arrow pointing to complement region
            arrow_to_complement = Arrow(
                start=bc_label.get_right() + RIGHT * 0.1,
                end=circle_A.get_center() + LEFT * 1.2,
                color="#505050",
                buff=0.1,
                stroke_width=2,
                tip_length=0.15
            )
            
            # Show B^c notation
            self.play(
                Write(bc_label),
                Create(arrow_to_complement),
                run_time=2
            )
            
            # Alternative notation at bottom right
            alternative_notation = MarkupText(
                '<i>Can be written C(B)</i>',
                color="#8B4B8B",  # Purple/magenta color
                font_size=28,
                font="sans-serif"
            )
            alternative_notation.to_edge(DOWN, buff=1.0)
            alternative_notation.to_edge(RIGHT, buff=1.0)
            
            # Show alternative notation
            self.play(Write(alternative_notation), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.5)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                definition_line1, definition_line2, circle_A, circle_B,
                label_A, label_B, complement_region, bc_label,
                arrow_to_complement, alternative_notation
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_universal_set_complement(self):
        """Show universal set and complement"""
        with self.voiceover(text="Here is where we introduce the universal set. The universal set U is a set of all elements that are relevant for some given topic of interest.") as tracker:
            # Definition at the top
            definition = MarkupText(
                '<b><i>The universal set (U) is the set of all elements.</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            definition.to_edge(UP, buff=1.0)
            
            # Show definition
            self.play(Write(definition), run_time=2.5)
            
            # === STEP 1: UNIVERSAL SET RECTANGLE FIRST ===
            
            # Universal set U (rounded rectangle) - NO FILL initially
            universal_rect = RoundedRectangle(
                width=6,
                height=3,
                corner_radius=0.3,
                color="#00396B",  # Blue border
                stroke_width=4.0,
                fill_opacity=0  # No fill initially
            )
            universal_rect.move_to(DOWN * 0.3)
            
            # Label U
            label_U = Text("U", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_U.move_to(universal_rect.get_corner(UP + LEFT) + DOWN * 0.3 + RIGHT * 0.3)
            
            # Show rectangle and U label first
            self.play(
                Create(universal_rect),
                Write(label_U),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)
        
        with self.voiceover(text="If our set A isn't the subset of something specific, we usually assume the complement of A is the universal set, and what that universal set is depends on context.") as tracker:
            # === STEP 2: ADD CIRCLE A ===
            
            # Circle A (white, inside U)
            circle_A = Circle(
                radius=0.5,
                color="#008000",  # Green border
                stroke_width=4.0,
                fill_opacity=0  # No fill initially
            )
            circle_A.move_to(universal_rect.get_center() + RIGHT * 1.3 + DOWN * 0.4)
            
            # Label A
            label_A = Text("A", font_size=28, color="#008000", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center())
            
            # Show circle A
            self.play(
                Create(circle_A),
                Write(label_A),
                run_time=2
            )
            
            # === STEP 3: FILL COMPLEMENT REGION WITH GRAY ===
            
            # Create complement region (rectangle minus circle)
            complement_region = Difference(universal_rect, circle_A)
            complement_region.set_fill(color="#A0A0A0", opacity=0.6)
            complement_region.set_stroke(width=0)
            
            # Fill the complement region
            self.play(FadeIn(complement_region), run_time=2)
            
            # === STEP 4: ADD A^c NOTATION ===
            
            # A^c label with arrow
            ac_label = MathTex(r'A^c', font_size=32, color="#505050")
            ac_label.move_to(universal_rect.get_center() + UP * 2.2 + LEFT * 0.5)
            
            # Curved arrow pointing to complement region
            arrow_to_complement = CurvedArrow(
                start_point=ac_label.get_bottom() + DOWN * 0.1,
                end_point=universal_rect.get_center() + LEFT * 1.5 + UP * 1.2,
                color="#505050",
                angle=-0.3,
                tip_length=0.15,
                stroke_width=2
            )
            
            # Show A^c notation
            self.play(
                Write(ac_label),
                Create(arrow_to_complement),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.0)
        
        with self.voiceover(text="This quote from The Foundations of Mathematics by Stewart and Tall sums it up nicely: In a discussion about dogs, when thinking about all non-sheepdogs, it's pointless to worry about camels.") as tracker:
            # === STEP 5: HUMOROUS QUOTE AT BOTTOM ===
            
            quote_line1 = MarkupText(
                '<i>"In a discussion about dogs, when thinking about all</i>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            quote_line2 = MarkupText(
                '<i>non-sheepdogs, it\'s pointless to worry about camels"</i>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            # Position quote at bottom
            quote_line1.to_edge(DOWN, buff=1.2)
            quote_line1.to_edge(LEFT, buff=0.5)
            quote_line2.next_to(quote_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show quote
            self.play(Write(quote_line1), run_time=2.5)
            self.play(Write(quote_line2), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                definition, universal_rect, label_U, circle_A, label_A,
                complement_region, ac_label, arrow_to_complement,
                quote_line1, quote_line2
            )),
            run_time=1
        )
        self.wait(1)
    
    def create_die_face(self, number, size=0.25):
        """Create a die face with the specified number of dots"""
        square = Square(side_length=size, color=BLACK, stroke_width=2)
        square.set_fill(WHITE, opacity=1)
        
        dots = VGroup()
        positions = {
            1: [(0, 0)],
            2: [(-0.06, 0.06), (0.06, -0.06)],
            3: [(-0.06, 0.06), (0, 0), (0.06, -0.06)],
            4: [(-0.06, 0.06), (0.06, 0.06), (-0.06, -0.06), (0.06, -0.06)],
            5: [(-0.06, 0.06), (0.06, 0.06), (0, 0), (-0.06, -0.06), (0.06, -0.06)],
            6: [(-0.06, 0.06), (0.06, 0.06), (-0.06, 0), (0.06, 0), (-0.06, -0.06), (0.06, -0.06)]
        }
        
        for pos in positions[number]:
            dot = Dot(point=[pos[0], pos[1], 0], radius=0.015, color=BLACK)
            dots.add(dot)
        
        return VGroup(square, dots)
    
    def create_dice_pair(self, num1, num2):
        """Create a pair of dice"""
        die1 = self.create_die_face(num1)
        die2 = self.create_die_face(num2)
        die2.next_to(die1, RIGHT, buff=0.03)
        return VGroup(die1, die2)
    
    def show_dice_complement_example(self):
        """Show dice complement example with Venn diagram"""
        with self.voiceover(text="Imagine we're throwing two dice. Let A be the set of outcomes of rolling a pair of dice in which both dice show the same number. A sensible universal set in this case would be the set of all possible outcomes of rolling two dice.") as tracker:
            # Definition text at the top - split into two lines
            definition_line1 = MarkupText(
                '<b><i>Let A be the set of outcomes of rolling a pair of</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            definition_line2 = MarkupText(
                '<b><i>dice in which both dice show the same number.</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            # Position definition text at the top
            definition_line1.to_edge(UP, buff=1.0)
            definition_line1.to_edge(LEFT, buff=0.5)
            definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show definition text
            self.play(Write(definition_line1), run_time=2.5)
            self.play(Write(definition_line2), run_time=2)
            
            # === STEP 1: GREEN RECTANGLE FIRST ===
            
            # Green boundary for set A (smaller size)
            set_A_boundary = RoundedRectangle(
                width=3.5,  # Reduced size
                height=1.8,  # Reduced size
                corner_radius=0.3,
                color="#008000",  # Green
                stroke_width=4.0,
                fill_opacity=0
            )
            set_A_boundary.move_to(DOWN * 1.3)
            
            # Show boundary first
            self.play(Create(set_A_boundary), run_time=2)
            
            # Label A positioned relative to rectangle
            label_A = Text("A", font_size=28, color="#008000", font="sans-serif", weight=BOLD)
            label_A.move_to(set_A_boundary.get_corner(UP + RIGHT) + LEFT * 0.4 + DOWN * 0.3)
            
            # Show label
            self.play(Write(label_A), run_time=1.5)
            
            # === STEP 2: ADD DICE PAIRS POSITIONED RELATIVE TO RECTANGLE ===
            
            same_numbers = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
            dice_pairs = []
            
            # Get rectangle center and dimensions for relative positioning
            rect_center = set_A_boundary.get_center()
            rect_width = set_A_boundary.width
            rect_height = set_A_boundary.height
            
            # Calculate positions relative to rectangle (2 rows of 3, centered)
            for i, (num1, num2) in enumerate(same_numbers):
                pair = self.create_dice_pair(num1, num2)
                
                row = i // 3
                col = i % 3
                
                # Position relative to rectangle center
                x_offset = (col - 1) * (rect_width * 0.25) 
                y_offset = (row - 0.5) * (rect_height * 0.4)
                
                pair.move_to(rect_center + RIGHT * x_offset + UP * y_offset)
                dice_pairs.append(pair)
            
            # Show each dice pair one by one
            for pair in dice_pairs:
                self.play(FadeIn(pair), run_time=0.8)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 12.8)

        with self.voiceover(text="And the complement of A would be the outcomes where each die shows a different number.") as tracker:
            # === STEP 3: MOVE SET A TO RIGHT CENTER FIRST ===
            
            # Calculate new position for A (where it will be within the future U)
            new_rect_position = RIGHT * 3.5 + DOWN * 0.6  # Right center position
            
            # Calculate displacement
            displacement = new_rect_position - set_A_boundary.get_center()
            
            # Create new versions in new positions
            new_set_A_boundary = set_A_boundary.copy()
            new_set_A_boundary.move_to(new_rect_position)
            
            new_label_A = label_A.copy()
            new_label_A.shift(displacement)
            
            new_dice_pairs = []
            for pair in dice_pairs:
                new_pair = pair.copy()
                new_pair.shift(displacement)
                new_dice_pairs.append(new_pair)
            
            # Smooth animation moving everything to the right first
            animations = [
                ReplacementTransform(set_A_boundary, new_set_A_boundary),
                ReplacementTransform(label_A, new_label_A)
            ]
            
            for i, pair in enumerate(dice_pairs):
                animations.append(ReplacementTransform(pair, new_dice_pairs[i]))
            
            self.play(*animations, run_time=2)
            
            # Update references
            set_A_boundary = new_set_A_boundary
            label_A = new_label_A
            dice_pairs = new_dice_pairs
            
            # === STEP 4: ADD UNIVERSAL SET U AROUND SET A ===
            
            # Universal set U (big blue rectangle around the moved A)
            universal_set_U = RoundedRectangle(
                width=12,  # Much wider
                height=4,  # Taller
                corner_radius=0.3,
                color="#00396B",  # Blue
                stroke_width=4.0,
                fill_opacity=0
            )
            universal_set_U.move_to(ORIGIN + DOWN * 0.6)  # Centered on screen
            
            # Show universal set
            self.play(Create(universal_set_U), run_time=2)
            
            # === STEP 5: ADD LABEL U AND CREATE VGROUP ===
            
            # Label U
            label_U = Text("U", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_U.move_to(universal_set_U.get_corner(UP + LEFT) + RIGHT * 0.4 + DOWN * 0.3)
            
            # Show label U
            self.play(Write(label_U), run_time=1.5)
            
            # Create VGroup structure
            set_A_group = VGroup(set_A_boundary, label_A, *dice_pairs)
            universal_group = VGroup(universal_set_U, label_U, set_A_group)

            # === STEP 6: ADD COMPLEMENT DICE PAIRS (A^c) WITH DECREASING COLUMNS ===
            
            # Create all possible dice combinations for the complement (where dice show different numbers)
            complement_pairs = []
            
            # Generate all combinations where dice show different numbers
            for first_die in range(1, 7):
                for second_die in range(1, 7):
                    if first_die != second_die:  # Different numbers (complement of A)
                        complement_pairs.append((first_die, second_die))
            
            # Create dice pair objects for complement
            complement_dice_objects = []
            
            # Get universal set dimensions and position for relative positioning
            u_center = universal_set_U.get_center()
            u_left = universal_set_U.get_left()[0]
            u_width = universal_set_U.width
            u_height = universal_set_U.height
            
            # Arrange in decreasing columns: 6, 5, 4, 3, 2 elements per column
            column_heights = [6, 5, 4, 3, 2, 1]  # Each column has one fewer element
            pair_index = 0
            
            # Same starting y-position for all columns
            y_start = u_center[1] + 1.5  # Top position for all columns
            
            for col, height in enumerate(column_heights):
                for row in range(height):
                    if pair_index < len(complement_pairs):
                        num1, num2 = complement_pairs[pair_index]
                        pair = self.create_dice_pair(num1, num2)
                        
                        # Position with increased spacing
                        x_offset = u_left + 1.0 + col * 1.0
                        # All columns start from same top position
                        y_offset = y_start - row * 0.6
                        
                        pair.move_to([x_offset, y_offset, 0])
                        complement_dice_objects.append(pair)
                        pair_index += 1
            
            # Show complement dice pairs VERTICALLY (column by column)
            current_index = 0
            for col, height in enumerate(column_heights):
                column_pairs = complement_dice_objects[current_index:current_index + height]
                current_index += height
                
                # Show entire column at once
                if column_pairs:
                    self.play(*[FadeIn(pair) for pair in column_pairs], run_time=0.8)
            
            # Update the universal group to include complement
            complement_group = VGroup(*complement_dice_objects)
            universal_group.add(complement_group)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 10.8)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(definition_line1, definition_line2, universal_group)),
            run_time=1
        )
        self.wait(1)
    
    def show_complement_examples(self):
        """Show other examples of complements"""
        with self.voiceover(text="Here are some other examples of complements. The complement of the set of odd numbers is the even numbers, and the complement of the rational numbers is the set of irrational numbers.") as tracker:
            # Title at the top
            title = MarkupText(
                '<b><i>Some other examples of complements...</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            title.to_edge(UP, buff=1.5)
            title.to_edge(LEFT, buff=0.5)
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # === FIRST EXAMPLE: ODD/EVEN NUMBERS ===
            
            # First example - split into parts for proper spacing
            example1 = MathTex(
                r'\{ x \in \mathbb{N} \mid x \text{ is odd} \}^c',
                r'=',
                r'\{ x \in \mathbb{N} \mid x \text{ is even} \}',
                font_size=46,
                color="#505050"
            )
            example1.move_to(UP * 0.8)
            example1.to_edge(LEFT, buff=0.5)
            
            # Show first example
            self.play(Write(example1), run_time=2.5)
            
            # === SECOND EXAMPLE: RATIONAL/IRRATIONAL NUMBERS ===
            
            # Second example - split into parts for proper spacing
            example2 = MathTex(
                r'\{ x \in \mathbb{R} \mid x \in \mathbb{Q} \}^c',
                r'=',
                r'\{ x \in \mathbb{R} \mid x \text{ is irrational} \}',
                font_size=46,
                color="#505050"
            )
            example2.move_to(DOWN * 0.8)
            example2.to_edge(LEFT, buff=0.5)
            
            # Show second example
            self.play(Write(example2), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 7.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(title, example1, example2)),
            run_time=1
        )
        self.wait(1)
    
    def show_complement_predicate_negation(self):
        """Show how complement negates the predicate"""
        with self.voiceover(text="Notice with the complement we often get something that feels like the opposite of the original set, and that's because the complement negates the predicate.") as tracker:
            # Title at the top
            title = MarkupText(
                '<b><i>The complement negates the predicate.</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            title.to_edge(UP, buff=1.0)
            title.to_edge(LEFT, buff=0.5)
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # === GENERAL FORMULAS ===
            
            # General set definition
            general_formula = MathTex(
                r'A = \{ x \in B \mid P \}',
                font_size=36,
                color="#505050"
            )
            general_formula.move_to(UP * 1.2)
            
            # Complement formula with negation
            complement_formula = MathTex(
                r'A^c = \{ x \in B \mid \neg P \}',
                font_size=36,
                color="#505050"
            )
            complement_formula.move_to(UP * 0.3)
            
            # Show formulas
            self.play(Write(general_formula), run_time=2)
            self.play(Write(complement_formula), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        with self.voiceover(text="With our set builder notation, we have a set A which contains all x from some set B such that it fulfills some predicate P. Well, the complement of A, the things not in A, must by definition not satisfy P. So the complement of A is the elements x in B such that P isn't true.") as tracker:
            # === VENN DIAGRAM CIRCLES ===
            
            # Animals circle (outer, blue)
            animals_circle = Circle(
                radius=1.3,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            animals_circle.move_to(RIGHT * 3 + DOWN * 1.5)
            
            # Dogs circle (inner, green) - positioned relative to animals circle
            dogs_circle = Circle(
                radius=0.6,
                color="#008000",
                stroke_width=4.0,
                fill_opacity=0
            )
            dogs_circle.move_to(animals_circle.get_center() + RIGHT * 0.4)
            
            # Labels positioned relative to circles
            animals_label = MathTex(r'\text{Animals}', font_size=20, color="#00396B")
            animals_label.move_to(animals_circle.get_center() + UP * 1.0)
            
            dogs_label = MathTex(r'\text{Dogs}', font_size=18, color="#008000")
            dogs_label.move_to(dogs_circle.get_center() + UP * 0.3)
            
            # Show circles and labels
            self.play(
                Create(animals_circle),
                Create(dogs_circle),
                Write(animals_label),
                Write(dogs_label),
                run_time=2.5
            )
            
            # === SPECIFIC EXAMPLE TEXT ===
            
            # Specific example
            example_text = MathTex(
                r'A = \{ \text{Animals that are dogs} \}',
                font_size=32,
                color="#505050"
            )
            example_text.move_to(DOWN * 1.5 + LEFT * 2.7)
            
            # Show example text
            self.play(Write(example_text), run_time=2)
            
            # === CURVED ARROW ===
            
            # Curved arrow from example text to dogs circle
            connecting_arrow = CurvedArrow(
                start_point=example_text.get_right() + RIGHT * 0.2,
                end_point=dogs_circle.get_left() + LEFT * 0.2,
                color="#505050",
                angle=-0.3,
                tip_length=0.15,
                stroke_width=2
            )
            
            # Show curved arrow
            self.play(Create(connecting_arrow), run_time=1.5)

            # === FILL COMPLEMENT REGION WITH GRAY ===
            
            # Create complement region (Animals - Dogs)
            complement_region = Difference(animals_circle, dogs_circle)
            complement_region.set_fill(color="#A0A0A0", opacity=0.6)
            complement_region.set_stroke(width=0)
            
            # Fill the complement area
            self.play(FadeIn(complement_region), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 10.0)
        
        with self.voiceover(text="For example, if A is the set of animals that are dogs, then the complement of A is animals that are not dogs.") as tracker:
            # === ADD COMPLEMENT EXAMPLE TEXT ===
            
            # Complement example text
            complement_example = MathTex(
                r'A^c = \{ \text{Animals that are not dogs} \}',
                font_size=32,
                color="#505050"
            )
            complement_example.next_to(example_text, DOWN, buff=0.8)
            
            # Show complement example text
            self.play(Write(complement_example), run_time=2.5)
            
            # === CURVED ARROW TO COMPLEMENT REGION ===
            
            # Curved arrow from complement text to gray area
            complement_arrow = CurvedArrow(
                start_point=complement_example.get_right() + RIGHT * 0.2,
                end_point=dogs_circle.get_center(),
                color="#505050",
                angle=0.3,
                tip_length=0.15,
                stroke_width=2
            )
            
            # Show complement arrow
            self.play(Create(complement_arrow), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, general_formula, complement_formula, animals_circle,
                dogs_circle, animals_label, dogs_label, example_text,
                connecting_arrow, complement_region, complement_example, complement_arrow
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_properties_title(self):
        """Display the properties title"""
        # Create the "Properties of Complements" title
        properties_title = Text(
            "Properties of Complements",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        properties_title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=properties_title.get_corner(DOWN + LEFT),
            end=properties_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(properties_title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(properties_title, underline)), run_time=1)
        self.wait(1)
    
    def show_complement_properties_list(self):
        """Show complement properties list with Venn diagram"""
        with self.voiceover(text="Let A and B be subsets of the universal set U. Because nothing is in the empty set, its complement is U. Similarly, the complement of U, which contains everything, is the empty set. Here's an interesting one: the complement of the complement of a set returns the original set.") as tracker:
            # === IMAGE 1: PROPERTIES LIST ===
            
            # Statement at the top
            statement = MarkupText(
                '<b><i>Let A and B be subsets of the universal set U.</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            statement.to_edge(UP, buff=1.0)
            statement.to_edge(LEFT, buff=0.5)
            
            # Properties list (bold LaTeX)
            properties = VGroup(
                MathTex(r'\mathbf{1. \quad \varnothing^c = U}', font_size=36, color="#505050"),
                MathTex(r'\mathbf{2. \quad U^c = \varnothing}', font_size=36, color="#505050"),
                MathTex(r'\mathbf{3. \quad (A^c)^c = A}', font_size=36, color="#505050")
            )
            properties.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
            properties.to_edge(LEFT, buff=0.5)
            properties.move_to(properties.get_center() + DOWN * 0.5)
            
            # Show statement and properties
            self.play(Write(statement), run_time=2)
            for prop in properties:
                self.play(Write(prop), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)
        
        with self.voiceover(text="That's because taking the complement of A leaves all the things in U but not in A. Taking the complement again, we can see that all that's left in U but not in our current set is A.") as tracker:
            # === IMAGE 2: ADD UNIVERSAL SET U WITH CIRCLE A ===
            
            # Universal set U
            universal_rect = RoundedRectangle(
                width=5,
                height=2.5,
                corner_radius=0.3,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            universal_rect.move_to(RIGHT * 2.5 + DOWN * 0.8)
            
            # Circle A inside U
            circle_A = Circle(
                radius=0.6,
                color="#008000",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(universal_rect.get_center() + RIGHT * 0.8)
            
            # Labels
            label_U = MathTex(r'\mathbf{U}', font_size=28, color="#00396B")
            label_U.move_to(universal_rect.get_corner(UP + LEFT) + RIGHT * 0.3 + DOWN * 0.3)
            
            label_A = MathTex(r'\mathbf{A}', font_size=24, color="#008000")
            label_A.move_to(circle_A.get_center())
            
            # Show universal set and A
            self.play(
                Create(universal_rect),
                Create(circle_A),
                Write(label_U),
                Write(label_A),
                run_time=2.5
            )
            
            # === IMAGE 3: FILL U WITH GRAY, ADD A^c LABEL ===
            
            # Fill complement region
            complement_region = Difference(universal_rect, circle_A)
            complement_region.set_fill(color="#A0A0A0", opacity=0.6)
            complement_region.set_stroke(width=0)
            
            # A^c label
            label_Ac = MathTex(r'\mathbf{A^c}', font_size=24, color="#505050")
            label_Ac.move_to(universal_rect.get_center() + LEFT * 1.2)
            
            # Fill and add label
            self.play(
                FadeIn(complement_region),
                Write(label_Ac),
                run_time=2
            )
            
            # === IMAGE 4: ADD CURVED ARROW ===
            
            # Curved arrow pointing to A circle
            curved_arrow = CurvedArrow(
                start_point=label_Ac.get_center() + RIGHT * 0.1 + UP * 0.2,
                end_point=circle_A.get_center() + UP * 0.2 + LEFT * 0.3,
                color="#505050",
                angle=-0.4,
                tip_length=0.15,
                stroke_width=2
            )
            
            # Show arrow
            self.play(Create(curved_arrow), run_time=1.5)
            
            # === IMAGE 5: REMOVE GRAY FROM RECTANGLE, FILL ONLY CIRCLE A ===
            
            # Fill A circle and remove complement region
            filled_A = circle_A.copy().set_fill(color="#A0A0A0", opacity=0.9)
            
            # Remove gray from complement and fill only A
            self.play(
                FadeOut(complement_region),
                ReplacementTransform(circle_A, filled_A),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                statement, properties, universal_rect, filled_A,
                label_U, label_A, label_Ac, curved_arrow
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_complement_property_4(self):
        """Show complement property 4 with visualization"""
        with self.voiceover(text="If A is a subset of B, then the complement of B is a subset of the complement of A. It's easy to show visually why this is true.") as tracker:
            # === EVERYTHING APPEARS TOGETHER WITH BORDERS ===
            
            # Property 4 text (bold)
            property4 = MathTex(
                r'\mathbf{4. \quad \text{If } A \subseteq B\text{, then } B^c \subseteq A^c}',
                font_size=36,
                color="#505050"
            )
            property4.to_edge(UP, buff=1.0)
            property4.to_edge(LEFT, buff=0.5)
            
            # Universal set U (positioned lower, WITH BORDERS)
            universal_rect = RoundedRectangle(
                width=5, height=2.5, corner_radius=0.3,
                color="#00396B", stroke_width=4.0, fill_opacity=0
            )
            universal_rect.move_to(DOWN * 1.5)
            
            # Circle B (larger, red, WITH BORDERS)
            circle_B = Circle(radius=1.0, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_B.move_to(universal_rect.get_center())
            
            # Circle A (smaller, green, inside B, WITH BORDERS) - NEVER FILLED
            circle_A = Circle(radius=0.5, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_A.move_to(circle_B.get_center() + LEFT * 0.3)
            
            # Labels
            label_U = MathTex(r'\mathbf{U}', font_size=28, color="#00396B")
            label_U.move_to(universal_rect.get_corner(UP + LEFT) + RIGHT * 0.3 + DOWN * 0.3)
            
            label_B = MathTex(r'\mathbf{B}', font_size=24, color="#CC0000")
            label_B.move_to(circle_B.get_center() + RIGHT * 0.6 + UP * 0.2)
            
            label_A = MathTex(r'\mathbf{A}', font_size=20, color="#008000")
            label_A.move_to(circle_A.get_center())
            
            # Show everything together
            self.play(
                Write(property4),
                Create(universal_rect), Create(circle_B), Create(circle_A),
                Write(label_U), Write(label_B), Write(label_A),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.5)
        
        with self.voiceover(text="Since everything in A is also in B, there are things in B that aren't in A. I'm assuming that they're not equal here. That means that these elements that are in B but not in A will turn up in the complement of A but not the complement of B. And so we end up with the complement of A containing everything in the complement of B and more.") as tracker:
            # === FILL B CIRCLE AND U RECTANGLE WITH SAME OPACITY ===
            
            # Fill B circle (temporary)
            filled_B = Difference(circle_B, circle_A)  # B minus A to ensure A never gets filled
            filled_B.set_fill(color="#A0A0A0", opacity=0.4)
            filled_B.set_stroke(width=0)
            
            # Fill U rectangle (temporary)
            filled_U_initial = Difference(universal_rect, Union(circle_A, circle_B))
            filled_U_initial.set_fill(color="#A0A0A0", opacity=0.4)
            filled_U_initial.set_stroke(width=0)
            
            self.play(
                FadeIn(filled_B),
                FadeIn(filled_U_initial),
                run_time=1.5
            )
            
            # === INCREASE ONLY RECTANGLE OPACITY (EXCLUDING CIRCLES) ===
            
            # Higher opacity for U area only (B^c area)
            u_higher_opacity = Difference(universal_rect, Union(circle_A, circle_B))
            u_higher_opacity.set_fill(color="#A0A0A0", opacity=0.7)
            u_higher_opacity.set_stroke(width=0)
            
            self.play(
                ReplacementTransform(filled_U_initial, u_higher_opacity),
                run_time=1.5
            )
            
            # === EXTRACT COLORS AND MOVE UP (NO BORDERS) ===
            
            # Create color-only versions (no borders) positioned above
            extracted_U_area = RoundedRectangle(
                width=5, height=2.5, corner_radius=0.3,
                color="#A0A0A0", stroke_width=0, fill_opacity=0.7
            ).move_to(UP * 1.1)
            
            extracted_B = Circle(
                radius=1.0, color="#A0A0A0", stroke_width=0, fill_opacity=0.4
            ).move_to(extracted_U_area.get_center())
            
            # White A hole (A stays unfilled)
            white_A_hole = Circle(
                radius=0.5, color="#F0F0F0", stroke_width=0, fill_opacity=1.0
            ).move_to(extracted_B.get_center() + LEFT * 0.3)
            
            # Labels and arrows
            ac_label = MathTex(r'\mathbf{A^c}', font_size=24, color="#505050")
            ac_label.move_to(LEFT * 3 + UP * 0.8)
            
            bc_label = MathTex(r'\mathbf{B^c}', font_size=24, color="#505050")
            bc_label.move_to(RIGHT * 3 + UP * 0.8)
            
            ac_arrow = Arrow(
                start=ac_label.get_right() + RIGHT * 0.1,
                end=white_A_hole.get_center() + LEFT * 0.3,
                color="#505050", buff=0.1, stroke_width=2, tip_length=0.15
            )
            
            bc_arrow = CurvedArrow(
                start_point=bc_label.get_left() + LEFT * 0.1,
                end_point=extracted_U_area.get_center() + RIGHT * 2,
                color="#505050", angle=0.3, tip_length=0.15, stroke_width=2
            )
            
            # Extract colors above AND remove fills from original (keeping borders)
            self.play(
                # Remove gray fills from original
                FadeOut(VGroup(filled_B, u_higher_opacity)),
                # Show extracted colors above
                FadeIn(VGroup(extracted_U_area, extracted_B, white_A_hole)),
                Write(ac_label), Write(bc_label),
                Create(ac_arrow), Create(bc_arrow),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)
        
        # Clear everything before ending
        self.play(
            FadeOut(VGroup(
                property4, universal_rect, circle_B, circle_A,
                label_U, label_B, label_A, extracted_U_area, extracted_B, white_A_hole,
                ac_label, bc_label, ac_arrow, bc_arrow
            )),
            run_time=1
        )
        self.wait(2)