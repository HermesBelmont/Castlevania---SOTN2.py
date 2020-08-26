import pygame, sys, os
import random
import time
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((1340, 690), pygame.RESIZABLE)
pygame.display.set_caption("Castlevania: Symphony of the Night 2")
icons = [pygame.image.load(f'DATA/GRAPHICS/ICON/{i}.png').convert_alpha() for i in range(19)]
randomIcon = random.randrange(0,18)
GameIconImage = icons[randomIcon]
pygame.display.set_icon(GameIconImage)

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
scrollingOn = False
ScrollingVerticalOn = False
clock = pygame.time.Clock()

run = True
gameSpeed = 30

plat = False
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
menuTicks = 0 # main menu opening ticks
menuTicking = False # main menu opening ticking
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
items = [pygame.image.load(f'DATA/GRAPHICS/ITEMS/{i}.png').convert_alpha() for i in range(162)]

inventoryHoverX = 60 # Equip menu selection bar
inventoryHoverY = 402 # Equip menu selection bar
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

#==================================================================================================
#==================================================================================================
#=============== IMAGES ===========================================================================
#==================================================================================================
#==================================================================================================
#===============================================
#===============================================
#=============== SUB MENU ======================
#===============================================
#===============================================
SUBMENU = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/0/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU1 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/1/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU2 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/2/{i}.png').convert_alpha() for i in range(4)]
#SUBMENU3 = [pygame.image.load(f'DATA/GRAPHICS/MENUS/SUB MENU/3/{i}.png').convert_alpha() for i in range(4)]
#===============================================
#===============================================
#============= BACKGROUNDS =====================
#===============================================
#===============================================
#extraParallax = False
background1 = True
background1B = False
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

bgList = [background1,background1B,background2,background3,background4,background5,background6,background7,background8,background9,background10,
          background11,background12,background13,background14,background15,background16,background17,background18,background19,background20,
          background21,background22,background23,background24,background25,background26,background27,background28,background29,background30,
          background30b,background31,background32,backgroundSave]

#===============================================
#===============================================
#============= BACKGROUNDS ===================== ##### NON ESSENTIAL LOADING ########
#===============================================
#===============================================
#if background1 == True:
bg1 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "0.png")).convert_alpha()
#else:
#    bg1 = None
#if background1B == True:
bg1B = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "1.png")).convert_alpha()
#else:
#    bg1B = None
bg2 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "3.png")).convert_alpha()
bg3 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "4.png")).convert_alpha()
bg4 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "5.png")).convert_alpha()
bg5 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "6.png")).convert_alpha()
bg6 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "7.png")).convert_alpha()
bg7 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "8.png")).convert_alpha()
bg8 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "9.png")).convert_alpha()
bg9 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "10.png")).convert_alpha()
bg10 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "11.png")).convert_alpha()
bg11 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "12.png")).convert_alpha()
bg12 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "13.png")).convert_alpha()
bg13 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "14.png")).convert_alpha()
bg14 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "15.png")).convert_alpha()
bg15 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "16.png")).convert_alpha()
bg16 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "17.png")).convert_alpha()
bg17 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "18.png")).convert_alpha()
bg18 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "19.png")).convert_alpha()
bg19 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "20.png")).convert_alpha()
bg20 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "21.png")).convert_alpha()
bg21 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "22.png")).convert_alpha() # was out of memory, now is fine
bg22 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "23.png")).convert_alpha()
bg23 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "24.png")).convert_alpha()
bg24 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "25.png")).convert_alpha()
bg25 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "26.png")).convert_alpha()
bg26 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "27.png")).convert_alpha()
bg27 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "28.png")).convert_alpha()
bg28 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "29.png")).convert_alpha()
bg29 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "30.png")).convert_alpha()
#bg30 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "31.png")).convert_alpha() #out of memoy
#bg30b = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "32.png")).convert_alpha() #out of memory
bg31 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "33.png")).convert_alpha()
bg32 = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "34.png")).convert_alpha()
bgSave = pygame.image.load(os.path.join('DATA/GRAPHICS/BACKGROUNDS', "35.png")).convert_alpha()

#===============================================
#===============================================
#============== PARALLAX =======================##### NON ESSENTIAL LOADING ########
#===============================================
#===============================================
#if background1 == True or background1B == True:
X1PR1 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR1.png').convert()
X1PR2 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR2.png').convert_alpha()
X1PR3 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/OUTSIDE/X1PR3.png').convert_alpha()

#------------ X2PR1 = pygame.image.load(f'DATA/GRAPHICS/PARALLAX/INSIDE/X2PR1.jpg').convert() ##### NON ESSENTIAL LOADING ########
##else:
##    X1PR1 = None
##    X1PR2 = None
##    X1PR3 = None
##
##    X2PR1 = None
#animated parallax
#if extraParallax == True:
forest = [pygame.image.load(f'DATA/GRAPHICS/PARALLAX/FOREST/Forest{i}.png').convert_alpha() for i in range(8)]
Bg3Pillars = [pygame.image.load(f'DATA/GRAPHICS/PARALLAX/BG3 PILLARS/bg3-{i}.png').convert_alpha() for i in range(6)]
##else:
##    forest = None
##    Bg3Pillars =  None

#======================================================
#======================================================
#=============== SPEECHES IMAGES ====================== ##### NON ESSENTIAL LOADING ########
#======================================================
#======================================================
AlucardSpeech01 = False
AlucardSpeech01Count = 0

#if AlucardSpeech01 == True:
AlucardSP1 = [pygame.image.load(f'DATA/GRAPHICS/SPEECHES/Alucard Speech 01/{i}.jpg').convert_alpha() for i in range(105)]
#else:
#    AlucardSP1 = None

if AlucardSpeech01Count + 1 >= 105:
    AlucardSpeech01Count = 0
    Alucardspeech01 = False

