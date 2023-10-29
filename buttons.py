BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

def handle_button(pin):
  index = BUTTONS.index(pin)
  label = LABELS[index]

  if label == "X":
    print("X: Off display")
    return False
  if label == "Y":
    print("Y: On display")
    return True
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")
