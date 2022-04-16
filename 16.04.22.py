word = input()
n = int(input())
words = []
for i in range(n):
	words.append(input())


vowels = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")


def search_vowels(word: str):
	result = []
	for i in range(len(word)):
		if word[i] in vowels:
			result.append(i)
	return result


word_vowels = search_vowels(word)
words_vowels = []
for word in words:
	words_vowels.append(search_vowels(word))

for i in range(n):
	if word_vowels == words_vowels[i]:
		print(words[i])
	else:
		print(f"не подходит {words[i]}")
