import random as rnd


def show_grid():
    print('---------\n'
          f'| {cells[2][0]} {cells[2][1]} {cells[2][2]} |\n'
          f'| {cells[1][0]} {cells[1][1]} {cells[1][2]} |\n'
          f'| {cells[0][0]} {cells[0][1]} {cells[0][2]} |\n'
          '---------')


def check():
    rows = [cells[0], cells[1], cells[2],
            [cells[i][0] for i in range(0, 3)],
            [cells[i][1] for i in range(0, 3)],
            [cells[i][2] for i in range(0, 3)],
            [cells[i][i] for i in range(0, 3)],
            [cells[2 - i][i] for i in range(0, 3)]]

    x_result = any([all([row[i] == 'X' for i in range(3)]) for row in rows])
    o_result = any([all([row[i] == 'O' for i in range(3)]) for row in rows])
    draw_result = all([all([row[i] != ' ' for i in range(3)]) for row in rows])

    return x_result, o_result, draw_result


cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

free_cells = [[i, j] for i in range(3) for j in range(3)]

show_grid()

nums = '1234567890'

cords = []
x, y = -1, -1

k = 0

while True:

    cords = input('Enter the coordinates: ').lstrip('> ').split()

    if not all([el.isnumeric() for el in cords]):
        print('You should enter numbers!')
        continue

    cords = [int(el) - 1 for el in cords]

    y, x = cords[0], cords[1]

    if x > 2 or x < 0 or y > 2 or y < 0:
        print('Coordinates should be from 1 to 3!')
        continue

    if cells[x][y] != ' ':
        print('This cell is occupied! Choose another one!')
        continue

    cells[x][y] = 'X'

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

    print('Making move level "easy"')

    free_cells.remove([x, y])
    rnd.shuffle(free_cells)

    cells[free_cells[0][0]][free_cells[0][1]] = 'O'

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
