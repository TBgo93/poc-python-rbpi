import threading
import signal
import sys
import RPi.GPIO as GPIO

from display import display_empty, main
from buttons import handle_button, BUTTONS, isExecutable

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

exit_event = threading.Event()

def signal_handler(signum, frame):
  display_empty()
  exit_event.set()
  sys.exit(1)

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)

  # Handle buttons
  for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)
  print(isExecutable)
  t = threading.Thread(target=main, args=[isExecutable])
  t.start()
  t.join()
