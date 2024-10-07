import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy3
from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
    )

with open('test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokens = word_tokenize(text)
stop_words = set(stopwords.words('russian'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

filtered_text = ' '.join(filtered_tokens)
# filtered_text = filtered_text.replace(",", "").replace(".", "")

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

doc = Doc(filtered_text)

doc.segment(segmenter)
leng = len(doc.sents)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)
# print(doc.tokens[:5])

for i in range(0, leng):
    try:
        print(i)
        doc.sents[i].syntax.print()
    except ValueError as e:
        print("Error")
