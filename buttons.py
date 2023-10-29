import settings

BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

def handle_button(pin):
  index = BUTTONS.index(pin)
  label = LABELS[index]

  if label == "X":
    print("X: Display on/off")
    settings.is_executable = not settings.is_executable
  if label == "Y":
    print("RemoteControl: Y")
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")
