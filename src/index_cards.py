import webbrowser
import time
import pyautogui

def open_cartigo():
    edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open('https://cartigo.de/platform/login')
    time.sleep(3)

    pyautogui.moveTo(x=962, y=838)
    time.sleep(1)
    pyautogui.mouseDown(x=962, y=838, duration=0.1)  # click on "login", weis nicht warum da ssolche probleme macht
    pyautogui.mouseUp()
    #time.sleep(1)
    #pyautogui.click(x=962, y=838)
    time.sleep(1)
    pyautogui.click(x=959, y=349)  # click on "bücher"
    time.sleep(1)
    pyautogui.click(x=1435, y=833)  # click on "neue Karte"


def add_card(word_en: str, word_de: str) -> str:
    def write_on_card(word: str) -> None:
        pyautogui.moveTo(x=898, y=665, duration=0.1)
        pyautogui.mouseDown(x=898, y=665, duration=1)
        pyautogui.mouseUp()
        time.sleep(0.1)
        for letter in word:
            pyautogui.press(letter)
            time.sleep(0.1)
    
    write_on_card(word=word_en)
    pyautogui.click(x=961, y=872)  # turn card
    time.sleep(0.1)
    write_on_card(word=word_de)
    
    pyautogui.click(x=1836, y=840)  # save
    time.sleep(1)

