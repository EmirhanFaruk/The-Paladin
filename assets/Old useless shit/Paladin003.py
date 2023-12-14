"""
imma put da comments here
gonna try the resized image so hyped rn -_-
its 9:55 28/07/2022
fuck it didnt work
the resized looks like shit
without the fullscreen it works tho

done in 10:30 28/07/2022
gonna go have my breakfast


aight im b(l)ack
gonna test the tff file
"""
import pygame

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


# Background
background = pygame.image.load("Game_Title.png")
background2 = pygame.image.load("background.png")
dialogue_bubble = pygame.image.load("dialogue_bubble.png")
alfred_severed_head = pygame.image.load("Retard_Knight_Head.png")


monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

alfred_severed_head = pygame.transform.scale(alfred_severed_head, (monitor_size[0]//8, monitor_size[0]//8))
dialogue_bubble = pygame.transform.scale(dialogue_bubble, (monitor_size[0], monitor_size[1]//4))
background2 = pygame.transform.scale(background2, (monitor_size[0], (monitor_size[1]//4) * 3))

# Title and icon
pygame.display.set_caption("Paladin")
icon = pygame.image.load("paladin.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()



#the Paladin
paladinr = pygame.image.load("paladin.png")




#albert
#walking and standing
albertpic = pygame.image.load("Retard_Knight.png")
albertpicl = pygame.image.load("Retard_Knight_Left.png")
awr1 = pygame.image.load("Retard_Knight_walk_1.png")
awr2 = pygame.image.load("Retard_Knight_walk_2.png")
awl1 = pygame.image.load("Retard_Knight_walkl_1.png")
awl2 = pygame.image.load("Retard_Knight_walkl_2.png")
albertpic = pygame.transform.scale(albertpic, (128, 128))
albertpicl = pygame.transform.scale(albertpicl, (128, 128))
awr1 = pygame.transform.scale(awr1, (128, 128))
awr2 = pygame.transform.scale(awr2, (128, 128))
awl1 = pygame.transform.scale(awl1, (128, 128))
awl2 = pygame.transform.scale(awl2, (128, 128))
albertwalkr = [awr1, albertpic, awr2, albertpic]
albertwalkl = [awl1, albertpicl, awl2, albertpicl]

#attacking
aar1 = pygame.image.load("Retard_Knight_attack_1.png")
aar2 = pygame.image.load("Retard_Knight_attack_2.png")
aar3 = pygame.image.load("Retard_Knight_attack_3.png")
aal1 = pygame.image.load("Retard_Knight_attackl_1.png")
aal2 = pygame.image.load("Retard_Knight_attackl_2.png")
aal3 = pygame.image.load("Retard_Knight_attackl_3.png")

aar1 = pygame.transform.scale(aar1, (128, 128))
aar2 = pygame.transform.scale(aar2, (128, 128))
aar3 = pygame.transform.scale(aar3, (128, 128))
aal1 = pygame.transform.scale(aal1, (128, 128))
aal2 = pygame.transform.scale(aal2, (128, 128))
aal3 = pygame.transform.scale(aal3, (128, 128))

albertattackr = [aar1, aar2, aar3]
albertattackl = [aal1, aal2, aal3]




class Text():
    def __init__(self, x, y, text, size, colour, duration, variable = "", speed = 0):
        self.x, self.y, self.size, self.colour, self.duration, self.speed = x, y, size, colour, duration, speed
        self.text = text
        self.variable = variable
        self.font = pygame.font.SysFont('PKMN_RBYGSC.ttf', self.size)
        self.text_surface = self.font.render(self.text, False, self.colour)
        self.text_width = self.text_surface.get_width()

    def draw(self, win, texts):
        if self.duration == 0:
            texts.remove(self)
        if self.duration != -1:
            self.duration -= 1
        self.text_surface = self.font.render(self.text + str(self.variable), False, self.colour)
        self.text_width = self.text_surface.get_width()
        win.blit(self.text_surface, (self.x - self.text_width/2, self.y))
        self.y -= self.speed
        return




class Paladin():
    def __init__(self, x, y, w, h, direction, basedamage, basehealth, basespeed):
        self.x, self.y, self.w, self.h, self.direction, self.basedamage, self.basehealth, self.basespeed = x, y, w, h, direction, basedamage, basehealth, basespeed
        




class Albert():
    def __init__(self, x, y, w, h, speed):
        self.x, self.y, self.w, self.h, self.speed = x, y, w, h, speed
        self.wc = 0
        self.wr, self.wl = False, False
        self.lr, self.ll = True, False
        self.wu, self.wd = False, False
        self.attacking = False
        self.ac = 0
        self.acc = 0

    def move(self, monitor_size):
        if self.wr and self.x + self.w + self.speed < monitor_size[0]:
            self.x += self.speed
        elif self.wl and self.x - self.speed > 0 :
            self.x -= self.speed
        else:
            self.wr, self.wl = False, False
        if self.wu and self.y - self.speed > 0:
            self.y -= self.speed
        elif self.wd and self.y + self.h + self.speed < (monitor_size[1]//4) * 3:
            self.y += self.speed
        else:
            self.wu, self.wd = False, False

    def draw(self, win):
        if not self.attacking:
            if ((self.wu or self.wd) or self.wr) and self.lr:
                win.blit(albertwalkr[int(self.wc)%len(albertwalkr)], (self.x, self.y))
            elif ((self.wu or self.wd) or self.wl) and self.ll:
                win.blit(albertwalkl[int(self.wc)%len(albertwalkl)], (self.x, self.y))
            else:
                self.wc = 0
                if self.lr:
                    win.blit(albertpic, (self.x, self.y))
                else:
                    win.blit(albertpicl, (self.x, self.y))
            self.wc += 0.25
        else:
            self.wr = False
            self.wl = False
            self.wu = False
            self.wd = False
            if self.lr:
                win.blit(albertattackr[int(self.ac)%len(albertattackr)], (self.x, self.y))
                self.ac += 0.8
            elif self.ll:
                win.blit(albertattackl[int(self.ac)%len(albertattackl)], (self.x, self.y))
                self.ac += 0.8
            if int(self.ac) == len(albertattackr):
                self.ac = 0
                self.acc = 5
                self.attacking = False








alfred_name_text = Text(monitor_size[1]//6 , (monitor_size[1]//40) * 39, "ALFRED", 50, (0, 0, 0), -1)
fuck_you_text = Text((monitor_size[1]//12) * 9 , (monitor_size[1]//6) * 5, "Hello.", 100, (0, 0, 0), -1)
texts = [alfred_name_text, fuck_you_text]

albert = Albert(100, 300, 128, 128, 5)
running = True
while running:
    clock.tick(30)
    #win.fill((150, 150, 150))
    win.blit(background2, ((0, 0)))
    win.blit(dialogue_bubble, (0, (monitor_size[1]//4) * 3))
    #win.blit(alfred_severed_head, ((monitor_size[0]//85) * 6, ((monitor_size[1]//32) * 25) + monitor_size[1]//85))
    win.blit(alfred_severed_head, ((monitor_size[0]//85) * 6, (monitor_size[1]//4) * 3))
    for text in texts:
        text.draw(win, texts)
    #alfred_name_text.draw(win, texts)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    if albert.acc > 0:
        albert.acc -= 1

    if keys[pygame.K_LEFT]:
        albert.wl = True
        albert.wr = False
        albert.ll = True
        albert.lr = False
    elif keys[pygame.K_RIGHT]:
        albert.wr = True
        albert.wl = False
        albert.ll = False
        albert.lr = True
    if keys[pygame.K_UP]:
        albert.wu = True
        albert.wd = False
    elif keys[pygame.K_DOWN]:
        albert.wd = True
        albert.wu = False
    if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
        albert.wr, albert.wl = False, False
    if not (keys[pygame.K_DOWN] or keys[pygame.K_UP]):
        albert.wd, albert.wu = False, False
    if keys[pygame.K_SPACE]:
        if albert.acc <= 0:
            albert.attacking = True
            albert.wr, albert.wl, albert.wd, albert.wu = False, False, False, False
        
    albert.move(monitor_size)
    albert.draw(win)


    pygame.display.update()



