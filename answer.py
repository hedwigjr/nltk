import nltk
import re 
import urllib.request

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


text = urllib.request.urlopen('https://inlnk.ru/xv8mdX')
text = text.read().decode('utf-8')
tokens = word_tokenize(text=re.sub(r'[^\w\s]','', text))

data = []
for sent in tokens:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

#Существительное
Nouns= ['NN', 'NNP', 'NNPS', 'NNS']
nouns_output = 0

#Прилагательное
Adjectives= ['JJ', 'JJR', 'JJS']
Adjectives_output = 0

#Глаголы
Verbs= ['VB','VBP', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
Verbs_output = 0

#Наречия
Adverbs= ["RBR", "RBS"]
Adverbs_output = 0

#Междометия
Interjections= ['IN']
Interjections_output = 0

#Предлоги
Prepositions= ["PRP", "PRPS"]
Prepositions_output = 0



for word in data:
    for noun in Nouns:
        if word[1] == noun:
            nouns_output+=1
    for noun in Adjectives:
        if word[1] == noun:
            Adjectives_output+=1
    for noun in Verbs:
        if word[1] == noun:
            Verbs_output+=1

    for noun in Adverbs:
        if word[1] == noun:
            Adverbs_output+=1

    for noun in Interjections:
        if word[1] == noun:
            Interjections_output+=1
    for noun in Prepositions:
        if word[1] == noun:
            Prepositions_output+=1

print('Существительное:',nouns_output)
print('Прилагательное:',Adjectives_output)
print('Глаголы:',Verbs_output)
print('Наречия:',Adverbs_output)
print('Междометия:',Interjections_output)
print('Предлоги:',Prepositions_output)