"""
imma put da comments here
started in 30/08/2022 15:28
gonna fix the bandit names, the endings. Also gonna add the intro and maybe the outro?
its 17:38, added intro, fixed the bandit names and the combat names.
its 18:21, i the only thing that isnt done is a sound system and sounds, and an ending credits
its 20:01, i think the game(demo) is done, imma record and see
yep it works but sadly it doesnt record the sound for some reason


to do list:
-write a fucking proper code
-the image of the paladin seems off when looking right and left rapidly, maybe change its coordinates when he changes his way he's looking?(a friend said its not a big deal)
-write a function that does scripts - partly done, gonna add fading away effect
-finish the demo

"""
import pygame
import os
from random import choice, randint

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

#the directory
gf = os.getcwd()#C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\paladin

#sounds
pygame.mixer.set_num_channels(100)
die_sound_effect = pygame.mixer.Sound(gf + "\\assets\\sounds\\crying-emoji-dies.mp3")
die_sound_effect2 = pygame.mixer.Sound(gf + "\\assets\\sounds\\wilhelm-scream-sound-effect.mp3")
die_sound_effect.set_volume(0.2)
death_list = [die_sound_effect, die_sound_effect2]

combat_sound = pygame.mixer.Sound(gf + "\\assets\\sounds\\mount-blade-warband-ost-bandit-fight (1).mp3")#bird-chirping-sound-effect.mp3

bird_sound = pygame.mixer.Sound(gf + "\\assets\\sounds\\bird-chirping-sound-effect.mp3")

game_over_sound_effect = pygame.mixer.Sound(gf + "\\assets\\sounds\\that-nigga-gay.mp3")
startup_sound = pygame.mixer.Sound(gf + "\\assets\\sounds\\gameboy-startup-sound.mp3")

sword1 = pygame.mixer.Sound(gf + "\\assets\\sounds\\sword-cut-fx.wav")
sword2 = pygame.mixer.Sound(gf + "\\assets\\sounds\\sword-cut-fx-2.wav")
sword3 = pygame.mixer.Sound(gf + "\\assets\\sounds\\sword-cut-fx-3.wav")
sword4 = pygame.mixer.Sound(gf + "\\assets\\sounds\\sword-sfx-4.mp3")
sword_list = [sword1, sword2, sword3, sword4]

speak_blip = pygame.mixer.Sound(gf + "\\assets\\sounds\\dialogue-blip.mp3")


dialogue_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble.png")
idle_bubble = pygame.image.load(gf + "\\assets\\ui\\dialogue_bubble_old.png")
combat_bubble = pygame.image.load(gf + "\\assets\\ui\\combat_bubble.png")

#cursor
pygame.mouse.set_visible(False)
cursor = pygame.image.load(gf + "\\assets\\cursor\\cursor.png")
cursor_click = pygame.image.load(gf + "\\assets\\cursor\\cursor_click.png")
cursor = pygame.transform.scale(cursor, (64, 64))
cursor_click = pygame.transform.scale(cursor_click, (64, 64))

