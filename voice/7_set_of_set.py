from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover(VoiceoverScene):
    def construct(self):
        """Main method that orchestrates the entire Sets of Sets video with voiceover"""
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
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
        self.play(Create(underline), run_time=1)
        
        # Clear title before moving to next section
        self.play(FadeOut(VGroup(title, underline)), run_time=1)
        self.wait(1)
    
    def show_sets_example(self):
        """Show example of sets containing sets as elements"""
        with self.voiceover(text="The elements of a set may be sets themselves. If we have this set A, then the set containing zero is an element of A, but not zero on its own, since the elements of A are all sets.") as tracker:
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
            
            # Set definition
            set_definition = MathTex(
                r'A = \{ \{0\}, \{0, 1\}, \{0, 1, 2\} \}',
                font_size=48,
                color="#505050"
            )
            set_definition.move_to(UP * 1.2)
            
            # Show set definition
            self.play(Write(set_definition), run_time=2)
            
            # Left column statements
            statement1 = MathTex(
                r'\{0\} \in A',
                font_size=36,
                color="#505050"
            )
            statement1.move_to(LEFT * 2.5 + UP * 0.2)
            
            statement2 = MathTex(
                r'0 \notin A',
                font_size=36,
                color="#505050"
            )
            statement2.move_to(RIGHT * 2.5 + UP * 0.2)
            
            # Show first two statements
            self.play(Write(statement1), run_time=1.5)
            self.play(Write(statement2), run_time=1.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 7.0)

        with self.voiceover(text="Here it becomes tricky to keep track of what's an element and what's a subset. The set containing zero isn't a subset of A, it's an element as we've seen already. In fact, the set containing the set containing zero is a subset of A, and it's important to really think about the difference in cases like this.") as tracker:
            statement3 = MathTex(
                r'\{0\} \not\subset A',
                font_size=36,
                color="#505050"
            )
            statement3.move_to(LEFT * 2.5 + DOWN * 0.8)
            
            statement4 = MathTex(
                r'\{ \{0\} \} \subseteq A',
                font_size=36,
                color="#505050"
            )
            statement4.move_to(RIGHT * 2.5 + DOWN * 0.8)
            
            # Create check marks using built-in Manim symbols
            check1 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
            check1.next_to(statement1, RIGHT, buff=0.5)
            
            check2 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
            check2.next_to(statement2, RIGHT, buff=0.5)
            
            check3 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
            check3.next_to(statement3, RIGHT, buff=0.5)
            
            check4 = Text("✓", font_size=30, color=GREEN, weight=BOLD)
            check4.next_to(statement4, RIGHT, buff=0.5)
            
            # Show remaining statements and all checks
            self.play(Write(statement3), run_time=1.5)
            self.play(Write(statement4), run_time=1.5)
            self.play(FadeIn(VGroup(check1, check2, check3, check4)), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                statement, set_definition, statement1, statement2, statement3, statement4,
                check1, check2, check3, check4
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_power_set_definition(self):
        """Show power set definition and example"""
        with self.voiceover(text="The power set is a common thing to encounter and it contains all subsets of a given set. So let A be a set. The power set of A, P brackets A, contains all sets X such that X is a subset of A.") as tracker:
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
            
            # Power set definition - CENTERED and split for precise targeting
            power_set_definition = MathTex(
                r'P(A)', r'=', r'\{ X \mid X \subseteq A \}',
                font_size=48,
                color="#505050"
            )
            power_set_definition.move_to(UP * 0.3)
            
            # Show definition
            self.play(Write(power_set_definition), run_time=2)
            
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
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 8.0)
        
        with self.voiceover(text="So for A equals the set containing zero and one, the power set of A would contain the empty set, A itself, the set containing zero, and the set containing one.") as tracker:
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
            
            # Power set result - CENTERED
            power_set_result = MathTex(
                r'P(A) = \{ \varnothing, \{ 0, 1 \}, \{0\}, \{1\} \}',
                font_size=48,
                color="#505050"
            )
            power_set_result.move_to(DOWN * 1.8)
            
            # Show result
            self.play(Write(power_set_result), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 4.0)
        
        # Clear everything before next section
        self.play(
            FadeOut(VGroup(
                title, let_statement, power_set_definition, power_set_label, 
                arrow, example_statement, power_set_result
            )),
            run_time=1
        )
        self.wait(1)
    
    def show_indexed_families(self):
        """Show indexed families of sets"""
        with self.voiceover(text="We also have what are called indexed families of sets. Essentially each element, which is a set itself, is indexed by a number and usually written as a subscript. So A being A sub i for i in the set one, two, three is saying that A contains three sets: A one, A two, and A three.") as tracker:
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
            
            # General formula - CENTERED
            general_formula = MathTex(
                r'A = \{ A_i \mid i \in I \}',
                font_size=48,
                color="#505050"
            )
            general_formula.move_to(UP * 0.8)
            
            # Show general formula
            self.play(Write(general_formula), run_time=2)
            
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
            self.play(Write(double_arrow), run_time=1)
            self.play(Write(equivalent_notation), run_time=2)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 9.0)
        
        with self.voiceover(text="And in some cases it might be easier to read if we package things up like this. If A is the set containing set zero, set zero and one, and set zero, one, and two, we can write this as A one, A two, and A three, where A one is the set containing zero, A two is a set containing zero and one, and A three is the set containing zero, one, and two.") as tracker:
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
            
            # Individual indexed sets - CENTERED
            indexed_sets = MathTex(
                r'A_1 = \{0\} \quad A_2 = \{0, 1\} \quad A_3 = \{0, 1, 2\}',
                font_size=40,
                color="#505050"
            )
            indexed_sets.move_to(DOWN * 2.2)
            
            # Show indexed sets
            self.play(Write(indexed_sets), run_time=2.5)
            
            # Wait for remaining audio
            self.safe_wait(tracker.duration - 5.0)
        
        self.wait(2)