import random as r
"""
	*Игра в Пьяницу*
	Создать колоду из 36 карт:                                          ///+
		4 масти, 9 стоимостей карты
		коллекция из карт
		карта: масть + стоимость карты
	Перемешать колоду                                                   ///+

	Раздать карты:                                                      ///+
		карты игрока - 1/2 от колоды
		карты соперника - 1/2 от колоды
	Начать партию:                                                      ///+
		взять верхнюю карту игрока (-1) и положить на стол
		взять верхнюю карту соперника (-1) и положить на стол
	Сравниваем карты на столе:                                          ///
		вариант 1 - стоимость карты игрока > соперника:
			карты игрока += стол (вниз карт)
		вариант 2 - стоимость карты игрока < соперника:
			карты соперника += стол (вниз карт)
		вариант 3 - стоимость карты игрока = соперника
			выбросить ешё пару карт
	Победа и проигрыш:                                                  ///
		кончились карты
		нечем ответеть в споре
"""

suits = ("червей", "пик", "крестей", "бубен")
table = []


def make_deck(suits: int):
	deck = []
	for suit in suits:
		for value in range(6, 15):
			card = {}
			card["масть"] = suit
			card["стоимость"] = value
			deck.append(card)
	r.shuffle(deck)
	return deck


def distribute_cards(deck):
	user_deck = deck[:18]
	comp_deck = deck[18:]

	return user_deck, comp_deck


def start_round(user_deck, comp_deck, deck, table):
	table.append(user_deck.pop())
	table.append(comp_deck.pop())

	print("user", table[0]["стоимость"])
	print("comp", table[1]["стоимость"])

	def compare_cards(table, user_deck, comp_deck, deck):
		if table[0]["стоимость"] > table[1]["стоимость"]:
			print("user won")
			user_deck.insert(0, table)
		elif table[0]["стоимость"] < table[1]["стоимость"]:
			print("comp won")
			comp_deck.insert(0, table)
		else:
			print("dispute")
			controversial_table = []
			def compare_controversial_cards(table, user_deck, comp_deck, deck):
				controversial_table.append(user_deck.pop())
				controversial_table.append(comp_deck.pop())
				print("user's second card", controversial_table[0]["стоимость"])
				print("comp's second card", controversial_table[1]["стоимость"])
				if controversial_table[0]["стоимость"] > controversial_table[1]["стоимость"]:
					print("user won")
					user_deck.insert(0, controversial_table)
					user_deck.insert(0, table)
				elif controversial_table[0]["стоимость"] < controversial_table[1]["стоимость"]:
					print("comp won")
					comp_deck.insert(0, controversial_table)
					comp_deck.insert(0, table)
				else:
					print("dispute")
					table.append(controversial_table)
					print(table)
			compare_controversial_cards(table, user_deck, comp_deck, deck)
	compare_cards(table, user_deck, comp_deck, deck)
	


deck = make_deck(suits)
user_deck = distribute_cards(deck)[0]
comp_deck = distribute_cards(deck)[1]
print(user_deck)
print("-------------------------")
print(comp_deck)
print("=========================")
start_round(user_deck, comp_deck, deck, table)
print(user_deck)
print("-------------------------")
print(comp_deck)
