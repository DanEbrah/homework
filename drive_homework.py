'''homework: 




'''


class Car: 
    def __init__(self, brand, milage_km):
        self.brand = brand
        self.milage_km = milage_km

    def drive(self, distace_km):
        self.milage_km = self.milage_km + distace_km


class ElectricCar(Car): #subclass
    def __init__(self, brand, milage_km, range):
        super().__init__(brand, milage_km)
        self.range = range
    
    def drive(self, distance_km):
        self.milage_km = self.milage_km + distance_km
        self.range = self.range - distance_km # subtract from by drive distance


class ICECar(Car):
    def __init__(self, brand, milage_km, fuel_consumption, fuel_level):
        Car.__init__(self, brand, milage_km)
        self.fuel_consumption = fuel_consumption
        self.fuel_level = fuel_level

    def drive(self, distance_km):
        self.milage_km = self.milage_km + distance_km
        self.fuel_level = self.fuel_level - distance_km * self.fuel_consumption / 100

#my_E_C = ElectricCar("Mercades",300000, 500)
#print(my_E_C.__dict__)
#print(my_E_C)
#print("\n")

#ice_car = ICECar("toyota", 2500, 10, 60)
#print(ice_car.__dict__)

my_E_C = ElectricCar("Toyota", 130000, 10000)
my_E_C.drive(1000)
my_E_C.drive(2000)
my_E_C.drive(3000)
print(my_E_C.__dict__)

my_ice_car = ICECar("Mercades", 12000, 13, 100)
my_ice_car.drive(100)
print(my_ice_car.__dict__)