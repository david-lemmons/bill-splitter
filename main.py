def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

def calculate_total(bill_amount, tip_amount):
    return bill_amount + tip_amount

def calculate_amount_per_person(total_amount, people_count):
    return total_amount / people_count

while True:
    try:
        bill_amount = float(input("Enter the bill amount: "))
        if bill_amount <= 0:
            print("Bill amount must be greater than 0. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the bill amount.")

while True:
    try:
        tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        if tip_percentage < 0:
            print("Tip percentage cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the tip percentage.")

while True:
    try:
        people_count = int(input("Enter the number of people splitting the bill: "))
        if people_count <= 0:
            print("Number of people must be greater than 0. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number for the number of people.")
        


expected_tip = bill_amount * (tip_percentage / 100)
expected_total = bill_amount + expected_tip
amount_per_person = expected_total / people_count

print(f"Total bill amount (including tip): ${expected_total:.2f}")
print(f"Expected tip amount: ${expected_tip:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")