"""
imma put da comments here
started in 28/08/2022 08:42
got a mixed situation here, i think imma work a little more than 1 hour
now lets go make that combat ui
https://www.youtube.com/watch?v=0yBnIUX0QAE&ab_channel=ToploaderVEVO
today's vibe
i stopped at around 9 am, now i restart at 19:26
gonna change the cursor
im done at 19:45 with a fps showing thing and the cursor
i have no idea for how long i worked, its 23:15 rn
i did the combat ui, now time to make it work
nvm, i think imma get some sleep


to do list:
-write a fucking proper code
-the image of the paladin seems off when looking right and left rapidly, maybe change its coordinates when he changes his way he's looking?(a friend said its not a big deal)
-write a function that does scripts - partly done, gonna add fading away effect
-add combat
-finish the demo

"""
import pygame
import os
from random import choice

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

#the directory
gf = os.getcwd()#C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\paladin


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
backgrounds = [game_title, background, background]
bg_stage = 0
for i in range(len(backgrounds)):
    backgrounds[i] = pygame.transform.scale(backgrounds[i], (monitor_size[0], (monitor_size[1]//4) * 3))
backgrounds[0] = pygame.transform.scale(backgrounds[0], (monitor_size[0], monitor_size[1]))


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
        return False



class D_Text():
    def __init__(self, x, y, text, size, colour, width_limit, leftormiddle):#limit will be either 800 or smtg else, gotta specify bc of the narrator thing
        self.x, self.y, self.size, self.colour, self.lor = x, y, size, colour, leftormiddle
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
    img_list.append(D_Text(monitor_size[0] * 0.12 , monitor_size[1] * 0.94, nickname, 50, (0, 0, 0), monitor_size[0] * 0.69, "middle"))#its actually too much but idc tbh it wont be seen in the game i hope

    del loci, loc, idle, idlem, walk, walkm, attack, attackm, head
    return img_list



albert_img = get_images("Albert")
paladin_img = get_images("Paladin")

albert = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, 100, 25, 30, monitor_size[0]/250, albert_img, "Albert")#speed was 5
paladin = Player(monitor_size[0] * 4/5, monitor_size[1]//4, 128, 128, 100, 25, 30, monitor_size[0]/250, paladin_img, "Paladin")#the y was 300
paladin.ll = True
paladin.lr = False
bandit_img = get_images("Bandit")
bandit1 = Player(-monitor_size[0]/2, monitor_size[1]//4, 128, 128, 50, 40, 5, monitor_size[0]/200, get_images("Bandit", "I fried my balls"), "I fried my balls")
bandit2 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 - monitor_size[1] * 0.07, 128, 128, 50, 40, 5, monitor_size[0]/200, get_images("Bandit", "Bandit on the back"), "Bandit on the back")
bandit3 = Player(-monitor_size[0]/2 - monitor_size[0] * 0.2, monitor_size[1]//4 + monitor_size[1] * 0.07, 128, 128, 50, 40, 5, monitor_size[0]/200, get_images("Bandit", "I hate myself"), "I hate myself")
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
        if not in_combat:
            win.blit(idle_bubble, (0, (monitor_size[1]//4) * 3))
        else:
            win.blit(combat_bubble, (0, (monitor_size[1]//4) * 3))
            for teammate in team1:
                teammate.img[-1].draw(win)
                #monitor_size[0] * 0.34 bar length
                hp_per = (monitor_size[0] * 0.30) * (teammate.health / teammate.max_health)
                #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
                pygame.draw.rect(win, (150, 0, 0), pygame.Rect(monitor_size[0] * 0.65, teammate.img[-1].y + teammate.img[-1].size, monitor_size[0] * 0.30, teammate.img[-1].size))
                pygame.draw.rect(win, (0, 200, 100), pygame.Rect(monitor_size[0] * 0.65, teammate.img[-1].y + teammate.img[-1].size, hp_per, teammate.img[-1].size))
                
            for teammate in team2:
                teammate.img[-1].draw(win)
                #monitor_size[0] * 0.34 bar length
                hp_per = (monitor_size[0] * 0.30) * (teammate.health / teammate.max_health)
                #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
                pygame.draw.rect(win, (150, 0, 0), pygame.Rect(monitor_size[0] * 0.04, teammate.img[-1].y + teammate.img[-1].size, monitor_size[0] * 0.30, teammate.img[-1].size))
                pygame.draw.rect(win, (0, 200, 100), pygame.Rect(monitor_size[0] * 0.04, teammate.img[-1].y + teammate.img[-1].size, hp_per, teammate.img[-1].size))
                
            for button in buttons:
                button.draw(win, pygame.mouse.get_pos())







dtl1 = [["wait func", 45], ["Our story begins with the end of another one, The paladin, the bravest soldier of the king's army is guarding the gates at the entrance of the town, but something seems off.", "narrator"], ["move func", [["Albert", ["wr", "lr"]]], 270], ["wait func", 15], ["You still here?", "Albert"], ["wait func", 60], ["You should get going my friend, we have nothing to do... The town has been destroyed. You can see it by yourself.", "Albert"], ["wait func", 60], ["Look back! At the gates! Don't you see the destruction?!", "Albert"], ["I made a promise to the king, I promised that I'll guard this gates until the day I perish.", "Paladin"], ["Bu-but there are no people to protect anymore! The king's de-", "Albert"], ["move func", [["Albert", ["ll"]]], 10], ["move func", [["I fried my balls", ["wr", "lr"]], ["I hate myself", ["wr", "lr"]], ["Bandit on the back", ["wr", "lr"]]], 540], ["wait func", 30], ["You guys got nothing to do!!", "I fried my balls"], ["En garde!", "Paladin"], ["fade away"]]
dtl = []
for i in range(len(dtl1)):
    if dtl1[i][0] != "wait func" and dtl1[i][0] != "move func" and dtl1[i][0] != "fade away":
        if dtl1[i][1] != "narrator":
            dtl1[i][0] = D_Text(monitor_size[0] * 0.26, monitor_size[1] * 0.78, dtl1[i][0], 50, (0, 0, 0), monitor_size[0] * 0.69, "left")#0.69 is the ratio for the dialogue bubble with the head(funny reddit number) 
        else:
            dtl1[i][0] = D_Text(monitor_size[0] * 0.05, monitor_size[1] * 0.78, dtl1[i][0], 50, (0, 0, 0), monitor_size[0] * 0.87, "left")
            


in_combat = False

def draw_screen():
    win.blit(backgrounds[bg_stage], ((0, 0)))
    if bg_stage != 0:
        if not in_combat:
            dialogue(dtl, characters, in_combat)
            for character in characters:
                character.move(monitor_size)
                character.draw(win)
        else:
            dialogue(dtl, characters, in_combat)
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
        if bgs != 0:
            dialogue(dtl, characters, in_combat)
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
        dialogue(dtl, characters, in_combat)
        win.blit(fade, (0,0))
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


def combat_choice(team1, team2, turn, mouse_pos, stage, wait_count):#player, player_team, enemy_team
    if wait_count == 30:
        if turn == 0:#it will be always the paladin(player)
            if stage == 0:#stage 0: options for attack/defend/rest, stage 1: options to attack
                #draw UI
                return
            
        elif turn < len(team1):
            if team1[turn].health < (team1[turn].health * 25) / 100:
                wait_count = wait(wait_count)
                if wait_count <= 0:
                    team1[turn].rest()
                    wait_count = 30
                    turn += 1
            else:
                wait_count = wait(wait_count)
                if wait_count <= 0:
                    chosen_enemy = choice(team2)
                    while chosen_enemy.health <= 0:
                        chosen_enemy = choice(team2)
                    team2[team2.index(chosen_enemy)] = team1[turn].attack(chosen_enemy)
                    wait_count = 30
                    turn += 1
        elif turn < len(team2):
            if team2[turn].health < (team2[turn].health * 25) / 100:
                wait_count = wait(wait_count)
                if wait_count <= 0:
                    team2[turn].rest()
                    wait_count = 30
                    turn += 1
            else:
                wait_count = wait(wait_count)
                if wait_count <= 0:
                    chosen_enemy = choice(team1)
                    while chosen_enemy.health <= 0:
                        chosen_enemy = choice(team1)
                    team1[team1.index(chosen_enemy)] = team2[turn].attack(chosen_enemy)
                    wait_count = 30
                    turn += 1

def combat(team1, team2, turn):#team1 is always the player's team
    turns = []
    turns.append(team1)
    turns.append(team2)
    if turn > len(team1) + len(team2):
        turn = 0
    while True:#choosing the player(turn) with health more than 0
        if turn < len(team1):
            if team1[turn].health > 0:
                break
            else:
                turn += 1
                continue
        else:
            if team2[turn - len(team1)].health > 0:
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
    for i in range(len(team2)):
        team2[i].lr = True
    return team1, team2


font = pygame.font.SysFont("Arial" , 18 , bold = True)
def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    win.blit(fps_t,(0,0))
                            
will_fade = False
fcb = False

team1 = []
team2 = []
turn = -1

running = True
while running:
    clock.tick(30)
    mp = pygame.mouse.get_pos()
    md = False
    if bg_stage == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                md = True
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                will_fade = True
                fcb = True
        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
    
    elif bg_stage == 1:
        if will_fade:
            will_fade, bg_stage = fade_gb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 2)
            #D_Text(monitor_size[0] * 0.12 , monitor_size[1] * 0.94, nickname, 50, (0, 0, 0), monitor_size[0] * 0.69, "middle")
            #^this is the dialogue name part, gotta change its x and y(and its size if necessary) for the combat part
            #x = monitor_size[0] * 0.61, y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08, size = 30
            #team1 first guy text modification
            get_class("Albert", characters).img[-1].x = monitor_size[0] * 0.80
            get_class("Albert", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08
            get_class("Albert", characters).img[-1].size = 30
            #team1 second guy text modification(i can make a loop but i dont want to)
            get_class("Paladin", characters).img[-1].x = monitor_size[0] * 0.80
            get_class("Paladin", characters).img[-1].y = monitor_size[1] * 0.76
            get_class("Paladin", characters).img[-1].size = 30
            #team1 third guy text modification
            #get_class("Paladin", characters).img[-1].x = monitor_size[0] * 0.80
            #get_class("Paladin", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.16
            #get_class("Paladin", characters).img[-1].size = 30

            #team2 first guy text modification
            get_class("I fried my balls", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("I fried my balls", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.08
            get_class("I fried my balls", characters).img[-1].size = 30
            #team2 second guy text modification(i can make a loop but i dont want to)
            get_class("Bandit on the back", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("Bandit on the back", characters).img[-1].y = monitor_size[1] * 0.76
            get_class("Bandit on the back", characters).img[-1].size = 30
            #team2 third guy text modification
            get_class("I hate myself", characters).img[-1].x = monitor_size[0] * 0.20
            get_class("I hate myself", characters).img[-1].y = monitor_size[1] * 0.76 + monitor_size[1] * 0.16
            get_class("I hate myself", characters).img[-1].size = 30

            
            team1.append(get_class("Albert", characters))
            team1.append(get_class("Paladin", characters))
            team2.append(get_class("I fried my balls", characters))
            team2.append(get_class("Bandit on the back", characters))
            team2.append(get_class("I hate myself", characters))
            team1, team2 = get_team_locations_ready(team1, team2)
            in_combat = True
            characters = []
        elif fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 1)
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
            
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_ESCAPE]:
                running = False

            dialogue(dtl, characters, in_combat)
            if dtl != []:
                if dtl[0][0] == "wait func":
                    if dtl[0][1] > 0:
                        dtl[0][1] = wait(dtl[0][1])
                    else:
                        dtl.pop(0)
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
                if dtl[0][0] == "fade away":
                    will_fade = True
                    fcb = True
                    dtl.pop(0)


            if dtl == []:
                for da_index in range(len(characters)):
                    if characters[da_index].name == "Paladin":
                        characters[da_index] = move_c(characters[da_index], keys)
                        break
                
    elif bg_stage == 2:#combat_stage
        if fcb:
            fcb, bg_stage = fade_cb(monitor_size[0], monitor_size[1], win, backgrounds, bg_stage, 2)
        else:
            if in_combat:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        md = True
                    if event.type == pygame.QUIT:
                        running = False
                dialogue(dtl, characters, in_combat)
            
    
    characters = change_places_of_the_ch(characters)
    draw_screen()
    nmp = (mp[0] - 2, mp[1] - 2)
    if md:
        win.blit(cursor_click, nmp)
    else:
        win.blit(cursor, nmp)
    fps_counter()
    pygame.display.update()



