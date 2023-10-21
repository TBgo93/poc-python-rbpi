#!/usr/bin/env python3
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from ST7789 import ST7789


MESSAGE = "Hello World!"

# Create ST7789 LCD display class.

disp = ST7789(
  height=240,
  width=320,
  rotation=180,
  port=0,
  cs=1,
  dc=9,
  backlight=13,
  spi_speed_hz=60 * 1000 * 1000,
  offset_left=0,
  offset_top=0
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

size_x, size_y = draw.textsize(MESSAGE, font)

text_x = disp.width
text_y = (disp.height - size_y) // 2

t_start = time.time()

while True:
  x = (time.time() - t_start) * 100
  x %= (size_x + disp.width)
  draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
  draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
  disp.display(img)
