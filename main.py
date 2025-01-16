import random
import datetime
from PIL import Image, ImageDraw, ImageFont
import pyttsx3
import io

class DynamicAICharacter:
    def __init__(self, name, location, profession, hobbies, personality):
        self.name = name
        self.location = location
        self.profession = profession
        self.hobbies = hobbies
        self.personality = personality
        self.daily_routine = [
            "Morning meditation by the beach",
            "Working on creative projects",
            "Cooking a new recipe with local ingredients",
            "Exploring the city's art scene",
            "Relaxing under the stars",
        ]
        self.last_post_date = None

    def generate_text_post(self):
        prompts = [
            f"Hi friends! Today, I explored {self.location} and found a cozy spot perfect for {random.choice(self.hobbies)}. Feeling grateful for the little joys in life!",
            f"Life as a {self.profession} in {self.location} brings its own rhythm. This morning, I started with {random.choice(self.daily_routine)} and ended with some quiet time.",
            f"I believe that {random.choice(self.hobbies)} is a reflection of who we are. What do you think? Here's a thought: 'Every moment holds its own melody.'",
        ]
        return random.choice(prompts)

    def generate_image_post(self):
        text = f"{self.name} | {self.location} | {datetime.date.today().strftime('%B %d, %Y')}"
        bg_color = random.choice([(255, 228, 196), (135, 206, 250), (240, 230, 140)])
        img = Image.new('RGB', (800, 400), color=bg_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        # Add decorative text
        draw.text((50, 50), text, fill="black", font=font)
        draw.text((50, 200), f"A beautiful view for the day: {random.choice(self.hobbies).capitalize()}!", fill="black", font=font)

        output = io.BytesIO()
        img.save(output, format="PNG")
        output.seek(0)
        return output

    def generate_audio_post(self):
        text = f"Hey everyone, it's {self.name}! I just finished an amazing day of {random.choice(self.hobbies)} in {self.location}. Here's to finding beauty in every moment!"
        engine = pyttsx3.init()
        output_file = "daily_audio.mp3"
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        return output_file

    def create_post(self):
        post_type = random.choice(["text", "image", "audio"])
        today = datetime.date.today()

        if self.last_post_date == today:
            return "Post already generated for today."

        self.last_post_date = today

        if post_type == "text":
            return self.generate_text_post()
        elif post_type == "image":
            return self.generate_image_post()
        elif post_type == "audio":
            return self.generate_audio_post()


# Create a unique AI character
ai_character = DynamicAICharacter(
    name="Alex Solis",
    location="Kyoto, Japan",
    profession="Travel Blogger and Digital Artist",
    hobbies=["sketching temples", "writing haikus", "experimenting with ramen recipes", "photography"],
    personality="Alex is deeply curious and loves blending traditional aesthetics with modern creativity."
)

# Generate a daily post
post = ai_character.create_post()

# Handle the post output
if isinstance(post, str) and post.endswith(".mp3"):
    print(f"Audio Post saved as {post}.")
elif isinstance(post, str):
    print("Text Post:\n", post)
elif isinstance(post, io.BytesIO):
    with open("daily_post.png", "wb") as f:
        f.write(post.read())
    print("Image Post saved as 'daily_post.png'.")
