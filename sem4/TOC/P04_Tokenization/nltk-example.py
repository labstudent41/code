import nltk
# nltk.download('punkt')

text = '''
He TOC che practical aahe.
Amhi nltk waparto.
'''
print(nltk.word_tokenize(text))
print(nltk.line_tokenize(text))

text = '''
This is a sentence in english.
This can be written
in multiple lines
but must end with
a full stop.
'''

english = nltk.data.load('tokenizers/punkt/english.pickle')
print(english.tokenize(text))

# Shrimati mam is a nice teacher. She can teach anything and everything.
german_text = "Shrimati Mam ist eine nette Lehrerin. Sie kann alles und jedes unterrichten."
german = nltk.data.load('tokenizers/punkt/german.pickle')
print(english.tokenize(german_text))
