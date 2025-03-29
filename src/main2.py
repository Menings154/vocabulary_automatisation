import scrapping, voc_helper, text_recognition, ankitest

new_voc_all = set()
all_notes = scrapping.scrap_notes()

voc_notes = scrapping.sort_notes(all_notes, "orange")
for note in voc_notes:
    temp = ''
    for word in text_recognition.extract_words(note):
        temp += str(word)
        temp += ' '
    new_voc_all.add(temp[:-1])

total_voc = voc_helper.vocabulary()
new_voc = total_voc.check_new_words(new_voc_all)

new_voc_translated, problemlist = voc_helper.tanslate_vocabulary(new_voc)
print("This could not be translated", problemlist)
total_voc.save_vocabulary(new_voc)

# chekc ob es deutsche worte sind, deren bedeutung ich einfach nicht kenne

ankitest.create_flash_cards("Vokabeln", new_voc_translated)

print("Conclusion:")
print("All notes: ", len(all_notes))
print("voc_notes: ", len(voc_notes))
print("new voc:" , len(new_voc))
print("new voc translated:" , len(new_voc_translated))
print("problemlist:" , len(problemlist),)
print(problemlist)