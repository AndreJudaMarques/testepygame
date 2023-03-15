
import pygame #importa codigos do jogo

from pygame.locals import * #importa tudo dess classe

from sys import exit #inclui o x pra fechar a janela

from random import randint #funcao sorteia valores ()

pygame.init() #inicia o jogo


larguraTela = 640
alturaTela = 480

x = larguraTela / 2 - 20 #20 (referencia da largura do objeto)
y = alturaTela / 2

xAzul = randint(40,600) 
yAzul = randint(50, 430)

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('JogoPyTest')

relogio = pygame.time.Clock() #coloca elemento timer no jogo

while True:
    relogio.tick(40) #controla os frames do elemento time
    tela.fill((128, 128, 128))
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

    retVermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40,40))
    retAzul = pygame.draw.rect(tela, (0, 0, 255), (xAzul, yAzul, 40,40))

    if retVermelho.colliderect(retAzul):
        xAzul = randint(40,600)
        yAzul = randint(50, 430)

    pygame.display.update()
