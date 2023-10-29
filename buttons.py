BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']

isExecutable = False

def handle_button(pin):
  global isExecutable
  index = BUTTONS.index(pin)
  label = LABELS[index]

  if label == "X":
    print("X: Off display")
    isExecutable = False
  if label == "Y":
    print("Y: On display")
    isExecutable = True
  if label == "A":
    print("RemoteControl: A")
  if label == "B":
    print("RemoteControl: B")
