import pygame, sys, os, math, random, time, pickle, pyperclip
from pygame.locals import *
pygame.init()

##You can capture the contents of the Pygame.Surface by making a copy with screen.copy() then when you want to redraw you use screen.blit(copy, (0,0)). And then you draw on top of that.



##A python script is nothing more than a text file. So, you are able to open it as an external file and read & write on that. (Using __file__ variable you can get the exact name of your script):
##
##def updateCount():
##    fin = open(__file__, 'r')
##    code = fin.read()
##    fin.close()
##
##    second_line = code.split('\n')[1]
##    second_line_parts = second_line.split(' ')
##    second_line_parts[2] = str(int(second_line_parts[2])+1)
##
##    second_line = ' '.join(second_line_parts)
##    lines = code.split('\n')
##    lines[1] = second_line
##    code = '\n'.join(lines)
##
##    fout = open(__file__, 'w')
##    fout.write(code)
##    fout.close()


win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)#RESIZABLE / RESIZABLE
pygame.display.set_caption("Castlevania: Symphony of the Night 2")
iconTick = 0
gif = 0
b = random.randrange(0,15)
pygame.display.set_icon(pygame.image.load(f'DATA/GRAPHICS/ICON/0.png').convert_alpha())
icon = [pygame.image.load(f'DATA/GRAPHICS/ICON/{b}/{a}.png').convert_alpha() for a in range(3)]
pygame.display.set_icon(icon[gif//6])
fullscreen = False
gravity = True
falling = True
fallTick = 0
click = False
shooting = False
neg = -1
scroll = [0,0]
AlucardMenuOn = False
AlucardEquipMenuOn = False
AlucardInventoryOn = False
Touching_left_wall = False
Touching_right_wall = False
scrollingOn = False
ScrollingVerticalOn = False
clock = pygame.time.Clock()

run = True
main_menu = True
gameSpeed = 30

door_tick = 0
plat = False
Loading_Gallery = None

instructions = None
#===============================================
#===============================================
#=============== FUNCTIONS =====================
#===============================================
#===============================================
def paused():
    pygame.mixer.music.pause()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def Loading():
    b = random.randrange(0, 39)
    Loading_Gallery = pygame.image.load(f"DATA/GRAPHICS/LOADING/a ({b}).jpg").convert_alpha()
    win.blit(Loading_Gallery, (0,0))
    win.blit((font4.render(('Loading'), 1, (15,5,5))), (1105,605))
    win.blit((font4.render(('Loading'), 1, (30,10,10))), (1102,602))
    win.blit((font4.render(('Loading'), 1, (211,211,211))), (1100,600))
    pygame.display.flip()

def Loading_1():
    Loading()
    #DHURON
    DhuronWalkR = None
    DhuronWalkL = None
    DhuronAttackR = None
    DhuronAttackL = None
    #TIGER
    tigerIdleR = None
    tigerIdleL = None
    tigerAtkR = None
    tigerAtkL = None

def Loading_2():
    Loading()
    #DHURON
    DhuronWalkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/WALK-R/DH-L{i}.png').convert_alpha() for i in range(9)]
    DhuronWalkL = [pygame.transform.flip(a, True, False) for a in DhuronWalkR]
    DhuronAttackR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/ATK-R/DHATKR{i}.png').convert_alpha() for i in range(13)]
    DhuronAttackL = [pygame.transform.flip(a, True, False) for a in DhuronAttackR]
    #TIGER
    tigerIdleR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/IDLE-R/{i}.png').convert_alpha() for i in range(23)]
    tigerIdleL = [pygame.transform.flip(a, True, False) for a in tigerIdleR]
    tigerAtkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/ATK-R/{i}.png').convert_alpha() for i in range(25)]
    tigerAtkL = [pygame.transform.flip(a, True, False) for a in tigerAtkR]

def sprites(image_path, num_of_images, double_size = False):
    if double_size:
        image_list = [pygame.transform.scale2x(pygame.image.load(image_path + str(i) + '.png').convert_alpha()) for i in range(num_of_images)]
        return image_list
    else:    
        image_list = [pygame.image.load(image_path + str(i) + '.png').convert_alpha() for i in range(num_of_images)]
        return image_list

def flip_sprite(image_list):
    flipped_sprites = [pygame.transform.flip(a, True, False) for a in image_list]
    return flipped_sprites

##def bg_door(door, old_background, new_background, x, y, song):
##    if man.hitbox.colliderect(door.hitbox):
##        if old_background == True:
##            man.x = x
##            man.y = y
##            old_background = False
##            new_background = True
##            pygame.mixer.music.stop()
##            pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/' + (str(song)) + '.wav')
##            pygame.mixer.music.play(-1)

def Enemy_collision(enemy):
    for d in enemy:
        if d.visible == True and d.alive == True and d.tangible == True:
            if man.hitbox.colliderect(d.hitbox):
                    man.hit()
                    if man.x < d.x:
                        man.damageL = True
                    elif man.x > d.x:
                        man.damageR = True
    for d in enemy:
        if d.visible == True:
            if man.atkbox.colliderect(d.hitbox):
                if man.attacking == True and man.attackCount + 1 >= 3 and man.attackCount <= 4 or man.crouchATK == True and man.crouchATKcount + 1 >= 3 and man.crouchATKcount <= 4:
                          d.currentXposition = d.x
                          d.hit()

##def step_on_platform(platform_list):
##    for a in platform_list:
##        if neg == -1 and man.feetBox.colliderect(a.hitbox):
##            if a.visible:
##                if not (man.bat):
##                    man.y = a.y - 95
##                    man.jumpCount = 10
##                plat = True
##                falling = False
##                man.fallCount = 0
##                man.fallCountB = 0
##                man.jumpAtkCount = 0
##        else:
##            if not (man.isJump):
##                man.jumpCount = 0

##def Wall_collision(walls, man_collider):
##    Touching_left_wall = False
##    Touching_right_wall = False
##    for a in walls:
##        if a.visible == True:
##            if man_collider.colliderect(a.hitbox):
##                walls = True

def Fade(w,h): # It kinda works... its a bit weird. it fades some part of the screen... but it pauses the game while it happens.
    fade = pygame.Surface((w,h))
    fade.fill((0,0,0))
    for a in range(0,900):
        fade.set_alpha(a //3)
        #redrawGameWindow()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

#======================================================
#======================================================
#=============== MENU / STATUS ========================
#======================================================
#======================================================
AlucardLevel = 1
AlucardExp = 0
AlucardNextLevel = 137
AlucardGold = 0

AlucardKill = 0
AlucardRooms = 0

Alucardhealth = 108
AlucardMaxHealth = ((AlucardLevel * 17) + 91 ) 
AlucardMP = 50
AlucardMaxMP = 50
AlucardHearts = 0
AlucardMaxHearts = 30

AlucardATK = 20
AlucardATK2 = 20
AlucardDEF = 10

AlucardSTR = 10
AlucardLCK = 10
AlucardCON = 10
AlucardINT = 10

#======================================================
#======================================================
#=============== MENU / ITEMS =========================
#======================================================
#======================================================
equiping = 0 # main menu hovering bar transforming into selecting bar

positionTick = False # general menu ticks 
positionTicks = 0 # general menu ticks

hoverY = 363 # main menu selection bar 
position1 = True # main menu positions
position2 = False # main menu positions
position3 = False # main menu positions
position4 = False # main menu positions
position5 = False # main menu positions
mainMenuPositionList = [position1, position2, position3, position4, position5] # Main menu positions

equipHoverY = 52 # Equip menu selection bar
equipPosition1 = True # Equip menu positions
equipPosition2 = False # Equip menu positions
equipPosition3 = False # Equip menu positions
equipPosition4 = False # Equip menu positions
equipPosition5 = False # Equip menu positions
equipPosition6 = False # Equip menu positions
equipPosition7 = False # Equip menu positions
equipPositionList = [equipPosition1, equipPosition2, equipPosition3, equipPosition4, equipPosition5, equipPosition6, equipPosition7] # Equip menu positions

#===============================================
#===============================================
#================ ITEMS ========================
#===============================================
#===============================================

main_Menu_Display = None

items = [pygame.image.load(f'DATA/GRAPHICS/ITEMS/item ({i}).png').convert_alpha() for i in range(253)]
menuArrowUp = [pygame.image.load(f'DATA/GRAPHICS/MENUS/ARROW/{i}.png').convert_alpha() for i in range(6)]
menuArrowDown = [pygame.transform.flip(a, False, True) for a in menuArrowUp]
itemsNames = ['Empty hand', 'Map', 'Magic book', 'Apple', 'Banana', 'Pineapple', 'Grapes', 'Strawberry', 'Orange', 'Salt', 'Resist lightning', 'Resist wind', 'Resist Stoning', 'Resist Fire', 'Resist dark', '- - - - - - - - - -', '- - - - - - - - - -', '- - - - - - - - - -']
itemsDescription = ['No weapon (bare hands)', 'Area map', 'contains spells', 'One a day keeps the doctor away' , '99% human DNA', 'Takes 23 years to mature', 'Seedless grapes', 'Summer berry', 'High dose of vitamin C', 'Adds flavor', 'Adds resistance against lightning attacks', 'Adds resistance against poison attacks', 'Adds resistance against stoning attacks', 'Adds resistance against fire attacks', 'Adds resistance against dark attacks', 'Unequip', 'Unequip', 'Unequip']
font1 = pygame.font.SysFont('UnifrakturCook', 30)
font2 = pygame.font.SysFont('UnifrakturCook', 50)
font3 = pygame.font.SysFont('MedievalSharp', 30)
font4 = pygame.font.SysFont('UnifrakturCook', 50)
SelectedHand = 1
AlucardInventory = []
InventoryIDs = []
inventoryYaxe = 405
##text = font1.render('-5', 1, (255,0,0))
##win.blit(text, ((int((self.x + 10)+ self.width//2)), (int(self.y - self.height//2))))
inventoryHoverX = 60 # Equip menu selection bar
inventoryHoverY = 405 # Equip menu selection bar
invPos1 = True # inventory positions
invPos2 = False # inventory positions
invPos3 = False # inventory positions
invPos4 = False # inventory positions
invPos5 = False # inventory positions
invPos6 = False # inventory positions
invPos7 = False # inventory positions
invPos8 = False # inventory positions
invPos9 = False # inventory positions
invPos10 = False # inventory positions
invPos11 = False # inventory positions
invPos12 = False # inventory positions
invPos13 = False # inventory positions
invPos14 = False # inventory positions
invPos15 = False # inventory positions
invPos16 = False # inventory positions

## I do see a lot of redundant variables that would be better used as lists, or as pointers
## why not have invPos=1
##and increment/decrement as needed
##Also, for readability you'll want to have your code split up into multiple modules based on the tasks
##or else it'll become difficult to find some of your classes and methods

#==================================================================================================
#==================================================================================================
#=============== IMAGES ===========================================================================
#==================================================================================================
#==================================================================================================
KONAM = None
KONAMI = None
konami = True
konami_init = True

#===============================================
#===============================================
#=============== SUB MENU ======================
#===============================================
#===============================================
SUBMENU = sprites(f'DATA/GRAPHICS/MENUS/SUB MENU/0/',4 )
#SUBMENU = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/0/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU1 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/1/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU2 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/2/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU3 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/3/{i}.png').convert_alpha() for i in range(4)]
#===============================================
#===============================================
#============= BACKGROUNDS =====================
#===============================================
#===============================================
#extraParallax = False
##class Backgrounds_Class():
##    def __init__(self):
##        self.background1 = True
##        self.background1B = False
##bg = Backgrounds_Class()

background1 = True
background1B = False
background1C = False
background1D = False
background2 = False
background3 = False
background4 = False
background5 = False
background6 = False
background7 = False
background8 = False
background9 = False
background10 = False
background11 = False
background12 = False
background13 = False
background14 = False
background15 = False
background16 = False
background17 = False
background18 = False
background19 = False
background20 = False
background21 = False
background22 = False
background23 = False
background24 = False
background25 = False
background26 = False
background27 = False
background28 = False
background29 = False
background30 = False
background30b = False
background31 = False
background32 = False
backgroundSave = False

bgList = [background1,background1B, background1C,background2,background3,background4,background5,background6,background7,background8,background9,background10,
          background11,background12,background13,background14,background15,background16,background17,background18,background19,background20,
          background21,background22,background23,background24,background25,background26,background27,background28,background29,background30,
          background30b,background31,background32,backgroundSave]

#===============================================
#===============================================
#============= BACKGROUNDS =====================
#===============================================
#===============================================
bg1 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "0.png")).convert_alpha()
bg1B = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "1.png")).convert_alpha()
bg1C = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "2.png")).convert_alpha()
bg1D = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "2b.png")).convert_alpha()
bg2 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "3.png")).convert_alpha()
bg3 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "4.png")).convert_alpha()

bg4 = None
bg5 = None
bg6 = None
bg7 = None
bg8 = None

bg9 = None
bg10 = None
bg11 = None
bg12 = None
bg13 = None

bg14 = None
bg15 = None
bg16 = None
bg17 = None
bg18 = None

bg19 = None
bg20 = None
bg21 = None
bg22 = None
bg23 = None

bg24 = None
bg25 = None
bg26 = None
bg27 = None
bg28 = None

bg29 = None
bg30 = None
bg30b = None
bg31 = None
bg32 = None

bgSave = None

#===============================================
#===============================================
#============== PARALLAX =======================
#===============================================
#===============================================
X1PR1 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR1.png').convert()
X1PR2 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR2.png').convert_alpha()
X1PR3 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR3.png').convert_alpha()
X2PR1 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/INSIDE/X2PR1.jpg').convert()
forest = None
Bg3Pillars = None

#======================================================
#======================================================
#=============== SPEECHES IMAGES ======================
#======================================================
#======================================================
AlucardSpeech01 = False
AlucardSpeech01Count = 0
AlucardSP1 = None

if AlucardSpeech01Count + 1 >= 105:
    AlucardSpeech01Count = 0
    Alucardspeech01 = False

