import random
import time

class Car:
    # Class attribute (shared by all cars)
    max_speed = 180  # maximum speed in km/h

    # Constructor (defines how to build a car)
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.distance = 0  # how far the car has traveled

    # Method to accelerate randomly
    def accelerate(self):
        increase = random.randint(10, 30)
        if self.speed + increase < Car.max_speed:
            self.speed += increase
        else:
            self.speed = Car.max_speed

    # Method to move the car forward
    def move(self):
        # Add some randomness for fun
        self.accelerate()
        self.distance += self.speed * 0.05  # simulate distance covered per time unit

    # Method to display the car's status
    def show_status(self):
        print(f"{self.color} {self.name} → Speed: {self.speed} km/h | Distance: {self.distance:.2f} km")


def start_race(car1, car2, finish_line=5):
    print("\n🏁 The Race Begins! 🏁")
    print(f"Finish line: {finish_line} km\n")
    time.sleep(1)

    while car1.distance < finish_line and car2.distance < finish_line:
        car1.move()
        car2.move()

        # Print race status
        car1.show_status()
        car2.show_status()
        print("-" * 40)
        time.sleep(1)

    # Decide the winner
    if car1.distance >= finish_line and car2.distance >= finish_line:
        print("🤝 It's a tie!")
    elif car1.distance >= finish_line:
        print(f"🏆 {car1.color} {car1.name} wins the race!")
    else:
        print(f"🏆 {car2.color} {car2.name} wins the race!")


# Create car objects
car1 = Car("Ferrari", "Red")
car2 = Car("Lamborghini", "Yellow")

# Start the race
start_race(car1, car2)
