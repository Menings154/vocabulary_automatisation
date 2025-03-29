def append_voc_to_data(dic: dict) -> None:
    with open(r"C:\Users\Benja\Code\Python\vocabulary_automatisation\src\voclist\vocabulary.txt", "a") as file:
        for key in dic.keys():
                file.write(key)
                file.write("\t")
                file.write(str(dic[key]))
                file.write("\n")
    return