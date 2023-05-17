from animal import Zebra, Lion  
import random

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        
        self.timestep = 0
        self.world = world_size
        self.zebras = []
        self.lions = []

        # Randomly spawn zebras
        available_coordinates = [(x, y) for x in range(self.world) for y in range(self.world)]
        random.shuffle(available_coordinates)
        for _ in range(num_zebras):
            x, y = available_coordinates.pop()
            self.zebras.append(Zebra(x, y))

        # Randomly spawn lions
        available_coordinates = [(x, y) for x in range(self.world) for y in range(self.world)]
        random.shuffle(available_coordinates)
        for _ in range(num_lions):
            x, y = available_coordinates.pop()
            self.lions.append(Lion(x, y))

        print(f'\n')
        print("welcome to AIE safari")
        print(f'\nworld size = {world_size}')
        print(f'\nnum zebras = {num_zebras}')
        print(f'\nnum lions = {num_lions}')
        print(f'\n')
    
    def display(self):
        
        cell_size = 5
        self.update_grid()
        #para el 1234 de arriba
        coordenates = [f'{coord}' for coord in range(len(self.grid))]
        print(' ',end=' ')
        for coord in coordenates:
            if int(coord) < 10:
                print('    ' + coord, end=' ')
            else:
                print('   ' + coord, end=' ')
        print()

        # por la cantidad de cuadros por - te da cierta cantidad pero es insuficiente. Lo llenas con '--'
        print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
        for row_idx, row in enumerate(self.grid):
            if row_idx < 10:
                print(f"{coordenates[row_idx]}  |" + "|".join(row) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
            else:
                print(f"{coordenates[row_idx]} |" + "|".join(row) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')

        print(f'time step: {self.timestep}')

        #for line in self.grid:
            #print(line)

        key = input('press [q] to quit')
        if key == 'q':
            exit()

    def update_grid(self):

        cell_size = 5
        self.grid = []
        # arma 5 listas blancas
        for row in range(self.world):
            self.grid.append([])
            # en las que en cada lista tienen 5 espacios blancos de tamano 3.
            for col in range(self.world):
                #se puede entender como grid[row], como la parte row, lista 1,2,3,y asi
                is_empty = True
                for animal in self.zebras:
                    if animal.x == col and animal.y == row:
                        self.grid[row].append((" " *2) + "Z" + (" " *2))
                        is_empty = False
                        break
                    
                    for animal in self.lions:
                        if animal.x == col and animal.y == row:
                            self.grid[row].append((" " *2) + "L" + (" " *2))
                            is_empty = False
                            break

                if is_empty:
                    self.grid[row].append(" " * cell_size)

    def step_move(self):

        for zebra in self.zebras:
            zebra.move(self.grid)
            self.update_grid()

        for lion in self.lions:
            lion.move(self.grid)
            self.update_grid()

    def step_breed(self):
        for animal in self.zebras + self.lions:
            x, y = 0, 0
            animal.breed(x,y)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            #self.step_breed()
            #self.display()

if __name__ == '__main__':

    safari = CircleOfLife(20, 10, 10)
    safari.display()
    # safari.step_move()
    # safari.step_breed()
    safari.run(100)
