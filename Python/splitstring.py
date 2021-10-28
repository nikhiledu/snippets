#!/usr/bin/python

text = "Jack and jill were walking up the hill again; Yes!"

text = text.replace(';', '.')
text = text.replace('j', 'J')
sentence = text.split('.')

for i in sentence:
    print('')
    print(i.strip().capitalize()+'.', end='')