if AlucardSpeech01 == True:
    win.blit(AlucardSP1[AlucardSpeech01Count//3], (int(50), int(50)))
    AlucardSpeech01Count += 1

#===============================================
#===============================================
#================ DOORS ======================== ##### NON ESSENTIAL LOADING ########
#=============================================== #### EXISTS. TO BE USED. ####
#===============================================
##areaDoorClosed = [pygame.image.load(f'DATA/GRAPHICS/MISC/DOORS/AREA DOOR/CLOSED/{i}.png').convert_alpha() for i in range(5)]
##areaDoorOpen = [pygame.image.load(f'DATA/GRAPHICS/MISC/DOORS/AREA DOOR/OPEN/{i}.png').convert_alpha() for i in range(20)]
##sealedDoorClosed = [pygame.image.load(f'DATA/GRAPHICS/MISC/DOORS/SEALED DOOR/CLOSED/{i}.png').convert_alpha() for i in range(6)]
##sealedDoorOpen = [pygame.image.load(f'DATA/GRAPHICS/MISC/DOORS/SEALED DOOR/OPEN/{i}.png').convert_alpha() for i in range(12)]
##olroxDoor = [pygame.image.load(f'DATA/GRAPHICS/MISC/DOORS/OLROX DOOR/OPEN/{i}.png').convert_alpha() for i in range(14)]

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

walkRight = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/WALKING/{i}.png').convert_alpha() for i in range(31)]
walkLeft = [pygame.transform.flip(a, True, False) for a in walkRight]
ALKattack = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/ATTACK/H{i}.png').convert_alpha() for i in range(17)]
ALKattackLeft = [pygame.transform.flip(a, True, False) for a in ALKattack]
crouch = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/CROUCH/F{i}.png').convert_alpha() for i in range(17)]
crouch2 = [pygame.transform.flip(a, True, False) for a in crouch]
char = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/STANDING/B{i}.png').convert_alpha() for i in range(14)]
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
AlucardBatR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/BAT/K{i}.png').convert_alpha() for i in range(6)]
AlucardBatL = [pygame.transform.flip(a, True, False) for a in AlucardBatR]
idle1R = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/IDLE/{i}.png').convert_alpha() for i in range(2)]
idle1L = [pygame.transform.flip(a, True, False) for a in idle1R]

##################################### not assigned yet ##################################################################
stop = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/STOP/{i}.png').convert_alpha() for i in range(18)]
stop1R = stop[0:12]
stop1L = [pygame.transform.flip(a, True, False) for a in stop1R]
stop2R = (stop[0:7] + stop[13:18])
stop2L = [pygame.transform.flip(a, True, False) for a in stop2R]
SquatAtkR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/SQUAT ATK/SquatAtkR{i}.png').convert_alpha() for i in range(17)]
SquatAtkL = [pygame.transform.flip(a, True, False) for a in SquatAtkR]
idle2R = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/IDLE 2/{i}.png').convert_alpha() for i in range(2)]
idle2L = [pygame.transform.flip(a, True, False) for a in idle2R]
JumpATKR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/JUMP ATK/JumpATK{i}.png').convert_alpha() for i in range(4)]
JumpATKL = [pygame.transform.flip(a, True, False) for a in JumpATKR]
AlucardSwordR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/ALUCARD SWORD/J{i}.png').convert_alpha() for i in range(8)]
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
turnR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/TURNING AROUND/TurnR{i}.png').convert_alpha() for i in range(10)]
turnL = [pygame.transform.flip(a, True, False) for a in turnR]
deadR = [pygame.image.load(f'DATA/GRAPHICS/ALUCARD/DEAD/DEAD{i}.png').convert_alpha() for i in range(5)]
deadL = [pygame.transform.flip(a, True, False) for a in deadR]

# sitting and 2nd jump slope missing. idl2 not working
#=======================================================
#=======================================================
#================= MENUS / MISC ========================
#=======================================================
#=======================================================
#MENUS ----------------------------------------Main Menu
AlucardMenuSelection = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','Selection.png')).convert_alpha()
AlucardMenu = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','AlucardMenu.png')).convert()
AlucardEquipMenu = pygame.image.load(os.path.join('DATA/GRAPHICS/MENUS','Equip Menu.png')).convert()
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
#=============== ENEMIES ======================= ##### NON ESSENTIAL LOADING ########
#===============================================
#===============================================
#GRASSHOPPER
grasshopper = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GRASSHOPPER/WALK/Z{i}.png').convert_alpha() for i in range(8)]
grasshopperWalkR = [pygame.transform.flip(a, True, False) for a in grasshopper]
grasshopperAttack = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GRASSHOPPER/ATK/ZA{i}.png').convert_alpha() for i in range(6)]
grasshopperAttackR = [pygame.transform.flip(a, True, False) for a in grasshopperAttack]

#DHURON
DhuronWalkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/WALK-R/DH-L{i}.png').convert_alpha() for i in range(9)]
DhuronWalkL = [pygame.transform.flip(a, True, False) for a in DhuronWalkR]
DhuronAttackR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/DHURON/ATK-R/DHATKR{i}.png').convert_alpha() for i in range(13)]
DhuronAttackL = [pygame.transform.flip(a, True, False) for a in DhuronAttackR]

#GARGOYLE
gargoyleWalk = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GARGOYLE/WALK/{i}.png').convert_alpha() for i in range(5)]
gargoyleWalkLeft = [pygame.transform.flip(a, True, False) for a in gargoyleWalk]
gargoyleAtk = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/GARGOYLE/ATK/{i}.png').convert_alpha() for i in range(3)]
gargoyleAtkLeft = [pygame.transform.flip(a, True, False) for a in gargoyleAtk]

#TIGER
tigerIdleR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/IDLE-R/{i}.png').convert_alpha() for i in range(23)]
tigerIdleL = [pygame.transform.flip(a, True, False) for a in tigerIdleR]
tigerAtkR = [pygame.image.load(f'DATA/GRAPHICS/ENEMIES/TIGER/ATK-R/{i}.png').convert_alpha() for i in range(25)]
tigerAtkL = [pygame.transform.flip(a, True, False) for a in tigerAtkR]
    
#===============================================
#===============================================
#================= NPCS ======================== ##### NON ESSENTIAL LOADING ########
#===============================================
#===============================================
NPC1 = [pygame.image.load(f'DATA/GRAPHICS/NPCS/{i}.png').convert_alpha() for i in range(3)] #old man
#=====================================================================================================
#=====================================================================================================
#=============== SOUNDS ============================================================================== ##### NON ESSENTIAL LOADING ########
#=====================================================================================================
#=====================================================================================================
SOUNDS_A = [pygame.mixer.Sound(f'DATA/SOUNDS/SFX/{i}.wav')for i in range(31)]

#ALKJUMPFALL = pygame.mixer.Sound('????.wav') # ADD
#SOUNDsv_hrtbt = pygame.mixer.Sound('sv_hrtbt.wav') #
#SOUNDfam_sword1 = pygame.mixer.Sound('swd_dark.wav')#
#SOUNDdem_die = pygame.mixer.Sound('dem_die.wav') #
#SOUNDbreakpot = pygame.mixer.Sound('breakpot.wav') # break glass sound
#SOUNDthunder = pygame.mixer.Sound('thunder.wav')#

#======================================================
#======================================================
#=============== SPEECHES SOUNDS ====================== ##### NON ESSENTIAL LOADING ########
#======================================================
#======================================================
AlucardSpeech01SOUND = pygame.mixer.Sound(os.path.join('DATA/SOUNDS/SPEECHES', 'Alucard - He is too weak.wav'))

#=====================================================================================================
#===============================================
#===============================================
#================ MUSIC ======================== ##### NON ESSENTIAL LOADING ########
#===============================================
#===============================================
#if background1 == True:
pygame.mixer.music.stop()
pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
pygame.mixer.music.play(-1)

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
#=====================================================================================================
#=====================================================================================================
#===================================== CLASSES =======================================================
#=====================================================================================================
#=====================================================================================================
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
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 29, 52)
        self.inventHoverDisplay = False
        self.inventHoverDisplayCount = 0
        self.inv = False
        self.invC = 0
    
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

        if self.invC + 1 >= 63:
            self.invC = 0

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

        if self.inv == True:
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
        # self.initSpeed = -100 initial negative y speed
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
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 29, 52)
        self.atkbox = pygame.Rect(int(self.x), int(self.y), 60, 10)
        # MAKE STATUS HERE RATHER THAN USING GLOBAL...
        self.atk = 10
        self.damageR = False
        self.damageL = False
        self.damageCount = 0
        

                        # animations frames:JumpATKR

    def draw(self,win):

        
        if self.walkCount + 1 >= 62:
            self.walkCount = 30

        if self.standing == True:
            if self.idleCount + 1 >= 42:
                self.idleCount = 39
        else:
            self.idleCount = 0
            
        if self.shield == True:
            if self.shieldCount + 1 >= 3:
                self.shieldCount = 1

        if self.idle1 == True:
            self.idleCount = 0
            if self.idle1Count + 1 >= 2:
                self.idle1Count = 1
                
        if self.bat == True:
            if self.batCount + 1 >= 18:
                self.batCount = 0
                
        if self.fallCount + 1 >= 18:
            self.fallCount = 16
                
        if self.isJump == True:
            if self.jumpingUpCount + 1 >= 24:
                self.jumpingUpCount = 0

            if self.jumpAtkCount + 1 >= 4:
                self.jumpAtkCount = 0
        else:
            self.jumpingUpCount = 0
            self.jumpAtkCount = 0
            
        if self.crouching == True:
            if self.crouchCount + 1 >= 14:
                self.crouchCount = 13
        else:
            self.crouching = False

        if self.crouchATK == True:
            if self.crouchATKcount +1 >= 17:
                self.crouchATKcount = 0
                self.crouchATK = False

        if self.attacking == True:
            if self.attackCount + 1 >= 3 and self.right:
                self.atkbox = pygame.Rect(int(self.x + 70), int(self.y + 20), 120, 15)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.attackCount + 1 >= 3 and self.left:
                self.atkbox = pygame.Rect(int(self.x - 20), int(self.y + 20), -120, -15)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.attackCount >= 3:
                self.atkbox = pygame.Rect(int(0), int(0), 0, 0)
                pygame.draw.rect(win, (255,0,0), self.atkbox,2)
            if self.attackCount + 1 >= 17:
                self.attackCount = 0
                man.attacking = False
                
                        # animations assingment to actions and speed:


