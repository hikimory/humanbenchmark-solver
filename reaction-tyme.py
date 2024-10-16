import pyautogui, sys
from time import sleep

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

sleep(5)
for i in range(5):
    pyautogui.click(0, 167, button="left")
    while True:
        if pyautogui.pixelMatchesColor(1100, 293, (75, 219, 106)):
            pyautogui.click(0, 167, button="left")
            break
    sleep(0.1)