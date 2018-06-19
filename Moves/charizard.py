from pygame import *
screen = display.set_mode((1024,768))
running = True
clock = time.Clock()
posx = -100
posy = 200
posx1 = 600
posy1 = 95
frame = 0
click = False
attack_valid = True
charizard = []
attack = []
charizard1 = []
frame1 = 0
battle = image.load("battle.png").convert()
battle = transform.scale(battle,(1024,768))

select = ""
for i in range(1,143):
    charizard.append(image.load("Pokemon GIFS/Charizard_gif_backview/%s.gif" % i))
    charizard[i-1] = transform.scale(charizard[i-1],(500,500))
for i in range(1,143):
    charizard1.append(image.load("Pokemon GIFS/Charizard_gif_frontview/%s.gif" % i))
    charizard1[i-1] = transform.scale(charizard1[i-1],(300,300))
def CharizardAction():
    global frame
    screen.blit(charizard[frame],(posx,posy))
    screen.blit(charizard1[frame],(posx1,posy1))
    frame += 1
    if frame == 142:
        frame = 0
    clock.tick(20)
for i in range(0,14):
    attack.append(image.load("Other/Battles/%s.gif" % i))
    attack[i] = transform.scale(attack[i],(310,310))
    attack[i] = transform.flip(attack[i],1,0)
    attack[i] = transform.rotate(attack[i],80)
def attackaction():
    global frame1,attack_valid
    click = True
    if attack_valid == True:
        screen.blit(attack[frame1],(posx1,posy1))
        frame1 +=1
        for i in range(0,14):
            attack.append(image.load("Other/Battles/%s.gif" % i))
            attack[i] = transform.scale(attack[i],(310,310))
            attack[i] = transform.flip(attack[i],1,0)
            attack[i] = transform.rotate(attack[i],80)
            if frame1 == 13:
                attack_valid = False
                frame = 0
                break
            else:
                break
while running:
    for i in event.get():
        if i.type == QUIT:
            running = False
        if i.type == MOUSEBUTTONDOWN:
            click = True
    mx,my = mouse.get_pos()
    print (mx,my)
    if select == "":
        screen.blit(battle,(0,0))
        CharizardAction()
        if click:
            attackaction()
    display.flip()
quit()
