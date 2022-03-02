import string
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"/#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_digits = len(str(len(alphabet)))

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encode(text: str) -> str:
	result = ""
	for i in text:
		idx = alphabet.index(i)
		if len(str(idx)) == alphabet_digits:
			result += str(idx)
		else:
			zeroes = alphabet_digits - len(str(idx))
			for zero in range(zeroes):
				result += "0"
				result += str(idx)
	return result


code = encode("Дудос incoming")
print(code)


def decode(code: str) -> str:
	result = ""
	slices = len(code) // alphabet_digits
	iterator = 0
	for i in range(slices):
		id_code = code[iterator:iterator + alphabet_digits]
		if id_code == "000":
			result += alphabet[0]
		else:
			idx = id_code.lstrip('0')
			result += alphabet[int(idx)]
		iterator += alphabet_digits
	return result



decode(code)
