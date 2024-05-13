class Vehicle():
    vehicle_type = None

class Car():
    price = 1000000
    def horse_powers(self):
        return 100

class Nissan (Car, Vehicle):
    price = 150000
    vehicle_type = 'Sportcar'

    def horse_powers(self):
        return 240


My_Car = Nissan()
My_Car.price
My_Car.vehicle_type
My_Car.horse_powers
print(My_Car.vehicle_type)
print(My_Car.price)
print(My_Car.horse_powers)
