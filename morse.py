morse_dict = {
	"а" : "· −",
	"б" : "− · · ·",
	"в" : "· − −",
	"г" : "− − ·",
	"д" : "− · ·",
	"е" : "·",
	"ж" : "· · · −",
	"з" : "− − · ·",
	"и" : "· ·",
	"й" : "· − − −",
	"к" : "− · −",
	"л" : "· − · ·",
	"м" : "− −",
	"н" : "− ·",
	"о" : "− − −",
	"п" : "· − − ·",
	"р" : "· − ·",
	"с" : "· · ·",
	"т" : "−",
	"у" : "· · −",
	"ф" : "· · − ·",
	"х" : "· · · ·",
	"ц" : "− · − ·",
	"ч" : "− − − ·",
	"ш" : "− − − −",
	"щ" : "− − · −",
	"ъ" : "− − · − −",
	"ы" : "− · − −",
	"ь" : "− · · −",
	"э" : "· · − · ·",
	"ю" : "· · − −",
	"я" : "· − · −",
	" " : "− · · · −",
	"1" : "· − − − −",
	"2" : "· · − − −",
	"3" : "· · · − −",
	"4" : "· · · · − ",
	"5" : "· · · · ·",
	"6" : "− · · · ·",
	"7" : "− − · · ·",
	"8" : "− − − · ·",
	"9" : "− − − − ·",
	"0" : "− − − − −",

}

text1 = "· −"
def morse_decode(text: str) -> str:
	morse_dict_values_list = list(morse_dict.values())
	morse_dict_keys_list = list(morse_dict.keys())

	index = morse_dict_values_list.index(text)
	result = morse_dict_keys_list[index]
	return result



text = "ПриВет123"
def morse_encode(text:str) -> str:
	text = text.lower()
	encoded_text = []
	for letter in text:
		encoded_text.append(morse_dict[letter])

	return " ".join(encoded_text)


print(morse_encode(text))


assert morse_encode("бебра") == "− · · · · − · · · · − · · −" , "something wronge"
