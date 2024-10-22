from time import sleep
import pyautogui


TIME_BETWEEN_SCREENSHOTS = 1


def main():
    pyautogui.PAUSE = TIME_BETWEEN_SCREENSHOTS
    pyautogui.FAILSAFE = True

    while True:
        print( pyautogui.locateOnScreen("shake.png") )



if __name__ == '__main__':
    main()
