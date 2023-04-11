# -*- coding: utf-8 -*-

## to shuffle randomly from a list
import random

colors = ['blue','grey','red','purple','orange','black','white','green']
random.shuffle(colors)

## print the list randomly
for c in colors:
    print(c)

## use one random color from the list
print('My favorite color is '+c)    