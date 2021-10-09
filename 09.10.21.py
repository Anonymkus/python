import random


def play_dice(user_money):
	user_bet = int(input("Сколько ставишь? "))
	if user_bet > user_money:
		print("У тебя столько нет!")
		play_dice(user_money
	elif user_bet >= 0:
		print("И как ты собрался играть?")
		play_dice(user_money)

	return user_money


user_money = 5000
user_money = play_dice(user_money)
print(user_money)

