import pygame
import sys
from player import Player


class Game:
    def __init__(self):

        # Jugador
        player_sprite = Player((screen_w / 2, screen_h),
                               screen_w, 5)  # posicion inicial
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        # Actualizar todos los grupos de sprites
        # Dibujar todos los grupos de sprites

        # Actualizar y Dibujar Jugador
        self.player.update()
        self.player.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_w = 600
    screen_h = 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    game = Game()  # instancia de la clase

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30))  # relleno fondo
        game.run()

        pygame.display.flip()
        clock.tick(60)
