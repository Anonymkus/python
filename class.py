class Unit:
	hp = 100
	name = "entity"
	def __init__(self):
		self.eyecolor = "black"


class Zombie(Unit):
	name = Unit.name * 2
	hunger = 0
	


enemy = Zombie()
NOTenemy = Unit()

Unit.color = "purple"

print(NOTenemy.hp)
print(NOTenemy.name)
print(enemy.hp)
print(enemy.name)
print(NOTenemy.color)
print(enemy.color)
print(NOTenemy.eyecolor)
print(enemy.eyecolor)