#        if self.shield:
#            self.idle1 = True
#            if self.right:
#                win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 25), int(self.y + 10)))
#                self.shieldCount += 1
#            if self.left:
#                win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x + 25), int(self.y + 10)))
#                self.shieldCount += 1
#        else:
#            self.idle1 = False
        if self.damageR:
            win.blit(damageLeft[1], (int(self.x), int(self.y)))
        if self.damageL:
            win.blit(damage[1], (int(self.x), int(self.y)))
        if not (self.bat):
            #if neg == 1:
            #    if self.left:
            #        win.blit(jumpLeft[self.jumpingUpCount//2], (int(self.x), int(self.y)))
            #        self.jumpingUpCount += 1
            if not (self.standing):
                self.hitbox = pygame.Rect(int(self.x)+20, int(self.y), 30, 96)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)

                if self.left: 
                    if not (self.isJump) and falling == True:
                        win.blit(fallLeft[self.fallCount//3], (int(self.x), int(self.y)))
                        self.fallCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                            self.shieldCount += 1
                    
                    elif self.isJump:
                        win.blit(jumpLeft[self.jumpingUpCount//2], (int(self.x), int(self.y)))
                        self.jumpingUpCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                            self.shieldCount += 1
                    else:
                        win.blit(walkLeft[self.walkCount//2], (int(self.x), int(self.y)))
                        self.walkCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y + 10)))
                            self.shieldCount += 1
                            
                elif self.right:
                    if not (self.isJump) and falling == True:
                        win.blit(fallRight[self.fallCount//3], (int(self.x), int(self.y)))
                        self.fallCount += 1
                        if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y)))
                            self.shieldCount += 1
                    elif self.isJump:
                        win.blit(jumpRight[self.jumpingUpCount//2], (int(self.x), int(self.y)))
                        self.jumpingUpCount += 1
                        if self.shield:
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 72), int(self.y)))
                            self.shieldCount += 1
                    else:
                        win.blit(walkRight[self.walkCount//2], (int(self.x), int(self.y)))
                        self.walkCount += 1
                        if self.shield:
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 50), int(self.y + 10)))
                            self.shieldCount += 1
                
            elif self.isJump:
                self.hitbox = pygame.Rect(int(self.x)+20, int(self.y), 30, 96)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.right:
                    win.blit(jump[self.jumpingUpCount//2], (int(self.x), int(self.y)))
                    self.jumpingUpCount += 1
                    if self.shield:
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 30), int(self.y + 10)))
                            self.shieldCount += 1
                elif self.left:
                    win.blit(jump2[self.jumpingUpCount//2], (int(self.x), int(self.y)))
                    self.jumpingUpCount += 1
                    if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 15), int(self.y + 10)))
                            self.shieldCount += 1
                    
            elif self.crouching:
                self.y = self.y + 50
                self.hitbox = pygame.Rect(int(self.x)+20, int(self.y), 95, 50)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.right:
                    win.blit(crouch[self.crouchCount//1], (int(self.x - 50), int(self.y - 57)))
                    self.crouchCount += 1
                    if self.shield:
                            win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 50), int(self.y - 5)))
                            self.shieldCount += 1
                if self.left:
                    win.blit(crouch2[self.crouchCount//1], (int(self.x - 15), int(self.y - 57)))
                    self.crouchCount += 1
                    if self.shield:
                            win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 20), int(self.y - 5)))
                            self.shieldCount += 1

            elif self.crouchATK: 
                self.y = self.y + 50
                self.hitbox = pygame.Rect(int(self.x)+20, int(self.y), 30, 50)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.right:
                    win.blit(SquatAtkR[self.crouchATKcount//1], (int(self.x), int(self.y)))
                    self.crouchATKcount += 1
                if self.left:
                    win.blit(SquatAtkL[self.crouchATKcount//1], (int(self.x), int(self.y)))
                    self.crouchATKcount += 1
                
            elif self.attacking:
                self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 96)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                if self.right:
                    win.blit(ALKattack[self.attackCount//1], (int(self.x - 50), int(self.y - 25)))
                    self.attackCount += 1
                if self.left:
                    self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 100)
                    win.blit(ALKattackLeft[self.attackCount//1], (int(self.x - 150), int(self.y - 25)))
                    self.attackCount += 1
                    
            else:       
                if self.idle1:
                    b = random.randrange(0,1)
                    if self.right:
                        self.hitbox = pygame.Rect(int(self.x), int(self.y), 50, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        if b == 0:
                            win.blit(idle1R[self.idle1Count//1], (int(self.x), int(self.y)))
                            self.idle1Count += 1
                            if self.shield:
                                self.idle1 = True
                                win.blit(AlucardShieldR[self.shieldCount//1], (int(self.x + 25), int(self.y + 10)))
                                self.shieldCount += 1
                        if b == 1:
                            win.blit(idle2R[self.idle1Count//1], (int(self.x), int(self.y)))
                            self.idle1Count += 1
                            
                    if self.left:
                        self.hitbox = pygame.Rect(int(self.x), int(self.y), 50, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        if b == 0:
                            win.blit(idle1L[self.idle1Count//1], (int(self.x), int(self.y)))
                            self.idle1Count += 1
                            if self.shield:
                                win.blit(AlucardShieldL[self.shieldCount//1], (int(self.x - 15), int(self.y + 10)))
                                self.shieldCount += 1
                        if b == 1:
                            win.blit(idle2L[self.idle1Count//1], (int(self.x), int(self.y)))
                            self.idle1Count += 1
                else:
                    if self.left:
                            self.hitbox = pygame.Rect(int(self.x), int(self.y), 30, 96)
                            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                            win.blit(char2[self.idleCount//3], (int(self.x), int(self.y)))
                            self.idleCount += 1
                    else:
                        self.hitbox = pygame.Rect(int(self.x)+4, int(self.y), 35, 96)
                        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                        win.blit(char[self.idleCount//3], (int(self.x), int(self.y)))
                        self.idleCount += 1

#===========BAT Animation==================================================
        else:
            self.y -= 10
            if self.right:
                self.hitbox = pygame.Rect(int(self.x)+4, int(self.y), 35, 50)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                win.blit(AlucardBatR[self.batCount//3], (int(self.x), int(self.y)))
                self.batCount += 1
            if self.left:
                self.hitbox = pygame.Rect(int(self.x)+4, int(self.y), 35, 50)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                win.blit(AlucardBatL[self.batCount//3], (int(self.x), int(self.y)))
                self.batCount += 1



    def hit(self):

#just one if statement:
#if player's x > enemy's x, player gets moved positive x; else, player gets moved negative x

        b = random.randrange(0,4)
        if b == 0:
            SOUNDS_A[1].play()
        elif b == 1:
            SOUNDS_A[2].play()
        elif b == 2:
            SOUNDS_A[3].play()
        elif b == 3:
            SOUNDS_A[4].play()
        elif b == 4:
            SOUNDS_A[5].play()   
            # if damage + man.health//4 : ALUK.6play() # its high damageTaken hit sound
        self.isJump = False
        self.jumpCount = 10
        global bgX
        global bgXmountain
        global scrollingOn
        global platformsA
##        for d in Dhurons:
##            if self.x < d.x:
##                self.damageL = True
##                self.damageR = False
##            elif self.x > d.x:
##                self.damageR = True
##                self.damageL = False
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render('-5', 1, (255,0,0))
        if self.right == True:
            win.blit(text, ((int((self.x + 10)+ self.width//2)), (int(self.y - self.height//2))))
        elif self.left == True:
            win.blit(text, ((int((self.x - 50)+ self.width//2)), (int(self.y - self.height//2))))
        pygame.display.flip()
        i = 0
        while i < 300:
            pygame.time.delay(0)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 0
                    run = False
                    #pygame.quit()
        if Alucardhealth <= 0:
            ALK15.play() # this is not playing , i think it quits too fast , check later. but maybe if i
            ALK14.play() # just make it not quit the game and rather go to a game over screen i think it will work fine.
            run = False
            #pygame.quit() # maybe if i use a counter,like the time
            #sys.exit()

    def gravity(self):
        if gravity == True:
            if AlucardMenuOn == False:
                self.y += 10
            if self.y > 585 and self.y >= 0:
                self.y = 585
                
man = player(5-scroll[0], 557-scroll[1], 50, 95)

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============== DHURON =========================
class Dhuron(object):
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
        self.hitbox = pygame.Rect(self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.alive = True
        self.explode = False
        self.explodeCount = 0
        self.respawnCount = 0
        
        self.defense = 5
#===============================================
#===============================================
#========== DAMAGE NUMBERS =====================
#===============================================
#===============================================
        self.damage = (man.atk - self.defense)
        self.damageX = self.x + 3
        self.damageEnd = (self.damageX + 20)
        self.damagePath = [self.damageX, self.damageEnd]
        self.damaged = False
        self.fadingCount = 0

    def hit(self):
        if self.visible and self.damaged == False:
            self.damaged = True
            b = random.randrange(0,1)
            if b == 0:
                SOUNDS_A[24].play()
            if b == 1:
                SOUNDS_A[25].play()
            if self.health > 1:
                self.health -= self.damage
            else:
                self.alive = False
                SOUNDS_A[28].play()
                SOUNDS_A[29].play()

    def draw(self,win):
        self.move()

        if self.fadingCount + 1 >= 30:
            self.damaged = False
            self.fadingCount = 0

        if self.damaged:
            self.fadingCount += 1
            for i, d in enumerate(str(self.damage)):
              win.blit(NumDamage[d], (int(self.damageX), int(self.y -10)))
          
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
                if self.walkCount + 1 >= 27:
                    self.walkCount = 0
                if self.atkCount + 1 > 8 and self.atkCount +1 < 10:
                    SOUNDS_A[30].play()
                if self.atkCount + 1 >= 26:
                    self.atkCount = 0

                if self.vel > 0:
                    if self.path[0] <= man.x and man.x <= self.end and man.x >= self.x:
                        win.blit(DhuronAttackR[self.atkCount//2], (int(self.x), int(self.y)))
                        self.atkCount += 1
                    else:
                        win.blit(DhuronWalkR[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1

                else:
                    if self.path[0] <= man.x and man.x <= self.end and man.x <= self.x:
                        win.blit(DhuronAttackL[self.atkCount//2], (int(self.x), int(self.y)))
                        self.atkCount += 1
                    else:
                        win.blit(DhuronWalkL[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1

                #pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                #pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = pygame.Rect(self.x + 5, self.y + 2, 60, 100)
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
#============== CLASSES ========================
#===============================================
#============== TIGER =========================
class Tiger(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.left = False
        self.right = False
        self.leftAtk = False
        self.rightAtk = False
        self.atkCount = 0
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = pygame.Rect(self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.alive = True
        self.explode = False
        self.explodeCount = 0

    def draw(self,win):
        self.move()
        if self.visible:
            if self.alive:
                if self.walkCount + 1 >= 69:
                    self.walkCount = 0
                if self.atkCount + 1 > 8 and self.atkCount +1 < 10:
                    SOUNDS_A[30].play()
                if self.atkCount + 1 >= 50:
                    self.atkCount = 0

                if self.vel > 0:
                    if self.path[0] <= man.x and man.x <= self.end and man.x >= self.x:
                        win.blit(tigerAtkR[self.atkCount//2], (int(self.x), int(self.y)))
                        self.atkCount += 1
                    else:
                        win.blit(tigerIdleR[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1

                else:
                    if self.path[0] <= man.x and man.x <= self.end and man.x <= self.x:
                        win.blit(tigerAtkL[self.atkCount//2], (int(self.x), int(self.y)))
                        self.atkCount += 1
                    else:
                        win.blit(tigerIdleL[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1

                pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = pygame.Rect(self.x + 5, self.y + 2, 60, 100)
                pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            else:
                if self.explodeCount + 1 >= 36:
                    self.explodeCount = 0
                    global AlucardKill
                    global AlucardExp
                    global AlucardNextLevel
                    
                    AlucardKill += 1
                    AlucardExp += 4
                    AlucardNextLevel -= 4
                        
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

    def hit(self):
        if self.visible:
            b = random.randrange(0,1)
            if b == 0:
                SOUNDS_A[24].play()
            if b == 1:
                SOUNDS_A[25].play()
            if self.health > 1:
                self.health -= 1
            else:
                self.alive = False
                SOUNDS_A[28].play()
                SOUNDS_A[29].play()

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============ grasshopper ======================
class grasshopper(object):
    walkRight = grasshopper
    walkLeft = grasshopperAttack
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 10
        self.hitbox = pygame.Rect(int(self.x) + 17, int(self.y) + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //5], (int(self.x), int(self.y)))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //5], (int(self.x), int(self.y)))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = pygame.Rect(self.x + 5, self.y + 2, 60, 100)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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

    def hit(self):
        b = random.randrange(0,1)
        if b == 0:
            SOUNDS_A[24].play()
        if b == 1:
            SOUNDS_A[25].play()
        if self.health > 1:
            self.health -= 5
        else:
            self.visible = False

#===============================================
#===============================================
#============== CLASSES ========================
#===============================================
#============== GARGOYLE =======================
class Gargoyle(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.left = False
        self.right = False
        self.leftAtk = False
        self.rightAtk = False
        self.atkCount = 0
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = pygame.Rect(self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 20:
                self.walkCount = 0
            if self.atkCount + 1 > 8 and self.atkCount +1 < 10:
                SOUNDS_A[30].play()
            if self.atkCount + 1 >= 12:
                self.atkCount = 0

            if self.vel > 0:
                if self.path[0] <= man.x and man.x <= self.end and man.x >= self.x:
                    win.blit(gargoyleAtk[self.atkCount//4], (int(self.x), int(self.y)))
                    self.atkCount += 1
                else:                        
                    win.blit(gargoyleWalk[self.walkCount//4], (self.x, self.y))
                    self.walkCount += 1

            else:
                if self.path[0] <= man.x and man.x <= self.end and man.x <= self.x:
                    win.blit(gargoyleAtkLeft[self.atkCount//4], (int(self.x), int(self.y)))
                    self.atkCount += 1
                else:                        
                    win.blit(gargoyleWalkLeft[self.walkCount //4], (self.x, self.y))
                    self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = pygame.Rect(self.x + 5, self.y + 2, 60, 100)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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

    def hit(self):
        b = random.randrange(0,1)
        if b == 0:
            SOUNDS_A[24].play()
        if b == 1:
            SOUNDS_A[25].play()
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
        
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
#========= DOORS ==================
class doors(object):
    def __init__(self, x, y, width, height, destX, destY, doorNumber, Fnumber):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
        self.visible = True
        self.destX = destX
        self.destY = destY
        self.doorNumber = doorNumber
        self.Fnumber = Fnumber
        
    def draw(self,win):
        if self.visible:
            self.hitbox = pygame.Rect(int(self.x), int(self.y), int(self.width), int(self.height))
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

##    def hit(self):
##        if man.hitbox.colliderect(self.hitbox):
##            for a in bgList:
##                a = False
##                bgList[self.doorNumber] = True
##                man.draw(win)
##                man.x = self.destX
##                man.y = self.destY
##                print(self.destX)
##                print(self.destX)
##                print(bgList[self.doorNumber])
##                #pygame.mixer.music.stop()
##                #musicList = [music1,2,3,4]
##                #music1 = (f'DATA/SOUNDS/MUSIC/1.wav')
##                #pygame.mixer.music.load(musicList[doorNumber]) # or door music , if door music = Change.
##                #pygame.mixer.music.play(-1) 

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
            b = random.randrange(0,1)
            if b == 0:
                SOUNDS_A[24].play()
            if b == 1:
                SOUNDS_A[25].play()
        
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
    def __init__(self, x, y, img, name, description):
        global items
        self.x = x
        self.y = y
        self.img = items[img]
        self.hitbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
        self.visible = False
        self.name = str(name)
        self.description = str(description)

    def draw(self,win):
        self.y += 10
        if self.visible == False:
            win.blit(items[0], (self.x, self.y))
            self.hitbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        else:
            win.blit(img, (int(self.x), int(self.y)))
            self.hitbox = pygame.Rect(int(self.x), int(self.y), 16, 30)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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
bgX = 0 #bg1
bgXmountain = 0 #bg1

bg1BX = 0 #bg1B
bg1BXmountain = 0 #bg1B
bg1BY = 0#-205 #bg1B -645

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
            Dhuron1.draw(win)
            Dhuron2.draw(win)
            Dhuron3.draw(win)
            Dhuron4.draw(win)
            Dhuron5.draw(win)
            bg1doorA1.draw(win)

            item000.draw(win)

            bg1ground.visible = True
            bg1ground.draw(win)
            # platformsA
            for a in bg1platforms:
                a.visible = True
                a.draw(win)

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
            
        if background1B:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X1PR1, (0, 0))
            win.blit(X1PR2, (0, 0))
            win.blit(X1PR3, (int(bg1BXmountain), 0))
            win.blit(bg1B, (int(bg1BX), int(bg1BY)))
            Tiger1.draw(win)

            for a in bg1Bplatforms:
                a.visible = True
                a.draw(win)
            
            bg1ground1B.visible = True
            bg1ground1B.draw(win)

    #========================================================
    #====================================== 2 ==================
        if background2:
            for a in platformsA:
                a.visible = False
            for a in grounds:
                a.visible = False
            win.blit(X2PR1, (0-scroll[0],0-scroll[1]))
            win.blit(bg2, (0,0))
            grasshop1.draw(win)
            Gargoyle1.draw(win)
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
        man.draw(win)
        Alucardspeech01 = True
        
##        win.blit(ITEMpotion, (1240,595)) #  win blit selected item 1,2,3,4 if not , blit 0. something like that
        win.blit(SUBMENU[0], (1215,575))
                 
    else:
        if AlucardEquipMenuOn:
            TIME.on()
            win.blit(AlucardEquipMenu, (0, 0))
            AllParallaxes.draw(win)
            AllParallaxes.MpFullDisplay = False
            AllParallaxes.equipHoverDisplay = False
            AllParallaxes.inventHoverDisplay = True
            if AlucardInventoryOn:
                AllParallaxes.inv = True
                TIME.on()
                win.blit(AlucardEquipMenu, (0, 0))
                AllParallaxes.draw(win)
                AllParallaxes.MpFullDisplay = False
                AllParallaxes.equipHoverDisplay = False
                AllParallaxes.inventHoverDisplay = True
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


    pygame.display.flip()
    
#=============================================================================================================================================================
#=============================================================================================================================================================
#==================================================================================== VARIABLES ==============================================================
#=============================================================================================================================================================
#=============================================================================================================================================================
#theForest = parallax(0, 0, 0, 0) # --------- to use later.
#theBg3Pillars = parallax(0, 0, 0, 0) # ---------- to use later.

#==================================
font = pygame.font.SysFont('comicsans', 30, True)
AllParallaxes = parallax(0, 0, 0, 0)
TIME = time(0, 0, 0, 0)

# items
item000 = itemCLASS(300, 200, 0, 'emptyHand', 'Nothing')

# bacground 1
bg1ground = block(-670, 648, 6510, 1) #  if bg8ground.x >= -10659 and bg8ground.x <= -1339:    #4560  10720
bg1pa1 = block(245, 577, 240, 1)
bg1pa2 = block(523, 485, 240, 1)
bg1pa3 = block(799, 398, 1039, 1)
bg1pa4 = block(1877, 485, 240, 1)
bg1pa5 = block(2158, 555, 240, 1)
bg1pa6 = block(2845, 551, 156, 1)
bg1pa7 = block(2994, 454, 460, 1)
bg1pa8 = block(3462, 551, 146, 1)

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

Dhuron1 = Dhuron(500, 558, 50, 95, 1250, 500)
Dhuron2 = Dhuron(400, 558, 50, 95, 1250, 400)
Dhuron3 = Dhuron(300, 558, 50, 95, 1250, 300)
Dhuron4 = Dhuron(1885, 390, 50, 95, 2115, 1885)
Dhuron5 = Dhuron(3000, 359, 50, 95, 3447, 3000)
#bg1doorA1 = block(1300, 500, 50, 100)
bg1doorA1 = doors(1300, 500, 50, 100, 35, 565, 1, 0)

Tiger1 = Tiger(500, 300, 50, 95, 1250)

# bacground 1B
bg1ground1B = block(-670, 648, 6510, 1)

bg1Bpa1 = block(0, 683, 2011, 1)
bg1Bpa2 = block(288, 633, 25, 1)
bg1Bpa3 = block(433, 511, 25, 1)
bg1Bpa4 = block(518, 431, 25, 1)
bg1Bpa5 = block(575, 356, 112, 1)
bg1Bpa6 = block(739, 259, 25, 1)
bg1Bpa7 = block(719, 431, 25, 1)
bg1Bpa8 = block(804, 511, 25, 1)
bg1Bpa9 = block(949, 633, 25, 1)
bg1Bpa10 = block(371, 579, 520, 1)
bg1Bpa11 = block(2292, 685, 1143, 1)
bg1Bpa12 = block(3733, 684, 867, 1)
bg1Bpa13 = block(1142, 370, 573, 1)
bg1Bpa14 = block(1903, 400, 238, 1)
bg1Bpa15 = block(2402, 243, 943, 1)
bg1Bpa16 = block(1723, 1071, 589, 1)
bg1Bpa17 = block(2577, 1068, 292, 1)
bg1Bpa18 = block(3108, 1072, 292, 1)
bg1Bpa19 = block(3561, 1074, 292, 1)
bg1Bpa20 = block(3946, 1076, 600, 1)
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

# background 2b

bg2Bpa1 = block(0, 545, 891, 1)

                                                                  
# bacground 2
bg2doorB1 = block(15, 550, 20, 200)
#bg2doorB1 = doors(15, 550, 20, 200, 1250, 585, 3)
bg2groundB = block(0, 670, 1340, 1)
bg2pa1 = block(779, 600, 207, 1) # stone
bg2pa2 = block(866, 532, 123, 1) # first step
bg2pa3 = block(691, 460, 139, 1) # second step
bg2pa4 = block(908, 368, 600, 1) # roof
grasshop1 = grasshopper(200, 600, 50, 95, 1250)
bg2doorA1 = block(1320, 585, 40, 100)
bg2doorA2 = block(1320, 368, 600, 1)
#bg2doorA1 = doors(1320, 585, 40, 100, 35, 585, 4)
#bg2doorA2 = doors(1320, 368, 600, 1, 35, 585, 19)


# background 3
bg3doorB1 = block(15, 550, 20, 200)
#bg3doorB1 = doors(15, 550, 20, 200, 1257, 585, 3)
bg3groundB = block(0, 670, 1340, 1)
bg3doorA1 = block(1328, 600, 30, 80)                         # it doesnt look very good.....
#bg3doorA1 = doors(1328, 600, 30, 80, 35, 585, 5)

# background 4
bg4doorB1 = block(15, 550, 20, 200)
#bg4doorB1 = block(15, 550, 20, 200)
bg4doorA1 = block(900, 0, 30, 800)
#bg4doorA1 = block(900, 0, 30, 800)
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
Gargoyle1 = Gargoyle(500, 558, 50, 95, 1250)


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
# ------------------------------------ ====
#     ------ VAR LISTS ------------ =======
# ------------------------------------ ====
# blocks lists
platformsA = [bg1pa1, bg1pa2, bg1pa3, bg1pa4, bg1pa5, bg1pa6, bg1pa7, bg1pa8, bg2groundB, bg2pa1, bg2pa2, bg2pa3, bg2pa4, bg3groundB, bg5pa1, bg5pa2, bg5pa3, bg5pa4, bg8pa1, bg8pa2, bg8pa3, bg8pa4, bg8pa5, bg8pa6, bg8pa7, bg8pa8, bg8pa9, bg8pa10, bg8pa11, bg8pa12, bg8pa13, bg8pa14, bg8pa15, bg8pa16, bg8pa17, bg8pa18, bg8pa19, bg8pa20, bg8pa21, bg8pa22, bg8pa23, bg8pa24, bg8pa25, bg8pa26, bg8pa27, bg8pa28, bg8pa29, bg8pa30, bg8pa31, bg8pa32, bg8pa33, bg8pa34, bg8pa35, bg8pa36]
bg1platforms = [bg1pa1, bg1pa2, bg1pa3, bg1pa4, bg1pa5, bg1pa6, bg1pa7, bg1pa8]
bg1Bplatforms = [bg1Bpa1, bg1Bpa2, bg1Bpa3 ,bg1Bpa4, bg1Bpa5, bg1Bpa6, bg1Bpa7, bg1Bpa8, bg1Bpa9, bg1Bpa10, bg1Bpa11, bg1Bpa12, bg1Bpa13, bg1Bpa14, bg1Bpa15, bg1Bpa16, bg1Bpa17, bg1Bpa18, bg1Bpa19, bg1Bpa20, bg1Bpa21, bg1Bpa22, bg1Bpa23, bg1Bpa24, bg1Bpa25, bg1Bpa26, bg1Bpa27, bg1Bpa28, bg1Bpa29, bg1Bpa30, bg1Bpa31, bg1Bpa32, bg1Bpa33, bg1Bpa34, bg1Bpa35, bg1Bpa36, bg1Bpa37, bg1Bpa38, bg1Bpa39]
bg8platforms = [bg8pa1, bg8pa2, bg8pa3, bg8pa4, bg8pa5, bg8pa6, bg8pa7, bg8pa8, bg8pa9, bg8pa10, bg8pa11, bg8pa12, bg8pa13, 14, bg8pa15, bg8pa16, bg8pa17, bg8pa18, bg8pa19, bg8pa20, bg8pa21, bg8pa22, bg8pa23, bg8pa24, bg8pa25, bg8pa26, bg8pa27, bg8pa28, bg8pa29, bg8pa30, bg8pa31, bg8pa32, bg8pa33, bg8pa34, bg8pa35, bg8pa36]


grounds = [bg1ground, bg1ground1B, bg6ground, bg8ground, bg10ground, bg11ground, bg12ground, bg13ground, bg16ground, bg18ground, bg19ground, bg20ground, bg21ground, bg22ground, bg24ground]
#platformsB = [pb1, pb2, pb3...]
doors = [bg1doorA1, bg2doorA1, bg2doorA2, bg3doorA1, bg4doorA1, bg5doorA1, bg5doorA2, bg7doorA1, bg6doorA1, bg6doorA2, bg6doorA3, bg8doorA1, bg10doorA1, bg11doorA1, bg12doorA1, bg12doorA2, bg16doorA1, bg18doorA1, bg19doorA1, bg20doorA1, bg21doorA1, bg21doorA2, bg22doorA1, bg23doorA1, bg31doorA1]
doorsB = [bg2doorB1, bg3doorB1, bg4doorB1, bg5doorB1,bg6doorB1, bg7doorB1, bg8doorB1, bg9doorB1, bg18doorB1, bg10doorB1, bg10doorB2, bg11doorB1, bg12doorB1, bg13doorB1, bg18doorB1, bg19doorB1, bg20doorB1, bg21doorB1, bg24doorB1, bg16doorB1, bg17doorB1, bg22doorB1, bg23doorB1, bg31doorB1]
#walls = [bg1wallB1, bg1wallA1]

# Misc lists
candles = [bg1CD1, bg1CD2, bg1CD3, bg1CD4, bg1CD5]
allHearts = [bg1HT1, bg1HT2, bg1HT3, bg1HT4, bg1HT5]
itemsList = [item000]

# enemies lists
Dhurons = [Dhuron1, Dhuron2, Dhuron3, Dhuron4, Dhuron5]
Gargoyles = [Gargoyle1]

# end of enemies list with all enemies on a list
enemies = [Dhurons] # enemies [Dhurons, wolves, fairies...]

#======================================================================================================================================================================
#======================================================================================================================================================================
#============= MAIN LOOP ==============================================================================================================================================
#======================================================================================================================================================================
#======================================================================================================================================================================
while run:
    redrawGameWindow()
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
#================ ITEMS ========================
    for b in itemsList:
        for a in platformsA:
##        for a in platformsA, bg1Bplatforms, grounds:
            if b.hitbox.colliderect(a.hitbox):
                if a.visible:
                      b.y = a.y - 39

##    for d in itemsList:
##            if man.hitbox[1] < d.hitbox[1] + d.hitbox[3] and man.hitbox[1] + man.hitbox[3] > d.hitbox[1]:
##              if man.hitbox[0] + man.hitbox[2] > d.hitbox[0] and man.hitbox[0] < d.hitbox[0] + d.hitbox[2]:
##                  
                  #make item appear on inventory
                  
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
#================ GARGOYLE =====================
    for d in Gargoyles:
        if d.visible == True:
            if man.hitbox.colliderect(d.hitbox):
                  if background2 == True:
                      man.hit()
    for d in Gargoyles:
        if d.visible == True:
            if man.atkbox.colliderect(d.hitbox):
                  if background2 == True:
                      d.hit()
            
#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#================ DHURONS ======================
    for d in Dhurons:
        if d.visible == True and d.alive == True:
            if man.hitbox.colliderect(d.hitbox):
                if background1 == True:
                    man.hit()
                    if man.x < d.x:
                        man.damageL = True
                        #man.damageR = False
                    elif man.x > d.x:
                        man.damageR = True
                        #man.damageL = False
    for d in Dhurons:
        if d.visible == True:
            if man.atkbox.colliderect(d.hitbox):
                  if background1 == True:
                      d.hit()
                  
#===============================================
#===============================================
#=============== COLLISIONS ====================
#===============================================
#============== GRASSHOPPER ====================
    if grasshop1.visible == True:
         if man.hitbox.colliderect(grasshop1.hitbox):
                 if background2 == True:
                     man.hit()
                     Alucardhealth -= 5

    if grasshop1.visible == True:
         if man.atkbox.colliderect(grasshop1.hitbox):
                 if background2 == True:
                     grasshop1.hit()
                     
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
    if man.hitbox.colliderect(bg1doorA1.hitbox):
        if background1 == True:
                man.draw(win)
                man.x = 35
                man.y = 565
                background1B = True
                background3 = False
                background1 = False
                pygame.mixer.music.stop()
                pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/1.wav')
                pygame.mixer.music.play(-1)
####        bgList[bg1doorA1.Fnumber] = False
####        bgList[bg1doorA1.doorNumber] = True
####        man.draw(win)
####        man.x = bg1doorA1.destX
####        man.y = bg1doorA1.destY
####        print(bg1doorA1.destX)
####        print(bg1doorA1.destY)
        #print(bgList[bg1doorA1.doorNumber])
        #pygame.mixer.music.stop()
        #musicList = [music1,2,3,4]
        #music1 = (f'DATA/SOUNDS/MUSIC/1.wav')
        #pygame.mixer.music.load(musicList[doorNumber]) # or door music , if door music = Change.
        #pygame.mixer.music.play(-1) 


#=============== bg2doorB1 =====================
    if man.hitbox.colliderect(bg2doorB1.hitbox):
              if background2 == True:
                  man.draw(win)
                  man.x = 1250
                  man.y = 585
                  background2 = False
                  background1 = True
                  pygame.mixer.music.stop()
                  pygame.mixer.music.load(f'DATA/SOUNDS/MUSIC/0.wav')
                  pygame.mixer.music.play(-1)
                  
#=============== bg2doorA1 =====================
    if man.hitbox.colliderect(bg2doorA1.hitbox):
              if background2 == True:
                  man.draw(win)
                  man.x = 35
                  man.y = 585
                  background3 = True
                  background2 = False
                  background4 = False
                  #theBg3Pillars.Bg3Pillars = True

#=============== bg2doorA2 =====================
    if man.hitbox.colliderect(bg2doorA2.hitbox):
              if background2 == True:
                  man.draw(win)
                  man.x = 35
                  man.y = 585
                  background18 = True
                  background2 = False
                  background4 = False
                      
#=============== bg3doorB1 =====================
    if man.hitbox.colliderect(bg3doorB1.hitbox):
              if background3 == True:
                  man.draw(win)
                  man.x = 1257
                  man.y = 585
                  background2 = True
                  background3 = False
                  #theBg3Pillars.Bg3Pillars = False
   
#================ bg3doorA1 ====================
    if man.hitbox.colliderect(bg3doorA1.hitbox):
              if background3 == True:
                  if background4 == False:
                      man.draw(win)
                      man.x = 35
                      man.y = 585
                      background4 = True
                      background3 = False
                      background5 = False
                      #theBg3Pillars.Bg3Pillars = False

#=============== bg4doorB1 =====================
    if man.hitbox.colliderect(bg4doorB1.hitbox):
              if background4 == True:
                  man.draw(win)
                  man.x = 1265
                  man.y = 585
                  background4 = False
                  background3 = True
                  #theBg3Pillars.Bg3Pillars = True

#=============== bg4doorA1 =====================
    if man.hitbox.colliderect(bg4doorA1.hitbox):
              if background4 == True:
                  if background5 == False:
                      man.draw(win)
                      man.x = 261
                      man.y = 585
                      background5 = True
                      background4 = False
                      background6 = False

#=============== bg5doorB1 =====================
    if man.hitbox.colliderect(bg5doorB1.hitbox):
              if background5 == True:
                  man.draw(win)
                  man.x = 850
                  man.y = 585
                  background5 = False
                  background4 = True

#=============== bg5doorA1 =====================
    if man.hitbox.colliderect(bg5doorA1.hitbox):
              if background5 == True:
                  if background6 == False:
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
                      man.x = 1245
                      man.y = 264
                      background5 = True
                      background7 = False
                      background8 = False

#=============== bg7doorA1 =====================
    if man.hitbox.colliderect(bg7doorA1.hitbox):
              if background7 == True:
                  if background8 == False:
                      man.draw(win)
                      man.x = 163
                      man.y = 585
                      background8 = True
                      background7 = False
                      background5 = False

#=============== bg8doorB1 =====================
    if man.hitbox.colliderect(bg8doorB1.hitbox):
              if background8 == True:
                  if background7 == False:
                      man.draw(win)
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
                      man.draw(win)
                      man.x = 400
                      man.y = 400
                      background6 = True
                      background5 = False
                      background9 = False

#=============== bg10doorB1 ====================
    if man.hitbox.colliderect(bg10doorB1.hitbox):
              if background10 == True:
                  if background6 == False:
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
                      man.draw(win)
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
#=============== KEYS ===================================================================================================
#========================================================================================================================
#========================================================================================================================
    keys = pygame.key.get_pressed()

#===============================================
#===============================================
#========= KEYS - ATK SWORD ====================
#===============================================
#===============================================
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_KP7] or keys[pygame.K_x] and man.attackCount == 0:
            if AlucardMenuOn == False:
                man.attacking = True #SquatAtkR

                if man.attacking == True and man.attackCount == 0:
                    r = random.randrange(0,3)
                    if r == 0:
                        SOUNDS_A[7].play()
                    elif r == 1:
                        SOUNDS_A[8].play()
                    elif r == 2:
                        SOUNDS_A[9].play()
                    elif r == 3:
                        SOUNDS_A[10].play()

        else:
            man.crouchATK = False
            man.attacking = False
            man.attackCount = 0
            
#===============================================
#===============================================
#=============== KEYS - ESQ ====================
#===============================================
#===============================================
    if keys[pygame.K_ESCAPE]:
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
    if keys[pygame.K_f]:
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
    if man.damageCount >= 10:
        man.damageL = False
        man.damageR = False
        man.damageCount = 0
    if man.damageL == True or man.damageR == True:
        man.damageCount += 1
#===============================================
#===============================================
#=============== KEYS - LEFT ===================
#===============================================
#===============================================
    if keys[pygame.K_LEFT] and man.x > man.vel or keys[pygame.K_a] and man.x > man.vel or man.damageL == True and man.x > man.vel:
        if AlucardMenuOn == False:
            man.x -= 10
            for a in grounds:
                if a.visible == True:
                    a.x += man.vel
                    if scrollingOn == True:
                        Dhuron1.path = (int(bg1ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron2.path = (int(bg1ground.x + 670 + 660 + 400), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron3.path = (int(bg1ground.x + 670 + 660 + 300), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron4.path = (int(bg1ground.x + 670 + 660 + 1885), (bg1ground.x + 670 + 660 + 2085)) # 1885 is the initial Dhuron.x and 2115 is the Dhuron initial final destination
                        Dhuron5.path = (int(bg1ground.x + 670 + 660 + 3000), (bg1ground.x + 670 + 660 + 3417))
                        for a in allHearts:
                            a.path = (int(bg1ground.x + 670 + 660 + (a.end - 20)), (bg1ground.x + 670 + 660 + a.end))
                        #background8
                        #Gargoyle1.path = (int(bg8ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))                    
            if scrollingOn == False:
                for d in candles:
                    d.x = d.x
                for a in bg1platforms:
                    a.x = a.x
                for e in Dhurons:
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
    elif keys[pygame.K_RIGHT] and man.x < 1340 - man.width - man.vel or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel or man.damageR == True and man.x < 1340 - man.width - man.vel:
        if AlucardMenuOn == False:
            man.x += 10
            for a in grounds:
                if a.visible == True:
                    a.x -= man.vel
                    if scrollingOn == True:
                        Dhuron1.path = (int(bg1ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron2.path = (int(bg1ground.x + 670 + 660 + 400), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron3.path = (int(bg1ground.x + 670 + 660 + 300), (bg1ground.x + 670 + 660 + 1250))
                        Dhuron4.path = (int(bg1ground.x + 670 + 660 + 1885), (bg1ground.x + 670 + 660 + 2085)) # 1885 is the initial Dhuron.x and 2115 is the Dhuron initial final destination
                        Dhuron5.path = (int(bg1ground.x + 670 + 660 + 3000), (bg1ground.x + 670 + 660 + 3417))
                        for a in allHearts:
                            a.path = (int(bg1ground.x + 670 + 660 + (a.end - 20)), (bg1ground.x + 670 + 660 + a.end))
                        #background8
                        #Gargoyle1.path = (int(bg8ground.x + 670 + 660 + 500), (bg1ground.x + 670 + 660 + 1250))                    
            if scrollingOn == False:
                for d in candles:
                    d.x = d.x
                for a in bg1platforms:
                    a.x = a.x
                for e in Dhurons:
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
#============== KEYS - JUMP ====================
#===============================================
#===============================================
    if not(man.isJump):
        if keys[pygame.K_SPACE] and plat == True or keys[pygame.K_KP0] and plat == True:
            if AlucardMenuOn == False:
                man.isJump = True
                man.walkCount = 0
    else:
        if AlucardMenuOn == False:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            
            else:
                man.isJump = False
                man.jumpCount = 10

#===============================================
#===============================================
#============ KEYS - MENU SELECT ===============
#===============================================
#===============================================
    if keys[pygame.K_SPACE] or keys[pygame.K_KP0] and AlucardMenuOn == True:
        if equipHover == bar:
            equipHover = equipSelect
        if inventHover == barEquip:
            inventHover = inventSelect 
        if invHover == barInv:
            invHover = invSelect 

    if equiping >= 21:
        equiping = 0
        equipHover = bar
        inventHover = barEquip
        invHover = barInv
##        AlucardEquipMenuOn = True
        AlucardEquipMenuOn = not AlucardEquipMenuOn
        AllParallaxes.inventHoverDisplay = not AllParallaxes.inventHoverDisplay
        if AlucardEquipMenuOn:
            AlucardEquipMenuOn = True
        else:
            AlucardEquipMenuOn = False

    if equipHover == equipSelect:
        equiping += 1
        

#===============================================
#===============================================
#============ KEYS - INVT SELECT ===============
#===============================================
#===============================================
    if keys[pygame.K_SPACE] or keys[pygame.K_KP0] and AlucardInventoryOn == True:
        if equipHover == bar:
            equipHover = equipSelect
        if inventHover == barEquip:
            inventHover = inventSelect 
        if invHover == barInv:
            invHover = invSelect 

    if equiping >= 21:
        equiping = 0
        equipHover = bar
        inventHover = barEquip
        invHover = barInv
##        AlucardEquipMenuOn = True
        AlucardInventoryOn = not AlucardInventoryOn 
        AllParallaxes.inv = not AllParallaxes.inv
        if AlucardInventoryOn:
            AlucardInventoryOn = True
        else:
            AlucardInventoryOn = False

    if equipHover == equipSelect:
        equiping += 1

        
#===============================================
#===============================================
#=============== KEYS - CROUCH =================
#===============================================
#===============================================
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if AlucardInventoryOn:
            if positionTicks == 0:
                if invPos1 == True:
                    positionTick = True
                    invPos1 = False
                    invPos5 = True
                    inventoryHoverY = 448
                elif invPos2 == True:
                    positionTick = True
                    invPos2 = False
                    invPos6 = True
                    inventoryHoverY = 448
                elif invPos3 == True:
                    positionTick = True
                    invPos3 = False
                    invPos7 = True
                    inventoryHoverY = 448
                elif invPos4 == True:
                    positionTick = True
                    invPos4 = False
                    invPos8 = True
                    inventoryHoverY = 448
                elif invPos5 == True:
                    positionTick = True
                    invPos5 = False
                    invPos9 = True
                    inventoryHoverY = 493
                elif invPos6 == True:
                    positionTick = True
                    invPos6 = False
                    invPos10 = True
                    inventoryHoverY = 493
                elif invPos7 == True:
                    positionTick = True
                    invPos7 = False
                    invPos11 = True
                    inventoryHoverY = 493
                elif invPos8 == True:
                    positionTick = True
                    invPos8 = False
                    invPos12 = True
                    inventoryHoverY = 493
                elif invPos9 == True:
                    positionTick = True
                    invPos9 = False
                    invPos13 = True
                    inventoryHoverY = 536
                elif invPos10 == True:
                    positionTick = True
                    invPos10 = False
                    invPos14 = True
                    inventoryHoverY = 536
                elif invPos11 == True:
                    positionTick = True
                    invPos11 = False
                    invPos15 = True
                    inventoryHoverY = 536
                elif invPos12 == True:
                    positionTick = True
                    invPos12 = False
                    invPos16 = True
                    inventoryHoverY = 536
                    
        if AlucardEquipMenuOn:
            if positionTicks == 0:
                if equipPosition1 == True:
                    positionTick = True
                    equipPosition1 = False
                    equipPosition2 = True
                    equipHoverY = 94
                elif equipPosition2 == True:
                    positionTick = True
                    equipPosition2 = False
                    equipPosition3 = True
                    equipHoverY = 136
                elif equipPosition3 == True:
                    positionTick = True
                    equipPosition3 = False
                    equipPosition4 = True
                    equipHoverY = 179
                elif equipPosition4 == True:
                    positionTick = True
                    equipPosition4 = False
                    equipPosition5 = True
                    equipHoverY = 221
                elif equipPosition5 == True:
                    positionTick = True
                    equipPosition5 = False
                    equipPosition6 = True
                    equipHoverY = 259
                elif equipPosition6 == True:
                    positionTick = True
                    equipPosition6 = False
                    equipPosition7 = True
                    equipHoverY = 302
                elif equipPosition7 == True:
                    positionTick = True
                    equipPosition7 = False
                    equipPosition1 = True
                    equipHoverY = 52
                    
        elif AlucardMenuOn:
            if positionTicks == 0:
                if position1 == True:
                    positionTick = True
                    position1 = False
                    position2 = True
                    hoverY = 417
                elif position2 == True:
                    positionTick = True
                    position2 = False
                    position3 = True
                    hoverY = 468
                elif position3 == True:
                    positionTick = True
                    position3 = False
                    position4 = True
                    hoverY = 522
                elif position4 == True:
                    positionTick = True
                    position4 = False
                    position5 = True
                    hoverY = 579
                elif position5 == True:
                    positionTick = True
                    position5 = False
                    position1 = True
                    hoverY = 363
        else:
##            for a in mainMenuPositionList:
##                a = False
##            position1 = True
##            hoverY = 363
            if man.bat:
                man.y += 10
            else:
                man.crouching = True
                man.idleCount = 0
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_KP7] or keys[pygame.K_x] and man.attackCount == 0:
                        man.attacking = True #SquatAtkR
                                            
                        if man.attacking == True and man.crouchATKcount == 0 and man.crouching == True:
                            man.crouchATK = True
                            r = random.randrange(0,3)
                            if r == 0:
                                SOUNDS_A[7].play()
                            elif r == 1:
                                SOUNDS_A[8].play()
                            elif r == 2:
                                SOUNDS_A[9].play()
                            elif r == 3:
                                SOUNDS_A[10].play()
                        else:
                            man.crouchATK = False
    else:
        man.crouchCount = 0
        man.crouching = False

#===============================================
#===============================================
#=============== KEYS - SHIELD =================
#===============================================
#===============================================
    if keys[pygame.K_KP6] or keys[pygame.K_x]:
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
    if keys[pygame.K_KP9]:
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
    if keys[pygame.K_UP] or keys[pygame.K_w] and man.y > 0:
        if AlucardEquipMenuOn:
            if positionTicks == 0:
                if equipPosition1 == True:
                    positionTick = True
                    equipPosition1 = False
                    equipPosition7 = True
                    equipHoverY = 302
                elif equipPosition2 == True:
                    positionTick = True
                    equipPosition2 = False
                    equipPosition1 = True
                    equipHoverY = 52
                elif equipPosition3 == True:
                    positionTick = True
                    equipPosition3 = False
                    equipPosition2 = True
                    equipHoverY = 94
                elif equipPosition4 == True:
                    positionTick = True
                    equipPosition4 = False
                    equipPosition3 = True
                    equipHoverY = 136
                elif equipPosition5 == True:
                    positionTick = True
                    equipPosition5 = False
                    equipPosition4 = True
                    equipHoverY = 179
                elif equipPosition6 == True:
                    positionTick = True
                    equipPosition6 = False
                    equipPosition5 = True
                    equipHoverY = 221
                elif equipPosition7 == True:
                    positionTick = True
                    equipPosition7 = False
                    equipPosition6 = True
                    equipHoverY = 259  
            
        elif AlucardMenuOn:
            if positionTicks == 0:
                if position1 == True:
                    positionTick = True
                    position1 = False
                    position5 = True
                    hoverY = 579
                elif position2 == True:
                    positionTick = True
                    position2 = False
                    position1 = True
                    hoverY = 363
                elif position3 == True:
                    positionTick = True
                    position3 = False
                    position2 = True
                    hoverY = 417
                elif position4 == True:
                    positionTick = True
                    position4 = False
                    position3 = True
                    hoverY = 468
                elif position5 == True:
                    positionTick = True
                    position5 = False
                    position4 = True
                    hoverY = 522
        else:
            for a in mainMenuPositionList:
                a = False
            position1 = True
            hoverY = 363
            if man.bat:
                man.y -= 10
            else:
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
    if keys[pygame.K_KP_ENTER] and menuTicks == 0 or keys[pygame.K_RETURN] and menuTicks == 0:
        AlucardMenuOn = not AlucardMenuOn
        AllParallaxes.equipHoverDisplay = not AllParallaxes.equipHoverDisplay
        AllParallaxes.MpFullDisplay = not AllParallaxes.MpFullDisplay
        menuTicking = True
        if AlucardMenuOn:
            paused()
            AlucardMenuOn = True
        else:
            unpause()
            AlucardMenuOn = False
            for a in mainMenuPositionList:
                a = False
            position1 = True
            hoverY = 363
            #AlucardEquipMenuOn = False
            
    if menuTicks >= 15:
        menuTicks = 0
        menuTicking = False
    
    if menuTicking == True:
        menuTicks += 1

    if AlucardMenuOn == False:
        AlucardEquipMenuOn = False

#--------------------------------------------------------------
#----------------- PLATFORMS ----------------------------------
#--------------------- A --------------------------------------
    if fallTick >= 1:
        falling = True
        fallTick = 0
    if falling == False:
        fallTick += 1
    for a in platformsA:
        if neg == -1 and man.hitbox.colliderect(a.hitbox):
            if a.visible:
                man.y = a.y - 95
                plat = True
                falling = False
                man.fallCount = 0
                  
    for a in bg1Bplatforms:
        if background1B == True:
            if neg == -1 and man.hitbox.colliderect(a.hitbox):
                if a.visible:
                    man.y = a.y - 95
                    plat = True
                    falling = False
                    man.fallCount = 0
#--------------------------------------------------------------
#----------------- GROUNDS ----------------------------------
#--------------------------------------------------------------
    for a in grounds:
        if neg == -1 and man.hitbox.colliderect(a.hitbox):
            if a.visible:
                man.y = a.y - 95
                plat = True
                falling = False
                man.fallCount = 0

#--------------------------------------------------------------
#----------------- CAMERA ----------------------------------
#------------------- BG 1 -------------------------------------
    if background1:
        if bg1ground.x >= -4499 and bg1ground.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] and man.x > man.vel or keys[pygame.K_a] and man.x > man.vel or man.damageL == True and man.x > man.vel:
                bgX += man.vel
                bgXmountain += 2
                for a in bg1platforms:
                    a.x += man.vel
                for d in candles:
                    d.x += man.vel
                for e in Dhurons:
                    e.x += man.vel
                for a in allHearts:
                    a.x += man.vel

            elif keys[pygame.K_RIGHT] and man.x < 1340 - man.width - man.vel or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel or man.damageR == True and man.x < 1340 - man.width - man.vel:
                bgX -= man.vel
                bgXmountain -= 2
                for d in candles:
                    d.x -= man.vel
                for a in bg1platforms:
                    a.x -= man.vel
                for e in Dhurons:
                    e.x -= man.vel
                for a in allHearts:
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
    if background1B:

        if bg1BY >= -644 and bg1BY <= 0 and man.y >= 384 and man.y <= 386:            
            ScrollingVerticalOn = True
            
        if ScrollingVerticalOn == True:
            plat = False
            man.y = 385
            for a in bg1Bplatforms:
                if neg == -1 and man.hitbox[0] + man.hitbox[2] > a.hitbox[0] and man.hitbox[0] < a.hitbox[0] + a.hitbox[2] and man.hitbox[1] < a.hitbox[1] + a.hitbox[3] and man.hitbox[1] + man.hitbox[3] > a.hitbox[1]:
                    if a.visible:
                        man.y = a.y - 95
                        plat = True
                        man.vel = 0
                        
            if man.bat:
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    bg1BY -= man.vel
                    for a in bg1Bplatforms:
                        a.y -= man.vel
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    bg1BY += man.vel
                    for a in bg1Bplatforms:
                        a.y += man.vel
            else:
                if neg == -1:
                 
                    if plat == False:
                        man.vel = 10
                        bg1BY -= 10
                        for a in bg1Bplatforms:
                            a.y -= 10
                elif neg == 1:
                    plat = False
                    man.vel = 10
                    bg1BY += (man.jumpCount ** 2) * 0.5 * neg
                    for a in bg1Bplatforms:
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
            


        if bg1ground1B.x >= -4499 and bg1ground1B.x <= -1339:
            scrollingOn = True

        if scrollingOn == True:
            man.x = 670
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > man.vel:
                bg1BX += 10
                bg1BXmountain += 2
                for a in bg1Bplatforms:
                    a.x += 10
                #for d in candles:
                #    d.x += man.vel
                #for e in Dhurons:
                #    e.x += man.vel
                #for a in allHearts:
                #    a.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bg1BX -= 10
                bg1BXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                for a in bg1Bplatforms:
                    a.x -= 10
                #for e in Dhurons:
                #    e.x -= man.vel
                #for a in allHearts:
                #    a.x -= man.vel
                    
        if bg1ground1B.x <= -4499 or bg1ground1B.x >= -1339:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX3 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX5 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX6 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX7 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX8 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX13 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX4 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX9 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX10 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX11 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX11 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
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
                #for e in Dhurons:
                #    e.x += man.vel

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < 1340 - man.width - man.vel:
                bgX12 -= man.vel
                #bgXmountain -= 2
                #for d in candles:
                #    d.x -= man.vel
                #for a in bg8platforms:
                #    a.x -= man.vel
                #for e in Dhurons:
                #    e.x -= man.vel

        if bg24ground.x <= -1912 or bg24ground.x >= 0:
            scrollingOn = False
            
        if man.x <= 5 and man.left == True:
            man.vel = 0
        elif man.x >= 1310 and man.right == True:
            man.vel = 0
        else:
            man.vel = 10

#-------------------------------------------------------------
#==========================PRINTING FOR TESTS AREA=====================================
#    print(bg10ground.x)
#    print(man.y)
#    print(man.x)
#    print(Dhuron1.x)
#    print(Dhuron1.left)
#    print(bg1HT3.x)
#    print(fallRight[0])
#
#
#
#======================================================================================
pygame.quit()
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================

# Aha! I solved it! All I had to do was go to the Sprite Editor, go to the Slice tab change the Pivot to Center, and the Method to Smart.
# Then alter the height to my liking. Now I gotta rearrange the layers so my character isn't limping.
