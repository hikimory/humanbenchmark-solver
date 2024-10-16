import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image
from time import sleep

sleep(4)
pyautogui.click(955, 610)
words = []
for i in range(100):
    sleep(0.5)
    screen = pyautogui.screenshot(region=(430, 430, 1030, 80))
    screen.save('my_verbal.png')
    img2 = cv2.imread('my_verbal.png')
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh_img = Image.fromarray(thresh)
    thresh_img.save('my_verbal2.png')
    word = pytesseract.image_to_string(thresh, config='--psm 6', lang='eng') 
    # print(word)
    # sleep(4)
    if word in words:
        pyautogui.click(890, 550)
    else:
        words.append(word)
        pyautogui.click(1025, 550)
