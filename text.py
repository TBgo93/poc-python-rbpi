#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from ST7789 import ST7789


MESSAGE = "Hello World!"

# Create ST7789 LCD display class.

disp = ST7789(
  height=240,
  width=320,
  rotation=90,
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

while True:
  draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
  draw.text((0, 0), MESSAGE, font=font, fill=(255, 255, 255))
  disp.display(img)
