class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        # Initializing the flight data
        self.flights.append(Flight("AI161E90", "BLR", "BOM", 5600))
        self.flights.append(Flight("BR161F91", "BOM", "BBI", 6750))
        self.flights.append(Flight("AI161F99", "BBI", "BLR", 8210))
        self.flights.append(Flight("VS171E20", "JLR", "BBI", 5500))
        self.flights.append(Flight("AS171G30", "HYD", "JLR", 4400))
        self.flights.append(Flight("AI131F49", "HYD", "BOM", 3499))
    
    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result
    
    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result
    
    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    while True:
        print("Choose a search parameter:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            city = input("Enter the city: ")
            results = flight_table.search_by_city(city)
        elif choice == 2:
            source = input("Enter the source city: ")
            results = flight_table.search_by_source(source)
        elif choice == 3:
            source = input("Enter the source city: ")
            destination = input("Enter the destination city: ")
            results = flight_table.search_between_cities(source, destination)
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if not results:
            print("No flights found.")
        else:
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in results:
                print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")

        another_search = input("Do you want to perform another search? (yes/no): ")
        if another_search.lower() != "yes":
            break

if __name__ == "__main__":
    main()
