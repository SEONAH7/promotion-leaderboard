const { createCanvas } = require('canvas');
const fs = require('fs');

// Create canvas (1200x630 is standard for OG images)
const canvas = createCanvas(1200, 630);
const ctx = canvas.getContext('2d');

// Background gradient
const gradient = ctx.createLinearGradient(0, 0, 1200, 630);
gradient.addColorStop(0, '#F5FAFF');
gradient.addColorStop(1, '#FFFFFF');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 1200, 630);

// Main title
ctx.font = 'bold 72px "Arial"';
ctx.fillStyle = '#0082FF';
ctx.textAlign = 'center';
ctx.fillText('프로모션 리더보드', 600, 150);

// Subtitle
ctx.font = 'bold 60px "Arial"';
ctx.fillStyle = '#1A1B22';
ctx.fillText('모인', 600, 230);

// Description
ctx.font = '36px "Arial"';
ctx.fillStyle = '#6B6C74';
ctx.textAlign = 'center';
ctx.fillText('송금 금액에 따른 보상 혜택', 600, 330);

// Rewards preview
ctx.font = '28px "Arial"';
ctx.fillStyle = '#1A1B22';
ctx.textAlign = 'left';
const rewards = [
  '💰 최대 iPad A16 실버',
  '🎁 100,000원 현금',
  '🏆 매일 업데이트되는 혜택'
];

let yPos = 400;
for (const reward of rewards) {
  ctx.fillText(reward, 150, yPos);
  yPos += 60;
}

// Logo/branding bottom
ctx.font = 'bold 24px "Arial"';
ctx.fillStyle = '#0082FF';
ctx.textAlign = 'center';
ctx.fillText('www.themoin.com', 600, 600);

// Save to file
const buffer = canvas.toBuffer('image/png');
fs.writeFileSync('/Users/seonah/promotion-leaderboard/og-image.png', buffer);
console.log('✅ OG image created: og-image.png');
