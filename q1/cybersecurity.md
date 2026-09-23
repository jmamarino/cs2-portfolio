# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** [James Matthew A. Mariño]
**Section:** Dahlia
**Quarter:** 1

## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct, expected, and appropriate input.

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case
**Case Number:** Case 1
**Case Title:** Fake Login Alert
> A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

### 1. What cybersecurity threat is shown?
The threat shown is **Phishing** (specifically, account-deactivation scam / credential harvesting).

### 2. What warning signs make the situation suspicious?
- **Urgent or Threatening Language:** Claims the account will be immediately disabled.
- **Unsolicited Link:** Directs the user to click an external link to resolve the issue.
- **Request for Sensitive Credentials:** Requests the user's username and password.

### 3. What may be affected?
- [x] Data
- [x] Account
- [ ] Application
- [ ] Device
- [ ] Network
- [ ] Financial information

**Explanation:** The attacker aims to steal the user credentials. If successful, the student's account and all personal data stored within that account (e.g., grades, emails, personal information) will be compromised.

### 4. What information could be exposed or misused?
Usernames, passwords, personal student emails, academic records, and private communications within the school platform may be exposed or misused.

### 5. What should the user do to reduce the risk?
- Do **not** click any links or enter credentials.
- Verify the status of the account through official school administration or direct portal URL.
- Report the phishing message to the school IT department.

---

# Part B - Data Privacy and Secure Data Capture

| Data Field | Collect / Do Not Collect | Reason |
| :--- | :--- | :--- |
| **Student Name** | COLLECT | Necessary to identify who is registering. |
| **Section** | COLLECT | Necessary to organize students by class section. |
| **Club Choice** | COLLECT | Essential core data needed for club assignment. |
| **School Email** | COLLECT | Required for communication and membership verification. |
| **Attendance Status** | COLLECT | Necessary for recording student attendance during club sessions. |
| **Password** | DO NOT COLLECT | Unnecessary and unsafe; registering for a club does not require account creation. |
| **OTP** | DO NOT COLLECT | OTPs are for identity verification during login, not club forms. |
| **Home Address** | DO NOT COLLECT | Excessive personal data irrelevant to club registration. |
| **Parent Bank Account** | DO NOT COLLECT | Unnecessary financial data that creates extreme security risks. |

## Privacy Question
### Why is it safer to collect only information that the program actually needs?
Collecting only necessary data follows the principle of **Data Minimization**. If the database or system is ever breached or accesed, attackers cannot access sensitive information (such as financial or login details) because it was never collected in the first place.

---

# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Student Name** | Non-empty text | Blank input or bypass | `[blank]` | Must not be empty or whitespace | Student name is required. |
| **Section** | Valid PSHS section (e.g., Dahlia) | Unrecognized section | Rose | Must match allowed section list | Please select a valid section. |
| **Club Choice** | Allowed club name | Invalid or non-existent club | Gaming | Must match allowed list (Robotics, Science, Mathematics, Programming) | Please choose a valid club. |
| **School Email** | Valid email with `@` and `.` | Malformed email address | studentpshs.edu.ph | Must contain both `@` and `.` characters | Invalid email format. Email must contain '@' and '.'. |
| **Attendance Status** | Present, Absent, or Late | Invalid status string | Excused | Must be strictly 'Present', 'Absent', or 'Late' | Invalid attendance status. |

## Secure Data Capture Questions

### 1. What should your program accept?
Inputs that pass all strict validation checks: valid non-empty names, recognized sections, official club choices, properly formatted email addresses (`@` and `.`), and valid attendance statuses.

### 2. What should your program reject?
Blank fields, unrecognized sections or clubs, improperly formatted emails, and invalid attendance statuses.

### 3. How do your validation rules help reduce incorrect or unsafe input?
Validation rules ensure that the system only processes clean, structured data, preventing errors and blocking potential injection attacks or unexpected software crashes caused by invalid data.

---

# Part D - Secure Program Implementation

## Program
Create a simple **PSHS Club Registration System**.

## Source Code File
[`secure_registration.py`](secure_registration.py)

## Final Code
```python
# PSHS Secure Club Registration System

section = ["Dahlia"]
club = ["Robotics", "Science", "Mathematics", "Programming"]
attendance = ["Present", "Absent", "Late"]

def main():
    print("=== PSHS Secure Club Registration System ===")
    
    # 1. Student Name Validation
    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        print("Error: Student name is required.")
        return

    # 2. Section Validation
    section = input("Enter Section: ").strip()
    if section not in section:
        print("Error: Please enter a valid section.")
        return

    # 3. Club Choice Validation
    club_choice = input("Enter Club Choice: ").strip()
    if club_choice not in club:
        print("Error: Please choose a valid club.")
        return

    # 4. Email Validation
    email = input("Enter School Email: ").strip()
    if "@" not in email or "." not in email:
        print("Error: Invalid email format. Email must contain '@' and '.'.")
        return

    # 5. Attendance Status Validation
    attendance = input("Enter Attendance Status: ").strip()
    if attendance not in attendance:
        print("Error: Invalid attendance status. Must be Present, Absent, or Late.")
        return

    # Final Output upon Success
    print("\nREGISTRATION ACCEPTED")
    print(f"Student: {student_name}")
    print(f"Section: {section}")
    print(f"Club: {club_choice}")
    print(f"Email: {email}")
    print(f"Attendance: {attendance}")

if __name__ == "__main__":
    main()

