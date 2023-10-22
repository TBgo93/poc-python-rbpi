#!/usr/bin/env python3
import ST7789
import RPi.GPIO as GPIO
import threading

from time import sleep, localtime, strftime
from psutil import virtual_memory, net_if_addrs, cpu_percent
from sys import exit

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_button(pin):
  label = LABELS[BUTTONS.index(pin)]

  if label == "X":
    print("RemoteControl: X")
  if label == "Y":
    print("RemoteControl: Y")
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")

def init_display():
  return ST7789.ST7789(
    height=240,
    width=240,
    rotation=90,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0
  )

def display_text(WIDTH, HEIGHT):
  VM = virtual_memory()
  NET = net_if_addrs()
  WLAN = NET.get("wlan0")[0]
  TEMP_COMMAND_RESULT = int(open('/sys/class/thermal/thermal_zone0/temp').read())

  IP = "IP: " + str(WLAN.address)
  CPU = "Uso de CPU: " + str(cpu_percent()) + "%"
  RAM = "Uso de RAM: " + str(VM.percent) + "%"
  TEMP = "Temp: " + str(TEMP_COMMAND_RESULT / 1000) +"°C"
  TIME = strftime("%d/%m/%Y %H:%M:%S", localtime())

  img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

  draw = ImageDraw.Draw(img)

  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)

  font_datetime = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

  draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))
  draw.text((5, 1), IP, font=font, fill=(255, 255, 255))
  draw.text((5, 31), CPU, font=font, fill=(255, 255, 255))
  draw.text((5, 61), RAM, font=font, fill=(255, 255, 255))
  draw.text((5, 91), TEMP, font=font, fill=(255, 255, 255))
  draw.text((5, 220), TIME, font=font_datetime, fill=(255, 255, 255))
  return img

def display_empty():
  # Create instance
  disp = init_display()

  # Initialize display.
  disp.begin()

  WIDTH = disp.width
  HEIGHT = disp.height
  img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

  ImageDraw.Draw(img)
  disp.display(img)


def main():
  # Handle buttons
  for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)

  # Create instance
  disp = init_display()

  # Initialize display.
  disp.begin()

  WIDTH = disp.width
  HEIGHT = disp.height

  while True:
    img = display_text(WIDTH, HEIGHT)
    disp.display(img)
    sleep(1)

exit_event = threading.Event()

try:
  t = threading.Thread(target=main)
  t.start()
  t.join()
except (KeyboardInterrupt, SystemExit):
  print("[*] Exiting...")
  display_empty()
  exit_event.set()
  exit(1)
