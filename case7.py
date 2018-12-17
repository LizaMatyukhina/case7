"""
Case-study #7 Generation of sentences
Developers:
- Aigerim Rashidova
- Alina Romanenko
- Elizaveta Matyukhina.
"""

# Aigerim - work with file and text.
with open('input.txt', encoding="UTF-8") as f_in:
    text = f_in.read()
with open('output.txt', 'w', encoding="UTF-8") as f_out:
    symbols_of_end = ['.', '!', '?']
    for i in symbols_of_end:
        if i in text:
            text = text.replace(i, ' ')
    symbols = ['"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']', '^', '_',
               '`', '{', '|', '}', '~', '—', '«', '»']
    for i in symbols:
        if i in text:
            text = text.replace(i, '')
    punctuation = [' .', ' ,', ' !', ' ?']
    for i in punctuation:
        if i in text:
            if i == ' .':
                text = text.replace(i, '.')
            elif i == ' ,':
                text = text.replace(i, ',')
            elif i == ' !':
                text = text.replace(i, '!')
            elif i == ' ?':
                text = text.replace(i, '?')
    f_out.write(text)

# Alina - work with words and dictionaries.

keywords = []
allwords = []
slovar = {}
with open('output.txt', encoding="UTF-8") as f_in:
    text = f_in.read()
    lst = text.split()
    for i in range(len(lst)-1):
        nextword = []
        if lst[i] not in allwords:
            for m in range(len(lst)):
                if lst[i] == lst[m]:
                    nextword.append(lst[m+1])
            slovar[lst[i]] = nextword
            allwords.append(lst[i])
        if lst[i].lower() != lst[i] and lst[i] not in keywords:
            keywords.append(lst[i])
print(keywords)
print(slovar)
# Liza - work with dictionaries, sentences and random.
