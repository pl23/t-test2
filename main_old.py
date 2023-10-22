import pygame
import getpass
import socket
import random
import numpy
from pprint import pprint

pygame.display.set_caption("")
block_size = 30
board_size = (10, 20)
board = [[0 for _ in range(board_size[0])] for _ in range(board_size[1])]
displayed_board = [[0 for _ in range(board_size[0])] for _ in range(board_size[1])]  # 10,20 d2
game_started = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pieces_gen_flag = False


board_screen_size = (board_size[0] * block_size, board_size[1] * block_size)

screen = pygame.display.set_mode(board_screen_size)
CLOCK = pygame.time.Clock()
fps = 5

pieces_list = [
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [1, 1, 1],
        [1, 0, 0]
    ],
    [
        [1, 1, 1],
        [0, 0, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]


def print_piece(picked_piece, displayed_board, x, y):
    s_y = y
    row_of_picked_piece = picked_piece[0]
    coll_of_picked_piece = row_of_picked_piece[0]
    n_row = len(picked_piece)
    n_coll = len(row_of_picked_piece)

    for a in range(n_row):
        for b in range(n_coll):
            if picked_piece[a][b] == 1:
                displayed_board[x][y] = 1
            else:
                displayed_board[x][y] = 0
            y += 1
        y = s_y
        x += 1


def pick_piece(input_list):
    if len(input_list) == 0:
        raise ValueError("Error: No list found!")
    else:
        n = len(input_list)
        n -= 1
        r = random.randint(0, n)
        picked_piece = pieces_list[r]
        return picked_piece


def piece_rotations(picked_piece):
    picked_piece = numpy.rot90(picked_piece)
    return picked_piece


def clamp(value, lower, upper):
    return min(max(lower, value), upper)


def draw_grid():
    for y in range(board_size[1]):
        for x in range(board_size[0]):
            cell_color = WHITE if displayed_board[y][x] == 0 else BLACK
            pygame.draw.rect(screen, cell_color, (x * block_size, y * block_size, block_size, block_size))


def update_displayed_board():
    x = 0
    y = 0
    for y_count in range(board_size[0]):
        for x_count in range(board_size[1]):
            if board[x_count][y_count] == 1:
                displayed_board[x_count][y_count] = 1
            elif board[x_count][y_count] == 0:
                displayed_board[x_count][y_count] = 0

        # a_count = 0
        # b_count = 0
        # print(board[x][y])

        # while a_count != 19:
        # while b_count != 9:
        #    if board[x][y] == 1:
        #        displayed_board[x][y] = 1
        #    elif board[x][y] == 0:
        #        displayed_board[x][y] = 0
        #    y += 1
        #    b_count += 1
        # y = 0
        # x += 1
        # a_count += 1
        # b_count = 0


def update_board():
    x = 0
    y = 0
    for y_count in range(board_size[0]):
        for x_count in range(board_size[1]):
            if displayed_board[x_count][y_count] == 1:
                board[x_count][y_count] = 1
            elif displayed_board[x_count][y_count] == 0:
                board[x_count][y_count] = 0


def game_loop(x,y):
    global pieces_gen_flag, picked_pieces


    if not pieces_gen_flag:
        picked_pieces = pick_piece(pieces_list)
        pieces_gen_flag = True

    else:
        update_displayed_board()
        falling_piece(x, y, picked_pieces)

    pprint (picked_pieces)




    draw_grid()
    pygame.display.flip()


def falling_piece(x, y, is_piece_in_memory):
    global displayed_board
    print_piece(is_piece_in_memory, displayed_board, x, y, )
    



def main():
    x,y = 0,4
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_loop(x,y)
        if x != 18:
            x += 1
        else:
            x = 0
            update_board()
            global pieces_gen_flag, picked_pieces
            pieces_gen_flag = True
            picked_pieces = pick_piece(pieces_list)
        CLOCK.tick(fps)


if __name__ == "__main__":
    main()
    pygame.quit()
    pprint(displayed_board)
