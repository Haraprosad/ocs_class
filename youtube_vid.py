import pyautogui,time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.typewrite("chrome",0.5)
pyautogui.press("enter")
time.sleep(4)
pyautogui.typewrite("www.youtube.com\n")
time.sleep(14)
pyautogui.moveTo(698,162,0.5)
time.sleep(3)
pyautogui.click()
time.sleep(3)
pyautogui.typewrite("sotyi bolchi tomake r valobashi na\n",0.5)
time.sleep(5)

pyautogui.moveTo(565,301,0.5)
pyautogui.click()

## to get cursor position after 4 seconds
#time.sleep(4)
#print(pyautogui.position())
