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


class Accueil:
    def __init__(self,ecran):
        self.ecran = ecran
        self.horloge = pygame.time.Clock()
        self.fps = 60
        self.running = False

    def gerer_entree(self): #Gère les entrées du joueur

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    
    def dessiner_fenetre (self):
        screen.fill((155,200,175))
        pygame.display.flip()
    
    def lancer(self):
        self.running = True

        while self.running:
            self.gerer_entree()
            self.dessiner_fenetre()
            self.horloge.tick(self.fps)
        

    

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Jeu")
    #pygame.display.set_icon("icon.ico")
    screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    #startGame()
    jeu = Accueil(screen)
    jeu.lancer()
    pygame.quit()