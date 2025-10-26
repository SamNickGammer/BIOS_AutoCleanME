"""
Create placeholder images for the slideshow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_images():
    """Create 5 sample placeholder images"""
    if not os.path.exists('assets/images'):
        os.makedirs('assets/images')
    
    colors = [
        ('#4A90E2', 'Welcome! 🎉'),
        ('#7ED321', 'Features ⚡'),
        ('#F5A623', 'Tools 🛠️'),
        ('#D0021B', 'Security 🔒'),
        ('#9013FE', 'Support 💜')
    ]
    
    for i, (color, text) in enumerate(colors, 1):
        # Create image
        img = Image.new('RGB', (400, 250), color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a nice font, fallback to default
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
        
        # Get text size and center it
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (400 - text_width) // 2
        y = (250 - text_height) // 2
        
        # Draw text
        draw.text((x, y), text, fill='white', font=font)
        
        # Save image
        img.save(f'assets/images/slide_{i}.png')
        print(f"Created slide_{i}.png")

if __name__ == "__main__":
    create_placeholder_images()