from googletrans import Translator

translator = Translator()
text = "Replace with your english text"  # Replace with your English text
translated = translator.translate(text, dest='vi')
print(translated.text)