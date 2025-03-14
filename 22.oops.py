class Vehicle:
    def __init__(self, v_type, rent_per_day):
        self.v_type = v_type
        self.rent_per_day = rent_per_day
    
    def show_availability(self):
        print(f"{self.v_type} available: {self.stock} | Rent per day: Rs {self.rent_per_day} | Agency: {self.agency}")

class RentalAgency(Vehicle):
    def __init__(self, agency, v_type, rent_per_day):
        self.agency = agency
        super().__init__(v_type, rent_per_day)
    
    def get_days(self):
        return int(input("Enter number of days for rental: "))

class RentalBooking(RentalAgency):
    def __init__(self, agency, v_type, stock, rent_per_day):
        self.stock = stock
        super().__init__(agency, v_type, rent_per_day)
    
    def calculate_total(self, days, qty):
        return days * self.rent_per_day * qty

print("Welcome to the Rental System!")
print("------------------------------")

car_count = 450
car_rent = 45
bus_count = 200
bus_rent = 65

while True:
    print("\nOptions:")
    print("1. Rent a Car")
    print("2. Rent a Bus")
    print("3. Exit")
    
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if option == 1:
        car_rental = RentalBooking("Mumbai tour Rentals", "Car", car_count, car_rent)
        car_rental.show_availability()
        qty = int(input("How many cars do you need? "))
        if qty > car_count:
            print("Not enough cars available.")
            continue
        car_count -= qty
        days = car_rental.get_days()
        total = car_rental.calculate_total(days, qty)
        print(f"Booking Confirmed: {qty} cars from Mumbai tour Rentals. Total Cost: Rs {total}")
    
    elif option == 2:
        bus_rental = RentalBooking("SRS Travels", "Bus", bus_count, bus_rent)
        bus_rental.show_availability()
        qty = int(input("How many buses do you need? "))
        if qty > bus_count:
            print("Not enough buses available.")
            continue
        bus_count -= qty
        days = bus_rental.get_days()
        total = bus_rental.calculate_total(days, qty)
        print(f"Booking Confirmed: {qty} buses from SRS Travels. Total Cost: Rs {total}")
    
    elif option == 3:
        print("Thanks for visiting! Have a great day!")
        break
    
    else:
        print("Invalid choice, try again.")
