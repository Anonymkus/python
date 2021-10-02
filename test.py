import random
u_age = 0
u_name = 0
u_money = 500
u_choice = 0
u_bet = 0
casino_money = 5000
casino_bet = 100

def show_gamble():
	global u_money
	global casino_money
	global casino_bet
	u_choice = input("Играть или нет? (Напишите да или нет) ")
	if u_choice == "да":
		print(f"Ты пришёл в казино, играть можешь пока не кончатся деньги либо у тебя, либо у казино, у казино {casino_money} денег")
		u_bet = input("Сколько поставишь денег? (только помни, не ставь больше, чем у тебя есть) ") 
		print(f"Ты поставил {u_bet}, казино поставило {casino_bet} чтож, играем!") 
		u_dice = random.randint(2, 12)
		casino_dice = random.randint(2, 12)
		print(f"Тебе выпало {u_dice}")
		print(f"Сопернику выпало {casino_dice}")
		if u_dice > casino_dice:
			print(f"Опа, плюс мани! у тебя{u_money}.")
			u_money += casino_dice
			show_gamble()
		elif u_dice < casino_dice:
			print(f"Минус мани, молодец чо,у тебя{u_money}. Иди работай, а не в казино рубись!")
			u_money -= u_dice
			show_gamble()
		else:
			print("Даже хз повезло тебе или нет.")
			show_gamble()
	elif u_choice == "нет" :
		print("Вы решили уйти обратно")
		show_location_primary
	else:
		print("Соберись и реши нормально, да или нет")
		show_gamble()


show_gamble()