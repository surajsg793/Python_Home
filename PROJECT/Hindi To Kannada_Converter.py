from googletrans import Translator

def translate_kannada_to_english(text):
    try:
        translator = Translator()
        translated = translator.translate(text, src='kn', dest='en')
        return translated.text
    except Exception as e:
        return str(e)

while True:
    input_text = input("Enter a Kannada sentence (or 'exit' to quit): ")
    
    if input_text.lower() == 'exit':
        break
    
    translated_text = translate_kannada_to_english(input_text)
    print("Translated to English:", translated_text)

