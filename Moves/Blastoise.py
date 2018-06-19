from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -100
posy = 200
posx1 = 600
posy1 = 95
frame = 0
Blastoise = []
Blastoise1 = []
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(1,64):
    Blastoise.append(image.load("Pokemon GIFS/Blastoise_gif_backview/%s.gif" % i))
    Blastoise[i-1] = transform.scale(Blastoise[i-1],(500,500))
for i in range(1,64):
    Blastoise1.append(image.load("Pokemon GIFS/Blastoise_gif_frontview/%s.gif" % i))
    Blastoise1[i-1] = transform.scale(Blastoise1[i-1],(300,300))
def CharizardActionFront():
    global frame
    screen.blit(Blastoise[frame],(posx,posy))
    screen.blit(Blastoise1[frame],(posx1,posy1))
    frame += 1
    if frame == 63:
        frame = 0
    clock.tick(20)
def CharizardActionBack():
    screen.blit(Blastoise1[frame],(posx1,posy1))
    frame += 1
    if frame == 63:
        frame = 0
    global frame
    screen.blit(Blastoise[frame],(posx,posy))
    screen.blit(Blastoise1[frame],(posx1,posy1))
    frame += 1
    if frame == 63:
        frame = 0
    clock.tick(20)
while running:
    for i in event.get():
        if i.type == QUIT:
            running = False
    mx,my = mouse.get_pos()
    print (mx,my)
    if select == "":
        screen.blit(battle,(0,0))
        CharizardActionFront()
    display.flip()
quit()

