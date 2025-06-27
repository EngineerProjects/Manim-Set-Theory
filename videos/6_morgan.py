from manim import *

class DeMorganLaws(Scene):
    def construct(self):
        """Main method that orchestrates the entire De Morgan's Laws video"""
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_laws_statement()
        self.show_duality_principle()
    
    def show_title(self):
        """Display the main title: De Morgan's Laws"""
        # Create the "De Morgan's Laws" title
        title = Text(
            "De Morgan's Laws",
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
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(title, underline)), run_time=1)
        self.wait(0.5)
    
    def show_laws_statement(self):
        """Show De Morgan's Laws statement with examples"""
        # Title
        title = Text(
            "De Morgan's Laws",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        title.to_edge(UP, buff=1.0)
        
        # Condition statement
        condition = MarkupText(
            '<b><i>If A and B are subsets of the universal set U</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        condition.move_to(UP * 1.5)
        condition.to_edge(LEFT, buff=0.5)
        
        # First De Morgan's Law - CENTERED
        law1 = MathTex(
            r'(A \cup B)^c = A^c \cap B^c',
            font_size=56,
            color="#505050"
        )
        law1.move_to(UP * 0.2)
        
        # Second De Morgan's Law
        law2 = MathTex(
            r'(A \cap B)^c = A^c \cup B^c',
            font_size=56,
            color="#505050"
        )
        law2.move_to(DOWN * 1.2)
        
        # Show all elements
        self.play(Write(title), run_time=2)
        self.play(Write(condition), run_time=2)
        self.play(Write(law1), run_time=2)
        self.play(Write(law2), run_time=2)
        self.wait(2)

        # Clear the condition and second law
        self.play(FadeOut(VGroup(condition, law2)), run_time=1)
        
        # Move law1 to bottom right position
        law1_new_position = law1.copy()
        law1_new_position.set(font_size=44)
        law1_new_position.to_edge(DOWN, buff=1.0)
        self.play(ReplacementTransform(law1, law1_new_position), run_time=1)
        self.wait(0.5)

        # Show first example (animals)
        self._show_animal_example(title, law1_new_position)
        
        # Show second example (mathematical)
        self._show_mathematical_example(title)
    
    def _show_animal_example(self, title, law1_position):
        """Helper method to show the animal example"""
        # Animal example setup - split into two lines
        example_line1 = MarkupText(
            '<b><i>Let U be the set of all animals. Let A be the set</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        example_line2 = MarkupText(
            '<b><i>of Dogs and B be the set of Cats.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )

        example_line1.move_to(UP * 1.8)
        example_line1.to_edge(LEFT, buff=0.5)
        example_line2.next_to(example_line1, DOWN, buff=0.1, aligned_edge=LEFT)

        # Real-world formula - CENTERED
        real_formula = MathTex(
            r'(Dogs \cup Cats)^c = Dogs^c \cap Cats^c',
            font_size=48,
            color="#505050"
        )
        real_formula.move_to(UP * 0.5)

        # Quote explanation - split into two lines
        quote_line1 = MarkupText(
            '<b><i>"Animals that are neither dogs nor cats are not</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        quote_line2 = MarkupText(
            '<b><i>dogs and are not cats"</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        
        quote_line1.move_to(DOWN * 0.6)
        quote_line1.to_edge(LEFT, buff=0.5)
        quote_line2.next_to(quote_line1, DOWN, buff=0.1, aligned_edge=LEFT)

        # Show animal example
        self.play(Write(example_line1), run_time=2)
        self.play(Write(example_line2), run_time=1.5)
        self.wait(1)

        # Show real formula in center
        self.play(Write(real_formula), run_time=2)
        self.wait(1)

        # Add quote
        self.play(Write(quote_line1), run_time=2)
        self.play(Write(quote_line2), run_time=1.5)
        self.wait(3)

        # Clear everything except title for next example
        self.play(
            FadeOut(VGroup(example_line1, example_line2, real_formula, quote_line1, quote_line2, law1_position)),
            run_time=1
        )
        self.wait(0.5)
    
    def _show_mathematical_example(self, title):
        """Helper method to show the mathematical example"""
        # New mathematical example setup - split into two lines
        math_example_line1 = MarkupText(
            '<b><i>Let U be the set ℕ, Let A be the set of prime</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        math_example_line2 = MarkupText(
            '<b><i>numbers and B be the set { x ∈ ℕ | x &lt; 100 }.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )

        math_example_line1.move_to(UP * 1.8)
        math_example_line1.to_edge(LEFT, buff=0.5)
        math_example_line2.next_to(math_example_line1, DOWN, buff=0.1, aligned_edge=LEFT)

        # Second De Morgan's Law - CENTERED
        law2_abstract = MathTex(
            r'(A \cap B)^c = A^c \cup B^c',
            font_size=48,
            color="#505050"
        )
        law2_abstract.move_to(UP * 0.5)

        # Double arrow
        double_arrow = MathTex(
            r'\updownarrow',
            font_size=40,
            color="#505050"
        )
        double_arrow.move_to(ORIGIN)

        # Real-world mathematical formula - CENTERED
        math_real_formula = MathTex(
            r'(Prime \cap <100)^c = Prime^c \cup (<100)^c',
            font_size=48,
            color="#505050"
        )
        math_real_formula.move_to(DOWN * 0.5)

        # Quote explanation - split into three lines
        quote_math_line1 = MarkupText(
            '<b><i>"The set of numbers that are not prime and less than</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        quote_math_line2 = MarkupText(
            '<b><i>100 is the set of numbers that are either not prime or</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        quote_math_line3 = MarkupText(
            '<b><i>greater than 100"</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )

        quote_math_line1.move_to(DOWN * 1.8)
        quote_math_line1.to_edge(LEFT, buff=0.5)
        quote_math_line2.next_to(quote_math_line1, DOWN, buff=0.1, aligned_edge=LEFT)
        quote_math_line3.next_to(quote_math_line2, DOWN, buff=0.1, aligned_edge=LEFT)

        # Show mathematical example
        self.play(Write(math_example_line1), run_time=2)
        self.play(Write(math_example_line2), run_time=1.5)
        self.wait(1)

        # Show abstract law
        self.play(Write(law2_abstract), run_time=2)
        self.wait(1)

        # Show arrow and real formula
        self.play(Write(double_arrow), run_time=1)
        self.play(Write(math_real_formula), run_time=2)
        self.wait(1)

        # Add quote explanation
        self.play(Write(quote_math_line1), run_time=2)
        self.play(Write(quote_math_line2), run_time=2)
        self.play(Write(quote_math_line3), run_time=1.5)
        self.wait(3)

        # Clear everything except title before next section
        self.play(
            FadeOut(VGroup(
                math_example_line1, math_example_line2, law2_abstract, double_arrow,
                math_real_formula, quote_math_line1, quote_math_line2, quote_math_line3
            )),
            run_time=1
        )
        
        # Clear title as well
        self.play(FadeOut(title), run_time=1)
        self.wait(0.5)
    
    def show_duality_principle(self):
        """Show De Morgan's Duality Principle"""
        # Title
        title = Text(
            "De Morgan's Duality Principle",
            font_size=50,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        title.to_edge(UP, buff=1.0)
        
        # Show title
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Vertical dividing line
        vertical_line = Line(
            start=UP * 2.5,
            end=DOWN * 0.7,
            color="#505050",
            stroke_width=3
        )
        vertical_line.move_to(ORIGIN)
        
        # Show vertical line first
        self.play(Create(vertical_line), run_time=1)
        self.wait(1)
        
        # Left column formulas
        distributive_left = MathTex(
            r'\mathbf{A \cap (B \cup C) = (A \cap B) \cup (A \cap C)}',
            font_size=32,
            color="#505050"
        )
        distributive_left.move_to(LEFT * 3 + UP * 1.2)
        
        demorgan_left = MathTex(
            r'\mathbf{(A \cup B)^c = A^c \cap B^c}',
            font_size=32,
            color="#505050"
        )
        demorgan_left.move_to(LEFT * 3 + DOWN * 0.2)
        
        # Right column formulas
        distributive_right = MathTex(
            r'\mathbf{A \cup (B \cap C) = (A \cup B) \cap (A \cup C)}',
            font_size=32,
            color="#505050"
        )
        distributive_right.move_to(RIGHT * 3 + UP * 1.2)
        
        demorgan_right = MathTex(
            r'\mathbf{(A \cap B)^c = A^c \cup B^c}',
            font_size=32,
            color="#505050"
        )
        demorgan_right.move_to(RIGHT * 3 + DOWN * 0.2)
        
        # Show formulas one by one
        self.play(Write(distributive_left), run_time=2)
        self.wait(1)
        self.play(Write(distributive_right), run_time=2)
        self.wait(1)
        self.play(Write(demorgan_left), run_time=2)
        self.wait(1)
        self.play(Write(demorgan_right), run_time=2)
        self.wait(1)
        
        # Explanatory text at bottom - split into three lines
        explanation_line1 = MarkupText(
            '<b><i>Given any set-theoretic identity involving ∪ and ∩,</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        explanation_line2 = MarkupText(
            '<b><i>if ∪ and ∩ are interchanged throughout, then the</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        explanation_line3 = MarkupText(
            '<b><i>result will be another valid identity.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        
        explanation_line1.move_to(DOWN * 2.2)
        explanation_line1.to_edge(LEFT, buff=0.5)
        explanation_line2.next_to(explanation_line1, DOWN, buff=0.1, aligned_edge=LEFT)
        explanation_line3.next_to(explanation_line2, DOWN, buff=0.1, aligned_edge=LEFT)
        
        # Show explanatory text
        self.play(Write(explanation_line1), run_time=2)
        self.wait(1)
        self.play(Write(explanation_line2), run_time=2)
        self.wait(1)
        self.play(Write(explanation_line3), run_time=2)
        self.wait(3)