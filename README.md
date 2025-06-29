# Set Theory Animation Project

## Overview
This project recreates Dr. Will Wood's "Set Theory | All-in-One Video" using Python and Manim (Mathematical Animation Engine). The animations explain key concepts in set theory through visual demonstrations with synchronized AI voiceovers.

## System Requirements

### Linux (Debian/Ubuntu-based systems)

**Before installing Python dependencies**, you must install the following system packages:

```bash
# Essential build tools and Cairo/Pango for rendering
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev

# LaTeX for mathematical typesetting (choose one)
sudo apt install texlive-full        # Complete LaTeX installation (recommended)
# OR for minimal installation:
# sudo apt install texlive texlive-latex-extra texlive-fonts-extra

# SoX for audio processing (required for manim-voiceover)
sudo apt install sox
```

### Other Systems

For **macOS**, **Windows**, or **other Linux distributions**, please refer to the official Manim installation guide:
- 📖 **[Manim Installation Guide](https://docs.manim.community/en/stable/installation.html)**

This guide provides detailed instructions for:
- macOS (using Homebrew)
- Windows (using Chocolatey or manual installation)
- Fedora/CentOS/RHEL systems
- Arch Linux
- And other platforms

## Python Installation

After installing the system dependencies above:

```bash
# Clone the repository
git clone [your-repo-url]
cd Set_theory

# Install Python dependencies using uv (recommended)
uv sync

# OR using pip
pip install -e .
```

## Features

- 🎥 **Animated explanations** of core set theory concepts
- 🗣️ **AI-generated voiceovers** synchronized with animations  
- 📊 **Visual demonstrations** using geometric shapes and mathematical notation
- 🔄 **Modular structure** with individual classes for each topic
- 🎯 **Educational focus** following established mathematical pedagogy

## Video Chapters

The project recreates the following chapters from the original video:

- **0:00** - The Basics
- **4:21** - Subsets  
- **7:25** - The Empty Set
- **8:21** - Union and Intersection
- **20:02** - The Complement
- **24:10** - De Morgan's Laws
- **26:13** - Sets of Sets, Power Sets, Indexed Families

## Usage

### Basic Animation (No Audio)
```bash
# Render a specific scene
manim -pql scenes/empty_set.py EmptySet

# Render all scenes in a file
manim -pql scenes/empty_set.py
```

### With AI Voiceover
```bash
# Using Google TTS (free)
manim -pql scenes/set_definition.py SetDefinition

# For higher quality voices, set up API keys:
# ElevenLabs: export ELEVEN_API_KEY=your_key
# OpenAI: export OPENAI_API_KEY=your_key
```

## Text-to-Speech Services

The project supports multiple TTS services:

- **Google TTS (gTTS)**: Free, good for testing
- **ElevenLabs**: Premium quality, most human-like voices
- **OpenAI TTS**: Good balance of quality and cost
- **Microsoft Azure**: Enterprise-grade with neural voices

See the [Manim Voiceover documentation](https://voiceover.manim.community/) for setup instructions.

## Project Structure

```
Set_theory/
├── videos/           # Individual scene classes
├── tests/           # Test implementations  
├── images/          # SVG assets and graphics
├── scripts/         # Audio scripts and transcripts
└── output/          # Rendered video files
```

## Development

### Adding New Scenes
1. Create a new class inheriting from `VoiceoverScene`
2. Implement the `construct()` method with animations
3. Add voiceover segments using `with self.voiceover():`
4. Test with `manim -pql your_file.py YourScene`

### Code Style
- Follow the established pattern from existing scenes
- Use descriptive variable names
- Include docstrings for methods
- Maintain consistent visual styling

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-concept`)
3. Commit your changes (`git commit -am 'Add new set theory concept'`)
4. Push to the branch (`git push origin feature/new-concept`)
5. Create a Pull Request

## Reference

**Original Video**: [Set Theory | All-in-One Video by Dr. Will Wood](https://www.youtube.com/watch?v=5ZhNmKb-dqk)

## License

[Your License Here]

## Troubleshooting

### Common Issues

**"SoX not found" error:**
```bash
sudo apt install sox  # Linux
brew install sox      # macOS
```

**LaTeX rendering issues:**
```bash
sudo apt install texlive-full  # Comprehensive LaTeX installation
```

**Import errors:**
```bash
# Reinstall dependencies
uv sync --refresh
```

For more help, see the [Manim Community FAQ](https://docs.manim.community/en/stable/faq/index.html).