class Animal:
    def __init__(self,weight,height):
            self.weight = weight
            self.height = height

    def move (self):
            pass
    
class Snake(Animal):
    def move(self):
        print("I slither")

class Bird(Animal): 
    def __init__(self, weight, height, max_altitude): 
        super().__init__(weight, height)
        self.max_altitude = max_altitude   

    def move(self):
        print("I fly")      

# Instances of Snake and Bird
snake = Snake(10, 50)
bird = Bird(5, 30, 1000)


snake.move()  
bird.move()   