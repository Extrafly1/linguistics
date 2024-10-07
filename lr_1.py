import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open('test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokens = word_tokenize(text)
stop_words = set(stopwords.words('russian'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("Оригинальные токены:", tokens)
print("Токены без стоп-слов:", filtered_tokens)
