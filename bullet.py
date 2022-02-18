import pygame
import random
import os
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired form the ship"""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = ai_game.screen 
		self.settings = ai_game.settings
		#self.color = self.settings.bullet_color

		# create a bullet rect at (0, 0) and then set correct position.
		#self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
		#	self.settings.bullet_height)
		self.images = []
		for i in range(7):
			# self.images.append(pygame.image.load(os.path.join("images", 
			# 	f"heart{i}.png")).convert())
			self.images.append(pygame.image.load(os.path.join("images", 
				f"heart{i}.png")))
		self.image = random.choice(self.images)

		#self.image = pygame.image.load('images/heart0.png')
		self.image = pygame.transform.scale(self.image, self.settings.bullet_scale)
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.ship.rect.midtop

		#store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y -= self.settings.bullet_speed
		# Update the rect position.
		self.rect.y = self.y

	def blitme(self):
		""""Draw the bullet to the screen."""
		#pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)