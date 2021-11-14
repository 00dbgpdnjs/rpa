# Automate windows 
# ex) Find out where the program [calculator] is currently.
# And automation to coordinates based on the program [calculator] location.
# ex) Click "3".

import pyautogui

# fw = pyautogui.getActiveWindow() # fw : forground(??) window ; 활성화된 윈도우 / The func : 현재 활성화된 창 (VSCode)
# print(fw.title) # The title at the top of VSCode is printed.
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20) # Wherever VSCode is, its icon will be clicked



# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 제목에 "제목 없음" 이라는 텍스트가 들어간 창 얻기 
print(w)
if w.isActive == False:
    w.activate() # Activation; Bring it to the front.

# if w.isMaximized == False:
#     w.maximize()

if w.isMinimized == False: # 창이 내려져 있을 때 ; 작을 때가 아니라
    w.minimize()

pyautogui.sleep(1)

w.restore() # 복원

w.close()