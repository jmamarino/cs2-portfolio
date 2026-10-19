"""
Documentation Questions & Answers:

1. What does each function do?

   - The function calculate_total(price, quantity) multiplies the item's price by the 
quantity purchased to compute and return the total cost.

   - The function calculate_change(payment, total) subtracts the total cost from the 
     amount paid by the customer to return either the change or the additional amount owed.

2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?

   - The parameters (price, quantity) are the variables defined in the function. Arguments are the actual values or variables passed into 
the function.
     
3. Where is the returned total stored, and how is it reused?

   - The returned total from calculate_total() is stored in a variable. It is then reused by passing it as an argument into the 
calculate_change() function. And also used to display the final output to 
the user.

4. Why is it useful to separate total calculation from change calculation?

Because separation makes the code modular, easier to read, debug, and reuse if other parts of the program need just the total or just the change.
"""

def calculate_total(price, quantity):
    """Calculates and returns the total purchase cost."""
    return price * quantity

def calculate_change(payment, total):
    """Calculates and returns the amount of change or shortage."""
    return payment - total

def main():
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    payment = float(input("Enter amount paid: "))

    total_cost = calculate_total(price, quantity)

    change_or_shortage = calculate_change(payment, total_cost)

    print(f"Total Cost: PHP {total_cost:.2f}")

    if change_or_shortage >= 0:
        print(f"Change: PHP {change_or_shortage:.2f}")
    else:
        print(f"Insufficient payment! Additional amount needed: PHP{abs(change_or_shortage):.2f}")

if __name__ == "__main__":
    main()
  
