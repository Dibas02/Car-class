class vehcle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage


bmw = vehcle(200, 22)

print("Max speed: ", bmw.max_speed)
print("Milage: ", bmw.milage)

