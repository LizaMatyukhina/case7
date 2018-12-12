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


# Liza - work with dictionaries, sentences and random.

