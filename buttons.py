BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

def handle_button(pin):
  global is_executable
  index = BUTTONS.index(pin)
  label = LABELS[index]

  if label == "X":
    print("X: Off display")
    is_executable = False
  if label == "Y":
    print("Y: On display")
    is_executable = True
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")
