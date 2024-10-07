import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy3

with open('test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokens = word_tokenize(text)
stop_words = set(stopwords.words('russian'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

filtered_text = ' '.join(filtered_tokens)
filtered_text = filtered_text.replace(",", "").replace(".", "")

tokens = word_tokenize(filtered_text, language='russian')
morph = pymorphy3.MorphAnalyzer()

for token in tokens:
    p = morph.parse(token)[0]
    print(f"Слово: {token}, Лемма: {p.normal_form}, Часть речи: {p.tag.POS}, Падеж: {p.tag.case}")

