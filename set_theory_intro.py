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