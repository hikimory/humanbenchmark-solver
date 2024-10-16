import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image
from time import sleep

sleep(4)
pyautogui.click(955, 610)
while True:
    sleep(0.5)
    screen = pyautogui.screenshot(region=(340, 400, 1310, 510))
    screen.save('my_screenshot.png')
    img2 = cv2.imread('my_screenshot.png')
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh_img = Image.fromarray(thresh)
    thresh_img.save('my_screenshot2.png')
    text = pytesseract.image_to_string(thresh, config='--psm 6', lang='eng') 
    print(text)
    sleep(20)
    pyautogui.moveTo(950, 470)
    pyautogui.click()
    pyautogui.write(text)
    pyautogui.click(950, 541)
    sleep(3)
    pyautogui.click(956, 616)
