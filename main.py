from pygame import *

WIDTH = 800
HEIGHT = 600


window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("ping-pong")

background = transform.scale(image.load("stol.jpg"), (WIDTH, HEIGHT))


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

