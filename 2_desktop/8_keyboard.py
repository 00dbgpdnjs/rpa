# Typing Auto.
# automatetheboringstuff.com -> chapter 20

import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# 1. num or eng
# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25) # 2nd arg : For each letter.

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.4)
# Write t e s t, press the left rudder twice, ...


# 2. Special characters : shift + 4 -> $
# pyautogui.keyDown("shift")
# pyautogui.press("4") # pyautogui.keyDown("4") + pyautogui.keyUp("4")
# pyautogui.keyUp("shift")

# 3. 조합키 (Hot Key) : ctrl + a
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 3-1. more convenient method
# pyautogui.hotkey("ctrl", "alt", "shift", "a") # keyDown from the start and keyup from the end
# pyautogui.hotkey("ctrl", "a")

# 4. kor
# $ pip install pyperclip
import pyperclip
# pyperclip.copy("나도코딩") # Save "나도코딩" on the cliboard.
# pyautogui.hotkey("ctrl", "v") # Paste the contents of the clipboard

# 4-1. more conveninet way
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 5. Terminate the auto program.
# win : ctrl + alt + del