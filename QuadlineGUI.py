import pygame
from quadline import Quadline


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
        margin_x = 30
        margin_y = 25
        radius = 20

        # Operates the GUI while the window is open
        running_title = True
        running_manual = False
        while running:

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
                    pygame.draw.rect(display, (255, 255, 51),
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
                        elif manual_button.collidepoint(pos):
                            running_title = False
                            running_manual = True

                pygame.display.update()

            # Sets up the manual screen layout
            # running_manual = True
            pygame.Surface.fill(display, (0, 0, 0))

            # Operates the manual screen
            while running_manual:
                manual_font = pygame.font.SysFont("Arial", 70)
                manual_title_text = manual_font.render("How to Play", True,
                                                       (255, 255, 255))
                display.blit(manual_title_text, (115, 25))

                # Sets up menu button
                menu_button = pygame.draw.rect(display, (255, 255, 255),
                                               [265, 350, 75, 25])
                menu_font = pygame.font.SysFont("Arial", 12)
                menu_text = menu_font.render("Main Menu", True, (0, 0, 0))
                display.blit(menu_text, (273, 355))
                if menu_button.collidepoint(pygame.mouse.get_pos()):
                    menu_button = pygame.draw.rect(display, (255, 255, 51),
                                                   [265, 350, 75, 25])
                    display.blit(menu_text, (273, 355))

                # Display rules of the game
                rule_font = pygame.font.SysFont("Arial", 18)
                rule_text1 = rule_font.render("Number of players: 2 Players. "
                                              "Yellow and Red.", True,
                                              (255, 255, 255))
                rule_text2 = rule_font.render("Goal of the game: Create a "
                                              "4-in-a-row in any direction ",
                                              True, (255, 255, 255))
                rule_text3 = rule_font.render("before your opponent to win.",
                                              True, (255, 255, 255))
                rule_text4 = rule_font.render("Who moves first: Yellow moves "
                                              "first.", True, (255, 255, 255))
                rule_text5 = rule_font.render("Making your move: When it is "
                                              "your turn, click on one of ",
                                              True, (255, 255, 255))
                rule_text6 = rule_font.render("the move buttons to drop your "
                                              "token to the last empty ", True,
                                              (255, 255, 255))
                rule_text7 = rule_font.render("space in the specified column. "
                                              "Once you have made a move, ",
                                              True, (255, 255, 255))
                rule_text8 = rule_font.render("it becomes the opponents turn. "
                                              "Take turns dropping tokens ",
                                              True, (255, 255, 255))
                rule_text9 = rule_font.render("until someone wins.", True,
                                              (255, 255, 255))
                display.blit(rule_text1, (80, 120))
                display.blit(rule_text2, (80, 145))
                display.blit(rule_text3, (80, 170))
                display.blit(rule_text4, (80, 195))
                display.blit(rule_text5, (80, 220))
                display.blit(rule_text6, (80, 245))
                display.blit(rule_text7, (80, 270))
                display.blit(rule_text8, (80, 295))
                display.blit(rule_text9, (80, 320))

                # Run events in the manual screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        running = False
                        running_title = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(pos):
                            QuadlineGUI()

                pygame.display.update()

            # Sets up the game screen layout
            quadline = Quadline.Quadline()
            running_game = True
            pygame.Surface.fill(display, (0, 0, 0))
            pygame.draw.rect(display, (0, 4, 255), [45, 95, 360, 280])

            # Operates the game
            while running_game:

                # Monitor player's turn
                status_font = pygame.font.SysFont("Arial", 20)
                pygame.draw.rect(display, (0, 0, 0), [460, 150, 85, 50])
                status_string = ""
                if not quadline.is_game_over():
                    turn = quadline.get_current_player().color
                    if turn == "Y":
                        status_string = "P1's Turn"
                    elif turn == "R":
                        status_string = "P2's Turn"
                else:
                    winner = quadline.get_winner()
                    if winner == "Y":
                        status_string = "P1 Wins!"
                    elif winner == "R":
                        status_string = "P2 Wins!"
                    else:
                        status_string = "No Winner"
                status_text = status_font.render(status_string, True,
                                                 (255, 255, 255))
                display.blit(status_text, (460, 150))

                # Sets up a highlight of the move buttons
                move_buttons = []
                for col in range(7):
                    if not quadline.is_game_over():
                        button = pygame.draw.circle(display, (100, 100, 100),
                                                    ((margin_x + radius)*col +
                                                     75, (margin_y + radius) +
                                                     25), radius)
                        move_buttons.append(button)
                        if button.collidepoint(pygame.mouse.get_pos()):
                            color = (0, 0, 0)
                            if quadline.get_current_player().color == "Y":
                                color = (255, 255, 0)
                            elif quadline.get_current_player().color == "R":
                                color = (255, 0, 0)
                            pygame.draw.circle(display, color,
                                               ((margin_x + radius)*col + 75,
                                                (margin_y + radius) + 25),
                                               radius)
                    else:
                        pygame.draw.circle(display, (0, 0, 0),
                                                    ((margin_x + radius) * col +
                                                     75, (margin_y + radius) +
                                                     25), radius)

                # Sets up move button borders
                for i in range(8):
                    pygame.draw.line(display, (255, 255, 255), ((50*i)+49, 45),
                                     ((50*i)+49, 95), 1)

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
                                           ((margin_x + radius) * col + 75,
                                            (margin_y + radius) * row + 125),
                                           radius)

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
                        if restart_button.collidepoint(pos):
                            running_game = False
                        if not quadline.is_game_over():
                            for i in range(len(move_buttons)):
                                if move_buttons[i].collidepoint(pos):
                                    quadline.make_move(i)

                pygame.display.update()


if __name__ == '__main__':
    QuadlineGUI()
