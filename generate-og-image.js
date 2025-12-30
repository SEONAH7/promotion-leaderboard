const fs = require('fs');
const path = require('path');

// Try using sharp for image manipulation
const sharp = require('sharp');

async function generateOGImage() {
  try {
    // Load the title image
    const titleImagePath = path.join(__dirname, 'images', 'title.png');

    // Create SVG with hooking message
    const svgMessage = `
      <svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg">
        <!-- Light blue background -->
        <rect width="1200" height="630" fill="#F0F7FF"/>

        <!-- Title image placeholder (will be added via canvas) -->
        <rect width="1200" height="450" fill="#F0F7FF"/>

        <!-- Hooking message line -->
        <text x="600" y="540" font-family="Arial, sans-serif" font-size="42" font-weight="bold" text-anchor="middle" fill="#0082FF">
          송금 금액에 따른 보상 혜택을 확인하세요!
        </text>
      </svg>
    `;

    // For now, let's try a simpler approach using composite
    // First, create the title image area with message
    const metadata = await sharp(titleImagePath).metadata();
    const titleWidth = metadata.width;
    const titleHeight = metadata.height;

    // Create a new image with the proper dimensions for social media (1200x630)
    const outputPath = path.join(__dirname, 'og-image.png');

    // Resize title image to fit in 1200x630 and add message below
    await sharp({
      create: {
        width: 1200,
        height: 630,
        channels: 3,
        background: { r: 240, g: 247, b: 255 } // #F0F7FF
      }
    })
    .composite([
      {
        input: titleImagePath,
        top: 90,
        left: Math.floor((1200 - 600) / 2) // Center horizontally, assuming title is ~600px wide
      }
    ])
    .png()
    .toFile(outputPath);

    console.log('✓ OG image generated successfully!');
    console.log(`✓ Saved to: ${outputPath}`);

  } catch (error) {
    console.error('Error generating OG image:', error.message);
    console.error('Attempting fallback method...');

    // Fallback: Just copy the title image if sharp fails
    try {
      const source = path.join(__dirname, 'images', 'title.png');
      const dest = path.join(__dirname, 'og-image.png');
      fs.copyFileSync(source, dest);
      console.log('✓ Fallback: Copied title image as og-image');
    } catch (fallbackError) {
      console.error('Fallback also failed:', fallbackError.message);
    }
  }
}

generateOGImage();
