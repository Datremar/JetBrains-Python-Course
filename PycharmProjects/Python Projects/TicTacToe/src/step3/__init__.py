import random as rnd


class Player:

    def __init__(self, mode, sign):
        self.mode = mode
        self.sign = sign

    def make_move(self, x, y, grid):
        grid[x][y] = self.sign


def show_grid():
    print('---------\n'
          f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} |\n'
          f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} |\n'
          f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} |\n'
          '---------')


def check():
    rows = [grid[0], grid[1], grid[2],
            [grid[i][0] for i in range(0, 3)],
            [grid[i][1] for i in range(0, 3)],
            [grid[i][2] for i in range(0, 3)],
            [grid[i][i] for i in range(0, 3)],
            [grid[2 - i][i] for i in range(0, 3)]]

    x_result = any([all([row[i] == 'X' for i in range(3)]) for row in rows])
    o_result = any([all([row[i] == 'O' for i in range(3)]) for row in rows])
    draw_result = all([all([row[i] != ' ' for i in range(3)]) for row in rows])

    return x_result, o_result, draw_result


while True:

    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    free_cells = [[i, j] for i in range(3) for j in range(3)]

    cords = []
    x, y = -1, -1

    k = 0

    commands = input('Input command: ').lstrip('> ').split()

    if len(commands) == 1:
        if commands[0] == 'exit':
            exit(0)
        else:
            print('Bad parameters!')
            continue
    elif len(commands) == 3:
        if not all(command == 'start' or command == 'user' or command == 'easy' for command in commands):
            print('Bad parameters!')
            continue
    else:
        print('Bad parameters!')
        continue

    player_1 = Player(commands[1], 'X')
    player_2 = Player(commands[2], 'O')

    show_grid()

    while True:

        if player_1.mode == 'user':
            cords = input('Enter the coordinates: ').lstrip('> ').split()

            if not all([el.isnumeric() for el in cords]):
                print('You should enter numbers!')
                continue

            cords = [int(el) - 1 for el in cords]

            y, x = cords[0], cords[1]

            if x > 2 or x < 0 or y > 2 or y < 0:
                print('Coordinates should be from 1 to 3!')
                continue

            if grid[x][y] != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            player_1.make_move(x, y, grid)
            free_cells.remove([x, y])
        else:
            print('Making move level "easy"')

            rnd.shuffle(free_cells)

            player_1.make_move(free_cells[0][0], free_cells[0][1], grid)

            free_cells.remove(free_cells[0])

        show_grid()

        k += 1

        if k >= 5:
            x_res, o_res, draw_res = check()
            if x_res:
                print('X wins')
                break
            elif o_res:
                print('O wins')
                break
            elif draw_res:
                print('Draw')
                break

        if player_2.mode == 'user':
            cords = input('Enter the coordinates: ').lstrip('> ').split()

            if not all([el.isnumeric() for el in cords]):
                print('You should enter numbers!')
                continue

            cords = [int(el) - 1 for el in cords]

            y, x = cords[0], cords[1]

            if x > 2 or x < 0 or y > 2 or y < 0:
                print('Coordinates should be from 1 to 3!')
                continue

            if grid[x][y] != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            player_2.make_move(x, y, grid)
            free_cells.remove([x, y])
        else:
            print('Making move level "easy"')

            rnd.shuffle(free_cells)

            player_2.make_move(free_cells[0][0], free_cells[0][1], grid)

            free_cells.remove(free_cells[0])

        show_grid()

        k += 1

        if k >= 5:
            x_res, o_res, draw_res = check()
            if x_res:
                print('X wins')
                break
            elif o_res:
                print('O wins')
                break
            elif draw_res:
                print('Draw')
                break
