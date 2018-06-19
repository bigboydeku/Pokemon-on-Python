#Test Battle
from pygame import*
screen = display.set_mode((800,600))
clock = time.Clock()
select = ""
running = True
frame = 0
frame1 = 0
posx = 450
posx1 = 281
posy = 300
posy1 = 225
click = False

lugia = []
attack = []
for i in range(0,19):
    lugia.append(image.load("gh/%s.gif" % i))
def lugiaaction():
    global frame
    screen.blit(lugia[frame],(posx,posy))
    frame+=1
    if frame == 18:
        frame = 0
for i in range(0,14):
    attack.append(image.load("%s.gif" % i))
    attack[i] = transform.scale(attack[i],(310,310))
    attack[i] = transform.flip(attack[i],1,0)
    attack[i] = transform.rotate(attack[i],80)
def attackaction():
    global frame1
    screen.blit(attack[frame1],(posx1,posy1))
    frame1 +=1
    if frame1 == 13:
        frame1 = 0
##        print (click)
    
while running:
    click = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            click = True
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    

    if select == "":
        screen.fill((255,255,255))
        lugiaaction()
        if click:
            attackaction()
            
    display.flip()
    clock.tick(25)
quit()
