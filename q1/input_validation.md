# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator  
**Name:** [Your Name]  
**Section:** [Your Section]  
**Quarter:** 1  

---

## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration system. The program checks whether user input satisfies specific requirements before accepting the registration. 

The program validates:
- Student name
- Age
- Grade level
- Email address
- Registration code

---

# Part A - Validation Requirements

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Non-empty text | Presence | `""` (empty) | Name must not be blank | Student name is required. |
| Age | Integer (11 to 18) | Data Type & Range | `fourteen` / `25` | Must be an integer from 11 to 18 | Age must be a number. / Age must be from 11 to 18. |
| Grade Level | 7, 8, 9, 10, 11, or 12 | Acceptable Value | `13` | Must be one of: 7, 8, 9, 10, 11, 12 | Invalid grade level. |
| Email Address | String with `@` and `.` | Simple Pattern | `studentpshs.edu.ph` | Must contain both `@` and `.` characters | Email must contain '@' and '.'. |
| Registration Code | String of 6 characters | Length | `A123` | Length must be exactly 6 characters | The registration code must contain exactly 6 characters. |

---

## Validation Questions

### 1. Why should the student name not be blank?
> A blank name prevents the system from identifying who is registering, leading to incomplete or anonymous records in the database.

### 2. Why should age be checked for both data type and range?
> Data type validation prevents program crashes when doing calculations or numeric comparisons (e.g., entering text instead of numbers), while range validation ensures the student meets the specific age eligibility criteria (11–18 years old) for the workshop.

### 3. Why should grade level only accept specific values?
> PSHS high school grade levels only run from Grade 7 to 12. Restricting acceptable values prevents impossible inputs (e.g., Grade 13 or Grade -1) from corrupting student records.

### 4. What format requirements did you use for the email address?
> The email must contain both an `@` symbol and a period (`.`).

### 5. What length requirement did you use for the registration code?
> The registration code must contain exactly 6 characters.

---

# Part B - Program Design

## Pseudocode

```text
START
    PRINT "Enter student name:"
    READ name
    IF name is empty THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: Student name is required."
        EXIT
    ENDIF

    PRINT "Enter age:"
    READ age_input
    TRY
        CONVERT age_input TO integer age
    CATCH
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: Age must be a number."
        EXIT
    ENDTRY

    IF age < 11 OR age > 18 THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: Age must be from 11 to 18."
        EXIT
    ENDIF

    PRINT "Enter grade level:"
    READ grade
    IF grade NOT IN ["7", "8", "9", "10", "11", "12"] THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: Invalid grade level."
        EXIT
    ENDIF

    PRINT "Enter email:"
    READ email
    IF "@" NOT IN email OR "." NOT IN email THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: Email must contain '@' and '.'."
        EXIT
    ENDIF

    PRINT "Enter registration code:"
    READ reg_code
    IF LENGTH(reg_code) != 6 THEN
        PRINT "REGISTRATION NOT ACCEPTED"
        PRINT "Reason: The registration code must contain exactly 6 characters."
        EXIT
    ENDIF

    PRINT "------------------------------"
    PRINT "REGISTRATION ACCEPTED"
    PRINT "------------------------------"
    PRINT "Student: " + name
    PRINT "Age: " + age
    PRINT "Grade Level: " + grade
    PRINT "Email: " + email
    PRINT "Registration Code: " + reg_code
END
```
---

