import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))


# Background
#background1 = pygame.image.load("background1.png")
#background2 = pygame.image.load("background2.png")
#background3 = pygame.image.load("background3.png")

# Title and icon
pygame.display.set_caption("Paladin")
icon = pygame.image.load("paladin.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()

#tfw i realize i have to do the animations myself
#-_-
#for now only the image
paladinr = pygame.image.load("paladin.png")

class Paladin():
    def __init__(self, x, y, w, h, direction, basedamage, basehealth, basespeed):
        self.x, self.y, self.w, self.h, self.direction, self.basedamage, self.basehealth, self.basespeed = x, y, w, h, direction, basedamage, basehealth, basespeed
        
#smh already spent half an hour on this shit including the paladin image, done in 00:09 in 27.07.2022 
