#!/bin/python
#
# kör programmet så här:
# ./hex_to_dec.py *hextal*

import sys

# import av argument
hexnum = sys.argv[1]

length = len(hexnum) - 1

# Först tänkte jag skriva en massa if statements, men det hade varit väldigt oelegant.
# Typkonversion för siffrorna kan göras på enklare sätt, men det här blir snyggast tycker jag,
# eftersom man med den inbyggda "int()" funtionen måste konvertera siffror och bokstäver separat.
tabell = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

halvvägs = []

resultat_list = []

# Jag antar att det finns mycket mer effektiva sätt än det här,
# men det är allt jag kommer på just nu

# hex -> dec konversion fas 1:
for i in hexnum:
    halvvägs.append(tabell[i])
    print(i)

print(halvvägs)

# hex -> dec konversion fas 2:
for i in range(0, len(hexnum)):
    print("i: ", i)
    x = length - i
    print("x: ", x)
    print("halv: ", halvvägs[x])
    print("asdf: ", 16**i)
    halvvägs[x] = halvvägs[x] * (16 ** i)
    resultat = halvvägs[x] + halvvägs[x+1]
    resultat_list.append(halvvägs[x])



print("Det här är vad min algoritm säger: ", resultat)

print("Det här är vad den inbyggda python algoritmen säger: ", int(hexnum, 16))
