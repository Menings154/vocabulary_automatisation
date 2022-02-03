import pyautogui
import time
import webbrowser

# time.sleep(5)
# print(pyautogui.position())
# time.sleep(5)
# print(pyautogui.position())
# im = pyautogui.screenshot()
# im.show()

# im = pyautogui.screenshot(region=(511, 561, 12, 42))

#im.save(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\brown.png")

# delete all images from before
# go in browser and open site
# edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
# webbrowser.get('edge').open('https://read.amazon.com/notebook')
# die ersten 2 punkte erstmal überlegen wie ich spezielles buch einfügen lann

# locate on screen
i = 0
for pos in pyautogui.locateAllOnScreen(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\brown.png"): #, confidence=0.9):
    i += 1
    # take image and save in folder
    im = pyautogui.screenshot(region=(pos.left, pos.top, 300, pos.height))
    im.save(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots\_" + str(i) + r".png")


# repeat until all found
# press "Seite down"
# repeat until finished
