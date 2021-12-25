def count_item():
	with open('items.txt', 'r', encoding='utf-8') as file:
		items_list = file.read().splitlines()
	
	pistol = 0
	shotgun = 0
	machine_gun = 0
	armor = 0
	medkit = 0

	for i in items_list:
		if i == "пистолетные":
			pistol += 1
		elif i == "ружейные":
			shotgun += 1
		elif i == "автоматные":
			machine_gun += 1
		elif i == "броня":
			armor += 1
		else:
			medkit += 1

	items_total = len(items_list)

	print("пистолетные:", pistol, pistol * 100/ items_total, "%")
	print("ружейные:", shotgun, shotgun * 100/ items_total, "%")
	print("автоматные:", machine_gun, machine_gun * 100/ items_total, "%")
	print("броня:", armor, armor * 100/ items_total, "%")
	print("аптечка:", medkit, medkit * 100/ items_total, "%")

count_item()