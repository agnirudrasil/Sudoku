import time
from math import inf
import random
import copy
import generator
import pygame
import win32api
import menu

diff, hin, mis = menu.diff, menu.hin, menu.mis
hin, diff, mis = int(hin), int(diff), int(mis)
BOARD = generator.SudokuGenerator(diff).grid
print(BOARD)
BOARD_SOLVED = copy.deepcopy(BOARD)
BOARD_SOLVED = generator.SudokuGenerator(diff, BOARD_SOLVED).grid
print(BOARD_SOLVED)
MISTAKE = ""
squares = 9 * 9
running = True
selected = False
selected_pencil = False
BOARD_USER = copy.deepcopy(BOARD)
BOARD_TEMP = [[[0 for col in range(9)] for col in range(9)] for row in range(9)]
START = time.time()

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((540, 600))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
font = pygame.font.SysFont("Arial Bold", 60)
font2 = pygame.font.SysFont("Jetbrains Mono", 15)
fonttime = pygame.font.SysFont("Jetbrains Mono Extra Bold", 35)
screen.blit(fonttime.render(f"5", True, (0, 0, 0)), (0, 550))
screen.fill((255, 255, 255))
pygame.display.set_caption("Sudoku")
pygame.display.set_icon(pygame.image.load("icon.png"))
TIME = pygame.Surface((540, 60))


def has_won(ai, board=BOARD_USER, master=BOARD_SOLVED):
    global running
    if len(MISTAKE) == mis:
        win32api.MessageBox(0, 'Game Over', 'Sudoku', 0x00001000)
        running = False
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != master[i][j]:
                return
    if board == master and ai:
        win32api.MessageBox(0, 'Machines > Humans 😉', 'Sudoku', 0x00001000)
        running = False
    if not ai:
        win32api.MessageBox(0, 'Congratulations! You Have Won!', 'Sudoku', 0x00001000)
        running = False
    return


def find_empty_random(board):
    empty_cells = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    print(empty_cells)
    try:
        return empty_cells[random.randint(0, len(empty_cells) - 1)]
    except:
        pass


def render_time(start=START):
    current_time = round(time.time() - start)
    min = str(current_time // 60)
    sec = str(current_time % 60)
    if len(sec) < 2:
        sec = "0" + sec
    if len(min) < 2:
        min = "0" + min
    TIME.fill((255, 255, 255))
    TIME.blit(fonttime.render(f"{min}:{sec}", True, (0, 0, 0)), (425, 7))
    TIME.blit(fonttime.render(MISTAKE, True, (255, 0, 0)), (5, 7))
    screen.blit(TIME, (0, 540))
    pygame.display.flip()


def render_pencil(pos, num, board=BOARD_TEMP, master=BOARD_USER):
    if master[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]][num - 1] = num
        if num == 1:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 5, pos[1] * 60 + 5))
        if num == 2:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 26, pos[1] * 60 + 5))
        if num == 3:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 48, pos[1] * 60 + 5))
        if num == 4:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 48, pos[1] * 60 + 23))
        if num == 5:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 48, pos[1] * 60 + 40))
        if num == 6:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 26, pos[1] * 60 + 40))
        if num == 7:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 5, pos[1] * 60 + 40))
        if num == 8:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 5, pos[1] * 60 + 23))
        if num == 9:
            screen.blit(font2.render(f"{num}", True, (120, 120, 120)), (pos[0] * 60 + 26, pos[1] * 60 + 23))
        master[pos[0]][pos[1]] = 0
        pygame.display.flip()
    elif master[pos[0]][pos[1]] != 0:
        temp = master[pos[0]][pos[1]]
        master[pos[0]][pos[1]] = 0
        render_pencil(pos, temp)
        reset_display()


def clear_comments(pos, board=BOARD_TEMP):
    for k in range(0, 9):
        board[pos[0]][pos[1]][k] = 0


def clear_final(pos, board=BOARD_USER):
    board[pos[0]][pos[1]] = 0


def render_pencil_marks(board=BOARD_TEMP):
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                if board[i][j][k] != 0:
                    print("K is here")
                    render_pencil((i, j), k + 1)
    pygame.display.flip()


