import pyautogui
from time import sleep
import keyboard
import sys

x, y = 1486, 904
print("Нажми на 'q', чтобы выйти из программы")


while True:
    color = pyautogui.pixel(x, y)
    if color != (242, 242, 242):
        keyboard.press_and_release('space')
        print("Пробел нажат!")
    print("Цвет пикселя:", color)
    def my_action():
        print("Выход из программы")
        sys.exit(1)


    keyboard.add_hotkey('q', my_action)
