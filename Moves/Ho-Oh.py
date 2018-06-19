from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -100
posy = 200
posx1 = 600
posy1 = 95
frame = 0
HoOh = []
HoOh1 = []
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(0,83):
    HoOh.append(image.load("Pokemon GIFS/Ho-oh_gif_backview/%s.gif" % i))
    HoOh[i-1] = transform.scale(HoOh[i-1],(500,500))
for i in range(0,83):
    HoOh1.append(image.load("Pokemon GIFS/Ho-oh_gif_frontview/%s.gif" % i))
    HoOh1[i-1] = transform.scale(HoOh1[i-1],(300,300))
def HoOhAction():
    global frame
    screen.blit(HoOh[frame],(posx,posy))
    screen.blit(HoOh1[frame],(posx1,posy1))
    frame += 1
    if frame == 82:
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
        HoOhAction()
    display.flip()
quit()
