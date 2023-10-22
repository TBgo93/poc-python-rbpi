BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

def handle_button(pin):
  label = LABELS[BUTTONS.index(pin)]

  if label == "X":
    print("X: Power OFF")
  if label == "Y":
    print("Y: Reboot")
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")
