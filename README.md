# Set Theory Animation Project

## Overview
This project recreates Dr. Will Wood's "Set Theory | All-in-One Video" using Python and Manim (Mathematical Animation Engine). The animations explain key concepts in set theory through visual demonstrations.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Manim Community Edition v0.19.0
- Required SVG files in the `/images` directory

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv set-theory
   source set-theory/bin/activate  # On Windows: set-theory\Scripts\activate
   ```

2. Install Manim and dependencies:
   ```bash
   pip install manim
   ```

3. Place the required SVG files in the `images/` directory:
   - `car-svgrepo-com.svg`
   - `atom-symbol-svgrepo-com.svg`
   - `check.svg`
   - `cross.svg`

## Running the Animations

To run individual scenes:

```bash
# Introduction scene
manim -pql set_theory_intro.py SetTheoryIntroExact

# Set definition with objects
manim -pql set_theory_intro.py SetDefinition

# Set of triangles demonstration
manim -pql set_theory_intro.py SetOfTriangles
```

To generate higher quality videos, replace `-pql` with `-pqh`.

## Project Structure

The project contains several scene classes:

1. **SetTheoryIntroExact**: The opening title with "Set Theory" and author credit
2. **SetDefinition**: Explains what a set is with examples (car, atom, equation)
3. **SetOfTriangles**: Demonstrates the concept of a set of triangles with validation

## Creating a Full Video

To compile all scenes into a single video, you can either:

1. Use the `FullVideo` class (add this to your code):
   ```python
   class FullVideo(Scene):
       def construct(self):
           SetTheoryIntroExact().construct()
           self.clear()
           self.wait(0.5)
           
           SetDefinition().construct()
           self.clear()
           self.wait(0.5)
           
           SetOfTriangles().construct()
   ```

2. Or use FFmpeg to concatenate the rendered videos:
   ```bash
   ffmpeg -f concat -safe 0 -i scenes.txt -c copy full_video.mp4
   ```
   Where `scenes.txt` contains:
   ```
   file 'SetTheoryIntroExact.mp4'
   file 'SetDefinition.mp4'
   file 'SetOfTriangles.mp4'
   ```

## Customization

To modify animations:
- Adjust timing by changing `run_time` and `self.wait()` values
- Change colors using hex values (e.g., `#008000` for green)
- Modify positions with `move_to()`, `shift()`, and `next_to()`
- Change scaling with `scale()`

## Next Steps

Future scenes to implement:
- Subsets demonstration
- Empty set explanation
- Union and intersection operations
- Complement and De Morgan's Laws
- Sets of sets, power sets, and indexed families