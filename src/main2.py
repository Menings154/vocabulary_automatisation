import scrapping

import screenshots, text_recognition, index_cards, anki
import os, glob, googletrans

voc_translated = {}
vocabulary = set()

all_notes = scrapping.scrap_notes()
vocabulary = scrapping.sort_notes(all_notes, "orange")


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