import pyautogui
from time import sleep
import keyboard

x, y = 1486, 904
running = True

def exit_handler():
    global running
    print("Exiting program")
    running = False

keyboard.add_hotkey('q', exit_handler)
print("Press 'q' to exit")

def is_target(color, target=(242, 242, 242), tol=5):
    return all(abs(a - b) <= tol for a, b in zip(color, target))

while running:
    color = pyautogui.pixel(x, y)
    if not is_target(color):
        keyboard.press_and_release('space')
        print("Space pressed!")
    else:
        print("Pixel color:", color)
    sleep(0.02)