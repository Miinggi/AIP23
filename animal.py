class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def move(self, direction='right'):
        print(f'moving to {direction}. <<< NOT IMPLEMETED YET>>>')
        self.x += 1

    def breed(self, x, y):
        return Animal(x, y)
    
    print('animals')