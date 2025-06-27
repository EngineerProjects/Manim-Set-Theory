from manim import *

class SetsOfSetsPowerSetsIndexedFamilies(Scene):
    def construct(self):
        """Main method that orchestrates the entire video"""
        # Set consistent background color for entire video
        self.camera.background_color = "#F0F0F0"
        
        # Execute all sections in sequence
        self.show_title()
        self.show_sets_example()
        self.show_power_set_definition()
        self.show_indexed_families()
    
    def show_title(self):
        """Display the main title: Sets of Sets"""
        # Create the "Sets of Sets" title
        title = Text(
            "Sets of Sets",
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
    
    def show_sets_example(self):
        """Show example of sets containing sets as elements"""
        # Statement at the top
        statement = MarkupText(
            '<b><i>The elements of a set may be sets themselves:</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        statement.to_edge(UP, buff=1.0)
        statement.to_edge(LEFT, buff=0.5)
        
        # Show statement
        self.play(Write(statement), run_time=2)
        self.wait(1)
        
        # Set definition
        set_definition = MathTex(
            r'A = \{ \{0\}, \{0, 1\}, \{0, 1, 2\} \}',
            font_size=48,
            color="#505050"
        )
        set_definition.move_to(UP * 1.2)
        
        # Show set definition
        self.play(Write(set_definition), run_time=2)
        self.wait(1)
        
        # Left column statements
        statement1 = MathTex(
            r'\{0\} \in A',
            font_size=36,
            color="#505050"
        )
        statement1.move_to(LEFT * 2.5 + UP * 0.2)
        
        statement3 = MathTex(
            r'\{0\} \not\subset A',
            font_size=36,
            color="#505050"
        )
        statement3.move_to(LEFT * 2.5 + DOWN * 0.8)
        
        # Right column statements
        statement2 = MathTex(
            r'0 \notin A',
            font_size=36,
            color="#505050"
        )
        statement2.move_to(RIGHT * 2.5 + UP * 0.2)
        
        statement4 = MathTex(
            r'\{ \{0\} \} \subseteq A',
            font_size=36,
            color="#505050"
        )
        statement4.move_to(RIGHT * 2.5 + DOWN * 0.8)
        
        # Create check marks using built-in Manim symbols instead of SVG
        check1 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
        check1.next_to(statement1, RIGHT, buff=0.5)
        
        check2 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
        check2.next_to(statement2, RIGHT, buff=0.5)
        
        check3 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
        check3.next_to(statement3, RIGHT, buff=0.5)
        
        check4 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
        check4.next_to(statement4, RIGHT, buff=0.5)
        
        # Show statements and checks one by one
        self.play(Write(statement1), run_time=1.5)
        self.play(FadeIn(check1), run_time=1)
        self.wait(1)
        
        self.play(Write(statement2), run_time=1.5)
        self.play(FadeIn(check2), run_time=1)
        self.wait(1)
        
        self.play(Write(statement3), run_time=1.5)
        self.play(FadeIn(check3), run_time=1)
        self.wait(1)
        
        self.play(Write(statement4), run_time=1.5)
        self.play(FadeIn(check4), run_time=1)
        self.wait(3)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                statement, set_definition, statement1, statement2, statement3, statement4,
                check1, check2, check3, check4
            )),
            run_time=1
        )
        self.wait(0.5)
    
    def show_power_set_definition(self):
        """Show power set definition and example"""
        # Title at the top
        title = MarkupText(
            '<b><i>The power set contains all subsets of a given set.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        title.to_edge(UP, buff=1.0)
        title.to_edge(LEFT, buff=0.5)
        
        # Show title
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # "Let A be a set."
        let_statement = MarkupText(
            '<b><i>Let A be a set.</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        let_statement.move_to(UP * 1.2)
        let_statement.to_edge(LEFT, buff=0.5)
        
        # Show let statement
        self.play(Write(let_statement), run_time=1.5)
        self.wait(1)
        
        # Power set definition - CENTERED and split for precise targeting
        power_set_definition = MathTex(
            r'P(A)', r'=', r'\{ X \mid X \subseteq A \}',
            font_size=48,
            color="#505050"
        )
        power_set_definition.move_to(UP * 0.3)
        
        # Show definition
        self.play(Write(power_set_definition), run_time=2)
        self.wait(1)
        
        # "Power set of A" label
        power_set_label = MarkupText(
            '<b><i>"Power set of A"</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        power_set_label.move_to(RIGHT * 2.2 + UP * 1.5)
         
        # Arrow pointing specifically to P(A) part (index 0)
        arrow = CurvedArrow(
            start_point=power_set_label.get_bottom() + UP * 0.1 + LEFT * 1.9,
            end_point=power_set_definition[0].get_top() + UP * 0.1,
            color="#505050",
            angle=0.4,
            tip_length=0.15,
            stroke_width=2
        )
        
        # Show arrow and label
        self.play(Create(arrow), run_time=1)
        self.play(Write(power_set_label), run_time=1.5)
        self.wait(1)
        
        # Example setup
        example_statement = MarkupText(
            '<b><i>For A = { 0, 1 },</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        example_statement.move_to(DOWN * 0.8)
        example_statement.to_edge(LEFT, buff=0.5)
        
        # Show example statement
        self.play(Write(example_statement), run_time=1.5)
        self.wait(1)
        
        # Power set result - CENTERED
        power_set_result = MathTex(
            r'P(A) = \{ \varnothing, \{ 0, 1 \}, \{0\}, \{1\} \}',
            font_size=48,
            color="#505050"
        )
        power_set_result.move_to(DOWN * 1.8)
        
        # Show result
        self.play(Write(power_set_result), run_time=2.5)
        self.wait(3)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, let_statement, power_set_definition, power_set_label, 
                arrow, example_statement, power_set_result
            )),
            run_time=1
        )
        self.wait(0.5)
    
    def show_indexed_families(self):
        """Show indexed families of sets"""
        # Title
        title = Text(
            "Indexed families of sets",
            font_size=40,
            color=BLACK,
            font="sans-serif",
            slant=ITALIC,
            weight=LIGHT
        )
        title.to_edge(UP, buff=1.0)
        
        # Show title
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Subtitle
        subtitle = MarkupText(
            '<b><i>Each element is indexed by a number</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        subtitle.move_to(UP * 1.8)
        subtitle.to_edge(LEFT, buff=0.5)
        
        # Show subtitle
        self.play(Write(subtitle), run_time=2)
        self.wait(1)
        
        # General formula - CENTERED
        general_formula = MathTex(
            r'A = \{ A_i \mid i \in I \}',
            font_size=48,
            color="#505050"
        )
        general_formula.move_to(UP * 0.8)
        
        # Show general formula
        self.play(Write(general_formula), run_time=2)
        self.wait(1)
        
        # Example with specific index - CENTERED
        specific_example = MathTex(
            r'A = \{A_i \mid i \in \{1, 2, 3\} \}',
            font_size=40,
            color="#505050"
        )
        specific_example.move_to(LEFT * 2.5 + DOWN * 0.2)
        
        # Double arrow
        double_arrow = MathTex(
            r'\leftrightarrow',
            font_size=40,
            color="#505050"
        )
        double_arrow.move_to(ORIGIN + DOWN * 0.2)
        
        # Equivalent notation - CENTERED
        equivalent_notation = MathTex(
            r'A = \{A_1, A_2, A_3\}',
            font_size=40,
            color="#505050"
        )
        equivalent_notation.move_to(RIGHT * 2.5 + DOWN * 0.2)
        
        # Show example with arrow
        self.play(Write(specific_example), run_time=2)
        self.wait(1)
        self.play(Write(double_arrow), run_time=1)
        self.play(Write(equivalent_notation), run_time=2)
        self.wait(1)
        
        # Example text
        example_text = MarkupText(
            '<b><i>Let A = { {0}, {0, 1}, {0, 1, 2} }, we can write this as</i></b>',
            color="#505050",
            font_size=32,
            font="sans-serif"
        )
        example_text.move_to(DOWN * 1.2)
        example_text.to_edge(LEFT, buff=0.5)
        
        # Show example text
        self.play(Write(example_text), run_time=2.5)
        self.wait(1)
        
        # Individual indexed sets - CENTERED
        indexed_sets = MathTex(
            r'A_1 = \{0\} \quad A_2 = \{0, 1\} \quad A_3 = \{0, 1, 2\}',
            font_size=40,
            color="#505050"
        )
        indexed_sets.move_to(DOWN * 2.2)
        
        # Show indexed sets
        self.play(Write(indexed_sets), run_time=2.5)
        self.wait(3)