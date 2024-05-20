from bhashini_translator import Bhashini
from dotenv import load_dotenv

load_dotenv()

def bhashini_translate(sourceLanguage, targetLanguage, text):
    bhashini = Bhashini( sourceLanguage,  targetLanguage)
    return bhashini.translate(text)

print(bhashini_translate('en','ka', 'Hello, How is your day?'))
