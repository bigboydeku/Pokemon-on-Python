#Pokemon Battle
#Brendyn St.Louis
#Denis Nadarevic

from pygame import* #Loads PyGame Module
from random import* #Loads Random Module
from time import sleep
global title, player1Health, player2Health
font.init()
init()
select = ""
select2 = ""
choose = False
screen = display.set_mode((1024,768)) #Sets screen size to 1024,768 pixels
turn = 'player 1'
music = True
font = font.SysFont("Showcard Gothic", 40)
P1Text = font.render("GO! PLAYER 1!", 1, (255,0,0))
P2Text = font.render("GO! PLAYER 2!", 1, (255,0,0))

#------------Image/Music Load------------#

intro = image.load("images/fadein.jpg").convert() #Loads background picture
intro = transform.scale(intro,(1024,768)).convert() #Changes intro1 image to 1024,768 pixels
title = image.load("images/title.jpg").convert() #Loads title screen
title = transform.scale(title,(1024,768)).convert() #Changes title image to 1024,768 pixels
title_vs = image.load("images/title - vs.jpg").convert()
title_vs = transform.scale(title_vs,(1024,768))
title_controls = image.load("images/title - controls.jpg").convert()
title_controls = transform.scale(title_controls,(1024,768))
title_extras = image.load("images/title - extras.jpg").convert()
title_extras = transform.scale(title_extras,(1024,768))
battle = image.load("images/battle.png").convert()
battle = transform.scale(battle,(1024,768))
pokeP1= image.load("images/pokeP1.jpg").convert()
pokeP1 = transform.scale(pokeP1,(1024,768))
pokeP2 = image.load("images/pokeP2.jpg").convert()
pokeP2 = transform.scale(pokeP2,(1024,768))
controlScreen = image.load("images/controlScreen.jpg").convert()
controlScreen = transform.scale(controlScreen,(1024,768))
extras = image.load("images/extras.jpg").convert()
extras = transform.scale(extras,(1024,768))
Stats1 = image.load("images/Stats1.jpg").convert()
Stats2 = image.load("images/Stats2.jpg").convert()
typechart = image.load("images/typechart.jpg").convert()
areyousure = image.load("images/areyousure.jpg").convert()
intro_song = mixer.music.load("music/intro_song.mp3")
bonus = image.load("images/photo.jpg").convert()
bonus = transform.scale(bonus,(100,100))

#----------Other variables------#

move = False
running = True
clock = time.Clock()
FPS = 30 #Desired framerate in Frames Per Second
playtime = 0.0
Black = (0,0,0)
White = (255,255,255)
green = (0,255,0)
frame = 0
frame1 = 0
frame2 = 0
frame3 = 0
frame4 = 0
frame5 = 0
frame6 = 0
posx = 410
posy = 450
posxa = -100
posya = 200
posxb = 600
posyb = 95
player_1 = ""
player_2 = ""
areyousure2 = False
atktype = 0
atktypeback = 0
atktypefront = 0
player1Health = ()
#----player 1
charizard_dmg = 1
charizard_dmg1 = 0
venusaur_dmg = 1
venusaur_dmg1 = 0
blastoise_dmg = 1
blastoise_dmg1 = 0
pikachu_dmg = 1
pikachu_dmg1 = 0
hooh_dmg = 1
hooh_dmg1 = 0
lugia_dmg = 1
lugia_dmg1 = 0
#----player 2
charizard_dmgfront = 1
charizard_dmgfront1 = 0
venusaur_dmgfront = 1
venusaur_dmgfront1 = 0
blastoise_dmgfront = 1
blastoise_dmgfront1 = 0
pikachu_dmgfront = 1
pikachu_dmgfront1 = 0
hooh_dmgfront = 1
hooh_dmgfront1 = 0
lugia_dmgfront = 1
lugia_dmgfront1 = 0
x = 0
y = 0
player2Health = (100,300,x,y)
health = 0
healthfront = 0
dmg = False
dmg2 = False
#---------------Empty Lists---------------#
#front
pikachu = []
charizard = []
blastoise = []
lugia = []
hooh = []
venusaur = []
pikachu1 = []
#back
charizard1 = []
blastoise1 = []
lugia1 = []
hooh1 = []
venusaur1 = []
#moves
Ancient_Power = []
Blast_Burn = []
Crunch = []
Fly = []
Frenzy = []
Hydro_Pump = []
Light_Blast = []
Mean_Look = []
Mud = []
Mud_Shot = []
Needle_Arm = []
Rock_Smash = []
Scary_Face = []
Seed_Flare = []
Shadow_Ball = []
Surf = []
Swift = []
Wood_Hammer = []
#-----
Ancient_Power1 = []
Blast_Burn1 = []
Crunch1 = []
Fly1 = []
Frenzy1 = []
Hydro_Pump1 = []
Light_Blast1 = []
Mean_Look1 = []
Mud1 = []
Mud_Shot1 = []
Needle_Arm1 = []
Rock_Smash1 = []
Scary_Face1 = []
Seed_Flare1 = []
Shadow_Ball1 = []
Surf1 = []
Swift1 = []
Wood_Hammer1 = []
atk1 = Rect(452,666,572,51)
atk2 = Rect(452,715,267,51)
atk3 = Rect(282,715,742,51)
atkA = Rect(2,45,578,48)
atkB = Rect(3,93,287,46)
atkC = Rect(291,94,551,44)
#---------------Functions-----------------#
def fadein():
    global select
    #intro_song = mixer.music.play(-1)
    for i in range(0,255,5):
        screen.fill((White))
        intro.set_alpha(i)
        screen.blit(intro,(0,0))
        clock.tick(20)#modify the ticks to indicate how fast u want the fade
        display.flip()
    time.delay(2000) #delays this sequence
    for i in range(255,-5,-5):
        screen.fill((White))
        intro.set_alpha(i)
        screen.blit(intro,(0,0))
        clock.tick(20)
        display.flip()
    select = "title"

