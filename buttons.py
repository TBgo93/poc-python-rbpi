import settings

BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

def handle_button(pin):
  index = BUTTONS.index(pin)
  label = LABELS[index]

  if label == "X":
    print("Y: Shutdown")
    settings.shutdown = True
  if label == "Y":
    print("Y: Reset")
    settings.reset = True
  if label == "A":
    print("A: Display on/off")
    settings.is_executable = not settings.is_executable
  if label == "B":
    print("RemoteControl: B")
