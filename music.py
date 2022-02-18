import pygame
from pygame import mixer

class Music:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.play_bgm()

    def play_bgm(self):
        mixer.init()
        mixer.music.load('images/bgm.mp3')
        mixer.music.play(-1)

