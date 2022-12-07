from translate import Translator

def Translate(input, lang1, lang2):
    languages = {'Русский': 'Russian', 'Английский': 'English', 'Немецкий': 'German'}
    for key, value in languages.items():
        if key == lang1:
            lang1 = value
        if key == lang2:
            lang2 = value
    translator = Translator(from_lang=lang1, to_lang=lang2)
    Translation = translator.translate(input)
    new_input = input.capitalize()
    return Translation

def handle_file(file):
    strng = ''
    for chunk in file.chunks():
        strng += str(chunk)
    return str(strng[2:-1])