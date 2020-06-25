import random as rnd


class Cell:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign


class Grid:
    def __init__(self):
        self.cells = [[Cell(0, 0, ' '), Cell(1, 0, ' '), Cell(2, 0, ' ')],
                      [Cell(0, 1, ' '), Cell(1, 1, ' '), Cell(2, 1, ' ')],
                      [Cell(0, 2, ' '), Cell(1, 2, ' '), Cell(2, 2, ' ')]]
        self.free_cells = [(cell.x, cell.y) for row in self.cells for cell in row]

    def check_cell(self, x, y, sign):
        for row in self.cells:
            for cell in row:
                if x == cell.x and y == cell.y:
                    cell.sign = sign
                    self.update_free_cells()
                    break

    def get_cell_sign(self, x, y):
        for row in self.cells:
            for cell in row:
                if cell.x == x and cell.y == y:
                    return cell.sign
        return None

    def update_free_cells(self):
        self.free_cells = [(cell.x, cell.y) for row in self.cells for cell in row if cell.sign == ' ']

    def shuffle_free_cells(self):
        rnd.shuffle(self.free_cells)

    def show(self):
        print('---------\n'
              f'| {self.cells[2][0].sign} {self.cells[2][1].sign} {self.cells[2][2].sign} |\n'
              f'| {self.cells[1][0].sign} {self.cells[1][1].sign} {self.cells[1][2].sign} |\n'
              f'| {self.cells[0][0].sign} {self.cells[0][1].sign} {self.cells[0][2].sign} |\n'
              '---------')


class User:

    def __init__(self, sign):
        self.sign = sign
        self.mode = 'user'

    def make_move(self, x, y, grid):
        grid.check_cell(x, y, self.sign)


class AI:
    def __init__(self, sign, mode):
        self.sign = sign
        self.mode = mode
        self.opponents_sign = 'X' if self.sign == 'O' else 'O'

    def make_move(self, grid):
        if self.mode == 'easy':
            print('Making move level "easy"')
            self.easy_move(grid)
        elif self.mode == 'medium':
            print('Making move level "medium"')
            self.medium_move(grid)

    def easy_move(self, grid):
        grid.shuffle_free_cells()
        grid.check_cell(grid.free_cells[0][0], grid.free_cells[0][1], self.sign)

    def medium_move(self, grid):
        strategy = self.where_do_i_win(grid.cells)

        if strategy[0]:
            grid.check_cell(strategy[1], strategy[2], self.sign)
        else:
            strategy = self.where_does_opponent_win(grid.cells)

            if strategy[0]:
                grid.check_cell(strategy[1], strategy[2], self.sign)
            else:
                self.easy_move(grid)

    def where_do_i_win(self, cells):
        rows = [cells[0], cells[1], cells[2],
                [cells[i][0] for i in range(3)],
                [cells[i][1] for i in range(3)],
                [cells[i][2] for i in range(3)],
                [cells[i][i] for i in range(3)],
                [cells[2 - i][i] for i in range(3)]]

        for row in rows:
            if [cell.sign for cell in row].count(self.sign) == 2:
                for cell in row:
                    if cell.sign == ' ':
                        return True, cell.x, cell.y

        return False, None, None

    def where_does_opponent_win(self, cells):

        opponent_sign = 'X' if self.sign == 'O' else 'O'

        rows = [cells[0], cells[1], cells[2],
                [cells[i][0] for i in range(3)],
                [cells[i][1] for i in range(3)],
                [cells[i][2] for i in range(3)],
                [cells[i][i] for i in range(3)],
                [cells[2 - i][i] for i in range(3)]]

        for row in rows:
            if [cell.sign for cell in row].count(opponent_sign) == 2:
                for cell in row:
                    if cell.sign == ' ':
                        return True, cell.x, cell.y

        return False, None, None


def win_check(cells):
    horizontals = [cells[0], cells[1], cells[2]]
    verticals = [[cells[i][0] for i in range(3)],
                 [cells[i][1] for i in range(3)],
                 [cells[i][2] for i in range(3)]]
    diagonals = [[cells[i][i] for i in range(3)],
                 [cells[2 - i][i] for i in range(3)]]

    for row in horizontals:
        if all(cell.sign == 'X' for cell in row):
            return True, False, False

    for row in horizontals:
        if all(cell.sign == 'O' for cell in row):
            return False, True, False

    for row in verticals:
        if all(cell.sign == 'X' for cell in row):
            return True, False, False

    for row in verticals:
        if all(cell.sign == 'O' for cell in row):
            return False, True, False

    for row in diagonals:
        if all(cell.sign == 'X' for cell in row):
            return True, False, False

    for row in diagonals:
        if all(cell.sign == 'O' for cell in row):
            return False, True, False

    if all(cell.sign != ' ' for row in cells for cell in row):
        return False, False, True
    else:
        return False, False, False


while True:

    commands = input('Input command: ').lstrip('> ').split()

    cords = []
    x, y = -1, -1

    k = 0

    if len(commands) == 1:
        if commands[0] == 'exit':
            exit(0)
        else:
            print('Bad parameters!')
            continue
    elif len(commands) == 3:
        if not all(command == 'start' or command == 'user' or command == 'easy' or command == 'medium' for command in
                   commands):
            print('Bad parameters!')
            continue
    else:
        print('Bad parameters!')
        continue

    grid = Grid()

    if commands[1] == 'user':
        player_1 = User('X')
    else:
        player_1 = AI('X', commands[1])

    if commands[2] == 'user':
        player_2 = User('O')
    else:
        player_2 = AI('O', commands[2])

    grid.show()

    while True:

        if player_1.mode == 'user':
            cords = input('Enter the coordinates: ').lstrip('> ').split()

            if not all([el.isnumeric() for el in cords]):
                print('You should enter numbers!')
                continue

            cords = [int(el) - 1 for el in cords]

            x, y = cords[0], cords[1]

            if x > 2 or x < 0 or y > 2 or y < 0:
                print('Coordinates should be from 1 to 3!')
                continue

            if grid.get_cell_sign(x, y) != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            player_1.make_move(x, y, grid)
        else:
            player_1.make_move(grid)

        grid.show()

        k += 1

        if k >= 5:
            x_res, o_res, draw_res = win_check(grid.cells)
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

            x, y = cords[0], cords[1]

            if x > 2 or x < 0 or y > 2 or y < 0:
                print('Coordinates should be from 1 to 3!')
                continue

            if grid.get_cell_sign(x, y) != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            player_2.make_move(x, y, grid)
        else:
            player_2.make_move(grid)

        grid.show()

        k += 1

        if k >= 5:
            x_res, o_res, draw_res = win_check(grid.cells)
            if x_res:
                print('X wins')
                break
            elif o_res:
                print('O wins')
                break
            elif draw_res:
                print('Draw')
                break
