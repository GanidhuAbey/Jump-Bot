#TODO: currently the program is crashing at random points in the game; my current belief is that the bots are crashing right when they are about to jump
#TODO: the the game is still using some old 'player' variables that need to be changed to 'bot'

#simple game to train neural network with
#player is a block that must just over obstacles, longer they survive the higher their score

import pygame as py
import random
import bot

PLAYER_COLOUR = 0
PLAYER_SIZE = 10

HEIGHT = 640
WIDTH = 480

py.init()

class Player:
    jump = False
    jump_height = 0.7
    rect = py.Rect(WIDTH * 0.25, HEIGHT * jump_height, PLAYER_SIZE, PLAYER_SIZE)
    dead = False
    falling = False
    score = 0

    def jumping(self):
        if self.jump and self.jump_height > 0.5:
            self.jump_height = self.jump_height - 0.001
            self.rect = py.Rect(WIDTH * 0.25, HEIGHT * self.jump_height, PLAYER_SIZE, PLAYER_SIZE)

        elif self.jump_height <= 0.5:
            self.jump = False
            self.falling = True
    
    def fall(self, obstacle):
        if self.falling:
            self.jump_height = self.jump_height * 1.001
            self.rect = py.Rect(WIDTH * 0.25, HEIGHT * self.jump_height, PLAYER_SIZE, PLAYER_SIZE)

            if self.jump_height >= 0.7:
                self.falling = False
                self.jump_height = 0.7
                print(obstacle.rect)
                self.rect = py.Rect(WIDTH * 0.25, HEIGHT * self.jump_height, PLAYER_SIZE, PLAYER_SIZE)

            


class Obstacles:
    move_rate = 0.7
    speed = 0.0005
    rect = py.Rect(WIDTH * move_rate, HEIGHT * 0.7, PLAYER_SIZE, PLAYER_SIZE)
    new_spawn = False

    def update_rect(self):
        self.move_rate = self.move_rate - self.speed
        
        self.rect = py.Rect(WIDTH * self.move_rate, HEIGHT * 0.7, PLAYER_SIZE, PLAYER_SIZE)
        if self.new_spawn == True:
            self.move_rate = 0.7
            if self.speed <= 0.0005:
                self.speed = self.speed / 0.90
            self.new_spawn = False
    
    def respawn(self, score):
        if (WIDTH * self.move_rate) < 100:
            self.new_spawn = True
            return score + 1
        
        return score


def check_collision(p_height, o_height, bot):
    #needs to check if the two squares are overlapping eachother
    player_loc = WIDTH * 0.25
    obstacle_loc = WIDTH * obstacle.move_rate

    if (obstacle_loc - player_loc) < 10 and (obstacle_loc - player_loc) > 0 and (p_height - o_height) == 0:
        return True
        
#create a screen
window = py.display.set_mode((HEIGHT, WIDTH))
background = py.Surface(window.get_size())
background.fill((255, 255, 255))
background = background.convert() 

#blit = painting
window.blit(background, (0, 0))

running = True
obstacle = Obstacles()

gene = bot.generate_genes()

bot_list = []
for i in range(len(gene)): #wasteful to call the range and the length function when we already know what the lengths gonna be
    bot_list.append(Player())

time = float(py.time.get_ticks())

while running:
    window.fill((255, 255, 255))

    #do we really need 3 different for loops when they all iterate through the same thing?
    for i in range(len(gene)):
        if time % (float(gene[0][0]) / float(gene[0][1])) == 0:
            bot_list[i].jump = True
    
    for bot in range(len(bot_list)):
        bot_list[bot].jumping()
        bot_list[bot].fall(obstacle)
        py.draw.rect(window, (PLAYER_COLOUR, PLAYER_COLOUR, PLAYER_COLOUR), bot_list[bot].rect)
        dead = check_collision(HEIGHT * bot_list[bot].jump_height, HEIGHT * 0.7, bot_list[bot])
        bot_list[bot].dead = dead
        bot_list[bot].score = obstacle.respawn(bot_list[bot].score)

    py.draw.rect(window, (178,34,34), obstacle.rect)
    obstacle.update_rect()
    

    

    py.display.flip()

for i in range(len(bot_list)):
    print("PRINT DAMMIT")
    print(bot.score)

py.quit()

#window.fill((255, 255, 255))
#    for event in py.event.get():
#        if event.type == py.QUIT
#            running = False
#        elif event.type == py.KEYDOWN:
#            if event.key == py.K_UP:
#                player.jump = True
#                print(obstacle.rect)
#            elif event.key == py.K_ESCAPE:
#                running = False
#    if player.dead == True:
#        running = False
#
#    player.jumping()
#    player.fall(obstacle)
#    py.draw.rect(window, (PLAYER_COLOUR, PLAYER_COLOUR, PLAYER_COLOUR), player.rect)
#
#    py.draw.rect(window, (178,34,34), obstacle.rect)
#    obstacle.update_rect()
#    player.score = obstacle.respawn(player.score)
#
#    check_collision(HEIGHT * player.jump_height, HEIGHT * 0.7)
#
#    py.display.flip()