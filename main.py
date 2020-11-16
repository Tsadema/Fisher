import pyautogui
import time

time.sleep(5)

while True:
    x = 0
    while x < 11:
        pyautogui.write('%f')
        pyautogui.press("enter")
        time.sleep(3.5)
        x += 1
    pyautogui.write('%sell all')
    pyautogui.press("enter")
