def count_unique_words(file_path):
    unique_words = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            unique_words.update(words)

    return unique_words


def count_word_frequency(file_path):
    word_frequency = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_frequency[:10]


file_path_1 = "brian_output.txt"
file_path_2 = "swe_news_output.txt"

unique_words_1 = count_unique_words(file_path_1)
unique_words_2 = count_unique_words(file_path_2)

total_unique_words = unique_words_1.union(unique_words_2)
print(f"Total number of unique words in both files: {len(total_unique_words)}")

top_10_words_1 = count_word_frequency(file_path_1)
top_10_words_2 = count_word_frequency(file_path_2)

print("\nTop 10 most frequent words in file 1:")
for word, count in top_10_words_1:
    print(f"{word}: {count}")

print("\nTop 10 most frequent words in file 2:")
for word, count in top_10_words_2:
    print(f"{word}: {count}")