import pyautogui
import time
import random

time.sleep(3)

file = open('spam_text.txt', 'r').read()
file = file.splitlines()

for _ in range(50):
    pyautogui.typewrite(random.choice(file))
    pyautogui.press('enter')
    time.sleep(0.2)
