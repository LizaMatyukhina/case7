"""
Case-study #7 Generation of sentences
Developers:
- Aigerim Rashidova
- Alina Romanenko
- Elizaveta Matyukhina.
"""

import random
from ru_local import *

file_in = input(ENTER_NAME_OF_FILE)

try:
    input_file = open(file_in, 'r')
    with open(file_in, encoding="UTF-8") as f_in:
        startwords = []
        allwords = []
        endwords = []
        dict = {}
        symbols = ['"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']', '^',
                   '_',
                   '`', '{', '|', '}', '~', '—', '«', '»']
        symbols_of_end = ['.', '!', '?']

        text = f_in.read()
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

        lst = text.split()
        for i in range(len(lst) - 1):
            next_word = []
            word = lst[i]
            if word not in allwords:
                for m in range(len(lst)):
                    if word == lst[m] and word not in next_word:
                        next_word.append(lst[m + 1])
                dict[word] = next_word
                allwords.append(word)
            if word.lower() != word and word not in startwords and word[-1] not in symbols_of_end:
                startwords.append(word)
            if word[-1] in symbols_of_end and word not in endwords:
                endwords.append(word)

        number_of_sentences = input(ENTER_NUMBER_OF_SENTENCES)
        try:
            number = int(number_of_sentences)
            with open('output.txt', 'w', encoding="UTF-8") as f_out:
                for i in range(int(number_of_sentences)):
                    count = 0
                    sentence = []
                    first_word = random.choice(startwords)
                    while first_word in endwords or len(dict[first_word]) < 2:
                        first_word = random.choice(startwords)
                    sentence.append(first_word)
                    count += 1
                    while count < 20:
                        while count < 5:
                            word = random.choice(dict[sentence[-1]])
                            sentence.append(word)
                            if word in endwords:
                                sentence.pop()
                                word = random.choice(dict[sentence[-1]])
                                sentence.append(word)
                            count += 1
                        if len(sentence) < 5 and sentence[-1][-1] == '.':
                            break
                        elif len(sentence) >= 5 and sentence[-1][-1] == '.':
                            print(*sentence, sep=' ', end=' ', file=f_out)
                            break
                        else:
                            word = random.choice(dict[sentence[-1]])
                            if word in endwords:
                                sentence.append(word)
                                break
                            if count == 19 and word not in endwords:
                                if word[-1] != ',':
                                    word = word + '.'
                                elif word[-1] == ',':
                                    word.replace(',', '')
                        sentence.append(word)
                        count += 1
                    print(*sentence, sep=' ', end=' ', file=f_out)
        except ValueError:
            print(NOT_CORRECT_NUMBER)
except FileNotFoundError:
    print(FILE_NOT_FOUND)
