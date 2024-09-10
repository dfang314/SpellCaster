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

WORDS = [] # decreasing points order TODO

def random_letter():
  return "a" # TODO

class Letter:
    def __init__(self, letter=None):
        if letter is None:
            letter = random_letter()
        self.letter = letter
        self.value = LETTER_VALUES[letter]
        self.gem = False
        self.dl = False
        self.tl = False
        self.double = False
        