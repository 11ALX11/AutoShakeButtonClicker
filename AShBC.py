import pyautogui
from pyscreeze import Point


def main():
    pyautogui.PAUSE = 0.2
    pyautogui.FAILSAFE = True

    print("Looking for shake.png... (move mouse to 1 of 4 screen corners to turn off script)")

    coords: Point
    while True:
        try:
            pyautogui.failSafeCheck()
            coords = pyautogui.locateCenterOnScreen("shake.png", grayscale=True, confidence=0.8)
            pyautogui.click(coords.x, coords.y)

        except pyautogui.ImageNotFoundException:
            pass
        except pyautogui.FailSafeException as err:
            print(err)
            break


if __name__ == '__main__':
    main()
