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
  
