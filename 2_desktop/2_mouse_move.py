import pyautogui

# # Move the mouse to the absolute coordinates.
# pyautogui.moveTo(200, 100)
# pyautogui.moveTo(100, 200, duration=3) # Move for 3s

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)


p = pyautogui.position() # obj which get the curr curser pos
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y


# # Move the mouse to the relative coordinates; from the curr location of the cursor
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25) # +100, +100
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())