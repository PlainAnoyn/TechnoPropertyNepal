from tabulate import tabulate
from datetime import datetime

# Function to read land data from a text file
def read_land_data(file_name):
    with open(file_name, "r") as file:
        land_data = []
        for line in file:
            parts = line.strip().split(",")
            kitta_number, city_district, land_faced, area, price, availability = parts
            land_data.append({
                "kitta_number": kitta_number,
                "city_district": city_district,
                "land_faced": land_faced,
                "area": area,
                "price": price,
                "availability": availability
            })
        return land_data

# Function to display the menu options
def display_menu():
    print("Land Renting System")
    print("Options:")
    print("Press '1' To Rent a land")
    print("Press '2' To Return a land")
    print("Press 'Q' To Quit")

# Function to handle renting a land
def rent_land(land_data, customer_name, rent_duration):
    if not land_data:
        print("Land data is empty")
        return

    available_lands = [land for land in land_data if land["availability"] == "Available"]
    headers = ["Kitta Number", "City/District", "Land Faced", "Area (anna)", "Price (Rs.)"]
    land_list = [[land["kitta_number"], land["city_district"], land["land_faced"], land["area"], land["price"]] for land in available_lands]
    print(tabulate(land_list, headers=headers, tablefmt="grid"))

    while True:
        kitta_number = input("Enter the Kitta Number of the land you want to rent: ")
        selected_land = next((land for land in available_lands if land["kitta_number"] == kitta_number), None)
        if selected_land:
            selected_land["availability"] = "Not Available"
            rent_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_amount = int(selected_land["price"]) * rent_duration
            print_rent_bill(customer_name, f"Kitta Number: {selected_land['kitta_number']}, City/District: {selected_land['city_district']}, Land Faced: {selected_land['land_faced']}, Area: {selected_land['area']} anna", rent_date, rent_duration, total_amount)
            return
        else:
            print("Invalid Kitta Number")

# Function to print a rent bill
def print_rent_bill(customer_name, land_info, rent_date, rent_duration, total_amount):
  """Prints and saves a rent bill as a text file.

  Args:
      customer_name (str): Name of the customer renting the land.
      land_info (str): Information about the rented land.
      rent_date (str): Date on which the land is rented.
      rent_duration (int): Duration of the rent in months.
      total_amount (int): Total amount to be paid for the rent.
  """  

  with open(f"rent_bill_{customer_name}.txt", "w") as bill_file:
    # Write bill content to the file
    bill_file.write("Land Renting System - Rent Bill\n")
    bill_file.write(f"Customer Name: {customer_name}\n")
    bill_file.write(f"Land Information: {land_info}\n")
    bill_file.write(f"Rent Date: {rent_date}\n")
    bill_file.write(f"Rent Duration: {rent_duration} months\n")
    bill_file.write(f"Total Amount: Rs. {total_amount}\n")
    bill_file.write("Rent bill generated. Thank you for using the Land Renting System!\n")

  # Console message can be removed if not desired
  print(f"Rent bill saved for customer {customer_name}.")

# Similar modifications can be made to the print_return_bill function...

# Function to handle returning a land
def return_land(land_data, customer_name):
    rented_lands = [land for land in land_data if land["availability"] == "Not Available"]
    headers = ["Kitta Number", "City/District", "Land Faced", "Area (anna)", "Price (Rs.)"]
    land_list = [[land["kitta_number"], land["city_district"], land["land_faced"], land["area"], land["price"]] for land in rented_lands]
    print(tabulate(land_list, headers=headers, tablefmt="grid"))

    while True:
        kitta_number = input("Enter the Kitta Number of the land you want to return: ")
        selected_land = next((land for land in rented_lands if land["kitta_number"] == kitta_number), None)
        if selected_land:
            selected_land["availability"] = "Available"
            return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rent_duration = int(input("Enter the rent duration in months: "))
            total_amount = int(selected_land["price"]) * rent_duration
            print_return_bill(customer_name, f"Kitta Number: {selected_land['kitta_number']}, City/District: {selected_land['city_district']}, Land Faced: {selected_land['land_faced']}, Area: {selected_land['area']} anna", return_date, rent_duration, total_amount)
            return
        else:
            print("Invalid Kitta Number")

# Function to print a return bill
def print_rent_bill(customer_name, land_info, rent_date, rent_duration, total_amount):
  """Prints and saves a rent bill as a text file.

  Args:
      customer_name (str): Name of the customer renting the land.
      land_info (str): Information about the rented land.
      rent_date (str): Date on which the land is rented.
      rent_duration (int): Duration of the rent in months.
      total_amount (int): Total amount to be paid for the rent.
  """  

  with open(f"return_bill_{customer_name}.txt", "w") as bill_file:
    # Write bill content to the file
    bill_file.write("Land Returning System - Rent Bill\n")
    bill_file.write(f"Customer Name: {customer_name}\n")
    bill_file.write(f"Land Information: {land_info}\n")
    bill_file.write(f"Return Date: {rent_date}\n")
    bill_file.write(f"Return Duration: {rent_duration} months\n")
    bill_file.write(f"Total Amount: Rs. {total_amount}\n")
    bill_file.write("Return bill generated. Thank you for using the Land Renting System!\n")

  # Console message can be removed if not desired
  print(f"Return bill saved for customer {customer_name}.")

# Similar modifications can be made to the print_return_bill function...

# Main program function
def main():
    land_data = read_land_data("land_data.txt")
    print(land_data)

    display_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter your name: ")
            rent_duration = int(input("Enter the rent duration in months: "))
            rent_land(land_data, customer_name, rent_duration)
        elif choice == "2":
            customer_name = input("Enter your name: ")
            return_land(land_data, customer_name)
        elif choice.lower() == "q":
            print("Thank you for using the Land Renting System. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
