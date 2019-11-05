import pygame


class QuadlineGUI:

    def __init__(self):
        pygame.init()
        display = pygame.display.set_mode((600, 400))
        # myfont = pygame.font.SysFont("Arial", 60)
        # label = myfont.render("Quadline", 1, (255, 255, 0))
        # window.blit(label, (100, 100))
        pygame.display.set_caption("QuadlineGUI")

        running = True
        MARGIN_X = 30
        MARGIN_Y = 25
        RADIUS = 20
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            pygame.draw.rect(display, (0, 4, 255), [45, 95, 360, 280])
            # Sets up Quadline grid borders

            for row in range(6):
                for col in range(7):
                    pygame.draw.circle(
                        display, (0, 0, 0),
                        ((MARGIN_X+RADIUS)*col+75, (MARGIN_Y+RADIUS)*row+125),
                        RADIUS)
            # Sets up empty Quadline grid

            pygame.display.update()


if __name__ == '__main__':
    QuadlineGUI()
