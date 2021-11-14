# < curr time > 
import time
print(time.strftime('%d-%b-%Y')) # f: format /  %a - 요일, %b - 월

# < specific date >
import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d") # p : parse / 뒤의 형태로 앞의 형태를 분석해서 객체를 만듬
print(type(dt))
print(dt.strftime('%d-%b-%Y'))