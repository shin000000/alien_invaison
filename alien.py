import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien"""

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and set its rect attribute.
		#self.image = pygame.image.load('images/alien.bmp')
		#self.image = pygame.transform.scale(self.image, (80, 64))
		self.image_ori = pygame.image.load('images/donut6.png')
		self.image = self.image_ori.copy()
		#self.image = pygame.image.load('images/donut6.png')

		self.total_degree = 0
		self.rot_degree = 0.5

		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width / 2 
		self.rect.y = self.rect.height / 2 

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
			
	def update(self):
		 """move the alien to the right."""
		 self.rotate()
		 self.x += (self.settings.alien_speed * 
		 				self.settings.fleet_direction)
		 self.rect.x = self.x

	def rotate(self):
		"""rotate the alien when collide."""

		self.total_degree += self.rot_degree
		self.total_degree = self.total_degree % 360
		self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
		center = self.rect.center
		self.rect = self.image.get_rect()
		self.rect.center = center
