#!/usr/bin/env python3
"""
Solution 1: Render chapters separately and concatenate them.
This is the most reliable approach that preserves audio and visual quality.
"""

import subprocess
import os
from pathlib import Path

def render_complete_video():
    """
    Render all chapters separately and concatenate them into a single video.
    """
    
    # Define all chapters in order
    chapters = [
        ("scenes/ch01_basics", "BasicsWithVoiceover"),
        ("scenes/ch02_subsets", "SubsetsWithVoiceover"), 
        ("scenes/ch03_empty_set", "EmptySetWithVoiceover"),
        ("scenes/ch04_union_and_intersection", "UnionAndIntersectionWithVoiceover"),
        ("scenes/ch05_complement", "TheComplementWithVoiceover"),
        ("scenes/ch06_de_morgan_laws", "DeMorganLawsWithVoiceover"),
        ("scenes/ch07_sets_of_sets_and_power_sets", "SetsOfSetsPowerSetsIndexedFamiliesWithVoiceover"),
        ("scenes/ch08_russells_paradox", "RussellsParadoxWithVoiceover"),
    ]
    
    # Output and temporary directories
    output_dir = Path("media/videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    temp_dir = Path("temp_chapters")
    temp_dir.mkdir(exist_ok=True)
    
    # Video quality settings
    quality = "-qh"  # high quality
    
    rendered_files = []
    
    print("Rendering individual chapters...")
    
    # Step 1: Render each chapter individually
    for i, (module, class_name) in enumerate(chapters, 1):
        print(f"Rendering Chapter {i}: {class_name}")
        
        # Check if the file exists
        scene_file = Path(f"{module}.py")
        if not scene_file.exists():
            print(f"Error: Scene file {scene_file} does not exist!")
            print(f"Current working directory: {Path.cwd()}")
            print(f"Looking for: {scene_file.absolute()}")
            return False
        
        print(f"Found scene file: {scene_file}")
        
        # Construct the corrected manim command
        cmd = [
            "manim",
            "render",  # Add explicit render command
            quality,
            f"{module}.py",
            class_name,
            "-o", f"chapter_{i:02d}_{class_name}"  # Correct output flag syntax
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Chapter {i} rendered successfully")
            
            # Find the generated video file
            chapter_file = find_generated_video(class_name, i)
            if chapter_file:
                rendered_files.append(chapter_file)
            else:
                print(f"Could not find output file for Chapter {i}")
                
        except subprocess.CalledProcessError as e:
            print(f"Error rendering Chapter {i}: {e}")
            print(f"STDOUT: {e.stdout}")
            print(f"STDERR: {e.stderr}")
            return False
    
    if len(rendered_files) != len(chapters):
        print(f"Only {len(rendered_files)} of {len(chapters)} chapters rendered successfully")
        return False
    
    print(f"All {len(chapters)} chapters rendered successfully")
    
    # Step 2: Create file list for ffmpeg
    file_list_path = temp_dir / "file_list.txt"
    with open(file_list_path, 'w') as f:
        for video_file in rendered_files:
            f.write(f"file '{video_file.absolute()}'\n")
    
    # Step 3: Concatenate videos using ffmpeg
    print("Concatenating chapters into final video...")
    
    final_output = output_dir / "SetTheoryCompleteVideo.mp4"
    
    ffmpeg_cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(file_list_path),
        "-c", "copy",
        "-y",
        str(final_output)
    ]
    
    try:
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True)
        print(f"Final video created: {final_output}")
        
        # Clean up temporary files
        cleanup_temp_files(temp_dir)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error concatenating videos: {e}")
        print(f"STDERR: {e.stderr}")
        return False

def find_generated_video(class_name, chapter_num):
    """Find the generated video file for a chapter."""
    
    possible_paths = [
        Path("media/videos") / f"chapter_{chapter_num:02d}_{class_name}.mp4",
        Path("media/videos") / f"{class_name}.mp4",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    # Search recursively in media directory
    media_dir = Path("media")
    if media_dir.exists():
        for video_file in media_dir.rglob("*.mp4"):
            if class_name in video_file.name or f"chapter_{chapter_num:02d}" in video_file.name:
                return video_file
    
    return None

def cleanup_temp_files(temp_dir):
    """Clean up temporary files."""
    try:
        import shutil
        shutil.rmtree(temp_dir)
        print("Temporary files cleaned up")
    except Exception as e:
        print(f"Could not clean up temporary files: {e}")

def list_scene_files():
    """List all scene files to help with debugging."""
    scenes_dir = Path("scenes")
    if scenes_dir.exists():
        print(f"Found scenes directory: {scenes_dir.absolute()}")
        print("Scene files found:")
        for py_file in scenes_dir.glob("*.py"):
            print(f"  - {py_file}")
    else:
        print(f"Scenes directory not found: {scenes_dir.absolute()}")
    
def test_manim_command():
    """Test if manim command works with current syntax."""
    try:
        result = subprocess.run(["manim", "--help"], capture_output=True, text=True, check=True)
        print("Manim command is working correctly")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error testing manim command: {e}")
        return False

if __name__ == "__main__":
    # List scene files for debugging
    list_scene_files()
    
    # Test manim first
    if not test_manim_command():
        print("Manim command test failed. Please check your installation.")
        exit(1)
    
    success = render_complete_video()
    if success:
        print("Complete video rendering finished successfully")
    else:
        print("Video rendering failed")
        exit(1)