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
    f_out.write(text)

# Alina - work with words and dictionaries.

startwords = []
allwords = []
endwords = []
slovar = {}
symbols_of_end = ['.', '!', '?']
with open('output.txt', encoding="UTF-8") as f_in:
    text = f_in.read()
    lst = text.split()
    for i in range(len(lst)-1):
        nextword = []
        word = lst[i]
        if word not in allwords:
            for m in range(len(lst)):
                if word == lst[m]:
                    nextword.append(lst[m+1])
            slovar[word] = nextword
            allwords.append(word)
        if word.lower() != word and word not in startwords and word[-1] not in symbols_of_end:
            startwords.append(word)
        if word[-1] in symbols_of_end:
            endwords.append(word)
print(startwords)
print(endwords)
print(slovar)
# Liza - work with dictionaries, sentences and random.
