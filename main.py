from googletrans import Translator
while True:
    sentence = input("--> ")
    translator = Translator()
    result = translator.translate(sentence, src = "en", dest = "ne")
    print(result.text)