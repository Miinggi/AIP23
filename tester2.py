
def get_neighbors(self, grid, target):

    world_width = len(grid)
    world_height = len(grid[0])
    x, y = self.x, self.y
    neighbors = []
    neighbors.append([x-1, y])
    neighbors.append([x+1, y])
    neighbors.append([x, y-1])
    neighbors.append([x, y+1])
    neighbors_valid = [neighbor for neighbor in neighbors
                        if grid[neighbor[1]] [neighbor[0]] == target
                        and neighbor[0] >= 0
                        and neighbor[0] < world_width
                        and neighbor[1] >= 0
                        and neighbor[1] < world_height]
    return neighbors_valid

get_neighbors(3,)