import random
import datetime
import pyttsx3
import io
import os
from PIL import Image
import torch
from diffusers import DiffusionPipeline
from dotenv import load_dotenv


class DynamicAICharacter:
    def __init__(self, name, location, profession, hobbies, personality, device="cuda"):
        self.name = name
        self.location = location
        self.profession = profession
        self.hobbies = hobbies
        self.personality = personality
        self.mood_states = ["excited", "reflective", "peaceful", "energetic", "creative", "grateful"]
        self.current_mood = random.choice(self.mood_states)
        self.last_post_date = None
        self.device = "cuda" if torch.cuda.is_available() and device == "cuda" else "cpu"

        # Initialize the image generation pipeline
        try:
            print("Loading FLUX.1 model...")
            self.pipe = DiffusionPipeline.from_pretrained(
                "black-forest-labs/FLUX.1-dev",
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            ).to(self.device)

            print("Loading Midjourney Mix2 LoRA...")
            self.pipe.load_lora_weights("strangerzonehf/Flux-Midjourney-Mix2-LoRA")

            # Enable memory efficient attention if using cuda
            if self.device == "cuda":
                self.pipe.enable_xformers_memory_efficient_attention()

        except Exception as e:
            raise Exception(f"Failed to initialize image generation pipeline: {str(e)}")

    def generate_image_post(self):
        """Generate an image using FLUX.1 model with Midjourney Mix2 LoRA"""
        try:
            # Create a detailed prompt based on character's context
            time_of_day = self._get_time_of_day()
            current_activity = random.choice(self.hobbies)
            prompt = self._generate_image_prompt(time_of_day, current_activity)

            # Generate the image
            print(f"Generating image with prompt: {prompt}")
            image = self.pipe(
                prompt=prompt,
                num_inference_steps=30,
                guidance_scale=7.5,
                width=768,
                height=768,
            ).images[0]

            # Convert to bytes for saving
            output = io.BytesIO()
            image.save(output, format='PNG')
            output.seek(0)

            return output

        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None

    def _generate_image_prompt(self, time_of_day, activity):
        """Generate a detailed prompt for the FLUX model"""

        location_prompts = {
            "morning": "during golden hour, early morning light, soft illumination",
            "afternoon": "under bright natural daylight, vivid colors, clear visibility",
            "evening": "during sunset, golden light, warm tones",
            "night": "under moonlight and city lights, atmospheric night scene"
        }

        mood_prompts = {
            "excited": "vibrant and energetic scene, dynamic composition",
            "reflective": "contemplative atmosphere, serene moment",
            "peaceful": "tranquil setting, harmonious composition",
            "energetic": "dynamic scene, movement and energy",
            "creative": "artistic composition, imaginative scene",
            "grateful": "heartwarming scene, emotional moment"
        }

        style_prompts = [
            "cinematic lighting",
            "professional photography",
            "detailed composition",
            "high resolution",
            "masterpiece",
            "best quality",
            "trending on artstation",
            "award winning photo"
        ]

        prompt = f"A stunning scene in {self.location} of someone {activity}, "
        prompt += f"{location_prompts[time_of_day]}, {mood_prompts[self.current_mood]}, "
        prompt += f"{', '.join(random.sample(style_prompts, 3))}"

        # Add negative prompt elements
        self.negative_prompt = "blurry, low quality, distorted, deformed, ugly, watermark"

        return prompt

    def _get_time_of_day(self):
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 22:
            return "evening"
        else:
            return "night"

    def generate_text_post(self):
        """Generate a text post"""
        time_of_day = self._get_time_of_day()
        template = (
                f"📍 {self.location} | {time_of_day.title()}\n\n"
                f"Feeling {self.current_mood} while {random.choice(self.hobbies)}. "
                f"{random.choice(['The atmosphere is absolutely magical!', 'Every moment feels special here.', 'So grateful for these experiences!'])} "
                f"#Life{self.profession.replace(' ', '')}" + " #" + self.location.replace(' ', '') + " 🌟"
        )
        return template

    def generate_audio_post(self):
        """Generate an audio post"""
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        text = (
            f"Hi everyone! This is {self.name} coming to you from {self.location}. "
            f"Today I'm feeling {self.current_mood} as I spend time {random.choice(self.hobbies)}. "
            f"The {self._get_time_of_day()} here is absolutely beautiful!"
        )
        output_file = f"daily_audio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        return output_file

    def create_post(self):
        """Create a random post (text, image, or audio)"""
        today = datetime.date.today()
        if self.last_post_date == today:
            return "Post already generated for today."

        self.current_mood = random.choice(self.mood_states)
        post_type = random.choice(["text", "image", "audio"])

        self.last_post_date = today

        if post_type == "text":
            return self.generate_text_post()
        elif post_type == "image":
            return self.generate_image_post()
        else:
            return self.generate_audio_post()


# Example usage
if __name__ == "__main__":
    try:
        # Create character
        ai_character = DynamicAICharacter(
            name="Alex Solis",
            location="Barcelona, Spain",
            profession="Freelance Writer and Photographer",
            hobbies=[
                "exploring ancient Gothic architecture",
                "capturing street life with a vintage camera",
                "sketching in a sunlit plaza",
                "playing Spanish guitar in Park Güell",
                "learning to cook paella from local chefs"
            ],
            personality="A thoughtful observer with a passion for finding beauty in everyday moments.",
            device="cuda"  # Use "cpu" if no GPU available
        )

        # Test each type of post
        print("\nTesting all post types:")

        # Test text post
        print("\nGenerating text post...")
        text_post = ai_character.generate_text_post()
        print(text_post)

        # Test image post
        print("\nGenerating image post...")
        image_post = ai_character.generate_image_post()
        if image_post:
            with open(f"generated_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png", "wb") as f:
                f.write(image_post.read())
            print("Image saved successfully!")

        # Test audio post
        print("\nGenerating audio post...")
        audio_post = ai_character.generate_audio_post()
        print(f"Audio saved as '{audio_post}'")

    except Exception as e:
        print(f"Error: {str(e)}")