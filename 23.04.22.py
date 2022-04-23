n = int(input())
emails = list()
for i in range(n):
	emails.append(input())
m = int(input())
users = list()
for j in range(m):
	users.append(input())


emails_cut = list()
for email in emails:
	for idx, symbol in enumerate(email):
		if symbol.isalpha() or symbol == "-":
			continue
		else:
			emails_cut.append(email[:idx])
			break

result = list()
for user in users:
	count = emails_cut.count(user)
	if count:
		result.append(f"{user}{count}@beegeek.bzz")
	else:
		result.append(f"{user}@beegeek.bzz")

print(result)

