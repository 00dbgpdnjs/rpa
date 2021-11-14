import sys
import pyautogui
import pyperclip

# 1번 구현

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2) # Opening / If IndexError, Adjust time

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized == False:
    window.maximize()

# 2번 구현
# 2-1. 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png") # 못 찾으면 confidence 주기
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 2-2. 흰 영역 
pyautogui.click(200, 200, duration=0.5)

# another way : 글자크기 바꾸는 자동화는 안에 숫자가 달라지니까 그걸 캡쳐하면 컴퓨터가 못 찾으므로 이렇게 상대적으로 찾아야함
# btn_brush = pyautogui.locateOnScreen("btn_brush.png")
# pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 3번 구현
pyautogui.sleep(5)

window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음