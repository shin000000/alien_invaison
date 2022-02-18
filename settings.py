import pygame

class Settings:
    """ A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """initializing the game's static settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_scale = (self.screen_width, self.screen_height)
        self.bg_color = (255, 153, 255)

        # caption and icon
        pygame.display.set_caption("僕のドーナツはどこだ?")
        pygame.display.set_icon(pygame.image.load('images/ship.bmp'))
        
        #ship settings
        #self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        #self.bullet_width = 3
        #self.bullet_height = 15
        self.bullet_width = 15
        self.bullet_height = 20
        self.bullet_scale = (self.bullet_width, self.bullet_height)
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # background image settings
        self.bg_img = pygame.image.load('images/bg.bmp')
        self.bg_img = pygame.transform.scale(self.bg_img, self.screen_scale)
        self.bg_img_2 = pygame.image.load('images/bg2.bmp')
        self.bg_img_2 = pygame.transform.scale(self.bg_img_2, self.screen_scale)

    def initialize_dynamic_settings(self):
            """initialize settings that change throughout the game. """
            # self.ship_speed = 1.5
            # self.bullet_speed = 3.0
            # self.alien_speed = 1.0
            self.ship_speed = 5
            self.bullet_speed = 9
            self.alien_speed = 4

            self.alien_points = 50

            #fleet direction of 1 represents right; -1 represents left.
            self.fleet_direction = 1

    def increase_speed(self):
            """increase speed settings and slien point values"""
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale

            self.alien_points = int(self.alien_points * self.score_scale)
            print(self.alien_points)









