# Young
#KNIGHT'S HONOUR
#November - January, 2015

'''------------------------------PRE-GAME CODE----------------------------'''
''' This is the section of code that initializes pygame, opens libraries,
    sets variables, and makes the program actually play out. '''
#Libraries
import pygame
import random
import pyganim
import time
import math
import ast

'''
List of Enhancements and Bug Fixes

Short List of All Changes
Many sound effect changes, such as a quieter attack sound
No longer can the character infinitely spin in a circle
Greater use of various modules, such as utilizing time.Time() for more accurate timing
Consistent character spawning, no longer will the character be running in place
Addition of a totally new game mode, Survival mode including but not limited to:
Unlimited waves
Limited attacking
Score system
Encrypted high scores
Power ups

Speaking of Power ups:
Totally new system
3 New power ups
Health bonus
Speed bonus
Invincibility

Redesign of level one
Re balancing of the entire game allowing power ups and a nice balance between skill and luck
Addition of new music

'''
#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (  0,   0, 255)
white = (255, 255, 255)
blue = (19,0,101)

#Current Screen
currentScreen = "mainScreen"

#Initializes Pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048) 

#Screen Size
screen_width = 1265
screen_height = 750
#Defining variables fro fullscreen
size = (screen_width, screen_height)
screen = pygame.display.set_mode((size),pygame.FULLSCREEN)

#Game Title - Knights Honour 
pygame.display.set_caption("Knights Honour")
 
#Loop until the user clicks the close button.
done = False
 
#Used to manage how fast the screen updates
clock = pygame.time.Clock()

'''------------------------------CLASSES----------------------------'''
'''This section of code defines classes for instances to develop within.'''
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
    #Methods
    def __init__(self, x, y):
        """Constructor function"""
        #Call the parent's constructor
        super().__init__()
        #Set height, width and filling the colour for the player
        #self.image = pygame.Surface([90, 145])
        #self.image.fill(BLUE)
        self.image = pygame.image.load("Transparents/Transparent_Player.png")
        #Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.walls = None
        #Attributes
        #Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.direction = ""
    #Defining function changespeed of the player, for movement
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
    #Updating the players position
    def update(self,wall):
        """ Find a new position for the player"""
        #Updating player with the movement in the x
        self.rect.x += self.change_x
        #If the player collides with a wall
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        #Moving the player if they hit a block
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        #Updating the player with movement in the y
        self.rect.y += self.change_y
        #If the player collides with a wall
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        #Moving the player if they hit a wall
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
        #4 if loops to check for collision on each side of the screen
        if self.rect.x > screen_width - 90:
            self.rect.x = screen_width - 90
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > screen_height - 145:
            self.rect.y = screen_height - 145
        if self.rect.y < 0:
            self.rect.y = 0

    #Defining the attack method
    def attack(self):
        #attack sound
        menuSelect.play()
        #Launching the attack animation
        attackAnim.play()
        #If the player is attacking in the eaast
        if self.direction == "east":
            #Registering the attack for enemies
            for j in bad_block_list:
                if j.rect.x  > self.rect.x and (j.rect.x - 250) < self.rect.x:
                    if j.rect.y > (self.rect.y - 250) and j.rect.y < (self.rect.y + 250):
                        j.rect.x = 100000
                        j.rect.y = 100000
        #If the player is attacking in the south
        elif self.direction == "south":
            #Registering the attack for the enemies
            for j in bad_block_list:
                if (self.rect.x + 50) > j.rect.x and (j.rect.x - 50) < self.rect.x:
                    if j.rect.y > self.rect.y and j.rect.y < (self.rect.y + 250):
                        j.rect.x = 100000
                        j.rect.y = 100000
        #If the player is attacking in the west
        elif self.direction == "west":
            #Registering the attack for the enemies
            for j in bad_block_list:
                if j.rect.x  < self.rect.x and (j.rect.x + 200) > self.rect.x:
                    if j.rect.y > (self.rect.y - 250) and j.rect.y < (self.rect.y + 250):
                        j.rect.x = 100000
                        j.rect.y = 100000
        #If the player is attacking in the north
        elif self.direction == "north":
            #Registering the attack for the enemies
            for j in bad_block_list:
                if (self.rect.x + 50) > j.rect.x and (j.rect.x - 50) < self.rect.x:
                    if j.rect.y < self.rect.y and j.rect.y > (self.rect.y - 200):
                        j.rect.x = 100000
                        j.rect.y = 100000

#Creating a class for the walls
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #Where the width, height, x, and y are used
        self.image = pygame.Surface((width,height))
        #Filling the walls blue
        self.image.fill(BLUE)
        #Gathering the position of the walls
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
            
