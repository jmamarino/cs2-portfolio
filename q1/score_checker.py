student_score = int(input("Enter student score: "))

if student_score < 0 or student_score > 100:
    print("This is an Invalid Score.")

elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
  
