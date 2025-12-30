#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
title_image_path = os.path.join(script_dir, 'images', 'correct_title.png')
output_path = os.path.join(script_dir, 'og-image-new.png')

# Open the title image
title_img = Image.open(title_image_path).convert('RGBA')

# Resize title image much larger - make it take up most of the space
# 제목 이미지를 훨씬 크게 - 약 480px 높이
target_height = 480
aspect_ratio = title_img.width / title_img.height
target_width = int(target_height * aspect_ratio)

# If it's too wide, constrain by width instead
if target_width > 1100:
    target_width = 1100
    target_height = int(target_width / aspect_ratio)

title_img_resized = title_img.resize((target_width, target_height), Image.Resampling.LANCZOS)

# Create a new image with standard social media dimensions (1200x630)
og_image = Image.new('RGB', (1200, 630), color=(240, 247, 255))  # #F0F7FF light blue

# Calculate position to center title image both horizontally and vertically
title_x = (1200 - target_width) // 2
title_y = (630 - target_height) // 2

# Paste the title image with alpha blending
og_image.paste(title_img_resized, (title_x, title_y), title_img_resized)

# Add sub text message at the bottom
draw = ImageDraw.Draw(og_image)

# Message text
message = "송금하고 쿠폰부터 아이패드까지 받아가세요!"

# Try to use a nice font
try:
    font_paths = [
        '/System/Library/Fonts/Arial.ttf',
        '/System/Library/Fonts/Helvetica.ttc',
        '/Library/Fonts/Arial.ttf',
    ]
    font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, 36)
                break
            except:
                continue
    if not font:
        font = ImageFont.load_default()
except:
    font = ImageFont.load_default()

# Draw the message at the bottom with white background
text_y = 560
text_color = (0, 130, 255)  # #0082FF blue
background_color = (255, 255, 255)  # white

# Get text bounding box to center it
bbox = draw.textbbox((0, 0), message, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (1200 - text_width) // 2

# Draw the text (no background box)
draw.text((text_x, text_y), message, fill=text_color, font=font)

# Save the og image
og_image.save(output_path, 'PNG', optimize=True)
print(f'✓ OG image generated successfully!')
print(f'✓ Title image: {title_image_path}')
print(f'✓ Title resized from {title_img.size} to {title_img_resized.size}')
print(f'✓ Title centered at position: ({title_x}, {title_y})')
print(f'✓ Hooking message: {message}')
print(f'✓ Saved to: {output_path}')
print(f'✓ Dimensions: 1200x630')