def reset_display(board=BOARD_USER):
    screen.fill((255, 255, 255))
    render_text(board)
    render_pencil_marks()
    draw_grid()
    render_time()
    pygame.display.flip()


def render_text(board, master=BOARD_SOLVED):
    global running
    for i in range(0, 540, 60):
        for j in range(0, 540, 60):
            if board[i // 60][j // 60] != 0 and board[i // 60][j // 60] == master[i // 60][j // 60]:
                text = font.render(str(board[i // 60][j // 60]), True, (0, 0, 0))
                screen.blit(text, (18 + i, 13 + j))
            elif board[i // 60][j // 60] != 0 and board[i // 60][j // 60] != master[i // 60][j // 60]:
                text = font.render(str(board[i // 60][j // 60]), True, (255, 0, 0))
                screen.blit(text, (18 + i, 13 + j))
                """if len(MISTAKE) == 10:
                    win32api.MessageBox(0, 'Game Over', 'Sudoku', 0x00001000)
                    pygame.quit()"""
            if board[i // 60][j // 60] == 0:
                text = font.render("", True, (0, 0, 0))
                screen.blit(text, (18 + i, 13 + j))


def render_text_ai(board, master=BOARD_SOLVED):
    for i in range(0, 540, 60):
        for j in range(0, 540, 60):
            if board[i // 60][j // 60] != 0 and board[i // 60][j // 60] == master[i // 60][j // 60]:
                text = font.render(str(board[i // 60][j // 60]), True, (0, 0, 0))
                screen.blit(text, (18 + i, 13 + j))
            elif board[i // 60][j // 60] != 0 and board[i // 60][j // 60] != master[i // 60][j // 60]:
                text = font.render(str(board[i // 60][j // 60]), True, (255, 0, 0))
                screen.blit(text, (18 + i, 13 + j))
            if board[i // 60][j // 60] == 0:
                text = font.render("", True, (0, 0, 0))
                screen.blit(text, (18 + i, 13 + j))


def display_text_animation(string):
    text = ''
    font = pygame.font.SysFont("Arial Bold", 60)
    for i in range(len(string)):
        screen.fill((255, 255, 255))
        text += string[i]
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (540/2, 600/2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)


def get_mouse_pos(pos):
    row, col = pos
    i = 0
    diff_row = diff_col = inf
    while True:
        if i < row:
            diff_row = min(diff_row, row - i)
        else:
            pass
        if i < col:
            diff_col = min(diff_col, col - i)
        else:
            pass
        if i > row and i > col:
            break
        i += 60
    return row - diff_row, col - diff_col


def draw_grid():
    gap = 540 // 9

    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            pygame.draw.line(screen, (0, 0, 0), (0, i * gap), (540, i * gap), 3)
            pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, 540), 3)

        pygame.draw.line(screen, (0, 0, 0), (0, i * gap), (540, i * gap))
        pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, 540))
    pygame.draw.line(screen, (0, 0, 0), (0, 540), (540, 540), 3)
    pygame.display.flip()


def find_empty(board=BOARD):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return i, j


def valid(num, pos, bo=BOARD):
    for i in range(0, 9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(0, 9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def reset_display_ai(board=BOARD_USER):
    screen.fill((255, 255, 255))
    render_text_ai(board)
    draw_grid()
    print(BOARD_USER)
    pygame.display.flip()


def find_empty_count(board):
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                count += 1
    return count


def solve():
    try:
        find = find_empty(BOARD_USER)
        if not find:
            return True
        else:
            row, col = find

        for i in range(0, 10):
            if valid(i, find, BOARD_USER):
                BOARD_USER[row][col] = i
                reset_display_ai()

                if solve():
                    return True

            BOARD_USER[row][col] = 0

        return False
    except:
        pass


render_text(BOARD)
draw_grid()
i = j = 1000
pen_x = pen_y = 1000
AI = False

while running:
    render_time()
    has_won(AI)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            i, j = pos[0] // 60, pos[1] // 60
            if BOARD[i][j] != 0:
                i = j = 1000
                continue
            if pos[1] > 540:
                continue
            reset_display()
            print(pos)
            row, col = get_mouse_pos(pos)
            print(row, col)
            pygame.draw.rect(screen, (0, 255, 0), (row, col, 60, 60), 3)
            selected = True
            selected_pencil = False
            pygame.display.flip()
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            pen_x, pen_y = pos[0] // 60, pos[1] // 60
            if BOARD[pen_x][pen_y] != 0:
                i = j = 1000
                continue
            if pos[1] > 540:
                continue
            if BOARD_USER[pen_x][pen_y] != 0:
                render_pencil((pen_x, pen_y), 0)
            reset_display()
            print(pos)
            row, col = get_mouse_pos(pos)
            print(row, col)
            pygame.draw.rect(screen, (120, 120, 120), (row, col, 60, 60), 3)
            selected = False
            selected_pencil = True
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if int(hin) > 0:
                    cell = find_empty_random(BOARD_USER)
                    hin -= 1
                    BOARD_USER[cell[0]][cell[1]] = BOARD_SOLVED[cell[0]][cell[1]]
                    display_text_animation(f"Hints Left: {hin}")
                    time.sleep(0.2)
                    reset_display()
                    pygame.draw.rect(screen, (0, 0, 255), (cell[0] * 60, cell[1] * 60, 60, 60), 3)
            if event.key == pygame.K_SPACE:
                AI = True
                display_text_animation("AI Solving in 3, 2, 1!")
                time.sleep(0.1)
                reset_display()
                for i in range(0, 9):
                    for j in range(0, 9):
                        if BOARD_USER[i][j] != BOARD[i][j]:
                            BOARD_USER[i][j] = 0
                MISTAKE = ""
                BOARD_TEMP = [[[0 for col in range(9)] for col in range(9)] for row in range(9)]
                reset_display()
                START = time.time()
                solve()
            if event.key == pygame.K_1 or event.key == pygame.K_KP1 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 1
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_2 or event.key == pygame.K_KP2 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 2
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_3 or event.key == pygame.K_KP3 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 3
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_4 or event.key == pygame.K_KP4 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 4
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_5 or event.key == pygame.K_KP5 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 5
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_6 or event.key == pygame.K_KP6 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 6
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_7 or event.key == pygame.K_KP7 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 7
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_8 or event.key == pygame.K_KP8 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 8
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_9 or event.key == pygame.K_KP9 and selected:
                try:
                    clear_comments((i, j))
                    if BOARD_USER[i][j] != 0:
                        screen.fill((255, 255, 255))
                        draw_grid()
                        render_text(BOARD_USER)
                    BOARD_USER[i][j] = 9
                    if BOARD_USER[i][j] != BOARD_SOLVED[i][j]:
                        MISTAKE += "X"
                    reset_display()
                    selected = False
                    i = j = 1000
                except:
                    pass
            if event.key == pygame.K_1 or event.key == pygame.K_KP1 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 1)
                except:
                    pass
            if event.key == pygame.K_2 or event.key == pygame.K_KP2 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 2)
                except:
                    pass
            if event.key == pygame.K_3 or event.key == pygame.K_KP3 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 3)
                except:
                    pass
            if event.key == pygame.K_4 or event.key == pygame.K_KP4 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 4)
                except:
                    pass
            if event.key == pygame.K_5 or event.key == pygame.K_KP5 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 5)
                except:
                    pass
            if event.key == pygame.K_6 or event.key == pygame.K_KP6 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 6)
                except:
                    pass
            if event.key == pygame.K_7 or event.key == pygame.K_KP7 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 7)
                except:
                    pass
            if event.key == pygame.K_8 or event.key == pygame.K_KP8 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 8)
                except:
                    pass
            if event.key == pygame.K_9 or event.key == pygame.K_KP9 and selected_pencil:
                try:
                    print("I Was Here")
                    render_pencil((pen_x, pen_y), 9)
                except:
                    pass
            if event.key == pygame.K_DELETE and selected_pencil or selected:
                print("Delete Was Pressed")
                try:
                    clear_comments((pen_x, pen_y))
                except:
                    pass
                try:
                    clear_final((i, j))
                except:
                    pass
                reset_display()

pygame.quit()
