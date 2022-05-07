a = int(input())
b = int(input())

temp1 = max((a, b))
temp2 = min((a, b))


while True:
	if not temp1 * temp2:
		print("error")
		break
	elif temp1 % temp2 == 0:
		print("НОД:", temp2)
		break
	else:
		remainder = temp1 % temp2
		temp1 = temp2
		temp2 = remainder

