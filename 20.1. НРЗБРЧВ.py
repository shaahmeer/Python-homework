translatedText = 'двтльнй фкт н ткст н зк НРЗБРЧВ кзвтс двльн прст чтть Дсттчн нбльшй трнрвк в смжт т длть'

def translate(text):
    global translatedText
    redLetter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if redLetter.count(text[i]) == 0:
            translatedText = translatedText + text[i]
    translatedText = ' '.join(translatedText.split())
    return translatedText

print(translate(""))