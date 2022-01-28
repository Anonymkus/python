alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet += alphabet.upper()


def encrypt(message:str, shift:int) -> str:
	result = ""
	for letter in message:
		if letter in alphabet:
			index = alphabet.index(letter)
			index_shifted = (index + shift) % len(alphabet)
			result += alphabet[index_shifted]
		else:
			result += letter
	return result

message_encrypted = encrypt("Привет", 5)


def bruteforce_encrypt(message:str, func) -> str:
	for i in range(len(alphabet)):
		print(i, encrypt(message_encrypted, i * -1))


bruteforce_encrypt(message_encrypted, encrypt)

