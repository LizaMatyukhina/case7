"""
Case #7

Developers:
- Aigerim Rashidova
- Alina Romanenko
- Elizaveta Matyukhina.
"""

# Aigerim - work with file and text.
with open('input.txt') as f_in:
    text = f_in.read()
symbols_of_end = '.!?'
for i in symbols_of_end:
    if i in text:
        text = text.replace(i, ' ')
symbols = '"#$%&\'()*+-/:;<=>@[]^_`{|}~'
for i in symbols:
    if i in text:
        text.replace(i, '')
punc = '.,!?'
for i in punc:
    a = ' i'
    if a in text:
        text.replace(a, i)

# Alina - work with words and dictionaries.


# Liza - work with dictionaries, sentences and random.

