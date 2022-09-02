import pyautogui
import keyboard
import time

def functionMain():
        count = 1
        while keyboard.is_pressed('c') == False:
                #count = file.read()
                count = count + 1
                print(count)
                time.sleep(3)
                #CAPTURA POSIÇÃO
                positionSend = pyautogui.locateOnScreen('send.png', grayscale=True,confidence=0.8)
                positionCenter = pyautogui.center(positionSend)
                pyautogui.click(positionCenter.x,positionCenter.y)
                time.sleep(1)

functionMain()
