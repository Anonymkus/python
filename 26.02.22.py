import string
alphabet = string.ascii_lowercase + string.ascii_uppercase
alphabet += "0123456789_-" 

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-


def encrypt(text: str) -> str:
	result = ""
	for i in text:
		if len(str(alphabet.index(i))) == 1:
			result += "0" + str(alphabet.index(i))
		else:
			result += str(alphabet.index(i))
	return result


print(encrypt("hI1"))
