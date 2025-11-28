import pygame
import sys

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 8
BOARD_ROWS = 3
BOARD_COLS = 3
CELL_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 8
CROSS_WIDTH = 10
SPACE = CELL_SIZE // 4

BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
RED = (220, 20, 60)
GREEN = (80, 200, 120)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe — Pygame")
font = pygame.font.SysFont(None, 48)

board = [" " for _ in range(9)]
current_player = "X"
game_over = False
winner = None

def draw_board():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (CELL_SIZE * 2, 0), (CELL_SIZE * 2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, CELL_SIZE * 2), (WIDTH, CELL_SIZE * 2), LINE_WIDTH)

def draw_marks():
    for idx, mark in enumerate(board):
        row = idx // BOARD_COLS
        col = idx % BOARD_COLS
        cx = col * CELL_SIZE + CELL_SIZE // 2
        cy = row * CELL_SIZE + CELL_SIZE // 2

        if mark == "O":
            pygame.draw.circle(screen, GREEN, (cx, cy), CIRCLE_RADIUS, CIRCLE_WIDTH)
        elif mark == "X":
            p1 = (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE)
            p2 = (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE)
            pygame.draw.line(screen, RED, p1, p2, CROSS_WIDTH)
            p3 = (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE)
            p4 = (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE)
            pygame.draw.line(screen, RED, p3, p4, CROSS_WIDTH)

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return cond
    return None

def is_draw():
    return all(c != " " for c in board)

def show_message(text, subtext=None):
    text_surf = font.render(text, True, WHITE)
    rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
    screen.blit(text_surf, rect)

    if subtext:
        small_font = pygame.font.SysFont(None, 28)
        sub_surf = small_font.render(subtext, True, WHITE)
        sub_rect = sub_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 25))
        screen.blit(sub_surf, sub_rect)

def highlight_cells(cells):
    for idx in cells:
        row = idx // BOARD_COLS
        col = idx % BOARD_COLS
        rect = pygame.Rect(col * CELL_SIZE + LINE_WIDTH//2, row * CELL_SIZE + LINE_WIDTH//2,
                           CELL_SIZE - LINE_WIDTH, CELL_SIZE - LINE_WIDTH)
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        s.fill((255, 255, 255, 30))
        screen.blit(s, rect.topleft)

clock = pygame.time.Clock()

while True:
    draw_board()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = event.pos
            col = mx // CELL_SIZE
            row = my // CELL_SIZE
            idx = row * BOARD_COLS + col

            if 0 <= idx < 9 and board[idx] == " ":
                board[idx] = current_player
                win_cells = check_winner(current_player)

                if win_cells:
                    game_over = True
                    winner = current_player
                    winning_cells = win_cells
                elif is_draw():
                    game_over = True
                    winner = None
                    winning_cells = None
                else:
                    current_player = "O" if current_player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [" " for _ in range(9)]
                current_player = "X"
                game_over = False
                winner = None

    if game_over:
        if winner:
            highlight_cells(winning_cells)
            show_message(f"Player {winner} wins!", "Press R to restart")
        else:
            show_message("It's a draw!", "Press R to restart")
    else:
        small_font = pygame.font.SysFont(None, 28)
        turn_surf = small_font.render(f"Turn: {current_player}  (Press R to restart)", True, WHITE)
        screen.blit(turn_surf, (10, 10))

    pygame.display.flip()
    clock.tick(60)
