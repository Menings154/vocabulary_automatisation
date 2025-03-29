import screenshots, text_recognition, index_cards, anki
import os, glob, googletrans

voc_translated = {}
vocabulary = set()

# create the screenshots
screenshots.del_all_images_in_dir(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots")
# screenshots.open_edge() # shows most recently opened book
screenshots.open_chrome()
screenshots.make_screenshots()
screenshots.close_edge()

# recognize the text in the screenshots
img_list = glob.glob(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\images\temporary screenshots\*.png")
for img in img_list:
    text_list = text_recognition.img_to_text(img)
    for text in text_list:
        words = text_recognition.extract_words(text)
        vocabulary.update(words)

# translate into german and make a dictionary where the keys are the english words and the values the german translation
translator = googletrans.Translator()
for word in vocabulary:
    translation = translator.translate(word, dest='de').text
    translation = translation.replace('ß', 'sz')
    translation = translation.replace('Ü', 'Ue')
    translation = translation.replace('Ä', 'Ae')
    translation = translation.replace('Ö', 'Oe')
    translation = translation.replace('ü', 'ue')
    translation = translation.replace('ä', 'ae')
    translation = translation.replace('ö', 'oe')

    voc_translated[word] = translation

# create index_cards
# index_cards.open_cartigo()
# for key in voc_translated.keys():
#     index_cards.add_card(word_en=key, word_de=voc_translated[key])
# screenshots.close_edge()

# save as a txt
anki.append_voc_to_data(voc_translated)
print(voc_translated)