import pyautogui, sys
from time import sleep

sleep(4)
pyautogui.click(950, 503)
for i in range(30):
    screen = pyautogui.screenshot(region=(443, 249, 1034, 534))
    for x in range(443, 1477, 70):
        for y in range(249, 783, 70):
            #                        center               color
            if screen.getpixel((x - 443, y - 249)) != (43, 135, 209):
                pyautogui.click(x, y)
                break