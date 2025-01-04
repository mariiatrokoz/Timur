'''Необхідно написати програму яка буде приймати в якості аргументів програми довільну кількість слів
та робити з них рандомномні (випадковом) пари.
Програма буде використовуватись для створювання випадкових пар.
Назвати програму random_pairs.

USAGE:
	python3 random_pairs.py timur ivan mariia anna dima lena
OUTPUT:
	timur - mariia
	dima - ivan
	lena - anna

У випадку якщо є слово без пари ігнорувати його.'''

import sys
import random

names = sys.argv[1:]
random.shuffle(names)

for pair in zip(names[::2], names[1::2]):
    print(pair)
