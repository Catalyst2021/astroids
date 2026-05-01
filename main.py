import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True: 
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
        
        #Make screen black
        screen.fill("black")

        updatable.update(dt) 
        for draws in drawable: 
            draws.draw(screen)
            
        #Draw player 
        #player.update(dt)
        #player.draw(screen) 
        
        
           

    
        #Refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock .tick(60) / 1000

            
if __name__ == "__main__":
    main()
