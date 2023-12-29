import os


def clean_script(script):
    unwanted_tokens = ["'", ":", "!", "[", "]", ".", ",", ".", "?", ";"]
    for token in unwanted_tokens:
        script = script.replace(token, '')

    rawwords = script.lower().split()

    unwanted_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    words = []
    for element in rawwords:
        number_count = 0
        for char in unwanted_characters:
            if char in element:
                number_count += 1

        if number_count == 0:
            words.append(element)

    return words


def get_words(path, file_name):

    with open(f'{path}/{file_name}', 'r', encoding='utf-8') as file:
        script_text = file.read()
        words = clean_script(script_text)
        return words


def write_file(words, path, output_file):

    with open(f'{path}/{output_file}', 'w', encoding='utf-8') as file:

        for word in words:
            file.write(word+"\n")


path = os.getcwd()
input_file = 'life_of_brian.txt'
words = get_words(path, input_file)
output_file = f'brian_{len(words)}_words.txt'

words = get_words(path, input_file)

write_file(words, path, output_file)
