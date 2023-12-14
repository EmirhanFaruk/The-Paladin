"""
imma put da comments here
its 07/08/2022
now its 00:25 08/08/2022
i did the dialogue
i gotta make it so we'll have lines at the dialogues
the image thing now also works well
code is also a bit proper
still no start menu
i deserve a chocolate milk but there's none
imma go get some sleep ig

to do list:
-get the proper images, mirror and get them ready to use
-write a fucking proper code
-make a start menu
-dialogues? maybe

"""
import pygame
import os

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

#the directory
gf = os.getcwd()#C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\paladin
#print(gf)#it used \ ?



dialogue_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble.png")
idle_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble_old.png")

# Background
#\\assets\\UI\\
print(gf + "\\assets\\ui\\Game_Title.png")
game_title = pygame.image.load(gf + "\\assets\\ui\\Game_Title.png")
background = pygame.image.load(gf + "\\assets\\Backgrounds\\background.png")


monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

#alfred_severed_head = pygame.transform.scale(alfred_severed_head, (monitor_size[0]//8, monitor_size[0]//8))
dialogue_bubble = pygame.transform.scale(dialogue_bubble, (monitor_size[0], monitor_size[1]//4))
idle_bubble = pygame.transform.scale(idle_bubble, (monitor_size[0], monitor_size[1]//4))
background = pygame.transform.scale(background, (monitor_size[0], (monitor_size[1]//4) * 3))

# Title and icon
pygame.display.set_caption("The Paladin")
icon = pygame.image.load(gf + "\\assets\\icon\\Icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()




"""
#albert
#walking and standing
albertpic = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Idle\\Retard_Knight.png")
awr1 = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Walk\\Retard_Knight_walk_1.png")
awr2 = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Walk\\Retard_Knight_walk_2.png")
albertpic = pygame.transform.scale(albertpic, (128, 128))
albertpicl = pygame.transform.flip(albertpic, True, False)#reversing the scaled image
awr1 = pygame.transform.scale(awr1, (128, 128))
awr2 = pygame.transform.scale(awr2, (128, 128))
awl1 = pygame.transform.flip(awr1, True, False)
awl2 = pygame.transform.flip(awr2, True, False)
albertwalkr = [awr1, albertpic, awr2, albertpic]
albertwalkl = [awl1, albertpicl, awl2, albertpicl]

#attacking
aar1 = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Attack\\Retard_Knight_attack_1.png")
aar2 = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Attack\\Retard_Knight_attack_2.png")
aar3 = pygame.image.load(gf + "\\assets\\characters\\Alfred\\Attack\\Retard_Knight_attack_3.png")

aar1 = pygame.transform.scale(aar1, (128, 128))
aar2 = pygame.transform.scale(aar2, (128, 128))
aar3 = pygame.transform.scale(aar3, (128, 128))
aal1 = pygame.transform.flip(aar1, True, False)
aal2 = pygame.transform.flip(aar2, True, False)
aal3 = pygame.transform.flip(aar3, True, False)

albertattackr = [aar1, aar2, aar3]
albertattackl = [aal1, aal2, aal3]
"""



class Button:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        return
    
    def check_pressing(self, da_point):
        if da_point[0] > self.x and da_point[0] < self.x + self.w:
            if da_point[1] > self.y and da_point[1] < self.y + self.h:
                return  True        
        return False


class Text():
    def __init__(self, x, y, text, size, colour, duration, variable = "", speed = 0):
        self.x, self.y, self.size, self.colour, self.duration, self.speed = x, y, size, colour, duration, speed
        self.text = text
        self.variable = variable
        self.font = pygame.font.SysFont(gf + "\\assets\\font\\PKMN_RBYGSC.ttf", self.size)
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

class D_Text():
    def __init__(self, x, y, text, size, colour):
        self.x, self.y, self.size, self.colour = x, y, size, colour
        self.text = text
        self.font = pygame.font.SysFont(gf + "\\assets\\font\\PKMN_RBYGSC.ttf", self.size)
        self.text_surface = self.font.render(self.text, False, self.colour)
        self.text_width = self.text_surface.get_width()

    def draw(self, win):
        self.text_surface = self.font.render(self.text, False, self.colour)
        self.text_width = self.text_surface.get_width()
        win.blit(self.text_surface, (self.x - self.text_width/2, self.y))
        return


"""
class Player():
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
"""


class Player():
    def __init__(self, x, y, w, h, speed, img):
        self.x, self.y, self.w, self.h, self.speed, self.img = x, y, w, h, speed, img
        self.wc = 0#walk count
        self.wr, self.wl = False, False
        self.lr, self.ll = True, False
        self.wu, self.wd = False, False
        self.attacking = False
        self.ac = 0#attack count
        self.acc = 6#attack count cooldown

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
            if self.acc > 0:
                self.acc -= 1
            if ((self.wu or self.wd) or self.wr) and self.lr:
                win.blit(self.img[2][int(self.wc)%len(self.img[2])], (self.x, self.y))
            elif ((self.wu or self.wd) or self.wl) and self.ll:
                win.blit(self.img[3][int(self.wc)%len(self.img[3])], (self.x, self.y))
            else:
                self.wc = 0
                if self.lr:
                    win.blit(self.img[0], (self.x, self.y))
                else:
                    win.blit(self.img[1], (self.x, self.y))
            self.wc += self.speed/20#0.25
        else:
            self.wr = False
            self.wl = False
            self.wu = False
            self.wd = False
            if self.lr:
                win.blit(self.img[4][int(self.ac)%len(self.img[4])], (self.x, self.y))
                self.ac += self.speed/4#0.8
            elif self.ll:
                win.blit(self.img[5][int(self.ac)%len(self.img[5])], (self.x, self.y))
                self.ac += self.speed/4#0.8
            if int(self.ac) >= len(self.img[4]):
                self.ac = 0
                self.acc = 6
                self.attacking = False



def get_images(name):
    img_list = []#[idle, idle_reversed, walk_right, walk_left, attack_right, attack_left, head, name text]
    #idle 0
    #idler 1
    #walkr 2
    #walkl 3
    #attackr 4
    #attackl 5
    #head 6
    #nt 7
    #getting idle image
    loci = os.listdir(gf + "\\assets\\characters\\" + name + "\\Idle")
    idle = pygame.image.load(gf + "\\assets\\characters\\" + name + "\\Idle\\" + loci[0])
    idle = pygame.transform.scale(idle, (128, 128))#scaling image
    idlem = pygame.transform.flip(idle, True, False)#reversing the scaled image
    img_list.append(idle)
    img_list.append(idlem)
    #getting walk animation
    loc = os.listdir(gf + "\\assets\\characters\\" + name + "\\Walk")
    walk = []
    for i in range(len(loc)):
        walk.append(pygame.image.load(gf + "\\assets\\characters\\" + name + "\\Walk\\" + loc[i]))
        walk.append(pygame.image.load(gf + "\\assets\\characters\\" + name + "\\Idle\\" + loci[0]))
    for i in range(len(walk)):
        walk[i] = pygame.transform.scale(walk[i], (128, 128))
    walkm = []
    for i in range(len(walk)):
        walkm.append(pygame.transform.flip(walk[i], True, False))
    img_list.append(walk)
    img_list.append(walkm)
    #getting attack animation
    loc = os.listdir(gf + "\\assets\\characters\\" + name + "\\Attack")
    attack = []
    for i in range(len(loc)):
        attack.append(pygame.image.load(gf + "\\assets\\characters\\" + name + "\\Attack\\" + loc[i]))
    for i in range(len(attack)):
        attack[i] = pygame.transform.scale(attack[i], (128, 128))
    attackm = []
    for i in range(len(attack)):
        attackm.append(pygame.transform.flip(attack[i], True, False))
    img_list.append(attack)
    img_list.append(attackm)
    #getting severed head
    loc = os.listdir(gf + "\\assets\\characters\\" + name + "\\Head")
    head = pygame.image.load(gf + "\\assets\\characters\\" + name + "\\Head\\" + loc[0])
    head = pygame.transform.scale(head, (monitor_size[0]//8, monitor_size[0]//8))
    img_list.append(head)
    #getting text name
    img_list.append(D_Text(monitor_size[1]//6 , (monitor_size[1]//40) * 39, name, 50, (0, 0, 0)))

    del loci, loc, idle, idlem, walk, walkm, attack, attackm, head
    return img_list



albert_img = get_images("Albert")
paladin_img = get_images("Paladin")


def dialogue(text_list, person_list):
    if text_list != []:
        win.blit(dialogue_bubble, (0, (monitor_size[1]//4) * 3))
        da_text = Text((monitor_size[1]//12) * 9 , (monitor_size[1]//6) * 5, text_list[0], 100, (0, 0, 0), -1)
        da_text.draw(win, text_list)
        win.blit(person_list[0].img[6], ((monitor_size[0]//85) * 6, (monitor_size[1]//4) * 3))
        person_list[0].img[7].draw(win)
    else:
        win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))




albert = Player(100, 300, 128, 128, 5, albert_img)#speed was 5
paladin = Player(400, 300, 128, 128, 5, paladin_img)
paladin.ll = True
paladin.lr = False


#alfred_name_text = Text(monitor_size[1]//6 , (monitor_size[1]//40) * 39, "ALFRED", 50, (0, 0, 0), -1)
#fuck_you_text = Text((monitor_size[1]//12) * 9 , (monitor_size[1]//6) * 5, "Hello.", 100, (0, 0, 0), -1)
#texts = [albert_img[7], fuck_you_text]

dtl = ["Hey Albert", "Why don't you tell us", "A fun fact?", "The US war crimes", "Are the violation", " of the laws", "And customs of war", "Which", "The US armed forces", "Has commited", "Against signatories", "After the signing of", "The Hague Conventions", "Of 1899 and 1907.", "...", "I like cheesburgers"]#dialogue text list, about 20 character limit
dpl = [paladin, paladin, paladin, albert, albert, albert, albert, albert, albert, albert, albert, albert, albert, albert, paladin, albert]

running = True
while running:
    clock.tick(30)
    #win.fill((150, 150, 150))
    win.blit(background, ((0, 0)))
    #win.blit(dialogue_bubble, (0, (monitor_size[1]//4) * 3))
    #win.blit(alfred_severed_head, ((monitor_size[0]//85) * 6, ((monitor_size[1]//32) * 25) + monitor_size[1]//85))
    #win.blit(alfred_severed_head, ((monitor_size[0]//85) * 6, (monitor_size[1]//4) * 3))
    #for text in texts:
        #text.draw(win, texts)
    #alfred_name_text.draw(win, texts)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dtl:
                dtl.pop(0)
                dpl.pop(0)

    dialogue(dtl, dpl)

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False


    if not dtl:
        if not albert.attacking:
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
            if keys[pygame.K_SPACE] and albert.acc <= 0:
                albert.attacking = True
                albert.wr, albert.wl, albert.wd, albert.wu = False, False, False, False
        
    albert.move(monitor_size)
    albert.draw(win)
    paladin.draw(win)


    pygame.display.update()



