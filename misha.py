import pygame
import os

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((500, 500))

geroy = pygame.Rect(65, 65, 29, 22)

# hero = 1
# vin = 2
# pol = 3
# stone = 4

go_right = False
go_left = False
go_up = False
go_down = False
# textures
dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

stone = pygame.image.load(img_path + "/stone.png")
pol = pygame.image.load(img_path + "/pol.png")
hero = pygame.image.load(img_path + "/hero.png")
vin = pygame.image.load(img_path + "/vin.png")

textures = [
    [4,4,4,4,4,4,4,4,4,4],
    [4,3,3,3,3,3,3,3,3,4],
    [4,3,4,3,4,3,4,3,3,4],
    [4,4,3,3,3,4,3,3,3,4],
    [4,3,3,3,3,3,3,3,3,4],
    [4,3,3,3,3,3,4,4,4,4],
    [4,4,4,4,3,3,4,4,3,4],
    [4,3,3,3,4,3,3,3,3,4],
    [4,2,3,3,3,3,3,3,3,4],
    [4,4,4,4,4,4,4,4,4,4]
]

rects = []
rects_textures = []
good = []
bad = []

x = 0
y = 0

for texture in textures:    # рядки - 10
    for i in texture:       # клітинки - 10
        kvadrat = pygame.Rect(x, y, 50, 50) # - 100
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 4:
            bad.append(kvadrat)
        if i == 2:
            good.append(kvadrat)
        x += 50 
    y += 50   
    x = 0

font = pygame.font.SysFont("Arial Rounded MT Bold", 50)
text = font.render("YOU WIN!", True, (0,255,0))

game = True

while game:
    
    display.fill((0, 200, 100))
    
    for i in range(100):
        if rects_textures[i] == 2:
            display.blit(vin, rects[i])
        if rects_textures[i] == 3:
            display.blit(pol, rects[i])
        if rects_textures[i] == 4:
            display.blit(stone, rects[i])

    display.blit(hero, geroy)

    for ba in bad:
        if geroy.colliderect(ba):
            geroy.x = 65
            geroy.y = 65

    for goo in good:
        if geroy.colliderect(goo):
            display.fill((13, 152, 186))
            display.blit(text, (160,160))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True
            if event.key == pygame.K_s:
                go_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False
    
    if go_right == True:
        geroy.x += 5
    if go_left == True:
        geroy.x -= 5
    if go_up == True:
        geroy.y -= 5
    if go_down == True:
        geroy.y += 5

    pygame.display.flip()
    clock.tick(60)