# Background
#\\assets\\UI\\
game_title = pygame.image.load(gf + "\\assets\\ui\\Game_Title.png")
background = pygame.image.load(gf + "\\assets\\Backgrounds\\background.png")
background = pygame.transform.scale(background, (monitor_size[0], (monitor_size[1]//4) * 3))
game_intro_1 = pygame.image.load(gf + "\\assets\\Backgrounds\\game_intro_1.png")
game_intro_2 = pygame.image.load(gf + "\\assets\\Backgrounds\\game_intro_2.png")
credit1 = pygame.image.load(gf + "\\assets\\Backgrounds\\credits_1.png")
credit2 = pygame.image.load(gf + "\\assets\\Backgrounds\\credits_2.png")
credit1 = pygame.transform.scale(credit1, (monitor_size[0], monitor_size[1]))
credit2 = pygame.transform.scale(credit2, (monitor_size[0], monitor_size[1]))


backgrounds = [game_intro_1, game_intro_2, game_title, background, background, background, credit1, credit2]
bg_stage = 0
for i in range(3):
    backgrounds[i] = pygame.transform.scale(backgrounds[i], (monitor_size[0], monitor_size[1]))


#alfred_severed_head = pygame.transform.scale(alfred_severed_head, (monitor_size[0]//8, monitor_size[0]//8))
dialogue_bubble = pygame.transform.scale(dialogue_bubble, (monitor_size[0], monitor_size[1]//4))
idle_bubble = pygame.transform.scale(idle_bubble, (monitor_size[0], monitor_size[1]//4))
combat_bubble = pygame.transform.scale(combat_bubble, (monitor_size[0], monitor_size[1]//4))


# Title and icon
pygame.display.set_caption("The Paladin")
icon = pygame.image.load(gf + "\\assets\\icon\\Icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


class Button:
    def __init__(self, x, y, w, h, tag):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tag = tag
        self.image = pygame.image.load(gf + "\\assets\\ui\\buttons\\" + tag + "_button.png")
        self.image_hover = pygame.image.load(gf + "\\assets\\ui\\buttons\\" + tag + "_button_hover.png")
        self.image = pygame.transform.scale(self.image, (int(w), int(h)))
        self.image_hover = pygame.transform.scale(self.image_hover, (int(w), int(h)))
        
    def draw(self, win, da_point):
        if da_point[0] > self.x and da_point[0] < self.x + self.w:
            if da_point[1] > self.y and da_point[1] < self.y + self.h:
                win.blit(self.image_hover, (self.x, self.y))
                return
        win.blit(self.image, (self.x, self.y))
        return
    
    def check_pressing(self, da_point):
        if da_point[0] > self.x and da_point[0] < self.x + self.w:
            if da_point[1] > self.y and da_point[1] < self.y + self.h:
                return [True, self.tag]
        return [False, self.tag]



class D_Text():
    def __init__(self, x, y, text, size, colour, width_limit, leftormiddle):#limit will be either 800 or smtg else, gotta specify bc of the narrator thing
        self.x, self.y, self.size, self.colour, self.lor = x, y, size, colour, leftormiddle
        self.text = text
        self.text_list = []
        self.font = pygame.font.Font(gf + "\\assets\\font\\PKMN_RBYGSC.ttf", self.size)#Retro Gaming.ttf
        #self.font = pygame.font.SysFont(gf + "\\assets\\font\\Retro Gaming.ttf", self.size)
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
        decalage = -self.size
        for sentence_part in self.text_list:
            decalage = decalage + (self.size * 12/10)
            self.text_surface = self.font.render(sentence_part, False, self.colour)
            if self.lor == "left":
                win.blit(self.text_surface, (int(self.x), int(self.y) + decalage))
            elif self.lor == "middle":
                self.text_width = self.text_surface.get_width()
                win.blit(self.text_surface, (int(self.x - self.text_width/2), int(self.y) + decalage))
        return


class Player():
    def __init__(self, x, y, w, h, health, attackdmg, defense, speed, img, name):
        self.x, self.y, self.w, self.h, self.health, self.attackdmg, self.defense, self.speed, self.img, self.name = x, y, w, h, health, attackdmg, defense, speed, img, name
        self.max_health = self.health
        self.wc = 0#walk count
        self.wr, self.wl = False, False
        self.lr, self.ll = True, False
        self.wu, self.wd = False, False
        self.attacking = False
        self.ac = 0#attack count
        self.acc = 6#attack count cooldown

    def check_hover(self, da_point):
        if da_point[0] > self.x and da_point[0] < self.x + self.w:
            if da_point[1] > self.y and da_point[1] < self.y + self.h:
                pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x - 1, self.y - 1, self.w + 2, self.h + 2), 2)

    def check_click(self, da_point):
        if da_point[0] > self.x and da_point[0] < self.x + self.w:
            if da_point[1] > self.y and da_point[1] < self.y + self.h:
                return True
        return False
    
    def move(self, monitor_size):
        """
        #goodbye old code, you will be missed
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
        """
        if self.wr:
            self.x += self.speed
        elif self.wl:
            self.x -= self.speed
        else:
            self.wr, self.wl = False, False
        if self.wu:
            self.y -= self.speed
        elif self.wd:
            self.y += self.speed
        else:
            self.wu, self.wd = False, False
    
    def attack(self, enemy):
        self.attacking = True
        if enemy.defense > self.attackdmg:
            if 2 == randint(1, 5):
                enemy.health -= self.attackdmg - enemy.defense//2
        else:
            enemy.health -= self.attackdmg - enemy.defense//2
        if enemy.health <= 0:
            enemy.health = 0
            pygame.mixer.find_channel().play(choice(death_list))
        
        return enemy

    def rest(self):
        self.health += self.max_health//10
        if self.health > self.max_health:
            self.health = self.max_health
        
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



def get_images(name, nickname = ""):
    if nickname == "":
        nickname = name
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
    img_list.append(D_Text(monitor_size[0] * 0.12 , monitor_size[1] * 0.93, nickname, 30, (0, 0, 0), monitor_size[0] * 0.69, "middle"))#its actually too much but idc tbh it wont be seen in the game i hope

    del loci, loc, idle, idlem, walk, walkm, attack, attackm, head
    return img_list



albert_img = get_images("Albert")
paladin_img = get_images("Paladin")

albert = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, 100, 25, 30, monitor_size[0]/250, albert_img, "Albert")#speed was 5
paladin = Player(monitor_size[0] * 4/5, monitor_size[1]//4, 128, 128, 100, 25, 30, monitor_size[0]/250, paladin_img, "Paladin")#the y was 300
paladin.ll = True
paladin.lr = False
bandit_img = get_images("Bandit")
bandit1 = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, 50, 30, 5, monitor_size[0]/200, get_images("Bandit"), "Bandit1")
bandit2 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 - monitor_size[1] * 0.07, 128, 128, 50, 30, 5, monitor_size[0]/200, get_images("Bandit"), "Bandit2")
bandit3 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 + monitor_size[1] * 0.07, 128, 128, 50, 30, 5, monitor_size[0]/200, get_images("Bandit"), "Bandit3")
characters = [albert, paladin, bandit1, bandit2, bandit3]

#Combat positions
#team1:(team at the right)
#(monitor_size[0]/2 + monitor_size[0] * 0.2, monitor_size[1]//4)
#(monitor_size[0]/2 + monitor_size[0] * 0.4, monitor_size[1]//4 - monitor_size[1] * 0.07)
#(monitor_size[0]/2 + monitor_size[0] * 0.4, monitor_size[1]//4 + monitor_size[1] * 0.07)
#team2:(team at the left)
#(monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4)
#(monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 - monitor_size[1] * 0.07)
#(monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 + monitor_size[1] * 0.07)
buttons = []
the_step = 0
da_list = ["attack", "defend", "rest", "run"]
for button in da_list:
    buttons.append(Button(monitor_size[0] * 0.39, monitor_size[1] * 0.76 + the_step, monitor_size[0] * 0.22, (monitor_size[1] * 0.20) / len(da_list), button))
    the_step += (monitor_size[0] * 0.20) / (len(da_list) + 1)
del da_list, the_step



def dialogue(text_list, characters, in_combat):
    if text_list != []:
        if text_list[0][0] != "wait func" and text_list[0][0] != "move func" and text_list[0][0] != "fade away":
            if text_list[0][1] != "narrator":
                win.blit(dialogue_bubble, (0, (monitor_size[1]//4) * 3))
                text_list[0][0].draw(win)
                for character in characters:
                    if character.name == text_list[0][1]:
                        win.blit(character.img[6], ((monitor_size[0]//85) * 6, (monitor_size[1]//4) * 3))
                        character.img[7].draw(win)
                        break
            else:
                win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
                text_list[0][0].draw(win)
        else:
            win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
    else:
        if not in_combat and not(bg_stage in [0, 1, 2, 6, 7]):
            win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
        elif in_combat:
            win.blit(combat_bubble, (0, (monitor_size[1]//4) * 3))
            if turn < len(team1) + len(team2) and turn >= len(team1):
                pygame.draw.rect(win, (200, 50, 50), pygame.Rect(team2[turn - len(team1)].x, team2[turn - len(team1)].y + team2[turn - len(team1)].h, team2[turn - len(team1)].w, 10))
            if turn < len(team1):
                pygame.draw.rect(win, (50, 200, 50), pygame.Rect(team1[turn].x, team1[turn].y + team1[turn].h, team1[turn].w, 10))
            for teammate in team1:
                teammate.img[-1].draw(win)
                #monitor_size[0] * 0.34 bar length
                hp_per = (monitor_size[0] * 0.30) * (teammate.health / teammate.max_health)
                #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
                pygame.draw.rect(win, (150, 0, 0), pygame.Rect(monitor_size[0] * 0.65, teammate.img[-1].y + (teammate.img[-1].size * 1.3), monitor_size[0] * 0.30, teammate.img[-1].size))
                pygame.draw.rect(win, (0, 200, 100), pygame.Rect(monitor_size[0] * 0.65, teammate.img[-1].y + (teammate.img[-1].size * 1.3), hp_per, teammate.img[-1].size))
                
            for teammate in team2:
                teammate.img[-1].draw(win)
                #monitor_size[0] * 0.34 bar length
                hp_per = (monitor_size[0] * 0.30) * (teammate.health / teammate.max_health)
                #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
                pygame.draw.rect(win, (150, 0, 0), pygame.Rect(monitor_size[0] * 0.04, teammate.img[-1].y + (teammate.img[-1].size * 1.3), monitor_size[0] * 0.30, teammate.img[-1].size))
                pygame.draw.rect(win, (0, 200, 100), pygame.Rect(monitor_size[0] * 0.04, teammate.img[-1].y + (teammate.img[-1].size * 1.3), hp_per, teammate.img[-1].size))
                
            for button in buttons:
                button.draw(win, pygame.mouse.get_pos())






dtl0 = [["wait func", 5], ["fade away"]]
dtl1 = [["wait func", 5], ["Our story begins with the end of another one, The paladin, the bravest soldier of the king's army is guarding the gates at the entrance of the town, but something seems off.", "narrator"], ["move func", [["Albert", ["wr", "lr"]]], 270], ["wait func", 15], ["You still here?", "Albert"], ["wait func", 60], ["You should get going my friend, we have nothing to do... The town has been destroyed. You can see it by yourself.", "Albert"], ["wait func", 60], ["Look back! At the gates! Don't you see the destruction?!", "Albert"], ["I made a promise to the king, I promised that I'll guard this gates until the day I perish.", "Paladin"], ["Bu-but there are no people to protect anymore! The king's de-", "Albert"], ["move func", [["Albert", ["ll"]]], 10], ["move func", [["Bandit1", ["wr", "lr"]], ["Bandit2", ["wr", "lr"]], ["Bandit3", ["wr", "lr"]]], 540], ["wait func", 30], ["You guys got nothing to do!!", "Bandit1"], ["En garde!", "Paladin"], ["fade away"]]
dtl2 = [["wait func", 30], ["move func", [["Albert", ["lr"]]], 10], ["Phew! That was close! Well, as I was saying-", "Albert"], ["I\'m tired of killing bandits here, I want to know from where and why they are coming.", "Paladin"], ["Hmmm... These bandits must be bountyhunters that the Slime King has hired.", "Albert"], ["What are we waiting for then? Let\'s go find that guy!!!", "Paladin"], ["move func", [["Paladin", ["wl", "ll"]], ["Albert", ["wl", "ll"]]], 600], ["...and so, our brave heroes went inside the forest to end the Slime King\'s life!", "narrator"], ["fade away"]]
dtl3 = [["wait func", 5], ["Albert, no...", "Paladin"], ["I WILL MAKE THESE PEOPLE PAY FOR WHAT THEY DID!", "Paladin"], ["move func", [["Paladin", ["wl"]]], 600], ["Raged by his best friend\'s death, Paladin ran towards the forest, hoping to find where these bandits came from while not knowing the adventures he\'s getting into...", "narrator"], ["fade away"]]
dtl4 = [["wait func", 5], ["move func", [["Albert", ["lr"]]], 10], ["Paladin...", "Albert"], ["At least we could clash by shoulder again before you died...", "Albert"], ["wait func", 30], ["THOUGH IT DOESN\'T MEAN THAT I\'M NOT GOING TO AVENGE YOU! I\'M COMING FOR YOU SLIME KING!", "Albert"], ["move func", [["Albert", ["wl", "ll"]]], 600], ["Raged by his best friend\'s death, Albert ran towards the forest, hoping to find the Slime King while not knowing the adventures he\'s getting into...", "narrator"], ["fade away"]]
dtl = []


def get_texts(liste):
    for i in range(len(liste)):
        if liste[i][0] != "wait func" and liste[i][0] != "move func" and liste[i][0] != "fade away":
            if liste[i][1] != "narrator":
                liste[i][0] = D_Text(monitor_size[0] * 0.26, monitor_size[1] * 0.78, liste[i][0], 30, (0, 0, 0), monitor_size[0] * 0.69, "left")#0.69 is the ratio for the dialogue bubble with the head(funny reddit number) 
            else:
                liste[i][0] = D_Text(monitor_size[0] * 0.05, monitor_size[1] * 0.78, liste[i][0], 30, (0, 0, 0), monitor_size[0] * 0.87, "left")
    return liste
            
dtl1 = get_texts(dtl1)
dtl2 = get_texts(dtl2)
dtl3 = get_texts(dtl3)
dtl4 = get_texts(dtl4)


            


in_combat = False

font = pygame.font.SysFont("Arial" , 18 , bold = True)
def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    win.blit(fps_t,(0,0))

def draw_screen():
    win.blit(backgrounds[bg_stage], ((0, 0)))
    if not(bg_stage in [0, 1, 2]):
        dialogue(dtl, characters, in_combat)
        if not in_combat:
            for character in characters:
                character.move(monitor_size)
                character.draw(win)
        else:
            if len(team1) > 0:
                for character in team1:
                    character.move(monitor_size)
                    character.draw(win)
            if len(team2) > 0:
                for character in team2:
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
        if not(bgs in [0, 1, 2, 6, 7]):
            dialogue(dtl, characters, in_combat)
            draw_screen()
        win.blit(fade, (0,0))
        fps_counter()
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
        win.blit(backgrounds[bgsw], ((0, 0)))
        if not(bgs in [0, 1, 2, 6, 7]):
            dialogue(dtl, characters, in_combat)
            draw_screen()
        win.blit(fade, (0,0))
        fps_counter()
        pygame.display.update()
        pygame.time.delay(5)
        alpha -= 1
    return False, bgsw

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







def enemy_combat_choice(team1, team2, turn, waiter):#player_team, enemy_team
    #print(f"{turn} < {len(team1) + len(team2) - 1} and {turn} >= {len(team1)}")
    #print(waiter)
    if turn < len(team1) + len(team2) and turn >= len(team1):
        #pygame.draw.rect(win, (200, 50, 50), pygame.Rect(team2[turn - len(team1)].x, team2[turn - len(team1)].y + team2[turn - len(team1)].h, team2[turn - len(team1)].w, 50))
        waiter = wait(waiter)
        if waiter <= 0:
            if team2[turn - len(team1)].health < (team2[turn - len(team1)].health * 25) / 100:
                team2[turn - len(team1)].rest()
                waiter = 30
                turn += 1
            else:
                chosen_enemy = choice(team1)
                while chosen_enemy.health <= 0:
                    chosen_enemy = choice(team1)
                team1[team1.index(chosen_enemy)] = team2[turn - len(team1)].attack(chosen_enemy)
                pygame.mixer.find_channel().play(choice(sword_list))
                waiter = 30
                turn += 1
    return team1, team2, turn, waiter

def get_turn(team1, team2, turn):#team1 is always the player's team
    for i in range(len(team1)):
        if team1[i].health == 0:
            team1.pop(i)
            break
    for i in range(len(team2)):
        if team2[i].health == 0:
            team2.pop(i)
            break
    if turn > len(team1) + len(team2) - 1:
        turn = 0
    while True:#choosing the player(turn) with health more than 0
        if turn < len(team1):
            if team1[turn].health > 0:
                #pygame.draw.line(win, (50, 200, 50), (team1[turn].x, team1[turn].y + team1[turn].h), (team1[turn].x + team1[turn].w, team1[turn].y + team1[turn].h))
                pygame.draw.rect(win, (50, 200, 50), pygame.Rect(team1[turn].x, team1[turn].y + team1[turn].h, team1[turn].w, 10))
                #pygame.draw.rect(win, (200, 50, 50), pygame.Rect(team1[turn].x - 1, team1[turn].y - 1, team1[turn].w + 2, team1[turn].h + 2))
                break
            else:
                turn += 1
                continue
        else:
            if team2[turn - len(team1)].health > 0:
                #pygame.draw.line(win, (200, 50, 50), (team2[turn - len(team1)].x, team2[turn - len(team1)].y + team2[turn - len(team1)].h), (team2[turn - len(team1)].x + team2[turn - len(team1)].w, team2[turn - len(team1)].y + team2[turn - len(team1)].h))
                pygame.draw.rect(win, (200, 50, 50), pygame.Rect(team2[turn - len(team1)].x, team2[turn - len(team1)].y + team2[turn - len(team1)].h, team2[turn - len(team1)].w, 10))
                break
            else:
                turn += 1
                continue
    
    return team1, team2, turn
    
    

def change_places_of_the_ch(characters):
    for step in range(len(characters)):
        key = characters[step]
        brah = step - 1
        while brah >= 0 and key.y < characters[brah].y:
            characters[brah + 1] = characters[brah]
            brah -= 1
        characters[brah + 1] = key
    return characters
            
    
def get_class(name, characters):
    for i in range(len(characters)):
        if name == characters[i].name:
            return characters[i]

#Combat positions
#team1:(team at the right)
#(monitor_size[0]/2 + monitor_size[0] * 0.2, monitor_size[1]//4)
#(monitor_size[0]/2 + monitor_size[0] * 0.4, monitor_size[1]//4 - monitor_size[1] * 0.07)
#(monitor_size[0]/2 + monitor_size[0] * 0.4, monitor_size[1]//4 + monitor_size[1] * 0.07)
#team2:(team at the left)
#(monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4)
#(monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 - monitor_size[1] * 0.07)
#(monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 + monitor_size[1] * 0.07)

def get_team_locations_ready(team1, team2):
    if len(team1) > 0:
        team1[0].x, team1[0].y = monitor_size[0]/2, monitor_size[1]//4
    if len(team1) > 1:
        team1[1].x, team1[1].y = monitor_size[0]/2 + monitor_size[0] * 0.2, monitor_size[1]//4 - monitor_size[1] * 0.07
    if len(team1) > 2:
        team1[2].x, team1[2].y = monitor_size[0]/2 + monitor_size[0] * 0.2, monitor_size[1]//4 + monitor_size[1] * 0.07
        
    if len(team2) > 0:
        team2[0].x, team2[0].y = monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4
    if len(team2) > 1:
        team2[1].x, team2[1].y = monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 - monitor_size[1] * 0.07
    if len(team2) > 2:
        team2[2].x, team2[2].y = monitor_size[0]/2 - monitor_size[0] * 0.4, monitor_size[1]//4 + monitor_size[1] * 0.07

    for i in range(len(team1)):
        team1[i].ll = True
        team1[i].lr = False
    for i in range(len(team2)):
        team2[i].lr = True
        team2[i].ll = False
    return team1, team2



                            
will_fade = False
fcb = False


#combat things
team1 = []
team2 = []
turn = -1
waiter = 30
decision = ["", None]
p_wait = 0
game_over_text = D_Text(monitor_size[0]/2, monitor_size[1]/4, "GAME OVER", monitor_size[0]//12, (255, 0, 0), monitor_size[0], "middle")#x, y, text, size, colour, width_limit, leftormiddle)
died = False
combat_ending_wait = 1200
died_fr = False


sound_check = False

ending_wait = 60

running = True
while running:
    clock.tick(30)
    mp = pygame.mouse.get_pos()
    md = False

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_ESCAPE]:
        running = False
        break
    
    characters = change_places_of_the_ch(characters)
    draw_screen()
    nmp = (mp[0] - 2, mp[1] - 2)
    if died and not(bg_stage in [0, 1, 2, 6, 7]):
        game_over_text.draw(win)
        
    if bg_stage == 0:
        if not fcb:
            #startup_sound
            pygame.mixer.find_channel().play(startup_sound)
            will_fade = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    md = True
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    will_fade = True


        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
            fcb = True
            
    if bg_stage == 1:
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
        if not fcb:
            will_fade = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    md = True
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    will_fade = True

        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 2)
            fcb = True
            
    if bg_stage == 2:
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 2)
        if not fcb:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    md = True
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    will_fade = True
                    
        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 3)
            fcb = True
            bird_sound.play(-1)
    
    elif bg_stage == 3:
        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 4)
            #D_Text(monitor_size[0] * 0.12 , monitor_size[1] * 0.94, nickname, 50, (0, 0, 0), monitor_size[0] * 0.69, "middle")
            #^this is the dialogue name part, gotta change its x and y(and its size if necessary) for the combat part
            #x = monitor_size[0] * 0.61, y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08, size = 30
            #team1 first guy text modification
            get_class("Albert", characters).img[-1].x = monitor_size[0] * 0.80
            get_class("Albert", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08
            get_class("Albert", characters).img[-1].size = 25
            #team1 second guy text modification(i can make a loop but i dont want to)
            get_class("Paladin", characters).img[-1].x = monitor_size[0] * 0.80
            get_class("Paladin", characters).img[-1].y = monitor_size[1] * 0.76
            get_class("Paladin", characters).img[-1].size = 25
            #team1 third guy text modification
            #get_class("Paladin", characters).img[-1].x = monitor_size[0] * 0.80
            #get_class("Paladin", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.16
            #get_class("Paladin", characters).img[-1].size = 30

            #team2 first guy text modification
            get_class("Bandit1", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("Bandit1", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08
            get_class("Bandit1", characters).img[-1].size = 25
            #team2 second guy text modification(i can make a loop but i dont want to)
            get_class("Bandit2", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("Bandit2", characters).img[-1].y = monitor_size[1] * 0.76
            get_class("Bandit2", characters).img[-1].size = 25
            #team2 third guy text modification
            get_class("Bandit3", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("Bandit3", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.16
            get_class("Bandit3", characters).img[-1].size = 25

            
            team1.append(get_class("Albert", characters))
            team1.append(get_class("Paladin", characters))
            team2.append(get_class("Bandit1", characters))
            team2.append(get_class("Bandit2", characters))
            team2.append(get_class("Bandit3", characters))
            team1, team2 = get_team_locations_ready(team1, team2)
            in_combat = True
            characters = []
            turn = 2
            bird_sound.stop()
            combat_sound.play(-1)
        elif fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 3)
            if not fcb:
                dtl = dtl1
        if not fcb and not will_fade:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    md = True
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if dtl != []:
                        if event.key == pygame.K_SPACE and dtl[0][0] != "wait func" and dtl[0][0] != "move func":
                            dtl.pop(0)
                            sound_check = False

            if len(dtl) > 0 and not(sound_check):
                if dtl[0][0] != "wait func" and dtl[0][0] != "move func":
                    speak_blip.play()
                    sound_check = True
            

            dialogue(dtl, characters, in_combat)
            if dtl != []:
                if dtl[0][0] == "wait func":
                    if dtl[0][1] > 0:
                        dtl[0][1] = wait(dtl[0][1])
                    else:
                        dtl.pop(0)
                        sound_check = False
                if dtl[0][0] == "move func":
                    if dtl[0][2] > 0:
                        for index in range(len(dtl[0][1])):
                            for character_index in range(len(characters)):
                                if dtl[0][1][index][0] == characters[character_index].name:
                                    dtl[0][2], [characters[character_index], dtl[0][1][index][1]] = script_ds(dtl[0][2], [characters[character_index], dtl[0][1][index][1]])
                    else:
                        for index in range(len(dtl[0][1])):
                            for character_index in range(len(characters)):
                                if dtl[0][1][index][0] == characters[character_index].name:
                                    characters[character_index].wr, characters[character_index].wl, characters[character_index].wu, characters[character_index].wd = False, False, False, False
                        dtl.pop(0)
                        sound_check = False
                if dtl[0][0] == "fade away":
                    will_fade = True
                    fcb = True
                    dtl.pop(0)


            if dtl == []:
                for da_index in range(len(characters)):
                    if characters[da_index].name == "Paladin":
                        characters[da_index] = move_c(characters[da_index], keys)
                        break
                
    elif bg_stage == 4:#combat_stage
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 4)
        elif will_fade:
            if died_fr:
                will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 6)
                game_over_sound_effect.stop()
            else:
                will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 5)
                bird_sound.play(-1)
            fcb = True
            combat_sound.stop()
            
            
        else:
            if in_combat and len(team1) > 0 and len(team2) > 0:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        md = True
                    if event.type == pygame.QUIT:
                        running = False
                
                dialogue(dtl, characters, in_combat)
                team1, team2, turn = get_turn(team1, team2, turn)
                team1, team2, turn, waiter = enemy_combat_choice(team1, team2, turn, waiter)
                p_wait = wait(p_wait)
                if turn < len(team1) and p_wait <= 0:
                    m_pos = pygame.mouse.get_pos()
                    for enemy in team2:#didnt work bc the game puts everything on it so it cant be seen
                        enemy.check_hover(m_pos)
                    #detect choice with the mouse pos(attack, defend, rest, run)
                    if md:
                        if decision[0] == "attack":
                            #check if hovering an enemy
                            for i in range(len(team2)):
                                if team2[i].check_click(m_pos):
                                    team2[i] = team1[turn].attack(team2[i])
                                    pygame.mixer.find_channel().play(choice(sword_list))
                                    turn += 1
                                    p_wait = 2
                                        
                        if decision[0] == "rest":
                            team1[turn].rest()
                            p_wait = 2
                            turn += 1
                        else:
                            for index in range(len(buttons)):
                                check = buttons[index].check_pressing(m_pos)
                                if check[0]:
                                    decision[0] = check[1]
                                    break
                        
                else:
                    decision = ["", None]
            else:
                
                if len(team1) == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            md = True
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN:
                            combat_ending_wait = 0
                            
                    game_over_text.draw(win)
                    if not died:
                        combat_sound.stop()
                        game_over_sound_effect.play(-1)
                        died = True
                        died_fr = True
                    combat_ending_wait = wait(combat_ending_wait)
                    if combat_ending_wait <= 0:
                        in_combat = False
                        will_fade = True
                if len(team2) == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            md = True
                        if event.type == pygame.QUIT:
                            running = False
                    combat_ending_wait = wait(combat_ending_wait)
                    if combat_ending_wait <= 0:
                        in_combat = False
                        characters = team1
                        for chindex in range(len(characters)):
                            characters[chindex].img[-1].x = monitor_size[0] * 0.12
                            characters[chindex].img[-1].y = monitor_size[1] * 0.93
                            characters[chindex].img[-1].size = 50
                            if characters[0].name == "Paladin":
                                dtl = dtl3
                            elif characters[0].name == "Albert":
                                dtl = dtl4
                        else:
                            dtl = dtl2
                        will_fade = True
    elif bg_stage == 5:#after combat
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 5)

        elif will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 5)
            #fcb = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if dtl != []:
                        if event.key == pygame.K_SPACE and dtl[0][0] != "wait func" and dtl[0][0] != "move func":
                            dtl.pop(0)
                            sound_check = False

            if len(dtl) > 0 and not(sound_check):
                if dtl[0][0] != "wait func" and dtl[0][0] != "move func":
                    speak_blip.play()
                    sound_check = True
                    
            dialogue(dtl, characters, in_combat)
            if dtl != []:
                if dtl[0][0] == "wait func":
                    if dtl[0][1] > 0:
                        dtl[0][1] = wait(dtl[0][1])
                    else:
                        dtl.pop(0)
                        sound_check = False
                if dtl[0][0] == "move func":
                    if dtl[0][2] > 0:
                        for index in range(len(dtl[0][1])):
                            for character_index in range(len(characters)):
                                if dtl[0][1][index][0] == characters[character_index].name:
                                    dtl[0][2], [characters[character_index], dtl[0][1][index][1]] = script_ds(dtl[0][2], [characters[character_index], dtl[0][1][index][1]])
                    else:
                        for index in range(len(dtl[0][1])):
                            for character_index in range(len(characters)):
                                if dtl[0][1][index][0] == characters[character_index].name:
                                    characters[character_index].wr, characters[character_index].wl, characters[character_index].wu, characters[character_index].wd = False, False, False, False
                        dtl.pop(0)
                        sound_check = False
                if dtl[0][0] == "fade away":
                    will_fade = True
                    fcb = True
                    dtl.pop(0)


            if dtl == []:
                for da_index in range(len(characters)):
                    if characters[da_index].name == "Paladin":
                        characters[da_index] = move_c(characters[da_index], keys)
                        break
                    
    elif bg_stage == 6:#end credits
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 6)
            will_fade = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        ending_wait = wait(ending_wait)
        if will_fade and ending_wait <= 0:
            if died_fr:
                will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 7)
                game_over_sound_effect.play(-1)
            else:
                will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 6)
                running = False
                break

    elif bg_stage == 7:#jk you just died lmao
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
    if not(bg_stage in [0, 1, 2, 6, 7]):
        if md:
            win.blit(cursor_click, nmp)
        else:
            win.blit(cursor, nmp)
    fps_counter()
    pygame.display.update()



