import random

LETTER_VALUES = {"a": 1,
                "b": 4,
                "c": 5,
                "d": 3,
                "e": 1,
                "f": 5,
                "g": 3,
                "h": 4,
                "i": 1,
                "j": 7,
                "k": 6,
                "l": 3,
                "m": 4,
                "n": 2,
                "o": 1,
                "p": 4,
                "q": 8,
                "r": 2,
                "s": 2,
                "t": 2,
                "u": 4,
                "v": 5,
                "w": 5,
                "x": 7,
                "y": 4,
                "z": 8,}

WORDS = set() # decreasing points order

with open("sowpods.txt") as f:
    read = False
    for line in f:
        word = line[:-1] # ignore newline at end of every word
        if read and len(word) > 0:
            WORDS.add(word)
        elif word == "STARTREAD":
            read = True

with open("scowl.txt") as f:
    read = False
    for line in f:
        word = line[:-1] # ignore newline at end of every word
        if read and len(word) > 0 and word in WORDS:
            WORDS.remove(word)
        elif word == "STARTREAD":
            read = True

WORDS = list(WORDS)

WORDS.sort(key=lambda word:-sum([LETTER_VALUES[char] for char in word]))
# print(WORDS[:2], WORDS[-2:])

def random_char():
  return random.choice(list(LETTER_VALUES.keys())) # TODO

class Letter:
    def __init__(self, char=None):
        if char is None:
            char = random_char()
        self.char = char
        self.value = LETTER_VALUES[char]
        self.gem = False
    
    def __str__(self):
        return self.char

    def __repr__(self):
        return self.char
