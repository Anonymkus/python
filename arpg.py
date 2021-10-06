u_age = 0
u_name = 0
u_money = 500
u_choice = 0
import random


def show_casino_location():
	global u_money
	casino_money = 5000
	casino_bet = 100
	if u_money > 0 and casino_money > 0:
		u_choice = input("Играть или нет? (Напишите да или нет) ")
		if u_choice == "да":
			print(f"Ты пришёл в казино, играть можешь пока не кончатся деньги либо у тебя, либо у казино, у казино {casino_money} денег")
			u_bet = int(input("Сколько поставишь денег? (только помни, не ставь больше, чем у тебя есть) "))
			print(f"Ты поставил {u_bet}, казино поставило {casino_bet} чтож, играем!") 
			u_dice = random.randint(2, 12)
			casino_dice = random.randint(2, 12)
			print(f"Тебе выпало {u_dice}")
			print(f"Сопернику выпало {casino_dice}")
			if u_dice > casino_dice:
				casino_money -= casino_bet
				u_money += casino_bet
				print(f"Опа, плюс мани! у тебя {u_money}.")
				print(f"У казино {casino_money}")
				show_casino_location()
			elif u_dice < casino_dice:
				casino_money += u_bet
				u_money -= u_bet
				print(f"Минус мани, молодец чо,у тебя {u_money}. Иди работай, а не в казино рубись!")
				print(f"У казино {casino_money}")
				show_casino_location()
			else:
				print("Даже хз повезло тебе или нет.")
				show_casino_location()
		elif u_choice == "нет" :
				print("Вы решили уйти обратно")
				show_location_primary()
		else:
			print("Соберись и реши нормально, да или нет")
			show_casino_location()
	else:
		print("Денег нет, валите!")
		show_location_primary()

def show_location_primary():
	global u_choice
	print("1 дорожка ведёт в казино, деньги есть, так что можно и сходить.")
	print("2 дорожка ведёт на махач с кем-то, но щас ты немножечко лох, так что не думаю, что туда щас надо идти.")
	print("3 дорожка ведет в магаз, денег чуть убавилось, потому что налоги никто не отменял")
	u_choice = input("По какой дорожке пойдёшь? ")

print("Привет обитатель интернета, добро пожаловать в примитивную игрушку на Python")
print("Чтобы у тебя было ощущение выбора хоть где-то, ")
print("напиши сам данные своего персонажа, не забудь нажать на ENTER")
u_age = (input("Сколько тебе лет милок? "))
u_name = (input("А звать тeбя то как? "))
print("Тебе задонатили 500 рубликов, ничо так.")
print("Ты прoснулся где-тo, а главнoе зачем-тo. Гoлoва твoя бoлит, а пoп-ита как назлo нет")
print("И тут тебя посещает гениальная мысль пойти по 1-ой из 3 дорожек")
print("По странной и непонятной причине ты знаешь куда ведут дорожки")


show_location_primary()



if u_choice == "1":
	show_casino_location()



