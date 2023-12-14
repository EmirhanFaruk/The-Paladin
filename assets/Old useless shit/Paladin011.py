"""
imma put da comments here
started in the morning 10/08/2022 11:58
aight bois lets go
had a 10 min breakfast at 12:30
duh i realized i cant do things simultaniously(yes that thing that i cant write) if i use this system, but for now it shouldnt be a problem as this is just a demo
its 14:06(i also went outside etc)
its 00:10 12/08/2022

to do list:
-write a fucking proper code
-write a function that does scripts - partly done, gonna add fading away effect
-add combat
-finish the demo

"""
import pygame
import os

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

#the directory
gf = os.getcwd()#C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\paladin


dialogue_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble.png")
idle_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble_old.png")

# Background
#\\assets\\UI\\
game_title = pygame.image.load(gf + "\\assets\\ui\\Game_Title.png")
background = pygame.image.load(gf + "\\assets\\Backgrounds\\background.png")
backgrounds = [game_title, background]
bg_stage = 0
for i in range(len(backgrounds)):
    backgrounds[i] = pygame.transform.scale(backgrounds[i], (monitor_size[0], (monitor_size[1]//4) * 3))
backgrounds[0] = pygame.transform.scale(backgrounds[0], (monitor_size[0], monitor_size[1]))


#alfred_severed_head = pygame.transform.scale(alfred_severed_head, (monitor_size[0]//8, monitor_size[0]//8))
dialogue_bubble = pygame.transform.scale(dialogue_bubble, (monitor_size[0], monitor_size[1]//4))
idle_bubble = pygame.transform.scale(idle_bubble, (monitor_size[0], monitor_size[1]//4))



# Title and icon
pygame.display.set_caption("The Paladin")
icon = pygame.image.load(gf + "\\assets\\icon\\Icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


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

"""
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
"""

class D_Text():
    def __init__(self, x, y, text, size, colour, width_limit):#limit will be either 800 or smtg else, gotta specify bc of the narrator thing
        self.x, self.y, self.size, self.colour = x, y, size, colour
        self.text = text
        self.text_list = []
        self.font = pygame.font.SysFont(gf + "\\assets\\font\\PKMN_RBYGSC.ttf", self.size)
        self.text_surface = self.font.render(self.text, False, self.colour)
        self.text_width = self.text_surface.get_width()
        if self.text_width > width_limit:
            while self.text_width > width_limit:
                text_word_list = []
                word = ""
                for index in range(len(text)):
                    if index == len(text) - 1:
                        word = word + text[index]
                        text_word_list.append(word)
                        self.text = ""
                        break
                    if text[index] != " ":
                        word = word + text[index]
                    else:
                        word = word + " "
                        text_word_list.append(word)
                        word = ""
                    self.text = text[index:]
                self.text_surface = self.font.render(self.text, False, self.colour)
                self.text_width = self.text_surface.get_width()
            sentence_part_counter = -1
            self.text_list.append("")
            self.text_list[0] = self.text_list[0] + text_word_list[0]
            text_word_list.pop(0)
            self.text_surface = self.font.render(self.text_list[0], False, self.colour)
            self.text_width = self.text_surface.get_width()
            full_words = ""
            for word in text_word_list:
                full_words = full_words + word
            self.text_surface2 = self.font.render(full_words, False, self.colour)
            self.text_width2 = self.text_surface2.get_width()
            while self.text_width2 > width_limit:
                sentence_part_counter += 1
                self.text_list[sentence_part_counter] = self.text_list[sentence_part_counter] + text_word_list[0]
                text_word_list.pop(0)
                self.text_surface = self.font.render(self.text_list[sentence_part_counter], False, self.colour)
                self.text_width = self.text_surface.get_width()
                while self.text_width <= width_limit and text_word_list != []:
                    self.text_list[sentence_part_counter] = self.text_list[sentence_part_counter] + text_word_list[0]
                    
                    self.text_surface = self.font.render(self.text_list[sentence_part_counter], False, self.colour)
                    self.text_width = self.text_surface.get_width()
                    if self.text_width > width_limit:
                        self.text_list[sentence_part_counter] = self.text_list[sentence_part_counter][:len(self.text_list[sentence_part_counter]) - len(text_word_list[0])]
                        break
                    else:
                        text_word_list.pop(0)
                    
                full_words = ""
                for word in text_word_list:
                    full_words = full_words + word
                self.text_surface2 = self.font.render(full_words, False, self.colour)
                self.text_width2 = self.text_surface2.get_width()
                self.text_list.append("")
            if full_words != "":
                self.text_list[-1] = full_words#self.text_list.append(full_words)
        else:
            self.text_list.append(text)

    def draw(self, win):
        decalage = -self.size * 3/4
        for sentence_part in self.text_list:
            decalage = decalage + (self.size * 3/4)
            self.text_surface = self.font.render(sentence_part, False, self.colour)
            win.blit(self.text_surface, (int(self.x), int(self.y) + decalage))
        return


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
    img_list.append(D_Text(monitor_size[0] * 0.05 , monitor_size[1] * 0.94, name, 50, (0, 0, 0), monitor_size[0] * 0.69))#its actually too much but idc tbh it wont be seen in the game i hope

    del loci, loc, idle, idlem, walk, walkm, attack, attackm, head
    return img_list



albert_img = get_images("Albert")
paladin_img = get_images("Paladin")


def dialogue(text_list):
    if text_list != []:
        if text_list[0][0] != "wait func" and text_list[0][0] != "move func":
            if text_list[0][1] != "narrator":
                win.blit(dialogue_bubble, (0, (monitor_size[1]//4) * 3))
                text_list[0][0].draw(win)
                win.blit(text_list[0][1].img[6], ((monitor_size[0]//85) * 6, (monitor_size[1]//4) * 3))
                text_list[0][1].img[7].draw(win)
            else:
                win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
                text_list[0][0].draw(win)
        else:
            win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
    else:
        win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))





albert = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, monitor_size[0]/250, albert_img)#speed was 5
paladin = Player(monitor_size[0] * 4/5, monitor_size[1]//4, 128, 128, monitor_size[0]/250, paladin_img)#the y was 300
paladin.ll = True
paladin.lr = False
bandit_img = get_images("Bandit")
bandit1 = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, monitor_size[0]/200, get_images("Bandit"))
bandit2 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 - monitor_size[1] * 0.07, 128, 128, monitor_size[0]/200, get_images("Bandit"))
bandit3 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 + monitor_size[1] * 0.07, 128, 128, monitor_size[0]/200, get_images("Bandit"))
characters = [albert, paladin, bandit1, bandit2, bandit3]

dtl1 = [["Our story begins with the end of another one, The paladin, the bravest soldier of the king's army is guarding the gates at the entrance of the town, but something seems off.", "narrator"], ["move func", [[characters[0], ["wr", "lr"]]], 270], ["wait func", 15], ["You still here?", characters[0]], ["wait func", 60], ["You should get going my friend, we have nothing to do... The town has been destroyed. You can see it by yourself.", characters[0]], ["wait func", 60], ["Look back! At the gates! Don't you see the destruction?!", characters[0]], ["I made a promise to the king, I promised that I'll guard this gates until the day I perish.", characters[1]], ["Bu-but there are no people to protect anymore! The king's de-", characters[0]], ["move func", [[characters[0], ["ll"]]], 10], ["move func", [[characters[2], ["wr", "lr"]], [characters[3], ["wr", "lr"]], [characters[4], ["wr", "lr"]]], 540], ["wait func", 30], ["You guys got nothing to do!!", characters[2]], ["En garde!", characters[1]]]
dtl = []
for i in range(len(dtl1)):
    if dtl1[i][0] != "wait func" and dtl1[i][0] != "move func":
        if dtl1[i][1] != "narrator":
            dtl1[i][0] = D_Text(monitor_size[0] * 0.26 , monitor_size[1] * 0.78, dtl1[i][0], 50, (0, 0, 0), monitor_size[0] * 0.69)#0.69 is the ratio for the dialogue bubble with the head(funny reddit number) 
        else:
            dtl1[i][0] = D_Text(monitor_size[0] * 0.05 , monitor_size[1] * 0.78, dtl1[i][0], 50, (0, 0, 0), monitor_size[0] * 0.85)


def draw_screen():
    win.blit(backgrounds[bg_stage], ((0, 0)))
    if bg_stage != 0:
        dialogue(dtl)
        for character in characters:
            character.move(monitor_size)
            character.draw(win)


def wait(counter):
    if counter > 0:
        counter -= 1
    return counter

def script_ds(wc, cl):
    if wc > 0:
        wc -= 1
        if "wr" in cl[1]:
            cl[0].wr = True
            cl[0].wl = False
        elif "wl" in cl[1]:
            cl[0].wl = True
            cl[0].wr = False
        if "wu" in cl[1]:
            cl[0].wu = True
            cl[0].wd = False
        elif "wd" in cl[1]:
            cl[0].wd = True
            cl[0].wu = False
        if "lr" in cl[1]:
            cl[0].lr = True
            cl[0].ll = False
        elif "ll" in cl[1]:
            cl[0].ll = True
            cl[0].lr = False
    else:
        cl[0].wr, cl[0].wl, cl[0].wu, cl[0].wd = False, False, False, False
    return wc, cl


def fade_gb(width, height, win, backgrounds, bgs, bgsw): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    alpha = 0
    while alpha <= 255:
        fade.set_alpha(alpha)
        win.blit(backgrounds[bg_stage], ((0, 0)))
        if bgs != 0:
            dialogue(dtl)
            draw_screen()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
        alpha += 1
    return False, bgsw
def fade_cb(width, height, win, backgrounds, bgs, bgsw): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    alpha = 255
    while alpha > -1:
        fade.set_alpha(alpha)
        draw_screen()
        dialogue(dtl)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
        alpha -= 1
    return False, 1

def move_c(character, keys):
    if not character.attacking:
        if keys[pygame.K_LEFT]:
            character.wl = True
            character.wr = False
            character.ll = True
            character.lr = False
        elif keys[pygame.K_RIGHT]:
            character.wr = True
            character.wl = False
            character.ll = False
            character.lr = True
        if keys[pygame.K_UP]:
            character.wu = True
            character.wd = False
        elif keys[pygame.K_DOWN]:
            character.wd = True
            character.wu = False
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            character.wr, character.wl = False, False
        if not (keys[pygame.K_DOWN] or keys[pygame.K_UP]):
            character.wd, character.wu = False, False
        if keys[pygame.K_SPACE] and character.acc <= 0:
            character.attacking = True
            character.wr, character.wl, character.wd, character.wu = False, False, False, False
    return character


                            
will_fade = False
fcb = False

wait_counter = 30
walk_counter = 270
first_script = True

running = True
while running:
    clock.tick(30)
    #win.blit(backgrounds[bg_stage], ((0, 0)))
    if bg_stage == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                
                will_fade = True
                fcb = True
    if will_fade:
        will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
    
    elif bg_stage == 1:
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
            if not fcb:
                dtl = dtl1
        if not fcb:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if dtl != []:
                        if event.key == pygame.K_SPACE and dtl[0][0] != "wait func" and dtl[0][0] != "move func":
                            dtl.pop(0)
            
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_ESCAPE]:
                running = False

            dialogue(dtl)
            if dtl != []:
                if dtl[0][0] == "wait func":
                    if dtl[0][1] > 0:
                        dtl[0][1] = wait(dtl[0][1])
                    else:
                        dtl.pop(0)
                if dtl[0][0] == "move func":
                    if dtl[0][2] > 0:
                        for index in range(len(dtl[0][1])):
                            dtl[0][2], dtl[0][1][index] = script_ds(dtl[0][2], dtl[0][1][index])
                    else:
                        for index in range(len(dtl[0][1])):
                            dtl[0][1][index][0].wr, dtl[0][1][index][0].wl, dtl[0][1][index][0].wu, dtl[0][1][index][0].wd = False, False, False, False
                        dtl.pop(0)
                    
            if dtl == []:
                characters[1] = move_c(characters[1], keys)
                
            
    

    draw_screen()
    pygame.display.update()



