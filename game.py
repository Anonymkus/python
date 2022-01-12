import random as r
"""
	*Игра в Пьяницу*

	Создать колоду из 36 карт:                                          ///+
		4 масти, 9 стоимостей карты
		коллекция из карт
		карта: масть + стоимость карты

	Перемешать колоду													///+

	Раздать карты:														///+
		карты игрока - 1/2 от колоды
		карты соперника - 1/2 от колоды

	Начать партию:														///+
		взять верхнюю карту игрока (-1) и положить на стол
		взять верхнюю карту соперника (-1) и положить на стол

	Сравниваем карты на столе:											///
		вариант 1 - стоимость карты игрока > соперника:
			карты игрока += стол (вниз карт)
		вариант 2 - стоимость карты игрока < соперника:
			карты соперника += стол (вниз карт)
		вариант 3 - стоимость карты игрока = соперника
			выбросить ешё пару карт

	Победа и проигрыш:													///
		кончились карты
		нечем ответеть в споре
"""

suits = ("червей", "пик", "крестей", "бубен")

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
	computer_deck = deck[18:]

	return user_deck, computer_deck


def start_round(user_deck, computer_deck, deck):
	desk = []
	desk.append(user_deck.pop())
	desk.append(computer_deck.pop())

	print("user", desk[0]["стоимость"])
	print("comp", desk[1]["стоимость"])

	if desk[0]["стоимость"] > desk[1]["стоимость"]:
		print("user won")
	elif desk[0]["стоимость"] < desk[1]["стоимость"]:
		print("comp won")
	else:
		print("dispute")


deck = make_deck(suits)
user_deck = distribute_cards(deck)[0]
computer_deck = distribute_cards(deck)[1]
start_round(user_deck, computer_deck, deck)