def menuscreen():
    screen.blit(title,(0,0))
    if Rect(48,404,228,62).collidepoint((mx,my)):
        screen.blit(title_vs,(0,0))
    elif Rect(44,490,236,66).collidepoint((mx,my)):
        screen.blit(title_controls,(0,0))
    elif Rect(40,576,163,68).collidepoint((mx,my)):
        screen.blit(title_extras,(0,0))
#   
for i in range(0,112):
    pikachu.append(image.load("Pokemon GIFS/Pikachu_gif_frontview/%s.gif" % i))
    pikachu[i] = transform.scale(pikachu[i],(200,200))
for i in range(1,143):
    charizard.append(image.load("Pokemon GIFS/Charizard_gif_frontview/%s.gif" % i))
    charizard[i-1] = transform.scale(charizard[i-1],(300,300))
for i in range(0,64):
    blastoise.append(image.load("Pokemon GIFS/Blastoise_gif_frontview/%s.gif" % i))
    blastoise[i] = transform.scale(blastoise[i],(300,300))
for i in range(0,19):
    lugia.append(image.load("Pokemon GIFS/Lugia_gif_frontview/%s.gif" % i))
    lugia[i] = transform.scale(lugia[i],(300,300))
for i in range(0,83):
    hooh.append(image.load("Pokemon GIFS/Ho-oh_gif_frontview/%s.gif" % i))
    hooh[i] = transform.scale(hooh[i],(300,300))
for i in range(0,75):
    venusaur.append(image.load("Pokemon GIFS/Venisaur_gif_frontview/%s.gif" % i))
    venusaur[i] = transform.scale(venusaur[i],(300,300))
#--------backview--------------------------------
for i in range(1,143):
    charizard1.append(image.load("Pokemon GIFS/Charizard_gif_backview/%s.gif" % i))
    charizard1[i-1] = transform.scale(charizard1[i-1],(500,500))
for i in range(0,97):
    blastoise1.append(image.load("Pokemon GIFS/Blastoise_gif_backview/%s.gif" % i))
    blastoise1[i-1] = transform.scale(blastoise1[i-1],(500,500))
for i in range(0,83):
    hooh1.append(image.load("Pokemon GIFS/Ho-oh_gif_backview/%s.gif" % i))
    hooh1[i-1] = transform.scale(hooh1[i-1],(500,500))
for i in range(0,19):
    lugia1.append(image.load("Pokemon GIFS/Lugia_gif_backview/%s.gif" % i))
    lugia1[i-1] = transform.scale(lugia1[i-1],(600,600))
for i in range(0,112):
    pikachu1.append(image.load("Pokemon GIFS/Pikachu_gif_backview/%s.gif" % i))
    pikachu1[i-1] = transform.scale(pikachu1[i-1],(300,300))
for i in range(0,167):
    venusaur1.append(image.load("Pokemon GIFS/Venisaur_gif_backview/%s.gif" % i))
    venusaur1[i-1] = transform.scale(venusaur1[i-1],(500,500))
#-------------MOVES FOR PLAYER 1----------------------#
#Charizard-----------
for i in range(0,14):
    Light_Blast.append(image.load("Assigned Moves/Light Blast/%s.gif" % i))
    Light_Blast[i] = transform.scale(Light_Blast[i],(480,400))
for i in range(0,9):
    Blast_Burn.append(image.load("Assigned Moves/Blast Burn/%s.gif" % i))
    Blast_Burn[i] = transform.scale(Blast_Burn[i],(480,400))
for i in range(1,6):
    Mean_Look.append(image.load("Assigned Moves/Mean Look/%s.png" % i))
    Mean_Look[i-1] = transform.scale(Mean_Look[i-1],(100,100))
#Blastoise-----------
for i in range(1,18):
    Hydro_Pump.append(image.load("Assigned Moves/HydroPump/%s.gif" % i))
    Hydro_Pump[i-1] = transform.scale(Hydro_Pump[i-1],(550,500))
    Hydro_Pump[i-1] = transform.rotate(Hydro_Pump[i-1],(350))
for i in range(0,5):
    Surf.append(image.load("Assigned Moves/Surf/%s.png" % i))
    Surf[i] = transform.scale(Surf[i],(300,300))
for i in range(0,12):
    Frenzy.append(image.load("Assigned Moves/Frenzy/tmp-%s.gif" % i))
    Frenzy[i] = transform.scale(Frenzy[i],(600,600))
#Ho-Oh---------------
for i in range(0,11):
    Swift.append(image.load("Assigned Moves/Swift/%s.gif" % i))
    Swift[i] = transform.scale(Swift[i],(600,600))
    Swift[i] = transform.rotate(Swift[i],(150))
