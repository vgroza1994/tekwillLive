text = input('Introduceți bucata de text:')

all_words = text.split()
print("Total cuvinte:", len(all_words))

unique_words = list(set(all_words))
print("Cuvinte unice:", len(unique_words))

count_list = [0] * len(unique_words)

for index, word in enumerate(unique_words):
    count_list[index] = all_words.count(word)

print("Frecvența cuvintelor:")
for word, count in zip(unique_words, count_list):
    print(f"{word}: {count}")