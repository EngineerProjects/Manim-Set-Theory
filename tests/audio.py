from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SetDefinition(VoiceoverScene):
    def construct(self):
        self.camera.background_color = "#F0F0F0"
        
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
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

        car_body = Rectangle(width=0.8, height=0.4, color=BLUE, fill_opacity=0.7)
        car_wheel1 = Circle(radius=0.15, color=BLACK, fill_opacity=0.7)
        car_wheel2 = Circle(radius=0.15, color=BLACK, fill_opacity=0.7)
        car_wheel1.move_to(car_body.get_bottom() + LEFT * 0.25 + DOWN * 0.1)
        car_wheel2.move_to(car_body.get_bottom() + RIGHT * 0.25 + DOWN * 0.1)
        car = VGroup(car_body, car_wheel1, car_wheel2)
        car.move_to(circle.get_center() + LEFT * 1.5)
        
        atom_center = Circle(radius=0.1, color=BLACK, fill_opacity=1)
        electron1 = Circle(radius=0.05, color=BLACK, fill_opacity=1)
        electron2 = Circle(radius=0.05, color=BLACK, fill_opacity=1)
        orbit1 = Ellipse(width=0.6, height=0.3, color=BLACK, stroke_width=2)
        orbit2 = Ellipse(width=0.6, height=0.3, color=BLACK, stroke_width=2).rotate(PI/3)
        electron1.move_to(atom_center.get_center() + RIGHT * 0.3)
        electron2.move_to(atom_center.get_center() + LEFT * 0.2 + UP * 0.15)
        atom = VGroup(orbit1, orbit2, atom_center, electron1, electron2)
        atom.move_to(circle.get_center() + DOWN * 1.5)
        
        equation = MathTex(r"\mathbf{1 + 1 = 2}", color=BLACK)
        equation.scale(0.8)
        equation.move_to(circle.get_center() + RIGHT * 1.0)
        
        with self.voiceover(text="A set is a collection of objects we call elements.") as tracker:
            self.play( 
                Write(definition),
                Create(circle),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="That could mean physical objects") as tracker:
            self.play(FadeIn(car), run_time=tracker.duration)
        
        with self.voiceover(text="thoughts, ideas and concepts") as tracker:
            self.play(FadeIn(atom), run_time=tracker.duration)
        
        with self.voiceover(text="including mathematical objects which will of course be the main focus for us.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        self.wait(1)