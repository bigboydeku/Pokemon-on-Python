from pygame import *
screen = display.set_mode((800,600))
running = True

attack = []
for i in range(0,14):
    attack.append(image.load("%s.gif" % i))

frame = 0
atktype = 0 # for multiple moves.
atk1 = Rect(100,500,50,50)
atk2 = Rect(200,500,50,50)

def attackaction():
    global frame, atktype
    screen.blit(attack[int(frame)], (400,300))
    frame += 0.2
    if frame >= 13:
        frame = 0
        atktype = 0
clock = time.Clock()
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            click = True
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    screen.fill((255,255,255))
    if click and atk1.collidepoint(mx,my):
        atktype = 1
    elif click and atk2.collidepoint(mx,my):
        atktype = 2
    if atktype == 1:
        attackaction()
        clock.tick(60) # 60 = FPS
    draw.rect(screen, (255,0,0), atk1)
    draw.rect(screen, (255,0,0), atk2)
    display.flip()
quit()
