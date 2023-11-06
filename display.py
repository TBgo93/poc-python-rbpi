#!/usr/bin/env python3
import settings
from time import localtime, strftime
from psutil import virtual_memory, net_if_addrs, cpu_percent

from ST7789 import ST7789

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


FONT_TEXT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
FONT_DATETIME = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
COLOR_TEXT = (255, 255, 255)
COLOR_BG = (0, 0, 0)

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

def stats():
  VM = virtual_memory()
  NET = net_if_addrs()
  WLAN = NET.get("wlan0")[0]
  TEMP_COMMAND_RESULT = int(open('/sys/class/thermal/thermal_zone0/temp').read())

  IP = "IP: " + str(WLAN.address)
  CPU = "Uso de CPU: " + str(cpu_percent()) + "%"
  RAM = "Uso de RAM: " + str(VM.percent) + "%"
  TEMP = "Temp: " + str(TEMP_COMMAND_RESULT / 1000) +"°C"
  TIME = strftime("%d/%m/%y %H:%M:%S", localtime())

  img = Image.new('RGB', (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT), color=COLOR_BG)
  draw = ImageDraw.Draw(img)

  draw.rectangle((0, 0, settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT), COLOR_BG)
  draw.text((5, 1), IP, font=FONT_TEXT, fill=COLOR_TEXT)
  draw.text((5, 31), CPU, font=FONT_TEXT, fill=COLOR_TEXT)
  draw.text((5, 61), RAM, font=FONT_TEXT, fill=COLOR_TEXT)
  draw.text((5, 91), TEMP, font=FONT_TEXT, fill=COLOR_TEXT)
  draw.text((5, 220), TIME, font=FONT_DATETIME, fill=COLOR_TEXT)

  return img

def empty():
  img = Image.new('RGB', (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT), color=COLOR_BG)
  ImageDraw.Draw(img)

  return img

def power_off():
  img = Image.new('RGB', (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT), color=COLOR_BG)
  draw = ImageDraw.Draw(img)

  draw.rectangle((0, 0, settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT), COLOR_BG)
  draw.text((5, 91), "The system will", font=FONT_TEXT, fill=COLOR_TEXT)
  draw.text((5, 111), "power off now!", font=FONT_TEXT, fill=COLOR_TEXT)

  return img

def draw_display(fn, disp):
  img = fn()
  disp.display(img)
