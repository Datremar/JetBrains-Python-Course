import random as rnd


class Cell:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign


class Grid:
    def __init__(self):
        self.cells = [[Cell(0, 0, 'O'), Cell(1, 0, 'O'), Cell(2, 0, 'X')],
                      [Cell(0, 1, ' '), Cell(1, 1, ' '), Cell(2, 1, 'X')],
                      [Cell(0, 2, ' '), Cell(1, 2, 'X'), Cell(2, 2, ' ')]]
        self.free_cells = [(cell.x, cell.y) for row in self.cells for cell in row if cell.sign == ' ']

    def check_cell(self, x, y, sign):
        for row in self.cells:
            for cell in row:
                if x == cell.x and y == cell.y and cell.sign == ' ':
                    cell.sign = sign
                    self.update_free_cells()
                    break
                # elif cell.sign != ' ':
                #     print('OCCUPIED!')
                #     exit(1)

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

    def copy(self, grid):
        self.cells = [[Cell(cell.x, cell.y, cell.sign) for cell in row] for row in grid.cells]
        self.free_cells = [(cell.x, cell.y) for row in self.cells for cell in row if cell.sign == ' ']

    def show(self):
        print('---------\n'
              f'| {self.cells[2][0].sign} {self.cells[2][1].sign} {self.cells[2][2].sign} |\n'
              f'| {self.cells[1][0].sign} {self.cells[1][1].sign} {self.cells[1][2].sign} |\n'
              f'| {self.cells[0][0].sign} {self.cells[0][1].sign} {self.cells[0][2].sign} |\n'
              '---------')


def win_check(cells):
    rows = [cells[0], cells[1], cells[2],
            [cells[i][0] for i in range(3)],
            [cells[i][1] for i in range(3)],
            [cells[i][2] for i in range(3)],
            [cells[i][i] for i in range(3)],
            [cells[2 - i][i] for i in range(3)]]

    for row in rows:
        if all(cell.sign == 'X' for cell in row):
            return True, False, False

    for row in rows:
        if all(cell.sign == 'O' for cell in row):
            return False, True, False

    if all(cell.sign != ' ' for row in cells for cell in row):
        return False, False, True
    else:
        return False, False, False


def score(grid, depth):
    if win_check(grid.cells)[0]:
        return 10 - depth
    elif win_check(grid.cells)[1]:
        return depth - 10
    else:
        return 0


def minimax(grid, depth, x_turn):

    grid.show()

    if any(win_check(grid.cells)) or depth == 0:
        print(win_check(grid.cells))
        points = score(grid, depth)
        print(points)
        return points, None

    scores = []
    moves = []

    for cell in grid.free_cells:
        possible_grid = Grid()
        possible_grid.copy(grid)
        sign = 'X' if x_turn else 'O'

        possible_grid.check_cell(cell[0], cell[1], sign)

        scores.append(minimax(possible_grid, depth - 1, not x_turn)[0])
        moves.append(cell)

    if x_turn:
        max_index = scores.index(max(scores))
        return scores[max_index], moves[max_index]
    else:
        min_index = scores.index(min(scores))
        return scores[min_index], moves[min_index]


grid_ = Grid()

result = minimax(grid_, 4, True)

print()
print(result[1])
