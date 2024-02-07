from collections import Counter

import pyautogui
import pynput

pyautogui.PAUSE = 0.3

points = [(840, 520), (950, 520), (1060, 520), (840, 630), (950, 630), (1060, 630)]


def run(key):
    try:
        if key.char == 's':
            colors = []

            for x, y in points:
                colors.append(pyautogui.pixel(x, y))

            counts = Counter(colors)
            different_color = min(counts, key=counts.get)

            pyautogui.moveTo(*points[colors.index(different_color)])
            pyautogui.click()

    except AttributeError:
        if key == pynput.keyboard.Key.esc:
            return False


with pynput.keyboard.Listener(on_press=run) as listener:
    listener.join()
