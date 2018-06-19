from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -75
posy = 400
posx1 = 700
posy1 = 250
frame = 0
Pikachu = []
Pikachu1 = []
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(0,112):
    Pikachu.append(image.load("Pokemon GIFS/Pikachu_gif_backview/%s.gif" % i))
    Pikachu[i-1] = transform.scale(Pikachu[i-1],(300,300))
for i in range(1,112):
    Pikachu1.append(image.load("Pokemon GIFS/Pikachu_gif_frontview/%s.gif" % i))
    Pikachu1[i-1] = transform.scale(Pikachu1[i-1],(150,150))
def PikachuAction():
    global frame
    screen.blit(Pikachu[frame],(posx,posy))
    screen.blit(Pikachu1[frame],(posx1,posy1))
    frame += 1
    if frame == 111:
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
        PikachuAction()
    display.flip()
quit()

