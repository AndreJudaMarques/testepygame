
import pygame

from pygame.locals import *

from sys import exit

pygame.init()


larguraTela = 640
alturaTela = 480
tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('JogoPyTest')

relogio = pygame.time.Clock()

x = larguraTela / 2 - 20 #20 (referencia da largura do objeto)
y = alturaTela / 2

while True:
    relogio.tick(40)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        ''' #exemplo de controle de teclas, porem a cada clique
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x -= 20
            if event.key == K_RIGHT:
                x += 20
            if event.key == K_UP:
                y -= 20
            if event.key == K_DOWN:
                y += 20
                '''
    #controle de teclas continuo
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 20
    if pygame.key.get_pressed()[K_UP]:
        y -= 20
    if pygame.key.get_pressed()[K_DOWN]:
        y += 20

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40,40))
       
    pygame.display.update()
