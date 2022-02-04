import screenshots, text_recognition
import os, glob

# create the screenshots
screenshots.del_all_images_in_dir(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots")
screenshots.open_edge() # shows most recently opened book
screenshots.make_screenshots()
screenshots.close_edge()

# recognize the text in the screenshots
vocabulary = set()

img_list = glob.glob(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots\*.png")
for img in img_list:
    text_list = text_recognition.img_to_text(img)
    for text in text_list:
        words = text_recognition.extract_words(text)
        vocabulary.update(words)

print(vocabulary)