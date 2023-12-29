import os
from math import ceil as c


def count_letters(file_path):

    alfabeth = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "x", "y", "z"]
    word_lst = []
    letter_occurs = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst.append(line.lower())

    for char in alfabeth:
        char_count = 0
        for word in word_lst:
            if char in word:
                for letter in word:
                    if letter == char:
                        char_count += 1
        letter_occurs[char] = char_count

    return letter_occurs


path = os.getcwd()
file_path = path + "/brian_13380_words.txt"
XXX = 200

for key, value in count_letters(file_path).items():
    print(key, "| " + ("*"*(c(value/XXX))))
