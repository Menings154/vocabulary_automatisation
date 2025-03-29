import pyautogui
import time
import webbrowser
import os
import glob

#TODO sleeptime may be optimized

# delete all images from before
def del_all_images_in_dir(dir_path: str) -> None:
    image_list = glob.glob(dir_path+r"\*.png")
    for image in image_list:
        os.remove(image)

# go in browser and open site
def open_edge():
    edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open('https://read.amazon.com/notebook')
    time.sleep(1)

def close_edge():
    pyautogui.hotkey('ctrl', 'w')

def open_chrome():
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('https://read.amazon.com/notebook')
    time.sleep(1)

# die ersten 2 punkte erstmal überlegen wie ich spezielles buch einfügen lann

# screenshot to be used to detect if end of page

def make_screenshots():
    time.sleep(5)
    pyautogui.click(1000, 500)
    pyautogui.press('end')
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(5)
    full_screen = pyautogui.screenshot(region=(0,0, 1900, 1000))
    full_screen.save(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\bottom_screen.png")
    time.sleep(1)
    pyautogui.press('home')
    time.sleep(1)

    i = 0
    while True:
        # locate on screen
        for pos in pyautogui.locateAllOnScreen(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\brown.png"): #, confidence=0.9):
            i += 1
            # take image and save in folder
            im = pyautogui.screenshot(region=(pos.left+pos.width, pos.top, 300, pos.height))
            im.save(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots\_" + str(i) + r".png")

        # next screen
        pyautogui.click(1000, 500)
        pyautogui.press('pagedown')
        time.sleep(1)
        temp_image = pyautogui.locateOnScreen(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\bottom_screen.png")
        if temp_image != None:  # stop if at bottom of page
            break

