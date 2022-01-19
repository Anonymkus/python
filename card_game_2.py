import random as r
import os 


suits = ("червей", "пик", "крестей", "бубен")
values = range(6, 15)


def populate_deck(suits, deck, values):
	for suit in suits:
		for value in values:
			card = {}
			card["масть"] = suit
			card["стоимость"] = value
			deck.append(card)
	r.shuffle(deck)


def distribute_cards(deck, user_deck, comp_deck):
	for card in deck[:len(deck) // 2]:
		user_deck.append(card)
	for card in deck[len(deck) // 2:]:
		comp_deck.append(card)
	

def start_new_game():
	deck = []
	user_deck = []
	comp_deck = []
	table = []

	populate_deck(suits, deck, values)
	distribute_cards(deck, user_deck, comp_deck)

	while user_deck and comp_deck:
		start_new_round(user_deck, comp_deck, deck, table)

	print("--- the game end! ---")
	if user_deck:
		print("user has won")
	else:
		print("computer has won")


def start_new_round(user_deck, comp_deck, deck, table):
	os.system("cls")
	print("\n------ user deck ------")
	for card in user_deck:
		print(f'{card["стоимость"]} {card["масть"]}, ', end="")
	print("\n\n------ comp deck ------")
	for card in comp_deck:
		print(f'{card["стоимость"]} {card["масть"]}, ', end="")


	user_card = (user_deck.pop())
	comp_card = (comp_deck.pop())
	table.append(user_card)
	table.append(comp_card)

	print("\n\n----- user move -----")
	print(user_card["стоимость"], user_card["масть"])
	

	print("\n----- comp move -----")
	print(comp_card["стоимость"], comp_card["масть"])


	while user_card['стоимость'] == comp_card['стоимость']:
		print("dispute")
		user_card = (user_deck.pop())
		comp_card = (comp_deck.pop())
		table.append(user_card)
		table.append(comp_card)

		print("\n\n----- user move in dispute -----")
		print(user_card["стоимость"], user_card["масть"])
		user_card 

		print("\n----- comp move in dispute -----")
		print(comp_card["стоимость"], comp_card["масть"])
		

	print("\n----- result round -----")
	if user_card["стоимость"] > comp_card["стоимость"]:
		print(f"user won and take ")
		for card in table:
			user_deck.insert(0, table)
			print(f'{card["стоимость"]} {card["масть"]}, ', end="")
	else:
		print(f"computer won and take ")
		for card in table:
			comp_deck.insert(0, table)
			print(f'{card["стоимость"]} {card["масть"]}, ', end="")
	table.clear()

start_new_game()
