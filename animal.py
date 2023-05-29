import random

class Animal:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 3
        self.age = 0

    def move_to(self, grid, target, me):
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            buffer = f'{me}, moved from: {self.x}, {self.y}'
            grid[self.x][self.y] = Empty(self.x, self.y) #empty animals location
            chosen_neighbor = random.choice(neighbors) #choose a random neighboring coordinate
            self.x, self.y = chosen_neighbor #assign new coordinates to self.x,y for the animal
            grid[self.x][self.y].hp = 0  # kill the animal in the new location(exclusive to lions)(refer to move within zebra and lions)
            grid[self.x][self.y] = self #move animal to no coordinates
            print(buffer + ' to:', self.y, self.x)
            return True
        else:
            return False
    
    def get_neighbors(self, grid, target):
        # get the width and height of the world and find potential coordinates to move animal to
        world_width = len(grid)
        world_height = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x - 1, y])
        neighbors.append([x + 1, y])
        neighbors.append([x, y - 1])
        neighbors.append([x, y + 1])
        # neighbor_valid checks if the coordinates are within the world and functions differently depending on what animal is moving
        neighbors_valid = []
        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor
            if (0 <= neighbor_x < world_width) and (0 <= neighbor_y < world_height):
                if str(grid[neighbor_x][neighbor_y]) == target:
                    neighbors_valid.append(neighbor)

        return neighbors_valid
    
    def breed(self, grid):
        cell_size = 5
        child = self.__class__(self.y, self.x) # create new animal(instance) with the same coordinates as the parent
        child.move_to(grid, target=(" " * cell_size), me=self)  # move the child to an empty cell
        grid[self.y][self.x] = self

class Empty(Animal): # empty cell class
    def __str__(self):
        cell_size = 5
        return (" " * cell_size)

class Zebra(Animal):
    
    def __str__(self):
        return ((" " *2) + "Z" + (" " *2))

    def move(self, grid):
        cell_size = 5
        self.move_to(grid, target=(" " * cell_size), me='Zebra')

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 3 == 0 # % == 0 sees if the division has a remainder of 0
    
class Lion(Animal):

    def __str__(self):
        return((" " *2) + "L" + (" " *2))
    
    def move(self, grid):
        cell_size = 5
        hunt_is_successful = self.move_to(grid, target=((" " *2) + "Z" + (" " *2)), me='Lion')  
        if hunt_is_successful:
            self.hp = 3
            print("Lion ate a zebra")
        else:
            self.move_to(grid, target=(" " * cell_size), me='Lion')
            self.hp -= 1

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 8 == 0
    