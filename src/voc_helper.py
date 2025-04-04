import googletrans

def tanslate_vocabulary(vocabulary):
    voc_translated = {}
    translator = googletrans.Translator()
    problem_list = []
    for word in vocabulary:
        try:
            translation = translator.translate(word, dest='de').text
            translation = translation.replace('ß', 'sz')
            translation = translation.replace('Ü', 'Ue')
            translation = translation.replace('Ä', 'Ae')
            translation = translation.replace('Ö', 'Oe')
            translation = translation.replace('ü', 'ue')
            translation = translation.replace('ä', 'ae')
            translation = translation.replace('ö', 'oe')

            voc_translated[word] = translation
        except:
            pass

    return voc_translated, problem_list

class vocabulary:
    def __init__(self):
        self.path = r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\voclist\vocabulary2.txt"
        self.all_vocs = self.load_vocabulary()
    
    def load_vocabulary(self):
        all_vocs = set()
        with open(self.path, 'r') as file:
            for line in file:
                line = line.strip('\n')
                all_vocs.add(line)
        return all_vocs

    def check_new_words(self, voc_new):
        return voc_new-self.all_vocs
    
    def save_vocabulary(self, new_voc):
        self.all_vocs = self.all_vocs|new_voc
        with open(self.path, 'w') as file:
            for word in self.all_vocs:
                file.write(word+'\n')
            file.close()


