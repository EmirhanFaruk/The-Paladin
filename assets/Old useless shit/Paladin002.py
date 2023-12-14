import pygame

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


# Background
background = pygame.image.load("Game_Title.png")
background2 = pygame.image.load("background.png")
#background2 = pygame.image.load("background2.png")
#background3 = pygame.image.load("background3.png")

background2 = pygame.transform.scale(background2, (width, height))

# Title and icon
pygame.display.set_caption("Paladin")
icon = pygame.image.load("paladin.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()



#for now imma finish at 19:03 27/07/2022
#tfw i realize i have to do the animations myself
#-_-
#for now only the image
paladinr = pygame.image.load("paladin.png")




#albert
#walking and standing
albertpic = pygame.image.load("Retard_Knight.png")
albertpicl = pygame.image.load("Retard_Knight_Left.png")
awr1 = pygame.image.load("Retard_Knight_walk_1.png")
awr2 = pygame.image.load("Retard_Knight_walk_2.png")
awl1 = pygame.image.load("Retard_Knight_walkl_1.png")
awl2 = pygame.image.load("Retard_Knight_walkl_2.png")
albertpic = pygame.transform.scale(albertpic, (64, 64))
albertpicl = pygame.transform.scale(albertpicl, (64, 64))
awr1 = pygame.transform.scale(awr1, (64, 64))
awr2 = pygame.transform.scale(awr2, (64, 64))
awl1 = pygame.transform.scale(awl1, (64, 64))
awl2 = pygame.transform.scale(awl2, (64, 64))
albertwalkr = [awr1, albertpic, awr2, albertpic]
albertwalkl = [awl1, albertpicl, awl2, albertpicl]

#attacking
aar1 = pygame.image.load("Retard_Knight_attack_1.png")
aar2 = pygame.image.load("Retard_Knight_attack_2.png")
aar3 = pygame.image.load("Retard_Knight_attack_3.png")
aal1 = pygame.image.load("Retard_Knight_attackl_1.png")
aal2 = pygame.image.load("Retard_Knight_attackl_2.png")
aal3 = pygame.image.load("Retard_Knight_attackl_3.png")

aar1 = pygame.transform.scale(aar1, (64, 64))
aar2 = pygame.transform.scale(aar2, (64, 64))
aar3 = pygame.transform.scale(aar3, (64, 64))
aal1 = pygame.transform.scale(aal1, (64, 64))
aal2 = pygame.transform.scale(aal2, (64, 64))
aal3 = pygame.transform.scale(aal3, (64, 64))

albertattackr = [aar1, aar2, aar3]
albertattackl = [aal1, aal2, aal3]

class Paladin():
    def __init__(self, x, y, w, h, direction, basedamage, basehealth, basespeed):
        self.x, self.y, self.w, self.h, self.direction, self.basedamage, self.basehealth, self.basespeed = x, y, w, h, direction, basedamage, basehealth, basespeed
        
#smh already spent half an hour on this shit including the paladin image, done in 00:09 in 27.07.2022 

class Albert():
    def __init__(self, x, y, w, h, speed):
        self.x, self.y, self.w, self.h, self.speed = x, y, w, h, speed
        self.wc = 0
        self.wr = False
        self.wl = False
        self.lr = True
        self.ll = False
        self.attacking = False
        self.ac = 0

    def move(self):
        if self.wr:
            self.x += self.speed
        elif self.wl:
            self.x -= self.speed
        else:
            self.wr, self.wl = False, False

    def draw(self, win):
        if not self.attacking:
            if self.wr:
                win.blit(albertwalkr[int(self.wc)%len(albertwalkr)], (self.x, self.y))
                self.wc += 0.3
            elif self.wl:
                win.blit(albertwalkl[int(self.wc)%len(albertwalkl)], (self.x, self.y))
                self.wc += 0.3
            else:
                self.wc = 0
                if self.lr:
                    win.blit(albertpic, (self.x, self.y))
                else:
                    win.blit(albertpicl, (self.x, self.y))
        else:
            self.wr = False
            self.wl = False
            if self.lr:
                win.blit(albertattackr[int(self.ac)%len(albertattackr)], (self.x, self.y))
                self.ac += 0.8
            elif self.ll:
                win.blit(albertattackl[int(self.ac)%len(albertattackl)], (self.x, self.y))
                self.ac += 0.8
            if int(self.ac) == len(albertattackr):
                self.ac = 0
                self.attacking = False










albert = Albert(100, 300, 16, 16, 5)
running = True
while running:
    clock.tick(30)
    #win.fill((150, 150, 150))
    win.blit(background2, ((0, 0)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        albert.wl = True
        albert.ll = True
        albert.lr = False
    if keys[pygame.K_RIGHT]:
        albert.wr = True
        albert.ll = False
        albert.lr = True
    if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
        albert.wr, albert.wl = False, False
    if keys[pygame.K_SPACE]:
        albert.attacking = True

    albert.move()
    albert.draw(win)


    pygame.display.update()



