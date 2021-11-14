import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")



# pyautogui.mouseInfo() # -> 34,585 58,168,242 #3AA8F2

# pixel = pyautogui.pixel(34, 585) # (x,y)
# print(pixel) # >> (58, 168, 242) ; rgb of (24, 585) coordinates

print(pyautogui.pixelMatchesColor(34, 585, (58, 168, 242))) # >> True ; The pixel[34, 585] matches with the rgb?