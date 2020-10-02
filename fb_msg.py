import pyautogui,time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.typewrite("chrome",0.5)
pyautogui.press("enter")
time.sleep(4)
pyautogui.typewrite("www.facebook.com\n")
time.sleep(14)

# #for liking the news feed's posts
# n =5
# while n>0:
#     pyautogui.press("j")
#     time.sleep(2)
#     pyautogui.press("l")
#     time.sleep(0.5)
#     pyautogui.press("tab")
#     time.sleep(0.5)
#     pyautogui.press("enter")
#     n = n-1

#for sending sms(multiple sms) to someone
pyautogui.press("q")
time.sleep(3)
pyautogui.typewrite("alauddin",0.5)
time.sleep(5)
pyautogui.press("down")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

n=5
while n>0:
    pyautogui.typewrite("Boss",0.5)
    time.sleep(1)
    pyautogui.press("enter")
    n = n-1