for i in range(1,7):
    Fly.append(image.load("Assigned Moves/Fly/%s.png" % i))
    Fly[i-1] = transform.scale(Fly[i-1],(150,150))
    Fly[i-1] = transform.rotate(Fly[i-1],(180))
for i in range(0,6):
    Mud.append(image.load("Assigned Moves/Mud/%s.png" % i))
    Mud[i] = transform.scale(Mud[i],(200,200))
#Lugia---------------
for i in range(0,7):
    Scary_Face.append(image.load("Assigned Moves/ScaryFace/%s.png" % i))
    Scary_Face[i] = transform.scale(Scary_Face[i],(300,300))
for i in range(0,23):
    Shadow_Ball.append(image.load("Assigned Moves/Shadowball/%s.gif" % i))
    Shadow_Ball[i] = transform.scale(Shadow_Ball[i],(400,400))
for i in range(0,5):
    Wood_Hammer.append(image.load("Assigned Moves/Wood Hammer/tmp-%s.gif" % i))
    Wood_Hammer[i] = transform.scale(Wood_Hammer[i],(400,400))
#Pikachu-------------
for i in range(0,3):
    Needle_Arm.append(image.load("Assigned Moves/Needle Arm/%s.png" % i))
    Needle_Arm[i] = transform.scale(Needle_Arm[i],(200,200))
for i in range(0,10):
    Ancient_Power.append(image.load("Assigned Moves/Ancient Power/%s.png" % i))
    Ancient_Power[i] = transform.scale(Ancient_Power[i],(200,200))
for i in range(0,18):
    Mud_Shot.append(image.load("Assigned Moves/MudShot/tmp-%s.gif" % i))
    Mud_Shot[i] = transform.scale(Mud_Shot[i],(600,400))
#Venusaur------------
for i in range(0,9):
    Seed_Flare.append(image.load("Assigned Moves/Seed Flare/%s.gif" % i))
    Seed_Flare[i] = transform.scale(Seed_Flare[i],(300,300))
for i in range(0,13):
    Crunch.append(image.load("Assigned Moves/Crunch/%s.png" % i))
    Crunch[i] = transform.scale(Crunch[i],(300,300))
for i in range(0,5):
    Rock_Smash.append(image.load("Assigned Moves/Rock Smash/tmp-%s.gif" % i))
    Rock_Smash[i] = transform.scale(Rock_Smash[i],(300,300))
    
#-----------------Player 2 Moves------------------
    
for i in range(0,14):
    Light_Blast1.append(image.load("Assigned Moves/Light Blast/%s.gif" % i))
    Light_Blast1[i] = transform.scale(Light_Blast1[i],(480,400))
    Light_Blast1[i] = transform.rotate(Light_Blast1[i],(180))
for i in range(0,9):
    Blast_Burn1.append(image.load("Assigned Moves/Blast Burn/%s.gif" % i))
    Blast_Burn1[i] = transform.scale(Blast_Burn1[i],(480,400))
for i in range(1,6):
    Mean_Look1.append(image.load("Assigned Moves/Mean Look/%s.png" % i))
    Mean_Look1[i-1] = transform.scale(Mean_Look1[i-1],(100,100))
#Blastoise-----------
for i in range(1,18):
    Hydro_Pump1.append(image.load("Assigned Moves/HydroPump/%s.gif" % i))
    Hydro_Pump1[i-1] = transform.rotate(Hydro_Pump1[i-1],(180))
    Hydro_Pump1[i-1] = transform.scale(Hydro_Pump1[i-1],(600,500))
for i in range(0,5):
    Surf1.append(image.load("Assigned Moves/Surf/%s.png" % i))
    Surf1[i] = transform.scale(Surf[i],(300,300))
for i in range(0,12):
    Frenzy1.append(image.load("Assigned Moves/Frenzy/tmp-%s.gif" % i))
    Frenzy1[i] = transform.rotate(Frenzy1[i],(360))
    Frenzy1[i] = transform.scale(Frenzy1[i],(600,600))
#Ho-Oh---------------
for i in range(0,11):
    Swift1.append(image.load("Assigned Moves/Swift/%s.gif" % i))
    Swift1[i] = transform.scale(Swift1[i],(600,600))
for i in range(1,7):
    Fly1.append(image.load("Assigned Moves/Fly/%s.png" % i))
    Fly1[i-1] = transform.scale(Fly1[i-1],(150,150))
for i in range(0,6):
    Mud1.append(image.load("Assigned Moves/Mud/%s.png" % i))
    Mud1[i] = transform.scale(Mud1[i],(200,200))
#Lugia---------------
for i in range(0,7):
    Scary_Face1.append(image.load("Assigned Moves/ScaryFace/%s.png" % i))
    Scary_Face1[i] = transform.scale(Scary_Face1[i],(300,300))
for i in range(0,23):
    Shadow_Ball1.append(image.load("Assigned Moves/Shadowball/%s.gif" % i))
    Shadow_Ball1[i] = transform.scale(Shadow_Ball1[i],(300,300))
    Shadow_Ball1[i] = transform.rotate(Shadow_Ball[i],(180))
for i in range(0,5):
    Wood_Hammer1.append(image.load("Assigned Moves/Wood Hammer/tmp-%s.gif" % i))
    Wood_Hammer1[i] = transform.scale(Wood_Hammer1[i],(400,400))
