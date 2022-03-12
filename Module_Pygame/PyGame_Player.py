import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, screen):
		super().__init__()
		self.image = pygame.Surface((25, 175))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.center = (25, 300)


	def update(self):
		pass
