"""
Case-study #7 Generation of sentences
Developers:
- Aigerim Rashidova
- Alina Romanenko
- Elizaveta Matyukhina.
"""

import random

file_in = input('Введите имя файла: ')
with open(file_in, encoding="UTF-8") as f_in:
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

startwords = []
allwords = []
endwords = []
dict = {}
symbols_of_end = ['.', '!', '?']
lst = text.split()
for i in range(len(lst)-1):
    nextword = []
    word = lst[i]
    if word not in allwords:
        for m in range(len(lst)):
            if word == lst[m] and word not in nextword:
                nextword.append(lst[m+1])
        dict[word] = nextword
        allwords.append(word)
    if word.lower() != word and word not in startwords and word[-1] not in symbols_of_end:
        startwords.append(word)
    if word[-1] in symbols_of_end and word not in endwords:
        endwords.append(word)

number_of_sentences = int(input('Введите количество предложений: '))
for i in range(number_of_sentences):
    count = 0
    sentence = []
    first_word = random.choice(startwords)
    while first_word[-1] == '.':
        first_word = random.choice(startwords)
    sentence.append(first_word)
    count += 1
    while count < 20:
        while count < 5:
            word = random.choice(dict[sentence[-1]])
            sentence.append(word)
            if word[-1] == '.':
                sentence.remove(word)
                word = random.choice(dict[sentence[-1]])
                sentence.append(word)
            count += 1
        word = random.choice(dict[sentence[-1]])
        if word[-1] == '.':
            sentence.append(word)
            break
        if count == 19 and word not in endwords:
            if word[-1] != ',':
                word = word + '.'
            elif word[-1] == ',':
                word.replace(',', '')
        sentence.append(word)
        count += 1
    print(*sentence, sep=' ', end=' ')


