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

