# Digital Persona Forge 🤖✨

Create dynamic AI characters that generate personalized social media-style content through text, images, and audio outputs.

## 🌟 Features

- **Dynamic Character Creation**: Create AI personas with unique personalities, professions, and hobbies
- **Multi-Modal Content Generation**: 
  - Text posts with character-specific reflections and stories
  - Custom image generation with text overlays
  - Text-to-speech audio posts with character narration
- **Daily Post Management**: Prevents duplicate posts within the same day
- **Customizable Routines**: Define daily activities and hobbies for more authentic content

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed on your system.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/digital-persona-forge.git
cd digital-persona-forge
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Usage

```python
from digital_persona_forge import DynamicAICharacter

# Create a new AI character
ai_character = DynamicAICharacter(
    name="Alex Solis",
    location="Barcelona, Spain",
    profession="Freelance Writer and Photographer",
    hobbies=["hiking", "cooking fusion recipes", "playing guitar", "stargazing"],
    personality="Alex is an adventurous and introspective soul, always seeking deeper connections through art and nature."
)

# Generate a post
post = ai_character.create_post()
```

## 📝 Example Outputs

### Text Post
```
Alex Solis reflects on a day of stargazing in Barcelona, Spain. Life is like stargazing—you find joy in the unexpected.
```

### Image Post
- Generates a custom image with text overlay
- Saved as 'daily_post.png'

### Audio Post
- Creates an MP3 file with the character's voice
- Saved as 'daily_audio.mp3'

## 🛠️ Customization

You can customize your AI character by modifying:
- Daily routines
- Hobbies and interests
- Personality traits
- Location and profession
- Post generation prompts

## 📦 Project Structure

```
digital-persona-forge/
├── digital_persona_forge/
│   └── __init__.py
├── examples/
│   └── basic_usage.py
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PIL for image generation
- pyttsx3 for text-to-speech capabilities
- Python datetime and random libraries