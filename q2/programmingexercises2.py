import time

input("Press Enter to start Programming Activity 1, Exercise 1: My School Bag: ")

school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print()
print(school_items[0])
time.sleep(1)
print(school_items[1])
time.sleep(1)
print(school_items[2])
time.sleep(1)
print(school_items[3])
time.sleep(1)
print(school_items[4])
print()
time.sleep(1) 

input("Press Enter to start Programming Activity 2, Exercise 2: Travel Destination Manager: ")

destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

time.sleep(1)
print()

for i in range (0,1):
  time.sleep(1)
  print(destinations[0:4])

print()

input("Enter a destination to search: ")

print()

time.sleep(1)

if destinations[0:4] in destinations:
  print("The destination you searched for is on the list!")
else:
  print("The destination you searched for is NOT on the list!")

destinations[2] = "Iloilo"

time.sleep(1)

print()

time.sleep(1)

print("Here is the updated list of destinations for today: ")

print()

print(destinations[0])
time.sleep(1)
print(destinations[1])
time.sleep(1)
print(destinations[2])
time.sleep(1)
print(destinations[3])

  

