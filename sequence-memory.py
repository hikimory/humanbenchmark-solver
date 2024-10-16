import cv2
import numpy as np
import pyautogui
from time import sleep


def findCeters():
    screen = pyautogui.screenshot(region=(440, 275, 1037, 535))
    img = np.array(screen)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            return (cX, cY)
    return None

sleep(4)
pyautogui.click(950, 670)
sleep(1)
while True:
    centers = []
    while True:
        center = findCeters()
        if center is None:
            break; 
        if len(centers) == 0 or centers[-1] != center:
            centers.append(center)
    for x, y in centers:
        pyautogui.click(x + 440, y + 275)
    sleep(1.15)