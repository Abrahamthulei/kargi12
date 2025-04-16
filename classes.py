# Assignment 1: Design Your Own Class - Smartphone example 📱

class Smartphone:
    def __init__(self, brand, model, storage, camera_quality):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_quality = camera_quality

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a {self.camera_quality} quality photo. 📷")


# Inherited Class - GamingSmartphone 🎮
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_quality, gpu):
        super().__init__(brand, model, storage, camera_quality)
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"{self.brand} {self.model} is playing {game_name} with {self.gpu} GPU! 🕹️")


# Test the Smartphone and GamingSmartphone
phone1 = Smartphone("Samsung", "Galaxy S21", "128GB", "High")
phone1.call("123-456-7890")
phone1.take_photo()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", "256GB", "Ultra", "Adreno 730")
gaming_phone.call("987-654-3210")
gaming_phone.take_photo()
gaming_phone.play_game("PUBG Mobile")

print("\n" + "="*40 + "\n")

# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water. 🚢")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
