def display(self):
    print(f'Clock: {self.timestep}')
    top_coord_str = '/t'.joinA([f'{coord}' for coord in range(len(self.grid))])
    print(top_coord_str)
    for animal in self.zebras:
        self.grid[animal.y][animal.x] = 'Z'
    for animal in self.lions:
        self.grid[animal.y][animal.x] = 'L'
    for line in self.grid:
        print(line)
    # print_TODO('display()')
    key = input('press [q] to quit')
    if key == 'q':
        exit()