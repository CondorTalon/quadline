import pygame


class QuadlineGUI:
    """
    Class QuadlineGUI represents the display window where a game of Quadline will be played. 
    The class contains methods that operate the title screen, game screen, and other tasks such as 
    operating the Quadline game and highlighting moves made by each player

    DOCUMENTATION IS CURRENTLY UNFINISHED (MUHAMMAD) 

    """

    def __init__(self):
        pygame.init()
        display = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("QuadlineGUI")

        running = True

        MARGIN_X = 30
        MARGIN_Y = 25
        RADIUS = 20
        # token and margin size for visuals

        while running:  # Operates the GUI while the window is open
            running_title = True
            while running_title:  # Operates the titlescreen
                title_font = pygame.font.SysFont("Arial", 100)
                title_text = title_font.render("Quadline", True,
                                               (255, 255, 255))
                display.blit(title_text, (100, 50))
                play_button = pygame.draw.rect(display, (255, 255, 255),
                                               [250, 180, 100, 50])
                play_font = pygame.font.SysFont("Arial", 45)
                play_text = play_font.render("Play", True, (0, 0, 0))
                display.blit(play_text, (255, 178))
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    play_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [250, 180, 100, 50])
                    display.blit(play_text, (255, 178))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        running_title = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if play_button.collidepoint(pos):
                            running_title = False

                pygame.display.update()

            running_game = True
            pygame.Surface.fill(display, (0, 0, 0))
            pygame.draw.rect(display, (0, 4, 255), [45, 95, 360, 280])
            for row in range(6):
                for col in range(7):
                    pygame.draw.circle(display, (0, 0, 0),
                                       ((MARGIN_X+RADIUS)*col+75,
                                        (MARGIN_Y+RADIUS)*row+125), RADIUS)
            # Setting up the game screen

            while running_game:  # Operates the game

                turn_font = pygame.font.SysFont("Arial", 12)
                turn_text = turn_font.render("[insert player here]'s Turn",
                                             True, (255, 255, 255))
                display.blit(turn_text, (430, 150))

                for col in range(7):    # Sets up a highlight of the move
                    button = pygame.draw.circle(display, (0, 0, 0),
                                                ((MARGIN_X + RADIUS)*col + 75,
                                                 (MARGIN_Y + RADIUS) + 25),
                                                RADIUS)
                    if button.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.circle(display, (255, 255, 0),
                                           ((MARGIN_X + RADIUS)*col + 75,
                                            (MARGIN_Y + RADIUS) + 25), RADIUS)

                reset_button = pygame.draw.rect(display, (255, 255, 255),
                                               [450, 300, 75, 25])
                reset_font = pygame.font.SysFont("Arial", 12)
                reset_text = reset_font.render("Main Menu", True, (0, 0, 0))
                display.blit(reset_text, (458, 305))
                if reset_button.collidepoint(pygame.mouse.get_pos()):
                    reset_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [450, 300, 75, 25])
                    display.blit(reset_text, (458, 305))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        running_game = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if reset_button.collidepoint(pos):
                            QuadlineGUI()

                pygame.display.update()


if __name__ == '__main__':
    QuadlineGUI()
