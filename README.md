# Metro Ticketing System (Python)

## 📌 Overview
This is a simple Python program that simulates a metro ticket booking system.  
The user provides the starting station, destination, number of tickets, and payment method.  
The program then calculates the fare and generates a ticket confirmation.

## ⚙️ Features
- User-friendly input prompts.
- Input validation for:
  - Number of tickets (must be a positive integer).
  - Payment method (UPI, Card, or Cash).
  - Number of stations (must be a positive integer).
- Fare calculation based on:
  - Fixed fare per station (`fare_per_station`).
  - Number of tickets purchased.
- Ticket confirmation display with all entered details.

## 🖥️ Usage
1. Run the program:
   ```bash
   python metro_ticketing_system.py
   Enter details when prompted:

Starting station

Destination station

Number of tickets

Payment method (UPI, Card, or Cash)

Number of stations between start and destination

The program will display a ticket confirmation with the total fare.

💵 Fare Calculation
Total Fare = Number of Stations × Fare per Station × Number of Tickets


By default:

Fare per station = 10 (can be adjusted in the code).

📋 Example Run
Enter starting station: Ameerpet
Enter destination station: KPHB
Enter number of tickets: 2
Enter payment method (UPI, Card, Cash): UPI
Enter the number of stations between start and destination: 5

--- Metro Ticket Confirmation ---
Metro Route: Ameerpet to KPHB
Number of Stations: 5
Number of Tickets: 2
Total Fare: Rs. 100
Payment Mode: UPI
-------------------------------
