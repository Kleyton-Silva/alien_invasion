import pygame


class Ship():

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('src/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (90, 115))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
