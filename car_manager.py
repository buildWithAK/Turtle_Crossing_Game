from turtle import Turtle
import random 

COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "cyan",
    "brown",
    "gold",
    "gray",
    "navy",
    "magenta",
    "lime",
    "violet"
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 4)  # Adjust the range to control car creation frequency

        if random_chance == 1:
            random_y = random.randint(-240, 240)

            # Check if the new car is too close to an existing car
            for car in self.all_cars:
                if abs(car.ycor() - random_y) < 25 and abs(car.xcor() - 300) < 50:
                    return

            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
