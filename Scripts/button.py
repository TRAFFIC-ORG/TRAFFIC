import pygame

# constants
# ---------
WIDTH = 1000
HEIGHT = 700
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Button:
    def __init__(self, position, size, color, text):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)
        self.text = text

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)
