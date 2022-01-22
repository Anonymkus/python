import random as r
import os


suits = ("heart", "diamond", "club", "spade")
values = range(6, 15)


def populate_deck(suits, deck, values):
	for suit in suits:
		for value in values:
			card = {}
			card["suit"] = suit
			card["cost"] = value
			deck.append(card)
	r.shuffle(deck)


def distribute_cards(deck, user_deck, comp_deck):
	for card in deck[:len(deck) // 2]:
		user_deck.append(card)
	for card in deck[len(deck) // 2:]:
		comp_deck.append(card)


def start_new_game(start_new_round):
	deck = []
	table = []
	user_deck = []
	comp_deck = []

	populate_deck(suits, deck, values)
	distribute_cards(deck, user_deck, comp_deck)
	while user_deck and comp_deck:
		start_new_round(user_deck, comp_deck, deck, table)

	print("\n----- The game end! -----")
	if user_deck:
		print("user has won!")
	else:
		print("comp has won!")
	input("f")



def start_new_round(user_deck, comp_deck, deck, table):
	# input("ENTER - to continue")
	os.system("cls")
	print("\n----- user deck -----")
	for card in user_deck:
		print(card["cost"], card["suit"], end=", ")
	print("\n\n----- comp deck -----")
	for card in comp_deck:
		print(card["cost"], card["suit"], end=", ")

	user_card = user_deck.pop()
	comp_card = comp_deck.pop()	
	table.append(user_card)
	table.append(comp_card)


	print("\n\n----- User move -----")
	print(user_card["cost"], user_card["suit"])

	print("\n----- Comp move -----")
	print(comp_card["cost"], comp_card["suit"])


	while user_card["cost"] == comp_card["cost"]:
		print("dispute")
		user_card = (user_deck.pop())
		comp_card = (comp_deck.pop())
		table.append(user_card)
		table.append(comp_card)


		print("\n\n----- user move in dispute -----")
		print(user_card["cost"], user_card["suit"])

		print("\n----- comp move in dispute -----")
		print(comp_card["cost"], comp_card["suit"])
			

	print("\n----- result round -----")
	if user_card["cost"] == 14 and comp_card["cost"] == 6:
		print(f"computer won and take ")
		for card in table:
			comp_deck.insert(0, card)
			print(card["cost"], card["suit"], end=", ")
	elif user_card["cost"] == 6 and comp_card["cost"] == 14:
		print(f"user won and take ")
		for card in table:
			user_deck.insert(0, card)
			print(card["cost"], card["suit"], end=", ")
	else:
		if user_card["cost"] > comp_card["cost"]:
			print(f"user won and take ")
			for card in table:
				user_deck.insert(0, card)
				print(card["cost"], card["suit"], end=", ")
		else:
			print(f"computer won and take ")
			for card in table:
				comp_deck.insert(0, card)
				print(card["cost"], card["suit"], end=", ")
		# input("\nENTER - to continue")
	table.clear()
	# input("\npause")
			
	
start_new_game(start_new_round)
