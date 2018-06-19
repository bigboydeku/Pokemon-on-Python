#Pokemon Battle
#Brendyn St.Louis
#Denis Nadarevic

from pygame import* #Loads PyGame Module
from random import* #Loads Random Module
global title
init()
select = ""
screen = display.set_mode((1024,768)) #Sets screen size to 1024,768 pixels

#------------Image/Music Load------------#

intro = image.load("fadein.jpg").convert() #Loads background picture
intro = transform.scale(intro,(1024,768)).convert() #Changes intro1 image to 1024,768 pixels
title = image.load("title.jpg").convert() #Loads title screen
title = transform.scale(title,(1024,768)).convert() #Changes title image to 1024,768 pixels
title_vs = image.load("title - vs.jpg").convert()
title_vs = transform.scale(title_vs,(1024,768))
title_controls = image.load("title - controls.jpg").convert()
title_controls = transform.scale(title_controls,(1024,768))
title_extras = image.load("title - extras.jpg").convert()
title_extras = transform.scale(title_extras,(1024,768))
loading = image.load("loading.jpg").convert()
loading = transform.scale(loading,(1024,768))
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))
pokemon = image.load("poke.jpg").convert()
pokemon = transform.scale(pokemon,(1024,768))
controlScreen = image.load("controlScreen.jpg").convert()
controlScreen = transform.scale(controlScreen,(1024,767))
running = True
clock = time.Clock()
FPS = 30 #Desired framerate in Frames Per Second
playtime = 0.0
Black = (0,0,0)
White = (255,255,255)

#---------------Functions-----------------#

def fadein():
    global select
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

def pikachuAction():
    global frame
    screen.blit(blastoise[frame],(posx,posy))
    frame += 1
    if frame == 111:
        frame = 0
    clock.tick(100)
def Selections():
    myPokemon = ""
    if mb[0] == 1:
        if Rect(54,23,220,184).collidepoint((mx,my)):
            myPokemon = "charizard"
        elif Rect(47,265,245,206).collidepoint((mx,my)):
            myPokemon = "Lugia"
        elif Rect(89,598,175,112).collidepoint((mx,my)):
            myPokemon = "Ho-Oh"
        elif Rect(783,44,173,164).collidepoint((mx,my)):
            myPokemon = "Blastoise"
        elif Rect(769,274,219,191).collidepoint((mx,my)):
            myPokemon = "Venisaur"
        elif Rect(796,558,149,157).collidepoint((mx,my)):
            myPokemon = "Pikachu"
#-----------------------------------------------------------------
    if myPokemon == "charizard":
        screen.blit(loading,(0,0))
    if myPokemon == "Lugia":
        screen.blit(loading,(0,0))
    if myPokemon == "Ho-Oh":
        screen.blit(loading,(0,0))
    if myPokemon == "Blastoise":
        screen.blit(loading,(0,0))
    if myPokemon == "Venisaur":
        screen.blit(loading,(0,0))
    if myPokemon == "Pikachu":
        screen.blit(loading,(0,0))
#-----------Main Running Loop------------#
while running:
    milliseconds = clock.tick(FPS) #Do not go faster than this framerate
    playtime += milliseconds / 1000.0 #Adds seconds to the playtime
    for e in event.get():
        if e.type == QUIT: 
            running = False
        elif e.type == K_ESCAPE: #If "ESCAPE" key is pressed, game exits
            running = False


    mx,my = mouse.get_pos() #Gets x,y position of the mouse
    mb = mouse.get_pressed() #Checks if mouse button is pressed
    display.set_caption('~ Pokemon ~ Frame Rate: %.2f fps, time: %.2f seconds' % (clock.get_fps(), playtime))#Sets window title to this text
#    print(select)
#    print(mx,my)
#-----------Introduction Screen-----------#
    if select == "":
        fadein()
    if select == "title":
        menuscreen()
        if mb[0] == 1:
            if Rect(44,490,236,66).collidepoint((mx,my)):
                select = "controls"
            elif Rect(40,576,163,68).collidepoint((mx,my)):
                select = "Extras"
            elif Rect(48,404,234,55).collidepoint((mx,my)):
                select = "VS"
                
    if select == "VS":
        screen.blit(pokemon,(0,0))
        Selections()
        if Rect(1,670,75,96).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"
        
    if select == "controls":
        screen.blit(controlScreen,(0,0))
        time.wait(100)
        if Rect(1,670,75,96).collidepoint((mx,my)):
            if mb[0] == 1:
                select = "title"
    display.flip()
quit()
    
