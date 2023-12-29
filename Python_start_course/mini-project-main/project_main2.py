import HashSet as hs
import BstMap as bst

# Initiera ett HashSet
unique_words = hs.HashSet()
unique_words.init()

# Filsökvägar
file_path_1 = "brian_output.txt"
file_path_2 = "swe_news_output.txt"

# Lägg till ord i HashSet från den första filen
with open(file_path_1, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            unique_words.add(word)

# Lägg till ord i HashSet från den andra filen
with open(file_path_2, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            unique_words.add(word)

# Totalt antal unika ord från båda filerna
total_unique_words = unique_words.get_size()
print(f"Total number of unique words in both files: {total_unique_words}")

# Skapa en BstMap för ordfrekvens
word_frequency = bst.BstMap()

# Räkna ordfrekvensen i den första filen
with open(file_path_1, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            current_count = word_frequency.get(word)
            if current_count is None:
                current_count = 0
            word_frequency.put(word, current_count + 1)

# Hämta och sortera ordfrekvensen för den första filen
sorted_word_frequency_1 = word_frequency.as_list()
sorted_word_frequency_1.sort(key=lambda x: x[1], reverse=True)

# Skriv ut de 10 mest frekventa orden i den första filen
print("\nTop 10 most frequent words in file 1:")
for word, count in sorted_word_frequency_1[:10]:
    print(f"{word}: {count}")

# Skapa en ny BstMap för ordfrekvens för den andra filen
word_frequency = bst.BstMap()

# Räkna ordfrekvensen i den andra filen
with open(file_path_2, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            current_count = word_frequency.get(word)
            if current_count is None:
                current_count = 0
            word_frequency.put(word, current_count + 1)

# Hämta och sortera ordfrekvensen för den andra filen
sorted_word_frequency_2 = word_frequency.as_list()
sorted_word_frequency_2.sort(key=lambda x: x[1], reverse=True)

# Skriv ut de 10 mest frekventa orden i den andra filen
print("\nTop 10 most frequent words in file 2:")
for word, count in sorted_word_frequency_2[:10]:
    print(f"{word}: {count}")

# ta fram bucket list size
bucket_listsize = unique_words.bucket_list_size()

# ta fram storleken av den bucket med flest element
max_bucket_size = unique_words.max_bucket_size()

# ta fram förhållandet av tomma buckets
zero_bucket_ratio = unique_words.zero_bucket_ratio()

print(f'\nBucket list size: {bucket_listsize}')

print(f'\nMax bucket size: {max_bucket_size}')

print(f'\nZero bucket ratio: {zero_bucket_ratio}')

node = bst.Node()

# räknar alla nodes
node_count = word_frequency.root.count()

# hämtar det maximala djupet i trädet
max_depth = word_frequency.max_depth()

# räknar alla de noder som har minst ett barn
internal_node_count = word_frequency.count_internal_nodes()

print(f'\nNumber of tree nodes: {node_count}')

print(f'\nThe maximum depth of the tree: {max_depth}')

print(f'\nInternal node count of the tree: {internal_node_count}')
