#Student Performance Evaluator

score1 = int(input("Enter your first score (Between 0-100): "))
score2 = int(input("Enter your second score (Between 0-100): "))
score3 = int(input("Enter your third score (Between 0-100): "))

completed_tasks = int(input("Enter your number of completed tasks(From 0 to 5): "))

def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3

def get_performance(average):
  if average >= 85:
    return("Mastery")
  if average >= 70:
    return("Developing")
  if average <= 70:
    return("Needs Review")

def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return(True)
  else: 
    return(False)
  
average = calculate_average(score1, score2, score3)

performance = get_performance(average)

eligible = is_eligible(average, completed_tasks)

print(f"Average:", average)
print(f"Performance:", performance)
print(f"Eligible for Challenge:", eligible)

#Documentation Questions: 1. The calculate_average() function returns a number, the get_performance() function returns a string, and the is_eligible() function returns a boolean. | 2. The numerical average is computed and returned by the function calculate_average() and passed as an argument to function get_performance(). | 3. When a student has a high average but has less than three tasks, they achieve high performance, but their eligibility for the challenge will be False. | 4. Using return is more appropriate because it sends the data back to the main program so the other functions can just reuse the values, rather than just printing the text on screen.  


  
