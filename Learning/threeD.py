from manim import *
import numpy as np

# ======================= BASIC 3D SETUP =======================

class Basic3DScene(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1], 
            z_range=[-3, 3, 1],
            x_length=8,
            y_length=8,
            z_length=6
        )
        
        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y") 
        z_label = axes.get_z_axis_label("z")
        
        # Create 3D objects
        cube = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.7)
        sphere = Sphere(radius=1, color=RED).shift(UP * 2)
        
        # Add everything to scene
        self.add(axes, x_label, y_label, z_label)
        self.play(Create(cube), Create(sphere))
        
        # Interactive camera movement
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()

# ======================= 3D MATHEMATICAL FUNCTIONS =======================

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1]
        )
        
        # Create 3D surface: z = sin(x) * cos(y)
        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
            fill_color=BLUE,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=0.5
        )
        
        # FIXED: Use MathTex instead of Tex for mathematical formulas
        title = MathTex("z = \\sin(x) \\cdot \\cos(y)", font_size=48).to_edge(UP)
        
        self.add(axes, title)
        self.play(Create(surface), run_time=3)
        
        # Camera animation for "interactive" feel
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)

# ======================= ML VISUALIZATION: 3D DATA POINTS =======================

class MLDataVisualization(ThreeDScene):
    def construct(self):
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2], 
            z_range=[0, 10, 2],
            axis_config={"color": WHITE}
        )
        
        # Generate random 3D data points (like ML dataset)
        np.random.seed(42)
        n_points = 50
        
        # Create two clusters of data
        cluster1 = np.random.normal([3, 3, 3], 1, (25, 3))
        cluster2 = np.random.normal([7, 7, 7], 1, (25, 3))
        
        data_points = []
        
        # Cluster 1 - Blue points
        for point in cluster1:
            dot = Dot3D(
                point=axes.c2p(point[0], point[1], point[2]),
                color=BLUE,
                radius=0.1
            )
            data_points.append(dot)
            
        # Cluster 2 - Red points  
        for point in cluster2:
            dot = Dot3D(
                point=axes.c2p(point[0], point[1], point[2]),
                color=RED,
                radius=0.1
            )
            data_points.append(dot)
        
        # Add title
        title = Text("3D ML Dataset Visualization", font_size=36).to_edge(UP)
        
        # Add axes labels
        x_label = axes.get_x_axis_label("Feature 1")
        y_label = axes.get_y_axis_label("Feature 2")
        z_label = axes.get_z_axis_label("Feature 3")
        
        self.add(axes, title, x_label, y_label, z_label)
        
        # Animate points appearing
        self.play(*[Create(dot) for dot in data_points], run_time=3)
        
        # Interactive camera movement
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.move_camera(phi=70 * DEGREES, theta=120 * DEGREES, run_time=3)
        self.move_camera(phi=70 * DEGREES, theta=210 * DEGREES, run_time=3)
        self.wait(1)


# ======================= INTERACTIVE CONTROLS =======================

class InteractiveCameraControls(ThreeDScene):
    def construct(self):
        # Create axes and objects
        axes = ThreeDAxes()
        cube = Cube(fill_color=BLUE, fill_opacity=0.7)
        sphere = Sphere(color=RED).shift(UP * 2)
        cylinder = Cylinder(height=2, radius=0.5, color=GREEN).shift(RIGHT * 3)
        
        objects = VGroup(cube, sphere, cylinder)
        
        # Instructions text
        instructions = VGroup(
            Text("Camera Controls Demonstration", font_size=36),
            Text("• Phi: Up/Down rotation", font_size=24),
            Text("• Theta: Left/Right rotation", font_size=24),
            Text("• Distance: Zoom in/out", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        
        self.add(axes, objects, instructions)
        
        # Series of camera movements to show "interactive" behavior
        # Simulate different viewing angles
        camera_positions = [
            {"phi": 75 * DEGREES, "theta": 30 * DEGREES, "distance": 8},
            {"phi": 60 * DEGREES, "theta": 120 * DEGREES, "distance": 6},
            {"phi": 45 * DEGREES, "theta": 210 * DEGREES, "distance": 10},
            {"phi": 90 * DEGREES, "theta": 0 * DEGREES, "distance": 8},    # Top view
            {"phi": 0 * DEGREES, "theta": 0 * DEGREES, "distance": 8},     # Side view
        ]
        
        for i, pos in enumerate(camera_positions):
            self.move_camera(
                phi=pos["phi"], 
                theta=pos["theta"], 
                distance=pos["distance"],
                run_time=2
            )
            
            # Add a label showing current view
            view_label = Text(f"View {i+1}", font_size=32, color=YELLOW).to_corner(UR)
            self.add_fixed_in_frame_mobjects(view_label)
            self.wait(1)
            self.remove(view_label)
        
        # End with ambient rotation
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)