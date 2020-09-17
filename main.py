import random
import readchar
import os


NUMBER_WORDS_PRINTED = 3
ROUND_NUMBER = 3

words = ["je", "suis", "en", "direction", "de", "paris"]


def grab_words(words):
    if len(words) == 0:
       return False

    words_printed = []

    for _ in range(NUMBER_WORDS_PRINTED):
        word = random.choice(words)
        words_printed.append(word)
        words.remove(word)

    return words_printed

def printParity(entries, words):
    # cut words
    parity = ""
    for i, char in enumerate(words):
        if i > len(entries) - 1:
            parity = parity + "\033[00m" + char
        elif char == entries[i]:
            parity = parity + "\033[42m\033[30m" + char
        else:
            parity = parity + "\033[41m\033[30m" + char

    print(parity + "\033[00m")

for rounds in range(ROUND_NUMBER):
    words_grabed = grab_words(words)
    entries = ""
    char = b""

    if not words_grabed == False:
        words_string = " ".join(words_grabed)

        # get charactere
        while not char == b"\r" or len(entries) < len(words_string):

            print("-- Round ", rounds, "--")
            print(words_string)
            printParity(entries, words_string)

            char = readchar.readchar()
            if b'\x08' == char:
                entries = entries[:-1]
            elif b'\x1b' == char:
                entries = ""
            elif char in []:
                pass
            else:
                entries = entries + char.decode("utf-8")

            os.system("cls")

    else:
        print("--end--")
