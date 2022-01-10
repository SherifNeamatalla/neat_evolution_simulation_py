import pygame


class PyGameWindow:
    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.game_over = False
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((170, 238, 187))
        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
            background.blit(text, textpos)

        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def tick(self):
        self.clock.tick(60)
        pygame.display.flip()
