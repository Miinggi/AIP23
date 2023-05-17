import random

class Animal:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def move_to(self, grid, target, me):
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            print(me, 'moved to:', chosen_neighbor)
            return True
        else:
            return False

    def breed(self, x, y):
        return Animal(x, y)
    
    def get_neighbors(self, grid, target):
        
        #para la cantidad de rows
        world_width = len(grid)
        #print(len(grid))
        #para la cantidad de columns
        world_height = len(grid[0])
        #print(grid[1])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x-1, y])
        neighbors.append([x+1, y])
        neighbors.append([x, y-1])
        neighbors.append([x, y+1])
        print(neighbors)
        neighbors_valid = [neighbor for neighbor in neighbors
                           if  neighbor[0] >= 0
                           and neighbor[0] < world_width
                           and neighbor[1] >= 0
                           and neighbor[1] < world_height
                           and grid[neighbor[0]] [neighbor[1]] == target]
        print(neighbors_valid)
        return neighbors_valid

class Zebra(Animal):
    def move(self, grid):
        cell_size = 5
        self.move_to(grid, target=(" " * cell_size), me='Zebra')

class Lion(Animal):
    def move(self, grid):
        cell_size = 5
        hunt_is_successful = self.move_to(grid, target=(" " * (int(cell_size/2)-1)) + "Z" + (" " * int(cell_size/2)), me='Lion')
        if hunt_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target=(" " * cell_size), me='Lion')