import pygame
from quadline import Quadline

# TODO: IF ANY OF YOU ARE GOOD AT PYGAME OR HAVE TIME, FIX THE GUI STRUCTURE
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

        # token and margin size for visuals
        MARGIN_X = 30
        MARGIN_Y = 25
        RADIUS = 20

        # Operates the GUI while the window is open
        while running:
            running_title = True

            # Operates the title screen
            while running_title:
                title_font = pygame.font.SysFont("Arial", 100)
                title_text = title_font.render("Quadline", True,
                                               (255, 255, 255))
                display.blit(title_text, (100, 50))

                # Sets up play button
                play_button = pygame.draw.rect(display, (255, 255, 255),
                                               [215, 220, 170, 35])
                play_font = pygame.font.SysFont("Arial", 30)
                play_text = play_font.render("Play", True, (0, 0, 0))
                display.blit(play_text, (270, 220))
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    play_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [215, 220, 170, 35])
                    display.blit(play_text, (270, 220))

                # Sets up manual button
                manual_button = pygame.draw.rect(display, (255, 255, 255),
                                                 [215, 270, 170, 35])
                manual_font = pygame.font.SysFont("Arial", 30)
                manual_text = manual_font.render("How to Play", True, (0, 0, 0))
                display.blit(manual_text, (220, 270))
                if manual_button.collidepoint(pygame.mouse.get_pos()):
                    manual_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [215, 270, 170, 35])
                    display.blit(manual_text, (220, 270))

                # Run events in title screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        running = False
                        running_title = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if play_button.collidepoint(pos):
                            running_title = False

                pygame.display.update()

            # Sets up the game screen layout
            quadline = Quadline.Quadline()
            running_game = True
            pygame.Surface.fill(display, (0, 0, 0))
            pygame.draw.rect(display, (0, 4, 255), [45, 95, 360, 280])

            # pygame.draw.circle(display, (255, 255, 51),
            #                    (125, 350), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (175, 305), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (175, 260), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (225, 350), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (225, 260), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (275, 215), RADIUS)
            # pygame.draw.circle(display, (255, 255, 51),
            #                    (325, 350), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (125, 305), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (175, 350), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (225, 305), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (275, 260), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (275, 305), RADIUS)
            # pygame.draw.circle(display, (255, 0, 0),
            #                    (275, 350), RADIUS)

            # Operates the game
            while running_game:

                # Monitor player's turn TODO: fix this later
                turn_font = pygame.font.SysFont("Arial", 20)
                if not quadline.is_game_over():
                    turn = quadline.get_current_player().color
                    turn_text = ""
                    if turn == "Y":
                        turn_text = turn_font.render("P1's Turn",
                                                     True, (255, 255, 255))
                    elif turn == "R":
                        turn_text = turn_font.render("P2's Turn",
                                                     True, (255, 255, 255))
                    display.blit(turn_text, (460, 150))

                # Sets up a highlight of the move buttons
                move_buttons = []
                for col in range(7):
                    if not quadline.is_game_over():
                        button = pygame.draw.circle(display, (100, 100, 100),
                                                    ((MARGIN_X + RADIUS)*col + 75,
                                                     (MARGIN_Y + RADIUS) + 25),
                                                    RADIUS)
                        move_buttons.append(button)
                        if button.collidepoint(pygame.mouse.get_pos()):
                            color = (0, 0, 0)
                            if quadline.get_current_player().color == "Y":
                                color = (255, 255, 0)
                            elif quadline.get_current_player().color == "R":
                                color = (255, 0, 0)
                            pygame.draw.circle(display, color,
                                               ((MARGIN_X + RADIUS)*col + 75,
                                                (MARGIN_Y + RADIUS) + 25), RADIUS)
                    else:
                        button = pygame.draw.circle(display, (0, 0, 0),
                                                    ((MARGIN_X + RADIUS) * col + 75,
                                                     (MARGIN_Y + RADIUS) + 25),
                                                    RADIUS)

                for i in range(8):      # Sets up move button borders
                    line = pygame.draw.line(display, (255, 255, 255), ((50*i)+49, 45), ((50*i)+49, 95), 1)

                # Sets up menu button
                menu_button = pygame.draw.rect(display, (255, 255, 255),
                                                [462, 280, 75, 25])
                menu_font = pygame.font.SysFont("Arial", 12)
                menu_text = menu_font.render("Main Menu", True, (0, 0, 0))
                display.blit(menu_text, (470, 285))
                if menu_button.collidepoint(pygame.mouse.get_pos()):
                    menu_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [462, 280, 75, 25])
                    display.blit(menu_text, (470, 285))

                # Maintains the grid
                for row in range(6):
                    for col in range(7):
                        test = quadline.grid.get_token(row, col)
                        if test == "Y":
                            color = (255, 255, 0)
                        elif test == "R":
                            color = (255, 0, 0)
                        else:
                            color = (0, 0, 0)
                        pygame.draw.circle(display, color,
                                           ((MARGIN_X + RADIUS) * col + 75,
                                            (MARGIN_Y + RADIUS) * row + 125),
                                           RADIUS)

                # Sets up restart button
                restart_button = pygame.draw.rect(display, (255, 255, 255),
                                               [462, 320, 75, 25])
                restart_font = pygame.font.SysFont("Arial", 12)
                restart_text = restart_font.render("Restart", True, (0, 0, 0))
                display.blit(restart_text, (478, 325))
                if restart_button.collidepoint(pygame.mouse.get_pos()):
                    restart_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [462, 320, 75, 25])
                    display.blit(restart_text, (478, 325))

                # Run events in the game screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        running = False
                        running_game = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(pos):
                            QuadlineGUI()
                        # if restart_button.collidepoint(pos):
                        if not quadline.is_game_over():
                            if move_buttons[0].collidepoint(pos):
                                quadline.make_move(0)
                            if move_buttons[1].collidepoint(pos):
                                quadline.make_move(1)
                            if move_buttons[2].collidepoint(pos):
                                quadline.make_move(2)
                            if move_buttons[3].collidepoint(pos):
                                quadline.make_move(3)
                            if move_buttons[4].collidepoint(pos):
                                quadline.make_move(4)
                            if move_buttons[5].collidepoint(pos):
                                quadline.make_move(5)
                            if move_buttons[6].collidepoint(pos):
                                quadline.make_move(6)
                            quadline.grid.get_grid()

                pygame.display.update()


if __name__ == '__main__':
    QuadlineGUI()
