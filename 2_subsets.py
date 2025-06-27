from manim import *

class Subsets(Scene):
    def construct(self):
        """Main method that orchestrates the entire video"""
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.clear()
        self.show_definition()
        self.clear()
        self.show_question()
        self.clear()
        self.show_equality_theorem()
        self.clear()
        self.show_transitivity()

    
    def show_title(self):
        """Display the main title: Subsets"""
        # Create the "Subsets" title
        subsets_title = Text(
            "Subsets",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        
        # Center the title
        subsets_title.move_to(ORIGIN)
        
        # Create underline
        underline = Line(
            start=subsets_title.get_corner(DOWN + LEFT),
            end=subsets_title.get_corner(DOWN + RIGHT),
            color=BLACK,
            stroke_width=2
        )
        underline.shift(DOWN * 0.2)

        # Animation sequence
        self.play(AddTextLetterByLetter(subsets_title), run_time=2)
        self.wait(0.5)
        self.play(Create(underline), run_time=1)
        self.wait(2)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(subsets_title, underline)), run_time=1)
        self.wait(0.5)
    
    def show_definition(self):
        """Show subset definition with visual examples and formal notation"""
        # Definition text at the top
        definition_line1 = MarkupText(
            '<b><i>A set is a subset of another if all of it\'s elements</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        definition_line2 = MarkupText(
            '<b><i>are also elements of another set.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the definition text
        definition_line1.to_edge(UP, buff=1.0)
        definition_line1.to_edge(LEFT, buff=0.5)
        definition_line2.next_to(definition_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show definition text
        self.play(Write(VGroup(definition_line1, definition_line2)), run_time=2)
        self.wait(2)
        
        # Create the larger green circle (B) - smaller and centered
        circle_B = Circle(
            radius=2.0,  # Reduced from 2.5
            color="#008000",  # Green color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_B.move_to(ORIGIN)
        
        # Create the smaller blue circle (A) inside B - much smaller and positioned to the left
        circle_A = Circle(
            radius=0.8,  # Much smaller, reduced from 1.5
            color="#00396B",  # Blue color  
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_A.move_to(LEFT * 0.8)  # Position to the left inside circle B
        
        # Add labels A and B
        label_A = MarkupText(
            '<b><i>A</i></b>',
            color="#00396B",  # Blue color to match circle
            font_size=28,
            font="sans-serif"
        )
        
        label_B = MarkupText(
            '<b><i>B</i></b>',
            color="#008000",  # Green color to match circle
            font_size=28,
            font="sans-serif"
        )
        
        # Position labels - A in the smaller left circle, B in the upper right area (both moved up)
        label_A.move_to(circle_A.get_center() + UP * 0.3)  # Moved up
        # Position B in the upper right area of the outer circle, outside the inner circle (moved up)
        label_B.move_to(circle_B.get_center() + UP * 1.6 + RIGHT * 0.3)  # Moved up
        
        # Create both circles and labels at the same time as requested
        self.play(
            Create(circle_B),
            Create(circle_A),
            Write(label_A),
            Write(label_B),
            run_time=2
        )
        self.wait(1)
        
        # Bottom conclusion text - aligned with the left edge of the definition
        conclusion_text = MarkupText(
            '<b><i>"A is a subset of B"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        conclusion_text.move_to(DOWN * 3)
        conclusion_text.to_edge(LEFT, buff=0.5)  # Align with the definition text
        
        # Show conclusion
        self.play(Write(conclusion_text), run_time=1.5)
        
        # Hold the final scene
        self.wait(1.5)

        self.play(
            FadeOut(conclusion_text),
            FadeOut(circle_A),
            FadeOut(circle_B),
            FadeOut(label_A),
            FadeOut(label_B),
            run_time=1.5
        )
        self.wait(1)

        # Add the sets A and B with proper indexing for precise arrow positioning
        set_A = MathTex(r'A', r'=', r'\{', r'2', r',', r'4', r',', r'6', r'\}', font_size=36, color="#505050")
        set_B = MathTex(r'B', r'=', r'\{', r'1', r',', r'2', r',', r'3', r',', r'4', r',', r'6', r'\}', font_size=36, color="#505050")
        
        # Position the sets
        set_A.move_to(LEFT * 2.5 + DOWN * 0.5)
        set_B.move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        # Show the sets
        self.play(Write(set_A), run_time=1.5)
        self.wait(0.5)
        self.play(Write(set_B), run_time=1.5)
        self.wait(1)
        
        # Create arrows from A elements to corresponding B elements (curving upward)
        # Arrow from "2" in A to "2" in B
        arrow_2 = CurvedArrow(
            start_point=set_A[3].get_top(),    # Top of "2" in A (index 3)
            end_point=set_B[5].get_top(),      # Top of "2" in B (index 5)
            color="#505050",
            angle=-PI/4,
            tip_length=0.15
        )
        
        # Arrow from "4" in A to "4" in B
        arrow_4 = CurvedArrow(
            start_point=set_A[5].get_top(),    # Top of "4" in A (index 5)
            end_point=set_B[9].get_top(),      # Top of "4" in B (index 9)
            color="#505050",
            angle=-PI/5,
            tip_length=0.15
        )
        
        # Arrow from "6" in A to "6" in B
        arrow_6 = CurvedArrow(
            start_point=set_A[7].get_top(),    # Top of "6" in A (index 7)
            end_point=set_B[11].get_top(),     # Top of "6" in B (index 11)
            color="#505050",
            angle=-PI/6,
            tip_length=0.15
        )
        
        # Show arrows sequentially
        self.play(Create(arrow_2), run_time=1)
        self.wait(1)
        self.play(Create(arrow_4), run_time=1)
        self.wait(1)
        self.play(Create(arrow_6), run_time=1)
        self.wait(2)
        
        # Show the subset notation A ⊆ B
        subset_notation = MathTex(r'A \subseteq B', font_size=42, color="#505050")
        subset_notation.move_to(DOWN * 1.8)
        
        self.play(Write(subset_notation), run_time=1.5)
        self.wait(2)
        
        # Show final conclusion
        final_conclusion = MarkupText(
            '<b><i>"A is a subset of B"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        final_conclusion.move_to(DOWN * 2.8)
        
        self.play(Write(final_conclusion), run_time=1.5)
        self.wait(1.5)

        # Create a transparent black highlight over the subset symbol
        highlight_box = RoundedRectangle(
            width=0.8,
            height=0.6,
            corner_radius=0.1,
            color=BLACK,
            fill_opacity=0.3,
            stroke_opacity=0
        )
        highlight_box.move_to(subset_notation.get_center())
        
        # Dim everything else slightly
        dimmed_definition_line1 = definition_line1.copy().set_opacity(0.4)
        dimmed_definition_line2 = definition_line2.copy().set_opacity(0.4)
        dimmed_set_A = set_A.copy().set_opacity(0.4)
        dimmed_set_B = set_B.copy().set_opacity(0.4)
        dimmed_arrows = VGroup(arrow_2, arrow_4, arrow_6).copy().set_opacity(0.4)
        dimmed_conclusion = final_conclusion.copy().set_opacity(0.4)
        
        # Apply the highlighting effect
        self.play(
            FadeIn(highlight_box),
            ReplacementTransform(definition_line1, dimmed_definition_line1),
            ReplacementTransform(definition_line2, dimmed_definition_line2),
            ReplacementTransform(set_A, dimmed_set_A),
            ReplacementTransform(set_B, dimmed_set_B),
            ReplacementTransform(VGroup(arrow_2, arrow_4, arrow_6), dimmed_arrows),
            ReplacementTransform(final_conclusion, dimmed_conclusion),
            run_time=1.5
        )

        self.wait(3)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                highlight_box, dimmed_definition_line1, dimmed_definition_line2,
                dimmed_set_A, dimmed_set_B, dimmed_arrows, dimmed_conclusion, subset_notation
            )),
            run_time=1
        )
        self.wait(0.5)
    
    def show_question(self):
        """Display practice question with multiple choice answers"""
        # Question text - bigger font
        question_line1 = MarkupText(
            '<b><i>Question. If B = {b ∈ ℕ | b is even}, which</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        question_line2 = MarkupText(
            '<b><i>of these are subsets of B?</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        # Position the question text
        question_line1.to_edge(UP, buff=1.0)
        question_line1.to_edge(LEFT, buff=0.5)
        question_line2.next_to(question_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Show question text
        self.play(Write(VGroup(question_line1, question_line2)), run_time=2)
        self.wait(2)
        
        # Option (a) - aligned with question text
        option_a = MathTex(
            r'\text{(a) } 4',
            font_size=44,
            color="#505050"
        )
        option_a.to_edge(LEFT, buff=0.5)
        option_a.next_to(question_line2, DOWN, aligned_edge=LEFT, buff=1.0)
        
        # Show option (a)
        self.play(Write(option_a), run_time=1.5)
        self.wait(2.5)
        
        # Option (b) - aligned with option (a)
        option_b = MathTex(
            r'\text{(b) } \{ 10, 100, 1000 \}',
            font_size=44,
            color="#505050"
        )
        option_b.next_to(option_a, DOWN, aligned_edge=LEFT, buff=0.8)
        
        # Show option (b)
        self.play(Write(option_b), run_time=1.5)
        self.wait(3)
        
        # Option (c) - aligned with options (a) and (b)
        option_c = MathTex(
            r'\text{(c) } \{ a \mid a = 2k, k \in \mathbb{N} \}',
            font_size=44,
            color="#505050"
        )
        option_c.next_to(option_b, DOWN, aligned_edge=LEFT, buff=0.8)
        
        # Show option (c)
        self.play(Write(option_c), run_time=1.5)
        self.wait(3)
        
        # Symbols positioned to align with the letters (a), (b), (c)
        # X mark for option (a) - aligned with the letter "a"
        x_mark_a = SVGMobject("images/cross.svg")
        x_mark_a.set_color("#FF0000")
        x_mark_a.scale(0.15)
        x_mark_a.move_to([
            option_a.get_left()[0] + 6,  # Slightly right of the left edge to align with "a"
            option_a.get_center()[1],      # Same vertical position as option a
            0
        ])
        
        # Checkmark for option (b) - aligned with the letter "b"
        check_mark_b = SVGMobject("images/check.svg")
        check_mark_b.set_color("#008000")
        check_mark_b.scale(0.15)
        check_mark_b.move_to([
            option_b.get_left()[0] + 6,  # Same horizontal position as x_mark_a
            option_b.get_center()[1],      # Same vertical position as option b
            0
        ])
        
        # Checkmark for option (c) - aligned with the letter "c"
        check_mark_c = SVGMobject("images/check.svg")
        check_mark_c.set_color("#008000")
        check_mark_c.scale(0.15)
        check_mark_c.move_to([
            option_c.get_left()[0] + 6,  # Same horizontal position as others
            option_c.get_center()[1],      # Same vertical position as option c
            0
        ])
        
        # Show symbols sequentially
        self.play(FadeIn(x_mark_a), run_time=1)
        self.wait(1)
        
        self.play(FadeIn(check_mark_b), run_time=1)
        self.wait(1)
        
        self.play(FadeIn(check_mark_c), run_time=1)
        
        # Hold the final scene
        self.wait(3)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                question_line1, question_line2, option_a, option_b, option_c,
                x_mark_a, check_mark_b, check_mark_c
            )),
            run_time=1
        )
        self.wait(0.5)
    
    def show_equality_theorem(self):
        """Show set equality theorem and proper subset definition"""
        # Theorem text at the top
        theorem_text = MathTex(
            r'\text{If } A \subseteq B \text{ and } B \subseteq A \text{ then } A = B',
            font_size=44,
            color="#505050"
        )
        theorem_text.to_edge(UP, buff=1.0)
        theorem_text.to_edge(LEFT, buff=0.5)
        
        # Show theorem text
        self.play(Write(theorem_text), run_time=2)
        # No wait here - circles appear immediately
        
        # Create circle A (smaller, inner circle)
        circle_A = Circle(
            radius=1.8,  # Smaller radius
            color="#00396B",  # Blue color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_A.move_to(ORIGIN)
        
        # Create circle B (bigger, outer circle)
        circle_B = Circle(
            radius=1.9,  # Larger radius
            color="#008000",  # Green color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_B.move_to(ORIGIN)
        
        # Create labels A and B
        label_A = MarkupText(
            '<b><i>A</i></b>',
            color="#00396B",  # Blue color to match circle
            font_size=28,
            font="sans-serif"
        )
        
        label_B = MarkupText(
            '<b><i>B</i></b>',
            color="#008000",  # Green color to match circle
            font_size=28,
            font="sans-serif"
        )
        
        # Position labels - A inside circle A, B outside the circles
        label_A.move_to(circle_A.get_center() + LEFT * 1.5)  # A in the center of circle A
        label_B.move_to(circle_B.get_center() + RIGHT * 2.1)  # B outside, upper right
        
        # Show both circles and labels simultaneously
        self.play(
            Create(circle_A),
            Create(circle_B),
            Write(label_A),
            Write(label_B),
            run_time=2
        )
        
        self.wait(1.5)

        # New circle B (outer circle) - centered
        new_circle_B = Circle(
            radius=1.8,
            color="#008000",  # Green color
            stroke_width=4.0,
            fill_opacity=0
        )
        new_circle_B.move_to(ORIGIN)
        
        # New circle A (much smaller) - positioned bottom-left within B
        new_circle_A = Circle(
            radius=1.0,  # Much smaller
            color="#00396B",  # Blue color
            stroke_width=4.0,
            fill_opacity=0
        )
        new_circle_A.move_to(ORIGIN + LEFT * 0.5 + DOWN * 0.5)
        
        # New labels
        new_label_A = MarkupText(
            '<b><i>A</i></b>',
            color="#00396B",
            font_size=24,
            font="sans-serif"
        )
        new_label_A.move_to(new_circle_A.get_center())
        
        new_label_B = MarkupText(
            '<b><i>B</i></b>',
            color="#008000",
            font_size=28,
            font="sans-serif"
        )
        new_label_B.move_to(new_circle_B.get_center() + UP * 1.5 + RIGHT * 0.1)
        
        # Smooth transition animation - fade out EVERYTHING (including theorem text), fade in new circles
        self.play(
            FadeOut(VGroup(theorem_text, circle_A, circle_B, label_A, label_B)),
            run_time=0.5
        )
        
        self.play(
            FadeIn(VGroup(new_circle_A, new_circle_B, new_label_A, new_label_B)),
            run_time=0.8
        )
        
        self.wait(1.5)

        # Add the proper subset theorem text at the top
        proper_subset_text = MathTex(
            r'\text{If } A \subseteq B \text{ but } A \neq B\text{, then } A \text{ is a }',
            r'\underline{\text{proper subset}}',
            r'\text{ of } B',
            font_size=40,
            color="#505050"
        )
        
        # Make "proper subset" blue and underlined
        proper_subset_text[1].set_color("#1853A2")  # Blue color for underlined part
        
        # Position at the top
        proper_subset_text.to_edge(UP, buff=1.0)
        proper_subset_text.to_edge(LEFT, buff=0.5)
        
        # Show the theorem text
        self.play(Write(proper_subset_text), run_time=2.5)
        self.wait(1)
        
        # Add explanatory text and arrow pointing to the space between circles
        explanation_text = MarkupText(
            '<b><i>Elements in B</i></b>\n<b><i>but not in A</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        
        # Position the text to the right
        explanation_text.move_to(RIGHT * 5 + UP * 1.6)
        
        # Create arrow pointing to the space between A and B (the ring area)
        arrow = CurvedArrow(
            start_point=explanation_text.get_left() + LEFT * 0.2,
            end_point=new_circle_B.get_center() + UP * 1.2 + RIGHT * 0.5,
            color="#505050",
            angle=-0.5,
            tip_length=0.2
        )
        
        # Show arrow and explanation text
        self.play(
            Create(arrow),
            Write(explanation_text),
            run_time=1.8
        )
        
        self.wait(2)

        # Add the notation explanation at the bottom
        notation_text = MathTex(
            r'\text{Sometimes denoted } \underline{A \subset B}\text{, sometimes } \underline{A \subsetneq B}',
            font_size=36,
            color="#505050"
        )
        
        # Position at the bottom
        notation_text.to_edge(DOWN, buff=1.0)
        notation_text.to_edge(LEFT, buff=0.5)
        
        # Show the notation text
        self.play(Write(notation_text), run_time=2)
        
        # Hold the final scene
        self.wait(3)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                proper_subset_text, new_circle_A, new_circle_B, new_label_A, new_label_B,
                explanation_text, arrow, notation_text
            )),
            run_time=1
        )
        self.wait(0.5)
    
    def show_transitivity(self):
        """Show subset transitivity property with visual and real-world examples"""
        # Transitivity theorem text at the top
        transitivity_text = MathTex(
            r'\text{If } A \subseteq B \text{ and } B \subseteq C \text{ then } A \subseteq C',
            font_size=44,
            color="#505050"
        )
        transitivity_text.to_edge(UP, buff=1.0)
        transitivity_text.to_edge(LEFT, buff=0.5)
        
        # Show theorem text
        self.play(Write(transitivity_text), run_time=2)
        self.wait(1)
        
        # Define the center position (moved down)
        center_position = DOWN * 0.8
        
        # Create circle C (largest, outermost) - positioned first to establish base
        circle_C = Circle(
            radius=2.2,
            color="#CC0000",  # Red color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_C.move_to(center_position)
        
        # Create circle B (medium, inside C, bottom-left)
        circle_B = Circle(
            radius=1.4,
            color="#008000",  # Green color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_B.move_to(center_position + LEFT * 0.6 + DOWN * 0.4)
        
        # Create circle A (smallest, inside B, bottom-left)
        circle_A = Circle(
            radius=0.8,
            color="#00396B",  # Blue color
            stroke_width=4.0,
            fill_opacity=0
        )
        circle_A.move_to(circle_B.get_center() + LEFT * 0.3 + DOWN * 0.3)
        
        # Create labels with efficient positioning
        label_A = MarkupText(
            '<b><i>A</i></b>',
            color="#00396B",
            font_size=28,
            font="sans-serif"
        )
        label_A.move_to(circle_A.get_center())
        
        label_B = MarkupText(
            '<b><i>B</i></b>',
            color="#008000",
            font_size=32,
            font="sans-serif"
        )
        label_B.move_to(circle_B.get_center() + UP * 1.0 + RIGHT * 0.4)
        
        label_C = MarkupText(
            '<b><i>C</i></b>',
            color="#CC0000",
            font_size=36,
            font="sans-serif"
        )
        label_C.move_to(circle_C.get_center() + UP * 1.8 + RIGHT * 0.5)
        
        # Show circle A and label A
        self.play(
            Create(circle_A),
            Write(label_A),
            run_time=1.5
        )
        self.wait(1.5)
        
        # Show circle B and label B
        self.play(
            Create(circle_B),
            Write(label_B),
            run_time=1.5
        )
        self.wait(1.5)
        
        # Show circle C and label C
        self.play(
            Create(circle_C),
            Write(label_C),
            run_time=1.5
        )
        
        # Hold the final scene
        self.wait(2)

        # Remove everything from the screen with transition
        self.play(
            FadeOut(VGroup(transitivity_text, circle_A, circle_B, circle_C, label_A, label_B, label_C)),
            run_time=0.8
        )
        self.wait(0.5)
        
        # Center position for the nested sets
        center = ORIGIN
        
        # Create "Odd Numbers" text first (blue)
        odd_numbers_text = MarkupText(
            '<b><i>Odd\nNumbers</i></b>',
            color="#00396B",  # Blue color
            font_size=36,
            font="sans-serif"
        )
        odd_numbers_text.move_to(center)
        
        # Show "Odd Numbers" text
        self.play(Write(odd_numbers_text), run_time=1.5)
        self.wait(1)
        
        # Create blue ellipse that fits around "Odd Numbers" text
        odd_ellipse = Ellipse(
            width=odd_numbers_text.width + 1.0,  # Text width + padding
            height=odd_numbers_text.height + 0.8,  # Text height + padding
            color="#00396B",
            stroke_width=4.0,
            fill_opacity=0
        )
        odd_ellipse.move_to(center)
        
        # Show blue ellipse
        self.play(Create(odd_ellipse), run_time=1.5)
        self.wait(1)
        
        # Create "Integers" text (green)
        integers_text = MarkupText(
            '<b><i>Integers</i></b>',
            color="#008000",  # Green color
            font_size=36,
            font="sans-serif"
        )
        integers_text.move_to(center + UP * 1.3)
        
        # Show "Integers" text
        self.play(Write(integers_text), run_time=1.5)
        self.wait(1)
        
        # Create green ellipse that encompasses both odd ellipse and integers text
        # Calculate bounding box of existing content
        existing_group = VGroup(odd_ellipse, integers_text)
        integers_ellipse = Ellipse(
            width=existing_group.width + 1.5,  # Group width + padding
            height=existing_group.height + 1.0,  # Group height + padding
            color="#008000",
            stroke_width=4.0,
            fill_opacity=0
        )
        integers_ellipse.move_to(existing_group.get_center())
        
        # Show green ellipse
        self.play(Create(integers_ellipse), run_time=1.5)
        self.wait(1)
        
        # Create "Rational Numbers" text (red)
        rational_text = MarkupText(
            '<b><i>Rational Numbers</i></b>',
            color="#CC0000",  # Red color
            font_size=36,
            font="sans-serif"
        )
        rational_text.move_to(center + UP * 2.5)
        
        # Show "Rational Numbers" text
        self.play(Write(rational_text), run_time=1.5)
        self.wait(1)
        
        # Create red ellipse that encompasses everything
        all_content = VGroup(integers_ellipse, rational_text)
        rational_ellipse = Ellipse(
            width=all_content.width + 2.0,  # All content width + padding
            height=all_content.height + 1.2,  # All content height + padding
            color="#CC0000",
            stroke_width=4.0,
            fill_opacity=0
        )
        rational_ellipse.move_to(all_content.get_center())
        
        # Show red ellipse
        self.play(Create(rational_ellipse), run_time=1.5)
        
        # Hold the final scene
        self.wait(4)