#Pikachu-------------
for i in range(0,3):
    Needle_Arm1.append(image.load("Assigned Moves/Needle Arm/%s.png" % i))
    Needle_Arm1[i] = transform.scale(Needle_Arm1[i],(200,200))
for i in range(0,10):
    Ancient_Power1.append(image.load("Assigned Moves/Ancient Power/%s.png" % i))
    Ancient_Power1[i] = transform.scale(Ancient_Power1[i],(200,200))
for i in range(0,18):
    Mud_Shot1.append(image.load("Assigned Moves/MudShot/tmp-%s.gif" % i))
    Mud_Shot1[i] = transform.scale(Mud_Shot1[i],(600,400))
    Mud_Shot1[i] = transform.rotate(Mud_Shot[i],(180))
#Venusaur------------
for i in range(0,9):
    Seed_Flare1.append(image.load("Assigned Moves/Seed Flare/%s.gif" % i))
    Seed_Flare1[i] = transform.scale(Seed_Flare1[i],(300,300))
for i in range(0,13):
    Crunch1.append(image.load("Assigned Moves/Crunch/%s.png" % i))
    Crunch1[i] = transform.scale(Crunch1[i],(300,300))
for i in range(0,5):
    Rock_Smash1.append(image.load("Assigned Moves/Rock Smash/tmp-%s.gif" % i))
    Rock_Smash1[i] = transform.scale(Rock_Smash1[i],(300,300))
#-------------FRONT VIEW DONT YOU DARE TOUCH BRENDYN'S MOM-------------#
def PikachuActionFront():
    global frame1,posxa,posxb
    screen.blit(pikachu[frame1],(700,190))
    frame1 += 1
    if frame1 == 111:
        frame1 = 0
    clock.tick(100)   
def CharizardActionFront():
    global frame2
    screen.blit(charizard[frame2],(posxb,posyb))
    frame2 += 1
    if frame2 == 142:
        frame2 = 0
    clock.tick(100)
def BlastoiseActionFront():
    global frame3
    screen.blit(blastoise[frame3],(posxb,posyb))
    frame3 += 1
    if frame3 == 63:
        frame3 = 0
    clock.tick(100)
def LugiaActionFront():
    global frame4
    screen.blit(lugia[frame4],(posxb,posyb))
    frame4 += 1
    if frame4 == 18:
        frame4 = 0
    clock.tick(100)
def HoohActionFront():
    global frame5
    screen.blit(hooh[frame5],(posxb,posyb))
    frame5 += 1
    if frame5 == 18:
        frame5 = 0
    clock.tick(100)
def VenusaurActionFront():
    global frame6
    screen.blit(venusaur[frame6],(posxb,posyb))
    frame6 += 1
    if frame6 == 74:
        frame6 = 0
    clock.tick(100)
#-------------BACK VIEW DONT YOU DARE TOUCH BRENDYN'S MOM-------------#
def PikachuActionBack():
    global frame1,posxa,posxb
    screen.blit(pikachu1[frame1],(50,380))
    frame1 += 1
    if frame1 == 111:
        frame1 = 0
    clock.tick(100)
def CharizardActionBack():
    global frame2
    screen.blit(charizard1[frame2],(posxa,posya))
    frame2 += 1
    if frame2 == 142:
        frame2 = 0
    clock.tick(100)
def BlastoiseActionBack():
    global frame3
    screen.blit(blastoise1[frame3],(posxa,posya))
    frame3 += 1
    if frame3 == 96:
        frame3 = 0
    clock.tick(100)
def LugiaActionBack():
    global frame4
    screen.blit(lugia1[frame4],(posxa,105))
    frame4 += 1
    if frame4 == 18:
        frame4 = 0
    clock.tick(100)
def HoohActionBack():
    global frame5
    screen.blit(hooh1[frame5],(posxa,posya))
    frame5 += 1
    if frame5 == 18:
        frame5 = 0
    clock.tick(100)
def VenusaurActionBack():
    global frame6
    screen.blit(venusaur1[frame6],(posxa,posya))
    frame6 += 1
    if frame6 == 74:
        frame6 = 0
    clock.tick(100)
def displayPokemonFront(poke):
    if poke == "lugia":
        LugiaActionFront();
    if poke == "hooh":
        HoohActionFront()
    if poke == "blastoise":
        BlastoiseActionFront()
    if poke == "charizard":
        CharizardActionFront()
    if poke == "pikachu":
        PikachuActionFront()
    if poke == "venusaur":
        VenusaurActionFront()
def displayPokemonBack(poke):
    if poke == "lugia":
        LugiaActionBack();
    if poke == "hooh":
        HoohActionBack()
    if poke == "blastoise":
        BlastoiseActionBack()
    if poke == "charizard":
        CharizardActionBack()
    if poke == "pikachu":
        PikachuActionBack()
    if poke == "venusaur":
        VenusaurActionBack()
#Front moves-------------------------------
def CharizardAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
def BlastoiseAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 11:
        frame = 0
        atktype = 0
def LugiaAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
def VenusaurAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
def PikachuAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
def HoohAttackActionFront():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
#Back moves---------------------------------
def CharizardAttackActionBack():
    global frame, atktype, Light_Blast, Blast_Burn, Mean_Look, atktypeback
    if atktypeback == 1:
        screen.blit(Light_Blast[int(frame)], (220,250))
        frame += 0.5
        if frame == 14:
            frame = 0
            atktypeback = 0
    if atktypeback == 2:
        screen.blit(Blast_Burn[int(frame)], (600,120))
        frame += 0.5
        if frame == 8:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Mean_Look[int(frame)], (670,280))
        frame += 0.5
        if frame == 5:
            frame = 0
            atktypeback = 0
