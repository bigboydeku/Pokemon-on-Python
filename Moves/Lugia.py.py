from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -100
posy = 200
posx1 = 600
posy1 = 95
frame = 0
lugia = []
lugia1 = []
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(0,19):
    lugia.append(image.load("Pokemon GIFS/Lugia_gif_backview/%s.gif" % i))
    lugia[i-1] = transform.scale(lugia[i-1],(500,500))
for i in range(0,19):
    lugia1.append(image.load("Pokemon GIFS/Lugia_gif_frontview/%s.gif" % i))
    lugia1[i-1] = transform.scale(lugia1[i-1],(300,300))
def lugiaAction():
    global frame
    screen.blit(lugia[frame],(posx,posy))
    screen.blit(lugia1[frame],(posx1,posy1))
    frame += 1
    if frame == 18:
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
        lugiaAction()
    display.flip()
quit()
