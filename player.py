import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()

        # Mostrar sprite del jugador
        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

        # Atributos de movimiento
        self.speed = speed
        self.max_x_constraint = constraint

        # Atributos para disparar y recargar
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

    def get_inputs(self):  # Eventos del jugador
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # movimiento sobre eje x
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            print(self.laser_time)

    def shoot_laser(self):  # disparar laser
        print('!piu piu!')

    def recharge(self):
        if not self.ready:
            curent_time = pygame.time.get_ticks()
            if curent_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.get_inputs()
        self.constraint()
        self.recharge()
