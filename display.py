#!/usr/bin/env python3
from settings import is_executable, display_width, display_height
from time import sleep, localtime, strftime
from psutil import virtual_memory, net_if_addrs, cpu_percent

from ST7789 import ST7789

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def init_display():
  disp = ST7789(
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    width=240,
    height=240,
    rotation=90,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0
  )
  disp.begin()

  return disp

def text_display():
  VM = virtual_memory()
  NET = net_if_addrs()
  WLAN = NET.get("wlan0")[0]
  TEMP_COMMAND_RESULT = int(open('/sys/class/thermal/thermal_zone0/temp').read())

  IP = "IP: " + str(WLAN.address)
  CPU = "Uso de CPU: " + str(cpu_percent()) + "%"
  RAM = "Uso de RAM: " + str(VM.percent) + "%"
  TEMP = "Temp: " + str(TEMP_COMMAND_RESULT / 1000) +"°C"
  TIME = strftime("%d/%m/%y %H:%M:%S", localtime())

  img = Image.new('RGB', (display_width, display_height), color=(0, 0, 0))

  draw = ImageDraw.Draw(img)

  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)

  font_datetime = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

  draw.rectangle((0, 0, display_width, display_height), (0, 0, 0))
  draw.text((5, 1), IP, font=font, fill=(255, 255, 255))
  draw.text((5, 31), CPU, font=font, fill=(255, 255, 255))
  draw.text((5, 61), RAM, font=font, fill=(255, 255, 255))
  draw.text((5, 91), TEMP, font=font, fill=(255, 255, 255))
  draw.text((5, 220), TIME, font=font_datetime, fill=(255, 255, 255))
  return img


def empty_display():
  img = Image.new('RGB', (display_width, display_height), color=(0, 0, 0))

  ImageDraw.Draw(img)
  return img

def draw_display(fn: function, disp):
  img = fn()
  disp.display(img)


def main():
  # Create instance and initialize display
  disp = init_display()

  while True:
    if is_executable: 
      draw_display(text_display, disp)
      sleep(1)
    else: 
      draw_display(empty_display, disp)
      sleep(5)

      main()