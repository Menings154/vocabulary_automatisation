import scrapping, voc_helper, text_recognition

import  text_recognition, index_cards, anki
import os, glob, googletrans


all_notes = scrapping.scrap_notes()

new_voc_all= set([text_recognition.extract_words(word) for word in scrapping.sort_notes(all_notes, "orange")])

total_voc = voc_helper.vocabulary()
new_voc = total_voc.check_new_words(new_voc_all)

new_voc_translated = voc_helper.tanslate_vocabulary(new_voc)

total_voc.save_vocabulary(new_voc)

# chekc ob es deutsche worte sind, deren bedeutung ich einfach nicht kenne

# save as a txt
#anki.append_voc_to_data(voc_translated)
#print(voc_translated)