def BlastoiseAttackActionBack():
    global frame, atktype, Hydro_Pump, Surf, Frenzy, atktypeback
    frame += 0.2
    if atktypeback == 1:
        screen.blit(Hydro_Pump[int(frame)], (150,100))
        frame += 0.2
        if frame >= 17:
            frame = 0
            atktypeback = 0        
    if atktypeback == 2:
        screen.blit(Surf[int(frame)], (600,120))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Frenzy[int(frame)], (450,-60))
        frame += 0.1
        if frame >= 11:
            frame = 0
            atktypeback = 0
def LugiaAttackActionBack():
    global frame, atktype, Scary_Face, Shadow_Ball, Wood_Hammer, atktypeback
    frame += 0.2
    if atktypeback == 1:
        screen.blit(Scary_Face[int(frame)], (600,200))
        frame += 0.2
        if frame >= 6:
            frame = 0
            atktypeback = 0        
    if atktypeback == 2:
        screen.blit(Shadow_Ball[int(frame)], (450,200))
        frame += 0.6
        if frame >= 21:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Wood_Hammer[int(frame)], (400,190))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypeback = 0
def VenusaurAttackActionBack():
    global frame, atktype, Seed_Flare, Crunch, Rock_Smash, atktypeback
    frame += 0.2
    if atktypeback == 1:
        screen.blit(Seed_Flare[int(frame)], (650,100))
        frame += 0.2
        if frame >= 8:
            frame = 0
            atktypeback = 0        
    if atktypeback == 2:
        screen.blit(Crunch[int(frame)], (600,200))
        frame += 0.8
        if frame >= 13:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Rock_Smash[int(frame)], (600,200))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypeback = 0
def PikachuAttackActionBack():
    global frame, atktype, Needle_Arm, Ancient_Power, Mud_Shot, atktypeback
    frame += 0.2
    if atktypeback == 1:
        screen.blit(Needle_Arm[int(frame)], (600,200))
        frame += 0.2
        if frame >= 2:
            frame = 0
            atktypeback = 0        
    if atktypeback == 2:
        screen.blit(Ancient_Power[int(frame)], (600,200))
        frame += 0.2
        if frame >= 9:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Mud_Shot[int(frame)], (120,310))
        frame += 0.2
        if frame >= 17:
            frame = 0
            atktypeback = 0
def HoohAttackActionBack():
    global frame, atktype, Swift, Fly, Mud, atktypeback
    frame += 0.2
    if atktypeback == 1:
        screen.blit(Swift[int(frame)], (50,-50))
        frame += 0.2
        if frame >= 11:
            frame = 0
            atktypeback = 0        
    if atktypeback == 2:
        screen.blit(Fly[int(frame)], (650,150))
        frame += 0.2
        if frame >= 6:
            frame = 0
            atktypeback = 0
    if atktypeback == 3:
        screen.blit(Mud[int(frame)], (650,200))
        frame += 0.2
        if frame >= 5:
            frame = 0
            atktypeback = 0
#----------------------------------------------------------------------------Front Moves----------------------------------------------------
def CharizardAttackActionFront():
    global frame, atktype, Light_Blast1,Blast_Burn1,Mean_Look1,atktypefront
    if atktypefront == 1:
        screen.blit(Light_Blast1[int(frame)], (300,170))
        frame += 0.5
        if frame >= 14:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Blast_Burn1[int(frame)], (100,350))
        frame += 0.7
        if frame >= 9:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Mean_Look1[int(frame)], (200,450))
        frame += 0.5
        if frame >= 5:
            frame = 0
            atktypefront = 0
def BlastoiseAttackActionFront():
    global frame, atktype, Hydro_Pump1, Surf1, Frenzy1,atktypefront
    frame += 0.2
    if atktypefront == 1:
        screen.blit(Hydro_Pump1[int(frame)], (300,10))
        frame += 0.2
        if frame >= 17:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Surf1[int(frame)], (100,350))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Frenzy1[int(frame)], (-50,200))
        frame += 0.2
        if frame >= 11:
            frame = 0
            atktypefront = 0
def LugiaAttackActionFront():
    global frame, atktype, Scary_Face1, Shadow_Ball1, Wood_Hammer1,atktypefront
    frame += 0.2
    if atktypefront == 1:
        screen.blit(Scary_Face1[int(frame)], (100,400))
        frame += 0.2
        if frame >= 6:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Shadow_Ball1[int(frame)], (200,400))
        frame += 0.6
        if frame >= 22:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Wood_Hammer1[int(frame)], (-100,450))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypefront = 0
def VenusaurAttackActionFront():
    global frame, atktype, Seed_Flare1, Crunch1, Rock_Smash1,atktypefront
    frame += 0.2
    if atktypefront == 1:
        screen.blit(Seed_Flare1[int(frame)], (100,300))
        frame += 0.2
        if frame >= 8:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Crunch1[int(frame)], (100,350))
        frame += 0.9
        if frame >= 13:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Rock_Smash1[int(frame)], (100,350))
        frame += 0.2
        if frame >= 4:
            frame = 0
            atktypefront = 0
