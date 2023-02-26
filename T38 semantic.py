import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("")

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
cat and monkey are similar as they are both animals
monkey and banana are similar since monkey each banana
banana and cat have low similarity since they have little connection
"""

# example of my own
print(nlp("food").similarity(nlp("water")))
print("")

"""
comparison between en_core_web_sm and en_core_web_md

en_core_web_md is more advanced hence gives more accurate similarity scores
en_core_web_sm is a small model  which don't ship with word vectors and is therefore not so good with sentences
"""
