from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class UnionAndIntersectionWithVoiceover(VoiceoverScene):
    def construct(self):
        """Main method that orchestrates the entire video with voiceover"""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_introduction()
        self.show_explanation()
        self.show_union_definition()
        self.show_intersection_definition()
        self.show_examples()
        self.show_examples_2()
        self.show_union_properties()
        self.show_intersection_properties()
        self.show_cardinality()
        self.show_mixing_unions_intersections()
        self.show_distributive_laws_comparison()
        self.show_union_real_world_example()
        self.show_distributive_law_proof()
        self.show_shirts_venn_diagram()
    
    def show_title(self):
        """Display the main title: Union and Intersection"""
        # Create the "Union and Intersection" title
        union_intersection_title = Text(
            "Union and Intersection",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        union_intersection_title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=union_intersection_title.get_corner(DOWN + LEFT),
            end=union_intersection_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(union_intersection_title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(union_intersection_title, underline)), run_time=1)
        self.wait(1)
    
    def show_introduction(self):
        """Show introduction with sets A and B, then transition to Venn diagram"""
        with self.voiceover(text="Two sets may share some elements. We indicate the elements in common to both sets using the overlap of two circles in what's known as a Venn diagram. Let me show you set A containing one, two, three, four, five, and six.") as tracker:
            # === SET A GROUP ===
            # Set A definition
            set_A_text = MathTex(
                r'A = \{ 1, 2, 3, 4, 5, 6 \}',
                font_size=40,
                color="#00396B"  # Blue color
            )
            
            # Circle A - positioned directly under set A text
            circle_A = Circle(
                radius=2.0,
                color="#00396B",  # Blue color
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.next_to(set_A_text, DOWN, buff=1.0)
            
            # Label A inside the circle
            label_A = Text(
                "A",
                font_size=36,
                color="#00396B",
                font="sans-serif",
                weight=BOLD
            )
            label_A.move_to(circle_A.get_center() + UP * 1.5)
            
            # Numbers inside circle A
            numbers_A = VGroup()
            for i in range(6):
                number = Text(
                    str(i + 1),
                    font_size=32,
                    color="#505050",
                    font="sans-serif"
                )
                # Position numbers horizontally across the circle
                x_pos = circle_A.get_center()[0] + (i - 2.5) * 0.5
                y_pos = circle_A.get_center()[1]
                number.move_to([x_pos, y_pos, 0])
                numbers_A.add(number)
            
            # Group all A elements together
            group_A = VGroup(set_A_text, circle_A, label_A, numbers_A)
            
            # === POSITIONING ===
            # Position group A on the left
            group_A.move_to(LEFT * 3)
            
            # === ANIMATIONS ===
            # Show set A group
            self.play(Write(set_A_text), run_time=2)
            self.play(Create(circle_A), run_time=1.5)
            self.play(Write(label_A), run_time=1)
            self.play(Write(numbers_A), run_time=2)
            
            # Wait for remaining audio if needed
            self.safe_wait(tracker.duration - 6.5)
        
        with self.voiceover(text="And set B containing two, four, six, and eight.") as tracker:
            # === SET B GROUP ===
            # Set B definition
            set_B_text = MathTex(
                r'B = \{ 2, 4, 6, 8 \}',
                font_size=40,
                color="#008000"  # Green color
            )
            
            # Circle B - positioned directly under set B text
            circle_B = Circle(
                radius=2.0,
                color="#008000",  # Green color
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.next_to(set_B_text, DOWN, buff=1.0)
            
            # Label B inside the circle
            label_B = Text(
                "B",
                font_size=36,
                color="#008000",
                font="sans-serif",
                weight=BOLD
            )
            label_B.move_to(circle_B.get_center() + UP * 1.5)
            
            # Numbers inside circle B
            numbers_B = VGroup()
            b_values = [2, 4, 6, 8]
            for i, value in enumerate(b_values):
                number = Text(
                    str(value),
                    font_size=32,
                    color="#505050",
                    font="sans-serif"
                )
                # Position numbers horizontally across the circle
                x_pos = circle_B.get_center()[0] + (i - 1.5) * 0.6
                y_pos = circle_B.get_center()[1]
                number.move_to([x_pos, y_pos, 0])
                numbers_B.add(number)
            
            # Group all B elements together
            group_B = VGroup(set_B_text, circle_B, label_B, numbers_B)
            
            # Position group B on the right
            group_B.move_to(RIGHT * 3)
            
            # Show set B group
            self.play(Write(set_B_text), run_time=2)
            self.play(Create(circle_B), run_time=1.5)
            self.play(Write(label_B), run_time=1)
            self.play(Write(numbers_B), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)

        with self.voiceover(text="Now let's arrange these as overlapping circles to create a Venn diagram showing the relationships between these sets.") as tracker:
            # === TRANSITION TO VENN DIAGRAM ===
            
            # Create overlapping circles (Venn diagram)
            circle_A_venn = Circle(
                radius=2.0,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A_venn.move_to(LEFT * 1.2)
            
            circle_B_venn = Circle(
                radius=2.0,
                color="#008000", 
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B_venn.move_to(RIGHT * 1.2)
            
            # New labels
            label_A_venn = Text("A", font_size=36, color="#00396B", font="sans-serif", weight=BOLD)
            label_A_venn.move_to(LEFT + UP * 1.5)
            
            label_B_venn = Text("B", font_size=36, color="#008000", font="sans-serif", weight=BOLD)
            label_B_venn.move_to(RIGHT + UP * 1.5)
            
            # Numbers in regions
            # A only: 1, 3, 5
            nums_A_only = VGroup(
                Text("1", font_size=32, color="#505050").move_to(LEFT * 2.5 + UP * 0.3),
                Text("3", font_size=32, color="#505050").move_to(LEFT * 2.5 + DOWN * 0.3), 
                Text("5", font_size=32, color="#505050").move_to(LEFT * 2.5 + DOWN * 0.9)
            )
            
            # Intersection: 2, 4, 6
            nums_intersection = VGroup(
                Text("2", font_size=32, color="#505050").move_to(UP * 0.5),
                Text("4", font_size=32, color="#505050").move_to(ORIGIN),
                Text("6", font_size=32, color="#505050").move_to(DOWN * 0.5)
            )
            
            # B only: 8
            nums_B_only = Text("8", font_size=32, color="#505050").move_to(RIGHT * 2.5)
            
            # Replace everything in one smooth transformation
            self.play(
                ReplacementTransform(circle_A, circle_A_venn),
                ReplacementTransform(circle_B, circle_B_venn),
                ReplacementTransform(label_A, label_A_venn),
                ReplacementTransform(label_B, label_B_venn),
                ReplacementTransform(numbers_A, nums_A_only),
                ReplacementTransform(numbers_B, VGroup(nums_intersection, nums_B_only)),
                FadeOut(VGroup(set_A_text, set_B_text)),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.5)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                circle_A_venn, circle_B_venn, label_A_venn, label_B_venn,
                nums_A_only, nums_intersection, nums_B_only
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_explanation(self):
        """Show explanation of union and intersection"""
        with self.voiceover(text="The union and intersection are two ways of combining the elements in two sets into a new set.") as tracker:
            # Explanation text - split into multiple lines for better formatting
            explanation_line1 = MarkupText(
                '<b><i>The union and intersection are two ways of</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            explanation_line2 = MarkupText(
                '<b><i>combining the elements in two sets into a new</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            explanation_line3 = MarkupText(
                '<b><i>set.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            # Position the text at the top
            explanation_line1.to_edge(UP, buff=1.5)
            explanation_line1.to_edge(LEFT, buff=0.5)
            explanation_line2.next_to(explanation_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            explanation_line3.next_to(explanation_line2, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show explanation text
            self.play(Write(explanation_line1), run_time=2)
            self.play(Write(explanation_line2), run_time=2)
            self.play(Write(explanation_line3), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)
        
        # Clear explanation before next section
        self.play(
            FadeOut(VGroup(explanation_line1, explanation_line2, explanation_line3)),
            run_time=1
        )
        self.wait(1)
    
    def show_union_definition(self):
        """Show union definition with formula and Venn diagram"""
        with self.voiceover(text="The union of two sets A and B is a set containing all the elements in A as well as all the elements in B.") as tracker:
            # Definition text at the top
            definition_line1 = MarkupText(
                '<b><i>The union of two sets A and B is the set</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            definition_line2 = MarkupText(
                '<b><i>containing all the elements in A as well as all the</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            definition_line3 = MarkupText(
                '<b><i>elements in B.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            # Position definition text at the top
            definition_line1.to_edge(UP, buff=1.0)
            definition_line1.to_edge(LEFT, buff=0.5)
            definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            definition_line3.next_to(definition_line2, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show definition text
            self.play(Write(definition_line1), run_time=2)
            self.play(Write(definition_line2), run_time=2)
            self.play(Write(definition_line3), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)
        
        with self.voiceover(text="We write this formally as A union B, where the large U shape symbolizes the union. This is the set x such that x is in A or x is in B. The word 'or' is the most important bit here.") as tracker:
            # Union formula - split into parts for precise targeting
            union_formula = MathTex(
                r'A', r'\cup', r'B', r'=', r'\{', r'x', r'\mid', 
                r'x', r'\in', r'A', r'\text{ or }', r'x', r'\in', r'B', r'\}',
                font_size=44,
                color="#505050"
            )
            union_formula.move_to(ORIGIN)
            
            # Show formula
            self.play(Write(union_formula), run_time=2.5)
            
            # Create underline for "or" - index 10 in our split formula
            or_part = union_formula[10]  # "\text{ or }" is at index 10
            or_underline = Line(
                start=or_part.get_corner(DOWN + LEFT),
                end=or_part.get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue color
                stroke_width=3
            )
            or_underline.shift(DOWN * 0.1)
            
            # Show underline for "or"
            self.play(Create(or_underline), run_time=1)
            
            # Arrow pointing to union symbol - index 1 in our split formula
            union_symbol = union_formula[1]  # "\cup" is at index 1
            
            arrow = CurvedArrow(
                start_point=union_symbol.get_center() + DOWN * 1.5 + LEFT * 2,
                end_point=union_symbol.get_center() + DOWN * 0.3,
                color="#505050",
                angle=0.3,
                tip_length=0.2
            )
            
            # "A union B" text below the arrow
            union_text = MarkupText(
                '<b><i>"A union B"</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            union_text.move_to(arrow.get_start() + DOWN * 0.3)
            
            # Show arrow and text
            self.play(
                Create(arrow),
                Write(union_text),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)

        with self.voiceover(text="This is like taking all of the elements indicated in this shaded area of the Venn diagram, and notice that it includes elements in both A and B.") as tracker:
            # === TRANSITION TO VENN DIAGRAM ===
            
            # Create simplified formula that will move to top
            simplified_formula = MathTex(
                r'A', r'\cup', r'B', r'=', r'\{', r'x', r'\mid', 
                r'x', r'\in', r'A', r'\text{ or }', r'x', r'\in', r'B', r'\}',
                font_size=40,
                color="#505050"
            )
            simplified_formula.to_edge(UP, buff=1.0)
            
            # Replace everything with formula moving up, fade out other elements
            self.play(
                ReplacementTransform(union_formula, simplified_formula),
                FadeOut(VGroup(
                    definition_line1, definition_line2, definition_line3,
                    or_underline, arrow, union_text
                )),
                run_time=2
            )
            
            # Create overlapping circles for Venn diagram
            circle_A = Circle(
                radius=2.0,
                color="#00396B",  # Blue border
                stroke_width=4.0,
                fill_opacity=0  # Start without fill
            )
            circle_A.move_to(LEFT * 1.2)
            
            circle_B = Circle(
                radius=2.0,
                color="#008000",  # Green border
                stroke_width=4.0,
                fill_opacity=0  # Start without fill
            )
            circle_B.move_to(RIGHT * 1.2)
            
            # Labels
            label_A = Text(
                "A",
                font_size=36,
                color="#00396B",
                font="sans-serif",
                weight=BOLD
            )
            label_A.move_to(LEFT + UP * 1.5)
            
            label_B = Text(
                "B", 
                font_size=36,
                color="#008000",
                font="sans-serif",
                weight=BOLD
            )
            label_B.move_to(RIGHT + UP * 1.5)
            
            # Create circles and labels
            self.play(
                Create(circle_A),
                Create(circle_B),
                Write(label_A),
                Write(label_B),
                run_time=2
            )
            
            # Now fill both circles with gray to show union
            filled_circle_A = circle_A.copy().set_fill(color="#A0A0A0", opacity=0.6)
            filled_circle_B = circle_B.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(circle_A, filled_circle_A),
                ReplacementTransform(circle_B, filled_circle_B),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                simplified_formula, filled_circle_A, filled_circle_B,
                label_A, label_B
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_intersection_definition(self):
        """Show intersection definition with formula and Venn diagram"""
        with self.voiceover(text="The intersection of sets A and B is a set containing elements that are in both A and B.") as tracker:
            # Definition text at the top
            definition_line1 = MarkupText(
                '<b><i>The intersection of sets A and B is the set</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            definition_line2 = MarkupText(
                '<b><i>containing elements that are in both A and B.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            # Position definition text at the top
            definition_line1.to_edge(UP, buff=1.0)
            definition_line1.to_edge(LEFT, buff=0.5)
            definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Show definition text
            self.play(Write(definition_line1), run_time=2)
            self.play(Write(definition_line2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        with self.voiceover(text="The intersection of A and B, or A intersect B for short, is symbolized with an upside down union symbol and is formally defined as x such that x is in A and x is in B. The word 'and' is the most important bit.") as tracker:
            # Intersection formula - split into parts for precise targeting
            intersection_formula = MathTex(
                r'A', r'\cap', r'B', r'=', r'\{', r'x', r'\mid', 
                r'x', r'\in', r'A', r'\text{ and }', r'x', r'\in', r'B', r'\}',
                font_size=44,
                color="#505050"
            )
            intersection_formula.move_to(ORIGIN)
            
            # Show formula
            self.play(Write(intersection_formula), run_time=2.5)
            
            # Create underline for "and" - index 10 in our split formula
            and_part = intersection_formula[10]  # "\text{ and }" is at index 10
            and_underline = Line(
                start=and_part.get_corner(DOWN + LEFT),
                end=and_part.get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue color
                stroke_width=3
            )
            and_underline.shift(DOWN * 0.1)
            
            # Show underline for "and"
            self.play(Create(and_underline), run_time=1)
            
            # Arrow pointing to intersection symbol - index 1 in our split formula
            intersection_symbol = intersection_formula[1]  # "\cap" is at index 1
            
            arrow = CurvedArrow(
                start_point=intersection_symbol.get_center() + DOWN * 1.5 + LEFT * 2,
                end_point=intersection_symbol.get_center() + DOWN * 0.3,
                color="#505050",
                angle=0.3,
                tip_length=0.2
            )
            
            # "A intersect B" text below the arrow
            intersect_text = MarkupText(
                '<b><i>"A intersect B"</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            intersect_text.move_to(arrow.get_start() + DOWN * 0.3)
            
            # Show arrow and text
            self.play(
                Create(arrow),
                Write(intersect_text),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.5)
        
        with self.voiceover(text="If the elements of the intersection must be in both A and B, then we're talking about the overlapping part of the Venn diagram.") as tracker:
            # === CONTINUATION: TRANSITION TO VENN DIAGRAM ===
            
            # Create simplified formula that will move to top
            simplified_formula = MathTex(
                r'A', r'\cap', r'B', r'=', r'\{', r'x', r'\mid', 
                r'x', r'\in', r'A', r'\text{ and }', r'x', r'\in', r'B', r'\}',
                font_size=40,
                color="#505050"
            )
            simplified_formula.to_edge(UP, buff=1.0)
            
            # Replace everything with formula moving up, fade out other elements
            self.play(
                ReplacementTransform(intersection_formula, simplified_formula),
                FadeOut(VGroup(
                    definition_line1, definition_line2,
                    and_underline, arrow, intersect_text
                )),
                run_time=2
            )
            
            # Create overlapping circles for Venn diagram
            circle_A = Circle(
                radius=2.0,
                color="#00396B",  # Blue border
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(LEFT * 1.2)
            
            circle_B = Circle(
                radius=2.0,
                color="#008000",  # Green border
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.move_to(RIGHT * 1.2)
            
            # Labels
            label_A = Text(
                "A",
                font_size=36,
                color="#00396B",
                font="sans-serif",
                weight=BOLD
            )
            label_A.move_to(LEFT + UP * 1.5)
            
            label_B = Text(
                "B", 
                font_size=36,
                color="#008000",
                font="sans-serif",
                weight=BOLD
            )
            label_B.move_to(RIGHT + UP * 1.5)
            
            # Create circles and labels
            self.play(
                Create(circle_A),
                Create(circle_B),
                Write(label_A),
                Write(label_B),
                run_time=2
            )
            
            intersection_area = Intersection(circle_A, circle_B)
            intersection_area.set_fill(color="#A0A0A0", opacity=0.6)
            intersection_area.set_stroke(width=0)
            
            # Fill only the intersection area with gray
            self.play(
                FadeIn(intersection_area),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                simplified_formula, circle_A, circle_B, intersection_area,
                label_A, label_B
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_examples(self):
        """Show first set of examples"""
        with self.voiceover(text="Let A be the set containing zero and one, and B be the set containing one, two, and three. What is A union B? And what is A intersect B?") as tracker:
            # Given sets at the top
            given_sets = MarkupText(
                '<b><i>Let A = {0, 1} and B = {1, 2, 3}.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            given_sets.to_edge(UP, buff=1.5)
            given_sets.to_edge(LEFT, buff=0.5)
            
            # Show given sets
            self.play(Write(given_sets), run_time=2.5)
            
            # Question 1: Union
            question1 = MarkupText(
                '<b><i>1. What is A ∪ B ?</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            question1.next_to(given_sets, DOWN, buff=1.5)
            question1.to_edge(LEFT, buff=0.5)
            
            # Show question 1
            self.play(Write(question1), run_time=2)
            
            # Question 2: Intersection
            question2 = MarkupText(
                '<b><i>2. What is A ∩ B ?</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            question2.next_to(question1, DOWN, buff=1.2)
            question2.to_edge(LEFT, buff=0.5)
            
            # Show question 2
            self.play(Write(question2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)

        with self.voiceover(text="The union of A and B contains all the elements in A, so zero and one, as well as everything in B, which is one, two, and three. So all together, and ignoring the repeating one, we have the union of A and B is the set containing zero, one, two, and three.") as tracker:
            # Answer 1: Union result
            answer1 = MathTex(
                r'\{ 0, 1, 2, 3 \}',
                font_size=50,
                color="#505050"
            )
            answer1.move_to(question1.get_center() + RIGHT * 6)
            
            # Show answer 1
            self.play(Write(answer1), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        with self.voiceover(text="The intersection of A and B will contain only elements in both A and B. In this case, only one is common to both A and B, and so the intersection of A and B is the set containing one.") as tracker:
            # Answer 2: Intersection result
            answer2 = MathTex(
                r'\{ 1 \}',
                font_size=50,
                color="#505050"
            )
            answer2.move_to(question2.get_center() + RIGHT * 6)
            
            # Show answer 2
            self.play(Write(answer2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(given_sets, question1, question2, answer1, answer2)),
            run_time=1
        )
        self.wait(1)
    
    def show_examples_2(self):
        """Show second set of examples"""
        with self.voiceover(text="Let's do a second example. Let A be the set of little a in the natural numbers such that little a is odd - the odd numbers for short - and B be the set of even natural numbers. What is A union B? And what is A intersect B?") as tracker:
            # Given sets at the top - split into two lines for better readability
            given_sets_line1 = MarkupText(
                '<b><i>Let A = {a ∈ ℕ | a is odd} and B = {b ∈ ℕ |</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            given_sets_line2 = MarkupText(
                '<b><i>b is even}.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            
            # Position the given sets
            given_sets_line1.to_edge(UP, buff=1.0)
            given_sets_line1.to_edge(LEFT, buff=0.5)
            given_sets_line2.next_to(given_sets_line1, DOWN, buff=0.1, aligned_edge=LEFT)
            
            # Show given sets
            self.play(Write(given_sets_line1), run_time=2.5)
            self.play(Write(given_sets_line2), run_time=2)
            
            # Question 1: Union
            question1 = MarkupText(
                '<b><i>1. What is A ∪ B ?</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            question1.next_to(given_sets_line2, DOWN, buff=1.5)
            question1.to_edge(LEFT, buff=0.5)
            
            # Show question 1
            self.play(Write(question1), run_time=2)
            
            # Question 2: Intersection
            question2 = MarkupText(
                '<b><i>2. What is A ∩ B ?</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            question2.next_to(question1, DOWN, buff=1.2)
            question2.to_edge(LEFT, buff=0.5)
            
            # Show question 2
            self.play(Write(question2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.5)
        
        with self.voiceover(text="The union of A and B will be a set that contains all the odd numbers and all the even numbers, which is the set of all natural numbers.") as tracker:
            # Answer 1: Union result (all natural numbers)
            answer1 = MathTex(
                r'\mathbb{N}',
                font_size=50,
                color="#505050"
            )
            answer1.move_to(question1.get_center() + RIGHT * 6)
            
            # Show answer 1
            self.play(Write(answer1), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        with self.voiceover(text="The intersection of A and B would contain only numbers that are both odd and even. There aren't any numbers which fit this criterion, and so the intersection of A and B is just the empty set.") as tracker:
            # Answer 2: Intersection result (empty set)
            answer2 = MathTex(
                r'\varnothing',
                font_size=50,
                color="#505050"
            )
            answer2.move_to(question2.get_center() + RIGHT * 6)
            
            # Show answer 2
            self.play(Write(answer2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 2.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                given_sets_line1, given_sets_line2, question1, question2, answer1, answer2
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_union_properties(self):
        """Show properties of the union"""
        with self.voiceover(text="Let's look at some properties of the union. Firstly, the union of any set A with the empty set is just A, since the empty set has no elements. We have a similar situation with taking the union of any set A with itself, which just gives A.") as tracker:
            # Title at the top - centered and moved up
            title = MarkupText(
                '<b><i>Properties of the Union</i></b>',
                color="#505050",
                font_size=48,
                font="sans-serif"
            )
            title.to_edge(UP, buff=0.5)  # Moved up more
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # All properties aligned to the left at same position
            properties = VGroup(
                MathTex(r'1. \quad A \cup \varnothing = A', font_size=36, color="#505050"),
                MathTex(r'2. \quad A \cup A = A', font_size=36, color="#505050"),
                MathTex(r'3. \quad \text{if } A \subseteq B\text{, then } A \cup B = B', font_size=36, color="#505050")
            )
            
            # Position all properties to the left with consistent alignment
            properties.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
            properties.to_edge(LEFT, buff=0.8)
            properties.move_to(properties.get_center() + UP * 0.5)
            
            # Show first property
            self.play(Write(properties[0]), run_time=2)
            # Show second property
            self.play(Write(properties[1]), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        with self.voiceover(text="If A is a subset of B, then the union of A and B is just B, because all of the elements in A are already in B, and so we don't add anything new to the union.") as tracker:
            self.play(Write(properties[2]), run_time=2)
            
            # Create smaller circles on the right
            circle_B = Circle(
                radius=1.8,
                color="#008000",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            circle_A = Circle(
                radius=1.0,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(circle_B.get_center() + LEFT * 0.4 + DOWN * 0.3)
            
            # Labels
            label_A = Text("A", font_size=28, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center())
            
            label_B = Text("B", font_size=28, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 1.3 + RIGHT * 0.3)
            
            # Create circles and labels
            self.play(
                Create(circle_B),
                Create(circle_A),
                Write(label_A),
                Write(label_B),
                run_time=2.5
            )
            
            # Fill with gray
            filled_circle_B = circle_B.copy().set_fill(color="#A0A0A0", opacity=0.6)
            filled_circle_A = circle_A.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(circle_B, filled_circle_B),
                ReplacementTransform(circle_A, filled_circle_A),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)
        
        with self.voiceover(text="Another example is that the union of A and B is the same thing as taking the union of B with A. The final property of unions is if we have three sets A, B, and C, we can exchange the order we take the union by moving the brackets and we'll still get the same outcome.") as tracker:
            # Property 4 - Commutative property
            property4 = MathTex(
                r'4. \quad A \cup B = B \cup A',
                font_size=36,
                color="#505050"
            )
            property4.next_to(properties[2], DOWN, buff=0.8)
            property4.to_edge(LEFT, buff=0.8)
            
            # Show property 4
            self.play(Write(property4), run_time=2)

            # === TRANSITION: Keep only title ===
            
            # Fade out everything except the title
            self.play(
                FadeOut(VGroup(
                    properties, property4, filled_circle_B, filled_circle_A, label_A, label_B
                )),
                run_time=1.5
            )
            
            # Property 5 - Associative property
            property5 = MathTex(
                r'5. \quad A \cup (B \cup C) = (A \cup B) \cup C',
                font_size=36,
                color="#505050"
            )
            property5.to_edge(LEFT, buff=0.8)
            property5.move_to(property5.get_center() + UP * 2)
            
            # Show property 5
            self.play(Write(property5), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        with self.voiceover(text="On the left hand side we take the union of B with C first and then take the union with A. We end with all the elements in A as well as all those in B and C. Taking the right hand side, we start with the union of A and B and then take the union of that with C, and just as before we get all the elements from all three sets.") as tracker:
            # Create three-circle template
            circle_A = Circle(radius=1.2, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A.move_to(LEFT * 0.7 + DOWN * 1.2)
            
            circle_B = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B.move_to(ORIGIN + DOWN * 0.2)
            
            circle_C = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C.move_to(RIGHT * 0.7 + DOWN * 1.2)
            
            label_A = Text("A", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + LEFT * 0.8)
            
            label_B = Text("B", font_size=24, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 0.8)
            
            label_C = Text("C", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            label_C.move_to(circle_C.get_center() + RIGHT * 0.8)
            
            venn_template = VGroup(circle_A, circle_B, circle_C, label_A, label_B, label_C)
            
            # === LEFT DIAGRAM: A ∪ (B ∪ C) ===
            left_diagram = venn_template.copy()
            left_diagram.move_to(LEFT * 2.5)
            
            # Show left diagram
            self.play(FadeIn(left_diagram), run_time=2)
            
            # First show B ∪ C union
            bc_union = Union(left_diagram[1], left_diagram[2])  # B and C circles
            bc_union.set_fill(color="#A0A0A0", opacity=0.6)
            bc_union.set_stroke(width=0)
            
            self.play(FadeIn(bc_union), run_time=2)
            
            # Then show final A ∪ (B ∪ C) - all three circles
            abc_union_left = Union(left_diagram[0], Union(left_diagram[1], left_diagram[2]))
            abc_union_left.set_fill(color="#808080", opacity=0.8)  # Darker for final result
            abc_union_left.set_stroke(width=0)
            
            self.play(
                FadeOut(bc_union),
                FadeIn(abc_union_left),
                run_time=2
            )
            
            # === RIGHT DIAGRAM: (A ∪ B) ∪ C ===
            right_diagram = venn_template.copy()
            right_diagram.move_to(RIGHT * 2.5)
            
            # Show right diagram
            self.play(FadeIn(right_diagram), run_time=2)
            
            # First show A ∪ B union
            ab_union = Union(right_diagram[0], right_diagram[1])  # A and B circles
            ab_union.set_fill(color="#A0A0A0", opacity=0.6)
            ab_union.set_stroke(width=0)
            
            self.play(FadeIn(ab_union), run_time=2)
            
            # Then show final (A ∪ B) ∪ C - all three circles
            abc_union_right = Union(Union(right_diagram[0], right_diagram[1]), right_diagram[2])
            abc_union_right.set_fill(color="#808080", opacity=0.8)  # Darker for final result
            abc_union_right.set_stroke(width=0)
            
            self.play(
                FadeOut(ab_union),
                FadeIn(abc_union_right),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 12.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, property5, left_diagram, right_diagram,
                abc_union_left, abc_union_right
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_intersection_properties(self):
        """Show properties of the intersection"""
        with self.voiceover(text="Some properties of the intersection now. Remember, this is all the elements common to both sets. Firstly, for any set A, the intersection of A with the empty set is just the empty set, since the empty set has no elements it can't have any elements in common with any other set. The intersection of any set with itself is just itself. If you remember, this is exactly the same as with unions.") as tracker:
            # Title at the top - centered and moved up
            title = MarkupText(
                '<b><i>Properties of the Intersection</i></b>',
                color="#505050",
                font_size=48,
                font="sans-serif"
            )
            title.to_edge(UP, buff=0.5)
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # All properties aligned to the left at same position
            properties = VGroup(
                MathTex(r'1. \quad A \cap \varnothing = \varnothing', font_size=36, color="#505050"),
                MathTex(r'2. \quad A \cap A = A', font_size=36, color="#505050"),
                MathTex(r'3. \quad \text{if } A \subseteq B\text{, then } A \cap B = A', font_size=36, color="#505050")
            )
            
            # Position all properties to the left with consistent alignment
            properties.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
            properties.to_edge(LEFT, buff=0.8)
            properties.move_to(properties.get_center() + UP * 0.5)
            
            # Show first property
            self.play(Write(properties[0]), run_time=2)
            # Show second property
            self.play(Write(properties[1]), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        with self.voiceover(text="If A is a subset of B, then the intersection of A and B is just A, the smaller set of the two, as indicated by the shaded area. This is because the elements in A are also in B.") as tracker:
            self.play(Write(properties[2]), run_time=2)
            
            # Create circles to illustrate property 3 (A ⊆ B case)
            circle_B = Circle(
                radius=1.8,
                color="#008000",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_B.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            circle_A = Circle(
                radius=1.0,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(circle_B.get_center() + LEFT * 0.4 + DOWN * 0.3)
            
            # Labels
            label_A = Text("A", font_size=28, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + UP * 0.5)
            
            label_B = Text("B", font_size=28, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 1.3 + RIGHT * 0.3)
            
            # Create circles and labels
            self.play(
                Create(circle_B),
                Create(circle_A),
                Write(label_A),
                Write(label_B),
                run_time=2.5
            )
            
            # Fill only circle A with gray to show A ∩ B = A
            filled_circle_A = circle_A.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(circle_A, filled_circle_A),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)
        
        with self.voiceover(text="And just like with the union, A intersect B is the same as B intersect A. That is, the order of the sets doesn't make any difference to the intersection. Again, like with the union, the fact that the order doesn't matter extends to three or more sets with brackets.") as tracker:
            # Property 4 - Commutative property
            property4 = MathTex(
                r'4. \quad A \cap B = B \cap A',
                font_size=36,
                color="#505050"
            )
            property4.next_to(properties[2], DOWN, buff=0.8)
            property4.to_edge(LEFT, buff=0.8)
            
            # Show property 4
            self.play(Write(property4), run_time=2)

            # === TRANSITION: Keep only title ===
            
            # Fade out everything except the title
            self.play(
                FadeOut(VGroup(
                    properties, property4, circle_B, filled_circle_A, label_A, label_B
                )),
                run_time=1.5
            )
            
            # Property 5 - Associative property for intersection
            property5 = MathTex(
                r'5. \quad A \cap (B \cap C) = (A \cap B) \cap C',
                font_size=36,
                color="#505050"
            )
            property5.to_edge(LEFT, buff=0.8)
            property5.move_to(property5.get_center() + UP * 2)
            
            # Show property 5
            self.play(Write(property5), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.0)
        
        with self.voiceover(text="We can see that B intersects C, then the intersection of the result of that with A is the same as taking the intersection of A and B and then the intersection of that with C. In both cases we end up with a set containing the elements found in A and B and C, the shaded area in the middle.") as tracker:
            # Create three-circle template for intersections
            circle_A = Circle(radius=1.2, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A.move_to(LEFT * 0.7 + DOWN * 1.2)
            
            circle_B = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B.move_to(ORIGIN + DOWN * 0.2)
            
            circle_C = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C.move_to(RIGHT * 0.7 + DOWN * 1.2)
            
            label_A = Text("A", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + LEFT * 0.8)
            
            label_B = Text("B", font_size=24, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 0.8)
            
            label_C = Text("C", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            label_C.move_to(circle_C.get_center() + RIGHT * 0.8)
            
            venn_template = VGroup(circle_A, circle_B, circle_C, label_A, label_B, label_C)
            
            # === LEFT DIAGRAM: A ∩ (B ∩ C) ===
            left_diagram = venn_template.copy()
            left_diagram.move_to(LEFT * 2.5)
            
            # Show left diagram
            self.play(FadeIn(left_diagram), run_time=2)
            
            # First show B ∩ C intersection
            bc_intersection = Intersection(left_diagram[1], left_diagram[2])  # B and C circles
            bc_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            bc_intersection.set_stroke(width=0)
            
            self.play(FadeIn(bc_intersection), run_time=2)
            
            # Then show final A ∩ (B ∩ C) - center intersection
            abc_intersection_left = Intersection(left_diagram[0], Intersection(left_diagram[1], left_diagram[2]))
            abc_intersection_left.set_fill(color="#808080", opacity=0.8)  # Darker for final result
            abc_intersection_left.set_stroke(width=0)
            
            self.play(
                FadeOut(bc_intersection),
                FadeIn(abc_intersection_left),
                run_time=2
            )
            
            # === RIGHT DIAGRAM: (A ∩ B) ∩ C ===
            right_diagram = venn_template.copy()
            right_diagram.move_to(RIGHT * 2.5)
            
            # Show right diagram
            self.play(FadeIn(right_diagram), run_time=2)
            
            # First show A ∩ B intersection
            ab_intersection = Intersection(right_diagram[0], right_diagram[1])  # A and B circles
            ab_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            ab_intersection.set_stroke(width=0)
            
            self.play(FadeIn(ab_intersection), run_time=2)
            
            # Then show final (A ∩ B) ∩ C - center intersection
            abc_intersection_right = Intersection(Intersection(right_diagram[0], right_diagram[1]), right_diagram[2])
            abc_intersection_right.set_fill(color="#808080", opacity=0.8)  # Darker for final result
            abc_intersection_right.set_stroke(width=0)
            
            self.play(
                FadeOut(ab_intersection),
                FadeIn(abc_intersection_right),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 12.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, property5, left_diagram, right_diagram,
                abc_intersection_left, abc_intersection_right
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_cardinality(self):
        """Show union and intersection cardinality"""
        with self.voiceover(text="Let's look at the cardinality of the union and intersection of two sets, because there's a useful identity. Let A be the set containing one, two, and three, and B be the set containing three and four. We can see that A contains three elements and B contains two elements.") as tracker:
            # Set A definition at the top left - closer to center
            set_A_text = MathTex(
                r'A = \{1, 2, 3\}',
                font_size=40,
                color="#505050"
            )
            set_A_text.to_edge(UP, buff=1.0)
            set_A_text.move_to(set_A_text.get_center() + LEFT * 2.5)
            
            # Show set A
            self.play(Write(set_A_text), run_time=2)
            
            # Circle A (centered)
            circle_A = Circle(
                radius=2.0,
                color="#00396B",
                stroke_width=4.0,
                fill_opacity=0
            )
            circle_A.move_to(ORIGIN)
            
            # Label A
            label_A = Text("A", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + UP * 1.5)
            
            # Numbers in A
            numbers_A = VGroup(
                Text("1", font_size=28, color="#505050").move_to(LEFT * 0.8),
                Text("2", font_size=28, color="#505050").move_to(LEFT * 0.3),
                Text("3", font_size=28, color="#505050").move_to(RIGHT * 0.3)
            )
            
            # Show circle A with numbers
            self.play(
                Create(circle_A),
                Write(label_A),
                Write(numbers_A),
                run_time=2.5
            )
            
            # Set B definition at the top right - closer to center
            set_B_text = MathTex(
                r'B = \{3, 4\}',
                font_size=40,
                color="#505050"
            )
            set_B_text.to_edge(UP, buff=1.0)
            set_B_text.move_to(set_B_text.get_center() + RIGHT * 2.5)
            
            # Show set B
            self.play(Write(set_B_text), run_time=2)
            
            # Create overlapping circles for Venn diagram
            circle_A_venn = Circle(radius=2.0, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A_venn.move_to(LEFT * 1.2)
            
            circle_B_venn = Circle(radius=2.0, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B_venn.move_to(RIGHT * 1.2)
            
            # New labels
            label_A_venn = Text("A", font_size=32, color="#00396B", font="sans-serif", weight=BOLD)
            label_A_venn.move_to(LEFT * 1.7 + UP * 1.5)
            
            label_B_venn = Text("B", font_size=32, color="#008000", font="sans-serif", weight=BOLD)
            label_B_venn.move_to(RIGHT * 1.7 + UP * 1.5)
            
            # New number positioning for Venn diagram
            numbers_venn = VGroup(
                Text("1", font_size=28, color="#505050").move_to(LEFT * 2.2),      # A only
                Text("2", font_size=28, color="#505050").move_to(LEFT * 1.7),      # A only
                Text("3", font_size=28, color="#505050").move_to(ORIGIN),          # Intersection
                Text("4", font_size=28, color="#505050").move_to(RIGHT * 1.7)      # B only
            )
            
            # Transform to Venn diagram
            self.play(
                ReplacementTransform(circle_A, circle_A_venn),
                ReplacementTransform(label_A, label_A_venn),
                ReplacementTransform(numbers_A, numbers_venn),
                Create(circle_B_venn),
                Write(label_B_venn),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 11.0)
        
        with self.voiceover(text="And the union of A and B would contain one, two, three, and four, and so has a cardinality of four. The intersection of A and B contains only three, and so has a cardinality of one. Now notice that the two on the left added together equals the two on the right. This isn't coincidental, but it's always true.") as tracker:
            # Cardinalities at the bottom - split into parts for precise targeting
            card_A = MathTex(r'|A|', r'=', r'3', font_size=36, color="#505050")
            card_A.move_to(DOWN * 2.5 + LEFT * 4.5)
            
            card_B = MathTex(r'|B|', r'=', r'2', font_size=36, color="#505050")
            card_B.move_to(DOWN * 2.5 + LEFT * 1.5)
            
            card_union = MathTex(r'|A \cup B|', r'=', r'4', font_size=36, color="#505050")
            card_union.move_to(DOWN * 2.5 + RIGHT * 1.5)
            
            card_intersection = MathTex(r'|A \cap B|', r'=', r'1', font_size=36, color="#505050")
            card_intersection.move_to(DOWN * 2.5 + RIGHT * 4.5)
            
            cardinalities = [card_A, card_B, card_union, card_intersection]
            
            # Show cardinalities sequentially
            for card in cardinalities:
                self.play(Write(card), run_time=1.5)
            
            # Create underlines for the numbers
            underline_3 = Line(
                start=card_A[2].get_corner(DOWN + LEFT),
                end=card_A[2].get_corner(DOWN + RIGHT),
                color="#1853A2",
                stroke_width=3
            )
            underline_3.shift(DOWN * 0.1)
            
            underline_2 = Line(
                start=card_B[2].get_corner(DOWN + LEFT),
                end=card_B[2].get_corner(DOWN + RIGHT),
                color="#1853A2",
                stroke_width=3
            )
            underline_2.shift(DOWN * 0.1)
            
            underline_4 = Line(
                start=card_union[2].get_corner(DOWN + LEFT),
                end=card_union[2].get_corner(DOWN + RIGHT),
                color="#1853A2",
                stroke_width=3
            )
            underline_4.shift(DOWN * 0.1)
            
            underline_1 = Line(
                start=card_intersection[2].get_corner(DOWN + LEFT),
                end=card_intersection[2].get_corner(DOWN + RIGHT),
                color="#1853A2",
                stroke_width=3
            )
            underline_1.shift(DOWN * 0.1)
            
            # Create operators positioned between cardinalities
            plus_1 = MathTex(r'+', font_size=40, color="#1853A2")
            plus_1.move_to((card_A.get_center() + card_B.get_center()) / 2)
            
            equals_1 = MathTex(r'=', font_size=40, color="#1853A2")
            equals_1.move_to((card_B.get_center() + card_union.get_center()) / 2)
            
            plus_2 = MathTex(r'+', font_size=40, color="#1853A2")
            plus_2.move_to((card_union.get_center() + card_intersection.get_center()) / 2)
            
            # Show underlines and operators
            self.play(
                Create(underline_3),
                Write(plus_1),
                Create(underline_2),
                Write(equals_1),
                Create(underline_4),
                Write(plus_2),
                Create(underline_1),
                run_time=3
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.5)

        with self.voiceover(text="The identity is usually written as the cardinality of the union of A and B is equal to the cardinality of A plus the cardinality of B minus the cardinality of the intersection of A and B. Also, because we're taking away the cardinality of A intersect B, we can also write this as an inequality.") as tracker:
            # === TRANSITION TO CARDINALITY FORMULAS ===
            
            # Clear everything and show title
            self.play(
                FadeOut(VGroup(
                    set_A_text, set_B_text, circle_A_venn, circle_B_venn,
                    label_A_venn, label_B_venn, numbers_venn,
                    card_A, card_B, card_union, card_intersection,
                    underline_3, underline_2, underline_4, underline_1,
                    plus_1, equals_1, plus_2
                )),
                run_time=1.5
            )
            
            # Title
            title = MarkupText(
                '<b><i>Union and Intersection Cardinality</i></b>',
                color="#505050",
                font_size=48,
                font="sans-serif"
            )
            title.to_edge(UP, buff=1.0)
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # First formula - split for precise targeting
            formula1 = MathTex(
                r'|A \cup B|', r'=', r'|A|', r'+', r'|B|', r'-', r'|A \cap B|',
                font_size=44,
                color="#505050"
            )
            formula1.move_to(UP * 0.8)
            
            # Show first formula
            self.play(Write(formula1), run_time=2.5)
            
            # Underline |A ∩ B| (index 6 in the split formula)
            intersection_underline = Line(
                start=formula1[6].get_corner(DOWN + LEFT),
                end=formula1[6].get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue color
                stroke_width=3
            )
            intersection_underline.shift(DOWN * 0.1)
            
            # Show underline
            self.play(Create(intersection_underline), run_time=1.5)
            
            # Second formula
            formula2 = MathTex(
                r'|A \cup B| \leq |A| + |B|',
                font_size=44,
                color="#505050"
            )
            formula2.move_to(DOWN * 1.2)
            
            # Show second formula
            self.play(Write(formula2), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(title, formula1, formula2, intersection_underline)),
            run_time=1
        )
        self.wait(2)
    
    def show_mixing_unions_intersections(self):
        """Show mixing unions and intersections with distributive property"""
        with self.voiceover(text="We also have a couple of identities involving both unions and intersections for three sets A, B, and C. Taking the union of A with the intersection of B and C is the same as if we take the union of A and B and the union of A and C separately and then taking the intersection.") as tracker:
            # Title
            title = MarkupText(
                '<b><i>Mixing Unions and Intersections</i></b>',
                color="#505050",
                font_size=48,
                font="sans-serif"
            )
            title.to_edge(UP, buff=0.8)
            
            # Show title
            self.play(Write(title), run_time=2)
            
            # Distributive formula
            formula = MathTex(
                r'A \cup (B \cap C) = (A \cup B) \cap (A \cup C)',
                font_size=40,
                color="#505050"
            )
            formula.next_to(title, DOWN, buff=1.0)
            
            # Show formula
            self.play(Write(formula), run_time=2.5)
            
            # Create three-circle template - moved down more
            circle_A = Circle(radius=1.2, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A.move_to(LEFT * 0.7 + DOWN * 1.8)  # Moved down more
            
            circle_B = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B.move_to(ORIGIN + DOWN * 0.8)  # Moved down more
            
            circle_C = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C.move_to(RIGHT * 0.7 + DOWN * 1.8)  # Moved down more
            
            label_A = Text("A", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center() + LEFT * 0.8)
            
            label_B = Text("B", font_size=24, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 0.8)
            
            label_C = Text("C", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            label_C.move_to(circle_C.get_center() + RIGHT * 0.8)
            
            venn_template = VGroup(circle_A, circle_B, circle_C, label_A, label_B, label_C)
            
            # === LEFT DIAGRAM: A ∪ (B ∩ C) ===
            left_diagram = venn_template.copy()
            left_diagram.move_to(LEFT * 2.5 + DOWN * 1.1)  # Moved down more
            
            # Show left diagram
            self.play(FadeIn(left_diagram), run_time=2)
            
            # Step 1: Show B ∩ C intersection only
            bc_intersection = Intersection(left_diagram[1], left_diagram[2])  # B and C
            bc_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            bc_intersection.set_stroke(width=0)
            
            self.play(FadeIn(bc_intersection), run_time=2)
            
            # Step 2: Add A circle filled to show A ∪ (B ∩ C)
            filled_A_left = left_diagram[0].copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(FadeIn(filled_A_left), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 10.5)
        
        with self.voiceover(text="On the right side, we start with A union B and then take the intersection of that with A union C.") as tracker:
            # === RIGHT DIAGRAM: (A ∪ B) ∩ (A ∪ C) ===
            right_diagram = venn_template.copy()
            right_diagram.move_to(RIGHT * 2.5 + DOWN * 1.1)
            
            # Show right diagram
            self.play(FadeIn(right_diagram), run_time=2)
            
            # Step 3: Show A ∪ B on right
            filled_A_right = right_diagram[0].copy().set_fill(color="#A0A0A0", opacity=0.6)
            filled_B_right = right_diagram[1].copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                FadeIn(filled_A_right),
                FadeIn(filled_B_right),
                run_time=2
            )
            
            # Step 4: Show intersection with A ∪ C (A and C more pronounced, B lighter)
            # Keep B with lighter gray, make A and C darker
            filled_A_final = right_diagram[0].copy().set_fill(color="#808080", opacity=0.9)  # Darker
            filled_B_light = right_diagram[1].copy().set_fill(color="#C0C0C0", opacity=0.6)  # Lighter
            filled_C_final = right_diagram[2].copy().set_fill(color="#808080", opacity=0.9)  # Darker
            
            self.play(
                ReplacementTransform(filled_A_right, filled_A_final),
                ReplacementTransform(filled_B_right, filled_B_light),
                FadeIn(filled_C_final),
                run_time=2
            )

            # Step 5: Show final intersection (A ∪ B) ∩ (A ∪ C) - should match left side
            # This will be A plus the intersection of B and C
            final_A_right = right_diagram[0].copy().set_fill(color="#A0A0A0", opacity=0.6)
            final_bc_intersection = Intersection(right_diagram[1], right_diagram[2])  # B ∩ C
            final_bc_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            final_bc_intersection.set_stroke(width=0)
            
            self.play(
                FadeOut(filled_A_final),
                FadeOut(filled_B_light), 
                FadeOut(filled_C_final),
                FadeIn(final_A_right),
                FadeIn(final_bc_intersection),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 10.5)

        # Remove all gray colors from both diagrams
        self.play(
            FadeOut(filled_A_left),
            FadeOut(bc_intersection),
            FadeOut(final_A_right),
            FadeOut(final_bc_intersection),
            run_time=1.5
        )
        
        with self.voiceover(text="This identity works if we exchange the unions for intersections and the intersections for unions. Here the intersection of A with the union of B and C is the same as the union of A intersect B with A intersect C.") as tracker:
            # Replace the formula with the dual distributive law
            new_formula = MathTex(
                r'A \cap (B \cup C) = (A \cap B) \cup (A \cap C)',
                font_size=40,
                color="#505050"
            )
            new_formula.move_to(formula.get_center())
            
            # Transform the formula (swap unions and intersections)
            self.play(
                ReplacementTransform(formula, new_formula),
                run_time=2
            )

            # === LEFT SIDE: A ∩ (B ∪ C) ===
            
            # Step 1: Show B ∪ C on left (Image 1)
            bc_union_left = Union(left_diagram[1], left_diagram[2])  # B ∪ C
            bc_union_left.set_fill(color="#A0A0A0", opacity=0.6)
            bc_union_left.set_stroke(width=0)
            
            self.play(FadeIn(bc_union_left), run_time=1.5)
            
            # Step 2: Show A ∩ (B ∪ C) on left (Image 2)
            a_intersect_bc_left = Intersection(left_diagram[0], Union(left_diagram[1], left_diagram[2]))
            a_intersect_bc_left.set_fill(color="#A0A0A0", opacity=0.6)
            a_intersect_bc_left.set_stroke(width=0)
            
            self.play(
                FadeOut(bc_union_left),
                FadeIn(a_intersect_bc_left),
                run_time=1.5
            )
            
            # === RIGHT SIDE: (A ∩ B) ∪ (A ∩ C) ===
            
            # Step 3: Show A ∩ B on right (Image 3)
            ab_intersection_right = Intersection(right_diagram[0], right_diagram[1])  # A ∩ B
            ab_intersection_right.set_fill(color="#A0A0A0", opacity=0.6)
            ab_intersection_right.set_stroke(width=0)
            
            self.play(FadeIn(ab_intersection_right), run_time=1.5)
            
            # Step 4: Add A ∩ C on right (Image 4) - union of both intersections
            ac_intersection_right = Intersection(right_diagram[0], right_diagram[2])  # A ∩ C
            ac_intersection_right.set_fill(color="#A0A0A0", opacity=0.6)
            ac_intersection_right.set_stroke(width=0)
            
            self.play(FadeIn(ac_intersection_right), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, new_formula, left_diagram, right_diagram,
                a_intersect_bc_left, ab_intersection_right, ac_intersection_right
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_distributive_laws_comparison(self):
        """Show comparison of distributive laws"""
        with self.voiceover(text="As we've already discussed, these identities are similar to multiplying out the brackets, and this kind of property in general is known as distributivity or the distributive property.") as tracker:
            # Split formulas into parts for precise targeting of B and C
            formula1 = MathTex(
                r'A \cup (', r'B', r'\cap', r'C', r') = (A \cup ', r'B', r') \cap (A \cup ', r'C', r')',
                font_size=40,
                color="#505050"
            )
            formula1.move_to(UP * 2)
            
            formula2 = MathTex(
                r'A \cap (', r'B', r'\cup', r'C', r') = (A \cap ', r'B', r') \cup (A \cap ', r'C', r')',
                font_size=40,
                color="#505050"
            )
            formula2.move_to(ORIGIN)
            
            formula3 = MathTex(
                r'A \times (B + C) = (A \times B) + (A \times C)',
                font_size=40,
                color="#505050"
            )
            formula3.move_to(DOWN * 2)
            
            # Show formulas sequentially without pauses
            self.play(Write(formula1), run_time=1.5)
            self.play(Write(formula2), run_time=1.5)
            self.play(Write(formula3), run_time=1.5)
            
            # Create green frame around the third formula
            green_frame = Rectangle(
                width=formula3.width + 0.5,
                height=formula3.height + 0.3,
                color="#008000",
                stroke_width=4,
                fill_opacity=0
            )
            green_frame.move_to(formula3.get_center())
            
            # Show green frame
            self.play(Create(green_frame), run_time=1.5)
            
            # Arrows for first formula: B to B, C to C
            # Arrow from first B to second B
            arrow1_B = CurvedArrow(
                start_point=formula1[1].get_center() + UP * 0.3,  # First B
                end_point=formula1[5].get_center() + UP * 0.3,    # Second B
                color="#00396B",
                angle=-PI/4,
                tip_length=0.15
            )
            
            # Arrow from first C to second C
            arrow1_C = CurvedArrow(
                start_point=formula1[3].get_center() + UP * 0.3,  # First C
                end_point=formula1[7].get_center() + UP * 0.3,    # Second C
                color="#00396B",
                angle=-PI/4,
                tip_length=0.15
            )
            
            # Arrows for second formula: B to B, C to C
            # Arrow from first B to second B
            arrow2_B = CurvedArrow(
                start_point=formula2[1].get_center() + UP * 0.3,  # First B
                end_point=formula2[5].get_center() + UP * 0.3,    # Second B
                color="#00396B",
                angle=-PI/4,
                tip_length=0.15
            )
            
            # Arrow from first C to second C
            arrow2_C = CurvedArrow(
                start_point=formula2[3].get_center() + UP * 0.3,  # First C
                end_point=formula2[7].get_center() + UP * 0.3,    # Second C
                color="#00396B",
                angle=-PI/4,
                tip_length=0.15
            )
            
            # Show arrows for first formula
            self.play(
                Create(arrow1_B),
                Create(arrow1_C),
                run_time=2
            )
            
            # Show arrows for second formula
            self.play(
                Create(arrow2_B),
                Create(arrow2_C),
                run_time=2
            )
            
            # Conclusion text at bottom right
            conclusion_text = MarkupText(
                '<b><i>distributive property</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            conclusion_text.to_edge(RIGHT, buff=1.0)
            conclusion_text.to_edge(DOWN, buff=1.0)
            
            # Blue underline for conclusion
            conclusion_underline = Line(
                start=conclusion_text.get_corner(DOWN + LEFT),
                end=conclusion_text.get_corner(DOWN + RIGHT),
                color="#1853A2",
                stroke_width=3
            )
            conclusion_underline.shift(DOWN * 0.1)
            
            # Show conclusion and underline
            self.play(
                Write(conclusion_text),
                Create(conclusion_underline),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 12.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                formula1, formula2, formula3, green_frame,
                arrow1_B, arrow1_C, arrow2_B, arrow2_C,
                conclusion_text, conclusion_underline
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_union_real_world_example(self):
        """Show real world example with cycling and distributive law"""
        with self.voiceover(text="You might be thinking at this point, how are these identities useful? So I'm what they call a fair weather cyclist. I only cycle in the summer or in the winter when it's warmer than twenty degrees celsius. Let's make sets of these potential days I could ride a bike. We have summer, winter, and those that are more than twenty degrees celsius.") as tracker:
            # Main statement text - split into two lines and positioned properly
            statement_line1 = MarkupText(
                '<b><i>I only cycle in the summer or in the winter when it\'s</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            statement_line2 = MarkupText(
                '<b><i>warmer than 20°C</i></b>',
                color="#505050",
                font_size=32,
                font="sans-serif"
            )
            
            # Position text at top, centered properly
            statement_line1.to_edge(UP, buff=1.0)
            statement_line1.to_edge(LEFT, buff=0.5)  # Align to left edge properly
            statement_line2.next_to(statement_line1, DOWN, buff=0.1, aligned_edge=LEFT)
            
            # Show the main statement
            self.play(Write(statement_line1), run_time=2)
            self.play(Write(statement_line2), run_time=1.5)
            
            # === SUMMER CIRCLE (positioned like in original) ===
            summer_circle = Circle(
                radius=1.2,  # Smaller circle
                color="#00396B",  # Blue
                stroke_width=4.0,
                fill_opacity=0
            )
            summer_circle.move_to(DOWN * 1.7 + LEFT * 1.5)  # Move down from center
            
            summer_label = Text(
                "Summer",
                font_size=20,
                color="#00396B",
                font="sans-serif",
                weight=BOLD
            )
            # Position Summer label above and to the left of circle
            summer_label.move_to(summer_circle.get_center() + LEFT * 1.7 + UP * 1.0)
            
            # Show Summer circle
            self.play(
                Write(summer_label),
                Create(summer_circle),
                run_time=2
            )

            # === WINTER CIRCLE (positioned to the side and upper) ===
            winter_circle = Circle(
                radius=1.2,  # Same size as summer
                color="#008000",  # Green
                stroke_width=4.0,
                fill_opacity=0
            )
            # Position winter to the right and slightly up from summer
            winter_circle.move_to(summer_circle.get_center() + RIGHT * 2.2 + UP * 1.0)
            
            winter_label = Text(
                "Winter",
                font_size=20,
                color="#008000",
                font="sans-serif",
                weight=BOLD
            )
            # Position Winter label above and to the right of its circle
            winter_label.move_to(winter_circle.get_center() + RIGHT * 1.7 + UP * 1.0)
            
            # Show Winter circle
            self.play(
                Write(winter_label),
                Create(winter_circle),
                run_time=2
            )

            # === TEMPERATURE CIRCLES ===
            # Summer temperature circle (upper left inside summer circle)
            summer_temp_circle = Circle(
                radius=0.4,  # Small circle
                color="#CC0000",  # Red
                stroke_width=3.0,
                fill_opacity=0
            )
            summer_temp_circle.move_to(summer_circle.get_center() + RIGHT * 0.72 + UP * 0.3)
            
            summer_temp_text = Text(
                "> 20°C",
                font_size=14,
                color="#CC0000",
                font="sans-serif",
                weight=BOLD
            )
            summer_temp_text.move_to(summer_temp_circle.get_center())
            
            # Winter temperature circle (bottom inside winter circle)
            winter_temp_circle = Circle(
                radius=0.2,  # Small circle
                color="#CC0000",  # Red
                stroke_width=3.0,
                fill_opacity=0
            )
            winter_temp_circle.move_to(winter_circle.get_center() + DOWN * 0.4 + LEFT * 0.9)
            
            winter_temp_text = Text(
                "> 20°C",
                font_size=6,
                color="#CC0000",
                font="sans-serif",
                weight=BOLD
            )
            winter_temp_text.move_to(winter_temp_circle.get_center())
            
            # Show temperature circles
            self.play(
                Create(summer_temp_circle),
                Write(summer_temp_text),
                Create(winter_temp_circle),
                Write(winter_temp_text),
                run_time=2
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 11.5)

        with self.voiceover(text="The shaded area is therefore the days that I can cycle, and we could write this as the union of summer and the intersection of winter with days warmer than twenty degrees.") as tracker:
            # === FILL SUMMER CIRCLE WITH GRAY ===
            filled_summer_circle = summer_circle.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(summer_circle, filled_summer_circle),
                run_time=1.0
            )

            # === FILL WINTER TEMPERATOR CIRCLE WITH LIGHT GRAY ===
            filled_winter_temp_circle = winter_temp_circle.copy().set_fill(color="#C0C0C0", opacity=0.6)

            self.play(
                ReplacementTransform(winter_temp_circle, filled_winter_temp_circle),
                run_time=1.0
            )

            # === CONCLUSION ===
            conclusion_text = MathTex(
                r'\text{Summer} \cup (\text{Winter} \cap > 20°\text{C})',
                font_size=32,
                color="#505050"
            )
            conclusion_text.move_to(summer_circle.get_center() + DOWN * 1.5 + RIGHT * 3.0)
            
            # Blue underline for conclusion
            conclusion_underline = Line(
                start=conclusion_text.get_corner(DOWN + LEFT),
                end=conclusion_text.get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue
                stroke_width=3
            )
            conclusion_underline.shift(DOWN * 0.1)
            
            # Show conclusion
            self.play(Write(conclusion_text), run_time=2.5)
            self.play(Create(conclusion_underline), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.0)

        with self.voiceover(text="We can use the distributive property we've just seen to work with the logic of a given statement.") as tracker:
            # === CLEAR EVERYTHING FROM SCREEN FIRST ===
            self.play(
                FadeOut(VGroup(
                    statement_line1, statement_line2,
                    filled_summer_circle, filled_winter_temp_circle, winter_circle,
                    summer_label, winter_label, summer_temp_circle, summer_temp_text, 
                    winter_temp_text, conclusion_text, conclusion_underline
                )),
                run_time=1.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 1.5)
        
        with self.voiceover(text="So if we have the set of days in the summer or winter and more than twenty degrees, the identity says that this must be the same as summer or winter and summer or more than twenty degrees.") as tracker:
            # === START FRESH WITH DISTRIBUTIVE LAW DEMONSTRATION ===
            
            # Distributive law formula at the top - properly centered
            formula = MathTex(
                r'A \cup (B \cap C) = (A \cup B) \cap (A \cup C)',
                font_size=44,
                color="#505050"
            )
            formula.to_edge(UP, buff=1.0)
            
            # Show the formula
            self.play(Write(formula), run_time=2.5)
            
            # Real-world example line - centered
            example_text = MarkupText(
                '<b><i>Summer or ( Winter and > 20°C )</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            example_text.move_to(UP * 1.5)
            
            # Show the example
            self.play(Write(example_text), run_time=2.5)
            
            # Equals sign - centered
            equals_sign = MathTex(
                r'=',
                font_size=40,
                color="#505050"
            )
            equals_sign.move_to(UP * 0.5)
            
            # Distributive application - centered
            distributive_result = MarkupText(
                '<b><i>( Summer or Winter ) and ( Summer or > 20°C )</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            distributive_result.move_to(DOWN * 0.5)
            
            # Show the transformation
            self.play(Write(equals_sign), run_time=1)
            self.play(Write(distributive_result), run_time=3)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        with self.voiceover(text="Which at first sight doesn't seem to make much sense, but notice that summer or winter is anytime, and summer or more than twenty degrees is the days when I cycle. We're ignoring other seasons in this example, and we're taking the intersection of these, so we get something like I cycle any day of the year but only when it's summer or more than twenty degrees, which actually makes sense and is another way of saying the original statement.") as tracker:
            # Final conclusion at the bottom - split into two lines and darker
            final_conclusion_line1 = MarkupText(
                '<b><i>I cycle any day of the year but only when it\'s</i></b>',
                color="#303030",  # Darker color
                font_size=36,
                font="sans-serif"
            )
            final_conclusion_line1.move_to(DOWN * 2.0)
            
            final_conclusion_line2 = MarkupText(
                '<b><i>summer or > 20°C.</i></b>',
                color="#303030",  # Darker color  
                font_size=36,
                font="sans-serif"
            )
            final_conclusion_line2.next_to(final_conclusion_line1, DOWN, buff=0.1, aligned_edge=LEFT)
            
            # Show the conclusion - both lines together
            self.play(
                Write(final_conclusion_line1),
                Write(final_conclusion_line2),
                run_time=3
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 3.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                formula, example_text, equals_sign, distributive_result,
                final_conclusion_line1, final_conclusion_line2
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_distributive_law_proof(self):
        """Show complete distributive law proof"""
        with self.voiceover(text="But before we move on from unions and intersections, I want to show you how we can mathematically prove a statement such as this one. Remember how earlier we showed that if A is a subset of B and if B is a subset of A, then A is equal to B? Well here we can use that exact method to prove this equation.") as tracker:
            # Main distributive law formula at the top
            main_formula = MathTex(
                r'A \cup (B \cap C) = (A \cup B) \cap (A \cup C)',
                font_size=44,
                color="#505050"
            )
            main_formula.to_edge(UP, buff=1.0)
            
            # Show the main formula
            self.play(Write(main_formula), run_time=2.5)
            
            # Proof header - LEFT ALIGNED
            proof_header = MarkupText(
                '<b><i>Proof:</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            proof_header.next_to(main_formula, DOWN, buff=0.5)
            proof_header.to_edge(LEFT, buff=1.0)
            
            # Show proof header
            self.play(Write(proof_header), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        with self.voiceover(text="We'll show first that A union B intersect C is a subset of A union B intersected with A union C, and that A union B intersected with A union C is a subset of A union B intersect C, which implies they're equal to one another.") as tracker:
            # "We will show" text - LEFT ALIGNED
            we_will_show = MarkupText(
                '<b><i>We will show</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            we_will_show.next_to(proof_header, DOWN, buff=0.4)
            we_will_show.to_edge(LEFT, buff=1.0)
            
            # Show "We will show"
            self.play(Write(we_will_show), run_time=1.5)
            
            # First subset relation - CENTERED (LaTeX)
            first_subset = MathTex(
                r'A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)',
                font_size=40,
                color="#505050"
            )
            first_subset.next_to(we_will_show, DOWN, buff=0.3)
            # Center this LaTeX formula
            first_subset.move_to([0, first_subset.get_center()[1], 0])
            
            # Show first subset
            self.play(Write(first_subset), run_time=2.5)
            
            # "and" text - LEFT ALIGNED
            and_text = MarkupText(
                '<b><i>and</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            and_text.next_to(first_subset, DOWN, buff=0.4)
            and_text.to_edge(LEFT, buff=1.0)
            
            # Show "and"
            self.play(Write(and_text), run_time=1)
            
            # Second subset relation - CENTERED (LaTeX)
            second_subset = MathTex(
                r'(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)',
                font_size=40,
                color="#505050"
            )
            second_subset.next_to(and_text, DOWN, buff=0.3)
            # Center this LaTeX formula
            second_subset.move_to([0, second_subset.get_center()[1], 0])
            
            # Show second subset
            self.play(Write(second_subset), run_time=2.5)
            
            # "and so" text - LEFT ALIGNED
            and_so_text = MarkupText(
                '<b><i>and so</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            and_so_text.next_to(second_subset, DOWN, buff=0.4)
            and_so_text.to_edge(LEFT, buff=1.0)
            
            # Show "and so"
            self.play(Write(and_so_text), run_time=1)
            
            # Final conclusion formula - CENTERED (LaTeX)
            conclusion_formula = MathTex(
                r'A \cup (B \cap C) = (A \cup B) \cap (A \cup C)',
                font_size=40,
                color="#505050"
            )
            conclusion_formula.next_to(and_so_text, DOWN, buff=0.3)
            # Center this LaTeX formula
            conclusion_formula.move_to([0, conclusion_formula.get_center()[1], 0])
            
            # Show conclusion
            self.play(Write(conclusion_formula), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 12.0)

        with self.voiceover(text="First, suppose we have an element x which is in A union B intersect C. Well, it's either in A or it's in B intersect C, which would mean it's in both B and C. In either case, x is in both A union B and A union C, because if it's in A this is true, and if it's in B it's also in C so it's still true.") as tracker:
            # === CLEAR PREVIOUS PROOF STRUCTURE ===
            self.play(
                FadeOut(VGroup(
                    we_will_show, first_subset, and_text, 
                    second_subset, and_so_text, conclusion_formula
                )),
                run_time=1.5
            )
            
            # === START DETAILED PROOF ===
            
            # "Suppose x ∈ A ∪ (B ∩ C), then either x ∈ A or" - first line
            suppose_line1 = MathTex(
                r'\text{Suppose } x \in A \cup (B \cap C)\text{, then either } x \in A \text{ or}',
                font_size=36,
                color="#505050"
            )
            suppose_line1.next_to(proof_header, DOWN, buff=0.5)
            suppose_line1.to_edge(LEFT, buff=1.0)
            
            # "x ∈ (B ∩ C)" - second line
            suppose_line2 = MathTex(
                r'x \in (B \cap C)',
                font_size=36,
                color="#505050"
            )
            suppose_line2.next_to(suppose_line1, DOWN, buff=0.2)
            suppose_line2.to_edge(LEFT, buff=1.0)
            
            # Show suppose statement
            self.play(Write(suppose_line1), run_time=2.5)
            self.play(Write(suppose_line2), run_time=1.5)
            
            # === CREATE VENN DIAGRAM ON THE RIGHT ===
            
            # Three overlapping circles
            circle_A = Circle(radius=1.2, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A.move_to(RIGHT * 2.5 + DOWN * 1.2)
            
            circle_B = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B.move_to(RIGHT * 4.0 + DOWN * 0.3)
            
            circle_C = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C.move_to(RIGHT * 4.0 + DOWN * 2.1)
            
            # Labels for circles
            label_A = Text("A", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            label_A.move_to(circle_A.get_center())
            
            label_B = Text("B", font_size=24, color="#008000", font="sans-serif", weight=BOLD)
            label_B.move_to(circle_B.get_center() + UP * 0.8)
            
            label_C = Text("C", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            label_C.move_to(circle_C.get_center() + DOWN * 0.8)
            
            # Create circles and labels
            self.play(
                Create(circle_A),
                Create(circle_B),
                Create(circle_C),
                Write(label_A),
                Write(label_B),
                Write(label_C),
                run_time=2.5
            )
            
            # === FILL REGIONS WITH GRAY ===
            
            # Fill circle A with gray
            filled_A = circle_A.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            # Fill B ∩ C intersection with gray
            bc_intersection = Intersection(circle_B, circle_C)
            bc_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            bc_intersection.set_stroke(width=0)
            
            # Show filled regions
            self.play(
                ReplacementTransform(circle_A, filled_A),
                FadeIn(bc_intersection),
                run_time=2
            )
            
            # === ADD ANNOTATIONS WITH ARROWS ===
            
            # "x ∈ A" label with arrow
            x_in_A_label = MathTex(r'x \in A', font_size=24, color="#505050")
            x_in_A_label.move_to(circle_A.get_center() + LEFT * 1.8)
            
            # Arrow pointing to A
            arrow_to_A = Arrow(
                start=x_in_A_label.get_right() + RIGHT * 0.1,
                end=circle_A.get_center() + LEFT * 0.5,
                color="#505050",
                buff=0.1,
                stroke_width=2,
                tip_length=0.15
            )
            
            # "x ∈ (B ∩ C)" label with arrow
            x_in_BC_label = MathTex(r'x \in (B \cap C)', font_size=24, color="#505050")
            x_in_BC_label.move_to(RIGHT * 5.8 + DOWN * 1.2)
            
            # Arrow pointing to B∩C intersection
            arrow_to_BC = Arrow(
                start=x_in_BC_label.get_left() + LEFT * 0.1,
                end=RIGHT * 4.3 + DOWN * 1.2,
                color="#505050",
                buff=0.1,
                stroke_width=2,
                tip_length=0.15
            )
            
            # Show annotations with arrows
            self.play(
                Write(x_in_A_label),
                Create(arrow_to_A),
                Write(x_in_BC_label),
                Create(arrow_to_BC),
                run_time=2.5
            )
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 13.0)

        with self.voiceover(text="So this means that A union B intersect C, the thing we started with, is a subset of A union B intersected with A union C, since we've shown any element of the left hand side is an element of the right hand side.") as tracker:
            # === FADE OUT VENN DIAGRAM ===
            self.play(
                FadeOut(VGroup(
                    filled_A, circle_B, circle_C, bc_intersection,
                    label_A, label_B, label_C,
                    x_in_A_label, arrow_to_A, x_in_BC_label, arrow_to_BC
                )),
                run_time=1.5
            )
            
            # === ADD "IN EITHER CASE" TEXT ===
            in_either_case = MathTex(
                r'\text{In either case, } x \in (A \cup B) \text{ and } x \in (A \cup C).',
                font_size=36,
                color="#505050"
            )
            in_either_case.move_to(DOWN * 0.5)
            in_either_case.to_edge(LEFT, buff=1.0)
            
            # Show "In either case" text
            self.play(Write(in_either_case), run_time=2.5)
            
            # === ADD CONCLUSION WITH BLUE UNDERLINE ===
            conclusion_subset = MathTex(
                r'A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)',
                font_size=40,
                color="#505050"
            )
            conclusion_subset.move_to(DOWN * 2.2)
            # Center the conclusion formula
            conclusion_subset.move_to([0, conclusion_subset.get_center()[1], 0])
            
            # Blue underline for the conclusion
            blue_underline = Line(
                start=conclusion_subset.get_corner(DOWN + LEFT),
                end=conclusion_subset.get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue color
                stroke_width=3
            )
            blue_underline.shift(DOWN * 0.15)
            
            # Show conclusion and underline
            self.play(Write(conclusion_subset), run_time=2.5)
            self.play(Create(blue_underline), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 6.5)

        with self.voiceover(text="Now suppose x is in A union B intersect with A union C. Then x is in both A union B and A union C. If x is not in A, then x must be in both B and C, so it must be in the intersection of B and C. Otherwise x is in A, so x is in the union of A and B intersect C. Which means A union B intersect A union C is a subset of A union B intersect C.") as tracker:
            # === CLEAR EVERYTHING FROM SCREEN ===
            self.play(
                FadeOut(VGroup(
                    main_formula, proof_header, suppose_line1, suppose_line2,
                    in_either_case, conclusion_subset, blue_underline
                )),
                run_time=1.5
            )
            
            # === START SECOND PART OF PROOF ===
            
            # "Now suppose x ∈ (A ∪ B) ∩ (A ∪ C)" - first line
            now_suppose_line1 = MathTex(
                r'\text{Now suppose } x \in (A \cup B) \cap (A \cup C)',
                font_size=36,
                color="#505050"
            )
            now_suppose_line1.to_edge(UP, buff=1.0)
            now_suppose_line1.to_edge(LEFT, buff=1.0)
            
            # Show first line
            self.play(Write(now_suppose_line1), run_time=2.5)
            
            # "then x ∈ (A ∪ B) and x ∈ (A ∪ C)." - second line
            now_suppose_line2 = MathTex(
                r'\text{then } x \in (A \cup B) \text{ and } x \in (A \cup C).',
                font_size=36,
                color="#505050"
            )
            now_suppose_line2.next_to(now_suppose_line1, DOWN, buff=0.2)
            now_suppose_line2.to_edge(LEFT, buff=1.0)
            
            # Show second line
            self.play(Write(now_suppose_line2), run_time=2.5)
            
            # === CREATE VENN DIAGRAM - SHOWING A ∪ B FIRST ===
            
            # Three overlapping circles
            circle_A_new = Circle(radius=1.2, color="#00396B", stroke_width=4.0, fill_opacity=0)
            circle_A_new.move_to(RIGHT * 2.5 + DOWN * 1.2)
            
            circle_B_new = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B_new.move_to(RIGHT * 4.0 + DOWN * 0.3)
            
            circle_C_new = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C_new.move_to(RIGHT * 4.0 + DOWN * 2.1)
            
            # Labels for circles
            label_A_new = Text("A", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            label_A_new.move_to(circle_A_new.get_center())
            
            label_B_new = Text("B", font_size=24, color="#008000", font="sans-serif", weight=BOLD)
            label_B_new.move_to(circle_B_new.get_center() + UP * 0.8)
            
            label_C_new = Text("C", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            label_C_new.move_to(circle_C_new.get_center() + DOWN * 0.8)
            
            # Create circles and labels
            self.play(
                Create(circle_A_new),
                Create(circle_B_new),
                Create(circle_C_new),
                Write(label_A_new),
                Write(label_B_new),
                Write(label_C_new),
                run_time=2.5
            )
            
            # === FILL A ∪ B (IMAGE 1) ===
            filled_A_new = circle_A_new.copy().set_fill(color="#A0A0A0", opacity=0.6)
            filled_B_new = circle_B_new.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(circle_A_new, filled_A_new),
                ReplacementTransform(circle_B_new, filled_B_new),
                run_time=2
            )
            
            # === ADD SECOND LINE AND FILL A ∪ C (IMAGE 2) ===
            
            # Show second line and fill C as well
            filled_C_new = circle_C_new.copy().set_fill(color="#A0A0A0", opacity=0.6)
            
            self.play(
                ReplacementTransform(circle_C_new, filled_C_new),
                run_time=2.5
            )
            
            # === SHOW FINAL INTERSECTION A ∪ (B ∩ C) (IMAGE 3) ===
            
            # Remove B and C fills, keep A fill, add B ∩ C intersection
            circle_B_empty = Circle(radius=1.2, color="#008000", stroke_width=4.0, fill_opacity=0)
            circle_B_empty.move_to(RIGHT * 4.0 + DOWN * 0.3)
            
            circle_C_empty = Circle(radius=1.2, color="#CC0000", stroke_width=4.0, fill_opacity=0)
            circle_C_empty.move_to(RIGHT * 4.0 + DOWN * 2.1)
            
            bc_intersection_new = Intersection(circle_B_new, circle_C_new)
            bc_intersection_new.set_fill(color="#A0A0A0", opacity=0.9)
            bc_intersection_new.set_stroke(width=0)
            
            self.play(
                ReplacementTransform(filled_B_new, circle_B_empty),
                ReplacementTransform(filled_C_new, circle_C_empty),
                FadeIn(bc_intersection_new),
                run_time=2.5
            )
            
            # === FADE OUT VENN DIAGRAM ===
            self.play(
                FadeOut(VGroup(
                    filled_A_new, circle_B_empty, circle_C_empty, bc_intersection_new,
                    label_A_new, label_B_new, label_C_new
                )),
                run_time=1.5
            )
            
            # === ADD LOGICAL REASONING STEPS ===
            
            # "If x ∉ A, then x ∈ B and x ∈ C ⟹ x ∈ (B ∩ C)"
            if_step = MathTex(
                r'\text{If } x \notin A\text{, then } x \in B \text{ and } x \in C \Longrightarrow x \in (B \cap C)',
                font_size=36,
                color="#505050"
            )
            if_step.move_to(UP * 0.5)
            if_step.to_edge(LEFT, buff=1.0)
            
            # Show if step
            self.play(Write(if_step), run_time=2.5)
            
            # "Otherwise x ∈ A,"
            otherwise_step = MathTex(
                r'\text{Otherwise } x \in A,',
                font_size=36,
                color="#505050"
            )
            otherwise_step.next_to(if_step, DOWN, buff=0.8)
            otherwise_step.to_edge(LEFT, buff=1.0)
            
            # Show otherwise step
            self.play(Write(otherwise_step), run_time=1.5)
            
            # "Therefore x ∈ A ∪ (B ∩ C),"
            therefore_step = MathTex(
                r'\text{Therefore } x \in A \cup (B \cap C),',
                font_size=36,
                color="#505050"
            )
            therefore_step.next_to(otherwise_step, DOWN, buff=0.8)
            therefore_step.to_edge(LEFT, buff=1.0)
            
            # Show therefore step
            self.play(Write(therefore_step), run_time=2)
            
            # === FINAL CONCLUSION WITH BLUE UNDERLINE ===
            
            final_subset_conclusion = MathTex(
                r'(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)',
                font_size=40,
                color="#505050"
            )
            final_subset_conclusion.move_to(DOWN * 2.5)
            # Center the conclusion formula
            final_subset_conclusion.move_to([0, final_subset_conclusion.get_center()[1], 0])
            
            # Blue underline for the final conclusion
            final_blue_underline = Line(
                start=final_subset_conclusion.get_corner(DOWN + LEFT),
                end=final_subset_conclusion.get_corner(DOWN + RIGHT),
                color="#1853A2",  # Blue color
                stroke_width=3
            )
            final_blue_underline.shift(DOWN * 0.15)
            
            # Show final conclusion and underline
            self.play(Write(final_subset_conclusion), run_time=2.5)
            self.play(Create(final_blue_underline), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 18.5)

        with self.voiceover(text="If A union B intersect C is a subset of A union B intersected with A union C, and A union B intersected with A union C is a subset of A union B intersect C, then A union B intersect C equals A union B intersected with A union C.") as tracker:
            # === CLEAR EVERYTHING FROM SCREEN ===
            self.play(
                FadeOut(VGroup(
                    now_suppose_line1, now_suppose_line2, if_step, otherwise_step,
                    therefore_step, final_subset_conclusion, final_blue_underline
                )),
                run_time=1.5
            )
            
            # === FINAL LOGICAL CONCLUSION STRUCTURE ===
            
            # "If" with first subset relation
            if_statement = VGroup(
                MathTex(r'\text{If}', font_size=36, color="#505050"),
                MathTex(r'A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)', font_size=36, color="#505050")
            )
            if_statement.arrange(RIGHT, buff=0.5)
            if_statement.move_to(UP * 1.5)
            if_statement.to_edge(LEFT, buff=1.0)
            
            # Show if statement
            self.play(Write(if_statement), run_time=2.5)
            
            # "and" with second subset relation
            and_statement = VGroup(
                MathTex(r'\text{and}', font_size=36, color="#505050"),
                MathTex(r'(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)', font_size=36, color="#505050")
            )
            and_statement.arrange(RIGHT, buff=0.5)
            and_statement.move_to(ORIGIN)
            and_statement.to_edge(LEFT, buff=1.0)
            
            # Show and statement
            self.play(Write(and_statement), run_time=2.5)
            
            # "then" with final equality
            then_statement = VGroup(
                MathTex(r'\text{then}', font_size=36, color="#505050"),
                MathTex(r'A \cup (B \cap C) = (A \cup B) \cap (A \cup C)', font_size=36, color="#505050")
            )
            then_statement.arrange(RIGHT, buff=0.5)
            then_statement.move_to(DOWN * 1.5)
            then_statement.to_edge(LEFT, buff=1.0)
            
            # Show then statement
            self.play(Write(then_statement), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 7.5)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(if_statement, and_statement, then_statement)),
            run_time=1
        )
        self.wait(1)
    
    def show_shirts_venn_diagram(self):
        """Show shirts Venn diagram example with distributive law"""
        with self.voiceover(text="Now consider the statement 'I only wear white or blue shirts.' Here we have three sets: shirts, blue clothes, and white clothes. And for specifically blue and white shirts, we take the intersection of the union of blue and white clothes with shirts.") as tracker:
            # Statement at the top
            statement = MarkupText(
                '<b><i>I only wear white or blue shirts.</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            statement.to_edge(UP, buff=1.0)
            
            # Show statement
            self.play(Write(statement), run_time=2)
            
            # === SHIRTS CIRCLE (GREEN) - FIRST ===
            shirts_circle = Circle(
                radius=1.5,
                color="#008000",  # Green
                stroke_width=4.0,
                fill_opacity=0
            )
            shirts_circle.move_to(UP * 0.8)
            
            shirts_label = Text(
                "Shirts",
                font_size=32,
                color="#008000",
                font="sans-serif",
                weight=BOLD
            )
            shirts_label.move_to(shirts_circle.get_center() + UP * 0.5)
            
            # Show shirts circle
            self.play(
                Create(shirts_circle),
                Write(shirts_label),
                run_time=2
            )
            
            # === WHITE CLOTHES CIRCLE (RED) - SECOND ===
            white_circle = Circle(
                radius=1.5,
                color="#CC0000",  # Red
                stroke_width=4.0,
                fill_opacity=0
            )
            white_circle.move_to(DOWN * 0.8 + RIGHT * 1.2)
            
            white_label = VGroup(
                Text("White", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD),
                Text("clothes", font_size=24, color="#CC0000", font="sans-serif", weight=BOLD)
            )
            white_label.arrange(DOWN, buff=0.1)
            white_label.move_to(white_circle.get_center() + DOWN * 0.5)
            
            # Show white clothes circle
            self.play(
                Create(white_circle),
                Write(white_label),
                run_time=2
            )
            
            # === BLUE CLOTHES CIRCLE (BLUE) - THIRD ===
            blue_circle = Circle(
                radius=1.5,
                color="#00396B",  # Blue
                stroke_width=4.0,
                fill_opacity=0
            )
            blue_circle.move_to(DOWN * 0.8 + LEFT * 1.2)
            
            blue_label = VGroup(
                Text("Blue", font_size=24, color="#00396B", font="sans-serif", weight=BOLD),
                Text("clothes", font_size=24, color="#00396B", font="sans-serif", weight=BOLD)
            )
            blue_label.arrange(DOWN, buff=0.1)
            blue_label.move_to(blue_circle.get_center() + DOWN * 0.5)
            
            # Show blue clothes circle
            self.play(
                Create(blue_circle),
                Write(blue_label),
                run_time=2
            )
            
            # === FILL INTERSECTION AREAS WITH GRAY ===
            # Shirts ∩ White clothes
            shirts_white_intersection = Intersection(shirts_circle, white_circle)
            shirts_white_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            shirts_white_intersection.set_stroke(width=0)
            
            # Shirts ∩ Blue clothes
            shirts_blue_intersection = Intersection(shirts_circle, blue_circle)
            shirts_blue_intersection.set_fill(color="#A0A0A0", opacity=0.6)
            shirts_blue_intersection.set_stroke(width=0)
            
            # Show both intersections
            self.play(
                FadeIn(shirts_white_intersection),
                FadeIn(shirts_blue_intersection),
                run_time=2
            )
            
            # === FORMULA AT THE BOTTOM ===
            formula = MathTex(
                r'\text{Shirts} \cap (\text{Blue clothes} \cup \text{White Clothes})',
                font_size=42,
                color="#505050"
            )
            formula.to_edge(DOWN, buff=1.0)
            
            # Show formula
            self.play(Write(formula), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 14.5)

        with self.voiceover(text="Like before, we can use the distributive rule to play around with the logic. So shirts and blue or white becomes blue shirts or white shirts.") as tracker:
            # === CLEAR VENN DIAGRAM AND TRANSITION TO DISTRIBUTIVE LAW ===
            
            # Fade out the Venn diagram elements
            self.play(
                FadeOut(VGroup(
                    shirts_circle, white_circle, blue_circle,
                    shirts_label, white_label, blue_label,
                    shirts_white_intersection, shirts_blue_intersection, formula
                )),
                run_time=1.5
            )
            
            # Keep the original statement at top
            # statement is already there, no need to recreate
            
            # === DISTRIBUTIVE LAW DEMONSTRATION ===
            
            # Distributive law formula at the top
            distributive_formula = MathTex(
                r'A \cap (B \cup C) = (A \cap B) \cup (A \cap C)',
                font_size=44,
                color="#505050"
            )
            distributive_formula.move_to(UP * 2)
            
            # Show the formula
            self.play(Write(distributive_formula), run_time=2.5)
            
            # Real-world example line
            shirts_example = MarkupText(
                '<b><i>Shirts and ( Blue or white )</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            shirts_example.move_to(UP * 0.8)
            
            # Show the example
            self.play(Write(shirts_example), run_time=2.5)
            
            # Equals sign
            equals_sign = MathTex(
                r'=',
                font_size=40,
                color="#505050"
            )
            equals_sign.move_to(DOWN * 0.2)
            
            # Distributive application
            distributive_result = MarkupText(
                '<b><i>( Blue shirts ) or ( White shirts )</i></b>',
                color="#505050",
                font_size=36,
                font="sans-serif"
            )
            distributive_result.move_to(DOWN * 1.2)
            
            # Show the transformation
            self.play(Write(equals_sign), run_time=1)
            self.play(Write(distributive_result), run_time=3)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        with self.voiceover(text="This can now be interpreted as 'I only wear blue shirts or white shirts.' It doesn't feel too different to the original statement, but again it's quite satisfying that it comes straight out of the set theoretic rules.") as tracker:
            # Final conclusion at the bottom - in quotes and darker
            final_conclusion = MarkupText(
                '<b><i>"I only wear blue shirts or white shirts"</i></b>',
                color="#303030",  # Darker color
                font_size=36,
                font="sans-serif"
            )
            final_conclusion.to_edge(DOWN, buff=1.5)
            
            # Show the conclusion
            self.play(Write(final_conclusion), run_time=3)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 3.0)
        
        # Clear everything before ending
        self.play(
            FadeOut(VGroup(
                statement, distributive_formula, shirts_example, equals_sign, 
                distributive_result, final_conclusion
            )),
            run_time=1
        )
        self.wait(2)