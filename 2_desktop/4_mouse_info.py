import pyautogui

# pyautogui.mouseInfo() # ❗❗ KEY CODE ❗❗ Open the mouseinfo window. Move the mouse and press F1 and ctrl+v. Then "798,693 30,30,30 #1E1E1E" will be. 앞에 두 개는 좌표이고 세개는 rgb



# If you want to finish automation in the middle, move your cursor to one of the four corners of the screen. : fail-safe ❗❗ KEY CODE ❗❗
# How to turn off fail-safe : "pyautogui.FAILSAFE = False"  but most people don't use it
pyautogui.PAUSE = 1 # Apply sleep for 1 second to every move. Instead of sleep() below
for i in range(5):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)