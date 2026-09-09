name = str(input("Enter student name: "))

if name == "":
  print("Your input of name is blank.")
  valid = False

age = int(input("Enter your age (11-18 only): "))
  
if age < 11 or age > 18:
  print("Age must be from 11-18.")
  valid = False

gradelevel = int(input("Enter your grade level: "))

if gradelevel < 7 or gradelevel > 12:
  print("Invalid grade level.")
  valid = False

email = str(input("Enter your email (student@brc.pshs.edu.ph): "))

if "@" not in email:
  print("Invalid email.")
  valid = False
  
code = str(input("Enter your regristation code: "))

if len(code) > 6:
  print("Invalid regristration code.")
  valid = False

if valid:
  print("----------------")
  print("REGISTRATION ACCEPTED")
  print("----------------")
  print(f"Student {student}")
  print(f"Age: {age}")
  print(f"Grade Level: {gradelevel}")
  print(f"Email: {email}")
  print(f"Regisraion Code: {code}")
else:
  print("REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered. Thank you.")