# Part C - Program Implementation
## Programming Language
> Write the programming language used.
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
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
  print("REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered. 
```
---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Used on the Student Name input to check if the string is empty (name == "").
### Data Type Validation
Explain where you used data type validation.
> Used on the Age and Grade Level inputs by putting the input string to an integer using int().
### Range Validation
Explain where you used range validation.
> Used on the Age input (age < 11 or age > 18) to ensure that the age is between 11 and 18.

---

# Part D - Testing

Test your program using both valid and invalid inputs.

| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name | Presence | Your input of name is blank. <br> REGISTRATION NOT ACCEPTED. | Your input of name is blank. <br> REGISTRATION NOT ACCEPTED. | PASS |
| 3 | Age = `fourteen` | Data type | Program stops / ValueError | Program stops / ValueError | PASS |
| 4 | Age = `11` | Minimum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 5 | Age = `18` | Maximum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 6 | Age = `10` | Range | Age must be from 11-18. <br> REGISTRATION NOT ACCEPTED. | Age must be from 11-18. <br> REGISTRATION NOT ACCEPTED. | PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid grade level. <br> REGISTRATION NOT ACCEPTED. | Invalid grade level. <br> REGISTRATION NOT ACCEPTED. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Invalid email. <br> REGISTRATION NOT ACCEPTED. | Invalid email. <br> REGISTRATION NOT ACCEPTED. | PASS |
| 9 | Registration Code = `ABC` | Length | REGISTRATION ACCEPTED (Length <= 6) | REGISTRATION ACCEPTED | PASS |
| 10 | Registration Code = `CS2026` | Valid length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |

---

# Part E - Output Verification

Choose any **three tests** from Part D.

## Verification Test 1
**Input:**
```text
Enter student name: Maria Santos
Enter your age (11-18 only): 14
Enter your grade level: 8
Enter your email (student@brc.pshs.edu.ph): maria@brc.pshs.edu.ph
Enter your regristation code: CS2026
```

## Expected Output
```text
----------------
REGISTRATION ACCEPTED
----------------
Student Maria Santos
Age: 14
Grade Level: 8
Email: maria@brc.pshs.edu.ph
Registraion Code: CS2026
```

---

## Actual Output
```text
----------------
REGISTRATION ACCEPTED
----------------
Student Maria Santos
Age: 14
Grade Level: 8
Email: maria@brc.pshs.edu.ph
Regisraion Code: CS2026
```
---

### Result: PASS
### Explanation: All provided inputs satisfied every condition check (name != "", 11 <= age <= 18, 7 <= gradelevel <= 12, @ present in email, and len(code) <= 6). As a result, valid remained True, displaying the accepted summary block.

## Verification Test 2
**Input:**
```text
Enter student name: Juan Dela Cruz
Enter your age (11-18 only): 20
Enter your grade level: 8
Enter your email (student@brc.pshs.edu.ph): juan@brc.pshs.edu.ph
Enter your registration code: CS2026
```

## Expected Output
```text
Age must be from 11-18.
REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered
```

---

## Actual Output
```text
Age must be from 11-18.
REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered
```
---

### Result: PASS
### Explanation: The age input 20 triggered the range check age > 18, which printed the error message and flipped the flag to valid = False, properly failing the registration.

## Verification Test 3
**Input:**
```text
Enter student name: Juan Dela Cruz
Enter your age (11-18 only): 15
Enter your grade level: 8
Enter your email (student@brc.pshs.edu.ph): juan@brc.pshs.edu.ph
Enter your registration code: EXCEED12345
```

## Expected Output
```text
Invalid registration code.
REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered
```

---

## Actual Output
```text
Invalid regristration code.
REGISTRATION NOT ACCEPTED. Check the comments above to see the clear reasons to see why you are not registered
```
---

### Result: PASS
### Explanation: The code string EXCEED12345 has a character length greater than 6, triggering len(code) > 6. This correctly flagged valid = False and rejected the registration.
  
# Reflection

### 1. Why should a program validate input before processing it?
> Validating input protects software from unexpected crashes, prevents invalid data from entering databases, and provides immediate, user-friendly feedback to correct errors.
### 2. What is the difference between input validation and output verification?
> Input validation happens during execution to verify that incoming data meets required rules, whereas output verification happens after execution to confirm that actual outputs match expected test outcomes.
### 3. Which validation technique was easiest for you to implement? Why?
> Presence validation (name == "") was the easiest to implement because it only requires a straightforward equality check against an empty string.
### 4. Which validation technique was most challenging? Why?
> Data type validation was the most challenging because casting inputs directly with int() can crash the program with a ValueError if non-numeric characters are entered, requiring structured error handling to prevent.
### 5. How did testing invalid inputs help you improve your program?
> Testing invalid inputs helped verify that every failed check successfully set the boolean control flag valid = False and displayed the corresponding error message as expected.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- [_`input_validation.md`_](input_validation.md)
- Note: There is no Flowchart in this markdown. I used pseudocode.
---
[← Back to Main Portfolio](../README.md)

  

