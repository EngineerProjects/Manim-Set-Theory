from manim import *

class SubsetsTitle(Scene):
    def construct(self):
        # Same background color as previous scenes
        self.camera.background_color = "#F0F0F0"
        
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
        
        # Animation sequence
        self.play(AddTextLetterByLetter(subsets_title), run_time=2)
        self.wait(0.5)
        self.play(Create(underline), run_time=1)
        self.wait(2)