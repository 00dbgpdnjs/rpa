from subprocess import check_call
import pyautogui

# # win+shift+s -> Cut the file tap -> Open a memo pad ->  Paste -> Click 자르기 -> Save to file_menu.png
# file_menu = pyautogui.locateOnScreen("file_menu.png") # func: Find the img on screen and return info
# print(file_menu) # If there isn't, "None" is printed
# pyautogui.click(file_menu) # If same images, click the first found one.


# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)


# # When there are multiple identical images, it is clicked one by one by using this func.
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

#----------------------------------------------------
# < advanced - How to speed up >
# It takes a long time because it's looking from top to right.

# # 1. grayscale : Change your image to black and white and compare. (speed 30% up, accuracy dowun)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# # 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1559, 872, 1919 - 1559, 1035 - 872)) # (x,y,width, height)
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
# Starting coordinates : 1559,872
# Ending coordinates : 1919,1035

# 3. Accuracy adjustment. 
# Even if the pixels don't match 100% with the img, computer recognize as the same image. 
# $ pip install opencv-python
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)

#----------------------------------------------------
# < advanced 2 - wait >
# If the target of automation is not immediately visible - Wait for the target to be recognized
# ex) Wait when opening a note pad

# 1. Before
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("Failed to find")

# 2. After
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("Failed to find")

# pyautogui.click(file_menu_notepad)

# 3. 일정 시간동안만 기다리기 : Time out
# import time
# import sys

# timeout = 5
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout:
#         print("Time's up")
#         sys.exit() # End of this py program.

# pyautogui.click(file_menu_notepad)

# 4. 함수로 정리
import time
import sys

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break # Return "target" to None
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 3)