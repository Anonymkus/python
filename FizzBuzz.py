number = range(1,101)

"""
	/ на 3 - fizz
	/ на 5 - buzz
	/ на 3 и на 5 - fizzbuzz
	остальные - как есть
"""

for num in number:
	fizz = num % 3
	buzz = num % 5
	if fizz == 0 and buzz == 0:
		print(f"FizBuzz {num}")
	elif buzz == 0:
		print(f"buzz {num}")
	elif fizz == 0:
		print(f"fizz {num}")
	else:
		print(f"Другие числа {num}")
