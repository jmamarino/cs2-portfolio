#PSHS Student Score Checker

#Ask the user to enter their score
student_score = int(input("Enter student score: "))

#Range: Check if score is outside the 0-100 boundary
if student_score < 0 or student_score > 100:
    print("This is an Invalid Score.")

#Determine the performance rating for valid scores
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
  
