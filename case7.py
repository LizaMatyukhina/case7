"""
Case-study #7 Generation of sentences
Developers:
- Aigerim Rashidova
- Alina Romanenko
- Elizaveta Matyukhina.
"""

import random

# Aigerim - work with file and text.
with open('input.txt', encoding="UTF-8") as f_in:
    text = f_in.read()
    with open('output.txt', 'w', encoding="UTF-8") as f_out:
        symbols = ['"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']', '^', '_',
               '`', '{', '|', '}', '~', '—', '«', '»']
        for i in symbols:
            if i in text:
                text = text.replace(i, '')
        punctuation = [' .', ' ,', ' !', ' ?']
        for i in punctuation:
            if i in text:
                if i == ' ,':
                    text = text.replace(i, ',')
                elif i == ' .':
                    text = text.replace(i, '.')
                elif i == ' !':
                    text = text.replace(i, '!')
                elif i == ' ?':
                    text = text.replace(i, '?')

# Alina - work with words and dictionaries.

startwords = []
allwords = []
endwords = []
slovar = {}
symbols_of_end = ['.', '!', '?']
lst = text.split()
for i in range(len(lst)-1):
    nextword = []
    word = lst[i]
    if word not in allwords:
        for m in range(len(lst)):
            if word == lst[m] and word not in nextword:
                nextword.append(lst[m+1])
        slovar[word] = nextword
        allwords.append(word)
    if word.lower() != word and word not in startwords and word[-1] not in symbols_of_end:
        startwords.append(word)
    if word[-1] in symbols_of_end and word not in endwords:
        endwords.append(word)
# Liza - work with dictionaries, sentences and random.

textt = []
count = 0
number_of_sentences = int(input())
for i in range(number_of_sentences):
    sentence = []
    word = random.choice(startwords)
    sentence.append(word)
    count += 1
    while count < 20:
        word = random.choice(slovar[sentence[-1]])
        count += 1
        while word in endwords and count < 5:
            word = random.choice(slovar[sentence[-1]])
        if word in endwords and count > 5:
            sentence.append(word)
            break
        sentence.append(word)
    if count == 20 and sentence[-1] != ',':
        sentence[-1] = sentence[-1] + '.'
    elif count == 20 and sentence[-1] == ',':
        sentence[-1].replace(',', '')
    count = 0
    print(*sentence, sep=' ', end=' ')








