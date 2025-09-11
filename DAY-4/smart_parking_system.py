from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name
    
    def get_license_plate(self):
        return self.__license_plate
    
    def get_owner_name(self):
        return self.__owner_name

    
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self, id):
        print("---BIKE DETAILS---")
        print(f"ID: {id}")
        print(f"Owner Name: {self.get_owner_name()}")
        print(f"License Plate: {self.get_license_plate()}")
        print(f"Helmet Required: {self.helmet_required}")

    def parking_fee(self, hours):
        fee = 20 * hours
        print(f"Bike Parking Fee for {hours} hours: ₹{fee}")
        return fee

class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self, id):
        print("\n--- CAR DETAILS ---")
        print(f"ID: {id}")
        print(f"Owner Name: {self.get_owner_name()}")
        print(f"License Plate: {self.get_license_plate()}")
        print(f"Number of Seats: {self.seats}")

    def parking_fee(self, hours):
        fee = 50 * hours
        print(f"Car Parking Fee for {hours} hours: ₹{fee}")
        return fee


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self, id):
        print("\n--- SUV DETAILS ---")
        print(f"ID: {id}")
        print(f"Owner Name: {self.get_owner_name()}")
        print(f"License Plate: {self.get_license_plate()}")
        print(f"Four Wheel Drive: {self.four_wheel_drive}")

    def parking_fee(self, hours):
        fee = 70 * hours
        print(f"SUV Parking Fee for {hours} hours: ₹{fee}")
        return fee


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self, id):
        print("\n--- TRUCK DETAILS ---")
        print(f"ID: {id}")
        print(f"Owner Name: {self.get_owner_name()}")
        print(f"License Plate: {self.get_license_plate()}")
        print(f"Max Load Capacity: {self.max_load_capacity} tons")

    def parking_fee(self, hours):
        fee = 100 * hours
        print(f"Truck Parking Fee for {hours} hours: ₹{fee}")
        return fee

    
class Payment(ABC):
    @abstractmethod
    def pay(self): pass
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")

class ParkingSlot:
    def __init__(self, slot_id, size):
        self.slot_id = slot_id
        self.size = size
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        size_map = {'S': Bike, 'M': Car, 'L': SUV, 'XL': Truck}
        allowed = {
            'S': [Bike],
            'M': [Bike, Car],
            'L': [Bike, Car, SUV],
            'XL': [Bike, Car, SUV, Truck]
        }
        if type(vehicle) in allowed[self.size] and self.vehicle is None:
            self.vehicle = vehicle
            print(f"{vehicle.get_license_plate()} parked at Slot {self.slot_id} ({self.size})")
            return True
        return False

    def remove_vehicle(self):
        if self.vehicle:
            v = self.vehicle
            self.vehicle = None
            return v
        return None

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.slots = []

    def add_spot(self, slot):
        self.slots.append(slot)

    def show_spots(self):
        for s in self.slots:
            status = f"Occupied → {s.vehicle.get_license_plate()}" if s.vehicle else "Empty"
            print(f"Slot {s.slot_id} ({s.size}): {status}")

    def park_vehicle(self, vehicle):
        for s in self.slots:
            if s.assign_vehicle(vehicle):
                return
        print(f"No suitable slot for {vehicle.get_license_plate()}")

    def unpark_vehicle(self, vehicle, hours):
        for s in self.slots:
            if s.vehicle == vehicle:
                s.remove_vehicle()
                fee = vehicle.parking_fee(hours)
                print("Select payment method: 1.Cash 2.Card 3.UPI")
                choice = input("Enter choice: ")
                if choice == '1':
                    CashPayment().pay(fee)
                elif choice == '2':
                    CardPayment().pay(fee)
                elif choice == '3':
                    UPIPayment().pay(fee)
                return
        print(f"{vehicle.get_license_plate()} not found in parking lot")
def main():

    b1 = Bike("TS09AB1234","Mahi")
    c1 = Car("TS10CD5678","Meera")
    s1 = SUV("TS08EF9876","Shahi")
    t1 = Truck("TS07GH4567","sanvi", 15)

    lot = ParkingLot("City Center")
    lot.add_spot(ParkingSlot("S1","S"))
    lot.add_spot(ParkingSlot("S2","M"))
    lot.add_spot(ParkingSlot("S3","L"))
    lot.add_spot(ParkingSlot("S4","XL"))


    lot.show_spots()

    lot.park_vehicle(b1)
    lot.park_vehicle(c1)
    lot.park_vehicle(s1)
    lot.park_vehicle(t1)

    lot.show_spots()

    for v in [b1, c1, s1, t1]:
        v.display("V001")

    lot.unpark_vehicle(c1, 3) 
if __name__ == "__main__":
    main()