class Transport:
    period = 0
    
    def __init__(self, vehicle_type, rent_price):
        self.vehicle_type = vehicle_type
        self.rent_price = rent_price
    
    def show_availability(self):
        print(f"The available {self.vehicle_type}s from {self.company_name} agency are {self.total_stock}, each costing Rs {self.rent_price} per day.")


class RentalAgency(Transport):
    def __init__(self, company_name, vehicle_type, rent_price):
        self.company_name = company_name
        super().__init__(vehicle_type, rent_price)
    
    def get_rental_period(self):        
        rental_days = int(input("Enter the rental period in days: "))
        return rental_days


class RentalTransaction(RentalAgency):
    def __init__(self, company_name, vehicle_type, total_stock, rent_price):
        self.total_stock = total_stock        
        super().__init__(company_name, vehicle_type, rent_price)
    
    def calculate_total(self, rental_days, price_per_unit, quantity):
        total_cost = rental_days * price_per_unit * quantity
        return total_cost


print("                                Welcome to the Car & Bus Rental Service                         ")
print("--------------------------------------------------------------------------------------------------")

available_cars = 200
car_rent_price = 25
available_buses = 100
bus_rent_price = 50
counter = 1

while counter <= 20:
    counter += 1
    
    while True:
        if counter == 25:
            break
        
        print("Select an option from the menu:")
        print("1: Rent a Car  2: Rent a Bus  3: Exit")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            car_rental = RentalTransaction("Indigo", "Car", available_cars, car_rent_price)
            car_rental.show_availability()
            quantity = int(input("Enter the number of cars you want to rent: "))       
            available_cars -= quantity
            rental_days = car_rental.get_rental_period()
            total_amount = car_rental.calculate_total(rental_days, car_rent_price, quantity)
            print(f"Your order for {quantity} Cars from indigo agency is confirmed. Total payment: Rs {total_amount}")
            print("----------------------------------------------------------------------")
            
        elif user_choice == 2:
            bus_rental = RentalTransaction("Royal", "Bus", available_buses, bus_rent_price)
            bus_rental.show_availability()
            quantity = int(input("Enter the number of buses you want to rent: "))
            available_buses -= quantity
            rental_days = bus_rental.get_rental_period()
            total_amount = bus_rental.calculate_total(rental_days, bus_rent_price, quantity)
            print(f"Your order for {quantity} Buses from Royal agency is confirmed. Total payment: Rs {total_amount}")
            print("----------------------------------------------------------------------")
            
        elif user_choice == 3:
            print("Thank you for visiting. Have a great day!")
            counter = 25
