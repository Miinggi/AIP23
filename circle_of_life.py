from animal import Animal, Zebra, Lion
import os
import random

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        
        self.timestep = 0
        self.world = world_size
        self.zebras = [Zebra(0, 0) for _ in range(num_zebras)]
        self.lions = [Lion(1,1) for _ in range(num_lions)]
        print(f'\n')
        print("welcome to AIE safari")
        print(f'\nworld size = {world_size}')
        print(f'\nnum zebras = {num_zebras}')
        print(f'\nnum lions = {num_lions}')
        print(f'\n')

    def reset_grid(self):
        self.grid = []
    
    def display(self):
        cell_size = 10
        self.grid = []
        self.reset_grid()
        # arma 5 listas blancas
        for row in range(self.world):
            self.grid.append([])
            # en las que en cada lista tienen 5 espacios blancos de tamano 3.
            for col in range(self.world):
                #se puede entender como grid[row], como la parte row, lista 1,2,3,y asi
                is_empty = True
                for animal in self.zebras:
                    if animal.x == row and animal.y == col:
                        self.grid[row].append((" " *(int(cell_size/2)-1)) + "Z" + (" " *int(cell_size/2)))
                        is_empty = False
                        break

                if is_empty:
                    for animal in self.lions:
                        if animal.x == row and animal.y == col:
                            self.grid[row].append((" " *(int(cell_size/2)-1)) + "L" + (" " *int(cell_size/2)))
                            is_empty = False
                            break

                if is_empty:
                    self.grid[row].append(" " * cell_size)
                

        #para el 1234 de arriba
        coordenates = [f'{coord+1}' for coord in range(len(self.grid))]
        print('   ' + ((int(cell_size/2))*' ') + (cell_size*' ').join(coordenates))
        
        # por la cantidad de cuadros por - te da cierta cantidad pero es insuficiente. Lo llenas con '--'
        print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
        for row_idx, row in enumerate(self.grid):
            print(f"{coordenates[row_idx]}  |" + "|".join(row) + "|")
            print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')

        print(f'time step: {self.timestep}')

        #for line in self.grid:
            #print(line)

        key = input('press [q] to quit')
        if key == 'q':
            exit()

    def step_move(self):

        for zebra in self.zebras:
            zebra.move(self.grid)

        for lion in self.lions:
            lion.move(self.grid)

    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras + self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x,y)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()

if __name__ == '__main__':

    safari = CircleOfLife(5, 2, 2)
    safari.display()
    # safari.step_move()
    # safari.step_breed()
    safari.run(100)