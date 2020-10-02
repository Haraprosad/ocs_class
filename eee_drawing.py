import pyautogui,time
time.sleep(5)
pyautogui.click()

armLength = 100;

#  EEE drawing
n = 3
while n>0:
    pyautogui.drag(armLength,0,duration= 0.1)
    pyautogui.move(-armLength,0,duration= 0.1)
    pyautogui.drag(0,armLength,duration= 0.1)
    pyautogui.drag(armLength,0,duration= 0.1)
    pyautogui.move(-armLength,0,duration= 0.1)
    pyautogui.drag(0,armLength,duration=0.1)
    pyautogui.drag(armLength,0,duration= 0.1)
    pyautogui.move(20,-armLength*2,duration=0.2)
    n = n-1;

