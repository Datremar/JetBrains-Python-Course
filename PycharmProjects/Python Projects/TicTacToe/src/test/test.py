nums = '1234567890'



cords = []
x, y = -1, -1

cords = input('Enter the coordinates: ').lstrip('> ').split()

if not all([el in nums for el in cords]):
    print('You should enter numbers!')
    exit(0)