#Creating the enemy class
class Enemy(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
    #Methods
    def __init__(self, x, y, speed, kind, e_w, e_h,animObjs1):
        """Constructor function"""
        #Call the parent's constructor
        super().__init__()
        #Set height, width and filling the colour for the player
        self.image = pygame.Surface([e_w, e_h])
        #Variable to define which enemy is needed//
        self.kind = kind
        #Loading the transparent backgrounds for the enemy types
        if self.kind == "training":
            self.image = pygame.image.load("Transparents/Transparent_Dummy.png")
        if self.kind == "mask":
            self.image = pygame.image.load("Transparents/Transparent_mask.png")
        if self.kind == "phantom":
            self.image = pygame.image.load("Transparents/Transparent_Phantom.png")
        if self.kind == "wraith":
            self.image = pygame.image.load("Transparents/Tranparent_Brwraith.png")
        if self.kind == "healthup":
            self.image = pygame.image.load("Knights_Honour_sprites/Power_ups/Health.png")
        if self.kind == "invincible":
            self.image = pygame.image.load("Knights_Honour_sprites/Power_ups/Invincible.png")
        if self.kind == "speed":
            self.image = pygame.image.load("Knights_Honour_sprites/Power_ups/Speed.png")
        #Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Defining the walls variable
        self.walls = ''
        
        #Attributes
        #Set speed vector
        self.change_x = 0
        self.change_y = 0
        #Setting the speed
        self.speed = speed
        #Creating the direction variable
        self.direction = ""
        #Boolean variables if the enemies are moving
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        #Adding an additional verification that it is not a powerup
        if not self.kind == "healthup" or not self.kind == "invincible" or not self.kind == "speed":
            #Creating the animation conductor
            self.moveConductor = pyganim.PygConductor(animObjs1)
    #Defining function changespeed for the enemies
    def changespeed(self, x, y):
        """ Change the speed of the enemy"""
        self.change_x += x
        self.change_y += y
    def update(self,wall):
        """ Find a new position for the enemy"""
        #Updating the enemy with movement in the x
        self.rect.x += self.change_x
        #If the enemy collides with a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
        #Moving the enemy if they collide with a wall
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        #Updating the enemy with their movement in the y
        self.rect.y += self.change_y
        #If the enemy collides with a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
        #Moving the enemy if they collide with a wall
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        #Gathering the location of the enemy
        enemy_location=[self.rect.x,self.rect.y]
        #Creating the block hit list
        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
        #All locations of the enemy
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        #Calculating the movement style of the enemy
        dx=player_location[0]-enemy_location[0]
        dy=player_location[1]-enemy_location[1]
        #Using the hypotenuse of a triangle for enemy movement
        hyp=(dx**2+dy**2)**(1/2)
        ratio=self.speed/hyp
        x_speed=dx*ratio
        y_speed=dy*ratio
        #Adjusting enemy speed
        self.change_x=x_speed
        self.change_y=y_speed
        #Setting directional variables based off enemy movement
        if enemy_location[1] > player_location[1]:
            self.direction = "north"
            self.moveUp = True
        elif enemy_location[1] < player_location[1]:
            self.change_y =self.speed
            self.direction = "south"
            self.moveDown = True
        elif enemy_location[0] > player_location[0]:
            self.direction = "west"
            self.moveLeft = True
        elif enemy_location[0] < player_location[0]:
            self.direction = "east"
            self.moveRight = True
        #If the enemy moves into a block
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

#Creating the wall list
wall_list = pygame.sprite.Group()


'''---------------------------------Animation Logic------------------------------------'''
#Defining variables for direction and attack
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
SPACE = 'attack'
#If the enemies have to be drawn
drawEnemy = False
#All the still positions of the player
front_standing = pygame.image.load('Knights_Honour_sprites/player_sprites/knight_front.gif')
back_standing = pygame.image.load('Knights_Honour_sprites/player_sprites/knight_back.gif')
right_standing = pygame.image.load('Knights_Honour_sprites/player_sprites/knight_right_turn.gif')
left_standing = pygame.transform.flip(right_standing, True, False)
#Retrieving the size of the player
playerWidth, playerHeight = front_standing.get_size()
#Loading the player images to cycle through
animTypes = 'back_walk front_walk right_walk left_walk'.split()

#Animation for the training dummies
training_animObjs = {}
for animType in animTypes:
    #Locating and retrieving each animation image to cycle through
    imagesAndDurations = [('Knights_Honour_sprites/Dummy_sprite/Dummy_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(3)]
    training_animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
#Animation for the purple floating wraiths
wraith_animObjs = {}
for animType in animTypes:
    #Locating and retrieving each animation image to cycle through
    imagesAndDurations = [('Knights_Honour_sprites/Brwraith_sprite/Brwraith_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(2)]
    wraith_animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
#Animation for the tree masks
mask_animObjs = {}
for animType in animTypes:
    #Locating and retrieving each animation image to cycle through
    imagesAndDurations = [('Knights_Honour_sprites/Willow_mask_sprite/Willow_mask_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(2)]
    mask_animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
#Animation for the phantom knight sprites
phantom_animObjs = {}
for animType in animTypes:
    #Locating and retrieving each animation image to cycle through
    imagesAndDurations = [('Knights_Honour_sprites/Phantom_Sprites/Phantom_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(4)]
    phantom_animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

#Creating the PygAnimation objects for walking in all directions
animObjs = {}
for animType in animTypes:
    #Locating and retrieving each animation image to cycle through
    imagesAndDurations = [('Knights_Honour_sprites/player_sprites/knight_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
    animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

#Locating and retrieving each animation image to cycle through for the player attack-- 
attackAnim = pyganim.PygAnimation([('Knights_Honour_sprites/player_attack_sprites/blade_spin.000.png', 0.1),
                                   ('Knights_Honour_sprites/player_attack_sprites/blade_spin.001.png', 0.1),
                                   ('Knights_Honour_sprites/player_attack_sprites/blade_spin.002.png', 0.1),
                                   ('Knights_Honour_sprites/player_attack_sprites/blade_spin.003.png', 0.1)])

#Locating and retrieving each animation image to cycle through for the final boss movement
ZaddikaiAnim = pyganim.PygAnimation([('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.000.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.001.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.002.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.003.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.004.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.005.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.006.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.007.gif', 0.1),
                                     ('Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.008.gif', 0.1)])
'''
Have the animation objects managed by a conductor. With the conductor,
we can call play() and stop() on all the animtion objects at the same time, so
that way they'll always be in sync with each other
'''
moveConductor = pyganim.PygConductor(animObjs)
#Player starts off facing down (front)
direction = DOWN
#Defines the walkrate (speed)
walkrate = 6
moveUp = moveDown = moveLeft = moveRight = attack = False

'''---------------------------------Variables------------------------------------'''
#Timer
timer_tutorial = 0
#Counter for tutorial prompt boxes
teaching_counter = 0
#This is a list of 'sprites.' Each block in the program is
#added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
power_up_list = pygame.sprite.Group()
#This is a list of every sprite. 
#All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
#Create a player
player = Player(610, 295)
all_sprites_list.add(player)
#Adds player to sprite list
player.walls = wall_list
player_location=[player.rect.x,player.rect.y]
#Sets the initial player health
player_health = 5
#If we need to draw the sprites
sprites_draw_needed = False
#Controlling whether or not player is on gui
gui = 0
#Playing game sound
playing_game_sound = False
#While loop count
while_loop_count = 0
#X and y are the player's position
x_anim = player.rect.x
y_anim = player.rect.y
#If the wall positions need to be reset
wall_reset = False
#Counter for the limit on enemy spawning
enemy_counter = 0
#Rendering the first font
font = pygame.font.SysFont('Arial', 25, True, False)
#If attacking the boss text has to be displayed
attackBoss = False
#The credits movement speed
credits_y_one = 680
credits_y_two = 680
credits_y_three = 680
credits_y_four = 680
credits_y_five = 680
#Selecting the loot item variable
loot_variable_lvl1 = random.randrange(1,4)
#Counter for final boss attack
space_counter = 0
#Separate variable control
moving = 0
#Attacks remaining for survival mode
attacks_left = 10
#Mode
mode = "none"
#Checking if survival has already begun
survival_started = False

'''--------------Pictures--------------'''
#Tutorial loading screen
backGround = pygame.image.load("Cutscenes/Tutorial Screen.png")
#Tutorial floor
tutorial_ground = pygame.image.load("Floors/tutorial_floor.png")
#Boss Ground
boss_ground = pygame.image.load("Floors/boss_ground.png")
#--Text boxes for tutorial--
#Cutscene one
cutscene_one = pygame.image.load("Cutscenes/Tutorial_Cutscene1.png")
#Cutscene two
cutscene_two = pygame.image.load("Cutscenes/Tutorial_Cutscene2.png")
#Cutscene three
cutscene_three = pygame.image.load("Cutscenes/Tutorial_Cutscene3.png")
#Cutscene four
cutscene_four = pygame.image.load("Cutscenes/Tutorial_Cutscene4.png")
#W for forward
w_forward = pygame.image.load("Tutorial_Prompts/W_forward.png")
#S for backwards
s_backward = pygame.image.load("Tutorial_Prompts/S_backwards.png")
#A for left
a_left = pygame.image.load("Tutorial_Prompts/A_left.png")
#D for right
d_right = pygame.image.load("Tutorial_Prompts/D_right.png")
#Space for attack
space_attack = pygame.image.load("Tutorial_Prompts/Space_attack.png")
#Enter for continue
enter_skip = pygame.image.load("Tutorial_Prompts/Enter_skip.png")
#Level One Cutscene
levelOneCutscene = pygame.image.load("Cutscenes/Level One Cutscene.png")
#Level One Ground
levelOneGround = pygame.image.load("Floors/Level One Ground.png")
#Loading screen for Survival
loadingScreenSurvival1 = pygame.image.load("Cutscenes/Survival_Loading_Screen.png")
#Live Tree
live_tree = pygame.image.load("floors/tree.gif")
#Transparent wall
fancywall = pygame.image.load("floors/light_screen.png")
#Enhanced Edition
enhancedEdition = pygame.image.load("Cutscenes/EnhancedEdition.png")
#Boss iamge
boss_front = pygame.image.load("Knights_Honour_sprites/Zaddikai_sprites/Zaddikai.000.gif")
#Level One End Cutscene
levelOneExitScene = pygame.image.load("Cutscenes/levelOneExitPrompt.png")
#Town Square Intro Screen
townSquareIntro = pygame.image.load("Cutscenes/townSquareIntro.png")
#Town Square Cutscene One
townSquareSceneOne = pygame.image.load("Cutscenes/TownSquareScene1.png")
#Town Square Cutscene Two
townSquareSceneTwo = pygame.image.load("Cutscenes/TownSquareScene2.png")
#Level Two Intro
levelTwoIntro = pygame.image.load("Cutscenes/Level Two Intro.png")
#Level Two Ground
levelTwoGround = pygame.image.load("Floors/level2.png")
#Level Two Exit Scene One
levelTwoExitOne = pygame.image.load("Cutscenes/levelTwoExitOne.png")
#Level Two Exit Scene Two
levelTwoExitTwo = pygame.image.load("Cutscenes/levelTwoExitTwo.png")
#Death Screen
deathScreen = pygame.image.load("Cutscenes/Death_Screen.png")
#Selection Screen 
survivalSelection = pygame.image.load("Cutscenes/Survival_Selection.png")
#Boss Cutscene
bossCutscene = pygame.image.load("Cutscenes/BossCutsceneOne.png")
#MidBoss Cutscene
MidBossScene = pygame.image.load("Cutscenes/MidBossScene.png")
#Attack Text
AttackText = pygame.image.load("Cutscenes/BossAttack.png")
#--Final Cutscenes
BossFightExitScene = pygame.image.load("Cutscenes/BossFightExitScene.png")
ExitSceneTwo = pygame.image.load("Cutscenes/ExitSceneTwo.png")
ExitSceneThree = pygame.image.load("Cutscenes/ExitSceneThree.png")
ExitSceneFour = pygame.image.load("Cutscenes/ExitSceneFour.png")
#Credits Roll
CreditsRoll = pygame.image.load("Cutscenes/CreditsRoll.png")
#Credits speed
y_offset_credits = 5
#--Credits Text
developed_by = font.render("Developed By:",True, WHITE)
_Young = font.render("Austin Young - Code",True, WHITE)
_Blais = font.render("Joel Blais - Art",True, WHITE)
#--Loot Screens
#Level one
steel_dagger_img = pygame.image.load("Loot_Screens/steel_dagger.png")
steel_sword_img = pygame.image.load("Loot_Screens/steel_sword.png")
steel_battle_axe_img = pygame.image.load("Loot_Screens/steel_axe.png")
#Level two
tungsten_greatsword_img = pygame.image.load("Loot_Screens/tungsten_sword.png")
#--Final Boss Health
boss_health_6 = pygame.image.load("Cutscenes/Boss_Health_6.png")
boss_health_5 = pygame.image.load("Cutscenes/Boss_Health_5.png")
boss_health_4 = pygame.image.load("Cutscenes/Boss_Health_4.png")
boss_health_3 = pygame.image.load("Cutscenes/Boss_Health_3.png")
boss_health_2 = pygame.image.load("Cutscenes/Boss_Health_2.png")
boss_health_1 = pygame.image.load("Cutscenes/Boss_Health_1.png")

#Defining many new boolean values for the power ups 
invincibleup = False
speedup = False
healthup = False
invincibleOn = False
#Defining the time detection variables equal to 0 
time_spent = 0
time_spent_speed = 0
#One more boolean for the speed boost and a power up counter
speedBoost = False
powerup_count = 0

#New Highscore system!
#Opens file
file = open('highscore.txt','r')
#Saves text
text = file.readlines()
#Does a literal evaulation of the string to determine if it is actually a list
text = ast.literal_eval(text[0])

#Closes file
file.close()
#Current highscore
highscore = int(math.floor((len(text)**0.5)))


''' ------------------------ Game Screens and Functions ----------------------'''
''' This part of the code defines what the screen looks like.
    This does not include any actions or events. '''
#Creates the main screen
def mainScreen():
    #Loading the GUI mainscreen
    backGround = pygame.image.load("Cutscenes/Menu Screen.png")
    #Displaying it to the screenBryadon
    screen.blit(backGround,[ 0, 0])
    screen.blit(enhancedEdition,[0,100])
#Creates the instruction screen
def instructionScreen():
    #Loading the GUI instructions
    backGround = pygame.image.load("Cutscenes/Instruction Screen.png")
    #Displaying it to the screen
    screen.blit(backGround,[ 0, -4])
#Creates the survival screen
def survivalSelection():
    #Loading the GUI instructions
    backGround = pygame.image.load("Cutscenes/Survival_Selection.png")
    #Displaying it to the screen
    screen.blit(backGround,[ 0, -4])
#Creates the power ups
def powerUps():
    #Generates a random number from 1-12
    random_number = random.randint(1,12)
    #Sets all my earlier boolean values to global
    global speedup
    global healthup
    global invincibleup
    #If the random number is one then the power up is a health boost
    if random_number == 1:
        #Sets the other booleans to false
        invincibleup = False
        speedup = False
        #Creates the power up to a random location
        healthup = Enemy(random.randint(300,700),random.randint(200,550),0,"healthup",50,50,0)
        #Adds the power up to a list
        power_up_list.add(healthup)
        healthup = True
    #If the random number is two then the power up is an invincibility boost
    elif random_number == 2:
        #Sets the other booleans to false
        invincibleup = True
        speedup = False
        healthup = False
        #Creates the power up to a random location
        invincibleup = Enemy(random.randint(300,700),random.randint(200,550),0,"invincible",50,50,0)
        #Adds the power up to a list
        power_up_list.add(invincibleup)
        invincibleup = True
    #If the random number is three then the power up is a speed boost
    elif random_number == 3:
        #Sets the other booleans to false
        invincibleup = False
        speedup = True
        healthup = False
        #Creates the power up to a random location
        speedup = Enemy(random.randint(300,700),random.randint(200,550),0,"speed",50,50,0)
        #Adds the power up to a list
        power_up_list.add(speedup)
        speedup = True

'''------------------------------------SOUNDS------------------------------------'''
''' This section of code generates background music and effects. '''
#Background Menu Music
pygame.mixer.music.load("Sounds/Menu_Music.wav")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(-1)
#Menu Effect
menuSelect = pygame.mixer.Sound("Sounds/Sword Effect.wav")
#Changes the sound of the sword effect
menuSelect.set_volume(0.5)
#Attack Sound
attack_sound = pygame.mixer.Sound("Sounds/attack_sound.wav")
#Loot Sound
loot_sound = pygame.mixer.Sound("Sounds/Loot_Sound.wav")
#Survival Music
survivalMusic = pygame.mixer.Sound("Sounds/SurvivalBattleMusic.wav")


''' --------------------- Main Program Loop --------------------'''
while not done:
    ''' ---------------------GUI LOOP--------------------'''
    #If the player is in the GUI
    while gui == 0:
        for event in pygame.event.get():
            #Actions for mouse clicks

            if event.type == pygame.MOUSEBUTTONDOWN:
                #gets the position of the mouse
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                #If the mouse clicks on the main screen

                if currentScreen == "mainScreen":
                    #Play game button
                    if x >= 95 and x <= 250 and y >= 320 and y <= 375:
                        menuSelect.play()
                        #Sets the current screen value to first level loading screen
                        #currentScreen = "loadingScreen"
                        currentScreen = "Survival_Selection"
                        #Stops the menu screen music
                        pygame.mixer.music.stop()
                        #Fills the screen black
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Stops the program for a simulated loading screen
                        gui = 0
                    #Open instructions
                    elif x >= 95 and x <= 555 and y >= 450 and y <= 505:
                        menuSelect.play()
                        #Keeping track of the current screen
                        currentScreen = "instructionScreen"
                    #Quit Game
                    elif x >= 95 and x <= 245 and y >= 580 and y <= 635:
                        #Exits entire program loop
                        gui = 2
                        done = True
                elif currentScreen == "Survival_Selection":
                    #Play game button
                    if x >= 130 and x <= 350 and y >= 170 and y <= 250:
                        menuSelect.play()
                        #Sets the current screen value to first level loading screen
                        currentScreen = "loadingScreen"
                        #Stops the menu screen music
                        pygame.mixer.music.stop()
                        #Fills the screen black
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Stops the program for a simulated loading screen
                        time.sleep(2)
                        #Exiting the gui loop
                        gui = 1
                    #Open instructions
                    elif x >= 800 and x <= 1180 and y >= 170 and y <= 250:
                        menuSelect.play()
                        #Keeping track of the current screen
                        currentScreen = "loadingScreenSurvival"
                        pygame.mixer.music.stop()
                        #Fills the screen black
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Stops the program for a simulated loading screen
                        time.sleep(2)
                        #Exiting the gui loop
                        gui = 1
                #Returning from the instruction screen
                elif currentScreen == "instructionScreen":
                    #Return to Menu - RETURN
                    if x >= 90 and x <= 340 and y >= 660 and y <= 705:
                        menuSelect.play()
                        currentScreen = "mainScreen"
        
        #Clearing the screen
        screen.fill(BLACK)
        
        '''--------------MANEUVERING THROUGHOUT THE MENU-------------'''
        ''' This section of code deals with changing the screen when a command is
        clicked, i.e going to the instruction screen. '''
        #Checking the current screen
        if currentScreen == "mainScreen":
            mainScreen()
        #Checking the current screen
        elif currentScreen == "instructionScreen":
            instructionScreen()
        #Checking the current screen
        if currentScreen == "Survival_Selection":
            survivalSelection()

        
        #Updating the screen
        pygame.display.flip()
        #60 frames per second
        clock.tick(60)

        
    ''' ---------------------GAME LOOP--------------------'''
    #If the player has pressed play
    while gui == 1:
        #Making the mouse invisible
        pygame.mouse.set_visible(False)
        #Creating the tutorial ground
        if currentScreen == "tutorial":
            screen.blit(tutorial_ground,[0,0])
        #Update player location
        player_location=[player.rect.x,player.rect.y]
        #Playing the ingame music
        if playing_game_sound:
            #Background Game Music
            pygame.mixer.music.load("Sounds/Game_Music.wav")
            pygame.mixer.music.play(-1)
            playing_game_sound = False
        for event in pygame.event.get():
            #Closing the program
            if event.type == pygame.QUIT:
                done = True
            #When buttons are pressed down
            elif event.type == pygame.KEYDOWN:
                #User presses escape and exits
                if event.key == pygame.K_ESCAPE:
                    gui = 2
                    done = True
                #User presses enter to cycle screens
                elif event.key == pygame.K_RETURN:
                    #Survival Mode Selection
                    if currentScreen == "loadingScreenSurvival":
                        currentScreen = "survivalMode"
                        #Setting the mode
                        mode = "survival"
                        if survival_started == False:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("Sounds/SurvivalBattleMusic.wav")
                            pygame.mixer.music.play(-1)
                        survival_started = True
                    #Cycling to tutorial
                    elif currentScreen == "loadingScreen":
                        #Playing the music
                        playing_game_sound = True
                        #Going to the next screen
                        currentScreen = "cutsceneOne"
                        mode = "story"
                    #Cycling through the knight speeches
                    elif currentScreen == "cutsceneOne":
                        #Going to the next screen
                        currentScreen = "cutsceneTwo"
                    #Going to the second speech bubble before tutorial
                    elif currentScreen == "cutsceneTwo":
                        #Setting the screen to the tutorial
                        currentScreen = "tutorial"
                        #Creating the walls in the tutorial
                        wall = Wall(0,100,764,10)
                        wall_list.add(wall)
                        wall = Wall(764,0,10,110)
                        wall_list.add(wall)
                    #If the player is on the third cutscene
                    elif currentScreen == "cutsceneThree":
                        #Going to the next screen
                        currentScreen = "cutsceneFour"
                    #If the player is on cutscene four
                    elif currentScreen == "cutsceneFour":
                        #Stop the music and load the cutscene music
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Sounds/Cutscene One.wav")
                        #Screen goes to black
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Stop the program to simulate a loading screen
                        time.sleep(2)
                        #Launch the next level music
                        pygame.mixer.music.play(-1)
                        #Set the current screen to the first level cutscene
                        currentScreen = "levelOneCutscene"
                    #If enter was pressed on the level one intro cutscene
                    elif currentScreen == "levelOneCutscene":
                        #Stops the previous music and plays the new music
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Sounds/level1.wav")
                        pygame.mixer.music.play(-1)
                        #Creates the walls for level one
                        wall_list = 0
                        wall_list = pygame.sprite.Group()
                        wall = Wall(100,200,125,260)
                        wall_list.add(wall)
                        #wall = Wall(600,400,125,260)
                        #wall_list.add(wall)
                        wall = Wall(900,100,125,260)
                        wall_list.add(wall)
                        player.walls = wall_list
                        #Setting the amount of health the player has
                        player_health = 5
                        #Cycling from intro scene to the actual level
                        currentScreen = "levelOneGround"
                    #If player is exiting level one
                    elif currentScreen == "levelOneExitScene":
                        #Stopping the level music and playing loot sound
                        pygame.mixer.music.stop()
                        currentScreen = "levelOneLoot"
                        loot_sound.play()
                    #Exiting the loot screen
                    elif currentScreen == "levelOneLoot":
                        #Going through the midtown cutscenes
                        currentScreen = "townSquareIntro"
                        #Simulating a loading screen
                        screen.fill(BLACK)
                        pygame.display.flip()
                        time.sleep(2)
                    #In the first town square scene
                    elif currentScreen == "townSquareIntro":
                        #Clearing all sprite lists and variables
                        good_block_list = 0
                        bad_block_list = 0
                        power_up_list = 0
                        wall_list = 0
                        wall_list = pygame.sprite.Group()
                        all_sprites_list = 0
                        good_block_list = pygame.sprite.Group()
                        bad_block_list = pygame.sprite.Group()
                        power_up_list = pygame.sprite.Group()
                        while_loop_count = 0
                        enemy_counter = 0
                        #Setting the player health for level two
                        player_health = 15
                        #This is a list of every sprite. 
                        #All blocks and the player block as well.
                        all_sprites_list = pygame.sprite.Group()
                        #Creating the player
                        player = Player(610, 295)
                        all_sprites_list.add(player)

                        wall = Wall(0,0,220,screen_height)
                        wall_list.add(wall)
                        wall = Wall(screen_width-250,0,1000,screen_height)
                        wall_list.add(wall)
                        player.walls = wall_list
                        #Cycling to the second town square cutscene
                        currentScreen = "townSquareSceneOne"
                    elif currentScreen == "townSquareSceneOne":
                        currentScreen = "townSquareSceneTwo"
                        screen.fill(BLACK)
                    #Cycling to the third tpwn square cutscene
                    elif currentScreen == "townSquareSceneTwo":
                        currentScreen = "levelTwoIntro"
                        screen.fill(BLACK)
                        pygame.display.flip()
                        time.sleep(2)
                    #Intro to the second level
                    elif currentScreen == "levelTwoIntro":
                        currentScreen = "levelTwoGround"
                        #Starting the music for level two
                        pygame.mixer.music.load("Sounds/Level 2 song.wav")
                        pygame.mixer.music.play(-1)
                    #Exiting level two
                    elif currentScreen == "levelTwoExitSceneOne":
                        currentScreen = "levelTwoExitSceneTwo"
                        screen.fill(BLACK)
                    #Leaving level two and getting loot
                    elif currentScreen == "levelTwoExitSceneTwo":
                        #Playing the loot sound
                        pygame.mixer.music.stop()
                        currentScreen = "levelTwoLoot"
                        loot_sound.play()
                    #Exiting level two and moving to the boss intro
                    elif currentScreen == "levelTwoLoot":
                        currentScreen = "BossCutscene"
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Simulating a black cutscene
                        time.sleep(2)
                    #Moving to the boss level
                    elif currentScreen == "BossCutscene":
                        currentScreen = "FinalBossGround"
                        powerup_count = 0
                        #Resetting the sprite lists and variables
                        good_block_list = 0
                        bad_block_list = 0
                        power_up_list = 0
                        wall_list = 0
                        wall_list = pygame.sprite.Group()
                        all_sprites_list = 0
                        good_block_list = pygame.sprite.Group()
                        bad_block_list = pygame.sprite.Group()
                        power_up_list = pygame.sprite.Group()
                        while_loop_count = 0
                        enemy_counter = 0
                        #Setting player health for the level
                        player_health = 15
                        #This is a list of every sprite.
                        #All blocks and the player block as well.
                        all_sprites_list = pygame.sprite.Group()
                        #Creating the player
                        player = Player(610, 700)
                        all_sprites_list.add(player)
                        #Creating the wall
                        wall = Wall(0,0,screen_width,260)
                        wall_list.add(wall)
                        #Drawing the enemies
                        drawEnemy = True
                        player.walls = wall_list
                        #Playing the sounds
                        pygame.mixer.music.load("Sounds/BossMusic.wav")
                        pygame.mixer.music.play(-1)
                    #Midway through the boss fight
                    elif currentScreen == "MidBossScene":
                        sprites_draw_needed = True
                        drawEnemy = True
                        currentScreen = "BossFightPartTwo"
                    #Cycling through the final cutscenes of the game
                    elif currentScreen == "BossFightExitScene":
                        currentScreen = "ExitSceneTwo"
                    elif currentScreen == "ExitSceneTwo":
                        currentScreen = "ExitSceneThree"
                    elif currentScreen == "ExitSceneThree":
                        currentScreen = "ExitSceneFour"
                    #Entering the credits
                    elif currentScreen == "ExitSceneFour":
                        currentScreen = "Credits"
                        #Stopping the boss music
                        pygame.mixer.music.stop()
                        screen.fill(BLACK)
                        pygame.display.flip()
                        #Simulating loading screen
                        time.sleep(2)
                        #Loading credits image and song
                        pygame.mixer.music.load("Sounds/CreditsSong.wav")
                        pygame.mixer.music.play(-1)
                        screen.fill(BLACK)
                        screen.blit(CreditsRoll, [0,0])
                    
                #When key up is pressed
                if event.key == pygame.K_UP:
                    """ """
                    moving = 1
                    #Walking through tutorial controls
                    if teaching_counter==0:
                        teaching_counter += 1
                    #Player changing speed and direction/
                    player.changespeed(0, -walkrate/2)
                    player.direction = "north"
                    moveUp = True
                    moveDown = False
                    if not moveLeft and not moveRight:
                    #Only change the direction to up if the player wasn't moving left or right
                        direction = UP
                #When key down is pressed
                elif event.key == pygame.K_DOWN:
                    """ """
                    moving = 2
                    #Walking through tutorial controls
                    if teaching_counter==1:
                        teaching_counter += 1
                    #Player changing speed and direction/
                    player.changespeed(0, walkrate/2)
                    player.direction = "south"
                    moveDown = True
                    moveUp = False
                    if not moveLeft and not moveRight:
                        #Only change the direction to up if the player wasn't moving left or right
                        direction = DOWN
                #When key left is pressed
                elif event.key == pygame.K_LEFT:
                    """ """
                    moving = 3
                    #Walking through tutorial controls
                    if teaching_counter==2:
                        teaching_counter += 1
                    #Player changing speed and direction/
                    player.changespeed(-walkrate/2, 0)
                    player.direction = "west"
                    moveLeft = True
                    moveRight = False
                    if not moveUp and not moveDown:
                        #Only change the direction to up if the player wasn't moving left or right
                        direction = LEFT
                #When key right is pressed
                elif event.key == pygame.K_RIGHT:
                    """ """
                    moving = 4
                    #Walking through tutorial controls
                    if teaching_counter==3:
                        teaching_counter += 1
                    #Player changing speed and direction/
                    player.changespeed(walkrate/2, 0)
                    player.direction = "east"
                    moveRight = True
                    moveLeft = False
                    if not moveUp and not moveDown:
                        #Only change the direction to up if the player wasn't moving left or right
                        direction = RIGHT
                #When space button is pressed
                elif event.key == pygame.K_SPACE:
                    #Checks if the mode is story
                    if mode == "story":
                        #Sets the direction to attack
                        direction = SPACE
                        #Walking through tutorial controls
                        if teaching_counter==4:
                            teaching_counter += 1
                            currentScreen = "cutsceneThree"
                            sprites_draw_needed = False
                        #Counting the attacks on the boss fight
                        if currentScreen == "BossFightPartTwo":
                            space_counter +=1
                            #After six attacks exit the boss fight
                            if space_counter == 6:
                                currentScreen = "BossFightExitScene"
                                sprites_draw_needed = False
                                drawEnemy = False

                        #Sets the current time to a variable
                        setTime = time.time()
                        #Player attacking
                        player.attack()
                    #Checks if the game mode is survival
                    elif mode == "survival":
                        if attacks_left > 0:
                            #Sets the direction to attack
                            direction = SPACE
                            attacks_left -= 1
                            #Sets the current time to a variable
                            setTime = time.time()
                            #Player attacking
                            player.attack()


            #When keys are lifted
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    #Resetting player speed
                    player.changespeed(3, 0)
                    #Changing the direction player is facing
                    moveLeft = False
                    #Setting the player direction
                    if moveUp:
                        direction = UP
                    if moveDown:
                        direction = DOWN
                elif event.key == pygame.K_RIGHT:
                    #Resetting player speed
                    player.changespeed(-3, 0)
                    #Changing the direction player is facing
                    moveRight = False
                    #Setting the player direction
                    if moveUp:
                        direction = UP
                    if moveDown:
                        direction = DOWN
                elif event.key == pygame.K_UP:
                    #Resetting player speed
                    player.changespeed(0, 3)
                    #Changing the direction player is facing
                    moveUp = False
                    #Setting the player direction
                    if moveLeft:
                        direction = LEFT
                    if moveRight:
                        direction = RIGHT
                elif event.key == pygame.K_DOWN:
                    #Resetting player speed
                    player.changespeed(0, -3)
                    #Changing the direction player is facing
                    moveDown = False
                    #Setting the player direction
                    if moveLeft:
                        direction = LEFT
                    if moveRight:
                        direction = RIGHT
                elif event.key == pygame.K_SPACE:
                    #Resetting the animation as to stop the attack spinning
                    if moving == 3:
                        direction = LEFT
                    if moving == 4:
                        direction = RIGHT
                    if moving == 1:
                        direction = UP
                    if moving == 2:
                        direction = DOWN
                        
        '''------------------------GAME-------------------'''
        #Loading the transition screen to the tutorial
        if currentScreen == "loadingScreen":
            screen.blit(backGround,[0, 0])
        #First knight speech cutscene
        elif currentScreen == "loadingScreenSurvival":
            screen.blit(loadingScreenSurvival1,[0, 0])
            mode == "survival"
        elif currentScreen == "cutsceneOne":
            #Loading the ground
            screen.blit(tutorial_ground,[0,0])
            #Loading the first cutscene
            screen.blit(cutscene_one,[0,0])
        #Second knight speech cutscene
        elif currentScreen == "cutsceneTwo":
            #Loading the ground
            screen.blit(tutorial_ground,[0,0])
            #Loading the second cutscene
            screen.blit(cutscene_two,[0,0])
            
        #Tutorial
        elif currentScreen == "tutorial":
            #Initiaiting the sprites
            sprites_draw_needed = True
            while_loop_count += 1
            #Making the player invincible
            player_health = 5
            #All the user prompts
            if teaching_counter == 0:
                screen.blit(w_forward,[0,0])
            elif teaching_counter == 1:
                screen.blit(s_backward,[0,0])
            elif teaching_counter == 2:
                screen.blit(a_left,[0,0])
            elif teaching_counter == 3:
                screen.blit(d_right,[0,0])
            elif teaching_counter == 4:
                screen.blit(space_attack,[0,0])
            #Spawning enemies based after 5 seconds
            if while_loop_count == 300:
                #Resetting the counter
                while_loop_count = 0
                #Creating and adding enemy to sprite lists
                baddy = Enemy(random.randint(40,1200),random.randint(40,600),3,"training",1,92,training_animObjs)
                baddy.walls = wall_list
                baddy.direction = "Down"
                bad_block_list.add(baddy)
                all_sprites_list.add(baddy)
            #Creating and writing the health
            output_string = "Health: {0:01}".format(player_health)
            text_health = font.render((output_string),True,WHITE)
            screen.blit(text_health, [1050, 20])
            
        #Third knight speech cutscene
        elif currentScreen == "cutsceneThree":
            #Loading the ground
            screen.blit(tutorial_ground,[0,0])
            #Loading the third cutscene
            screen.blit(cutscene_three,[0,0])
        #Fourth knight speech cutscene
        elif currentScreen == "cutsceneFour":
            #Loading the ground
            screen.blit(tutorial_ground,[0,0])
            #Loading the fourth cutscene
            screen.blit(cutscene_four,[0,0])
            #Resetting some variable values
            wall_reset = True
            while_loop_count = 0
        #Cutscene Before Level One
        elif currentScreen == "levelOneCutscene":
            screen.blit(levelOneCutscene,[ 0, 0])
            #Removing all the walls
            while wall_reset == True:
                for wall in wall_list:
                    wall_list.remove(wall)
                wall_reset = False

        #Level One - Sticks & Stones
        elif currentScreen == "levelOneGround":
            #If the player has died
            if player_health <= 0:
                #Not drawing the sprites
                sprites_draw_needed = False
                #Stopping music
                pygame.mixer.music.stop()
                #Load death screen image
                screen.blit(deathScreen, [0,0])
                #Whether the player exits or restarts
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #Replaying the game from last cutscene
                        if event.key == pygame.K_RETURN:
                            #Change the current level to most recent cutscene
                            currentScreen = "levelOneCutscene"
                            #Resetting all the needed variables and sprites
                            good_block_list = 0
                            bad_block_list = 0
                            power_up_list = 0
                            wall_list = 0
                            wall_list = pygame.sprite.Group()
                            all_sprites_list = 0
                            powerup_count = 0
                            good_block_list = pygame.sprite.Group()
                            bad_block_list = pygame.sprite.Group()
                            power_up_list = pygame.sprite.Group()
                            enemy_counter = 0
                            player_health = 3
                            #This is a list of every sprite.
                            #All blocks and the player block as well.
                            all_sprites_list = pygame.sprite.Group()
                            #Creating the player
                            player = Player(610, 295)
                            all_sprites_list.add(player)
                            wall_list = 0
                            wall_list = pygame.sprite.Group()
                            wall = Wall(100,200,125,260)
                            wall_list.add(wall)
                            #wall = Wall(600,400,125,260)
                            #wall_list.add(wall)
                            wall = Wall(900,100,125,260)
                            wall_list.add(wall)
                            player.walls = wall_list
                        #If user chooses to exit the game
                        elif event.key == pygame.K_ESCAPE:
                            gui = 2
                            done = True
            #--If the player is alive
            elif player_health > 0:
                #Loading the ground
                screen.blit(levelOneGround,[ 0, 0])
                sprites_draw_needed = True
                #Loading the trees
                screen.blit(live_tree, [100,200])
                #screen.blit(live_tree, [600,400])
                screen.blit(live_tree, [900,100])

                #Enemy spawning
                while_loop_count += 1
                #Spawns an enemy every 2 seconds until nine have been spawned
                if while_loop_count == 120 and enemy_counter < 9:
                    #Calls the powerUps() function
                    powerUps()
                    while_loop_count = 0
                    #Spawns coming from a random direction
                    k = random.randint(1,4)
                    if k == 1:
                        baddy = Enemy(-100,random.randint(40,600),1,"wraith",42,109,wraith_animObjs)
                    if k == 2:
                        baddy = Enemy((screen_width + 100),random.randint(40,600),1,"wraith",42,109,wraith_animObjs)
                    if k == 3:
                        baddy = Enemy(random.randint(40,screen_width), -100 ,1,"wraith",42,109,wraith_animObjs)
                    if k == 4:
                        baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"wraith",42,109,wraith_animObjs)
                    #Starting direction and adding them to sprite lists
                    baddy.direction = "Down"
                    bad_block_list.add(baddy)
                    all_sprites_list.add(baddy)
                    enemy_counter +=1
                #Drawing the health text
                output_string = "Health: {0:01}".format(player_health)
                text_health = font.render((output_string),True,WHITE)
                screen.blit(text_health, [1050, 20])
                #Six seconds until the level continues and all enemies have been killed
                if while_loop_count == 360:
                    currentScreen = "levelOneExitScene"
                    sprites_draw_needed = False

        #Level one exit scene
        elif currentScreen == "levelOneExitScene":
            #Drawing the ground
            screen.blit(levelOneGround,[ 0, 0])
            #Loading the trees
            screen.blit(live_tree, [100,200])
            #screen.blit(live_tree, [600,400])
            screen.blit(live_tree, [900,100])
            #Loading the final cutscene
            screen.blit(levelOneExitScene, [0,0])
        #Loading the level one loot
        elif currentScreen == "levelOneLoot":
            #Drawing the random loot to the screen
            if loot_variable_lvl1 == 1:
                screen.blit(steel_dagger_img, [0,0])
            elif loot_variable_lvl1 == 2:
                screen.blit(steel_sword_img, [0,0])
            elif loot_variable_lvl1 == 3:
                screen.blit(steel_battle_axe_img, [0,0])
        #Loading the town square cutscenes
        elif currentScreen == "townSquareIntro":
            screen.blit(townSquareIntro, [0,0])
        elif currentScreen == "townSquareSceneOne":
            screen.blit(townSquareSceneOne, [0,0])
        elif currentScreen == "townSquareSceneTwo":
            screen.blit(townSquareSceneTwo, [0,0])
        #Loading the level two intro scene
        elif currentScreen == "levelTwoIntro":
            screen.blit(levelTwoIntro, [0,0])

        #Level 2 - Inferno Mountain
        elif currentScreen == "levelTwoGround":
            #If the player has died
            if player_health <= 0:
                #Stopping the current music
                pygame.mixer.music.stop()
                #Not drawing the sprites
                sprites_draw_needed = False
                #Load death screen image
                screen.blit(deathScreen, [0,0])
                #Whether the player exits or restarts
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #Replaying the game from last cutscene
                        if event.key == pygame.K_RETURN:
                            #Change the current level
                            currentScreen = "levelTwoIntro"
                            #Resetting all the needed variables and sprites
                            good_block_list = 0
                            bad_block_list = 0
                            power_up_list = 0
                            wall_list = 0
                            powerup_count = 0
                            wall_list = pygame.sprite.Group()
                            all_sprites_list = 0
                            good_block_list = pygame.sprite.Group()
                            bad_block_list = pygame.sprite.Group()
                            power_up_list = pygame.sprite.Group()
                            enemy_counter = 0
                            #Setting the player health
                            player_health = 10
                            #This is a list of every sprite. 
                            #All blocks and the player block as well.
                            all_sprites_list = pygame.sprite.Group()
                            #Creating the player
                            player = Player(610, 295)
                            all_sprites_list.add(player)
                            wall_list = 0
                            wall_list = pygame.sprite.Group()
                            wall = Wall(0,0,220,screen_height)
                            wall_list.add(wall)
                            wall = Wall(screen_width-250,0,1000,screen_height)
                            wall_list.add(wall)
                            player.walls = wall_list
                        #Exiting the game
                        elif event.key == pygame.K_ESCAPE:
                            gui = 2
                            done = True
            #--If the player is alive
            elif player_health > 0:
                #Loading the level two ground
                screen.blit(levelTwoGround,[ 0, 0])
                sprites_draw_needed = True
                while_loop_count +=1
                powerup_count +=1
                if powerup_count == 120:
                    #Calls the powerUps() function
                    powerUps()
                    powerup_count = 0
                #Enemy spawning
                if enemy_counter < 50:
                    #Spawns 50 enemies every third of a second
                    if while_loop_count == 20:
                        while_loop_count = 0
                        #Spawns from a random direction
                        k = random.randint(3,4)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), -100 ,1,"mask",51,56,mask_animObjs)
                        if k == 4:
                            baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"mask",51,56,mask_animObjs)

                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Spawns 100 enemies every sixth of a second
                if enemy_counter < 150 and enemy_counter >= 50:
                    if while_loop_count == 10:
                        while_loop_count = 0
                        #Spawns from a random direction
                        k = random.randint(3,4)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), -100 ,1,"mask",51,56,mask_animObjs)
                        if k == 4:
                            baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"mask",51,56,mask_animObjs)

                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Spawns 150 enemies every thirtieth of a second
                if enemy_counter < 300 and enemy_counter >= 150:
                    if while_loop_count == 2:
                        while_loop_count = 0
                        #Spawns from a random direction
                        k = random.randint(3,4)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), -100 ,1,"mask",51,56,mask_animObjs)
                        if k == 4:
                            baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"mask",51,56,mask_animObjs)
                        baddy.walls = wall_list
                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Spawns 50 enemies every third of a second
                if enemy_counter < 350 and enemy_counter >= 300:
                    if while_loop_count == 20:
                        while_loop_count = 0
                        #Spawns from a random direction
                        k = random.randint(3,4)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), -100 ,1,"mask",51,56,mask_animObjs)
                        if k == 4:
                            baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"mask",51,56,mask_animObjs)
                        baddy.walls = wall_list
                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Drawing the health text
                output_string = "Health: {0:01}".format(player_health)
                text_health = font.render((output_string),True,WHITE)
                screen.blit(text_health, [1050, 20])
                #Giving player time before next level
                if while_loop_count == 360:
                    currentScreen = "levelTwoExitSceneOne"
                    sprites_draw_needed = False

        #Level two exit cutscenes
        elif currentScreen == "levelTwoExitSceneOne":
            screen.blit(levelTwoExitOne, [0,0])
        elif currentScreen == "levelTwoExitSceneTwo":
            screen.blit(levelTwoExitTwo, [0,0])
        elif currentScreen == "levelTwoLoot":
            screen.blit(tungsten_greatsword_img, [0,0])
        #Intro boss cutscene
        elif currentScreen == "BossCutscene":
            screen.blit(bossCutscene, [0,0])


        #Final Boss Level - Zaddikai's Castle
        elif currentScreen == "FinalBossGround":
            #If the player has died
            if player_health <= 0:
                #Not drawing the sprites
                sprites_draw_needed = False
                #Load death screen image
                screen.blit(deathScreen, [0,0])
                #Whether the player exits or restarts
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #Replaying the game from last cutscene
                        if event.key == pygame.K_RETURN:
                            #Change the current level
                            currentScreen = "BossCutscene"
                            #Stopping the sound
                            pygame.mixer.music.stop()
                            #Resetting all the needed variables and sprites
                            good_block_list = 0
                            bad_block_list = 0
                            power_up_list = 0
                            wall_list = 0
                            powerup_count = 0
                            wall_list = pygame.sprite.Group()
                            all_sprites_list = 0
                            good_block_list = pygame.sprite.Group()
                            bad_block_list = pygame.sprite.Group()
                            power_up_list = pygame.sprite.Group()
                            enemy_counter = 0
                            #Setting the player health
                            player_health = 10
                            #This is a list of every sprite.
                            #All blocks and the player block as well.
                            all_sprites_list = pygame.sprite.Group()
                            #Creating the player
                            player = Player(610, 700)
                            all_sprites_list.add(player)
                            #Creating the walls
                            wall_list = 0
                            wall_list = pygame.sprite.Group()
                            wall = Wall(0,0,screen_width,260)
                            wall_list.add(wall)
                            screen.blit(fancywall, [0,200])
                            player.walls = wall_list
                        #Replaying the game from last cutscene
                        elif event.key == pygame.K_ESCAPE:
                            gui = 2
                            done = True
            #--If the player is alive
            elif player_health > 0:
                screen.blit(boss_ground,[ 0, 0])
                screen.blit(fancywall, [0,200])
                screen.blit(boss_health_6, [0,0])
                sprites_draw_needed = True
                powerup_count +=1
                if powerup_count == 120:
                    #Calls the powerUps() function
                    powerUps()
                    powerup_count = 0
                #Enemy spawning
                while_loop_count += 1
                #First fifty enemies
                if enemy_counter < 50:
                    #Every third of a second mask enemies spawn
                    if while_loop_count == 20:
                        while_loop_count = 0
                        #Spawning from three random directions
                        k = random.randint(2,4)
                        if k == 2:
                            baddy = Enemy(-100, random.randint(40,screen_height) ,1,"mask",51,56,mask_animObjs)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), 850 ,1,"mask",51,56,mask_animObjs)
                        if k == 4:
                            baddy = Enemy(screen_width+100, random.randint(40,screen_height) ,1,"mask",51,56,mask_animObjs)
                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Next 150 enemies are wraiths
                if enemy_counter < 200 and enemy_counter >= 50:
                    #spawn every sixth of a second
                    if while_loop_count == 10:
                        while_loop_count = 0
                        #Spawning from three random directions
                        k = random.randint(2,4)
                        if k == 2:
                            baddy = Enemy(-100, random.randint(40,screen_height) ,1,"wraith",42,109,wraith_animObjs)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), 850 ,1,"wraith",42,109,wraith_animObjs)
                        if k == 4:
                            baddy = Enemy(screen_width+100, random.randint(40,screen_height) ,1,"wraith",42,109,wraith_animObjs)
                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Next 250 enemies are phantom knights
                if enemy_counter < 450 and enemy_counter >= 200:
                    #Spawn every twelfth of a second
                    if while_loop_count == 5:
                        while_loop_count = 0
                        #Spawning from three random directions
                        k = random.randint(2,4)
                        if k == 2:
                            baddy = Enemy(-100, random.randint(40,screen_height) ,1,"phantom",93,123,phantom_animObjs)
                        if k == 3:
                            baddy = Enemy(random.randint(40,screen_width), 850 ,1,"phantom",93,123,phantom_animObjs)
                        if k == 4:
                            baddy = Enemy(screen_width+100, random.randint(40,screen_height) ,1,"phantom",93,123,phantom_animObjs)
                        baddy.direction = "Down"
                        bad_block_list.add(baddy)
                        all_sprites_list.add(baddy)
                        enemy_counter +=1
                #Eight seconds before the next level
                if while_loop_count == 540:
                    currentScreen = "MidBossScene"
                    sprites_draw_needed = False
                #Writing the helath to the screen
                output_string = "Health: {0:01}".format(player_health)
                text_health = font.render((output_string),True,WHITE)
                screen.blit(text_health, [1050, 20])
        #Mid Boss Cutscene
        elif currentScreen == "MidBossScene":
            screen.blit(boss_ground, [0, 0])
            screen.blit(MidBossScene, [0,0])
            while_loop_count = 0
        #Final section of boss fight
        elif currentScreen == "BossFightPartTwo":
            screen.blit(boss_ground, [0,0])
            #Displaying enemy health every space click
            if space_counter == 0:
                screen.blit(boss_health_6, [0,0])
            elif space_counter == 1:
                screen.blit(boss_health_5, [0,0])
            elif space_counter == 2:
                screen.blit(boss_health_4, [0,0])
            elif space_counter == 3:
                screen.blit(boss_health_3, [0,0])
            elif space_counter == 4:
                screen.blit(boss_health_2, [0,0])
            elif space_counter == 5:
                screen.blit(boss_health_1, [0,0])
            while_loop_count +=1
            #Displaying the "attack the boss" message
            if while_loop_count > 20 and while_loop_count < 80:
                attackBoss = True
            else:
                attackBoss = False
            #Writing the health to the screen
            output_string = "Health: {0:01}".format(player_health)
            text_health = font.render((output_string),True,WHITE)
            screen.blit(text_health, [1050, 20])

        #Final Cutscenes
        elif currentScreen == "BossFightExitScene":
            screen.blit(boss_ground, [0,0])
            screen.blit(BossFightExitScene, [0,0])
        elif currentScreen == "ExitSceneTwo":
            screen.blit(boss_ground, [0,0])
            screen.blit(ExitSceneTwo, [0,0])
        elif currentScreen == "ExitSceneThree":
            screen.blit(boss_ground, [0,0])
            screen.blit(ExitSceneThree, [0,0])
        elif currentScreen == "ExitSceneFour":
            screen.blit(boss_ground, [0,0])
            screen.blit(ExitSceneFour, [0,0])
            while_loop_counter = 0
        #Survival mode!
        elif currentScreen == "survivalMode":
            #If the player has died
            if player_health <= 0:
                #Not drawing the sprites
                sprites_draw_needed = False
                #Load death screen image
                screen.blit(deathScreen, [0,0])
                #Whether the player exits or restarts
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        #Replaying the game from last cutscene
                        if event.key == pygame.K_RETURN:
                            #Change the current level
                            currentScreen = "loadingScreenSurvival"
                            #New Highscore system!
                            #Opens file
                            file = open('highscore.txt','r')
                            #Saves text
                            text = file.readlines()
                            #Literally evluates the data
                            text = ast.literal_eval(text[0])

                            #Closes file
                            file.close()
                            #Saves the highscore
                            highscore = int(math.floor((len(text)**0.5)))

                            #Checks if the new score is higher than the highscore
                            if enemy_counter > highscore:
                                #Saves the score as the lines to be written
                                #Squaring the highscore
                                number = enemy_counter*enemy_counter
                                #Making a list for the encryption
                                number_list = []
                                #Making the list full of the number
                                for i in range(number):
                                    number_list.append(i)
                                #Creating the character list
                                characters = []
                                #Encrypts
                                for i in number_list:
                                    #Multiplies the number by 4
                                    encrypt = i*4
                                    #Takes the integer then roots it
                                    encrypt = int(encrypt**0.5)
                                    #Takes the proper chr value and appends it to the list
                                    encrypt = chr(encrypt+40)
                                    #Adds them to characters
                                    characters.append(encrypt)
                                #Sets the lines to the list of characaters
                                lines = [characters]
                                #Sets the text to the list of enemy_counter
                                text = [enemy_counter]
                                highscore = enemy_counter
                                #Saves those lines to the text
                                with open('highscore.txt','w') as file:
                                    file.writelines("%s\n" % l for l in lines)
                            #Checks for a new highscore
                            #Resetting all the needed variables and sprites 
                            good_block_list = 0
                            bad_block_list = 0
                            power_up_list = 0
                            all_sprites_list = 0
                            good_block_list = pygame.sprite.Group()
                            bad_block_list = pygame.sprite.Group()
                            power_up_list = pygame.sprite.Group()
                            enemy_counter = 0
                            #Setting the player health
                            player_health = 5
                            #This is a list of every sprite.
                            #All blocks and the player block as well.
                            all_sprites_list = pygame.sprite.Group()
                            #Creating the player
                            wall_list = 0
                            wall_list = pygame.sprite.Group()
                            player = Player(610, 295)
                            player.walls = wall_list
                            all_sprites_list.add(player)
                            #Player starts off facing down (front)
                            direction = DOWN
                            moveUp = moveDown = moveLeft = moveRight = attack = False
                            #Sets both attacks_left and powerup_count to 0
                            attacks_left = 10
                            powerup_count = 0


                        elif event.key == pygame.K_ESCAPE:
                            gui = 2
                            done = True
            #--If the player is alive
            elif player_health > 0:
                powerup_count +=1
                if powerup_count == 120:
                    #Calls the powerUps() function
                    powerUps()
                    powerup_count = 0
                #Loading the level two ground
                screen.blit(boss_ground,[ 0, 0])
                sprites_draw_needed = True
                while_loop_count +=1
                if while_loop_count == 1:
                    teaching_counter = 0
                #Enemy spawning
                if while_loop_count == 20:
                    while_loop_count = 0
                    #Spawns from a random direction
                    k = random.randint(1,4)
                    if k == 1:
                        #From the right
                        baddy = Enemy(-100,random.randint(40,screen_height) ,1,"phantom",93,123,phantom_animObjs)
                    if k == 2:
                        #From the left
                        baddy = Enemy((screen_width+100),random.randint(40,screen_height) ,1,"mask",51,56,mask_animObjs)
                    if k == 3:
                        #Above screen
                        baddy = Enemy(random.randint(40,screen_width), -100 ,1,"wraith",42,109,wraith_animObjs)
                    if k == 4:
                        #Below screen
                        baddy = Enemy(random.randint(40,screen_width),(screen_height + 100),1,"training",1,92,training_animObjs)

                    baddy.direction = "Down"
                    bad_block_list.add(baddy)
                    all_sprites_list.add(baddy)
                    enemy_counter +=1

                #Drawing the health text
                output_string = "Health: {0:01}".format(player_health)
                text_health = font.render((output_string),True,WHITE)
                screen.blit(text_health, [1050, 20])
                #Drawing the attacks left
                output_string = "Attacks Left: {0:01}".format(attacks_left)
                text_health = font.render((output_string),True,WHITE)
                screen.blit(text_health, [1050, 70])
                #Drawing the score
                output_string = "Score: {0:01}".format(enemy_counter)
                text_score = font.render((output_string),True,WHITE)
                screen.blit(text_score, [1050, 120])
                #Checks if the highscore is greater than the current score
                if int(highscore) > enemy_counter:
                    #Draws the highscore
                    output_string = "Highscore: {0:01}".format(int(highscore))
                else:
                    #Draws the current score which must also be the high score
                    output_string = "Highscore: {0:01}".format(enemy_counter)
                text_highscore = font.render((output_string),True,WHITE)
                screen.blit(text_highscore, [1050, 170])
                #Giving player time before next level
                if while_loop_count == 360:
                    currentScreen = "levelTwoExitSceneOne"
                    sprites_draw_needed = False
        #Credits
        elif currentScreen == "Credits":
            screen.fill(BLACK)
            #Credits rolling
            y_offset_credits = 1
            while_loop_counter +=1
            credits_y_one -= y_offset_credits
            screen.blit(developed_by, [558, credits_y_one])
            #SPawning each line of text after a specific time limit
            if while_loop_counter > 120:
                screen.blit(_Young, [560, credits_y_two])
                credits_y_two -= y_offset_credits
            if while_loop_counter > 170:
                screen.blit(_Lebeau, [562, credits_y_three])
                credits_y_three -= y_offset_credits
            if while_loop_counter > 220:
                screen.blit(_Strik, [560, credits_y_four])
                credits_y_four -= y_offset_credits
            if while_loop_counter > 270:
                screen.blit(_Blais, [575, credits_y_five])
                credits_y_five -= y_offset_credits
            screen.blit(CreditsRoll, [0,0])
            
                
        #Draw all the sprites
        if sprites_draw_needed:
            if invincibleOn == True:
                player_health = saved_health
                time_spent += 1
                if time_spent == 120:
                    invincibleOn = False
                    time_spent = 0
            if speedBoost == True:
                walkrate = 8
                time_spent_speed += 1
                if time_spent_speed == 120:
                    speedBoost = False
                    walkrate = 6
                    time_spent_speed = 0
            #Updates the players location
            player.update(wall_list)
            all_sprites_list.update(wall_list)
            all_sprites_list.draw(screen)
            power_up_list.draw(screen)
            #Drawing attack text after everything else
            if attackBoss == True:
                screen.blit(AttackText, [0,0])
            #If the boss animation has to happen
            if drawEnemy == True:
                ZaddikaiAnim.play()
                ZaddikaiAnim.blit(screen,((screen_width/2)-72,0))
            #Doing attack animation
            if direction == SPACE:
                if setTime + 1> time.time():
                    attackAnim.blit(screen,player_location)
                else:
                    direction = DOWN



            if moveUp or moveDown or moveLeft or moveRight or attack:
                #Draw the correct walking sprite from the animation object
                #Plays animations none stop until the key is let up on
                moveConductor.play()
                #Walking
                if direction == UP:
                    #Blits the animations (Facing backward) based on the image x and y (pixels)
                    animObjs['back_walk'].blit(screen, (x_anim, y_anim))
                elif direction == DOWN:
                    #Blits the animations (Facing forward) based on the image x and y (pixels)
                    animObjs['front_walk'].blit(screen, (x_anim, y_anim))
                elif direction == LEFT:
                    #Blits the animations (Facing left) based on the image x and y (pixels)
                    animObjs['left_walk'].blit(screen, (x_anim, y_anim))
                elif direction == RIGHT:
                    #Blits the animations (Facing right) based on the image x and y (pixels)
                    animObjs['right_walk'].blit(screen, (x_anim, y_anim))



                #Decrease along the y axis to move up
                if moveUp:
                    y_anim -= walkrate
                #Increase along the y axis to move down
                if moveDown:
                    y_anim += walkrate
                #Decrease along the y axis to move left
                if moveLeft:
                    x_anim -= walkrate
                #Increase along the y axis to move right
                if moveRight:
                    x_anim += walkrate

            else:
                #The player is standing still
                #Stops the player animations
                moveConductor.stop()
                #Blits the image of the player facing backwards
                if direction == UP:
                    screen.blit(back_standing, (x_anim, y_anim))
                #Blits the image of the player facing forward
                elif direction == DOWN:
                    screen.blit(front_standing, (x_anim, y_anim))
                #Blits the image of the player facing left
                elif direction == LEFT:
                    screen.blit(left_standing, (x_anim, y_anim))
                #Blits the image of the player facing right
                elif direction == RIGHT:
                    screen.blit(right_standing, (x_anim, y_anim))
                #Blits the attacking image
                elif direction == SPACE:
                    attackAnim.blit(screen,player.rect)


            for i in bad_block_list:

                if i.kind == "healthup" or i.kind == "invincible" or i.kind == "speed":
                    pass
                else:
                    if i.moveUp or i.moveDown or i.moveLeft or i.moveRight:
                        # Draw the correct walking sprite from the animation object
                        # Plays animations none stop until the key is let up on
                        i.moveConductor.play()
                        # walking

                        if i.moveUp == True and i.moveDown == True:
                            i.moveDown = False
                            i.moveUp = False

                        if i.kind == "training":
                            if i.direction == "north":
                                # Blits the animations (Facing backward) based on the image x and y (pixels
                                training_animObjs['back_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "south":
                                # Blits the animations (Facing forward) based on the image x and y (pixels)
                                training_animObjs['front_walk'].blit(screen, (i.rect.x, i.rect.y))
                        if i.kind == "training":
                            if i.direction == "west":
                                # Blits the animations (Facing left) based on the image x and y (pixels)
                                training_animObjs['left_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "east":
                                # Blits the animations (Facing right) based on the image x and y (pixels)
                                training_animObjs['right_walk'].blit(screen, (i.rect.x, i.rect.y))

                        if i.kind == "wraith":
                            if i.direction == "north":
                                # Blits the animations (Facing backward) based on the image x and y (pixels
                                wraith_animObjs ['back_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "south":
                                # Blits the animations (Facing forward) based on the image x and y (pixels)
                                wraith_animObjs ['front_walk'].blit(screen, (i.rect.x, i.rect.y))
                        if i.kind == "wraith":
                            if i.direction == "west":
                                # Blits the animations (Facing left) based on the image x and y (pixels)
                                wraith_animObjs ['left_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "east":
                                # Blits the animations (Facing right) based on the image x and y (pixels)
                                wraith_animObjs ['right_walk'].blit(screen, (i.rect.x, i.rect.y))

                        if i.kind == "mask":
                            if i.direction == "north":
                                # Blits the animations (Facing backward) based on the image x and y (pixels
                                mask_animObjs ['back_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "south":
                                # Blits the animations (Facing forward) based on the image x and y (pixels)
                                mask_animObjs ['front_walk'].blit(screen, (i.rect.x, i.rect.y))
                        if i.kind == "mask":
                            if i.direction == "west":
                                # Blits the animations (Facing left) based on the image x and y (pixels)
                                mask_animObjs ['left_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "east":
                                # Blits the animations (Facing right) based on the image x and y (pixels)
                                mask_animObjs ['right_walk'].blit(screen, (i.rect.x, i.rect.y))

                        if i.kind == "phantom":
                            if i.direction == "north":
                                # Blits the animations (Facing backward) based on the image x and y (pixels
                                phantom_animObjs ['back_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "south":
                                # Blits the animations (Facing forward) based on the image x and y (pixels)
                                phantom_animObjs ['front_walk'].blit(screen, (i.rect.x, i.rect.y))
                        if i.kind == "phantom":
                            if i.direction == "west":
                                # Blits the animations (Facing left) based on the image x and y (pixels)
                                phantom_animObjs ['left_walk'].blit(screen, (i.rect.x, i.rect.y))
                            elif i.direction == "east":
                                # Blits the animations (Facing right) based on the image x and y (pixels)
                                phantom_animObjs ['right_walk'].blit(screen, (i.rect.x, i.rect.y))


                
        #See if the player block has collided with anything.
        good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
        bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
        #Checks if any power ups exist
        if len(power_up_list) > 0:
            #Checks if the power up is health 
            if invincibleup == False and speedup == False:
                #Checks if the player has collided with it
                col = pygame.sprite.spritecollideany(player, power_up_list)
                if not col == None:
                    #Increases the players health
                    player_health += 5
                    #Clears the power_up_list
                    power_up_list = 0
                    power_up_list = pygame.sprite.Group()
            #Checks if the power up is invincibility 
            if healthup == False and speedup == False:
                #Checks if the player has collided with it
                col = pygame.sprite.spritecollideany(player, power_up_list)
                if not col == None:
                    #Saves the players health
                    saved_health = player_health
                    #Turns on the Invincibility
                    invincibleOn = True
                    #Clears the power_up_list
                    power_up_list = 0
                    power_up_list = pygame.sprite.Group()
            #Checks if the power up is speed 
            if invincibleup == False and healthup == False:
                #Checks if the player has collided with it
                col = pygame.sprite.spritecollideany(player, power_up_list)
                if not col == None:
                    #Sets the speed boost to true
                    speedBoost = True
                    #Clears the power_up_list
                    power_up_list = 0
                    power_up_list = pygame.sprite.Group()
        #Updating player position
        x_anim = player.rect.x
        y_anim = player.rect.y    
        #Check the list of collisions.
        for block in bad_blocks_hit_list:
            player_health -= 1

        
        #Update the screen with what we've drawn.
        pygame.display.flip()
     
        #Limit to 60 frames per second
        clock.tick(60)
    
#Close the window and quit.
#If you forget this line, the program will 'hang'
#on exit if running from IDLE.
pygame.quit()
