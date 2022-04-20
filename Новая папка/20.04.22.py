n = int(input())
emails = list()
for i in range(n):
	emails.append(input())
m = int(input())
users = list()
for j in range(m):
	users.append(input())

emails_cut = list()
for i in emails:
	emails_cut.append(i[:i.index("@")])
print(emails_cut)


result = []
for i in users:
	if i not in emails_cut:
		result.append(i + "@beegeek.bzz")
	else:
		num = 