def PikachuAttackActionFront():
    global frame, atktype, Needle_Arm1, Ancient_Power1, Mud_Shot1,atktypefront
    frame += 0.2
    if atktypefront == 1:
        screen.blit(Needle_Arm1[int(frame)], (100,400))
        frame += 0.2
        if frame >= 2:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Ancient_Power1[int(frame)], (100,400))
        frame += 0.2
        if frame >= 9:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Mud_Shot1[int(frame)], (350,150))
        frame += 0.2
        if frame >= 17:
            frame = 0
            atktypefront = 0
def HoohAttackActionFront():
    global frame, atktype, Swift1, Fly1, Mud1,atktypefront
    frame += 0.2
    if atktypefront == 1:
        screen.blit(Swift1[int(frame)], (300,100))
        frame += 0.2
        if frame >= 11:
            frame = 0
            atktypefront = 0        
    if atktypefront == 2:
        screen.blit(Fly1[int(frame)], (100,400))
        frame += 0.2
        if frame >= 6:
            frame = 0
            atktypefront = 0
    if atktypefront == 3:
        screen.blit(Mud1[int(frame)], (100,400))
        frame += 0.2
        if frame >= 5:
            frame = 0
            atktypefront = 0
#----------------------------------------------------------
def VSPlayer():
    global select,player_2,areyousure2,areyousure
    if areyousure2 != True:
        screen.blit(pokeP2,(0,0))
    if move:
        if select == "VS - Player 2":
            if Rect(796,558,149,157).collidepoint((mx,my)):
                #PikachuAction()
                if mb[0] == 1:
                    player_2 = "pikachu"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(54,23,220,184).collidepoint((mx,my)):
                #CharizardAction()
                if mb[0] == 1:
                    player_2 = "charizard"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(783,44,173,164).collidepoint((mx,my)):
                #BlastoiseAction()
                if mb[0] == 1:
                    player_2 = "blastoise"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(47,265,245,206).collidepoint((mx,my)):
                #LugiaAction()
                if mb[0] == 1:
                    player_2 = "lugia"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(89,598,175,112).collidepoint((mx,my)):
                #HoohAction()
                if mb[0] == 1:
                    player_2 = "hooh"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(769,274,219,191).collidepoint((mx,my)):
                #VenusaurAction()
                if mb[0] == 1:
                    player_2 = "venusaur"
                    screen.blit(areyousure,(0,0))
                    areyousure2 = True
            elif Rect(1,670,75,96).collidepoint((mx,my)):
                if mb[0] == 1:
                    select = "title"
    if keys[K_RETURN] and areyousure2 == True:
        select = "battle"
        areyousure2 = False
#-------------Health---------------------------------------#
def poke_Health_Front():
    global dmg,health,charizard_dmg1,charizard_dmg,lugia_dmg1,lugia_dmg,blastoise_dmg1,blastoise_dmg,venusaur_dmg1,venusaur_dmg,hooh_dmg1,hooh_dmg,pikachu_dmg1,pikachu_dmg,healthfront
    global charizard_dmgfront1,charizard_dmgfront,dmg2
    if player_2 == "charizard":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            charizard_dmgfront1 += 84/6.66666667
        if dmg2 == True:
            healthfront += charizard_dmgfront
            dmg2 = False
        if healthfront == charizard_dmgfront1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            quit()
    if player_2 == "blastoise":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            blastoise_dmg1 += 83/6.66666667
        if dmg2 == True:
            healthfront += blastoise_dmg
            dmg2 = False
        if healthfront >= blastoise_dmg1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            quit()
        time.wait(50)
    if player_2 == "hooh":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            hooh_dmg1 += 130/6.66666667
        if dmg2 == True:
            healthfront += hooh_dmg
            dmg2 = False
        if healthfront >= hooh_dmg1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            quit()
        time.wait(50)
    if player_2 == "lugia":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            lugia_dmg1 += 90/6.66666667
        if dmg2 == True:
            healthfront += lugia_dmg
            dmg2 = False
        if healthfront >= lugia_dmg1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            quit()
        time.wait(50)
    if player_2 == "pikachu":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            pikachu_dmg1 += 55/6.66666667
        if dmg2 == True:
            healthfront += pikachu_dmg
            dmg2 = False
        if healthfront >= pikachu_dmg1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            select = 'title'
        time.wait(50)
    if player_2 == "venusaur":
        if atktypefront == 1 or atktypefront == 2 or atktypefront == 3 and healthfront < 180:
            dmg2 = True
            venusaur_dmg1 += 82/6.66666667
        if dmg2 == True:
            healthfront += venusaur_dmg
            dmg2 = False
        if healthfront >= venusaur_dmg1:
            dmg2 = False
        if healthfront > 180:
            healthfront = 180
            select = 'title'
        time.wait(50)
