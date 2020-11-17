import pyautogui
import time

# Config
prefix = input("Prefix: ")

# Bee mode :)
if input == "activatebeemode":
    beemode = input("Do you want to activate bee mode? Y/N: ")
    if beemode == "y" or beemode == "Y":
        f = open("beemovie", "r")
        time.sleep(5)
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

# Config: the sequel
command = input("Command: ")
secondary = input("Secondary Command (Sell command or empty for none): ")
cooldown = float(input("Cooldown: "))
times = int(input("Amount (Times to execute command before secondary command): "))

# Warning before it starts
x = 5
while x > 0:
    time.sleep(1)
    print(f'Starting in {x}')
    x -= 1

# Program loop
while True:
    x = 0
    while x < times:
        pyautogui.write(command)
        pyautogui.press("enter")
        time.sleep(cooldown)
        x += 1
    pyautogui.write(secondary)
    pyautogui.press("enter")