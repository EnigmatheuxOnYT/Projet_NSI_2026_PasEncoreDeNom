import pygame

def startGame():
    go_to=menu
    while go_to!=None:
        go_to=go_to()

def menu():
    running=True
    new_go_to=menu
    #print("in menu")
    while running:
        dt = pygame.time.Clock().tick(60)/1000
        screen.fill((155,200,175))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_go_to=None
                running=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                new_go_to=test
                running=False

        pygame.display.update()

    return new_go_to

def test():
    print('test')
    return None

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Pas de Nom")
    screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    startGame()
    pygame.quit()