def poke_health():
    global dmg,health,charizard_dmg1,charizard_dmg,lugia_dmg1,lugia_dmg,blastoise_dmg1,blastoise_dmg,venusaur_dmg1,venusaur_dmg,hooh_dmg1,hooh_dmg,pikachu_dmg1,pikachu_dmg,healthfront
    global charizard_dmgfront1,charizard_dmgfront,dmg2,select
    if player_1 == "charizard":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            charizard_dmg1 += 84/6.66666667
        if dmg == True:
            health += charizard_dmg
            dmg = False
        if health == charizard_dmg1:
            dmg = False
            print ("lel")
        if health == 180:
            select2 = 'title'
    if player_1 == "blastoise":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            blastoise_dmg1 += 83/6.66666667
        if dmg == True:
            health += blastoise_dmg
            dmg = False
        if health >= blastoise_dmg1:
            dmg = False
            print ("lel")
        if health == 180:
            select2 = 'title'
        time.wait(50)
    if player_1 == "hooh":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            hooh_dmg1 += 130/6.66666667
        if dmg == True:
            health += hooh_dmg
            dmg = False
        if health >= hooh_dmg1:
            dmg = False
            print ("lel")
        if health == 180:
            select2 = 'title'
        time.wait(50)
    if player_1 == "lugia":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            lugia_dmg1 += 90/6.66666667
        if dmg == True:
            health += lugia_dmg
            dmg = False
        if health >= lugia_dmg1:
            dmg = False
            print ("lel-----------------------------------")
        if health == 180:
            select2 = 'title'
        time.wait(50)
    if player_1 == "pikachu":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            pikachu_dmg1 += 55/6.66666667
        if dmg == True:
            health += pikachu_dmg
            dmg = False
        if health >= pikachu_dmg1:
            dmg = False
            print ("lel-----------------------------------")
        if health == 180:
            select2 = 'title'
        time.wait(50)
    if player_1 == "venusaur":
        if atktypeback == 1 or atktypeback == 2 or atktypeback == 3 and health < 180:
            dmg = True
            venusaur_dmg1 += 82/6.66666667
        if dmg == True:
            health += venusaur_dmg
            dmg = False
        if health >= venusaur_dmg1:
            dmg = False
            print ("lel")
        if health == 180:
            select2 = 'title'
        time.wait(50)
    print(select)
#-----------Main Running Loop------------#

while running:
    click = False
    milliseconds = clock.tick(FPS) #Do not go faster than this framerate
    playtime += milliseconds / 1000.0 #Adds seconds to the playtime
    for e in event.get():
        if e.type == QUIT: 
            running = False
        elif e.type == K_ESCAPE: #If "ESCAPE" key is pressed, game exits
            running = False
        elif e.type == MOUSEBUTTONDOWN:
            move = True
            if e.button == 1:
                click = True
        elif e.type == MOUSEBUTTONUP:
            move = False
    keys = key.get_pressed()
    mx,my = mouse.get_pos() #Gets x,y position of the mouse
    mb = mouse.get_pressed() #Checks if mouse button is pressed
    display.set_caption('~ Pokemon ~ Frame Rate: %.2f fps, time: %.2f seconds' % (clock.get_fps(), playtime))#Sets window title to this text
    print(mx,my)
    
    
#-----------Introduction Screen-----------#

    if select == "" and select2 == "":
        fadein()
    if select == "title" or select2 == "title":
        menuscreen()
        if Rect(44,490,236,66).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "controls"
        elif Rect(40,576,163,68).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "Extras"
        elif Rect(48,404,234,55).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "VS - Player 1"
                #print(select)
                choose = False
    if move:
        if select == "VS - Player 1":
            screen.blit(pokeP1,(0,0))
            if Rect(796,558,149,157).collidepoint((mx,my)):
                #PikachuActionFront()
                if mb[0] == 1:
                    player_1 = "pikachu"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(54,23,220,184).collidepoint((mx,my)):
                #CharizardActionFront()
                if mb[0] == 1:
                    player_1 = "charizard"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(783,44,173,164).collidepoint((mx,my)):
                #BlastoiseActionFront()
                if mb[0] == 1:
                    player_1 = "blastoise"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(47,265,245,206).collidepoint((mx,my)):
                #LugiaActionFront()
                if mb[0] == 1:
                    player_1 = "lugia"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(89,598,175,112).collidepoint((mx,my)):
                #HoohActionFront()
                if mb[0] == 1:
                    player_1 = "hooh"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(769,274,219,191).collidepoint((mx,my)):
                #VenusaurActionFront()
                if mb[0] == 1:
                    player_1 = "venusaur"
                    screen.blit(areyousure,(0,0))
                    areyousure1 = True
            elif Rect(1,670,75,96).collidepoint((mx,my)):
                if mb[0] == 1:
                    select = "title"
    if keys[K_RETURN] and areyousure1 == True:
        select = "VS - Player 2"
        areyousure1 = False
        
    if select == "VS - Player 2":
        VSPlayer()

    if select == "battle":
        screen.blit(battle,(0,0))
        displayPokemonFront(player_2)
        displayPokemonBack(player_1)
        draw.rect(screen, green, (680,631,180,10))
        draw.rect(screen,(255,0,0),(860-healthfront,631,healthfront,10))
        draw.rect(screen, green, (47,162,178,10))
        draw.rect(screen,(255,0,0),(227-health,162,health,10))
