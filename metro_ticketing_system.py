def metro_ticketing_system():
    # Fixed fare per station
    fare_per_station = 10  # Adjust as needed

    # User input
    start_station = input("Enter starting station: ").strip()
    destination = input("Enter destination station: ").strip()
    
    # Ensure the number of tickets is a valid integer
    while True:
        try:
            num_tickets = int(input("Enter number of tickets: "))
            if num_tickets > 0:
                break
            else:
                print("Please enter a valid positive number of tickets.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Ensure valid payment method
    valid_payment_methods = ["UPI", "Card", "Cash"]
    while True:
        payment_method = input("Enter payment method (UPI, Card, Cash): ").strip()
        if payment_method in valid_payment_methods:
            break
        print("Invalid payment method. Choose from UPI, Card, or Cash.")

    # Manual input for number of stations (replace with actual logic if needed)
    while True:
        try:
            num_stations = int(input("Enter the number of stations between start and destination: "))
            if num_stations > 0:
                break
            else:
                print("Number of stations must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate total fare
    total_fare = num_stations * fare_per_station * num_tickets

    
    print("\n--- Metro Ticket Confirmation ---")
    print(f"Metro Route: {start_station} to {destination}")
    print(f"Number of Stations: {num_stations}")
    print(f"Number of Tickets: {num_tickets}")
    print(f"Total Fare: Rs. {total_fare}")
    print(f"Payment Mode: {payment_method}")
    print("-------------------------------")

# Run the ticketing system
metro_ticketing_system()