if AlucardSpeech01 == True:
    win.blit(AlucardSP1[AlucardSpeech01Count//3], (int(50), int(50)))
    AlucardSpeech01Count += 1

#===============================================
#===============================================
#================ DOORS ========================
#=============================================== 
#===============================================
areaDoorClosed = None
areaDoorOpen = None
sealedDoorClosed = None
sealedDoorOpen = None
olroxDoor = None

#===============================================
#===============================================
#=============== ALUCARD =======================
#===============================================
#===============================================
##test = walkingRight.copy() # testing the transparency stuff, it works , put under the animations loading images.
##for a in walkRight: #
##    a.fill((0, 0, 255, 100), special_flags=pygame.BLEND_RGBA_MULT) #

# claudeb already said it, make a list of the character's previous positions, update them however often you want to, and draw at those positions
# I would first blit something that makes color to go bluish and adds alpha.
# then draw next frame on it and finally blit animation surface on top of background.

walkRight = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/WALKING/a ({i}).png').convert_alpha() for i in range(31)]
walkLeft = [pygame.transform.flip(a, True, False) for a in walkRight]
ALKattack = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/ATTACK/H{i}.png').convert_alpha() for i in range(17)]
ALKattackLeft = [pygame.transform.flip(a, True, False) for a in ALKattack]
crouch = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/CROUCH/F{i}.png').convert_alpha() for i in range(17)]
crouch2 = [pygame.transform.flip(a, True, False) for a in crouch]
char = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/STANDING/{i}.png').convert_alpha() for i in range(14)]
char2 = [pygame.transform.flip(a, True, False) for a in char]
jumping = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMP/C{i}.png').convert_alpha() for i in range(15)]
jump = jumping[0:12]
jump2 = [pygame.transform.flip(a, True, False) for a in jump]
jumpSlopeR = (jump[0:8] + jump[12:14]) # NOT ASSIGNED
jumpSlopeL = [pygame.transform.flip(a, True, False) for a in jumpSlopeR] # NOT ASSIGNED
jumpRight = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMPRIGHT/G{i}.png').convert_alpha() for i in range(22)]
jumpLeft = [pygame.transform.flip(a, True, False) for a in jumpRight]
jumpRightKick = jumpRight[14]
jumpLeftKick = pygame.transform.flip(jumpRightKick, True, False)
fallRight = jumpRight[7:13]
fallLeft = [pygame.transform.flip(a, True, False) for a in fallRight]
AlucardShieldR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/ALUCARD SHIELD/S{i}.png').convert_alpha() for i in range(4)]
AlucardShieldL = [pygame.transform.flip(a, True, False) for a in AlucardShieldR]
AlucardBatR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/BAT/{i}.png').convert_alpha() for i in range(8)]
AlucardBatL = [pygame.transform.flip(a, True, False) for a in AlucardBatR]
idle1R = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/IDLE/{i}.png').convert_alpha() for i in range(2)]
idle1L = [pygame.transform.flip(a, True, False) for a in idle1R]
SquatAtkR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/SQUAT ATK/{i}.png').convert_alpha() for i in range(17)]
SquatAtkL = [pygame.transform.flip(a, True, False) for a in SquatAtkR]
JumpATKR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMP ATK/JumpATK{i}.png').convert_alpha() for i in range(4)]
JumpATKL = [pygame.transform.flip(a, True, False) for a in JumpATKR]

##################################### not assigned yet ##################################################################
idle2R = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/IDLE 2/{i}.png').convert_alpha() for i in range(2)]
idle2L = [pygame.transform.flip(a, True, False) for a in idle2R]
turnR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/TURNING AROUND/{i}.png').convert_alpha() for i in range(10)]
turnL = [pygame.transform.flip(a, True, False) for a in turnR]
stop = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/STOP/{i}.png').convert_alpha() for i in range(18)]
stop1R = stop[0:12]
stop1L = [pygame.transform.flip(a, True, False) for a in stop1R]
stop2R = (stop[0:7] + stop[13:18])
stop2L = [pygame.transform.flip(a, True, False) for a in stop2R]
AlucardSwordR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/ALUCARD SWORD/{i}.png').convert_alpha() for i in range(9)]
AlucardSwordL = [pygame.transform.flip(a, True, False) for a in AlucardSwordR]
damage = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/DAMAGE/{i}.png').convert_alpha() for i in range(4)]
damageLeft = [pygame.transform.flip(a, True, False) for a in damage]
statue = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/STATUE/{i}.png').convert_alpha() for i in range(6)]
statueLeft = [pygame.transform.flip(a, True, False) for a in statue]
doubleJumpR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/DOUBLE JUMP/{i}.png').convert_alpha() for i in range(4)]
doubleJumpL = [pygame.transform.flip(a, True, False) for a in doubleJumpR]
flyingKickR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/FLYING KICK/{i}.png').convert_alpha() for i in range(3)]
flyingKickL = [pygame.transform.flip(a, True, False) for a in flyingKickR]
hellfireR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/HELLFIRE/HELL{i}.png').convert_alpha() for i in range(11)]
hellfireL = [pygame.transform.flip(a, True, False) for a in hellfireR]
fireR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/HELLFIRE/FIRE{i}.png').convert_alpha() for i in range(5)]
fireL = [pygame.transform.flip(a, True, False) for a in fireR]
airDamageR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/AIR DAMAGE/{i}.png').convert_alpha() for i in range(4)]
airDamageL = [pygame.transform.flip(a, True, False) for a in airDamageR]
jumpAtkTransR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMP ATK TRANS/{i}.png').convert_alpha() for i in range(4)]
jumpAtkTransL = [pygame.transform.flip(a, True, False) for a in jumpAtkTransR]
jumpLowAtkR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMP LOW ATK/{i}.png').convert_alpha() for i in range(4)]
jumpLowAtkL = [pygame.transform.flip(a, True, False) for a in jumpLowAtkR]
squatAtkLowR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/SQUAT ATK DOWN/SquatAtkLowR{i}.png').convert_alpha() for i in range(15)]
SquatAtkLowL = [pygame.transform.flip(a, True, False) for a in squatAtkLowR]
deadR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/DEAD/DEAD{i}.png').convert_alpha() for i in range(5)]
deadL = [pygame.transform.flip(a, True, False) for a in deadR]

# sitting and 2nd jump slope missing. idl2 not working
#=======================================================
#=======================================================
#================= MENUS / MISC ========================
#=======================================================
#=======================================================
blank = [pygame.image.load(f'DATA/GRAPHICS/MENUS/BLANK/{i}.png').convert_alpha() for i in range(2)]
blankItem = blank.copy()
for a in blankItem:
    a.fill((0, 0, 255, 0), special_flags=pygame.BLEND_RGBA_MULT)
#MENUS ----------------------------------------Main Menu
AlucardMenuSelection = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','Selection.png')).convert_alpha()
AlucardMenu = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','AlucardMenu.png')).convert()
AlucardEquipMenu = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','Equip Menu.png')).convert_alpha()
AlucardItems = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','inventory.png')).convert()
#MENUS ----------------------------------------Main Menu
equipHover = [pygame.image.load(f'DATA/GRAPHICS/MENUS/BAR1/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
equipSelect = [pygame.image.load(f'DATA/GRAPHICS/MENUS/BAR1SELECT/{i}.png').convert_alpha() for i in range(33)] #hovering over equip on menu
bar = [pygame.image.load(f'DATA/GRAPHICS/MENUS/BAR1/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
equipHover = bar
#MENUS ----------------------------------------Equip Menu
inventHover = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBAR/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
inventSelect = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBARSELECT/{i}.png').convert_alpha() for i in range(33)] #hovering over equip on menu
barEquip = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBAR/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
inventHover = barEquip
##for a in inventHover: #
##    a.fill((255, 255, 255, 180), special_flags=pygame.BLEND_RGBA_MULT) #
#MENUS ----------------------------------------Inventory Menu
invHover = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBAR/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
invSelect = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBARSELECT/{i}.png').convert_alpha() for i in range(33)] #hovering over equip on menu
barInv = [pygame.image.load(f'DATA/GRAPHICS/MENUS/EQUIPBAR/{i}.png').convert_alpha() for i in range(21)] #hovering over equip on menu
invHover = barInv
# HUD ----------------------------------------
AlucardHealthHud = pygame.image.load(f'DATA/GRAPHICS/HUD/01HUD.png').convert_alpha()
AlucardLowHealthHud = pygame.image.load(f'DATA/GRAPHICS/HUD/HUD1.png').convert_alpha()
MpFull = [pygame.image.load(f'DATA/GRAPHICS/HUD/tile0{i}.png').convert_alpha() for i in range(30)]

#MISC ----------------------------------------
candle1 = [pygame.image.load(f'DATA/GRAPHICS/MISC/CANDLES/0/I{i}.png').convert_alpha() for i in range(5)]
hearts = pygame.image.load(os.path.join('DATA/GRAPHICS/HEART', "heart0.png")).convert_alpha()
heartsFading = [pygame.image.load(f'DATA/GRAPHICS/HEART/{i}.png').convert_alpha() for i in range(5)]
explosion = [pygame.image.load(f'DATA/GRAPHICS/EXPLOSION/{i}.png').convert_alpha() for i in range(13)]

#=======================================================
#=======================================================
#===================== NUMBERS =========================
#=======================================================
#=======================================================
#HealthNum = {name: pygame.image.load(f"DATA/GRAPHICS/NUMBERS/HealthNum/{i}.png") for i, name in enumerate("-0123456789")} #said to work instead, but its not.
num = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/HealthNum/{i}.png').convert_alpha() for i in range(10)] # Health on HUD numbers
HealthNum = {"-": num[0], "0": num[0], "1": num[1], "2": num[2], "3": num[3], "4": num[4], "5": num[5], "6": num[6], "7": num[7], "8": num[8], "9": num[9]}
Wnum = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumWhite/{i}.png').convert_alpha() for i in range(10)] # Hearts on HUD numbers
Whitenum = {"-": Wnum[0], "0": Wnum[0], "1": Wnum[1], "2": Wnum[2], "3": Wnum[3], "4": Wnum[4], "5": Wnum[5], "6": Wnum[6], "7": Wnum[7], "8": Wnum[8], "9": Wnum[9]}
Gnum = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumGreen/{i}.png').convert_alpha() for i in range(10)] # Hearts on HUD numbers
GreenNum = {"-": Gnum[0], "0": Gnum[0], "1": Gnum[1], "2": Gnum[2], "3": Gnum[3], "4": Gnum[4], "5": Gnum[5], "6": Gnum[6], "7": Gnum[7], "8": Gnum[8], "9": Gnum[9]}                    
NumDam = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumDamage/{i}.png').convert_alpha() for i in range(10)] # Enemy Damage
NumDamage = {"-": NumDam[0], "0": NumDam[0], "1": NumDam[1], "2": NumDam[2], "3": NumDam[3], "4": NumDam[4], "5": NumDam[5], "6": NumDam[6], "7": NumDam[7], "8": NumDam[8], "9": NumDam[9]}
#-----------------
# Alucard Menu On:
NumLvl = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumLvl/{i}.png').convert_alpha() for i in range(10)]
NumLevel = {"-": NumLvl[0], "0": NumLvl[0], "1": NumLvl[1], "2": NumLvl[2], "3": NumLvl[3], "4": NumLvl[4], "5": NumLvl[5], "6": NumLvl[6], "7": NumLvl[7], "8": NumLvl[8], "9": NumLvl[9]}
NumStats = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumStats/{i}.png').convert_alpha() for i in range(10)]
NumStatus = {"-": NumStats[0], "0": NumStats[0], "1": NumStats[1], "2": NumStats[2], "3": NumStats[3], "4": NumStats[4], "5": NumStats[5], "6": NumStats[6], "7": NumStats[7], "8": NumStats[8], "9": NumStats[9]}
NumAtk = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumAtk/{i}.png').convert_alpha() for i in range(10)]
NumAttack = {"-": NumAtk[0], "0": NumAtk[0], "1": NumAtk[1], "2": NumAtk[2], "3": NumAtk[3], "4": NumAtk[4], "5": NumAtk[5], "6": NumAtk[6], "7": NumAtk[7], "8": NumAtk[8], "9": NumAtk[9]}
NumHearts = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumHearts/{i}.png').convert_alpha() for i in range(10)]
NumHeart = {"-": NumHearts[0], "0": NumHearts[0], "1": NumHearts[1], "2": NumHearts[2], "3": NumHearts[3], "4": NumHearts[4], "5": NumHearts[5], "6": NumHearts[6], "7": NumHearts[7], "8": NumHearts[8], "9": NumHearts[9]}
NumHp = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumHp/{i}.png').convert_alpha() for i in range(10)]
NumHealthPoints = {"-": NumHp[0], "0": NumHp[0], "1": NumHp[1], "2": NumHp[2], "3": NumHp[3], "4": NumHp[4], "5": NumHp[5], "6": NumHp[6], "7": NumHp[7], "8": NumHp[8], "9": NumHp[9]}
NumMp = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumMp/{i}.png').convert_alpha() for i in range(10)]
NumMagicPoints = {"-": NumMp[0], "0": NumMp[0], "1": NumMp[1], "2": NumMp[2], "3": NumMp[3], "4": NumMp[4], "5": NumMp[5], "6": NumMp[6], "7": NumMp[7], "8": NumMp[8], "9": NumMp[9]}
NumRooms = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumRooms/{i}.png').convert_alpha() for i in range(10)]
NumRoom = {"-": NumRooms[0], "0": NumRooms[0], "1": NumRooms[1], "2": NumRooms[2], "3": NumRooms[3], "4": NumRooms[4], "5": NumRooms[5], "6": NumRooms[6], "7": NumRooms[7], "8": NumRooms[8], "9": NumRooms[9]}
NumTimer = [pygame.image.load(f'DATA/GRAPHICS/NUMBERS/NumTimer/{i}.png').convert_alpha() for i in range(10)]
NumTime = {"-": NumTimer[0], "0": NumTimer[0], "1": NumTimer[1], "2": NumTimer[2], "3": NumTimer[3], "4": NumTimer[4], "5": NumTimer[5], "6": NumTimer[6], "7": NumTimer[7], "8": NumTimer[8], "9": NumTimer[9]}

#===============================================
#===============================================
#=============== ENEMIES =======================
#===============================================
#===============================================
#DHURON
DhuronWalkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/WALK-R/DH-L{i}.png').convert_alpha() for i in range(9)]
DhuronWalkL = [pygame.transform.flip(a, True, False) for a in DhuronWalkR]
DhuronAttackR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/ATK-R/DHATKR{i}.png').convert_alpha() for i in range(13)]
DhuronAttackL = [pygame.transform.flip(a, True, False) for a in DhuronAttackR]

#SKELETON
skeleton_left = sprites(f'DATA/GRAPHICS/ENEMIES/SKELETON/', 8)
skeleton_right = flip_sprite(skeleton_left) #flipped

#FLYING SKULL HEAD
flying_skull_head_right = sprites(f'DATA/GRAPHICS/ENEMIES/FLYING SKULL HEAD/', 4, True)
flying_skull_head_left = flip_sprite(flying_skull_head_right) #flipped

#SKULL HEAD
skull_head_right = sprites(f'DATA/GRAPHICS/ENEMIES/SKULL HEAD/', 4)
skull_head_left = flip_sprite(skull_head_right) #flipped

#TIGER
tigerIdleR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/IDLE-R/{i}.png').convert_alpha() for i in range(23)]
tigerIdleL = [pygame.transform.flip(a, True, False) for a in tigerIdleR]
tigerAtkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/ATK-R/{i}.png').convert_alpha() for i in range(25)]
tigerAtkL = [pygame.transform.flip(a, True, False) for a in tigerAtkR]
    
#===============================================
#===============================================
#================= NPCS ========================
#===============================================
#===============================================
NPCS = None
#=====================================================================================================
#=====================================================================================================
#=============== SOUNDS ============================================================================== ##### NON ESSENTIAL LOADING ########
#=====================================================================================================
#=====================================================================================================
SOUNDS_A = [pygame.mixer.Sound(f'DATA/SOUNDS/SFX/{i}.wav')for i in range(31)]
SOUNDS_TICK = [pygame.mixer.Sound(f'DATA/SOUNDS/SFX/TICKS/a ({i}).wav')for i in range(14)]
intro = pygame.mixer.Sound(f'DATA/SOUNDS/SFX/Konami Intro.wav')
##ALKJUMPFALL = pygame.mixer.Sound('????.wav') # ADD
##SOUNDsv_hrtbt = pygame.mixer.Sound('sv_hrtbt.wav') #
##SOUNDfam_sword1 = pygame.mixer.Sound('swd_dark.wav')#
##SOUNDdem_die = pygame.mixer.Sound('dem_die.wav') #
##SOUNDbreakpot = pygame.mixer.Sound('breakpot.wav') # break glass sound
##SOUNDthunder = pygame.mixer.Sound('thunder.wav')#

#======================================================
#======================================================
#=============== SPEECHES SOUNDS ======================
#======================================================
#======================================================
AlucardSpeech01SOUND = pygame.mixer.Sound(os.path.join('DATA/SOUNDS/SPEECHES', 'Alucard - He is too weak.wav'))

#=====================================================================================================
#=====================================================================================================
#===================================== CLASSES =======================================================
#=====================================================================================================
#=====================================================================================================
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============= KONAMI LOGO =====================
class Konami_Logo_Class(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display = False
        self.displayCount = 0

    def draw(self,win): # animations per frame:
        if self.displayCount == 1:
            intro.play()
        if self.displayCount + 1 >= 50*5:
            global konami
            konami = False
        win.blit(KONAMI[self.displayCount//5], (int(0), int(0)))
        self.displayCount += 1
    
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============= MAIN MENU =======================
class Main_Menu_Class(object):
    def __init__(self, x, y, width, height, x2, y2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x2
        self.y2 = y2
        self.display = False
        self.displayCount = 0
        self.names = ['New Game', 'Continue', 'Quit']
        self.ColorsA = (211,211,211)
        self.ColorsB = (211,211,211)
        self.ColorsC = (211,211,211)
        self.newGame = font4.render(str(self.names[0]), 1, (self.ColorsA))
        self.continuar = font4.render(str(self.names[1]), 1, (self.ColorsB))
        self.quit = font4.render(str(self.names[2]), 1, (self.ColorsC))
        self.newGameShadow = font4.render(str(self.names[0]), 1, (15,15,15))
        self.continuarShadow = font4.render(str(self.names[1]), 1, (15,15,15))
        self.quitShadow = font4.render(str(self.names[2]), 1, (15,15,15))
        self.hitbox = pygame.Rect(int(self.x2) , int(self.y2), 150, 20)
        self.newGameHitbox = pygame.Rect(135 , int(300), 50, 20)
        self.continuarHitbox = pygame.Rect(160 , int(350), 50, 20)
        self.quitHitbox = pygame.Rect(190 , int(400), 50, 20)

    def draw(self,win): # animations per frame:
        if self.displayCount + 1 >= 27*3:
            self.displayCount = 0
        win.blit(main_Menu_Display[self.displayCount//3], (int(-10), int(-10)))
        self.displayCount += 1
        self.hitbox = pygame.Rect(int(self.x2) , int(self.y2), 150, 20)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        pygame.draw.rect(win, (0,255,0), self.newGameHitbox,2)
        pygame.draw.rect(win, (0,255,0), self.continuarHitbox,2)
        pygame.draw.rect(win, (0,255,0), self.quitHitbox,2)
        self.newGame = font4.render(str(self.names[0]), 1, (self.ColorsA))
        self.continuar = font4.render(str(self.names[1]), 1, (self.ColorsB))
        self.quit = font4.render(str(self.names[2]), 1, (self.ColorsC))
        
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============= PARALLAX's ======================
class parallax(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Forest = False
        self.ForestCount = 0
        self.Bg3Pillars = False
        self.Bg3PillarsCount = 0
        self.MpFullDisplay = True
        self.MpFullDisplayCount = 0
        self.equipHoverDisplay = False
        self.equipHoverDisplayCount = 0
        self.equipHoverbox = pygame.Rect(525 , int(self.y), 50, 20)
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 29, 52)
        self.inventHoverDisplay = False
        self.inventHoverDisplayCount = 0
    
    def draw(self,win): # animations per frame:
        if self.ForestCount + 1 >= 24:
            self.ForestCount = 0

        if self.MpFullDisplayCount + 1 >= 90:
            self.MpFullDisplayCount = 0

        if self.Bg3PillarsCount + 1 >= 18:
            self.Bg3PillarsCount = 0

##        if equipHover == bar:
##            self.equipHoverDisplayCount = 0

        if self.equipHoverDisplayCount + 1 >= 63:
            self.equipHoverDisplayCount = 0

        if self.inventHoverDisplayCount + 1 >= 63:
            self.inventHoverDisplayCount = 0

                        # Animation Montion:
            
        if self.Forest == True:
            win.blit(forest[self.ForestCount//3], (int(0), int(0)))
            self.animationCount += 1
            
        if self.Bg3Pillars == True:
            win.blit(Bg3Pillars[self.Bg3PillarsCount//3], (int(0), int(0)))
            self.Bg3PillarsCount += 1

        if self.MpFullDisplay == True:
            win.blit(MpFull[self.MpFullDisplayCount//3], (int(122), int(18)))
            self.MpFullDisplayCount += 1

        if self.equipHoverDisplay == True:
            win.blit(equipHover[self.equipHoverDisplayCount//3], (int(593), int(hoverY)))
            self.equipHoverDisplayCount += 1

        if self.inventHoverDisplay == True:
            win.blit(inventHover[self.inventHoverDisplayCount//3], (int(525), int(equipHoverY)))
            self.inventHoverDisplayCount += 1
            self.equipHoverbox = pygame.Rect(525, int(equipHoverY), 50, 20)
            pygame.draw.rect(win, (0,0,255), self.equipHoverbox,2)
            
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============= INV HOVER =======================
class InventoryHoverClass(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Forest = False
        self.inv = False
        self.invC = 0
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 1, 1)
        self.arrowUp = False
        self.arrowDown = False
        self.arrowC = 0

    def draw(self,win):
        if self.invC + 1 >= 63:
            self.invC = 0

        if self.arrowC + 1 >= 6:
            self.arrowC = 0
            self.arrowUp = False
            self.arrowDown = False

        win.blit(menuArrowUp[0], (20, 390))
        win.blit(menuArrowDown[0], (20, 540))
            
        if self.arrowUp == True:
            win.blit(menuArrowUp[self.arrowC], (20, 390))
            self.arrowC += 1

        if self.arrowDown == True:
            win.blit(menuArrowDown[self.arrowC], (20, 540))
            self.arrowC += 1

        if self.inv == True:
            self.hitbox = pygame.Rect(int(inventoryHoverX), int(inventoryHoverY), 50, 20)
            win.blit(invHover[self.invC//3], (int(inventoryHoverX), int(inventoryHoverY)))
            self.invC += 1
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============== PLAYER =========================
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.shield = False
        self.shieldCount = 0
        self.bat = False
        self.batCount = 0
        self.idle1 = False
        self.idle1Count = 0
        self.jumpAtk = False
        self.jumpAtkCount = 0
        self.crouchATK = False
        self.crouchATKcount = 0
        self.walkCount = 0
        self.idleCount = 0
        self.jumpingUpCount = 0
        self.attackCount = 0
        self.attacking = False
        #self.idle = False
        self.crouching = False
        self.crouchCount = 0
        self.midJump = False
        self.jumpCount = 10
        self.standing = True
        self.fallCount = 0
        self.fallCountB = 0
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 29, 52)
        self.atkbox = pygame.Rect(int(self.x), int(self.y), 60, 10)
        self.feetBox = pygame.Rect(int(self.x), int(self.y + 85), 30, 13)
        self.turnRight = False
        self.turnLeft = False
        self.turnCount = 0
        self.backDash = False
        self.backDashCount = 0
        self.rightcollider = pygame.Rect(int(self.x + int(self.width) - 30), int(self.y), 30, int(self.height))
        self.leftcollider = pygame.Rect(int(self.x - 15), int(self.y), 30, int(self.height))
        # MAKE STATUS HERE RATHER THAN USING GLOBAL...
        self.atk = 10
        self.damageR = False
        self.damageL = False
        self.damageCount = 0

                        # animations frames:JumpATKR

    def draw(self,win):
        self.feetBox = pygame.Rect(int(self.x)+3, int(self.y + 85), 30, 13)
        self.rightcollider = pygame.Rect(int(self.x + int(self.width) - 35), int(self.y), 30, int(self.height))
        self.leftcollider = pygame.Rect(int(self.x - 8), int(self.y), 30, int(self.height))
        pygame.draw.rect(win, (0,255,0), self.feetBox,2)
        pygame.draw.rect(win, (0,255,155), self.rightcollider,2)
        pygame.draw.rect(win, (0,255,155), self.leftcollider,2)
        
        if self.walkCount + 1 >= 2:
            self.idleCount = 0
        if self.walkCount + 1 >= 31:
            self.walkCount = 16

        if self.standing == True:
            if self.idleCount + 1 >= 42:
                self.idleCount = 39
        else:
            self.idleCount = 0

##        if self.turnRight == True:
##            if self.turnCount + 1 >= 18:
##                self.turnCount = 0
##                self.turnRight = False
##                self.right = True
##
##        elif self.turnLeft == True:
##            if self.turnCount + 1 >= 18:
##                self.turnCount = 0
##                self.turnLeft = False
##                self.left = True
##        else:
##            self.turnCount = 0
            
        if self.shield == True:
            self.idleCount = 0
            if self.shieldCount + 1 >= 3:
                self.shieldCount = 1

        if self.idle1 == True:
            self.idleCount = 0
            if self.idle1Count + 1 >= 2:
                self.idle1Count = 1
                
        if self.bat == True:
            self.idleCount = 0
            if self.batCount + 1 >= 24:
                self.batCount = 0
                
        if self.fallCount + 1 >= 12:
            self.idleCount = 0
            self.fallCount = 11

        if self.fallCountB + 1 >= 12:
            self.idleCountB = 0
            self.fallCountB = 11
                
        if self.isJump == True:
            self.idleCount = 0
            if self.jumpingUpCount + 1 >= 24:
                self.jumpingUpCount = 0
                self.idleCount = 0

            if self.jumpAtkCount + 1 >= 4*2:
                self.jumpAtkCount = 0
                self.idleCount = 0
                self.jumpAtk = False
        else:
            self.jumpingUpCount = 0
            self.jumpAtkCount = 0
            
            
        if self.crouching == True:
            self.idleCount = 0
            if self.crouchCount + 1 >= 14:
                self.crouchCount = 13
        else:
            self.crouching = False

        if self.crouchATK == True:
            self.crouching = True
            if self.crouchATKcount + 1 >= 3 and self.right:
                self.atkbox = pygame.Rect(int(self.x + 30), int(self.y + 45), 120, 20)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            elif self.crouchATKcount + 1 >= 3 and self.left:
                self.atkbox = pygame.Rect(int(self.x - 115), int(self.y + 45), 120, 20)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.crouchATKcount >= 4:
                self.atkbox = pygame.Rect(int(-100), int(-30), -100, -100)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.crouchATKcount + 1 >= 17:
                self.atkbox = pygame.Rect(int(-100), int(-30), -100, -100)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
                self.crouchATKcount = 0
                self.crouchATKcount = False
                self.crouchATK = False
                self.idleCount = 0

        if self.attacking == True:
            if self.attackCount + 1 >= 3 and self.right:
                self.atkbox = pygame.Rect(int(self.x + 30), int(self.y + 10), 120, 20)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            elif self.attackCount + 1 >= 3 and self.left:
                self.atkbox = pygame.Rect(int(self.x - 115), int(self.y + 10), 120, 20)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.attackCount >= 4:
                self.atkbox = pygame.Rect(int(-100), int(-100), -100, -100)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.attackCount + 1 >= 17:
                self.atkbox = pygame.Rect(int(-100), int(-100), -100, -100)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
                self.attackCount = 0
                self.attacking = False
                self.idleCount = 0
                
                
                        # animations assingment to actions and speed:

        if self.damageR:
            if self.isJump == True or falling == True:
                win.blit(airDamageL[3], (int(self.x), int(self.y)))
                man.y -= 15
            else:
                win.blit(damageLeft[1], (int(self.x), int(self.y)))
        if self.damageL:
            if self.isJump == True or falling == True:
                win.blit(airDamageR[3], (int(self.x), int(self.y)))
                man.y -= 15
            else:
                win.blit(damage[1], (int(self.x), int(self.y)))
                
        if not (self.bat):
            if not (self.standing):
                if self.left: 
                    if not (self.isJump) and falling == True and self.jumpAtk == False:
                        self.hitbox = pygame.Rect(int(self.x)+17, int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(fallLeft[self.fallCount//2], (int(self.x -20), int(self.y -20)))
                        self.fallCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                            self.shieldCount += 1
                        
                    elif self.isJump:
                        self.hitbox = pygame.Rect(int(self.x)+17, int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        if self.jumpAtk:
                            win.blit(JumpATKL[self.jumpAtkCount//2], (int(self.x), int(self.y)))
                            self.jumpAtkCount +=1
                        else:
                            win.blit(jumpLeft[self.jumpingUpCount//2], (int(self.x +5), int(self.y)))
                            self.jumpingUpCount += 1
                            if self.shield:
                                win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                                self.shieldCount += 1
                    else:
                        self.hitbox = pygame.Rect(int(self.x - 23), int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(walkLeft[self.walkCount//1], (int(self.x - 77), int(self.y - 17)))
                        self.walkCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 50), int(self.y + 11)))
                            self.shieldCount += 1
                            
                elif self.right:
                    if not (self.isJump) and falling == True and self.jumpAtk == False:
                        self.hitbox = pygame.Rect(int(self.x)+17, int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(fallRight[self.fallCount//2], (int(self.x -20), int(self.y -20)))
                        self.fallCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                            self.shieldCount += 1
                        
                    elif self.isJump:
                        self.hitbox = pygame.Rect(int(self.x)+17, int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        if self.jumpAtk:
                            win.blit(JumpATKR[self.jumpAtkCount//2], (int(self.x), int(self.y)))
                            self.jumpAtkCount +=1
                        else:
                            win.blit(jumpRight[self.jumpingUpCount//2], (int(self.x -5), int(self.y)))
                            self.jumpingUpCount += 1
                            if self.shield:
                                win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 72), int(self.y)))
                                self.shieldCount += 1
                    else:
                        self.hitbox = pygame.Rect(int(self.x)+17, int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(walkRight[self.walkCount//1], (int(self.x - 46), int(self.y - 17)))
                        self.walkCount += 1
                        if self.shield:
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 52), int(self.y + 11)))
                            self.shieldCount += 1
                
            elif self.isJump:
                self.hitbox = pygame.Rect(int(self.x)+20, int(self.y), 30, 96)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.left:
                    if self.jumpAtk:
                        win.blit(JumpATKL[self.jumpAtkCount//2], (int(self.x), int(self.y)))
                        self.jumpAtkCount +=1
                    else:
                        win.blit(jump2[self.jumpingUpCount//2], (int(self.x - 34), int(self.y - 18)))
                        self.jumpingUpCount += 1
                        if self.shield:
                                win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 15), int(self.y + 10)))
                                self.shieldCount += 1
                else:
                    if self.jumpAtk:
                        win.blit(JumpATKR[self.jumpAtkCount//2], (int(self.x), int(self.y)))
                        self.jumpAtkCount +=1
                    else:
                        win.blit(jump[self.jumpingUpCount//2], (int(self.x - 46), int(self.y - 18)))
                        self.jumpingUpCount += 1
                        if self.shield:
                                win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 30), int(self.y + 10)))
                                self.shieldCount += 1
                    
            elif self.crouching:
                if self.left:
                    self.hitbox = pygame.Rect(int(self.x), int(self.y + 49), 44, 48)
                    pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                    if self.shield:
                            win.blit(crouch2[self.crouchCount//1], (int(self.x - 20), int(self.y -4)))
                            self.crouchCount += 1
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 22), int(self.y + 47)))
                            self.shieldCount += 1
                    elif self.crouchATK:
                        win.blit(SquatAtkL[self.crouchATKcount//1], (int(self.x -109), int(self.y +14)))
                        self.crouchATKcount += 1
                        self.crouchCount = 13
                    else:
                        win.blit(crouch2[self.crouchCount//1], (int(self.x - 20), int(self.y -4)))
                        self.crouchCount += 1
                else:
                    self.hitbox = pygame.Rect(int(self.x +2), int(self.y + 49), 44, 48)
                    pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                    if self.shield:
                            win.blit(crouch[self.crouchCount//1], (int(self.x - 50), int(self.y -4)))
                            self.crouchCount += 1
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 39), int(self.y + 47)))
                            self.shieldCount += 1
                    elif self.crouchATK:
                        win.blit(SquatAtkR[self.crouchATKcount//1], (int(self.x -52), int(self.y +14)))
                        self.crouchATKcount += 1
                        self.crouchCount = 13
                    else:
                        win.blit(crouch[self.crouchCount//1], (int(self.x - 50), int(self.y -4)))
                        self.crouchCount += 1
                        
                
            elif self.attacking:
                self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 96)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.left:
                    self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 100)
                    win.blit(ALKattackLeft[self.attackCount//1], (int(self.x - 152), int(self.y - 24)))
                    self.attackCount += 1
                else:
                    win.blit(ALKattack[self.attackCount//1], (int(self.x - 58), int(self.y - 24)))
                    self.attackCount += 1
                    
            else:       
                if self.idle1: 
                    if self.left:
                        self.hitbox = pygame.Rect(int(self.x), int(self.y), 50, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(idle1L[self.idle1Count], (int(self.x - 23), int(self.y)))
                        self.idle1Count += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 26), int(self.y + 9)))
                            self.shieldCount += 1
                    else:
                        self.hitbox = pygame.Rect(int(self.x), int(self.y), 50, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(idle1R[self.idle1Count], (int(self.x - 2), int(self.y)))
                        self.idle1Count += 1
                        if self.shield:
                            self.idle1 = True
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 31), int(self.y + 9)))
                            self.shieldCount += 1 
                else:
                    if self.left:
                            self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 96)
                            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                            if falling == True and self.jumpAtk == False:
                                win.blit(fallLeft[self.fallCountB//2], (int(self.x -20), int(self.y -20)))
                                self.fallCountB += 1
                            else:
                                win.blit(char2[self.idleCount//3], (int(self.x)-20, int(self.y)-4))
                                self.idleCount += 1
                    else:
                        self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        if falling == True and self.jumpAtk == False:
                            win.blit(fallRight[self.fallCountB//2], (int(self.x -20), int(self.y -20)))
                            self.fallCountB += 1
                        else:
                            win.blit(char[self.idleCount//3], (int(self.x)-20, int(self.y)-4))
                            self.idleCount += 1

#===========BAT Animation==================================================
        else:
            self.y -= 10
            if self.left:
                self.hitbox = pygame.Rect(int(self.x)+13, int(self.y +12), 48, 40)
                self.feetBox = pygame.Rect(int(self.x)+13, int(self.y +12), 48, 40)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                pygame.draw.rect(win, (255,0,0), self.feetBox,2)
                win.blit(AlucardBatL[self.batCount//3], (int(self.x -30), int(self.y -70)))
                self.batCount += 1
            else:
                self.hitbox = pygame.Rect(int(self.x)-10, int(self.y +12), 48, 40)
                self.feetBox = pygame.Rect(int(self.x)-10, int(self.y +12), 48, 40)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                pygame.draw.rect(win, (255,0,0), self.feetBox,2)
                win.blit(AlucardBatR[self.batCount//3], (int(self.x -50), int(self.y -70)))
                self.batCount += 1




    def hit(self):
        SOUNDS_A[random.randrange(1,5)].play()
##            SOUNDS_A[5].play()   
            # if damage + man.health//4 : ALUK.6play() # its high damageTaken hit sound
        #self.isJump = False
        #self.jumpCount = 10
        global bgX
        global bgXmountain
        global scrollingOn
        global platformsA
        self.walkCount = 0
##        pygame.display.flip()
##        i = 0
##        while i < 300:
##            pygame.time.delay(0)
##            i += 1
##            for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                    i = 0
##                    run = False
                    #pygame.quit()
        if Alucardhealth <= 0:
            SOUNDS_A[16].play()   # this is not playing , i think it quits too fast , check later. but maybe if i
            SOUNDS_A[15].play()   # just make it not quit the game and rather go to a game over screen i think it will work fine.
            run = False
            #pygame.quit() # maybe if i use a counter,like the time
            #sys.exit()

    def gravity(self):
        if gravity == True:
            if AlucardMenuOn == False:
                self.y += 10
            if self.y > 585 and self.y >= 0:
                self.y = 585
                
man = player(5-scroll[0], 557-scroll[1], 50, 90)

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============== ENEMIES ========================
class Enemy(object):
    def __init__(self, x, y, width, height, end, respawnX):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.respawnX = respawnX
        self.left = False
        self.right = False
        self.leftAtk = False
        self.rightAtk = False
        self.atkCount = 0
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
        self.health = 10
        self.visible = True
        self.alive = True
        self.explode = False
        self.explodeCount = 0
        self.respawnCount = 0
        self.tangible = False
#===============================================
#===============================================
#================ MOTION =======================
#===============================================
#===============================================        
        self.walk_left = False
        self.walk_right = False
        self.attack_Right = False
        self.attack_Left = False
#===============================================
#===============================================
#=========== STATS NUMBERS =====================
#===============================================
#===============================================        
        self.defense = 1
        self.attack = 2
        self.item_1_drop_chance = 30
        self.item_2_drop_chance = 10
        self.money_drop_chance = 10
        self.gold = 5
#===============================================
#===============================================
#========== DAMAGE NUMBERS =====================
#===============================================
#===============================================
        self.damage = (man.atk - self.defense)
        self.currentXposition = 0
        self.damageNumberMotionX = 0
        self.damageNumberMotionY = 10 
        self.damaged = False
        self.fadingCount = 0

    def hit(self):
        if self.visible and self.damaged == False:
            self.damaged = True            
            SOUNDS_A[random.randrange(24,25)].play()
            if self.health > 1:
                self.health -= self.damage
            else:
                self.alive = False
                SOUNDS_A[28].play()
                SOUNDS_A[29].play()

    def draw(self, win, Animation_Length_times_three, Image_Right, Image_Left):
        self.move()
        if self.fadingCount + 1 >= 3:
            self.damageNumberMotionX = 2
            self.damageNumberMotionY += 1
        if self.fadingCount + 1 >= 5:
            self.damageNumberMotionX = 1
        if self.fadingCount + 1 >= 7:
            self.damageNumberMotionX = 0
        if self.fadingCount + 1 >= 10:
            self.damageNumberMotionX = -1
            
        if self.fadingCount + 1 >= 30:
            self.currentXposition = -100
            self.damaged = False
            self.fadingCount = 0
            self.damageNumberMotionX = 3
            self.damageNumberMotionY = 10

        if self.damaged:
            self.fadingCount += 1
            for i, d in enumerate(str(self.damage)):
              win.blit(NumDamage[d], (int(self.currentXposition + self.damageNumberMotionX), int(self.y - self.damageNumberMotionY)))
          
        if self.respawnCount >= 120:
            self.x = self.respawnX
            self.health = 10
            self.explode = False
            self.alive = True
            self.vel = 3
        if self.respawnCount >= 150:
            self.respawnCount = 0
            self.visible = True
            
        if self.visible == False:
            self.respawnCount += 1
        else:
            self.respawnCount = 0
        if self.visible:
            if self.alive:
                if self.walkCount + 1 >= Animation_Length_times_three:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(Image_Right[self.walkCount //3], (int(self.x), int(self.y)))
                    self.walkCount += 1

                else:
                    win.blit(Image_Left[self.walkCount //3], (int(self.x), int(self.y)))
                    self.walkCount += 1

                self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            else:
                self.vel = 0
                if self.explodeCount + 1 >= 36:
                    self.explodeCount = 0
                    global AlucardKill
                    global AlucardExp
                    global AlucardNextLevel
                    
                    AlucardKill += 1
                    AlucardExp += 3
                    AlucardNextLevel -= 3
                        
                    self.visible = False
                    
                win.blit(explosion[self.explodeCount//3], (int(self.x), int(self.y)))
                self.explodeCount += 1
                win.blit(explosion[self.explodeCount//3], (int(self.x), int(self.y + 50)))
                self.explodeCount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
##          Tiger Information:
##                if self.walkCount + 1 >= 69:
##                    self.walkCount = 0
##                if self.atkCount + 1 > 8 and self.atkCount +1 < 10:
##                    SOUNDS_A[30].play()
##                if self.atkCount + 1 >= 50:
##                    self.atkCount = 0
                    
##                if self.vel > 0:
##                    if self.path[0] <= man.x and man.x <= self.end and man.x >= self.x:
##                        win.blit(tigerAtkR[self.atkCount//2], (int(self.x - 182), int(self.y -224)))
##                        self.atkCount += 1
##                    else:
##                        win.blit(tigerIdleR[self.walkCount //3], (int(self.x -182), int(self.y -224)))
##                        self.walkCount += 1
##
##                else:
##                    if self.path[0] <= man.x and man.x <= self.end and man.x <= self.x:
##                        win.blit(tigerAtkL[self.atkCount//2], (int(self.x -182), int(self.y -224)))
##                        self.atkCount += 1
##                    else:
##                        win.blit(tigerIdleL[self.walkCount //3], (int(self.x -182), int(self.y -224)))
##                        self.walkCount += 1

##             Information about Gargoyle
##                if self.walkCount + 1 >= 20:
##                    self.walkCount = 0
##                if self.atkCount + 1 > 8 and self.atkCount +1 < 10:
##                    SOUNDS_A[30].play()
##                if self.atkCount + 1 >= 12:
##                    self.atkCount = 0
##
##                if self.vel > 0:
##                    if self.path[0] <= man.x and man.x <= self.end and man.x >= self.x:
##                        win.blit(gargoyleAtk[self.atkCount//4], (int(self.x), int(self.y)))
##                        self.atkCount += 1
##                    else:                        
##                        win.blit(gargoyleWalk[self.walkCount//4], (self.x, self.y))
##                        self.walkCount += 1
##
##                else:
##                    if self.path[0] <= man.x and man.x <= self.end and man.x <= self.x:
##                        win.blit(gargoyleAtkLeft[self.atkCount//4], (int(self.x), int(self.y)))
##                        self.atkCount += 1
##                    else:                        
##                        win.blit(gargoyleWalkLeft[self.walkCount //4], (self.x, self.y))
##                        self.walkCount += 1

        
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#========= WALLS/DOORS/FLOORS ==================
class block(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
        self.visible = True     

    def draw(self,win):
        if self.visible:
            self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#=============== CANDLE ========================
class candle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(int(self.x) + 9, int(self.y) + 42, int(self.width), int(self.height))
        self.visible = True
        self.flame = 0
        self.explode = False
        self.explodeCount = 0
        self.flameOn = True

    def draw(self,win):
        if self.visible:
            if self.flameOn:
                if self.flame + 1 >= 15:
                    self.flame = 0
                    
                self.hitbox = pygame.Rect(int(self.x) + 9, int(self.y) + 42, int(self.width), int(self.height))
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                win.blit(candle1[self.flame//5], (int(self.x), int(self.y)))
                self.flame += 1
            else:
                if self.explodeCount + 1 >= 36:
                    self.explodeCount = 0
                    self.visible = False
                    
                win.blit(explosion[self.explodeCount//3], (int(self.x), int(self.y + 30)))
                self.explodeCount += 1
                win.blit(explosion[self.explodeCount//3], (int(self.x), int(self.y + 80)))
                self.explodeCount += 1
            
    def hit(self):
        if self.visible:
            self.flameOn = False
            SOUNDS_A[28].play()
            SOUNDS_A[29].play()
            SOUNDS_A[random.randrange(24,25)].play()
        
#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#=============== HEART =========================
class heart(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 3
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 5, 5)
        self.visible = True
        self.motion = True
        self.fadingCount = 0
        self.fade = 0
        self.blink = False
        self.awaken = False
        self.got = False

    def draw(self,win):
        if self.got == False:
            self.move()
            if self.motion == False:
                self.fadingCount += 1
                if self.fadingCount + 1 >= 200:
                    self.blink = True
                if self.fade + 1 >= 6:
                    self.fade = 0
                if self.fadingCount + 1 >= 300:
                    self.visible = False

            
            if self.visible:
                if self.vel > 0:
                    win.blit(hearts, (int(self.x), int(self.y)))
                elif self.blink:
                    win.blit(heartsFading[self.fade//1], (int(self.x), int(self.y)))
                    self.fade += 1
                else:
                    win.blit(hearts, (int(self.x), int(self.y)))
            

                self.hitbox = pygame.Rect(self.x, self.y, 5, 5)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.got == False:
            self.visible = False
            if self.awaken == True:
                self.visible = True
                self.y += 3
                if self.y > 630 and self.y >= 0:
                    self.y = 630
                    self.motion = False
                if self.motion == True:
                    if self.vel > 0:
                        if self.x + self.vel < self.path[1]:
                            self.x += self.vel
                        else:
                            self.vel = self.vel * -1
                    else:
                        if self.x - self.vel > self.path[0]:
                            self.x += self.vel
                        else:
                            self.vel = self.vel * -1

    def hit(self):
        SOUNDS_A[16].play()
        self.got = True
        
#=====================
#=====================
#------ TIME ---------
#=====================
#=====================
class time(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.timeCounter = 0
        self.visible = False
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def on(self):
        self.timeCounter += 1
        if self.timeCounter + 1 >= 31:
            self.seconds += 1
            pygame.display.flip()
            self.timeCounter = 0

        if self.seconds + 1 >= 61:
            self.minutes += 1
            self.seconds = 0

        if self.minutes + 1 >= 61:
            self.hours += 1
            self.minutes = 0

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#=============== ITEMS =========================
class itemCLASS(object):
    def __init__(self, x, y, img, name, description, ID, tipo):
        global items
        self.x = x
        self.y = y
        self.ID = ID
        self.quantity = 0
        self.quantityDisplay = font1.render(str(self.quantity), 1, (211,211,211))
        self.img = items[img]
        self.tipo = tipo
        self.imgBig = pygame.transform.rotozoom(items[img], 0, 1.7)
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
        self.equipHoverbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
        self.visible = True
        self.name = font1.render((itemsNames[name]), 1, (211,211,211))
        self.description = font2.render((itemsDescription[description]), 1, (211,211,211))
        self.desccriptionBox = pygame.Rect(int(self.x), int(self.y), 16, 30)
        
    def draw(self,win):
        self.quantityDisplay = font1.render(str(self.quantity), 1, (211,211,211))
        self.y += 10
        if self.visible == True:
            win.blit(self.img, (int(self.x), int(self.y)))
            self.hitbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
    def gotItem(self):
        self.quantityDisplay = font1.render(str(self.quantity), 1, (211,211,211))
        global AlucardInventory
        global InventoryIDs
        if (self.ID) not in (InventoryIDs):
            InventoryIDs.append(self.ID)
            AlucardInventory.append(self) # items (self, x, y, img, name, description, ID, tipo)
            self.quantity += 1
        elif (self.ID) in (InventoryIDs):
            for a in AlucardInventory:
                if a.ID == self.ID:
                    a.quantity += 1
        self.visible = False


    def equipItem(self):
        self.quantityDisplay = font1.render(str(self.quantity), 1, (211,211,211))
        global AlucardInventory
        global AlucardLeftHandItem
        global AlucardRightHandItem
        global SelectedHand
        global AlucardInventoryOn
        if AlucardInventoryOn:
            if SelectedHand == 1: #leftHand
                    
                if self.quantity >= 1: # if quantity is one. and the lenght of quantity of items on hand is 2 or bigger, if the ID of the item 2 exist on the inventory
                    if len(AlucardLeftHandItem) >= 2: # we check the items on inventory and match it, and for that item, its quantity will be +1.
                        if ((AlucardLeftHandItem[1]).ID) in (InventoryIDs):# if the item 2 ID i not there, we will send that item to the inventory and its ID to 
                            for b in AlucardInventory: # the ID list and then add +1 to its quantity, since its 0.
                                if b.ID == (AlucardLeftHandItem[1]).ID:# after any of these situations, we will take out the item from the position 2 on the hand.
                                    b.quantity += 1 # and put the targeted item on the position 2. then, we will check how many of that item we have.
                        if ((AlucardLeftHandItem[1]).ID) not in (InventoryIDs): # we will check if the target item ID is on the ID list. 
                            InventoryIDs.append((AlucardLeftHandItem[1]).ID)# if it is, we will remove it, and remove it from the inventory list, and set
                            AlucardInventory.append(AlucardLeftHandItem[1])# its quantity to zero. remind : this only happens when u have 1 of that item.
                            if (AlucardLeftHandItem[1]).quantity == 0:
                                (AlucardLeftHandItem[1]).quantity += 1
                        AlucardLeftHandItem.pop(1)
                    AlucardLeftHandItem.append(self)
                    if (self.ID) in (InventoryIDs):
                        InventoryIDs.remove(self.ID)
                        AlucardInventory.remove(self)
                        if self.quantity == 1:
                            self.quantity = 0
 
            elif SelectedHand == 2: #rightHand
                
                if self.quantity >= 1: # if quantity is one. and the lenght of quantity of items on hand is 2 or bigger, if the ID of the item 2 exist on the inventory
                    if len(AlucardRightHandItem) >= 2: # we check the items on inventory and match it, and for that item, its quantity will be +1.
                        if ((AlucardRightHandItem[1]).ID) in (InventoryIDs):# if the item 2 ID i not there, we will send that item to the inventory and its ID to 
                            for b in AlucardInventory: # the ID list and then add +1 to its quantity, since its 0.
                                if b.ID == (AlucardRightHandItem[1]).ID:# after any of these situations, we will take out the item from the position 2 on the hand.
                                    b.quantity += 1 # and put the targeted item on the position 2. then, we will check how many of that item we have.
                        if ((AlucardRightHandItem[1]).ID) not in (InventoryIDs): # we will check if the target item ID is on the ID list. 
                            InventoryIDs.append((AlucardRightHandItem[1]).ID)# if it is, we will remove it, and remove it from the inventory list, and set
                            AlucardInventory.append(AlucardRightHandItem[1])# its quantity to zero. remind : this only happens when u have 1 of that item.
                            if (AlucardRightHandItem[1]).quantity == 0:
                                (AlucardRightHandItem[1]).quantity += 1
                        AlucardRightHandItem.pop(1)
                    AlucardRightHandItem.append(self)
                    if (self.ID) in (InventoryIDs):
                        InventoryIDs.remove(self.ID)
                        AlucardInventory.remove(self)
                        if self.quantity == 1:
                            self.quantity = 0           

    def unequipItem(self):
        global AlucardLeftHandItem
        global AlucardRightHandItem
        global SelectedHand
        if SelectedHand == LeftHand:
            AlucardLeftHandItem.pop(1)
            if (self.ID) not in (InventoryIDs):
                InventoryIDs.append(self.ID)
                AlucardInventory.append(self)
            self.quantity += 1
        elif SelectedHand == RightHand:
            AlucardRightHandItem.pop(1)
            if (self.ID) not in (InventoryIDs):
                InventoryIDs.append(self.ID)
                AlucardInventory.append(self)
            self.quantity += 1

    def useItem(self):
        self.quantity -= 1
        if self.quantity <= 0:
            InventoryIDs.remove(self.ID)
            AlucardInventory.remove(self)
        if EquippeddHand == LeftHand:
            AlucardLeftHandItem.pop(1)
        elif EquippeddHand == RightHand:
            AlucardRightHandItem.pop(1)
    
#==========================================================
#==========================================================

##equipPosition1 = False
##equipPosition2 = False
##equipPosition3 = False
##equipPosition4 = False
##equipPosition5 = False
##equipPosition6 = False
##equipPosition7 = False
##equipPositionList = [equipPosition1, equipPosition2, equipPosition3, equipPosition4, equipPosition5, equipPosition6, equipPosition7]
        
##items = [pygame.image.load(f'DATA/GRAPHICS/ITEMS/{i}.png').convert_alpha() for i in range(162)]
#==========================================================
#==========================================================

##    for a in equipPositionList:
##        if a = False:
##            a.img = 0
##
##
##    for a in itemsList:
##        if a = False:
##            a.img = 0

#==========================================================================================================================
#==========================================================================================================================
#============= MAIN FUNCTION ================================================ BLIT / DRAW =================================
#==========================================================================================================================
#==========================================================================================================================
            #------------------ X And Y Vertices of Scrolling Backgrounds ----------------------------------------
bgX = 0 #bg1
bgXmountain = 0 #bg1

bg1BX = 0 #bg1B
bg1BXmountain = 0 #bg1B
bg1BY = -32#-205 #bg1B -645

bg1CX = 0 #bg1C
bg1CXmountain = 0 #bg1C
bg1CY = 0 #bg1C

bg1DX = 0 #bg1D
bg1DXmountain = 0 #bg1D
bg1DY = 0 #bg1D

bgX2 = 0 #bg8
bgX3 = -2836 #bg6
bgX4 = 0 #bg18
bgX5 = -3128 #bg10
bgX6 = 0 #bg11
bgY6 = 0 #bg11
bgX7 = 0 #bg12
bgX8 = 0 #bg13
bgX9 = 0 #bg19
bgX10 = 0 #bg20
bgX11 = 0 #bg21
bgX12 = 0 #bg24
bgX13 = -1292 #bg16
bgX14 = 0 #bg22

def redrawGameWindow():
#==========================================================
#================= BACKGROUNDS ============================
#==========================================================
#========================================================
#====================================== 1 ==================
    if AlucardMenuOn == False:
        AllParallaxes.equipHoverDisplay = False
        AllParallaxes.inventHoverDisplay = False
        if background1:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X1PR1, (0, 0))
            win.blit(X1PR2, (0, 0))
            win.blit(X1PR3, (int(bgXmountain), 0))
            win.blit(bg1, (int(bgX), 0)) 
            bg1doorA1.draw(win)

            win.blit((font4.render(('Press T for instructions'), 1, (15,5,5))), (605 -20,305))
            win.blit((font4.render(('Press T for instructions'), 1, (30,10,10))), (602 -20,302))
            win.blit((font4.render(('Press T for instructions'), 1, (211,211,211))), (600 -20,300))
            for a in itemsList:
                a.draw(win)

            bg1ground.visible = True
            bg1ground.draw(win)
            # platformsA
            for a in bg1platforms:
                a.visible = True
                a.draw(win)


            for a in bg3_leftWalls:
                a.visible = False
            for a in  bg3_rightWalls:
                a.visible = False

            for a in bg2_leftWalls:
                a.visible = False
            for a in  bg2_rightWalls:
                a.visible = False
                
            for a in bg1_leftWalls:
                a.visible = True
                a.draw(win)
            for a in  bg1_rightWalls:
                a.visible = True
                a.draw(win)
                
            for a in skeletons:
                a.draw(win, 21, skeleton_right, skeleton_left)
                a.tangible = True
##            for a in experimental_enemies:
##                a.draw(win)
##                a.tangible = True
            for a in tigers:
                a.tangible = False

            bg1CD1.draw(win)
            bg1HT1.draw(win)
            bg1CD2.draw(win)
            bg1HT2.draw(win)
            bg1CD3.draw(win)
            bg1HT3.draw(win)
            bg1CD4.draw(win)
            bg1HT4.draw(win)
            bg1CD5.draw(win)
            bg1HT5.draw(win) 
    #========================================================
    #====================================== 1B ==================            
        if background1B:
            for a in bg1_leftWalls:
                a.visible = False
            for a in  bg1_rightWalls:
                a.visible = False
            for a in bg3_leftWalls:
                a.visible = False
            for a in  bg3_rightWalls:
                a.visible = False
                
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X1PR1, (0, 0))
            win.blit(X1PR2, (0, 0))
            win.blit(X1PR3, (int(bg1BXmountain), 0))
            win.blit(bg1B, (int(bg1BX), int(bg1BY)))
            bg1BdoorB1.draw(win)
            bg1BdoorA1.draw(win)
            
            bg1ground1B.visible = True
            bg1ground1B.draw(win)

            for a in bg1Bplatforms:
                a.visible = True
                a.draw(win)
                
            for a in tigers:
                a.draw(win, 12, flying_skull_head_right, flying_skull_head_left)
                a.tangible = True
            for a in bgCtigers:
                a.tangible = False
            for a in skeletons:
                a.tangible = False
            for a in bg2_leftWalls:
                a.visible = True
                a.draw(win)
            for a in  bg2_rightWalls:
                a.visible = True
                a.draw(win)               

    #========================================================
    #====================================== 1C ==================            
        if background1C:
            for a in bg2_leftWalls:
                a.visible = False
            for a in  bg2_rightWalls:
                a.visible = False
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X1PR1, (0, 0))
            win.blit(X1PR2, (0, 0))
            win.blit(X1PR3, (int(bg1CXmountain), 0))
            win.blit(bg1C, (int(bg1CX), int(bg1CY)))
            bg1CdoorB1.draw(win)
            bg1CdoorA1.draw(win)

            for a in bg1Cplatforms:
                a.visible = True
                a.draw(win)
            
            bg1ground1C.visible = True
            bg1ground1C.draw(win)
            for a in tigers:
                a.tangible = False
            for a in bgCtigers:
                a.draw(win, 12, flying_skull_head_right, flying_skull_head_left)
                a.tangible = True
            for a in bg3_leftWalls:
                a.visible = True
                a.draw(win)
            for a in  bg3_rightWalls:
                a.visible = True
                a.draw(win)
    #========================================================
    #====================================== 1D ==================            
        if background1D:
            for a in bg3_leftWalls:
                a.visible = False
            for a in  bg3_rightWalls:
                a.visible = False
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            for a in bgCtigers:
                a.draw(win, 12, flying_skull_head_right, flying_skull_head_left)
                a.tangible = False
                
            win.blit(X1PR1, (0, 0))
            win.blit(X1PR2, (0, 0))
            win.blit(X1PR3, (int(bg1DXmountain), 0))
            win.blit(bg1D, (int(bg1DX), int(bg1DY)))
            bg1DdoorB1.draw(win)
            bg1DdoorA1.draw(win)

            for a in bg1Dplatforms:
                a.visible = True
                a.draw(win)
            
            bg1ground1D.visible = True
            bg1ground1D.draw(win)

            for a in bg4_leftWalls:
                a.visible = True
                a.draw(win)
            for a in  bg4_rightWalls:
                a.visible = True
                a.draw(win)  
    #========================================================
    #====================================== 2 ==================
        if background2:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X2PR1, (0-scroll[0],0-scroll[1]))
            win.blit(bg2, (0,0))
            grasshop1.draw(win, 12, skull_head_right, skull_head_left)
            grasshop1.tangible = True
            Gargoyle1.draw(win, 12, skull_head_right, skull_head_left)
            Gargoyle1.tangible = True
            bg2doorB1.draw(win)
            bg2doorA1.draw(win)
            bg2doorA2.draw(win)

            # platformsA
            bg2groundB.visible = True
            bg2groundB.draw(win)
            bg2pa1.visible = True
            bg2pa1.draw(win)
            bg2pa2.visible = True
            bg2pa2.draw(win)
            bg2pa3.visible = True
            bg2pa3.draw(win)
            bg2pa4.visible = True
            bg2pa4.draw(win)
            for a in bgCtigers:
                a.tangible = False
    #========================================================
    #====================================== 3 ==================
        if background3:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False

            # platformsA
            bg2groundB.visible = True
            bg2groundB.draw(win)
            
            win.blit(bg3, (0,0))
            bg3doorB1.draw(win)
            bg3doorA1.draw(win)
            #theBg3Pillars.draw(win)
    #========================================================
    #====================================== 4 ==================     
        if background4:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(bg4, (0,0))
            win.blit(NPCS[1], (700,585))
            oldman.draw(win)
            bg4doorB1.draw(win)
            bg4doorA1.draw(win)
    #========================================================
    #====================================== 5 ==================       
        if background5:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(bg5, (0,0))
            bg5doorB1.draw(win)
            bg5doorA1.draw(win)
            bg5doorA2.draw(win)

            # platformsA
            bg5pa1.visible = True
            bg5pa1.draw(win)
            bg5pa2.visible = True
            bg5pa2.draw(win)
            bg5pa3.visible = True
            bg5pa3.draw(win)
            bg5pa4.visible = True
            bg5pa4.draw(win)
    #========================================================
    #====================================== 6 ==================
        if background6:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            bg6ground.visible = True
            bg6ground.draw(win)
            
            bg6doorB1.draw(win)
            bg6doorA1.draw(win)
            bg6doorA2.draw(win)
            bg6doorA3.draw(win)
            win.blit(bg6, (bgX3,0))
                    
    #========================================================
    #====================================== 7 ==================
        if background7:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
                
            win.blit(bg7, (0,0))
            for a in doors:
                a.visible = False
            for a in doorsB:
                a.visible = False
            bg7doorB1.draw(win)
            bg7doorA1.draw(win)

    #========================================================
    #====================================== 8 ==================
        if background8:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg8ground.visible = True
            bg8ground.draw(win)
            
            # platformsA
            for a in bg8platforms:
                a.visible = True
                a.draw(win)

            
            
            win.blit(bg8, (bgX2,0))
            bg8doorB1.draw(win)
            bg8doorA1.draw(win)

    #========================================================
    #====================================== 9 ==================
        if background9:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg9platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg9, (0,0))
            bg9doorB1.draw(win)

    #========================================================
    #====================================== 10 ==================
        if background10:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg10ground.visible = True
            bg10ground.draw(win)
            
            # platformsA
            #for a in bg10platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg10, (bgX5,0))
            bg10doorB1.draw(win)
            bg10doorB2.draw(win)
            bg10doorA1.draw(win)

    #========================================================
    #====================================== 11 ==================
        if background11:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg11ground.visible = True
            bg11ground.draw(win)
            
            # platformsA
            #for a in bg11platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg11, (bgX6,bgY6))
            bg11doorB1.draw(win)
            bg11doorA1.draw(win)

    #========================================================
    #====================================== 12 ==================
        if background12:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg12ground.visible = True
            bg12ground.draw(win)
            
            # platformsA
            #for a in bg12platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg12, (bgX7,0))
            bg12doorB1.draw(win)
            bg12doorA1.draw(win)
            bg12doorA2.draw(win)

    #========================================================
    #====================================== 13 ==================
        if background13:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg13ground.visible = True
            bg13ground.draw(win)
            
            # platformsA
            #for a in bg13platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg13, (bgX8,0))
            bg13doorB1.draw(win)
            #bg13doorA1.draw(win)

    #========================================================
    #====================================== 15 ==================
        if background15:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg15platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg15, (0,0))
            bg15doorB1.draw(win)
            bg15doorA1.draw(win)

    #========================================================
    #====================================== 16 ==================
        if background16:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg15platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg16, (bgX13,0))
            bg15doorB1.draw(win)
            bg15doorA1.draw(win)

    #========================================================
    #====================================== 17 ==================
        if background17:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg15platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg17, (0,0))
            bg17doorB1.draw(win)

    #========================================================
    #====================================== 18 ==================
        if background18:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg18ground.visible = True
            bg18ground.draw(win)

            # platformsA
            
            win.blit(bg18, (bgX4,0))
            bg18doorB1.draw(win)
            bg18doorA1.draw(win)

    #========================================================
    #====================================== 19 ==================
        if background19:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg19ground.visible = True
            bg19ground.draw(win)
            
            # platformsA
            #for a in bg19platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg19, (bgX9,0))
            bg19doorB1.draw(win)
            bg19doorA1.draw(win)


    #========================================================
    #====================================== 20 ==================
        if background20:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg20ground.visible = True
            bg20ground.draw(win)
            
            # platformsA
            #for a in bg19platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg20, (bgX10,0))
            bg20doorB1.draw(win)
            bg20doorA1.draw(win)

    #========================================================
    #====================================== 21 ==================
        if background21:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg21ground.visible = True
            bg21ground.draw(win)
            
            # platformsA
            #for a in bg21platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg21, (bgX11,0))
            bg21doorB1.draw(win)
            bg21doorA1.draw(win)

    #========================================================
    #====================================== 22 ==================
        if background22:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg22ground.visible = True
            bg22ground.draw(win)
            
            # platformsA
            #for a in bg21platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg22, (bgX14,0))
            bg22doorB1.draw(win)
            bg22doorA1.draw(win)

    #========================================================
    #====================================== 23 ==================
        if background23:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg21platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg23, (0,0))
            bg23doorB1.draw(win)
            bg23doorA1.draw(win)


    #========================================================
    #====================================== 24 ==================
        if background24:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
                
            bg24ground.visible = True
            bg24ground.draw(win)
            
            # platformsA
            #for a in bg24platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg20, (bgX12,0))
            bg24doorB1.draw(win)

    #========================================================
    #====================================== 31 ==================
        if background31:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            
            # platformsA
            #for a in bg31platforms:
            #    a.visible = True
            #    a.draw(win)
            
            win.blit(bg31, (0,0))
            #bg31doorB1.draw(win)
            #bg31doorA1.draw(win)  -----------------------
            
    #  ==================================================================================
    #     ================== All time on Screen ======================================
    #  ==================================================================================

    #=========================================================
    #=================== HUD==================================
        win.blit(AlucardHealthHud, (0, 0))

        for i, d in enumerate(str(Alucardhealth)):
          win.blit(HealthNum[d], (40 + i * 10, 60))

        for i, d in enumerate(str(AlucardHearts)):
          win.blit(Whitenum[d], (230 + i * 10, 55))

    # if **** win.blit(AlucarlowdHealthHud, (-9, -27))

    #=========================================================
    #=========================================================
        TIME.on()
        AllParallaxes.draw(win) # forest , bg3pillars , Mp Bar
        if instructionsOn == True:
            win.blit(instructions, (0,0))
        man.draw(win)
        Alucardspeech01 = True
        
##        win.blit(ITEMpotion, (1240,595)) #  win blit selected item 1,2,3,4 if not , blit 0. something like that
        win.blit(SUBMENU[0], (1215,575))
                 
    else:
        if AlucardEquipMenuOn:
            TIME.on()
            win.blit(AlucardItems, (14, 385))
            theHover.draw(win)
            (AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))]).desccriptionBox = pygame.Rect(1, 1, 50, 20)
            (AlucardRightHandItem[((len(AlucardRightHandItem) - 1))]).desccriptionBox = pygame.Rect(1, 1, 50, 20) 
            for i, a in enumerate(AlucardInventory):
              if a.quantity >= 1:
                  row = i // 4
                  column = i % 4
                  a.desccriptionBox = pygame.Rect(int(72 + (column * 315)), int(inventoryYaxe + (row * 44)), 50, 20)
                  win.blit(a.img, [72 + (column * 315), (inventoryYaxe + (row * 44))])
                  win.blit(a.name, [100 + (column * 315), (inventoryYaxe + (row * 44))])
                  win.blit(a.quantityDisplay, [305 + (column * 315), (inventoryYaxe + (row * 44) - 3)])
            win.blit(AlucardEquipMenu, (0, 0))
            AllParallaxes.draw(win)
            AllParallaxes.MpFullDisplay = False
            AllParallaxes.equipHoverDisplay = False
            AllParallaxes.inventHoverDisplay = True
            
            win.blit((AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))]).img, (550, 52))
            (AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))]).equipHoverbox = pygame.Rect(550, 52, 50, 20)
            win.blit((AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))]).name, (590, 48))
            win.blit((AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))]).quantityDisplay, (780, 48))
            
            win.blit((AlucardRightHandItem[((len(AlucardRightHandItem) - 1))]).img, (550, 96))
            (AlucardRightHandItem[((len(AlucardRightHandItem) - 1))]).equipHoverbox = pygame.Rect(550, 96, 50, 20)
            win.blit((AlucardRightHandItem[((len(AlucardRightHandItem) - 1))]).name, (590, 90))
            win.blit((AlucardRightHandItem[((len(AlucardRightHandItem) - 1))]).quantityDisplay, (780, 90))
            
            win.blit((AlucardHeadItem[0]).img, (550, 96 + 42))
            (AlucardHeadItem[0]).equipHoverbox = pygame.Rect(550, 96 + 42, 50, 20)
            win.blit((AlucardHeadItem[0]).name, (590, 89 + 47 - 3))
            win.blit((AlucardArmorItem[0]).img, (550, 96 + 87))
            (AlucardArmorItem[0]).equipHoverbox = pygame.Rect(550, 96 + 83, 50, 20)
            win.blit((AlucardArmorItem[0]).name, (590, 89 + 88 - 3))
            win.blit((AlucardAcessoryItem1[0]).img, (550, 96 + 88 + 44 - 7)) # cloak
            (AlucardAcessoryItem1[0]).equipHoverbox = pygame.Rect(550, 96 + 88 + 44 - 7, 50, 20)
            win.blit((AlucardAcessoryItem1[0]).name, (590, 89 + 88 + 44 - 6)) # cloak
            win.blit((AlucardAcessoryItem2[0]).img, (550, 96 + 88 + 88 - 10))
            (AlucardAcessoryItem2[0]).equipHoverbox = pygame.Rect(550, 96 + 90 + 88 - 13, 50, 20)
            win.blit((AlucardAcessoryItem2[0]).name, (590, 89 + 88 + 88 - 12))
            win.blit((AlucardAcessoryItem3[0]).img, (550, 96 + 88 + 88 + 44 - 13))
            (AlucardAcessoryItem3[0]).equipHoverbox = pygame.Rect(550, 96 + 88 + 88 + 44 - 13, 50, 20)         
            win.blit((AlucardAcessoryItem3[0]).name, (590, 89 + 88 + 88 + 44 - 11))

            for i, d in enumerate(str(AlucardSTR)):
              win.blit(NumStatus[d], (152 + i * 20, 238 - 22))
            for i, d in enumerate(str(AlucardCON)):
              win.blit(NumStatus[d], (152 + i * 20, 270 - 22))
            for i, d in enumerate(str(AlucardINT)):
              win.blit(NumStatus[d], (152 + i * 20, 304 - 22))
            for i, d in enumerate(str(AlucardLCK)):
              win.blit(NumStatus[d], (152 + i * 20, 333 - 22))

            for i, d in enumerate(str(AlucardSTR)):
              win.blit(NumStatus[d], (1164 + i * 20, 54 - 22))
            for i, d in enumerate(str(AlucardCON)):
              win.blit(NumStatus[d], (1164 + i * 20, 85 - 22))
            for i, d in enumerate(str(AlucardINT)):
              win.blit(NumStatus[d], (1164 + i * 20, 119 - 22))
            for i, d in enumerate(str(AlucardLCK)):
              win.blit(NumStatus[d], (1164 + i * 20, 149 - 22))

            for i, d in enumerate(str(AlucardATK)):
              win.blit(NumAttack[d], (1200 + i * 20, 285 - 19))
            for i, d in enumerate(str(AlucardATK2)):
              win.blit(NumAttack[d], (1200 + i * 20, 310 - 19))
            for i, d in enumerate(str(AlucardDEF)):
              win.blit(NumAttack[d], (1160 + i * 20, 354 - 19))

            for a in equipSelectionMenu:
                pygame.draw.rect(win, (255,255,0), a.equipHoverbox,2)
            for b in itemsList:
                pygame.draw.rect(win, (0,255,0), b.desccriptionBox,2)
            pygame.draw.rect(win, (255,0,255), theHover.hitbox,2)

            win.blit(descWinImg, (73,600))
            win.blit(descWinDesc, (120,590))
        else:
            AlucardInventoryOn = False
            TIME.on()
            win.blit(AlucardMenu, (0, 0))
            AllParallaxes.draw(win)
            AllParallaxes.MpFullDisplay = False
            AllParallaxes.inventHoverDisplay = False
            AllParallaxes.equipHoverDisplay = True
            win.blit(AlucardMenuSelection, (407, 346))

            # ----------- NUMBERS -------------

            for i, d in enumerate(str(AlucardExp)):
              win.blit(NumStatus[d], (304 + i * 22, 557))
            for i, d in enumerate(str(AlucardNextLevel)):
              win.blit(NumStatus[d], (304 + i * 22, 588))
            for i, d in enumerate(str(AlucardGold)):
              win.blit(NumStatus[d], (304 + i * 22, 621))
            for i, d in enumerate(str(AlucardSTR)):
              win.blit(NumStatus[d], (304 + i * 20, 401))
            for i, d in enumerate(str(AlucardCON)):
              win.blit(NumStatus[d], (304 + i * 20, 432))
            for i, d in enumerate(str(AlucardINT)):
              win.blit(NumStatus[d], (304 + i * 20, 464))
            for i, d in enumerate(str(AlucardLCK)):
              win.blit(NumStatus[d], (304 + i * 20, 496))
              
            for i, d in enumerate(str(AlucardLevel)):
              win.blit(NumLevel[d], (1171 + i * 26, 60))

            for i, d in enumerate(str(AlucardKill)):
              win.blit(NumRoom[d], (1133 + i * 22, 385))
            for i, d in enumerate(str(AlucardRooms)):
              win.blit(NumRoom[d], (1133 + i * 22, 351))

            for i, d in enumerate(str(Alucardhealth)):
              win.blit(NumHealthPoints[d], (710 + i * 15, 194))
            for i, d in enumerate(str(AlucardMaxHealth)):
              win.blit(NumHealthPoints[d], (785 + i * 15, 194))

            for i, d in enumerate(str(AlucardMP)):
              win.blit(NumMagicPoints[d], (710 + i * 15, 230))
            for i, d in enumerate(str(AlucardMaxMP)):
              win.blit(NumMagicPoints[d], (785 + i * 15, 230))

            for i, d in enumerate(str(AlucardHearts)):
              win.blit(NumHeart[d], (730 + i * 15, 268))
            for i, d in enumerate(str(AlucardMaxHearts)):
              win.blit(NumHeart[d], (780 + i * 15, 268))

            for i, d in enumerate(str(AlucardATK)):
              win.blit(NumAttack[d], (1157 + i * 20, 197))
            for i, d in enumerate(str(AlucardATK2)):
              win.blit(NumAttack[d], (1157 + i * 20, 221))
            for i, d in enumerate(str(AlucardDEF)):
              win.blit(NumAttack[d], (1157 + i * 20, 264))

                       # --- TIME ----
            for i, d in enumerate(str(TIME.seconds)):
              win.blit(NumTime[d], (1174 + i * 15, 558))
            for i, d in enumerate(str(TIME.minutes)):
              win.blit(NumTime[d], (1118 + i * 15, 558))
            for i, d in enumerate(str(TIME.hours)):
              win.blit(NumTime[d], (1069 + i * 15, 558))
    pygame.display.update()

#=============================================================== MAIN MENU BLIT ==============================================================================
#=============================================================================================================================================================
def main_menu_drawing_window():
    main_Menu_instance.draw(win)
    win.blit(main_Menu_instance.newGameShadow, (140,300 -25))
    win.blit(main_Menu_instance.newGame, (135,300 -30))
    
    win.blit(main_Menu_instance.continuarShadow, (165,350 -25))
    win.blit(main_Menu_instance.continuar, (160,350 -30))
    
    win.blit(main_Menu_instance.quitShadow, (195,400 -25))
    win.blit(main_Menu_instance.quit, (190,400 -30))

    pygame.display.flip()

#================================================================ KONAMI BLIT ================================================================================
#=============================================================================================================================================================
def konami_logo_drawing_window():
    logo_instance.draw(win)
    pygame.display.flip()
#=============================================================================================================================================================
#=============================================================================================================================================================

#=============================================================================================================================================================
#=============================================================================================================================================================
#           ======================================================= CLASSES INSTANCES ==============================================================
#=============================================================================================================================================================
#=============================================================================================================================================================
#theForest = parallax(0, 0, 0, 0) # --------- to use later.
#theBg3Pillars = parallax(0, 0, 0, 0) # ---------- to use later.
main_Menu_instance = Main_Menu_Class(0,0,0,0,130,300)
logo_instance = Konami_Logo_Class(0,0,0,0)
print(Enemy.__dict__)# will print all stuff related to Enemy class
#==================================
font = pygame.font.SysFont('comicsans', 30, True)
AllParallaxes = parallax(0, 0, 0, 0)
theHover = InventoryHoverClass(0, 0, 0, 0)
TIME = time(0, 0, 0, 0)

# items (self, x, y, img, name, description, ID, tipo)
item00 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #empty hand
copy_item_0 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
item000 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #empty hand
copy_item_1 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
itemHead = itemCLASS(300, 200, 15, 15, 15, 15, 0)
copy_item_2 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
itemBody = itemCLASS(300, 200, 17, 17, 17, 17, 0)
copy_item_3 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
itemBody2 = itemCLASS(300, 200, 16, 16, 16, 16, 0)# items (self, x, y, img, name, description, ID, tipo)
copy_item_4 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
itemBody3 = itemCLASS(300, 200, 16, 16, 16, 16, 0)
copy_item_5 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM
itemBody4 = itemCLASS(300, 200, 16, 16, 16, 16, 0)
copy_item_6 = itemCLASS(300, 200, 0, 0, 0, 0, 0) #COPY ITEM

descWinImg = blankItem[0]
descWinDesc = blankItem[0]
item001 = itemCLASS(310, 200, 1, 1, 1, 1, 0)
item002 = itemCLASS(320, 200, 2, 2, 2, 2, 0)
item003 = itemCLASS(330, 200, 3, 3, 3, 3, 0)# items (self, x, y, img, name, description, ID, tipo)
item004 = itemCLASS(340, 200, 4, 4, 4, 4, 0)
item005 = itemCLASS(350, 200, 5, 5, 5, 5, 0)
item006 = itemCLASS(360, 200, 6, 6, 6, 6, 0)
item007 = itemCLASS(360, 200, 7, 7, 7, 7, 0)
item008 = itemCLASS(360, 200, 8, 8, 8, 8, 0)
item009 = itemCLASS(360, 200, 9, 9, 9, 9, 0)# items (self, x, y, img, name, description, ID, tipo)
item0010 = itemCLASS(360, 200, 10, 10, 10, 10, 0)
item0011 = itemCLASS(360, 200, 11, 11, 11, 11, 0)
item0012 = itemCLASS(360, 200, 12, 12, 12, 12, 0)
item0013 = itemCLASS(360, 200, 13, 13, 13, 13, 0)
item0014 = itemCLASS(360, 200, 14, 14, 14, 14, 0)
item0015 = itemCLASS(360, 200, 14, 14, 14, 14, 0)
item0016 = itemCLASS(360, 200, 14, 14, 14, 14, 0)# items (self, x, y, img, name, description, ID, tipo)
item0017 = itemCLASS(360, 200, 14, 14, 14, 14, 0)
item0018 = itemCLASS(360, 200, 14, 14, 14, 14, 0)
item0019 = itemCLASS(360, 200, 14, 14, 14, 14, 0)
item0020 = itemCLASS(360, 200, 14, 14, 14, 14, 0)

##item0015 = itemCLASS(360, 200, 15, 15, 15, 15)
##item0016 = itemCLASS(360, 200, 16, 16, 16, 16)
##item0017 = itemCLASS(360, 200, 17, 17, 17, 17)
##item0018 = itemCLASS(360, 200, 18, 18, 18, 18)
##item0019 = itemCLASS(360, 200, 19, 19, 19, 19)
##item0020 = itemCLASS(360, 200, 20, 20, 20, 20)


# background 1 =========================================================================
bg1ground = block(-670, 648, 6510, 1) #  if bg8ground.x >= -10659 and bg8ground.x <= -1339:    #4560  10720
bg1pa1 = block(245, 577, 240, 1)
bg1pa2 = block(523, 485, 240, 1)
bg1pa3 = block(799, 398, 1039, 1)
bg1pa4 = block(1877, 485, 240, 1)
bg1pa5 = block(2158, 555, 240, 1)
bg1pa6 = block(2835, 551, 176, 20)
bg1pa7 = block(2990, 454, 468, 20)
bg1pa8 = block(3462, 551, 150, 20)

bg1wl1 = block(2836, 566, 10, 118)
bg1wl2 = block(2990, 469, 10, 84)
bg1wr1 = block(3602, 566, 10, 118)
bg1wr2 = block(3449, 469, 10, 84)

bg1CD1 = candle(430, 518, 30, 37) 
bg1HT1 = heart(450, 548, 30, 37, 470)# +20 +30 // // x+20
bg1CD2 = candle(550, 518, 30, 37) 
bg1HT2 = heart(570, 548, 30, 37, 590)
bg1CD3 = candle(1900, 518, 30, 37)
bg1HT3 = heart(1920, 548, 30, 37, 1950)
bg1CD4 = candle(2900, 422, 30, 37)
bg1HT4 = heart(2920, 452, 30, 37, 2950)
bg1CD5 = candle(3827, 518, 30, 37)
bg1HT5 = heart(3847, 548, 30, 37, 3867)

skeleton1 = Enemy(500, 558, 50, 95, 1250, 500)
skeleton2 = Enemy(400, 558, 50, 95, 1250, 400)
skeleton3 = Enemy(300, 558, 50, 95, 1250, 300)
skeleton4 = Enemy(1885, 390, 50, 95, 2115, 1885)
skeleton5 = Enemy(3000, 359, 50, 95, 3447, 3000)
bg1doorA1 = block(1300, 500, 50, 100)
#========================================================================================
# bacground 1B
bg1ground1B = block(-670, 648, 6510, 1)
bg1BdoorB1 = block(15, 150, 20, 300)
bg1Bpa1 = block(0, 683, 2022, 20)
bg1Bpa2 = block(288, 633, 25, 1)
bg1Bpa3 = block(433, 511, 25, 1)
bg1Bpa4 = block(518, 431, 25, 1)
bg1Bpa5 = block(563, 356, 128, 20)
bg1Bpa6 = block(739, 259, 25, 1)
bg1Bpa7 = block(719, 431, 25, 1)
bg1Bpa8 = block(804, 511, 25, 1)
bg1Bpa9 = block(949, 633, 25, 1)
bg1Bpa10 = block(360, 579, 544, 20)

bg1Bpa11 = block(2292, 685, 1143, 1)
bg1Bpa12 = block(3722, 684, 900, 20)
bg1Bpa13 = block(1142, 370, 573, 1)
bg1Bpa14 = block(1903, 400, 238, 1)
bg1Bpa15 = block(2390, 243, 967, 20)
bg1Bpa16 = block(1723, 1071, 597, 20)
bg1Bpa17 = block(2568, 1068, 310, 20)
bg1Bpa18 = block(3099, 1072, 310, 20)
bg1Bpa19 = block(3552, 1074, 310, 20)
bg1Bpa20 = block(3937, 1076, 630, 20)
bg1Bpa21 = block(2210, 320, 94, 1)    
bg1Bpa22 = block(2279, 421, 94, 1)
bg1Bpa23 = block(2280, 549, 94, 1)
bg1Bpa24 = block(2210, 320, 94, 1)
bg1Bpa25 = block(2193, 724, 94, 1)
bg1Bpa26 = block(2076, 822, 94, 1)
bg1Bpa27 = block(1930, 900, 94, 1)    
bg1Bpa28 = block(2094, 985, 94, 1)    
bg1Bpa29 = block(2403, 1011, 94, 1)    
bg1Bpa30 = block(2941, 999, 94, 1)    
bg1Bpa31 = block(3438, 993, 94, 1)    
bg1Bpa32 = block(3850, 986, 94, 1)    
bg1Bpa33 = block(3699, 912, 94, 1)  
bg1Bpa34 = block(3546, 826, 94, 1)  
bg1Bpa35 = block(3485, 727, 94, 1)  
bg1Bpa36 = block(3617, 626, 94, 1)  
bg1Bpa37 = block(3478, 537, 94, 1)  
bg1Bpa38 = block(3370, 435, 94, 1)  
bg1Bpa39 = block(3370, 276, 94, 1)  
bg1BdoorA1 = block(1320, 150, 40, 300)

bg2wl1 = block(360, 593 -32, 10, 49)
bg2wl2 = block(563, 371 -32, 10, 208)
bg2wl3 = block(3722, 695 -32, 10, 51)
bg2wl4 = block(2390, 258 -32, 10, 385)
bg2wl5 = block(4024, 1120 -32, 10, 400)
bg2wl6 = block(3639, 1120 -32, 10, 400)
bg2wl7 = block(3186, 1120 -32, 10, 400)
bg2wl8 = block(2655, 1120 -32, 10, 400)
bg2wl9 = block(2564, 1078 -32, 10, 34)
bg2wl10 = block(3095, 1082 -32, 10, 34)
bg2wl11 = block(3548, 1084 -32, 10, 34)
bg2wl12 = block(3933, 1086 -32, 10, 34)
bg2wl13 = block(4526, 750 -32, 10, 280)
bg2wl14 = block(776, 0 -32, 10, 340)

bg2wr1 = block(689, 371 -32, 10, 208)
bg2wr2 = block(892, 593 -32, 10, 49)
bg2wr3 = block(2012, 696 -32, 10, 51)
bg2wr4 = block(3348, 258 -32, 10, 385)
bg2wr5 = block(2224, 1120 -32, 10, 400)
bg2wr6 = block(2781, 1120 -32, 10, 400)
bg2wr7 = block(3312, 1120 -32, 10, 400)
bg2wr8 = block(3765, 1120 -32, 10, 400)
bg2wr9 = block(2314, 1086 -32, 10, 34)
bg2wr10 = block(2871, 1078 -32, 10, 34)
bg2wr11 = block(3402, 1083 -32, 10, 34)
bg2wr12 = block(3855, 1084 -32, 10, 34)
bg2wr13 = block(1722, 750 -32, 10, 280)
bg2wr14 = block(902, 0 -32, 10, 340)

Tiger1 = Enemy(500, bg1BY + 677 -95, 50, 25, 1250, 500)
Tiger2 = Enemy(1000, bg1BY + 677 -95, 50, 25, 1250, 1000)
Tiger3 = Enemy(1500, bg1BY + 677 -95, 50, 25, 1250, 1500)
Tiger4 = Enemy(2000, bg1BY + 677 -95, 50, 25, 1250, 2000)
Tiger5 = Enemy(2500, bg1BY + 677 -95, 50, 25, 1250, 2500)

Tiger6 = Enemy(500, bg1CY + 677 -95, 50, 25, 1250, 500)
Tiger7 = Enemy(1000, bg1CY + 677 -95, 50, 25, 1250, 1000)
Tiger8 = Enemy(1500, bg1CY + 677 -95, 50, 25, 1250, 1500)
Tiger9 = Enemy(2000, bg1CY + 677 -95, 50, 25, 1250, 2000)
Tiger10 = Enemy(2500, bg1CY + 677 -95, 50, 25, 1250, 2500)

# background 1C
bg1CdoorB1 = block(15, 150, 20, 300)
bg1ground1C = block(-670, 648, 6510, 1)
bg1Cpa0 = block(0, 545, 891, 1)
bg1Cpa1 = block(771, 447, 97, 1)
bg1Cpa2 = block(774, 345, 97, 1)
bg1Cpa3 = block(903, 321, 114, 1)
bg1Cpa4 = block(1373, 361, 239, 1)
bg1Cpa5 = block(1579, 237, 239, 1)
bg1Cpa6 = block(2011, 286, 114, 1)
bg1Cpa7 = block(2154, 320, 97, 1)
bg1Cpa8 = block(2155, 417, 97, 1)
bg1Cpa9 = block(2136, 505, 365, 1)
bg1Cpa10 = block(2482, 161, 251, 1)
bg1Cpa11 = block(2579, 498, 97, 1)
bg1Cpa12 = block(2623, 598, 110, 1)
bg1Cpa13 = block(2622, 724, 111, 1)
bg1Cpa14 = block(2092, 814, 642, 1)
bg1Cpa15 = block(972, 899, 1106, 1)
bg1Cpa16 = block(348, 848, 610, 1)
bg1Cpa17 = block(225, 890, 111, 1)
bg1Cpa18 = block(53, 945, 97, 1)
bg1Cpa19 = block(166, 1038, 97, 1)
bg1Cpa20 = block(46, 1125, 97, 1)
bg1Cpa21 = block(190, 1200, 97, 1)
bg1Cpa22 = block(21, 1300, 4500, 1)
bg1Cpa23 = block(3216, 269, 97, 1)
bg1Cpa24 = block(3456, 270, 97, 1)
bg1Cpa25 = block(3161, 366, 97, 1)
bg1Cpa26 = block(2992, 424, 97, 1)
bg1Cpa27 = block(2987, 534, 97, 1)
bg1Cpa28 = block(3049, 791, 97, 1)
bg1Cpa29 = block(3195, 963, 97, 1)
bg1Cpa30 = block(3366, 936, 97, 1)
bg1Cpa31 = block(3537, 997, 97, 1)
bg1Cpa32 = block(3710, 1081, 97, 1)
bg1Cpa33 = block(3810, 1147, 97, 1)
bg1Cpa34 = block(3905, 1222, 97, 1)
bg1Cpa35 = block(2930, 214, 253, 1)
bg1Cpa36 = block(4231, 295, 110, 1)
bg1Cpa37 = block(3877, 369, 110, 1)
bg1Cpa38 = block(3580, 464, 110, 1)
bg1Cpa39 = block(3133, 627, 110, 1)
bg1Cpa40 = block(3372, 736, 110, 1)
bg1Cpa41 = block(3999, 709, 110, 1)
bg1Cpa42 = block(3669, 862, 110, 1)
bg1Cpa43 = block(4248, 883, 110, 1)
bg1Cpa44 = block(3204, 1044, 110, 1)
bg1Cpa45 = block(3987, 1088, 110, 1)
bg1Cpa46 = block(4543, 203, 17, 1)
bg1CdoorA1 = block(1320, 1, 40, 200)


# background 1C
bg1DdoorB1 = block(15, 150, 20, 300)
bg1ground1D = block(-670, 648, 6510, 1)
bg1DdoorA1 = block(1280, 1, 40, 200)
                                       
# bacground 2
bg2doorB1 = block(15, 550, 20, 200)
bg2groundB = block(0, 670, 1340, 1)
bg2pa1 = block(779, 600, 207, 1) # stone
bg2pa2 = block(866, 532, 123, 1) # first step
bg2pa3 = block(691, 460, 139, 1) # second step
bg2pa4 = block(908, 368, 600, 1) # roof
bg2doorA1 = block(1320, 585, 40, 100)
bg2doorA2 = block(1320, 368, 600, 1)
grasshop1 = Enemy(200, 600, 50, 95, 1250, 200)
Gargoyle1 = Enemy(500, 558, 50, 95, 1250, 500)

# background 3
bg3doorB1 = block(15, 550, 20, 200)
bg3groundB = block(0, 670, 1340, 1)
bg3doorA1 = block(1328, 600, 30, 80)                         # it doesnt look very good.....

# background 4
bg4doorB1 = block(15, 550, 20, 200)
bg4doorA1 = block(900, 0, 30, 800)
oldman = block(700, 585, 50, 95)

# background 5
bg5doorB1 = block(197, 567, 56, 123)
bg5pa1 = block(642, 572, 110, 23)
bg5pa2 = block(750, 478, 145, 210)
bg5pa3 = block(898, 570, 70, 23)
bg5pa4 = block(960, 366, 500, 1)
bg5doorA1 = block(1020, 650, 230, 50)
bg5doorA2 = block(1330, 190, 50, 200)

# background 6
bg6ground = block(670, 690, 6226, 1) #( -4176 - 670 = -4846 )  
bg6doorB1 = block(1200, 1 , 77, 15)
bg6doorA1 = block(341, 362 , 17, 133)
bg6doorA2 = block(1200, 292 , 66, 138)
bg6doorA3 = block(1200, 549 , 66, 138)

# background 7
bg7doorB1 = block(15, 514, 10, 180)
bg7doorA1 = block(1321, 529, 19, 161)

# background 8 -----------------------------------------------------
bg8ground = block(-670, 670, 12670, 1)  #size + 2050 , x -4000
bg8doorB1 = block(106, 530, 52, 160)
bg8pa1 = block(550, 487, 339, 1)
bg8pa2 = block(485, 401, 93, 1)
bg8pa3 = block(197, 221, 160, 1)
bg8pa4 = block(851, 351, 666 , 1)
bg8pa5 = block(1525, 465, 392, 1)
bg8pa6 = block(1553, 212, 214, 1)
bg8pa7 = block(1819, 96, 408, 1)
bg8pa8 = block(373, 306, 105, 1)
bg8pa9 = block(4331, 542, 304, 1)
bg8pa10 = block(4677, 440, 334, 1)
bg8pa11 = block(5059, 337, 348, 1)
bg8pa12 = block(5468, 214, 353, 1)
bg8pa13 = block(5762, 172, 691, 1)
bg8pa14 = block(6453, 418, 1110, 1)
bg8pa15 = block(7180, 296, 215, 1)
bg8pa16 = block(7394, 191, 169, 1)
bg8pa17 = block(7565, 166, 343, 1)
bg8pa18 = block(7805, 533, 163, 1)
bg8pa19 = block(7973, 418, 383, 1)
bg8pa20 = block(8707, 113, 170, 1)
bg8pa21 = block(9481, 98, 168, 1)
bg8pa22 = block(8912, 201, 136, 1)
bg8pa23 = block(9245, 209, 226, 1)
bg8pa24 = block(9079, 277, 133, 1)
bg8pa25 = block(8864, 392, 166, 1)
bg8pa26 = block(9108, 467, 148, 1)
bg8pa27 = block(9307, 526, 183, 1)
bg8pa28 = block(10297, 560, 141, 1)
bg8pa29 = block(10366, 472, 71, 1)
bg8pa30 = block(10271, 445, 31, 1)
bg8pa31 = block(10021, 427, 175, 1)
bg8pa32 = block(9689, 389, 378, 1)
bg8pa33 = block(9919, 269, 123, 1)
bg8pa34 = block(10005, 229, 602, 1)
bg8pa35 = block(10605, 257, 41, 1)
bg8pa36 = block(10646, 288, 47, 1)
bg8doorA1 = block(1300, 184, 29, 137)

# background 9
bg9doorB1 = block(1319, 363, 17, 127)

# background 10
bg10ground = block(670, 690, 6226, 1) #( -4176 - 670 = -4846 )
bg10doorB1 = block(1300, 316 , 66, 138)
bg10doorB2 = block(1300, 565 , 66, 138)
bg10doorA1 = block(1, 585 , 20, 100)

# background 11
bg11ground = block(0, 1340, 11000, 1) 
bg11doorB1 = block(1, 100 , 18, 79)
bg11doorA1 = block(1300, 300 , 151, 59)

# background 12
bg12ground = block(0, 2010, 6000, 1)
bg12doorB1 = block(1, 100 , 18, 79)
bg12doorA1 = block(1300, 221 , 200, 220)
bg12doorA2 = block(1000, 221 , 200, 220)

# background 13
bg13ground = block(0, 2026, 15000, 1) 
bg13doorB1 = block(1, 351 , 43, 110)
#bg13doorA1 = block(3885, 221 , 200, 220)

# background 15
bg15doorB1 = block(1, 585 , 20, 100)
bg15doorA1 = block(1300, 585 , 20, 100)

# background 16
bg16ground = block(0, 688, 3000, 1)
bg16doorB1 = block(1300, 585 , 20, 100)
bg16doorA1 = block(1, 585 , 20, 100)

# background 17
bg17doorB1 = block(1300, 585 , 20, 100)

# background 18
bg18ground = block(0, 670, 5000, 1)
bg18doorB1 = block(5, 535, 50, 160)
bg18doorA1 = block(1300, 495 , 30, 160)

# background 19
bg19ground = block(0, 3528, 9000, 1) 
bg19doorB1 = block(1, 585 , 20, 100)
bg19doorA1 = block(1300, 585 , 20, 100)

# background 20
bg20ground = block(0, 3528, 9000, 1) 
bg20doorB1 = block(1, 585 , 20, 100)
bg20doorA1 = block(1300, 585 , 20, 100)

# background 21
bg21ground = block(0, 5312, 12000, 1) 
bg21doorB1 = block(1, 585 , 20, 100)
bg21doorA1 = block(1300, 585 , 20, 100)
bg21doorA2 = block(1300, 185 , 20, 100)
bg21doorA3 = block(1000, 585 , 20, 100)

# background 22
bg22ground = block(0, 670, 4000, 1)
bg22doorB1 = block(1, 185 , 20, 100)
bg22doorA1 = block(1300, 585 , 20, 100)

# background 23
bg23doorB1 = block(1300, 185 , 20, 100)
bg23doorA1 = block(1300, 585 , 20, 100)

# background 24
bg24ground = block(0, 5312, 12000, 1) 
bg24doorB1 = block(1, 585 , 20, 100)

# background 31
bg31doorB1 = block(1300, 0 , 20, 100)
bg31doorA1 = block(1300, 585 , 20, 100)
#   ------------------------------------------- ====
#     ------ Classes Instances Lists ------------ =======
#   ------------------------------------------- ====
AlucardLeftHandItem = [item00]
AlucardRightHandItem = [item000]
AlucardHeadItem = [itemHead]
AlucardArmorItem = [itemBody]
AlucardAcessoryItem1 = [itemBody2] # cloaks
AlucardAcessoryItem2 = [itemBody3]
AlucardAcessoryItem3 = [itemBody4]

equipSelectionMenu = [(AlucardLeftHandItem[((len(AlucardLeftHandItem)) - 1)]), (AlucardRightHandItem[((len(AlucardRightHandItem)) - 1)]), (AlucardHeadItem[((len(AlucardHeadItem)) - 1)]), (AlucardArmorItem[((len(AlucardArmorItem)) - 1)]), (AlucardAcessoryItem1[((len(AlucardAcessoryItem1)) - 1)]), (AlucardAcessoryItem2[((len(AlucardAcessoryItem2)) - 1)]), (AlucardAcessoryItem3[((len(AlucardAcessoryItem3)) - 1)])]

#--------platforms---------
##platformsA = All platforms and all Grounds
platformsA = []
bg1platforms = [bg1pa1, bg1pa2, bg1pa3, bg1pa4, bg1pa5, bg1pa6, bg1pa7, bg1pa8]
for a in bg1platforms:
    platformsA.append(a)
bg1Bplatforms = [bg1Bpa1, bg1Bpa2, bg1Bpa3 ,bg1Bpa4, bg1Bpa5, bg1Bpa6, bg1Bpa7, bg1Bpa8, bg1Bpa9, bg1Bpa10, bg1Bpa11, bg1Bpa12, bg1Bpa13, bg1Bpa14, bg1Bpa15, bg1Bpa16, bg1Bpa17, bg1Bpa18, bg1Bpa19, bg1Bpa20, bg1Bpa21, bg1Bpa22, bg1Bpa23, bg1Bpa24, bg1Bpa25, bg1Bpa26, bg1Bpa27, bg1Bpa28, bg1Bpa29, bg1Bpa30, bg1Bpa31, bg1Bpa32, bg1Bpa33, bg1Bpa34, bg1Bpa35, bg1Bpa36, bg1Bpa37, bg1Bpa38, bg1Bpa39]
for a in bg1Bplatforms:
    platformsA.append(a)
for a in bg1Bplatforms:
    a.y -= 32
bg1Cplatforms = [bg1Cpa0, bg1Cpa1, bg1Cpa2, bg1Cpa3, bg1Cpa4, bg1Cpa5, bg1Cpa6, bg1Cpa7, bg1Cpa8, bg1Cpa9, bg1Cpa10, bg1Cpa11, bg1Cpa12, bg1Cpa13, bg1Cpa14, bg1Cpa15, bg1Cpa16, bg1Cpa17, bg1Cpa18, bg1Cpa19, bg1Cpa20, bg1Cpa21, bg1Cpa22, bg1Cpa23, bg1Cpa24, bg1Cpa25, bg1Cpa26, bg1Cpa27, bg1Cpa28, bg1Cpa29, bg1Cpa30, bg1Cpa31, bg1Cpa32, bg1Cpa33, bg1Cpa34, bg1Cpa35, bg1Cpa36, bg1Cpa37, bg1Cpa38, bg1Cpa39, bg1Cpa40, bg1Cpa41, bg1Cpa42, bg1Cpa43, bg1Cpa44, bg1Cpa45, bg1Cpa46]
for a in bg1Cplatforms: 
    platformsA.append(a)
#============================== Appendances BG1C
bg1Cpa47 = block(1000, 581.5, 1080, 21 ) 
bg1Cplatforms.append(bg1Cpa47) 
bg1Cpa48 = block(3289, 1043.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa48) 
bg1Cpa49 = block(4072, 1087.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa49) 
bg1Cpa50 = block(4333, 882.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa50) 
bg1Cpa51 = block(3751, 861.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa51) 
bg1Cpa52 = block(4077, 709.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa52) 
bg1Cpa53 = block(3457, 735.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa53) 
bg1Cpa54 = block(3213, 627.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa54) 
bg1Cpa55 = block(3663, 463.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa55) 
bg1Cpa56 = block(3963, 368.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa56) 
bg1Cpa57 = block(4316, 294.5, 150, 1 ) 
bg1Cplatforms.append(bg1Cpa57) 
bg1Cpa58 = block(3198, 863.5, 90, 1 ) 
bg1Cplatforms.append(bg1Cpa58)
#======================== BG1 D ==========================

bg1Dplatforms = []

bg1Dpa1 = block(0, 294.0, 111, 11 ) 
bg1Dplatforms.append(bg1Dpa1) 
bg1Dpa2 = block(4, 294.0, 111, 11 ) 
bg1Dplatforms.append(bg1Dpa2) 
bg1Dpa3 = block(106, 302.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa3) 
bg1Dpa4 = block(106, 300.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa4) 
bg1Dpa5 = block(103, 297.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa5) 
bg1Dpa6 = block(114, 302.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa6) 
bg1Dpa7 = block(115, 303.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa7) 
bg1Dpa8 = block(117, 306.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa8) 
bg1Dpa9 = block(119, 309.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa9) 
bg1Dpa10 = block(117, 305.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa10) 
bg1Dpa11 = block(123, 307.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa11) 
bg1Dpa12 = block(128, 311.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa12) 
bg1Dpa13 = block(125, 309.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa13) 
bg1Dpa14 = block(129, 310.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa14) 
bg1Dpa15 = block(135, 312.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa15) 
bg1Dpa16 = block(138, 314.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa16) 
bg1Dpa17 = block(142, 316.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa17) 
bg1Dpa18 = block(143, 317.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa18) 
bg1Dpa19 = block(153, 322.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa19) 
bg1Dpa20 = block(150, 320.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa20) 
bg1Dpa21 = block(147, 319.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa21) 
bg1Dpa22 = block(142, 317.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa22) 
bg1Dpa23 = block(138, 317.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa23) 
bg1Dpa24 = block(150, 321.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa24) 
bg1Dpa25 = block(152, 323.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa25) 
bg1Dpa26 = block(155, 325.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa26) 
bg1Dpa27 = block(158, 326.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa27) 
bg1Dpa28 = block(162, 327.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa28) 
bg1Dpa29 = block(165, 330.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa29) 
bg1Dpa30 = block(168, 331.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa30) 
bg1Dpa31 = block(173, 336.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa31) 
bg1Dpa32 = block(181, 339.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa32) 
bg1Dpa33 = block(195, 344.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa33) 
bg1Dpa34 = block(209, 348.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa34) 
bg1Dpa35 = block(216, 353.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa35) 
bg1Dpa36 = block(225, 360.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa36) 
bg1Dpa37 = block(233, 364.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa37) 
bg1Dpa38 = block(228, 361.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa38) 
bg1Dpa39 = block(210, 354.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa39) 
bg1Dpa40 = block(231, 361.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa40) 
bg1Dpa41 = block(238, 364.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa41) 
bg1Dpa42 = block(245, 369.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa42) 
bg1Dpa43 = block(256, 372.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa43) 
bg1Dpa44 = block(263, 376.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa44) 
bg1Dpa45 = block(270, 380.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa45) 
bg1Dpa46 = block(276, 382.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa46) 
bg1Dpa47 = block(288, 387.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa47) 
bg1Dpa48 = block(298, 391.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa48) 
bg1Dpa49 = block(308, 397.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa49) 
bg1Dpa50 = block(318, 399.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa50) 
bg1Dpa51 = block(326, 404.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa51) 
bg1Dpa52 = block(337, 410.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa52) 
bg1Dpa53 = block(347, 414.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa53) 
bg1Dpa54 = block(355, 417.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa54) 
bg1Dpa55 = block(360, 420.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa55) 
bg1Dpa56 = block(371, 425.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa56) 
bg1Dpa57 = block(375, 426.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa57) 
bg1Dpa58 = block(380, 427.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa58) 
bg1Dpa59 = block(386, 430.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa59) 
bg1Dpa60 = block(389, 432.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa60) 
bg1Dpa61 = block(391, 434.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa61) 
bg1Dpa62 = block(393, 435.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa62) 
bg1Dpa63 = block(404, 440.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa63) 
bg1Dpa64 = block(411, 444.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa64) 
bg1Dpa65 = block(416, 447.0, 21, 11 ) 
bg1Dplatforms.append(bg1Dpa65) 

bg4_leftWalls = []
bg4_rightWalls = []

#===================================================
bg8platforms = [bg8pa1, bg8pa2, bg8pa3, bg8pa4, bg8pa5, bg8pa6, bg8pa7, bg8pa8, bg8pa9, bg8pa10, bg8pa11, bg8pa12, bg8pa13, bg8pa14, bg8pa15, bg8pa16, bg8pa17, bg8pa18, bg8pa19, bg8pa20, bg8pa21, bg8pa22, bg8pa23, bg8pa24, bg8pa25, bg8pa26, bg8pa27, bg8pa28, bg8pa29, bg8pa30, bg8pa31, bg8pa32, bg8pa33, bg8pa34, bg8pa35, bg8pa36]
for a in bg8platforms:
    platformsA.append(a)
#-----------walls-----------------
leftWalls = [bg1wl1, bg1wl2, bg2wl1, bg2wl2, bg2wl3, bg2wl4, bg2wl5, bg2wl6, bg2wl7, bg2wl8, bg2wl9, bg2wl10, bg2wl11, bg2wl12, bg2wl13, bg2wl14]
rightWalls = [bg1wr1, bg1wr2, bg2wr1, bg2wr2, bg2wr3, bg2wr4, bg2wr5, bg2wr6, bg2wr7, bg2wr8, bg2wr9, bg2wr10, bg2wr11, bg2wr12, bg2wr13, bg2wr14]
# LEFT WALLS ARE THE ONES COLLIDING WITH THE RIGHT RECT COLLIDER OF THE PLAYER. RIGHT IS OPPOSITE.
bg1_leftWalls = [bg1wl1, bg1wl2]
bg1_rightWalls = [bg1wr1, bg1wr2]

bg2_leftWalls = [bg2wl1, bg2wl2, bg2wl3, bg2wl4, bg2wl5, bg2wl6, bg2wl7, bg2wl8, bg2wl9, bg2wl10, bg2wl11, bg2wl12, bg2wl13, bg2wl14]
bg2_rightWalls = [bg2wr1, bg2wr2, bg2wr3, bg2wr4, bg2wr5, bg2wr6, bg2wr7, bg2wr8, bg2wr9, bg2wr10, bg2wr11, bg2wr12, bg2wr13, bg2wr14]

bg3_leftWalls = []
bg1Cwl1 = block(892, 321, 21, 240 ) 
bg3_leftWalls.append(bg1Cwl1) 
bg1Cwl2 = block(2001, 285.5, 21, 310 ) 
bg3_leftWalls.append(bg1Cwl2) 
bg1Cwl3 = block(2734, -1.5, 21, 610 ) 
bg3_leftWalls.append(bg1Cwl3) 
bg1Cwl4 = block(2734, 452.5, 21, 400 ) 
bg3_leftWalls.append(bg1Cwl4) 
bg1Cwl5 = block(2081, 814.5, 18, 92 ) 
bg3_leftWalls.append(bg1Cwl5) 
bg1Cwl6 = block(336, 848.5, 18, 95 ) 
bg3_leftWalls.append(bg1Cwl6) 
bg1Cwl7 = block(932, 942.5, 18, 46 ) 
bg3_leftWalls.append(bg1Cwl7) 
bg1Cwl8 = block(923, 926.5, 58, 26 ) 
bg3_leftWalls.append(bg1Cwl8) 
bg1Cwl9 = block(2733, 870.5, 18, 190 ) 
bg3_leftWalls.append(bg1Cwl9) 
bg1Cwl10 = block(2725, 887.5, 108, 30 ) 
bg3_leftWalls.append(bg1Cwl10) 
for a in bg3_leftWalls:
    leftWalls.append(a)
    
bg3_rightWalls = []
bg1Cwr1 = block(1007, 320.5, 21, 280 ) 
bg3_rightWalls.append(bg1Cwr1) 
bg1Cwr2 = block(1003, 574.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr2) 
bg1Cwr3 = block(998, 566.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr3) 
bg1Cwr4 = block(995, 562.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr4) 
bg1Cwr5 = block(991, 559.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr5) 
bg1Cwr6 = block(988, 554.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr6) 
bg1Cwr7 = block(986, 552.5, 41, 11 ) 
bg3_rightWalls.append(bg1Cwr7) 
bg1Cwr8 = block(2114, 299.5, 21, 231 ) 
bg3_rightWalls.append(bg1Cwr8) 
bg1Cwr9 = block(2109, 295.5, 21, 11 ) 
bg3_rightWalls.append(bg1Cwr9) 
bg1Cwr10 = block(2106, 291.5, 21, 11 ) 
bg3_rightWalls.append(bg1Cwr10) 
bg1Cwr11 = block(2489, 506.0, 21, 131 ) 
bg3_rightWalls.append(bg1Cwr11) 
bg1Cwr12 = block(948, 848.0, 21, 51 ) 
bg3_rightWalls.append(bg1Cwr12) 
bg1Cwr13 = block(0, 632.0, 21, 471 ) 
bg3_rightWalls.append(bg1Cwr13) 
bg1Cwr14 = block(0, 631.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr14) 
bg1Cwr15 = block(3, 626.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr15) 
bg1Cwr16 = block(6, 623.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr16) 
bg1Cwr17 = block(9, 622.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr17) 
bg1Cwr18 = block(10, 619.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr18) 
bg1Cwr19 = block(17, 616.0, 21, 21 ) 
bg3_rightWalls.append(bg1Cwr19) 
bg1Cwr20 = block(0, 945.0, 19, 401 ) 
bg3_rightWalls.append(bg1Cwr20) 
bg1Cwr21 = block(2086, 905.0, 19, 90 ) 
bg3_rightWalls.append(bg1Cwr21) 
bg1Cwr22 = block(2087, 897.0, 19, 30 ) 
bg3_rightWalls.append(bg1Cwr22) 
bg1Cwr23 = block(2093, 892.0, 19, 30 ) 
bg3_rightWalls.append(bg1Cwr23) 
bg1Cwr24 = block(2096, 888.0, 19, 30 ) 
bg3_rightWalls.append(bg1Cwr24) 
bg1Cwr25 = block(2101, 884.0, 19, 30 ) 
bg3_rightWalls.append(bg1Cwr25) 
bg1Cwr26 = block(2106, 880.0, 19, 30 ) 
bg3_rightWalls.append(bg1Cwr26) 
bg1Cwr27 = block(2912, 420.0, 19, 642 ) 
bg3_rightWalls.append(bg1Cwr27)
bg1Cwr28 = block(2880, -7.5, 50, 690 ) 
bg3_rightWalls.append(bg1Cwr28) 
for a in bg3_rightWalls:
    rightWalls.append(a)

#======================= BG1D WALLS=================================
bg4_leftWalls = []
##for a in bg4_leftWalls:
##    leftWalls.append(a)





bg4_rightWalls = []
##for a in bg4_rightWalls:
##    rightWalls.append(a)


#-------------others-------------------------------------------------------
grounds = [bg1ground, bg1ground1B, bg1ground1C, bg1ground1D, bg6ground, bg8ground, bg10ground, bg11ground, bg12ground, bg13ground, bg16ground, bg18ground, bg19ground, bg20ground, bg21ground, bg22ground, bg24ground]
doors = [bg1doorA1, bg1BdoorA1, bg1CdoorA1, bg1DdoorA1, bg2doorA1, bg2doorA2, bg3doorA1, bg4doorA1, bg5doorA1, bg5doorA2, bg7doorA1, bg6doorA1, bg6doorA2, bg6doorA3, bg8doorA1, bg10doorA1, bg11doorA1, bg12doorA1, bg12doorA2, bg16doorA1, bg18doorA1, bg19doorA1, bg20doorA1, bg21doorA1, bg21doorA2, bg22doorA1, bg23doorA1, bg31doorA1]
doorsB = [bg1BdoorB1, bg2doorB1, bg1CdoorB1, bg1DdoorB1, bg3doorB1, bg4doorB1, bg5doorB1,bg6doorB1, bg7doorB1, bg8doorB1, bg9doorB1, bg18doorB1, bg10doorB1, bg10doorB2, bg11doorB1, bg12doorB1, bg13doorB1, bg18doorB1, bg19doorB1, bg20doorB1, bg21doorB1, bg24doorB1, bg16doorB1, bg17doorB1, bg22doorB1, bg23doorB1, bg31doorB1]

# Misc lists
candles = [bg1CD1, bg1CD2, bg1CD3, bg1CD4, bg1CD5]
allHearts = [bg1HT1, bg1HT2, bg1HT3, bg1HT4, bg1HT5]
itemsList = [item001, item002, item003, item004, item005, item006, item007, item008, item009, item0010, item0011, item0012, item0013, item0014, item0015, item0016, item0017, item0018, item0019, item0020]

# enemies lists
skeletons = [skeleton1, skeleton2, skeleton3, skeleton4, skeleton5]
Gargoyles = [Gargoyle1]
tigers = [Tiger1, Tiger2, Tiger3, Tiger4, Tiger5]
bgCtigers = [Tiger6, Tiger7, Tiger8, Tiger9, Tiger10]
grasshoppers = [grasshop1]
# end of enemies list with all enemies on a list
enemies = [skeletons, tigers, Gargoyles, grasshoppers]

#========================================================
#   ------------------------------------------- ====
#     ------ Loading Variables ------------ =======
#   ------------------------------------------- ====
#========================================================
Loading_information = [AlucardExp, AlucardNextLevel, TIME.hours, TIME.minutes, TIME.seconds, AlucardLevel, AlucardGold, AlucardKill, AlucardRooms, Alucardhealth, AlucardMP, AlucardHearts, AlucardATK, AlucardATK2, AlucardDEF, AlucardSTR, AlucardLCK, AlucardCON, AlucardINT, bgX, bgXmountain, bg1BX, bg1BXmountain, bg1BY, bg1CX, bg1CXmountain, bg1CY, bgX2, bgX3, bgX4, bgX5, bgX6, bgY6, bgX7, bgX8, bgX9, bgX10, bgX11, bgX12, bgX13, bgX14, man.x, man.y]
Loading_Main_Menu = True
unloading_Main_Menu = False

#======================================================================================================================================================================
#======================================================================================================================================================================
#============= MAIN LOOP ==============================================================================================================================================
#======================================================================================================================================================================
#======================================================================================================================================================================
NNN = 8 #2 Is good for selection menu #3 is good for Main Menu
#====================================================================== debugging variables
PAUSED = False # DEBUGGING
debug_lines = None
pixel_ruler = None
debug_lines_load = True
ruler_on = False
grid_on = False
c0 = 0
c1 = 0
c2 = 0
c0done = False
c1done = False
c2done = False
pa_number = 0 # APPENDER
platforms_list = []
instructionsOn = False
selected_height = 50
selected_width = 50
fast_rect_increase_on = True
rect_increasing_variable_tick = 0
windows_copy = win.copy()
#pygame.mixer.music.stop()
#pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
#pygame.mixer.music.play(-1)

#==================================================================
previous_key = pygame.key.get_pressed()
while run:
    keys = pygame.key.get_pressed()
    #===== FOR DEBUGGING PURPOSES ================
    konami = False
    main_menu = False
    windows_copy = win.copy()
    mouse = pygame.mouse.get_pos()
    x = mouse[0]
    y = mouse [1]
    mouseRect = pygame.Rect(int(x), int(y), int(1), int(1))
    try:
        w = win.get_at((x,y))# takes the color that is at the coordinates x and y
    except IndexError:
        pass
    if keys[pygame.K_m] and not previous_key[pygame.K_m]:
        print(x,y) #print (x,y) to print just coordinates //// print (w,y,x) to print colors as well.
    if keys[pygame.K_p] and not previous_key[pygame.K_p]:
        PAUSED = True
        debug_lines_load = True
########rect = pygame.Rect(25, 25, 100, 50) # Saves a part of the screen as screenshot
########sub = screen.subsurface(rect)
########pygame.image.save(sub, "screenshot.jpg")
    while PAUSED:#===================================
        clock.tick(gameSpeed)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse [1]
        mouseRect = pygame.Rect(int(x), int(y), int(1), int(1))
        try:
            w = win.get_at((x,y))# takes the color that is at the coordinates x and y
        except IndexError:
            pass
        if keys[pygame.K_y]:
            print (w,x,y)
            
        if keys[pygame.K_u] and not previous_key[pygame.K_u]:
            #print (w,x,y)
            print (((bg1CX -(bg1CX*2)) + x), (bg1CY -(bg1CY*2)) +y)
        color_and_position = str(((bg1CX -(bg1CX*2)) + x,(bg1CY -(bg1CY*2)) +y,w))
        win.blit(windows_copy, (0,0))
        

        if debug_lines_load == True:
            debug_lines = pygame.image.load(f'DEBUGGING/grid.png').convert_alpha()
            pixel_ruler = pygame.image.load(f'DEBUGGING/pixel ruler.png').convert()
            debug_lines_load = False
            windows_copy = win.copy()
        win.blit(windows_copy, (0,0))
        if keys[pygame.K_k] and not previous_key[pygame.K_k]:
            if grid_on == True:
                grid_on = False
            else:
                grid_on = True
        if grid_on == True:
            win.blit(debug_lines, (0,0))


        rect_increasing_variable_tick += 1
        if rect_increasing_variable_tick == 7:
            rect_increasing_variable_tick = 0

        if keys[pygame.K_x] and not previous_key[pygame.K_x]:
            if fast_rect_increase_on == True:
                fast_rect_increase_on = False
            else:
                fast_rect_increase_on = True
            
        if keys[pygame.K_w]:
            if fast_rect_increase_on == True:
                selected_height -= 1
            else:
                if rect_increasing_variable_tick == 0:
                    selected_height -= 1
        if keys[pygame.K_s]:
            if fast_rect_increase_on == True:
                selected_height += 1
            else:
                if rect_increasing_variable_tick == 0:
                    selected_height += 1
        if keys[pygame.K_a]:
            if fast_rect_increase_on == True:
                selected_width -= 1
            else:
                if rect_increasing_variable_tick == 0:
                    selected_width -= 1
        if keys[pygame.K_d]:
            if fast_rect_increase_on == True:
                selected_width += 1
            else:
                if rect_increasing_variable_tick == 0:
                    selected_width += 1
        if keys[pygame.K_UP]:
            if fast_rect_increase_on == True:
                selected_height -= 10
            else:
                if rect_increasing_variable_tick == 0:
                    selected_height -= 10
        if keys[pygame.K_DOWN]:
            if fast_rect_increase_on == True:
                selected_height += 10
            else:
                if rect_increasing_variable_tick == 0:
                    selected_height += 10
        if keys[pygame.K_LEFT]:
            if fast_rect_increase_on == True:
                selected_width -= 10
            else:
                if rect_increasing_variable_tick == 0:
                    selected_width -= 10
        if keys[pygame.K_RIGHT]:
            if fast_rect_increase_on == True:
                selected_width += 10
            else:
                if rect_increasing_variable_tick == 0:
                    selected_width += 10
                    
        if selected_height <= 0:
            selected_height = 1
        if selected_width <= 0:
            selected_width = 1
            
##            selected_height = int(input('CHOOSE RECT HEIGHT: '))
##            selected_width = int(input('CHOOSE RECT WIDTH: '))
        if keys[pygame.K_v] and not previous_key[pygame.K_v]:
            with open( "floors.py", "w" ) as f:
                pa_number +=1
                platforms_list.append('bg1Dpa'+(str(pa_number)) + ' = block(' + (str(((bg1DX -(bg1DX*2)) + x))) + ', ' + (str((bg1DY -(bg1DY*2)) +y)) + ', ' + (str(selected_width)) + ', ' + (str(selected_height)) + ' ) \n' + ('bg1Dplatforms.append(bg1Dpa') +(str(pa_number)) + (') \n'))
                for i in range(len(platforms_list)):
                    f.write(str(platforms_list[i]))
                    print(platforms_list[i])
##                pa_number +=1
##                platforms_list.append('bg1Dwr'+(str(pa_number)) + ' = block(' + (str(((bg1DX -(bg1DX*2)) + x))) + ', ' + (str((bg1DY -(bg1DY*2)) +y)) + ', ' + (str(selected_width)) + ', ' + (str(selected_height)) + ' ) \n' + ('bg4_rightWalls.append(bg1Dwr') +(str(pa_number)) + (') \n'))
##                for i in range(len(platforms_list)):
##                    f.write(str(platforms_list[i]))
##                    print(platforms_list[i])
        if keys[pygame.K_i] and not previous_key[pygame.K_i]:
            if ruler_on == True:
                ruler_on = False
            else:
                ruler_on = True
        if ruler_on == True:
            c0 += 1
            c1 += 1
            c2 += 1
            if c0 >= 240:
                c0done = True
            if c0 <= 20:
                c0done = False
            if c0done == True:
                c0 -= 3
            else:
                c0 += 3
            if c1 >= 240:
                c1done = True
            if c1 <= 20:
                c1done = False
            if c1done == True:
                c1 -= 4
            else:
                c1 += 4
            if c2 >= 240:
                c2done = True
            if c2 <= 20:
                c2done = False
            if c2done == True:
                c2 -= 2
            else:
                c2 += 2
            rect_mold = pygame.Rect( x, y, selected_width, selected_height)
            #pygame.draw.line(win, (100,255,45), [x - 250, y +10], [x + 250, y +10], 1)
            win.blit((font4.render((color_and_position), 1, (c0,c1,c2))), (x,y +60))
            pygame.draw.rect(win, (255,0,0), rect_mold,2)
        else:
            win.blit(pixel_ruler, (x -200,y+10))
            
        win.blit((font4.render(('Paused'), 1, (15,5,5))), (605,305))
        win.blit((font4.render(('Paused'), 1, (30,10,10))), (602,302))
        win.blit((font4.render(('Paused'), 1, (211,211,211))), (600,300))
        pygame.display.flip()
        if keys[pygame.K_o] and not previous_key[pygame.K_o]:
            PAUSED = False
            pixel_ruler = None
            debug_lines = None
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
                run = False
                main_menu = False
                konami = False
                PAUSED = False
        if keys[pygame.K_f] and not previous_key[pygame.K_f]:
            fullscreen = not fullscreen
            if fullscreen:
                win = pygame.display.set_mode((1340, 690), pygame.FULLSCREEN)
            else:
                win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)
        if keys[pygame.K_ESCAPE] and not previous_key[pygame.K_ESCAPE]:
            win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
            run = False
            main_menu = False
            konami = False
            PAUSED = False
        if keys[pygame.K_n] and not previous_key[pygame.K_n]:
            man.draw(win)
            man.x = 35
            man.y = 565
            background1B = False
            background1D = True
            background1 = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/1.wav')
            pygame.mixer.music.play(-1)
        previous_key = keys
    #====================================================================================================
    while konami:
        gif += 1
        if gif == 3*6:
            gif = 0
        pygame.display.set_icon(pygame.image.load(f'DATA/GRAPHICS/ICON/0.png').convert_alpha())
        pygame.display.set_icon(icon[gif//6])
        if konami_init == True:
            KONAM = [pygame.image.load(f'DATA/GRAPHICS/KONAMI/a ({i}).png').convert_alpha() for i in range(52)]
            KONAMI = [pygame.transform.scale(a, (1340, 690)) for a in KONAM]
            konami_init = False

        konami_logo_drawing_window()
        clock.tick(gameSpeed)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
                run = False
                main_menu = False
                konami = False
        if keys[pygame.K_f] and not previous_key[pygame.K_f]:
            fullscreen = not fullscreen
            if fullscreen:
                win = pygame.display.set_mode((1340, 690), pygame.FULLSCREEN)
            else:
                win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)
        if keys[pygame.K_ESCAPE] and not previous_key[pygame.K_ESCAPE]:
            win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
            run = False
            main_menu = False
            konami = False
        previous_key = keys
    #====================== MAIN MENU ==========================================================            
    while main_menu and konami == False:
        gif += 1
        if gif == 3*6:
            gif = 0
        pygame.display.set_icon(pygame.image.load(f'DATA/GRAPHICS/ICON/0.png').convert_alpha())
        pygame.display.set_icon(icon[gif//6])
        if Loading_Main_Menu == True:
            KONAMI = None
            main_Menu_Display = [pygame.image.load(f'DATA/GRAPHICS/MENUS/MAIN MENU/a ({i}).png').convert_alpha() for i in range(28)]
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/Moonlight Nocturne.wav')
            pygame.mixer.music.play(-1)
            Loading_Main_Menu = False

        main_menu_drawing_window()
        clock.tick(gameSpeed)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
                run = False
                main_menu = False
        if keys[pygame.K_f] and not previous_key[pygame.K_f]:
            fullscreen = not fullscreen
            if fullscreen:
                win = pygame.display.set_mode((1340, 690), pygame.FULLSCREEN)
            else:
                win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)
        if keys[pygame.K_ESCAPE] and not previous_key[pygame.K_ESCAPE]:
            win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
            run = False
            main_menu = False
        if keys[pygame.K_DOWN] and not previous_key[pygame.K_DOWN] or keys[pygame.K_s] and not previous_key[pygame.K_s]:
            SOUNDS_TICK[NNN].play()
            if main_Menu_instance.y2 <= 399:
                main_Menu_instance.y2 += 50
            else:
                main_Menu_instance.y2 = 300
        if keys[pygame.K_UP] and not previous_key[pygame.K_UP] or keys[pygame.K_w] and not previous_key[pygame.K_w]:
            SOUNDS_TICK[NNN].play()
            if main_Menu_instance.y2 >= 301:
                main_Menu_instance.y2 -= 50
            else:
                main_Menu_instance.y2 = 400


        if main_Menu_instance.hitbox.colliderect(main_Menu_instance.newGameHitbox):
            main_Menu_instance.ColorsA = (211,25,25)
            if keys[pygame.K_KP_ENTER] and not previous_key[pygame.K_KP_ENTER] or keys[pygame.K_RETURN] and not previous_key[pygame.K_RETURN]:
                SOUNDS_A[27].play()
                main_menu = False
                unloading_Main_Menu = True
        else:
            main_Menu_instance.ColorsA = (211,211,211)
        if main_Menu_instance.hitbox.colliderect(main_Menu_instance.continuarHitbox):
            main_Menu_instance.ColorsB = (211,25,25)
            if keys[pygame.K_KP_ENTER] and not previous_key[pygame.K_KP_ENTER] or keys[pygame.K_RETURN] and not previous_key[pygame.K_RETURN]:
                SOUNDS_A[27].play()
                main_menu = False
                unloading_Main_Menu = True
                [AlucardExp, AlucardNextLevel, TIME.hours, TIME.minutes, TIME.seconds, AlucardLevel, AlucardGold, AlucardKill, AlucardRooms, Alucardhealth, AlucardMP, AlucardHearts, AlucardATK, AlucardATK2, AlucardDEF, AlucardSTR, AlucardLCK, AlucardCON, AlucardINT] = pickle.load( open( "DATA/SAVE/save.p", "rb" ) )
                for a in Loading_information:
                    print(a)
        else:
            main_Menu_instance.ColorsB = (211,211,211)
        if main_Menu_instance.hitbox.colliderect(main_Menu_instance.quitHitbox):
            main_Menu_instance.ColorsC = (211,25,25)
            if keys[pygame.K_KP_ENTER] and not previous_key[pygame.K_KP_ENTER] or keys[pygame.K_RETURN] and not previous_key[pygame.K_RETURN]:
                SOUNDS_A[27].play()
                main_menu = False
                run = False
                win = pygame.display.set_mode((1, 1), pygame.RESIZABLE)
        else:
            main_Menu_instance.ColorsC = (211,211,211)
        previous_key = keys
        
        #===================== UNLOADING MENU IMAGES ================================
    if unloading_Main_Menu == True:
        main_Menu_Display = None
        win = pygame.display.set_mode((1340, 690), pygame.FULLSCREEN)
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
        pygame.mixer.music.play(-1)
        unloading_Main_Menu = False
        
    #================================================================================   
    gif += 1
    if gif == 3*6:
        gif = 0
    pygame.display.set_icon(pygame.image.load(f'DATA/GRAPHICS/ICON/0.png').convert_alpha())
    pygame.display.set_icon(icon[gif//6])
    redrawGameWindow()
    Loading_Gallery = None
    clock.tick(gameSpeed)
    scroll[0] = int(scroll[0])
    scroll[0] += int(man.x - scroll[0])
    player.gravity(man)
    
#==========================================================
#==========================================================
#============ HEART RELATION ==============================
#==========================================================
#============== TYPE 1 ====================================
    if bg1CD1.flameOn == False:
        bg1HT1.awaken = True
    if bg1CD2.flameOn == False:
        bg1HT2.awaken = True
    if bg1CD3.flameOn == False:
        bg1HT3.awaken = True
    if bg1CD4.flameOn == False:
        bg1HT4.awaken = True
    if bg1CD5.flameOn == False:
        bg1HT5.awaken = True
#=========================================================================================================
#=========================================================================================================
#============ COLLISIONS =================================================================================
#=========================================================================================================
#============== CANDLE ===================================================================================
    for d in candles:
            if man.atkbox.colliderect(d.hitbox):
                if man.attacking == True and man.attackCount + 1 >= 3 and man.attackCount <= 4 or man.crouchATK == True and man.crouchATKcount + 1 >= 3 and man.crouchATKcount <= 4:
                      d.hit()
                  
#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================ HEART ========================
    for d in allHearts:
        if d.visible == True:
            if man.hitbox.colliderect(d.hitbox):
                  if d.got == False:
                      AlucardHearts += 1
                      d.hit()

#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================ WALLS ========================

    Touching_left_wall = False
    for a in leftWalls:
        if a.visible == True:
            if man.rightcollider.colliderect(a.hitbox):
                Touching_left_wall = True

    Touching_right_wall = False
    for a in rightWalls:
        if a.visible == True:
            if man.leftcollider.colliderect(a.hitbox):
                Touching_right_wall = True

#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================ ITEMS ========================
    descWinImg = blankItem[0]
    descWinDesc = blankItem[0]
    for b in itemsList:
        for a in platformsA:
            if b.hitbox.colliderect(a.hitbox):# when the item collides with the floor.
                if a.visible:
                      b.y = a.y - 39

        if b.hitbox.colliderect(man.hitbox):# when the item collides with Alucard.
            if b.visible:
                  b.gotItem()

        if theHover.hitbox.colliderect(b.desccriptionBox):# when on the inventory menu, you select an item , it will show the item's decription.
            descWinImg = b.imgBig
            descWinDesc = b.description
            if keys[pygame.K_KP0] and not previous_key[pygame.K_KP0]:
                b.equipItem()
#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================= MENU ========================   
    for a in equipSelectionMenu:
        if AllParallaxes.equipHoverbox.colliderect(a.equipHoverbox):# when on the Equipment selection menu, you select an slot , it will show the alot's decription.
            if AlucardInventoryOn == False:
                descWinImg = a.imgBig
                descWinDesc = a.description
                if equipHoverY == 52:
                    descWinImg = ((AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))])).imgBig
                    descWinDesc = ((AlucardLeftHandItem[((len(AlucardLeftHandItem) - 1))])).description
                if equipHoverY == 94:
                    descWinImg = ((AlucardRightHandItem[((len(AlucardRightHandItem) - 1))])).imgBig
                    descWinDesc = ((AlucardRightHandItem[((len(AlucardRightHandItem) - 1))])).description
                 
#===============================================
#===============================================
#============== LEVEL UP =======================
#===============================================
#===============================================
    if AlucardNextLevel <= 1:
        AlucardLevel += 1
        AlucardNextLevel = (AlucardNextLevel + (AlucardLevel * 137))
        AlucardMaxHealth = ((AlucardLevel * 17) + 91 )
        AlucardMaxMp = ((AlucardLevel * 3) + 7 )
        AlucardSTR = ((AlucardLevel * 1) + 9)
        AlucardLCK = ((AlucardLevel * 1) + 9)
        AlucardCON = ((AlucardLevel * 1) + 9)
        AlucardINT = ((AlucardLevel * 1) + 9)
            
#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================ ENEMIES ======================
    Enemy_collision(skeletons)
    Enemy_collision(tigers)
    Enemy_collision(grasshoppers)
    Enemy_collision(Gargoyles)

#===============================================
#===============================================
#===============================================
#===============================================
#================ ENDGAME ======================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            run = False
                    
#================================================================
#================================================================
#=============== COLLISIONS ===================== NPCS's ========
#================================================================
#================ OLD MAN =======================================
    if man.hitbox.colliderect(oldman.hitbox):
              if background4 == True:
                  AlucardSpeech01SOUND.play()
                  Alucardspeech01 = True
                  
#======================================================================================================================
#======================================================================================================================
#=============== COLLISIONS ====================== DOORS ==============================================================
#======================================================================================================================
#=============== bg1doorA1 ============================================================================================
##    bg_door(bg1doorA1, background1, background1B, 35, 100, 1)
##    print(background1B)
    if door_tick <=59:
        door_tick += 1
    else:
        door_tick = 60

    if man.hitbox.colliderect(bg1doorA1.hitbox):
              if background1 == True:
                      #man.draw(win)
                      man.x = 35
                      man.y = 100
                      background1B = True
                      background3 = False
                      background1 = False
                      pygame.mixer.music.stop()
                      pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/1.wav')
                      pygame.mixer.music.play(-1)

#=============== bg1BdoorB1 =====================
    if man.hitbox.colliderect(bg1BdoorB1.hitbox):
              if background1B == True:
                  #man.draw(win)
                  man.x = 1250
                  man.y = 585
                  background1B = False
                  background1 = True
                  pygame.mixer.music.stop()
                  pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
                  pygame.mixer.music.play(-1)

#=============== bg1BdoorA1 =====================
    if man.hitbox.colliderect(bg1BdoorA1.hitbox):
              if background1B == True:
                  #man.draw(win)
                  man.x = 35
                  man.y = 585
                  background1C = True
                  Loading()
                  grasshopper = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GRASSHOPPER/WALK/Z{i}.png').convert_alpha() for i in range(8)]
                  grasshopperWalkR = [pygame.transform.flip(a, True, False) for a in grasshopper]
                  grasshopperAttack = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GRASSHOPPER/ATK/ZA{i}.png').convert_alpha() for i in range(6)]
                  grasshopperAttackR = [pygame.transform.flip(a, True, False) for a in grasshopperAttack]
                  #GARGOYLE
                  gargoyleWalk = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GARGOYLE/WALK/{i}.png').convert_alpha() for i in range(5)]
                  gargoyleWalkLeft = [pygame.transform.flip(a, True, False) for a in gargoyleWalk]
                  gargoyleAtk = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GARGOYLE/ATK/{i}.png').convert_alpha() for i in range(3)]
                  gargoyleAtkLeft = [pygame.transform.flip(a, True, False) for a in gargoyleAtk]
                  background1B = False

#=============== bg1CdoorB1 =====================
    if man.hitbox.colliderect(bg1CdoorB1.hitbox):
              if background1C == True:
                  #man.draw(win)
                  man.x = 1250
                  man.y = 585
                  background1C = False
                  Loading_2()
                  background1B = True

#=============== bg1CdoorA1 =====================
    if man.hitbox.colliderect(bg1CdoorA1.hitbox) and door_tick == 60:
              if background1C == True:
                  #man.draw(win)
                  man.x = 35
                  man.y = 585
                  background1C = False
                  background1D = True
                  door_tick = 0
    
#=============== bg1DdoorB1 =====================
    if man.hitbox.colliderect(bg1DdoorB1.hitbox) and door_tick == 60:
              if background1D == True:
                  man.x = 1250
                  man.y = 585
                  background1D = False
                  background1C = True
                  door_tick = 0

#=============== bg1DdoorA1 =====================
    if man.hitbox.colliderect(bg1DdoorA1.hitbox) and door_tick == 60:
              if background1D == True:
                  man.x = 35
                  man.y = 585
                  background1D = False
                  background2 = True
                  door_tick = 0

#=============== bg2doorB1 =====================
    if man.hitbox.colliderect(bg2doorB1.hitbox):
              if background2 == True:
                  #man.draw(win)
                  man.x = 1250
                  man.y = 585
                  background2 = False
                  background1C = True
                  pygame.mixer.music.stop()
                  pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
                  pygame.mixer.music.play(-1)
                  
#=============== bg2doorA1 =====================
    if man.hitbox.colliderect(bg2doorA1.hitbox):
              if background2 == True:
                  #man.draw(win)
                  man.x = 35
                  man.y = 585
                  background3 = True
                  background2 = False
                  background4 = False
                  #theBg3Pillars.Bg3Pillars = True

#=============== bg2doorA2 =====================
    if man.hitbox.colliderect(bg2doorA2.hitbox):
              if background2 == True:
                  #man.draw(win)
                  man.x = 35
                  man.y = 585
                  background18 = True
                  background2 = False
                  background4 = False
                      
#=============== bg3doorB1 =====================
    if man.hitbox.colliderect(bg3doorB1.hitbox):
              if background3 == True:
                  #man.draw(win)
                  man.x = 1257
                  man.y = 585
                  background2 = True
                  background3 = False
                  #theBg3Pillars.Bg3Pillars = False
   
#================ bg3doorA1 ====================
    if man.hitbox.colliderect(bg3doorA1.hitbox):
              if background3 == True:
                  if background4 == False:
                      #man.draw(win)
                      man.x = 35
                      man.y = 585
                      background3 = False
                      background5 = False
                      Loading()
                      bg1 = None
                      bg1B = None
                      bg1C = None
                      bg2 = None
                      bg3 = None
                      bg4 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "5.png")).convert_alpha()
                      bg5 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "6.png")).convert_alpha()
                      bg6 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "7.png")).convert_alpha()
                      bg7 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "8.png")).convert_alpha()
                      bg8 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "9.png")).convert_alpha()
                      NPCS = [pygame.image.load(f'DATA/GRAPHICS/NPCS/{i}.png').convert_alpha() for i in range(3)]
                      background4 = True
                      #theBg3Pillars.Bg3Pillars = False

#=============== bg4doorB1 =====================
    if man.hitbox.colliderect(bg4doorB1.hitbox):
              if background4 == True:
                  #man.draw(win)
                  man.x = 1265
                  man.y = 585
                  background4 = False
                  Loading()
                  bg1 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "0.png")).convert_alpha()
                  bg1B = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "1.png")).convert_alpha()
                  bg1C = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "2.png")).convert_alpha()
                  bg2 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "3.png")).convert_alpha()
                  bg3 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "4.png")).convert_alpha()
                  bg4 = None
                  bg5 = None
                  bg6 = None
                  bg7 = None
                  bg8 = None
                  NPCS = None
                  background3 = True
                  #theBg3Pillars.Bg3Pillars = True

#=============== bg4doorA1 =====================
    if man.hitbox.colliderect(bg4doorA1.hitbox):
              if background4 == True:
                  if background5 == False:
                      #man.draw(win)
                      man.x = 261
                      man.y = 585
                      background5 = True
                      background4 = False
                      background6 = False

#=============== bg5doorB1 =====================
    if man.hitbox.colliderect(bg5doorB1.hitbox):
              if background5 == True:
                  #man.draw(win)
                  man.x = 850
                  man.y = 585
                  background5 = False
                  background4 = True

#=============== bg5doorA1 =====================
    if man.hitbox.colliderect(bg5doorA1.hitbox):
              if background5 == True:
                  if background6 == False:
                      #man.draw(win)
                      man.x = 1200
                      man.y = 30
                      background6 = True
                      background5 = False
                      background7 = False
                      background8 = False
                      background18 = False
                      
#=============== bg5doorA2 =====================
    if man.hitbox.colliderect(bg5doorA2.hitbox):
              if background5 == True:
                  if background7 == False:
                      #man.draw(win)
                      man.x = 30
                      man.y = 585
                      background7 = True
                      background6 = False
                      background8 = False
                      background5 = False
                      background18 = False

#=============== bg6doorA1 =====================
    if man.hitbox.colliderect(bg6doorA1.hitbox):
              if background6 == True:
                  if background9 == False:
                      #man.draw(win)
                      man.x = 1274
                      man.y = 400
                      background9 = True
                      background5 = False
                      background6 = False
                      background7 = False
                      background8 = False

#=============== bg6doorA2 =====================
    if man.hitbox.colliderect(bg6doorA2.hitbox):
              if background6 == True:
                  if background10 == False:
                      #man.draw(win)
                      man.x = 1100
                      man.y = 340
                      background10 = True
                      background5 = False
                      background6 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg6doorA3 =====================
    if man.hitbox.colliderect(bg6doorA3.hitbox):
              if background6 == True:
                  if background10 == False:
                      #man.draw(win)
                      man.x = 1100
                      man.y = 580
                      background10 = True
                      background5 = False
                      background6 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg6doorB1 =====================
    if man.hitbox.colliderect(bg6doorB1.hitbox):
              if background6 == True:
                  if background5 == False:
                      #man.draw(win)
                      man.x = 940
                      man.y = 670
                      background5 = True
                      background6 = False
                      background7 = False
                      background8 = False
                      
#=============== bg7doorB1 =====================
    if man.hitbox.colliderect(bg7doorB1.hitbox):
              if background7 == True:
                  if background5 == False:
                      #man.draw(win)
                      man.x = 1245
                      man.y = 264
                      background5 = True
                      background7 = False
                      background8 = False

#=============== bg7doorA1 =====================
    if man.hitbox.colliderect(bg7doorA1.hitbox):
              if background7 == True:
                  if background8 == False:
                      #man.draw(win)
                      man.x = 163
                      man.y = 585
                      background8 = True
                      background7 = False
                      background5 = False

#=============== bg8doorB1 =====================
    if man.hitbox.colliderect(bg8doorB1.hitbox):
              if background8 == True:
                  if background7 == False:
                      #man.draw(win)
                      man.x = 1245
                      man.y = 585
                      background7 = True
                      background8 = False
                      background9 = False

#=============== bg8doorA1 =====================
    if man.hitbox.colliderect(bg8doorA1.hitbox):
              if background8 == True:
                  if background11 == False:
                      man.draw(win)
                      man.x = 80
                      man.y = 178
                      background11 = True
                      background8 = False
                      background9 = False
                      background7 = False

#=============== bg9doorB1 =====================
    if man.hitbox.colliderect(bg9doorB1.hitbox):
              if background9 == True:
                  if background6 == False:
                      #man.draw(win)
                      man.x = 400
                      man.y = 400
                      background6 = True
                      background5 = False
                      background9 = False

#=============== bg10doorB1 ====================
    if man.hitbox.colliderect(bg10doorB1.hitbox):
              if background10 == True:
                  if background6 == False:
                      #man.draw(win)
                      man.x = 1100
                      man.y = 340
                      background6 = True
                      background5 = False
                      background10 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg10doorB2 ====================
    if man.hitbox.colliderect(bg10doorB2.hitbox):
              if background10 == True:
                  if background6 == False:
                      #man.draw(win)
                      man.x = 1100
                      man.y = 640
                      background6 = True
                      background5 = False
                      background10 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg10doorA1 ====================
    if man.hitbox.colliderect(bg10doorA1.hitbox):
              if background10 == True:
                  if background15 == False:
                      #man.draw(win)
                      man.x = 500
                      man.y = 300
                      background15 = True
                      background5 = False
                      background10 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg11doorB1 ====================
    if man.hitbox.colliderect(bg11doorB1.hitbox):
              if background11 == True:
                  if background8 == False:
                      #man.draw(win)
                      man.x = 1000
                      man.y = 131
                      background8 = True
                      background5 = False
                      background11 = False
                      background7 = False
                      background10 = False
                      background9 = False

#=============== bg11doorA1 ====================
    if man.hitbox.colliderect(bg11doorA1.hitbox):
              if background11 == True:
                  if background12 == False:
                      #man.draw(win)
                      man.x = 400
                      man.y = 210
                      background12 = True
                      background5 = False
                      background11 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg12doorB1 ====================
    if man.hitbox.colliderect(bg12doorB1.hitbox):
              if background12 == True:
                  if background11 == False:
                      #man.draw(win)
                      man.x = 1100
                      man.y = 1200
                      background11 = True
                      background5 = False
                      background12 = False
                      background7 = False
                      background8 = False
                      background9 = False

#=============== bg12doorA1 ====================
    if man.hitbox.colliderect(bg12doorA1.hitbox):
              if background12 == True:
                  if background13 == False:
                      #man.draw(win)
                      man.x = 120
                      man.y = 353
                      background13 = True
                      background11 = False
                      background12 = False
                      background10 = False
                      background8 = False
                      background9 = False

#=============== bg12doorA2 ====================
    if man.hitbox.colliderect(bg12doorA2.hitbox):
              if background12 == True:
                  if background31 == False:
                      man.draw(win)
                      man.x = 120
                      man.y = 353
                      background31 = True
                      background11 = False
                      background12 = False
                      background10 = False
                      background8 = False
                      background9 = False

#=============== bg13doorB1 ====================
    if man.hitbox.colliderect(bg13doorB1.hitbox):
              if background13 == True:
                  if background12 == False:
                      man.draw(win)
                      man.x = 1200
                      man.y = 353
                      background12 = True
                      background11 = False
                      background13 = False
                      background10 = False
                      background8 = False
                      background9 = False

#=============== bg15doorB1 ====================
    if man.hitbox.colliderect(bg15doorB1.hitbox):
              if background15 == True:
                  if background10 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background10 = True
                      background15 = False
                      background6 = False
                      background2 = False

#=============== bg15doorA1 ====================
    if man.hitbox.colliderect(bg15doorA1.hitbox):
              if background15 == True:
                  if background16 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background16 = True
                      background15 = False
                      background10 = False
                      background19 = False

#=============== bg16doorB1 ====================
    if man.hitbox.colliderect(bg16doorB1.hitbox):
              if background16 == True:
                  if background15 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background15 = True
                      background16 = False
                      background10 = False
                      background2 = False

#=============== bg16doorA1 ====================
    if man.hitbox.colliderect(bg16doorA1.hitbox):
              if background16 == True:
                  if background17 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background17 = True
                      background16 = False
                      background15 = False
                      background10 = False
                      
#=============== bg17doorB1 ====================
    if man.hitbox.colliderect(bg17doorB1.hitbox):
              if background17 == True:
                  if background6 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background5 = True
                      background17 = False
                      background15 = False
                      background10 = False

#=============== bg18doorB1 ====================
    if man.hitbox.colliderect(bg18doorB1.hitbox):
              if background18 == True:
                  if background2 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background2 = True
                      background3 = False
                      background18 = False
                      background19 = False

#=============== bg18doorA1 ====================
    if man.hitbox.colliderect(bg18doorA1.hitbox):
              if background18 == True:
                  if background19 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background19 = True
                      background3 = False
                      background18 = False
                      background2 = False
                      
#=============== bg19doorB1 ====================
    if man.hitbox.colliderect(bg19doorB1.hitbox):
              if background19 == True:
                  if background18 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background18 = True
                      background3 = False
                      background19 = False
                      background2 = False

#=============== bg19doorA1 ====================
    if man.hitbox.colliderect(bg19doorA1.hitbox):
              if background19 == True:
                  if background20 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background20 = True
                      background18 = False
                      background19 = False
                      background2 = False
                      
#=============== bg20doorB1 ====================
    if man.hitbox.colliderect(bg20doorB1.hitbox):
              if background20 == True:
                  if background19 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background19 = True
                      background20 = False
                      background21 = False
                      background2 = False

#=============== bg20doorA1 ====================
    if man.hitbox.colliderect(bg20doorA1.hitbox):
              if background20 == True:
                  if background21 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background21 = True
                      background18 = False
                      background19 = False
                      background2 = False

#=============== bg21doorB1 ====================
    if man.hitbox.colliderect(bg21doorB1.hitbox):
              if background21 == True:
                  if background20 == False:
                      man.draw(win)
                      man.x = 1245
                      man.y = 285
                      background20 = True
                      background21 = False
                      background19 = False
                      background2 = False

#=============== bg21doorA1 ====================
    if man.hitbox.colliderect(bg21doorA1.hitbox):
              if background21 == True:
                  if background24 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background24 = True
                      background21 = False
                      background20 = False
                      background19 = False

#=============== bg21doorA2 ====================
    if man.hitbox.colliderect(bg21doorA2.hitbox):
              if background21 == True:
                  if background22 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background22 = True
                      background21 = False
                      background20 = False
                      background19 = False

#=============== bg21doorA3 ====================
    if man.hitbox.colliderect(bg21doorA3.hitbox):
              if background21 == True:
                  if background23 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background23 = True
                      background21 = False
                      background20 = False
                      background19 = False

#=============== bg22doorB1 ====================
    if man.hitbox.colliderect(bg22doorB1.hitbox):
              if background22 == True:
                  if background21 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background21 = True
                      background22 = False
                      background20 = False
                      background19 = False

#=============== bg22doorA1 ====================
    if man.hitbox.colliderect(bg22doorA1.hitbox):
              if background22 == True:
                  if background23 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background23 = True
                      background22 = False
                      background20 = False
                      background21 = False

#=============== bg23doorB1 ====================
    if man.hitbox.colliderect(bg23doorB1.hitbox):
              if background23 == True:
                  if background22 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background22 = True
                      background23 = False
                      background20 = False
                      background21 = False

#=============== bg23doorA1 ====================
    if man.hitbox.colliderect(bg23doorA1.hitbox):
              if background23 == True:
                  if background21 == False:
                      man.draw(win)
                      man.x = 670
                      man.y = 285
                      background21 = True
                      background23 = False
                      background20 = False
                      background22 = False

#=============== bg24doorB1 ====================
    if man.hitbox.colliderect(bg24doorB1.hitbox):
              if background24 == True:
                  if background21 == False:
                      man.draw(win)
                      man.x = 60
                      man.y = 285
                      background21 = True
                      background24 = False
                      background20 = False
                      background19 = False

#========================================================================================================================
#========================================================================================================================
#================================================================= KEYS =================================================
#========================================================================================================================
#========================================================================================================================
#=====================================
#===================================== saving
#=====================================
    if keys[pygame.K_h] and not previous_key[pygame.K_h]:
        pickle.dump( [AlucardExp, AlucardNextLevel, TIME.hours, TIME.minutes, TIME.seconds, AlucardLevel, AlucardGold, AlucardKill, AlucardRooms, Alucardhealth, AlucardMP, AlucardHearts, AlucardATK, AlucardATK2, AlucardDEF, AlucardSTR, AlucardLCK, AlucardCON, AlucardINT], open( "DATA/SAVE/save.p", "wb" ) )
        for a in Loading_information:
            print(a)
        
#=====================================
#===================================== loading
#=====================================
    if keys[pygame.K_l] and not previous_key[pygame.K_l]:
        [AlucardExp, AlucardNextLevel, TIME.hours, TIME.minutes, TIME.seconds, AlucardLevel, AlucardGold, AlucardKill, AlucardRooms, Alucardhealth, AlucardMP, AlucardHearts, AlucardATK, AlucardATK2, AlucardDEF, AlucardSTR, AlucardLCK, AlucardCON, AlucardINT] = pickle.load( open( "DATA/SAVE/save.p", "rb" ) )
        for a in Loading_information:
            print(a)
            
#===============================================
#===============================================
#========= KEYS - ATK SWORD ====================
#===============================================
#===============================================
    if keys[pygame.K_KP4] and man.damageR == False and man.damageL == False and not previous_key[pygame.K_KP4] or keys[pygame.K_z] and man.damageR == False and man.damageL == False and not previous_key[pygame.K_z]:
        if AlucardMenuOn == False:
            if not (man.crouching) and not (man.isJump):
                man.attacking = True
            if man.crouching:
                man.crouchATK = True
            elif man.isJump:
                man.jumpAtk = True

            if man.attacking == True and man.attackCount == 0 or man.crouchATK == True and man.crouchATKcount == 0:
                r = SOUNDS_A[random.randrange(7,10)].play()

#===============================================
#===============================================
#=============== KEYS - ESQ ====================
#===============================================
#===============================================
    if keys[pygame.K_ESCAPE] and not previous_key[pygame.K_ESCAPE]:
        # Make Do you want to Exit the game screen here
        # y/n?
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
                run = False       
#===============================================
#===============================================
#=============== KEYS - F ======================
#===============================================
#============== FULLSCREN ======================
    if keys[pygame.K_f] and not previous_key[pygame.K_f]:
        fullscreen = not fullscreen
        if fullscreen:
            win = pygame.display.set_mode((1340, 690), pygame.FULLSCREEN)
        else:
            win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)
#===================================================================================================================================================================
#===================================================================================================================================================================
#=============================================================== ENEMIES MOTION AREA BELLOW ========================================================================
#===================================================================================================================================================================
#===================================================================================================================================================================
    if man.damageCount >= 10 and man.damageL == True:
        man.damageL = False
        man.right = True
        man.damageCount = 0

    if man.damageCount >= 10 and man.damageR == True:
        man.damageR = False
        man.left = True
        man.damageCount = 0
        
    if man.damageL == True or man.damageR == True:
        man.damageCount += 1
        if man.attacking == True or man.crouchATK == True:
            man.attacking = False
            man.crouchATK = False
            man.attackCount = 0
            man.crouchATKcount = 0
                
#===============================================
#===============================================
#=============== KEYS - LEFT ===================
#===============================================
#===============================================
    if keys[pygame.K_LEFT] and AlucardInventoryOn == True and not previous_key[pygame.K_LEFT] or keys[pygame.K_a] and AlucardInventoryOn == True and not previous_key[pygame.K_a]:
        if positionTicks == 0:
            SOUNDS_TICK[NNN].play()
            if invPos1 == True:
                invPos1 = False
                invPos4 = True
            elif invPos2 == True:
                invPos2 = False
                invPos1 = True
            elif invPos3 == True:
                invPos3 = False
                invPos2 = True
            elif invPos4 == True:
                invPos4 = False
                invPos3 = True
            elif invPos5 == True:
                invPos5 = False
                invPos8 = True
            elif invPos6 == True:
                invPos6 = False
                invPos5 = True
            elif invPos7 == True:
                invPos7 = False
                invPos6 = True
            elif invPos8 == True:
                invPos8 = False
                invPos7 = True
            elif invPos9 == True:
                invPos9 = False
                invPos12 = True
            elif invPos10 == True:
                invPos10 = False
                invPos9 = True
            elif invPos11 == True:
                invPos11 = False
                invPos10 = True
            elif invPos12 == True:
                invPos12 = False
                invPos11 = True
            elif invPos13 == True:
                invPos13 = False
                invPos16 = True
            elif invPos14 == True:
                invPos14 = False
                invPos13 = True
            elif invPos15 == True:
                invPos15 = False
                invPos14 = True
            elif invPos16 == True:
                invPos16 = False
                invPos15 = True

    elif keys[pygame.K_LEFT] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageR == False or keys[pygame.K_a] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageR == False or man.damageL == True and man.x > man.vel and Touching_right_wall == False :
        if man.damageL == True:
            man.damageR = False
        if AlucardMenuOn == False:
            man.x -= 10
            for a in grounds:
                if a.visible == True:
                    a.x += man.vel
                    if scrollingOn == True:
                        skeleton1.path = (int(bg1ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))
                        skeleton2.path = (int(bg1ground.x + 670 + 660 + 400), (bg1ground.x + 670 + 660 + 1250))
                        skeleton3.path = (int(bg1ground.x + 670 + 660 + 300), (bg1ground.x + 670 + 660 + 1250))
                        skeleton4.path = (int(bg1ground.x + 670 + 660 + 1885), (bg1ground.x + 670 + 660 + 2085)) # 1885 is the initial skeleton.x and 2115 is the skeleton initial final destination
                        skeleton5.path = (int(bg1ground.x + 670 + 660 + 3000), (bg1ground.x + 670 + 660 + 3417))
                        if background1B:
                            Tiger1.path = (int(bg1ground1B.x + 1330 + 500), (bg1ground1B.x + 1330 + 1250)) #500 = path[0] , 1250 = path[1]
                            Tiger2.path = (int(bg1ground1B.x + 1330 + 1000), (bg1ground1B.x + 1330 + 1000 +750))#1000 = path[0], 750 lenght of path, then path[1] = 1000+750
                            Tiger3.path = (int(bg1ground1B.x + 1330 + 1500), (bg1ground1B.x + 1330 + 1500 +750))
                            Tiger4.path = (int(bg1ground1B.x + 1330 + 2000), (bg1ground1B.x + 1330 + 2000 +750))
                            Tiger5.path = (int(bg1ground1B.x + 1330 + 2500), (bg1ground1B.x + 1330 + 2500 +750))
                        elif background1C:
                            Tiger6.path = (int(bg1ground1C.x + 1330 + 500), (bg1ground1C.x + 1330 + 1250)) #500 = path[0] , 1250 = path[1]
                            Tiger7.path = (int(bg1ground1C.x + 1330 + 1000), (bg1ground1C.x + 1330 + 1000 +750))#1000 = path[0], 750 lenght of path, then path[1] = 1000+750
                            Tiger8.path = (int(bg1ground1C.x + 1330 + 1500), (bg1ground1C.x + 1330 + 1500 +750))
                            Tiger9.path = (int(bg1ground1C.x + 1330 + 2000), (bg1ground1C.x + 1330 + 2000 +750))
                            Tiger10.path = (int(bg1ground1C.x + 1330 + 2500), (bg1ground1C.x + 1330 + 2500 +750))
                        for a in allHearts:
                            a.path = (int(bg1ground.x + 670 + 660 + (a.end - 20)), (bg1ground.x + 670 + 660 + a.end))
                        #background8
                        #Gargoyle1.path = (int(bg8ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))                    
            if scrollingOn == False:
                for d in candles:
                    d.x = d.x
                for a in bg1platforms:
                    a.x = a.x
                for e in skeletons:
                    e.x = e.x
                for a in allHearts:
                    a.x = a.x
                #for e in Gargoyles:
                #    e.x = e.x
            if man.damageL == True or man.damageR == True:
                man.left = False
                man.right = False
                man.standing = False
            else:
                man.left = True
                man.right = False
                man.standing = False
        
#===============================================
#===============================================
#=============== KEYS - RIGHT ==================
#===============================================
#===============================================
    elif keys[pygame.K_RIGHT] and AlucardInventoryOn == True and not previous_key[pygame.K_RIGHT] or keys[pygame.K_d] and AlucardInventoryOn == True and not previous_key[pygame.K_d]:
        if positionTicks == 0:
            SOUNDS_TICK[NNN].play()
            if invPos1 == True:
                invPos1 = False
                invPos2 = True
            elif invPos2 == True:
                invPos2 = False
                invPos3 = True
            elif invPos3 == True:
                invPos3 = False
                invPos4 = True
            elif invPos4 == True:
                invPos4 = False
                invPos1 = True
            elif invPos5 == True:
                invPos5 = False
                invPos6 = True
            elif invPos6 == True:
                invPos6 = False
                invPos7 = True
            elif invPos7 == True:
                invPos7 = False
                invPos8 = True
            elif invPos8 == True:
                invPos8 = False
                invPos5 = True
            elif invPos9 == True:
                invPos9 = False
                invPos10 = True
            elif invPos10 == True:
                invPos10 = False
                invPos11 = True
            elif invPos11 == True:
                invPos11 = False
                invPos12 = True
            elif invPos12 == True:
                invPos12 = False
                invPos9 = True
            elif invPos13 == True:
                invPos13 = False
                invPos14 = True
            elif invPos14 == True:
                invPos14 = False
                invPos15 = True
            elif invPos15 == True:
                invPos15 = False
                invPos16 = True
            elif invPos16 == True:
                invPos16 = False
                invPos13 = True 
                
    elif keys[pygame.K_RIGHT] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or keys[pygame.K_d] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or man.damageR == True and man.x < 1340 - man.width - man.vel and Touching_left_wall == False:
        if man.damageR == True:
            man.damageL = False    
        if AlucardMenuOn == False:
            man.x += 10
            for a in grounds:
                if a.visible == True:
                    a.x -= man.vel
                    if scrollingOn == True:
                        skeleton1.path = (int(bg1ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))
                        skeleton2.path = (int(bg1ground.x + 670 + 660 + 400), (bg1ground.x + 670 + 660 + 1250))
                        skeleton3.path = (int(bg1ground.x + 670 + 660 + 300), (bg1ground.x + 670 + 660 + 1250))
                        skeleton4.path = (int(bg1ground.x + 670 + 660 + 1885), (bg1ground.x + 670 + 660 + 2085)) # 1885 is the initial skeleton.x and 2115 is the skeleton initial final destination
                        skeleton5.path = (int(bg1ground.x + 670 + 660 + 3000), (bg1ground.x + 670 + 660 + 3417))
                        if background1B:
                            Tiger1.path = (int(bg1ground1B.x + 1330 + 500), (bg1ground1B.x + 1330 + 1250)) #500 = path[0] , 1250 = path[1]
                            Tiger2.path = (int(bg1ground1B.x + 1330 + 1000), (bg1ground1B.x + 1330 + 1000 +750))#1000 = path[0], 750 lenght of path, then path[1] = 1000+750
                            Tiger3.path = (int(bg1ground1B.x + 1330 + 1500), (bg1ground1B.x + 1330 + 1500 +750))
                            Tiger4.path = (int(bg1ground1B.x + 1330 + 2000), (bg1ground1B.x + 1330 + 2000 +750))
                            Tiger5.path = (int(bg1ground1B.x + 1330 + 2500), (bg1ground1B.x + 1330 + 2500 +750))
                        elif background1C:
                            Tiger6.path = (int(bg1ground1C.x + 1330 + 500), (bg1ground1C.x + 1330 + 1250)) #500 = path[0] , 1250 = path[1]
                            Tiger7.path = (int(bg1ground1C.x + 1330 + 1000), (bg1ground1C.x + 1330 + 1000 +750))#1000 = path[0], 750 lenght of path, then path[1] = 1000+750
                            Tiger8.path = (int(bg1ground1C.x + 1330 + 1500), (bg1ground1C.x + 1330 + 1500 +750))
                            Tiger9.path = (int(bg1ground1C.x + 1330 + 2000), (bg1ground1C.x + 1330 + 2000 +750))
                            Tiger10.path = (int(bg1ground1C.x + 1330 + 2500), (bg1ground1C.x + 1330 + 2500 +750))
                        for a in allHearts:
                            a.path = (int(bg1ground.x + 670 + 660 + (a.end - 20)), (bg1ground.x + 670 + 660 + a.end))
                        #background8
                        #Gargoyle1.path = (int(bg8ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))                    
            if scrollingOn == False:
                for d in candles:
                    d.x = d.x
                for a in bg1platforms:
                    a.x = a.x
                for e in skeletons:
                    e.x = e.x
                for a in allHearts:
                    a.x = a.x
                #for e in Gargoyles:
                #    e.x = e.x
            if man.damageL == True or man.damageR == True:
                man.left = False
                man.right = False
                man.standing = False
            else:
                man.right = True
                man.left = False
                man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
#===================================================================================================================================================================
#===================================================================================================================================================================
#=============================================================== ENEMIES MOTION AREA ABOVE =========================================================================
#===================================================================================================================================================================
#===================================================================================================================================================================        
#===============================================
#===============================================
#====== inventoryHoverX And Y Positions ========
#===============================================
#===============================================
    if invPos1 == True or invPos5 == True or invPos9 == True or invPos13 == True:
        inventoryHoverX = 60
    if invPos2 == True or invPos6 == True or invPos10 == True or invPos14 == True:
        inventoryHoverX = 375
    if invPos3 == True or invPos7 == True or invPos11 == True or invPos15 == True:
        inventoryHoverX = 690
    if invPos4 == True or invPos8 == True or invPos12 == True or invPos16 == True:
        inventoryHoverX = 1005

    if invPos1 == True or invPos2 == True or invPos3 == True or invPos4 == True:
        inventoryHoverY = 402
    if invPos5 == True or invPos6 == True or invPos7 == True or invPos8 == True:
        inventoryHoverY = 448
    if invPos9 == True or invPos10 == True or invPos11 == True or invPos12 == True:
        inventoryHoverY = 493
    if invPos13 == True or invPos14 == True or invPos15 == True or invPos16 == True:
        inventoryHoverY = 536
        
#===================================================
#=======================================================
#==== - KEYS - JUMP/SELECT AND - KEYS - UNSELECT ==============
#=======================================================
#===================================================
    if not(man.isJump):
        if keys[pygame.K_SPACE] and plat == True and not previous_key[pygame.K_SPACE] and man.attacking == False and man.crouchATK == False or keys[pygame.K_KP0] and man.attacking == False and man.crouchATK == False and plat == True and not previous_key[pygame.K_KP0]:
            if AlucardMenuOn == False:
                if man.damageL == False and man.damageR == False:
                    man.isJump = True
                    man.walkCount = 0
    else:
        if AlucardMenuOn == False:
            if man.jumpCount >= -10:
                neg = 1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                if man.jumpCount < 0:
                    neg = -1
                    man.isJump = False
            
            else:
                man.isJump = False
                man.jumpCount = 10
    #print(man.isJump)

#===============================================
#============ MENU SELECT/RETURN ==================
#===============================================
    if keys[pygame.K_x] and AlucardMenuOn == True and AlucardEquipMenuOn == False and not previous_key[pygame.K_x] or keys[pygame.K_KP0] and AlucardMenuOn == True and AlucardEquipMenuOn == False and not previous_key[pygame.K_KP0]:
        if equipHover == bar:
            equipHover = equipSelect
        if inventHover == barEquip:
            inventHover = inventSelect 
        if invHover == barInv:
            invHover = invSelect
            
    elif keys[pygame.K_c] and AlucardEquipMenuOn == True and AlucardInventoryOn == False and not previous_key[pygame.K_c] or keys[pygame.K_KP8] and AlucardEquipMenuOn == True and AlucardInventoryOn == False and not previous_key[pygame.K_KP8]:
        AlucardEquipMenuOn = False
    elif keys[pygame.K_c] and AlucardEquipMenuOn == False and AlucardInventoryOn == False and AlucardMenuOn == True and equiping == 0 and not previous_key[pygame.K_c] or keys[pygame.K_KP8] and AlucardEquipMenuOn == False and AlucardInventoryOn == False and AlucardMenuOn == True and equiping == 0 and not previous_key[pygame.K_KP8]:
        AlucardMenuOn = False
        AllParallaxes.equipHoverDisplay = True
        AllParallaxes.MpFullDisplay = True
        unpause()

    if equiping >= 21:
        equiping = 0
        equipHover = bar
        inventHover = barEquip
        invHover = barInv
        AlucardEquipMenuOn = True

    if equipHover == equipSelect:
        equiping += 1      

#===============================================
#======= INVETENTORY SELECT/RETURN ================
#===============================================
    elif keys[pygame.K_x] and AlucardEquipMenuOn == True  and not previous_key[pygame.K_x] or keys[pygame.K_KP0] and AlucardEquipMenuOn == True and not previous_key[pygame.K_KP0]:
        AlucardInventoryOn = True
        theHover.inv = True
    elif keys[pygame.K_c] and AlucardInventoryOn == True and not previous_key[pygame.K_c] or keys[pygame.K_KP8] and AlucardInventoryOn == True and not previous_key[pygame.K_KP8]:
        AlucardInventoryOn = False
        theHover.inv = False
        
#===============================================
#===============================================
#=============== KEYS - DOWN ===================
#===============================================
#===============================================
    if keys[pygame.K_DOWN] and not previous_key[pygame.K_DOWN] and AlucardInventoryOn == True or keys[pygame.K_s] and not previous_key[pygame.K_s] and AlucardInventoryOn == True:
        SOUNDS_TICK[NNN].play()
        if invPos1 == True:
            invPos1 = False
            invPos5 = True
        elif invPos2 == True:
            invPos2 = False
            invPos6 = True
        elif invPos3 == True:
            invPos3 = False
            invPos7 = True
        elif invPos4 == True:
            invPos4 = False
            invPos8 = True
        elif invPos5 == True:
            invPos5 = False
            invPos9 = True
        elif invPos6 == True:
            invPos6 = False
            invPos10 = True
        elif invPos7 == True:
            invPos7 = False
            invPos11 = True
        elif invPos8 == True:
            invPos8 = False
            invPos12 = True
        elif invPos9 == True:
            invPos9 = False
            invPos13 = True
        elif invPos10 == True:
            invPos10 = False
            invPos14 = True
        elif invPos11 == True:
            invPos11 = False
            invPos15 = True
        elif invPos12 == True:
            invPos12 = False
            invPos16 = True
        elif invPos13 == True or invPos14 == True or invPos15 == True or invPos16 == True:
            inventoryYaxe -= 44
            theHover.arrowDown = True

    elif keys[pygame.K_DOWN] and not previous_key[pygame.K_DOWN] and AlucardEquipMenuOn == True or keys[pygame.K_s] and not previous_key[pygame.K_s] and AlucardEquipMenuOn == True:
        SOUNDS_TICK[NNN].play()
        SelectedHand += 1
        if SelectedHand == 8:
            SelectedHand = 1
        equipHoverY += 42
        if equipHoverY >= 310:
            equipHoverY = 52
        if equipPosition1 == True:
            equipPosition1 = False
            equipPosition2 = True
        elif equipPosition2 == True:
            equipPosition2 = False
            equipPosition3 = True
        elif equipPosition3 == True:
            equipPosition3 = False
            equipPosition4 = True
        elif equipPosition4 == True:
            equipPosition4 = False
            equipPosition5 = True
        elif equipPosition5 == True:
            equipPosition5 = False
            equipPosition6 = True
        elif equipPosition6 == True:
            equipPosition6 = False
            equipPosition7 = True
        elif equipPosition7 == True:
            equipPosition7 = False
            equipPosition1 = True

    elif keys[pygame.K_DOWN] and not previous_key[pygame.K_DOWN] and AlucardMenuOn == True or keys[pygame.K_s] and not previous_key[pygame.K_s] and AlucardMenuOn == True:
        SOUNDS_TICK[NNN].play()
        hoverY += 54
        if hoverY >= 580:
            hoverY = 363
        if position1 == True:
            position1 = False
            position2 = True
        elif position2 == True:
            position2 = False
            position3 = True
        elif position3 == True:
            position3 = False
            position4 = True
        elif position4 == True:
            position4 = False
            position5 = True
        elif position5 == True:
            position5 = False
            position1 = True
  
    elif keys[pygame.K_DOWN] and man.y < 690 or keys[pygame.K_s] and man.y < 690:
        if man.bat:
        #---------------------------------------------------------------
            for a in platformsA:
                if neg == -1 and man.feetBox.colliderect(a.hitbox):
                    if a.visible:
                        man.y = a.y - 35
                        plat = True
                        falling = False
                        man.fallCount = 0
                        man.fallCountB = 0
                        man.jumpAtkCount = 0
                else:
                    plat = False
        #---------------------------------------------------------------                 
            for a in bg1Bplatforms:
                if background1B == True:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y - 7
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                else:
                    plat = False
        #----------------------------------------------------------------
            for a in bg1Cplatforms:
                if background1C == True:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y - 7
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                else:
                    plat = False
        #--------------------------------------------------------------
        #----------------- GROUNDS ----------------------------------
        #--------------------------------------------------------------
            for a in grounds:
                if neg == -1 and man.feetBox.colliderect(a.hitbox):
                    if a.visible:
                        man.y = a.y - 7
                        plat = True
                        falling = False
                        man.fallCount = 0
                        man.fallCountB = 0
                        man.jumpAtkCount = 0
                else:
                    plat = False
        #--------------------------------------------------------------
        #--------------------------------------------------------------
        #--------------------------------------------------------------
            if plat == False:
                man.y += 10
        else:
            if man.attacking == False:
                man.crouching = True
                man.idleCount = 0
    else:
        man.crouchCount = 0
        man.crouching = False

#===============================================
#===============================================
#=============== KEYS - SHIELD =================
#===============================================
#===============================================
    if keys[pygame.K_v] and man.attacking == False and man.crouchATK == False or keys[pygame.K_x] and man.attacking == False and man.crouchATK == False or keys[pygame.K_KP6] and man.attacking == False and man.crouchATK == False or keys[pygame.K_x] and man.attacking == False and man.crouchATK == False:
        if AlucardMenuOn == False:
            man.shield = True
    else:
        man.shieldCount = 0
        man.shield = False
#===============================================
#===============================================
#=============== KEYS - BAT ====================
#===============================================
#===============================================
    if keys[pygame.K_b] and not previous_key[pygame.K_b] and man.attacking == False and man.crouchATK == False or keys[pygame.K_KP9] and not previous_key[pygame.K_KP9] and man.attacking == False and man.crouchATK == False:
        if AlucardMenuOn == False:
            man.bat = not man.bat
            if man.bat:
                SOUNDS_A[18].play()
                man.bat = True # Add transformation effect
            else:
                SOUNDS_A[18].play()
                man.bat = False
            
    if man.bat == True:
        man.gravity = False
    else:
        if AlucardMenuOn == False:
            man.gravity = True

#===============================================
#===============================================
#=============== KEYS - UP ==================
#===============================================
#===============================================
    if keys[pygame.K_UP] and not previous_key[pygame.K_UP] and AlucardInventoryOn == True or keys[pygame.K_w] and not previous_key[pygame.K_w] and AlucardInventoryOn == True:
        SOUNDS_TICK[NNN].play()
        if invPos1 == True or invPos2 == True or invPos3 == True or invPos4 == True:
            if inventoryYaxe <= 400:
                inventoryYaxe += 44
            theHover.arrowUp = True
        elif invPos5 == True:
            invPos5 = False
            invPos1 = True
        elif invPos6 == True:
            invPos6 = False
            invPos2 = True
        elif invPos7 == True:
            invPos7 = False
            invPos3 = True
        elif invPos8 == True:
            invPos8 = False
            invPos4 = True
        elif invPos9 == True:
            invPos9 = False
            invPos5 = True
        elif invPos10 == True:
            invPos10 = False
            invPos6 = True
        elif invPos11 == True:
            invPos11 = False
            invPos7 = True
        elif invPos12 == True:
            invPos12 = False
            invPos8 = True
        elif invPos13 == True:
            invPos13 = False
            invPos9 = True
        elif invPos14 == True:
            invPos14 = False
            invPos10 = True
        elif invPos15 == True:
            invPos15 = False
            invPos11 = True
        elif invPos16 == True:
            invPos16 = False
            invPos12 = True
            
    elif keys[pygame.K_UP] and not previous_key[pygame.K_UP] and AlucardEquipMenuOn == True or keys[pygame.K_w] and not previous_key[pygame.K_w] and AlucardEquipMenuOn == True:
        SOUNDS_TICK[NNN].play()
        SelectedHand -= 1
        if SelectedHand == 0:
            SelectedHand = 7
        equipHoverY -= 42
        if equipHoverY <= 45:
            equipHoverY = 302
        if equipPosition1 == True:
            equipPosition1 = False
            equipPosition7 = True
        elif equipPosition2 == True:
            equipPosition2 = False
            equipPosition1 = True
        elif equipPosition3 == True:
            equipPosition3 = False
            equipPosition2 = True
        elif equipPosition4 == True:
            equipPosition4 = False
            equipPosition3 = True
        elif equipPosition5 == True:
            equipPosition5 = False
            equipPosition4 = True
        elif equipPosition6 == True:
            equipPosition6 = False
            equipPosition5 = True
        elif equipPosition7 == True:
            equipPosition7 = False
            equipPosition6 = True 

    elif keys[pygame.K_UP] and not previous_key[pygame.K_UP] and AlucardMenuOn == True or keys[pygame.K_w] and not previous_key[pygame.K_w] and AlucardMenuOn == True:
        SOUNDS_TICK[NNN].play()
        hoverY -= 54
        if hoverY <= 355:
            hoverY = 579
        if position1 == True:
            position1 = False
            position5 = True
        elif position2 == True:
            position2 = False
            position1 = True
        elif position3 == True:
            position3 = False
            position2 = True
        elif position4 == True:
            position4 = False
            position3 = True
        elif position5 == True:
            position5 = False
            position4 = True
                
    elif keys[pygame.K_UP] and man.y > 0 or keys[pygame.K_w] and man.y > 0: 
            if man.bat:
            #---------------------------------------------------------------
                for a in platformsA:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y + 7
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                    else:
                        plat = False
            #---------------------------------------------------------------                 
                for a in bg1Bplatforms:
                    if background1B == True:
                        if neg == -1 and man.feetBox.colliderect(a.hitbox):
                            if a.visible:
                                man.y = a.y + 7
                                plat = True
                                falling = False
                                man.fallCount = 0
                                man.fallCountB = 0
                                man.jumpAtkCount = 0
                    else:
                        plat = False
            #----------------------------------------------------------------
                for a in bg1Cplatforms:
                    if background1C == True:
                        if neg == -1 and man.feetBox.colliderect(a.hitbox):
                            if a.visible:
                                man.y = a.y + 7
                                plat = True
                                falling = False
                                man.fallCount = 0
                                man.fallCountB = 0
                                man.jumpAtkCount = 0
                    else:
                        plat = False
            #--------------------------------------------------------------
            #----------------- GROUNDS ----------------------------------
            #--------------------------------------------------------------
                for a in grounds:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y + 7
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                    else:
                        plat = False
            #--------------------------------------------------------------
            #--------------------------------------------------------------
            #--------------------------------------------------------------
                if plat == False:
                    man.y -= 10
            else:
                if man.attacking == False and man.crouchATK == False:
                    man.idle1 = True
    else:
        man.idle1 = False
    if positionTicks >= 7:
        positionTicks = 0
        positionTick = False
    if positionTick == True:
        positionTicks += 1
#===============================================
#===============================================
#========= KEYS - ALUCARD MENU =================
#===============================================
#===============================================    
    if keys[pygame.K_KP_ENTER] and not previous_key[pygame.K_KP_ENTER] or keys[pygame.K_RETURN] and not previous_key[pygame.K_RETURN]:
        AlucardMenuOn = not AlucardMenuOn
        menuTicking = True
        if AlucardMenuOn:
            paused()
            AlucardMenuOn = True
            AllParallaxes.equipHoverDisplay = False
            AllParallaxes.MpFullDisplay = False
        else:
            unpause()
            AlucardMenuOn = False
            AllParallaxes.equipHoverDisplay = True
            AllParallaxes.MpFullDisplay = True
            for a in mainMenuPositionList:
                a = False
            position1 = True
            hoverY = 363

    if AlucardMenuOn == False:
        AlucardEquipMenuOn = False
        AlucardInventoryOn = False
        theHover.inv = False       
#===============================================
#===============================================
#========= KEYS - INSTRUCTIONS =================
#===============================================
#===============================================    
    if keys[pygame.K_t] and not previous_key[pygame.K_t]:
        if instructionsOn == True:
            instructionsOn = False
            instructions = None
        else:
            instructions = pygame.image.load(f'DEBUGGING/instructions.png').convert_alpha()
            instructionsOn = True
        
#--------------------------------------------------------------
#----------------- PLATFORMS ----------------------------------
#--------------------- A --------------------------------------
    if fallTick >= 1:
        falling = True
        fallTick = 0
    if falling == False:
        fallTick += 1

##    step_on_platform(platformsA)
##    step_on_platform(bg1Bplatforms)
##    step_on_platform(bg1Cplatforms)
##    step_on_platform(grounds)

#--------------------------------------------------------------
    for a in platformsA:
        if neg == -1 and man.feetBox.colliderect(a.hitbox):
            if a.visible:
                if not (man.bat):
                    man.y = a.y - 95
                    man.jumpCount = 10
                plat = True
                falling = False
                man.fallCount = 0
                man.fallCountB = 0
                man.jumpAtkCount = 0
        else:
            if not (man.isJump):
                man.jumpCount = 0

#----------------------------------------------------------------
    for a in bg1Cplatforms:
        if background1C == True:
            if neg == -1 and man.feetBox.colliderect(a.hitbox):
                if a.visible:
                    if not (man.bat):
                        man.y = a.y - 95
                        man.jumpCount = 10
                    plat = True
                    falling = False
                    man.fallCount = 0
                    man.fallCountB = 0
                    man.jumpAtkCount = 0
        else:
            if not (man.isJump):
                man.jumpCount = 0
                
#----------------------------------------------------------------
    for a in bg1Dplatforms:
        if background1D == True:
            if neg == -1 and man.feetBox.colliderect(a.hitbox):
                if a.visible:
                    if not (man.bat):
                        man.y = a.y - 95
                        man.jumpCount = 10
                    plat = True
                    falling = False
                    man.fallCount = 0
                    man.fallCountB = 0
                    man.jumpAtkCount = 0
        else:
            if not (man.isJump):
                man.jumpCount = 0
#--------------------------------------------------------------
#----------------- GROUNDS ----------------------------------
#--------------------------------------------------------------
    for a in grounds:
        if neg == -1 and man.feetBox.colliderect(a.hitbox):
            if a.visible:
                if not (man.bat):
                    man.y = a.y - 95
                    man.jumpCount = 10
                plat = True
                falling = False
                man.fallCount = 0
                man.fallCountB = 0
                man.jumpAtkCount = 0
        else:
            if not (man.isJump):
                man.jumpCount = 0
#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 1 -------------------------------------
    if background1:
        if bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_a] and Touching_right_wall == False and man.damageL == False and man.damageR == False and man.x > man.vel and man.attacking == False and man.crouchATK == False or man.damageL == True and man.x > man.vel and Touching_right_wall == False:
                if AlucardMenuOn == False:
                    bgX += man.vel
                    bgXmountain += 2
                    for a in bg1platforms:
                        a.x += man.vel
                    for d in candles:
                        d.x += man.vel
                    for e in skeletons:
                        e.x += man.vel
                        e.currentXposition += man.vel
                        e.damageNumberMotionX += man.vel
                    for a in allHearts:
                        a.x += man.vel
                    for a in bg1_leftWalls:
                        a.x += man.vel
                    for a in bg1_rightWalls:
                        a.x += man.vel
                        
            elif keys[pygame.K_RIGHT] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_d] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or man.damageR == True and man.x < 1340 - man.width - man.vel and Touching_left_wall == False:
                if AlucardMenuOn == False:
                    bgX -= man.vel
                    bgXmountain -= 2
                    for d in candles:
                        d.x -= man.vel
                    for a in bg1platforms:
                        a.x -= man.vel
                    for e in skeletons:
                        e.x -= man.vel
                        e.currentXposition -= man.vel
                        e.damageNumberMotionX -= man.vel
                    for a in allHearts:
                        a.x -= man.vel
                    for a in bg1_leftWalls:
                        a.x -= man.vel
                    for a in bg1_rightWalls:
                        a.x -= man.vel
                    
        if bg1ground.x <= -4499 or bg1ground.x >= -1339:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 1 ---- BBBBBB -------------------------
    if background1B and AlucardMenuOn == False:
                #========== VERTICAL SCROLLING ==============
        if bg1BY >= -644 and bg1BY <= 0 and man.y >= 384 and man.y <= 386:            
            ScrollingVerticalOn = True
            
        if ScrollingVerticalOn == True:
            if man.damageR:
                if man.isJump == True or falling == True:
                    bg1BY += man.vel +5
                    for a in bg1Bplatforms:
                        a.y += man.vel +5
                    for a in tigers:
                        a.y += man.vel +5
                    for a in bg2_leftWalls:
                        a.y += man.vel +5
                    for a in bg2_rightWalls:
                        a.y += man.vel +5
            if man.damageL:
                if man.isJump == True or falling == True:
                    bg1BY += man.vel +5
                    for a in bg1Bplatforms:
                        a.y += man.vel +5
                    for a in tigers:
                        a.y += man.vel +5
                    for a in bg2_leftWalls:
                        a.y += man.vel +5
                    for a in bg2_rightWalls:
                        a.y += man.vel +5
            plat = False
            man.y = 385
            for a in bg1Bplatforms:
                if background1B == True:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y - 95
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                    else:
                        if not (man.isJump):
                            man.jumpCount = 0
                        
            if man.bat:
                if keys[pygame.K_DOWN] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_s] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1BY -= man.vel
                        for a in bg1Bplatforms:
                            a.y -= man.vel
                        for a in tigers:
                            a.y -= man.vel
                        for a in bg2_leftWalls:
                            a.y -= man.vel
                        for a in bg2_rightWalls:
                            a.y -= man.vel
                elif keys[pygame.K_UP] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_w] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1BY += man.vel
                        for a in bg1Bplatforms:
                            a.y += man.vel
                        for a in tigers:
                            a.y += man.vel
                        for a in bg2_leftWalls:
                            a.y += man.vel
                        for a in bg2_rightWalls:
                            a.y += man.vel
            else:
                if neg == -1:
                 
                    if plat == False:
                        man.vel = 10
                        bg1BY -= 10
                        for a in bg1Bplatforms:
                            a.y -= 10
                        for a in tigers:
                            a.y -= 10
                        for a in bg2_leftWalls:
                            a.y -= 10
                        for a in bg2_rightWalls:
                            a.y -= 10
                elif neg == 1:
                    plat = False
                    man.vel = 10
                    bg1BY += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg1Bplatforms:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in tigers:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg2_leftWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg2_rightWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
##                    if plat == False:
##                        man.vel = 10
##                        bg1BY += 10#(man.jumpCount ** 2) * 0.5 * neg
##                        for a in bg1Bplatforms:
##                            a.y += 10#(man.jumpCount ** 2) * 0.5 * neg
                
                
        if bg1BY <= -644:
            ScrollingVerticalOn = False
##            bg1BY = -644
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y <= 384:
                ScrollingVerticalOn = True
        elif bg1BY >= 0:
            ScrollingVerticalOn = False
##            bg1BY = 0
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y >= 386:
                ScrollingVerticalOn = True
            
                #==================== SIDE SCROLLING ==========================

        if bg1ground1B.x >= -4549 and bg1ground1B.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_a] and Touching_right_wall == False and man.damageL == False and man.damageR == False and man.x > man.vel and man.attacking == False and man.crouchATK == False or man.damageL == True and man.x > man.vel and Touching_right_wall == False:
                if AlucardMenuOn == False:
                    bg1BX += 10
                    bg1BXmountain += 2
                    for a in bg1Bplatforms:
                        a.x += 10
                    #for d in candles:
                    #    d.x += man.vel
                    for e in tigers:
                        e.x += man.vel
                        e.currentXposition += man.vel
                        e.damageNumberMotionX += man.vel
                    for a in bg2_leftWalls:
                        a.x += man.vel
                    for a in bg2_rightWalls:
                        a.x += man.vel
                    #for a in allHearts:
                    #    a.x += man.vel

            elif keys[pygame.K_RIGHT] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_d] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or man.damageR == True and man.x < 1340 - man.width - man.vel and Touching_left_wall == False:
                if AlucardMenuOn == False:
                    bg1BX -= 10
                    bg1BXmountain -= 2
                    #for d in candles:
                    #    d.x -= man.vel
                    for a in bg1Bplatforms:
                        a.x -= 10
                    for e in tigers:
                        e.x -= man.vel
                        e.currentXposition -= man.vel
                        e.damageNumberMotionX -= man.vel
                    for a in bg2_leftWalls:
                        a.x -= man.vel
                    for a in bg2_rightWalls:
                        a.x -= man.vel
                    #for a in allHearts:
                    #    a.x -= man.vel
                    
        if bg1ground1B.x <= -4549 or bg1ground1B.x >= -1339:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 1 ---- CCCCCC -------------------------
    if background1C:

        if bg1CY >= -644 and bg1CY <= 0 and man.y >= 384 and man.y <= 386:            
            ScrollingVerticalOn = True
            
        if ScrollingVerticalOn == True:
            if man.damageR:
                if man.isJump == True or falling == True:
                    bg1CY += man.vel +5
                    for a in bg1Cplatforms:
                        a.y += man.vel +5
                    for a in bgCtigers:
                        a.y += man.vel +5
                    for a in bg3_leftWalls:
                        a.y += man.vel +5
                    for a in bg3_rightWalls:
                        a.y += man.vel +5
            if man.damageL:
                if man.isJump == True or falling == True:
                    bg1CY += man.vel +5
                    for a in bg1Cplatforms:
                        a.y += man.vel +5
                    for a in bgCtigers:
                        a.y += man.vel +5
                    for a in bg3_leftWalls:
                        a.y += man.vel +5
                    for a in bg3_rightWalls:
                        a.y += man.vel +5
                        
            plat = False
            man.y = 385
            for a in bg1Cplatforms:
                if background1C == True:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y - 95
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                    else:
                        if not (man.isJump):
                            man.jumpCount = 0

            if man.bat:
                if keys[pygame.K_DOWN] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_s] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1CY -= man.vel
                        for a in bg1Cplatforms:
                            a.y -= man.vel
                        for a in bgCtigers:
                            a.y -= man.vel
                        for a in bg3_leftWalls:
                            a.y -= man.vel
                        for a in bg3_rightWalls:
                            a.y -= man.vel
                elif keys[pygame.K_UP] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_w] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1CY += man.vel
                        for a in bg1Cplatforms:
                            a.y += man.vel
                        for a in bgCtigers:
                            a.y += man.vel
                        for a in bg3_leftWalls:
                            a.y += man.vel
                        for a in bg3_rightWalls:
                            a.y += man.vel
                        
            else:
                if neg == -1:
                 
                    if plat == False:
                        man.vel = 10
                        bg1CY -= 10
                        for a in bg1Cplatforms:
                            a.y -= 10
                        for a in bg3_leftWalls:
                            a.y -= 10
                        for a in bg3_rightWalls:
                            a.y -= 10
                        for a in bgCtigers:
                            a.y -= 10
                elif neg == 1:
                    plat = False
                    man.vel = 10
                    bg1CY += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg1Cplatforms:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bgCtigers:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg3_leftWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg3_rightWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
##                    if plat == False:
##                        man.vel = 10
##                        bg1BY += 10#(man.jumpCount ** 2) * 0.5 * neg
##                        for a in bg1Bplatforms:
##                            a.y += 10#(man.jumpCount ** 2) * 0.5 * neg
                
                
        if bg1CY <= -644:
            ScrollingVerticalOn = False
##            bg1BY = -644
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y <= 384:
                ScrollingVerticalOn = True
        elif bg1CY >= 0:
            ScrollingVerticalOn = False
##            bg1BY = 0
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y >= 386:
                ScrollingVerticalOn = True
            
        #==================== SIDE SCROLLING ==========================

        if bg1ground1C.x >= -4549 and bg1ground1C.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_a] and Touching_right_wall == False and man.damageL == False and man.damageR == False and man.x > man.vel and man.attacking == False and man.crouchATK == False or man.damageL == True and man.x > man.vel and Touching_right_wall == False:
                if AlucardMenuOn == False:
                    bg1CX += 10
                    bg1CXmountain += 2
                    for a in bg1Cplatforms:
                        a.x += 10
                    for a in bg3_leftWalls:
                        a.x += 10
                    for a in bg3_rightWalls:
                        a.x += 10
                    #for d in candles:
                    #    d.x += man.vel
                    for e in bgCtigers:
                        e.x += man.vel
                    for a in allHearts:
                        a.x += man.vel

            elif keys[pygame.K_RIGHT] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_d] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or man.damageR == True and man.x < 1340 - man.width - man.vel and Touching_left_wall == False:
                if AlucardMenuOn == False:
                    bg1CX -= 10
                    bg1CXmountain -= 2
                    #for d in candles:
                    #    d.x -= man.vel
                    for a in bg1Cplatforms:
                        a.x -= 10
                    for a in bg3_leftWalls:
                        a.x -= 10
                    for a in bg3_rightWalls:
                        a.x -= 10
                    for e in bgCtigers:
                        e.x -= man.vel
                    #for a in allHearts:
                    #    a.x -= man.vel
                    
        if bg1ground1C.x <= -4549 or bg1ground1C.x >= -1339:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10



#
#
#

#
#
#
#
#
#
##

#
#
#
#
#





#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 1 ---- DDDDDD -------------------------
    if background1D:

        if bg1DY >= -644 and bg1DY <= 0 and man.y >= 384 and man.y <= 386:            
            ScrollingVerticalOn = True
            
        if ScrollingVerticalOn == True:
            if man.damageR:
                if man.isJump == True or falling == True:
                    bg1DY += man.vel +5
                    for a in bg1Dplatforms:
                        a.y += man.vel +5
##                    for a in bgDtigers:
##                        a.y += man.vel +5
                    for a in bg4_leftWalls:
                        a.y += man.vel +5
                    for a in bg4_rightWalls:
                        a.y += man.vel +5
            if man.damageL:
                if man.isJump == True or falling == True:
                    bg1DY += man.vel +5
                    for a in bg1Dplatforms:
                        a.y += man.vel +5
##                    for a in bgCtigers:
##                        a.y += man.vel +5
                    for a in bg4_leftWalls:
                        a.y += man.vel +5
                    for a in bg4_rightWalls:
                        a.y += man.vel +5
                        
            plat = False
            man.y = 385
            for a in bg1Dplatforms:
                if background1D == True:
                    if neg == -1 and man.feetBox.colliderect(a.hitbox):
                        if a.visible:
                            man.y = a.y - 95
                            plat = True
                            falling = False
                            man.fallCount = 0
                            man.fallCountB = 0
                            man.jumpAtkCount = 0
                    else:
                        if not (man.isJump):
                            man.jumpCount = 0

            if man.bat:
                if keys[pygame.K_DOWN] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_s] and man.y < 690 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1DY -= man.vel
                        for a in bg1Dplatforms:
                            a.y -= man.vel
##                        for a in bgCtigers:
##                            a.y -= man.vel
                        for a in bg4_leftWalls:
                            a.y -= man.vel
                        for a in bg4_rightWalls:
                            a.y -= man.vel
                elif keys[pygame.K_UP] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_w] and man.y > 0 and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False:
                    if AlucardMenuOn == False:
                        bg1DY += man.vel
                        for a in bg1Dplatforms:
                            a.y += man.vel
##                        for a in bgCtigers:
##                            a.y += man.vel
                        for a in bg4_leftWalls:
                            a.y += man.vel
                        for a in bg4_rightWalls:
                            a.y += man.vel
                        
            else:
                if neg == -1:
                 
                    if plat == False:
                        man.vel = 10
                        bg1DY -= 10
                        for a in bg1Dplatforms:
                            a.y -= 10
                        for a in bg4_leftWalls:
                            a.y -= 10
                        for a in bg4_rightWalls:
                            a.y -= 10
##                        for a in bgCtigers:
##                            a.y -= 10
                elif neg == 1:
                    plat = False
                    man.vel = 10
                    bg1DY += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg1Dplatforms:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
##                    for a in bgCtigers:
##                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg4_leftWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg4_rightWalls:
                        a.y += (man.jumpCount ** 2) * 0.5 * neg
##                    if plat == False:
##                        man.vel = 10
##                        bg1BY += 10#(man.jumpCount ** 2) * 0.5 * neg
##                        for a in bg1Bplatforms:
##                            a.y += 10#(man.jumpCount ** 2) * 0.5 * neg
                
                
        if bg1DY <= -644:
            ScrollingVerticalOn = False
##            bg1BY = -644
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y <= 384:
                ScrollingVerticalOn = True
        elif bg1DY >= 0:
            ScrollingVerticalOn = False
##            bg1BY = 0
##            for a in bg1Bplatforms:
##                a.y = a.y
            if man.y >= 386:
                ScrollingVerticalOn = True
            
        #==================== SIDE SCROLLING ==========================

        if bg1ground1D.x >= -4549 and bg1ground1D.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] and Touching_right_wall == False and man.x > man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_a] and Touching_right_wall == False and man.damageL == False and man.damageR == False and man.x > man.vel and man.attacking == False and man.crouchATK == False or man.damageL == True and man.x > man.vel and Touching_right_wall == False:
                if AlucardMenuOn == False:
                    bg1DX += 10
                    bg1DXmountain += 2
                    for a in bg1Dplatforms:
                        a.x += 10
                    for a in bg4_leftWalls:
                        a.x += 10
                    for a in bg4_rightWalls:
                        a.x += 10
                    #for d in candles:
                    #    d.x += man.vel
##                    for e in bgCtigers:
##                        e.x += man.vel
##                    for a in allHearts:
##                        a.x += man.vel

            elif keys[pygame.K_RIGHT] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False and man.damageL == False and man.damageR == False or keys[pygame.K_d] and Touching_left_wall == False and man.x < 1340 - man.width - man.vel and man.attacking == False and man.crouchATK == False or man.damageR == True and man.x < 1340 - man.width - man.vel and Touching_left_wall == False:
                if AlucardMenuOn == False:
                    bg1DX -= 10
                    bg1DXmountain -= 2
                    #for d in candles:
                    #    d.x -= man.vel
                    for a in bg1Dplatforms:
                        a.x -= 10
                    for a in bg4_leftWalls:
                        a.x -= 10
                    for a in bg4_rightWalls:
                        a.x -= 10
##                    for e in bgCtigers:
##                        e.x -= man.vel
                    #for a in allHearts:
                    #    a.x -= man.vel
                    
        if bg1ground1D.x <= -4549 or bg1ground1D.x >= -1339:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10












#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#




#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 6 -------------------------------------
    if background6:
        if bg6ground.x >= 669 and bg6ground.x <= 3514:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX3 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX3 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg6ground.x <= 669 or bg6ground.x >= 3514:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10
#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 8 -------------------------------------
    if background8:
        if bg8ground.x >= -10719 and bg8ground.x <= -1176:    #4560  10720 1339-163
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX2 += man.vel
                #bgXmountain += 2
                for a in bg8platforms:
                    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in Gargoyles:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX2 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                for a in bg8platforms:
                    a.x -= man.vel
                #for e in Gargoyles:
                #    e.x -= man.vel

        if bg8ground.x <= -10719 or bg8ground.x >= -1176:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 10 -------------------------------------
    if background10:
        if bg10ground.x >= 669 and bg10ground.x <= 3798:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX5 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX5 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg10ground.x <= 669 or bg10ground.x >= 3798:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 11 -------------------------------------
    if background11:
        if bg11ground.x >= -9400 and bg11ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX6 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX6 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg11ground.x <= -9400 or bg11ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 12 -------------------------------------
    if background12:
        if bg12ground.x >= -2681 and bg12ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX7 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX7 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg12ground.x <= -2681 or bg12ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 13 -------------------------------------
    if background13:
        if bg13ground.x >= -10720 and bg13ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX8 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX8 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg13ground.x <= -10720 or bg13ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 16-------------------------------------
    if background16:
        if background16.x >= -1292 and background16.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX13 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX13 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if background16.x <= -1292 or background16.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 18 -------------------------------------
    if background18:
        if bg18ground.x >= -3476 and bg18ground.x <= -669:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX4 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX4 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg18ground.x <= -3476 or bg18ground.x >= -669:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 19 -------------------------------------
    if background19:
        if bg19ground.x >= -7052 and bg19ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX9 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX9 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg19ground.x <= -7052 or bg19ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 20 -------------------------------------
    if background20:
        if bg20ground.x >= -7052 and bg20ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX10 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX10 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg20ground.x <= -7052 or bg20ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 21 -------------------------------------
    if background21:
        if bg21ground.x >= -8788 and bg21ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX11 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX11 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg21ground.x <= -8788 or bg21ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 22 -------------------------------------
    if background22:
        if bg22ground.x >= -1916 and bg22ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX11 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX11 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg22ground.x <= -1916 or bg22ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 24-------------------------------------
    if background24:
        if bg24ground.x >= -1912 and bg24ground.x <= 0:  #4560  10720 bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bgX12 += man.vel
                #bgXmountain += 2
                #for a in bg8platforms:
                #    a.x += man.vel
                #for d in candles:
                #    d.x += man.vel
                #for e in skeletons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX12 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in skeletons:
                #    e.x -= man.vel

        if bg24ground.x <= -1912 or bg24ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
    previous_key = keys
    #pygame.display.update()
#-------------------------------------------------------------
#==========================PRINTING FOR TESTS AREA=====================================
#    print(bg1ground1B.x)
#    print(man.y)
#    print(man.x)
#    print(skeleton1.x)
#    print(skeleton1.left)
#    print(SelectedHand)
#    print(fallRight[0]) 
#    print(len(AlucardInventory))
#    print(instructionsOn)
#    print(bg3extraplatforms[0].y)
#    print(bg1DX)
#======================================================================================
pygame.quit()
#===============================================
#===============================================
#===============================================
#===============================================Games to pick sprites from:
#===============================================Tiny Barbarian DX
#===============================================Timespinner
#===============================================
#===============================================
#===============================================
#===============================================