#--------------------------------------------------------Charizard------------------------------------------    
        if turn == 'player 1':
            screen.blit(P1Text, (675,50))
        if turn == 'player 2':
            screen.blit(P2Text, (675,50))
        if player_1 == "charizard":
            charizardP1 = image.load("images/Charizard_Moves.jpg").convert()
            screen.blit(charizardP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                CharizardAttackActionBack()
                print("test")
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                CharizardAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                CharizardAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------Blastoise------------------------------------------
        if player_1 == "blastoise":
            blastoiseP1 = image.load("images/Blastoise_Moves.jpg").convert()
            screen.blit(blastoiseP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                BlastoiseAttackActionBack()
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                BlastoiseAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                BlastoiseAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------Ho-Oh------------------------------------------
        if player_1 == "hooh":
            hoohP1 = image.load("images/Ho-oh_Moves.jpg").convert()
            screen.blit(hoohP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                HoohAttackActionBack()
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                HoohAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                HoohAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------Lugia------------------------------------------
        if player_1 == "lugia":
            lugiaP1 = image.load("images/Lugia_Moves.jpg").convert()
            screen.blit(lugiaP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                LugiaAttackActionBack()
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                LugiaAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                LugiaAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------Pikachu------------------------------------------
        if player_1 == "pikachu":
            pikachuP1 = image.load("images/Pikachu_Moves.jpg").convert()
            screen.blit(pikachuP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                PikachuAttackActionBack()
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                PikachuAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                PikachuAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------Venusaur------------------------------------------
        if player_1 == "venusaur":
            venusaurP1 = image.load("images/Venusaur_Moves.jpg").convert()
            screen.blit(venusaurP1,(452,666))
            if click and atk1.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 1
            elif click and atk2.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 2
            elif click and atk3.collidepoint(mx,my) and turn == 'player 1':
                turn = 'player 2'
                atktypeback = 3
            if atktypeback == 1:
                VenusaurAttackActionBack()
                clock.tick(600)
                poke_health()
            if atktypeback == 2:
                VenusaurAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
            if atktypeback == 3:
                VenusaurAttackActionBack()
                clock.tick(600)# 60 = FPS
                poke_health()
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Front Images------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Charizard------------------------------------------    
        if player_2 == "charizard":
            charizardP2 = image.load("images/Charizard_Moves.jpg").convert()
            screen.blit(charizardP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            elif click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            elif click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                CharizardAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                CharizardAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                CharizardAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
#--------------------------------------------------------Blastoise------------------------------------------
        if player_2 == "blastoise":
            blastoiseP2 = image.load("images/Blastoise_Moves.jpg").convert()
            screen.blit(blastoiseP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            elif click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            elif click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                BlastoiseAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                BlastoiseAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                BlastoiseAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
#--------------------------------------------------------Ho-Oh------------------------------------------
        if player_2 == "hooh":
            hoohP2 = image.load("images/Ho-oh_Moves.jpg").convert()
            screen.blit(hoohP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            elif click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            elif click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                HoohAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                HoohAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                HoohAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
#--------------------------------------------------------Lugia------------------------------------------
        if player_2 == "lugia":
            lugiaP2 = image.load("images/Lugia_Moves.jpg").convert()
            screen.blit(lugiaP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            if click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            if click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                LugiaAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                LugiaAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                LugiaAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
#--------------------------------------------------------Pikachu------------------------------------------
        if player_2 == "pikachu":
            pikachuP2 = image.load("images/Pikachu_Moves.jpg").convert()
            screen.blit(pikachuP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            elif click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            elif click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                PikachuAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                PikachuAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                PikachuAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
#--------------------------------------------------------Venusaur------------------------------------------
        if player_2 == "venusaur":
            venusaurP2 = image.load("images/Venusaur_Moves.jpg").convert()
            screen.blit(venusaurP2,(3,45))
            if click and atkA.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 1
            elif click and atkB.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 2
            elif click and atkC.collidepoint(mx,my) and turn == 'player 2':
                turn = 'player 1'
                atktypefront = 3
            if atktypefront == 1:
                VenusaurAttackActionFront()
                clock.tick(600)
                poke_Health_Front()
            if atktypefront == 2:
                VenusaurAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
            if atktypefront == 3:
                VenusaurAttackActionFront()
                clock.tick(600)# 60 = FPS
                poke_Health_Front()
                
    if select == "controls":
        if mb[0] == 1:
            screen.blit(controlScreen,(0,0))
            if Rect(114,114,116,25).collidepoint((mx,my)):
                if mb[0] == 1:
                    intro_song = mixer.music.set_volume(0.2)
            if Rect(806,72,118,115).collidepoint((mx,my)):
                if mb[0] == 1:
                    intro_song = mixer.music.set_volume(0.7)
            if Rect(426,13,172,45).collidepoint((mx,my)):
                if mb[0] == 1:
                    intro_song = mixer.music.set_volume(0.5)
            if Rect(974,718,50,50).collidepoint((mx,my)):
                for i in range(15):
                    screen.blit(bonus,(randint(0,1024),(randint(0,768))))
            if Rect(1,670,75,96).collidepoint((mx,my)):
                if mb[0] == 1:
                    select = "title"
                
    if select == "Extras":
        screen.blit(extras,(0,0))
        if Rect(938,693,72,69).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"
        elif Rect(156,132,731,177).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "typechart"
        elif Rect(153,354,733,178).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "Stats1"
    
    if select == "typechart":
        screen.blit(typechart,(0,0))
        if Rect(47,37,101,79).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"

    if select == "Stats1":
        screen.blit(Stats1,(0,0))
        if Rect(813,656,73,84).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"
        elif Rect(936,646,76,96).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "Stats2"

    if select == "Stats2":
        screen.blit(Stats2,(0,0))
        if Rect(804,636,85,96).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"

    if select == "bonus":
        screen.blit(bonus,(0,0))
        select = 'title'
    display.flip()
quit()
