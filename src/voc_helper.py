import googletrans

def tanslate_vocabulary(vocabulary):
    voc_translated = {}
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

    return voc_translated

class vocabulary:
    def __init__(self):
        self.all_vocs = self.load_vocabulary()
    
    def load_vocabulary(self):
        path = r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\voclist\vocabulary2.txt"
        all_vocs = set()
        with open(path, 'r') as file:
            for line in file:
                line = line.strip('\n')
                all_vocs.add(line)
        return all_vocs

    def check_new_words(self, voc_new):
        return voc_new-self.all_vocs 


