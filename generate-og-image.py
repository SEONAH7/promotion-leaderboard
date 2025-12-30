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
# Convert RGBA to RGB for pasting
if title_img_resized.mode == 'RGBA':
    # Create a white background for the title image area
    title_bg = Image.new('RGB', (1200, 630), color=(240, 247, 255))
    title_bg.paste(title_img_resized, (title_x, title_y), title_img_resized)
    og_image = title_bg
else:
    og_image.paste(title_img_resized, (title_x, title_y))

# Save the og image
og_image.save(output_path, 'PNG', optimize=True)
print(f'✓ OG image generated successfully!')
print(f'✓ Title image: {title_image_path}')
print(f'✓ Title resized from {title_img.size} to {title_img_resized.size}')
print(f'✓ Title centered at position: ({title_x}, {title_y})')
print(f'✓ Saved to: {output_path}')
print(f'✓ Dimensions: 1200x630')
