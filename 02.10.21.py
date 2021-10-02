u_age = 0
u_name = 0
u_money = 0
u_choice = 0
u_bet = 0


import random


def create_character():
	global u_name
	global u_age
	u_age = (input("Сколько тебе лет милок? "))
	u_name = (input("А звать тeбя то как? "))
	global u_money
	u_money = 500




def show_location_primary():
	print("1 дорожка ведёт в казино, деньги есть, так что можно и сходить.")
	print("2 дорожка ведёт на махач с кем-то, но щас ты немножечко лох, так что не думаю, что туда щас надо идти.")
	print("3 дорожка ведет в магаз, денег чуть убавилось, потому что налоги никто не отменял")

def show_gamble():
	u_choice = input("Играть или нет? (Напишите да или нет)")
	if u_choice == "да":
		u_dice = random.randint(2, 12)
		casino_dice = random.randint(2, 12)
		print(f"Тебе выпало {u_dice}")
		print(f"Сопернику выпало {casino_dice}")
		if u_dice > casino_dice:
			print("Опа, плюс мани!")
			show_gamble()
		elif u_dice < casino_dice:
			print("Минус мани, молодец чо. Иди работай, а не в казино рубись!")
			show_gamble()
			show_location_primary
		else:
			print("Даже хз повезло тебе или нет.")
			show_gamble()
	elif u_choice == "нет" :
		print("Вы решили уйти обратно")
		show_location_primary
	else:
		print("Соберись и реши нормально, да или нет")
		show_gamble()

def show_ask_user():
	global u_choice
	while u_choice not in ("1", "2", "3"):
		u_choice = input("Что выбрать? ")


print("Привет обитатель интернета, добро пожаловать в примитивную игрушку на Python")
print("Чтобы у тебя было ощущение выбора хоть где-то, ")
print("напиши сам данные своего персонажа, не забудь нажать на ENTER")
print("Тебе задонатили 500 рубликов, ничо так.")
print("Ты прoснулся где-тo, а главнoе зачем-тo. Гoлoва твoя бoлит, а пoп-ита как назлo нет")
print("И тут тебя посещает гениальная мысль пойти по 1-ой из 3 дорожек")
print("По странной и непонятной причине ты знаешь куда ведут дорожки")


show_location_primary()

show_ask_user()

if u_choice == "1":
	print("Ты пошёл по 1-ой дорожке.")
	show_gamble()
elif u_choice == "2":
	print("Ты пошёл по 2-ой дорожке.")
else:
	print("Ты пошёл по 3-ей дорожке")
