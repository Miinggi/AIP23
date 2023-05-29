from animal import Empty, Zebra, Lion  
import random

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        
        self.timestep = 0
        self.world = world_size
        self.zebras = []
        self.lions = []

        # Randomly spawn zebras
        available_coordinates = [(x, y) for x in range(self.world) for y in range(self.world)]
        random.shuffle(available_coordinates) #shuffle list of all possible coordianates randomly
        for _ in range(num_zebras):
            x, y = available_coordinates.pop() # pop assigns itself to x and y then deletes itself from the list of available_coordinates
            self.zebras.append(Zebra(x, y)) #add zebras to said x and y coordinates

        # Randomly spawn lions
        for _ in range(num_lions):
            x, y = available_coordinates.pop()
            self.lions.append(Lion(x, y))
        self.update_grid()

        print(f'\n')
        print("welcome to AIE safari")
        print(f'\nworld size = {world_size}')
        print(f'\nnum zebras = {num_zebras}')
        print(f'\nnum lions = {num_lions}')
        print(f'\n')
    
    def display(self):
        
        cell_size = 5
        # create vertical numbers along left side for y axis
        #para el 1234 de arriba
        coordenates = [f'{coord}' for coord in range(len(self.grid))]
        print(' ',end=' ')
        for coord in coordenates:
            if int(coord) < 10:
                print('    ' + coord, end=' ')
            else:
                print('   ' + coord, end=' ')
        print()

        # print the grid with horizontal numbers along the top for x axis
        # por la cantidad de cuadros por - te da cierta cantidad pero es insuficiente. Lo llenas con '--'
        print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
        for row_idx, row in enumerate(self.grid): #row_idx position within row, row is the individual row itself and repeats itself for each row
            buffer = [str(animal) for animal in row] #temp store for each animal and empty cell in row until for loop reiterates
            if row_idx < 10: #if rows go to double digits, add extra space to keep grid aligned
                print(f"{coordenates[row_idx]}  |" + "|".join(buffer) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
            else:
                print(f"{coordenates[row_idx]} |" + "|".join(buffer) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')

        print(f'time step: {self.timestep}')

        #for line in self.grid:
            #print(line)

        key = input('press [q] to quit')
        if key == 'q':
            exit()

    def update_grid(self):

        self.grid = []
        # arma 5 listas blancas
        for row in range(self.world):
            self.grid.append([])
            # en las que en cada lista tienen 5 espacios blancos de tamano 3.
            for col in range(self.world):
                #se puede entender como grid[row], como la parte row, lista 1,2,3,y asi
                #checks each cell in the grid to see if there is an animal in it, if there is, it adds it's string to the grid
                if any(animal.x == row and animal.y == col for animal in self.zebras): #if any animal in the list of zebras has the same x and y as the current cell, add it to the grid
                    self.grid[row].append(Zebra(col, row))
                elif any(animal.x == row and animal.y == col for animal in self.lions):
                    self.grid[row].append(Lion(col, row))
                else:
                    self.grid[row].append(Empty(col, row))

    def step_move(self):

        animals = [animal for row in self.grid for animal in row
                   if not isinstance(animal, Empty)] # initially empty, then filters out Empty from animals and adds the animals list
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)
                
    def step_breed(self):

        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)
                   and animal.is_ready_to_breed()]
        
        for animal in animals:
            animal.breed(self.grid)

    def age(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if animal.hp == 0:
                    print(f'animal at position ({y}, {x}) has died.')
                    self.grid[y][x] = Empty(y,x)
                else:
                    self.grid[y][x].age += 1

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()
            self.age()

if __name__ == '__main__':
    zebra = Zebra(0,0)
    lion = Lion(0,0)
    safari = CircleOfLife(10, 10, 10)
    safari.run(100)


#current problems:
#Lions can breed with zebras
#Empty cells somehow contain ghost animals
#Zebras always win instead of balance(maybe lions need bias?)
#though lions eat they start to death next time step
#animals are moving more than one cell in one time step
#incorrect moved to coordinates
#zebra random death
#moved from to false positives
#zebra death isn't real
#I can't tell if dead bodies are vanishing