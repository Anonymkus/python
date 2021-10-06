import random

def multi(number: int) -> int:
	"""
	   1.Понятное имя функции
	   2.Понятные аргументы
	   3.Аннотации типов(number: int)
	   4.Что возвращает(-> int)
	   5.Докстрока    
	"""
	number *= 2
	return number

result = multi(15)  
print(result)


def count_logs(forest_depth: int) -> int:
	logs = 2 * forest_depth
	return logs


print(count_logs(1.0))


def stitch_in_time(saves_nine: float) -> float:
	time = 1 / saves_nine
	return time


print(stitch_in_time(15.0))


def calculate_speed(time: float, distance:float) -> float:
	speed = distance / time
	return speed


print(calculate_speed(60, 30))


def play_dice(bet):
	gain = 0
	u_dice = random.randint(2, 12)
	casino_dice = random.randint(2, 12)
	if u_dice > casino_dice:
		gain += bet
	elif u_dice < casino_dice:
		gain -= bet
	else:
		print("draw")
	return gain


u_money = 10000
print(u_money)
u_money += play_dice(500)
print(u_money)
