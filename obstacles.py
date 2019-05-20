import pygame
import os


class saw(object):
    img  = [pygame.image.load(os.path.join('images', 'SAW0.png')),
            pygame.image.load(os.path.join('images', 'SAW1.png')),
            pygame.image.load(os.path.join('images', 'SAW2.png')),
            pygame.image.load(os.path.join('images', 'SAW3.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0

    def draw(self, screen):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        if self.count >= 8:
            self.count = 0
        screen.blit(pygame.transform.scale(self.img[self.count//2], (64, 64)), (self.x, self.y))
        self.count += 1
     #   pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                print('Saw')
                return True
        return False

class spike(saw):
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self, screen):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        screen.blit(self.img, (self.x, self.y))
      # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                print('Spike')
                return True
        return False
