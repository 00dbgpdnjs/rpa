import pyautogui

# pyautogui.sleep(3) # To move the mouse to the place you want ; To print the pos of the cursor of the place you want with the code just below ; ex) pos of file tap  to click
# print(pyautogui.position())

# pyautogui.click(64, 17, duration=1) # Move to the coordinates [file tap] for 1s and click
# pyautogui.click() = pyautogui.mouseDown() + pyautogui.mouseUp() ; Can drag and drop or paint by using two codes seperately

# Two codes are same
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)



# pyautogui.sleep(3) # Open mspaint
# pyautogui.click(clicks=500) # You can move the mouse as this code is run

# Paint a straight line on mspaint
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()



# pyautogui.rightClick()
# pyautogui.middleClick()
# pyautogui.scroll(300) # 위로 +300



pyautogui.sleep(3) # Open a memo pad and put the cursor on top of the notepad.
print(pyautogui.position())
pyautogui.moveTo(1357, 65) # put the result of the code just above
# pyautogui.drag(100, 0) # +100
pyautogui.drag(100, 0, duration=0.25) # 컴퓨터가 동작 보다 빨라서 보통 0.25를 줌
# pyautogui.dragTo(1514, 349, duration=0.25) # Instead of the code just above, to move to the absolute coordinates.
