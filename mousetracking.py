import pyautogui
import time
green_rgb = (75, 219, 106)
tolerance = 30
click_cooldown = 1
poll_rate = 0.1
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}")

        if pyautogui.pixelMatchesColor(
            x,y,green_rgb, tolerance=tolerance
        ):
            pyautogui.click(x,y)
            print(f"CLicked at: {x}, {y}")
            time.sleep(click_cooldown)
        time.sleep(poll_rate)
except KeyboardInterrupt:
    print("\nStopped")