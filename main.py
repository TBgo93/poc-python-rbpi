import threading
import signal
import sys
import subprocess
import RPi.GPIO as GPIO
import settings

from time import sleep

from display import init_display, empty, draw_display, stats, power_off
from buttons import handle_button, BUTTONS

# Init global vars
settings.init()

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

exit_event = threading.Event()

def signal_handler(signum, frame):
  # Create instance and initialize display
  disp = init_display()
  # Draw display
  draw_display(empty, disp)

  exit_event.set()
  sys.exit(1)


signal.signal(signal.SIGINT, signal_handler)

# Handle buttons
for pin in BUTTONS:
  GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)

def main():
  # Create instance and initialize display
  disp = init_display()

  while True:
    if settings.shutdown:
      draw_display(power_off, disp)
      sleep(3)
      draw_display(empty, disp)
      subprocess.run(["sudo", "shutdown", "-h", "now"]) 
      break

    if settings.is_executable: 
      draw_display(stats, disp)
      sleep(1)
    else: 
      draw_display(empty, disp)
      sleep(5)

      main()

t = threading.Thread(target=main)
t.start()
t.join()
