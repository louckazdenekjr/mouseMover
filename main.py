import pyautogui
import time

while True:
    try:
        pyautogui.moveRel(-10, 0)
        pyautogui.moveRel(10, 0)
        time.sleep(2)
    except:
        print("An exception occurred")
