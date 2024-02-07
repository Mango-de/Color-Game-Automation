from collections import Counter

import pynput
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.realtimecolors.com/game')


def on_press(key):
    if key == pynput.keyboard.Key.esc:
        browser.quit()
        exit()


listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

while True:
    elems = browser.find_elements(By.CLASS_NAME, 'square')
    colors = list(map(lambda elem: elem.get_attribute('style'), elems))

    counts = Counter(colors)
    different_color = min(counts, key=counts.get)

    elems[colors.index(different_color)].click()
