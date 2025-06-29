from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BasicsWithVoiceover(VoiceoverScene):
    def construct(self):
        # Set up TTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"), create_subcaption=False)
        
        # Scene 1: Set Theory Introduction
        self.set_theory_intro()
        self.clear()
        
        # Scene 2: Set Definition
        self.set_definition()
        self.clear()
        
        # Scene 3: Set of Triangles
        self.set_of_triangles()
        self.clear()
        
        # Scene 4: Set Notation
        self.set_notation()
        self.clear()
        
        # Scene 5: Element Of Symbol
        self.element_of_symbol()
        self.clear()
        
        # Scene 6: Set Builder Notation
        self.set_builder_notation()
        self.clear()
        
        # Scene 7: Number Sets Declaration
        self.number_sets_declaration()
        self.clear()
        
        # Scene 8: Set Equality
        self.set_equality()
        self.clear()
        
        # Scene 9: Order Doesn't Matter
        self.order_doesnt_matter()
        self.clear()
        
        # Scene 10: Repeated Elements Don't Matter
        self.repeated_elements_dont_matter()
        self.clear()
        
        # Scene 11: Set Cardinality
        self.set_cardinality()

    def set_theory_intro(self):
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
        underline.shift(DOWN * 0.2)
        
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
        
        author_name.to_corner(DR, buff=0.6)
        youtube_logo.next_to(author_name, LEFT, buff=0.2)
        
        # Create title and underline with no voiceover (just visual intro)
        self.play(AddTextLetterByLetter(main_title), run_time=2)
        self.play(Create(underline), run_time=1)
        
        self.play(
            FadeIn(youtube_logo),
            Write(author_name),
            run_time=1.5
        )
        
        # Animate name reduction with quick timing
        initial_text_bottom = author_name.get_bottom()
        final_logo_pos = author_name.get_right() + LEFT * (youtube_logo.width/2)
        
        for i in range(len(full_name)):
            if i < len(full_name) - 1:
                new_text = Text(
                    full_name[i+1:],
                    font_size=20,
                    color=BLACK,
                    font="DejaVu Serif",
                    slant=ITALIC
                )
                
                new_text.align_to(author_name, RIGHT)
                new_text.align_to(author_name, DOWN)
                
                logo_pos = new_text.get_left() + LEFT * (youtube_logo.width/2 + 0.2)
                
                self.play(
                    Transform(author_name, new_text),
                    youtube_logo.animate.move_to(logo_pos).align_to(new_text, DOWN),
                    run_time=0.06
                )
        
        self.play(
            FadeOut(author_name),
            youtube_logo.animate.move_to(final_logo_pos).align_to(initial_text_bottom, DOWN),
            run_time=0.1
        )
        
        self.wait(1)  # Brief pause before next scene

    def set_definition(self):
        self.camera.background_color = "#F0F0F0"
        
        definition = Text(
            "A set is a collection of objects (elements).",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        definition.to_edge(UP, buff=2.0)
        definition.shift(LEFT * 1)
        
        circle = Circle(
            radius=2.5,  
            color="#00396B",  
            stroke_width=3.0,
            fill_opacity=0
        )
        circle.next_to(definition, DOWN, buff=0.5)

        group = VGroup(definition, circle)
        group.shift(UP * 1.0)

        car = SVGMobject("images/car-svgrepo-com.svg")
        car.scale(0.3)
        car.move_to(circle.get_center() + LEFT * 1.5)
        
        atom = SVGMobject("images/atom-symbol-svgrepo-com.svg")
        atom.set_color(BLACK)
        atom.set_fill(BLACK, 1)
        atom.scale(0.4)
        atom.move_to(circle.get_center() + DOWN * 1.5)
        
        equation = MathTex(r"\mathbf{1 + 1 = 2}", color=BLACK)
        equation.scale(0.8)
        equation.move_to(circle.get_center() + RIGHT * 1.0)
        
        with self.voiceover(text="A set is a collection of objects we call elements.") as tracker:
            # Text should match speech pace
            self.play(Write(definition), run_time=2.0)
            # Circle at natural speed
            self.play(Create(circle), run_time=1.2)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 3.2
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="That could mean physical objects") as tracker:
            # Car appears exactly when "physical objects" is mentioned
            self.play(FadeIn(car), run_time=tracker.duration)
        
        with self.voiceover(text="thoughts, ideas and concepts") as tracker:
            # Atom appears exactly when "thoughts, ideas and concepts" is mentioned
            self.play(FadeIn(atom), run_time=tracker.duration)
        
        with self.voiceover(text="including mathematical objects which will of course be the main focus for us.") as tracker:
            # Equation appears exactly when "mathematical objects" is mentioned
            self.play(Write(equation), run_time=tracker.duration)
        
        with self.voiceover(text="Possibly more importantly, a set is a way of packaging up objects which share similar properties in a meaningful way.", create_subcaption=False) as tracker:
            self.wait(tracker.duration)

    def set_of_triangles(self):
        self.camera.background_color = "#F0F0F0"
        
        circle = Circle(
            radius=2,  
            color="#00396B",  
            stroke_width=3.0,
            fill_opacity=0
        )
        circle.shift(RIGHT * 1)
        
        set_text = Text(
            "The set of all\ntriangles",
            font_size=36,
            color=BLACK,
            font="sans-serif",
            weight=BOLD
        )
        set_text.move_to(LEFT * 4.5 + UP * 2)
        
        arrow = CurvedArrow(
            start_point=set_text.get_right() + RIGHT * 0.5 + UP * 0.1,
            end_point=circle.get_left() + UP * 0.8,
            color=BLACK,
            angle=-0.7,
            tip_length=0.2 
        )
        
        small_triangle = Triangle(color="#008000", stroke_width=4.0)
        small_triangle.scale(0.4)
        small_triangle.move_to(circle.get_center() + UP * 0.7) 
        
        right_triangle = Polygon(
            [0, 0, 0],
            [1.5, 0, 0],
            [0, 0.8, 0],
            color="#008000", 
            stroke_width=4.0
        )
        right_triangle.move_to(circle.get_center() + DOWN * 0.4)
        
        pentagon = RegularPolygon(5, color="#FF0000", stroke_width=4.0)
        pentagon.scale(0.7) 
        pentagon.move_to(RIGHT * 5 + UP * 1.2)
        
        sides_text = Text(
            "3 sides",
            font_size=30,
            color="#666666",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        sides_text.move_to(LEFT * 4.5 + DOWN * 2.5)
        
        check = SVGMobject("images/check.svg")
        check.set_color("#008000")
        check.scale(0.3)
        check.next_to(sides_text, RIGHT, buff=0.2)
        
        angles_text = Text(
            "sum of internal\nangles is 360°",
            font_size=30,
            color="#666666",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        angles_text.move_to(RIGHT * 4 + DOWN * 2.5)
        
        x_mark = SVGMobject("images/cross.svg")
        x_mark.set_color("#FF0000")
        x_mark.scale(0.3)
        x_mark.next_to(angles_text, RIGHT, buff=0.2)

        with self.voiceover(text="Consider the set of triangles.") as tracker:
            # Visual elements at natural speed
            self.play(Create(circle), run_time=1.0)
            self.play(Write(set_text), run_time=1.2)
            self.play(Create(arrow), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 3.0
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="We can unambiguously state whether something is or isn't in this set.", create_subcaption=False) as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="This is in") as tracker:
            # Triangle at normal speed
            self.play(Create(small_triangle), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 0.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="so is this") as tracker:
            # Triangle at normal speed
            self.play(Create(right_triangle), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 0.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="but this shape isn't. It's not a triangle.") as tracker:
            # Pentagon at normal speed
            self.play(Create(pentagon), run_time=1.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.0
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="This lack of ambiguity in what is or what isn't in a set is foundational to set theory.", create_subcaption=False) as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="We can also make claims about the set and assess again without ambiguity whether they're true or false.", create_subcaption=False) as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="It's true that an element of the set of triangles has three sides.") as tracker:
            # Text and check mark at reasonable speed
            self.play(Write(sides_text), run_time=1.5)
            self.play(FadeIn(check), run_time=0.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.0
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="But it's not true that the sum of the internal angles is 360 degrees.") as tracker:
            # Text and X mark at reasonable speed
            self.play(Write(angles_text), run_time=1.5)
            self.play(FadeIn(x_mark), run_time=0.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.0
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def set_notation(self):
        self.camera.background_color = "#F0F0F0"
        
        explanation1 = Text(
            "A set containing the numbers 1, 2, 3\nwould be written",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        explanation1.to_edge(UP, buff=1.0)
        explanation1.to_edge(LEFT, buff=2.0)
        
        set_notation = MathTex(
            r"\{ 1, 2, 3 \}",
            font_size=48,
            color=BLACK
        )
        set_notation.next_to(explanation1, DOWN, buff=1.0)
        
        explanation2 = Text(
            "We can also name the set.",
            font_size=36,
            color="#505050",
            font="sans-serif",
            slant=ITALIC,
            weight=BOLD
        )
        explanation2.next_to(set_notation, DOWN, buff=1.5)
        explanation2.to_edge(LEFT, buff=2.0)
        
        named_set = MathTex(
            r"A = \{ 1, 2, 3 \}",
            font_size=48,
            color=BLACK
        )
        named_set.next_to(explanation2, DOWN, buff=1.0)
        
        with self.voiceover(text="A set containing the numbers 1, 2, and 3 would be written") as tracker:
            # Text should match speech pace
            self.play(Write(explanation1), run_time=tracker.duration)
        
        with self.voiceover(text="like this with curly brackets and the elements separated by commas.") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_notation), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="We can name the set.") as tracker:
            # Text at reasonable speed
            self.play(Write(explanation2), run_time=1.2)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.2
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="In this case if we say A is equal to the set 1, 2, and 3, we can just refer to the set as A, which is much easier than saying the set containing 1, 2, and 3 again and again.") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(named_set), run_time=1.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def element_of_symbol(self):
        self.camera.background_color = "#F0F0F0"
        
        line1 = MarkupText(
            '<b><i>To express symbolically that an element</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        line2 = MarkupText(
            '<b><i>belongs to a set we use </i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        symbol_part = MarkupText(
            '<b><i> ∈</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        line1.to_edge(UP, buff=1.0)
        line1.to_edge(LEFT, buff=0.5)
        
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.1)
        symbol_part.next_to(line2, RIGHT, buff=0.2)
        
        full_text = VGroup(line1, line2, symbol_part)
        
        example_text = MarkupText(
            '<b><i>For example:</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        example_text.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.8)
        
        set_definition = MarkupText(
            '<b><i>If A = {1, 2, 3},</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        set_definition.next_to(example_text, DOWN, aligned_edge=LEFT, buff=0.5)
        set_definition.shift(RIGHT * 1.5)
        
        membership_math = MarkupText(
            '<b><i>then 1 ∈ A, 2 ∈ A</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        membership_math.next_to(set_definition, DOWN, aligned_edge=LEFT, buff=0.5)
        
        membership_english = MarkupText(
            '<b><i>"1 in A, 2 in A"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        membership_english.move_to(RIGHT * 3 + membership_math.get_center()[1] * UP)
        
        non_membership_math = MarkupText(
            '<b><i>but 4 ∉ A</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        non_membership_math.next_to(membership_math, DOWN, aligned_edge=LEFT, buff=0.5)
        
        non_membership_english = MarkupText(
            '<b><i>"4 not in A"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        non_membership_english.move_to(RIGHT * 3 + non_membership_math.get_center()[1] * UP)
        
        # Dimmed versions for the effect
        dimmed_line1 = line1.copy().set_opacity(0.15)
        dimmed_line2 = line2.copy().set_opacity(0.15)
        
        with self.voiceover(text="To express symbolically that an element belongs to a set we use this symbol.") as tracker:
            # Text should match speech pace
            self.play(Write(full_text), run_time=tracker.duration)
        
        with self.voiceover(text="For example") as tracker:
            # Dimming effect and example text at reasonable speed
            self.play(
                ReplacementTransform(line1, dimmed_line1),
                ReplacementTransform(line2, dimmed_line2),
                run_time=0.8
            )
            self.play(Write(example_text), run_time=1.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="if A is the set containing 1, 2, and 3") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_definition), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="then 1 is in A and 2 is in A") as tracker:
            # Mathematical expressions at reasonable speed
            self.play(Write(membership_math), run_time=1.2)
            self.play(Write(membership_english), run_time=1.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.2
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="but 4 is not in A. And we use the symbol for in but with a line through it to denote not in.") as tracker:
            # Mathematical expressions at reasonable speed
            self.play(Write(non_membership_math), run_time=1.2)
            self.play(Write(non_membership_english), run_time=1.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.2
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def set_builder_notation(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        underlined_text = MarkupText(
            '<b><i><u>set builder notation</u>.</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        intro_line3.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.1)
        underlined_text.next_to(intro_line3, RIGHT, buff=0.1)
        
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
        
        example_intro.next_to(intro_line3, DOWN, aligned_edge=LEFT, buff=0.8)
        example_intro2.next_to(example_intro, DOWN, aligned_edge=LEFT, buff=0.1)
        
        math_notation = MarkupText(
            '<b><i>P = {p | p is a prime}</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        math_notation.next_to(example_intro2, DOWN, buff=0.8)
        math_notation.shift(RIGHT * 1.5)
        
        english_explanation = MarkupText(
            '<b><i>"p such that p is a prime"</i></b>',
            color="#505050",
            font_size=36,
            font="sans-serif"
        )
        english_explanation.next_to(math_notation, DOWN, buff=0.6)
        english_explanation.shift(RIGHT * 0.5)
        
        predicate_label = MarkupText(
            '<b><i>Predicate</i></b>',
            color="#1853A2",
            font_size=36,
            font="sans-serif"
        )
        predicate_label.move_to(math_notation.get_right() + RIGHT * 1.5 + UP * 1.2)
        
        arrow = CurvedArrow(
            start_point=predicate_label.get_bottom() + DOWN * 0.1 + LEFT * 0.3,
            end_point=math_notation.get_center() + RIGHT * 1.2, 
            color="#1853A2",  
            angle=0.6,  
            tip_length=0.1
        )
        
        with self.voiceover(text="In most cases we don't write out all the elements in a set but we'll write a shorthand description using something called set builder notation.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(intro_line1, intro_line2, intro_line3, underlined_text)), run_time=tracker.duration)
        
        with self.voiceover(text="For example the set of prime numbers could be written as") as tracker:
            # Introductory text at reasonable speed
            self.play(Write(VGroup(example_intro, example_intro2)), run_time=1.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="capital P is the set of little p such that little p is prime") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(math_notation), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="Here the little p is a variable which must satisfy some criterion we call the predicate") as tracker:
            # English explanation and predicate label at reasonable speed
            self.play(Write(english_explanation), run_time=1.2)
            self.play(
                Create(arrow),
                Write(predicate_label),
                run_time=1.0
            )
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.2
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="since its belonging to the set is predicated on this criterion. In this case the predicate is being a prime number. Also notice we have a shorthand for the phrase such that which is this vertical line.", create_subcaption=False) as tracker:
            self.wait(tracker.duration)

    def number_sets_declaration(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        intro_line3.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.1)
        
        natural_set = MathTex(
            r'\{p \in \mathbb{N} \mid p < 5\}',
            font_size=42,
            color="#505050"
        )
        
        not_equal = MathTex(
            r'\neq',
            font_size=42,
            color="#505050"
        )
        
        real_set = MathTex(
            r'\{r \in \mathbb{R} \mid r < 5\}',
            font_size=42,
            color="#505050"
        )
        
        math_group = VGroup(natural_set, not_equal, real_set)
        math_group.arrange(RIGHT, buff=0.3)
        math_group.move_to(ORIGIN)
        
        with self.voiceover(text="It's good practice when dealing with sets of numbers to declare explicitly which sets you starting with. This is done before the such that symbol.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(intro_line1, intro_line2, intro_line3)), run_time=tracker.duration)
        
        with self.voiceover(text="For example, p in the natural numbers such that p is less than five") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(natural_set), run_time=1.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="is a completely different set to") as tracker:
            # Symbol at normal speed
            self.play(Write(not_equal), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 0.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="r in the real numbers such that r is less than five.") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(real_set), run_time=1.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def set_equality(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
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
        
        def_line1.next_to(intro_line2, DOWN, aligned_edge=LEFT, buff=0.8)
        def_line2.next_to(def_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        label_A = MarkupText('<b><i>A</i></b>', color="#00396B", font_size=28, font="sans-serif")
        label_B = MarkupText('<b><i>B</i></b>', color="#008000", font_size=28, font="sans-serif")
        
        label_A.move_to(LEFT * 2.5 + DOWN * 1.2)
        label_B.move_to(RIGHT * 2.5 + DOWN * 1.2)
        
        circle_A = Circle(radius=1.5, color="#00396B", stroke_width=3.0, fill_opacity=0)
        circle_A.move_to(label_A.get_center() + DOWN * 0.8)
        
        circle_B = Circle(radius=1.5, color="#008000", stroke_width=3.0, fill_opacity=0)
        circle_B.move_to(label_B.get_center() + DOWN * 0.8)
        
        element_a_in_A = MarkupText('<b><i>a</i></b>', color="#505050", font_size=24, font="sans-serif")
        element_b_in_A = MarkupText('<b><i>b</i></b>', color="#505050", font_size=24, font="sans-serif")
        element_a_in_B = MarkupText('<b><i>a</i></b>', color="#505050", font_size=24, font="sans-serif")
        element_b_in_B = MarkupText('<b><i>b</i></b>', color="#505050", font_size=24, font="sans-serif")
        
        element_a_in_A.move_to(circle_A.get_center() + LEFT * 0.5 + UP * 0.3)
        element_b_in_A.move_to(circle_A.get_center() + LEFT * 0.5 + DOWN * 0.3)
        element_a_in_B.move_to(circle_B.get_center() + LEFT * 0.5 + UP * 0.3)
        element_b_in_B.move_to(circle_B.get_center() + LEFT * 0.5 + DOWN * 0.3)
        
        arrow_a = CurvedArrow(
            start_point=element_a_in_A.get_right() + RIGHT * 0.2,
            end_point=element_a_in_B.get_left() + LEFT * 0.2,
            color="#505050",
            angle=0.15,
            tip_length=0.2
        )
        
        arrow_b = CurvedArrow(
            start_point=element_b_in_B.get_left() + LEFT * 0.2,
            end_point=element_b_in_A.get_right() + RIGHT * 0.2,
            color="#505050",
            angle=0.15,
            tip_length=0.2
        )
        
        and_underline = Line(
            start=def_line1.get_center() + RIGHT * 0.1 + DOWN * 0.3,
            end=def_line1.get_center() + RIGHT * 1 + DOWN * 0.3,
            color="#1853A2",
            stroke_width=3
        )
        
        with self.voiceover(text="Two sets are equal if they both contain the same elements.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(intro_line1, intro_line2)), run_time=tracker.duration)
        
        with self.voiceover(text="If for all little a in capital A, little a is also in B") as tracker:
            # Visual elements at natural speed
            self.play(
                Write(label_A),
                Write(label_B),
                Create(circle_A),
                Create(circle_B),
                run_time=1.0
            )

            self.play(Write(VGroup(def_line1, def_line2)))
            self.play(Write(VGroup(element_a_in_A, element_b_in_A, element_a_in_B, element_b_in_B)))
            self.play(Create(arrow_a), run_time=0.6)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.6
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="and for all little b in capital B, little b is also in capital A, then the sets A and B are equal.") as tracker:
            # Visual elements at natural speed
            self.play(Create(and_underline), Create(arrow_b), run_time=1.0)
            
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.0
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def order_doesnt_matter(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        set_A = MathTex(r'A', r'=', r'\{', r'1', r',', r'2', r',', r'3', r'\}', font_size=48, color="#505050")
        set_B = MathTex(r'B', r'=', r'\{', r'2', r',', r'3', r',', r'1', r'\}', font_size=48, color="#505050")
        
        set_A.move_to(LEFT * 3 + DOWN * 0.5)
        set_B.move_to(RIGHT * 3 + DOWN * 0.5)
        
        conclusion = MathTex(r'A = B', font_size=48, color="#505050")
        conclusion.move_to(DOWN * 2.5)
        
        # Arrows from original
        arrow_A_to_B_1 = CurvedArrow(
            start_point=set_A[3].get_bottom(),
            end_point=set_B[7].get_bottom(),
            color="#505050",
            angle=PI/3,
            tip_length=0.15
        )
        
        arrow_A_to_B_2 = CurvedArrow(
            start_point=set_A[5].get_bottom(),
            end_point=set_B[3].get_bottom(),
            color="#505050",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        arrow_A_to_B_3 = CurvedArrow(
            start_point=set_A[7].get_bottom(),
            end_point=set_B[5].get_bottom(),
            color="#505050",
            angle=PI/2,
            tip_length=0.15
        )
        
        arrow_B_to_A_2 = CurvedArrow(
            start_point=set_B[3].get_top(),
            end_point=set_A[5].get_top(),
            color="#FF6B6B",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        arrow_B_to_A_3 = CurvedArrow(
            start_point=set_B[5].get_top(),
            end_point=set_A[7].get_top(),
            color="#FF6B6B",
            angle=PI/2,
            tip_length=0.15
        )
        
        arrow_B_to_A_1 = CurvedArrow(
            start_point=set_B[7].get_top(),
            end_point=set_A[3].get_top(),
            color="#FF6B6B",
            angle=PI/3,
            tip_length=0.15
        )
        
        with self.voiceover(text="This definition means that the order of the elements doesn't matter.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(intro_line1, intro_line2)), run_time=tracker.duration)
        
        with self.voiceover(text="So if A contains one, two, and three") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_A), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="and B contains two, three, and one") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_B), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="we say one is in A and it's also in B,") as tracker:
            # Show only the arrow for "1"
            self.play(Create(arrow_A_to_B_1), run_time=tracker.duration)
        
        with self.voiceover(text="two is in A and it's also in B,") as tracker:
            # Show only the arrow for "2"
            self.play(Create(arrow_A_to_B_2), run_time=tracker.duration)
        
        with self.voiceover(text="and three is in A and it's also in B.") as tracker:
            # Show only the arrow for "3"
            self.play(Create(arrow_A_to_B_3), run_time=tracker.duration)
        
        with self.voiceover(text="We then do the same for all the elements in B.") as tracker:
            # Just the explanation, no arrows yet
            self.wait(tracker.duration)
        
        with self.voiceover(text="Two is in B and it's also in A,") as tracker:
            # Show arrow for "2"
            self.play(Create(arrow_B_to_A_2), run_time=tracker.duration)
        
        with self.voiceover(text="three is in B and it's also in A,") as tracker:
            # Show arrow for "3"
            self.play(Create(arrow_B_to_A_3), run_time=tracker.duration)
        
        with self.voiceover(text="and one is in B and it's also in A.") as tracker:
            # Show arrow for "1"
            self.play(Create(arrow_B_to_A_1), run_time=tracker.duration)
        
        with self.voiceover(text="and so we've shown that A is equal to B.") as tracker:
            # Conclusion at reasonable speed
            self.play(Write(conclusion), run_time=1.2)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.2
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def repeated_elements_dont_matter(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        intro_line1.to_edge(UP, buff=1.0)
        intro_line1.to_edge(LEFT, buff=0.5)
        intro_line2.next_to(intro_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        set_A = MathTex(r'A', r'=', r'\{', r'1', r',', r'2', r',', r'3', r'\}', font_size=48, color="#505050")
        set_B = MathTex(r'B', r'=', r'\{', r'2', r',', r'3', r',', r'3', r',', r'3', r',', r'1', r'\}', font_size=48, color="#505050")
        
        set_A.move_to(LEFT * 3 + DOWN * 0.5)
        set_B.move_to(RIGHT * 3 + DOWN * 0.5)
        
        conclusion_text = MathTex(r'A = B', font_size=48, color="#505050")
        conclusion_text.move_to(DOWN * 2.5 + LEFT * 0.5)
        
        checkmark = SVGMobject("images/check.svg")
        checkmark.set_color("#008000")
        checkmark.scale(0.4)
        checkmark.next_to(conclusion_text, RIGHT, buff=0.3)
        
        # Arrows from original
        arrow_A_to_B_1 = CurvedArrow(
            start_point=set_A[3].get_bottom(),
            end_point=set_B[11].get_bottom(),
            color="#505050",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        arrow_A_to_B_2 = CurvedArrow(
            start_point=set_A[5].get_bottom(),
            end_point=set_B[3].get_bottom(),
            color="#505050",
            angle=PI/3,
            tip_length=0.15
        )
        
        arrow_A_to_B_3 = CurvedArrow(
            start_point=set_A[7].get_bottom(),
            end_point=set_B[5].get_bottom(),
            color="#505050",
            angle=PI/4,
            tip_length=0.15
        )
        
        arrow_B_to_A_2 = CurvedArrow(
            start_point=set_B[3].get_top(),
            end_point=set_A[5].get_top(),
            color="#FF6B6B",
            angle=PI/3,
            tip_length=0.15
        )
        
        arrow_B_to_A_3_1 = CurvedArrow(
            start_point=set_B[5].get_top(),
            end_point=set_A[7].get_top(),
            color="#FF6B6B",
            angle=PI/4,
            tip_length=0.15
        )
        
        arrow_B_to_A_3_2 = CurvedArrow(
            start_point=set_B[7].get_top(),
            end_point=set_A[7].get_top(),
            color="#FF6B6B",
            angle=PI/3.5,
            tip_length=0.15
        )
        
        arrow_B_to_A_3_3 = CurvedArrow(
            start_point=set_B[9].get_top(),
            end_point=set_A[7].get_top(),
            color="#FF6B6B",
            angle=PI/3,
            tip_length=0.15
        )
        
        arrow_B_to_A_1 = CurvedArrow(
            start_point=set_B[11].get_top(),
            end_point=set_A[3].get_top(),
            color="#FF6B6B",
            angle=PI/2.5,
            tip_length=0.15
        )
        
        with self.voiceover(text="It also doesn't matter if the elements are repeated.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(intro_line1, intro_line2)), run_time=tracker.duration)
        
        with self.voiceover(text="Like before, as long as every element in one set can be shown to also be in the other, we still have equality.") as tracker:
            # Mathematical sets at reasonable speed
            self.play(Write(set_A), run_time=1.5)
            self.play(Write(set_B), run_time=2.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 3.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        # Show arrows demonstrating elements from A to B
        with self.voiceover(text="Like before, as long as every element in one set can be shown to also be in the other, we still have equality.") as tracker:
            # Arrows at natural speed
            self.play(Create(arrow_A_to_B_1), run_time=0.8)
            self.play(Create(arrow_A_to_B_2), run_time=0.8)
            self.play(Create(arrow_A_to_B_3), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.4
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        # This part doesn't have specific audio in the script - it's just a visual demonstration
        # So we can use a brief pause or minimal audio
        with self.voiceover(text="And we do the same for all elements in B.") as tracker:
            # Multiple arrows at natural speed
            self.play(Create(arrow_B_to_A_2), run_time=0.8)
            self.play(
                Create(arrow_B_to_A_3_1),
                Create(arrow_B_to_A_3_2),
                Create(arrow_B_to_A_3_3),
                run_time=1.2
            )
            self.play(Create(arrow_B_to_A_1), run_time=0.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="Generally we just write the elements in a way that's easiest to read, which usually means without repetitions and often in some sensible order") as tracker:
            # Conclusion at reasonable speed
            self.play(Write(conclusion_text), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="but just to be clear it makes no difference to the set, just to us as readers.") as tracker:
            # Checkmark at normal speed
            self.play(FadeIn(checkmark), run_time=0.6)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 0.6
            if remaining_time > 0.1:
                self.wait(remaining_time)

    def set_cardinality(self):
        self.camera.background_color = "#F0F0F0"
        
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
        
        title_line1.to_edge(UP, buff=1.0)
        title_line1.to_edge(LEFT, buff=0.5)
        title_line2.next_to(title_line1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        set_A = MathTex(r'A = \{1, 2, 3\}', font_size=48, color="#505050")
        set_A.move_to(LEFT * 2.5 + DOWN * 0.5)
        
        cardinality_A = MathTex(r'|A| = 3', font_size=48, color="#505050")
        cardinality_A.move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        set_P = MathTex(r'P = \{p \mid p \text{ is a prime}\}', font_size=48, color="#505050")
        set_P.move_to(LEFT * 2.5 + DOWN * 2.5)
        
        cardinality_P = MathTex(r'|P| = \infty', font_size=48, color="#505050")
        cardinality_P.move_to(RIGHT * 2.5 + DOWN * 2.5)
        
        with self.voiceover(text="The size or cardinality of a set is the number of elements it contains.") as tracker:
            # Text should match speech pace
            self.play(Write(VGroup(title_line1, title_line2)), run_time=tracker.duration)
        
        with self.voiceover(text="So if A contains one, two, and three, then the cardinality of A is three") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_A), run_time=1.8)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.8
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="and we denote the cardinality of a set with two vertical lines.") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(cardinality_A), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="If a set has an infinite number of elements, like the set of prime numbers for example") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(set_P), run_time=2.0)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 2.0
            if remaining_time > 0.1:
                self.wait(remaining_time)
        
        with self.voiceover(text="then it's perfectly fine to write the infinity symbol as the cardinality of the set.") as tracker:
            # Mathematical notation at reasonable speed
            self.play(Write(cardinality_P), run_time=1.5)
            # Wait for remaining audio only if there's significant time left
            remaining_time = tracker.duration - 1.5
            if remaining_time > 0.1:
                self.wait(remaining_time)