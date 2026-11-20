number = int(input("Enter a number: "))

def show_table(number):
  for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")

show_table(number)

#The number is entered and the it can only multiply with the entered number until 10. It is displayed by printing the num and i with the product.
