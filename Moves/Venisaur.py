from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -100
posy = 200
posx1 = 600
posy1 = 95
frame = 0
Venisaur = []
Venisaur1 = []
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(0,71):
    Venisaur.append(image.load("Pokemon GIFS/Venisaur_gif_backview/%s.gif" % i))
    Venisaur[i-1] = transform.scale(Venisaur[i-1],(500,500))
for i in range(0,71):
    Venisaur1.append(image.load("Pokemon GIFS/Venisaur_gif_frontview/%s.gif" % i))
    Venisaur1[i-1] = transform.scale(Venisaur1[i-1],(300,300))
def VenisaurAction():
    global frame
    screen.blit(Venisaur[frame],(posx,posy))
    screen.blit(Venisaur1[frame],(posx1,posy1))
    frame += 1
    if frame == 70:
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
        VenisaurAction()
    display.flip()
quit()

