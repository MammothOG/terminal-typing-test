import random
import readchar
import os
import time


NUMBER_WORDS_PRINTED = 3
ROUND_NUMBER = 3
cpm = []

def compute_cpm(time_ns, str_length):
    time_s = time_ns / 10**9
    cpm = (str_length * 60) / time_s
    return cpm

def read_file(file_name):
    words_list = []
    with open(file_name, "r") as file:
        raw = file.read()
        words_list = raw.split("\n")

    return words_list

def pick_words(words):
    if len(words) == 0:
       return False

    words_printed = []

    for _ in range(NUMBER_WORDS_PRINTED):
        word = random.choice(words)
        words_printed.append(word)

    return words_printed

def printParity(entries, words):
    # cut words
    parity = ""
    for i, char in enumerate(words):
        if i >= len(entries):
            parity = parity + "\033[00m" + char
        elif char == entries[i]:
            parity = parity + "\033[42m\033[30m" + char
        else:
            parity = parity + "\033[41m\033[30m" + char
    
    if len(entries) > len(words):
        parity = parity + "\033[41m\033[30m" + entries[i+1:]

    print(parity + "\033[00m")

#----------------------------------------------------------------
words = read_file("./words-set/default-en.txt")

for rounds in range(ROUND_NUMBER):
    entries = ""
    char = b""

    words_picked = pick_words(words)
    words_string = " ".join(words_picked)

    while not char == b"\r" or len(entries) < len(words_string):
        os.system("cls")

        print("-- Round ", rounds, "--")
        printParity(entries, words_string)

        char = readchar.readchar()
        if b'\x08' == char:
            entries = entries[:-1]
        elif b'\x1b' == char:
            entries = ""
        elif char in [b'\xfd']:
            pass
        else:
            entries = entries + char.decode("utf-8")

        if len(entries) == 1:
            start_time = time.time_ns()


    end_time = time.time_ns()
    cpm.append(compute_cpm(end_time-start_time, len(words_string)))

cpm_mean = 0
for i, cpm_round in enumerate(cpm):
    print("Rounds {} : {}".format(i, cpm_round))
    cpm_mean += cpm_round

cpm_mean /= len(cpm)
print("cpm mean : ", cpm_mean)