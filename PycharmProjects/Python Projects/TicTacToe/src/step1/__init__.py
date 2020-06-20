def show_grid(cells):
    print('---------\n'
          f'| {cells[2][0]} {cells[2][1]} {cells[2][2]} |\n'
          f'| {cells[1][0]} {cells[1][1]} {cells[1][2]} |\n'
          f'| {cells[0][0]} {cells[0][1]} {cells[0][2]} |\n'
          '---------\n')


cells = input('Enter cells: ').lstrip('> ')

cells = list(cells)
cells = [' ' if el == '_' else el for el in cells]
cells = [cells[6:9], cells[3:6], cells[0:3]]

show_grid(cells)

nums = '1234567890'

cords = []
x, y = -1, -1

while True:
    cords = input('Enter the coordinates: ').lstrip('> ').split()

    if not all([el in nums for el in cords]):
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

    xs_num = 0
    os_num = 0

    for line in cells:
        for el in line:
            if el == 'O':
                os_num += 1
            elif el == 'X':
                xs_num += 1

    if xs_num > os_num:
        cells[x][y] = 'O'
    else:
        cells[x][y] = 'X'

    show_grid(cells)
    break

rows = [cells[0], cells[1], cells[2],
        [cells[i][0] for i in range(0, 3)],
        [cells[i][1] for i in range(0, 3)],
        [cells[i][2] for i in range(0, 3)],
        [cells[i][i] for i in range(0, 3)],
        [cells[2 - i][i] for i in range(0, 3)]]

x_result = any([all([row[i] == 'X' for i in range(3)]) for row in rows])
o_result = any([all([row[i] == 'O' for i in range(3)]) for row in rows])
draw_result = all([all([row[i] != ' ' for i in range(3)]) for row in rows])

if x_result:
    print('X wins')
elif o_result:
    print('O wins')
elif draw_result:
    print('Draw')
else:
    print('Game not finished')
